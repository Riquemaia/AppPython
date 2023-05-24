schema_groups=ArrayType(StructType(
                [
                    StructField("id", StringType(), True),
                    StructField("isReadOnly", StringType(), True),
                    StructField("isOnDedicatedCapacity", StringType(), True),
                    StructField("capacityMigrationStatus", StringType(), True),
                    StructField("type", StringType(), True),
                    StructField("state", StringType(), True),
                    StructField("hasWorkspaceLevelSettings ", StringType(), True),
                    StructField("name", StringType(), True)
                ]
            ))

schema_reports=ArrayType(StructType(
                [
                    StructField("id", StringType(), True),
                    StructField("isReadOnly", StringType(), True),
                    StructField("isOnDedicatedCapacity", StringType(), True),
                    StructField("capacityMigrationStatus", StringType(), True),
                    StructField("type", StringType(), True),
                    StructField("state", StringType(), True),
                    StructField("hasWorkspaceLevelSettings ", StringType(), True),
                    StructField("name", StringType(), True),
                    StructField("dashboards", ArrayType(StructType([
                        StructField("id", StringType(), True),
                        StructField("displayName", StringType(), True),
                        StructField("isReadOnly", StringType(), True),
                        StructField("users", StringType(), True),
                        StructField("subscriptions", StringType(), True)
                    ])))
                ]
            ))

schema_datasets=ArrayType(StructType(
                [
                    StructField("id", StringType(), True),
                    StructField("isReadOnly", StringType(), True),
                    StructField("isOnDedicatedCapacity", StringType(), True),
                    StructField("capacityMigrationStatus", StringType(), True),
                    StructField("type", StringType(), True),
                    StructField("state", StringType(), True),
                    StructField("hasWorkspaceLevelSettings ", StringType(), True),
                    StructField("name", StringType(), True),
                    StructField("datasets", ArrayType(StructType([
                        StructField("id", StringType(), True),
                        StructField("name", StringType(), True),
                        StructField("addRowsAPIEnabled", StringType(), True),
                        StructField("isRefreshable", StringType(), True),
                        StructField("isEffectiveIdentityRequired", StringType(), True),
                        StructField("isEffectiveIdentityRolesRequired", StringType(), True),
                        StructField("targetStorageMode", StringType(), True),
                        StructField("createdDate", StringType(), True),
                        StructField("contentProviderType", StringType(), True),
                        StructField("upstreamDatasets", StringType(), True),
                        StructField("users", StringType(), True),
                        StructField("isInPlaceSharingEnabled", StringType(), True)
                    ])))
                ]
            ))

schema_users=StructType(
                [
                    StructField("id", StringType(), True),
                    StructField("isReadOnly", StringType(), True),
                    StructField("isOnDedicatedCapacity", StringType(), True),
                    StructField("capacityMigrationStatus", StringType(), True),
                    StructField("type", StringType(), True),
                    StructField("state", StringType(), True),
                    StructField("hasWorkspaceLevelSettings ", StringType(), True),
                    StructField("name", StringType(), True),
                    StructField("users", ArrayType(StructType([
                        StructField("emailAddress", StringType(), True),
                        StructField("groupUserAccessRight", StringType(), True),
                        StructField("displayName", StringType(), True),
                        StructField("identifier", StringType(), True),
                        StructField("principalType", StringType(), True)
                    ])))
                ]
            )

schema_activity= StructType(
                [
                    StructField('Id', StringType(), True),
                    StructField('RecordType', StringType(), True),
                    StructField('CreationTime', StringType(), True),
                    StructField('Operation', StringType(), True),
                    StructField('OrganizationId', StringType(), True),
                    StructField('UserType', StringType(), True),
                    StructField('UserKey', StringType(), True),
                    StructField('Workload', StringType(), True),
                    StructField('UserId', StringType(), True),
                    StructField('ClientIP', StringType(), True),
                    StructField('Activity', StringType(), True),
                    StructField('ItemName', StringType(), True),
                    StructField('WorkSpaceName', StringType(), True),
                    StructField('CapacityId', StringType(), True),
                    StructField('CapacityName', StringType(), True),
                    StructField('WorkspaceId', StringType(), True),
                    StructField('ObjectId', StringType(), True),
                    StructField('DataflowId', StringType(), True),
                    StructField('DataflowName', StringType(), True),
                    StructField('IsSuccess', StringType(), True),
                    StructField('DataflowRefreshScheduleType', StringType(), True),
                    StructField('DataflowType', StringType(), True),
                    StructField('RequestId', StringType(), True),
                    StructField('ActivityId', StringType(), True),
                    StructField('UserAgent', StringType(), True),
                    StructField('DataflowAccessTokenRequestParameters', StructType([
                        StructField("tokenLifetimeInMinutes", StringType(), True),
                        StructField('permissions', StringType(), True),
                        StructField('entityName', StringType(), True),
                        StructField('partitionUri', StringType(), True)
                        ])),
                    StructField('DatasetName', StringType(), True),
                    StructField('ReportName', StringType(), True),
                    StructField('AppName', StringType(), True),
                    StructField('DatasetId', StringType(), True),
                    StructField('ReportId', StringType(), True),
                    StructField('ArtifactId', StringType(), True),
                    StructField('ArtifactName', StringType(), True),
                    StructField('ReportType', StringType(), True),
                    StructField('AppReportId', StringType(), True),
                    StructField('DistributionMethod', StringType(), True),
                    StructField('ConsumptionMethod', StringType(), True),
                    StructField('AppId', StringType(), True),
                    StructField('ArtifactKind', StringType(), True),
                    StructField('EndPoint', StringType(), True),
                    StructField('DataConnectivityMode', StringType(), True),
                    StructField('RefreshType', StringType(), True),
                    StructField('LastRefreshTime', StringType(), True),
                    StructField('ModelsSnapshots', StringType(), True),
                ]
            )
