from logging import LogRecord, addLevelName, Handler, Logger, Formatter, DEBUG, StreamHandler
from json import dumps
import sys
import concurrent.futures
import urllib.parse
import urllib.request

OK = 25
addLevelName(OK, "OK")

class DataDogHandler(Handler):
    def __init__(self, datadog_api_key, datadog_url):
        super().__init__()
        self.datadog_api_key = datadog_api_key
        self.datadog_url = datadog_url
        self.process_pool = concurrent.futures.ProcessPoolExecutor(max_workers=1)

    def __del__(self):
        self.process_pool.shutdown(wait=True)

    def emit(self, record):
        formatted_msg = self.format(record)
        self.process_pool.submit(self.send_to_datadog, (formatted_msg, self.datadog_api_key, self.datadog_url))

    @staticmethod
    def send_to_datadog(args: tuple):
        msg, datadog_api_key, datadog_url = args
        headers = {"DD-API-KEY": datadog_api_key, "Content-Type": "application/json"}
        data = msg.encode("utf-8")
        print(f'send_to_datadog = {data}')
        req = urllib.request.Request(datadog_url, data, headers, method='POST')
        with urllib.request.urlopen(req) as resp:
            status_code = resp.getcode()
            body = resp.read().decode('utf-8')
            print(f"Status code: {status_code}, Mensagem: {body}\n")

# Classe personalizada para formatação de logs em JSON
class JsonFormatter(Formatter):
    def format(self, record: LogRecord) -> str:
        # Log padrão
        log_record = {
            "acronym": getattr(record, 'acronym', None),
            "aws_account_id": getattr(record, 'aws_account_id', None),
            "env": getattr(record, 'env', None),
            "host": getattr(record, 'host', None),
            "service": getattr(record, 'service', None),
            "level": record.levelname,
            "line": record.lineno,
            "message": record.getMessage(),
        }

        # Adiciona os atributos extras que você definir
        if hasattr(record, 'database'):
            log_record['database'] = record.database
        if hasattr(record, 'tabela'):
            log_record['tabela'] = record.tabela
        if hasattr(record, 'problema'):
            log_record['problema'] = record.problema

        return dumps(log_record)

class EtlLogger(Logger):
    def __init__(self,
                 dir_path='default',
                 acronym='inquality',
                 aws_account_id='xxxxx',
                 env='dev',
                 host='emr',
                 project_name='teste',
                 datadog_api_key='xxxxx',
                 datadog_url='xxxxx',
                 *args,
                 **kwargs,):
        
        # Atributos padrões para o logger
        self.acronym = acronym
        self.aws_account_id = aws_account_id
        self.env = env
        self.host = host
        self.project_name = project_name
        self.datadog_api_key = datadog_api_key
        self.datadog_url = datadog_url

        # Inicializa o logger
        Logger.__init__(self, name=project_name, *args, **kwargs)
        self.setLevel(DEBUG)

        # Configura formatadores e handlers
        self.formatter = JsonFormatter()
        self.addHandler(self.getConsoleHandler())
        self.addHandler(self.getDatadogHandler())

    def getConsoleHandler(self):
        console_handler = StreamHandler(sys.stdout)
        console_handler.setFormatter(self.formatter)
        return console_handler

    def getDatadogHandler(self):
        datadog_handler = DataDogHandler(self.datadog_api_key, self.datadog_url)
        datadog_handler.setFormatter(self.formatter)
        return datadog_handler

    def ok(self, msg, *args, **kwargs):
        if self.isEnabledFor(OK):
            self._log(OK, msg, args, **kwargs)

    # Método _log ajustado para passar atributos extras dinamicamente
    def _log(self, level, msg, args, exc_info=None, extra=None, stack_info=False):
        # Atualiza os extras com atributos padrão e novos atributos
        if extra is None:
            extra = {}
        extra.update({
            'acronym': self.acronym,
            'aws_account_id': self.aws_account_id,
            'env': self.env,
            'host': self.host,
            'service': self.project_name,
        })

        # Chama o método original do logger, passando os extras
        super()._log(level=level, msg=msg, args=args, exc_info=exc_info, extra=extra, stack_info=stack_info)
