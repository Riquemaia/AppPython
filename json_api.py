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