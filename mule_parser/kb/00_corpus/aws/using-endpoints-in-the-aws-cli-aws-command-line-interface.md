# Using endpoints in the AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-endpoints.html](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-endpoints.html)

---

To connect programmatically to an AWS service, you use an endpoint. An *endpoint* is the URL of the entry point for an AWS web
        service. The AWS Command Line Interface (AWS CLI) automatically uses the default endpoint for each service in
        an AWS Region, but you can specify an alternate endpoint for your API requests.

###### Endpoint topics

## Set endpoint for a single command

        To override any endpoint settings or environment variables for a single command, use
            the [--endpoint-url](./cli-configure-options.html#cli-configure-options-endpoint-url)

`$``aws s3 ls --endpoint-url``http://localhost:4567`

## Set global endpoint for all AWS services

        To route requests for all services to a custom endpoint URL, use one of the following settings:

- 
                Environment variables: - 
                        [AWS_IGNORE_CONFIGURED_ENDPOINT_URLS](./cli-configure-envvars.html#envvars-list-AWS_IGNORE_CONFIGURED_URLS)`$``export AWS_IGNORE_CONFIGURED_ENDPOINT_URLS=``true`
- 
                        [AWS_ENDPOINT_URL](./cli-configure-envvars.html#envvars-list-AWS_ENDPOINT_URL)`$``export AWS_ENDPOINT_URL=``http://localhost:4567`
 
- 
                        
- 
                The `config`file:- 
                        [ignore_configure_endpoint_urls](./cli-configure-files.html#cli-config-ignore_configure_endpoint_urls)`ignore_configure_endpoint_urls = true`
- 
                        [endpoint_url](./cli-configure-files.html#cli-config-endpoint_url)`endpoint_url =``http://localhost:4567`
 
- 
                        

Service-specific endpoints and the `--endpoint-url` command line option
            override any global endpoints.

## Set to use FIPs endpoints for all AWS services

        To route requests for all services to use FIPs endpoints, use one of the following:

- 
                [AWS_USE_FIPS_ENDPOINT](./cli-configure-envvars.html#envvars-list-AWS_USE_FIPS_ENDPOINT)`$``export AWS_USE_FIPS_ENDPOINT=``true`
- 
                [use_fips_endpoint](./cli-configure-files.html#cli-config-use_fips_endpoint)`use_fips_endpoint = true`

Some AWS services offer endpoints that support [Federal Information Processing Standard
                (FIPS) 140-2](http://aws.amazon.com/compliance/fips/) in some AWS Regions. When the AWS service supports FIPS,
            this setting specifies what FIPS endpoint the AWS CLI should use . Unlike standard AWS
            endpoints, FIPS endpoints use a TLS software library that complies with FIPS 140-2.
            These endpoints might be required by enterprises that interact with the United States
            government. 

If this setting is enabled, but a FIPS endpoint does not exist for the service in your
            AWS Region, the AWS command may fail. In this case, manually specify the endpoint to
            use in the command using the [--endpoint-url](./cli-configure-options.html#cli-configure-options-endpoint-url)[service-specific endpoints](#endpoints-service-specific).

For more information on specifying FIPS endpoints by AWS Region, see [FIPS Endpoints by
            Service](https://aws.amazon.com/compliance/fips/).

## Set to use dual-stack endpoints for all AWS services

        To route requests for all services to use dual-stack endpoints when available, use one of the following settings:

- 
                [AWS_USE_DUALSTACK_ENDPOINT](./cli-configure-envvars.html#envvars-list-AWS_USE_DUALSTACK_ENDPOINT)`$``export AWS_USE_DUALSTACK_ENDPOINT=``true`
- 
                [use_dualstack_endpoint](./cli-configure-files.html#cli-config-use_dualstack_endpoint)`use_dualstack_endpoint = true`

Enables the use of dual-stack endpoints to send AWS requests. To learn more about
            dual-stack endpoints, which support both IPv4 and IPv6 traffic, see [Using Amazon S3 dual-stack endpoints](https://docs.aws.amazon.com/AmazonS3/latest/userguide/dual-stack-endpoints.html) in the *Amazon Simple Storage Service
                User Guide*. Dual-stack endpoints are available for some services in some
            regions. If a dual-stack endpoint does not exist for the service or AWS Region, the
            request fails. This is disabled by default.

## Set service-specific endpoints

        Service-specific endpoint configuration provides the option to use a persistent endpoint of your choosing for AWS CLI requests. These settings provide flexibility to support local endpoints, VPC endpoints, and third-party local AWS development environments. Different endpoints can be used for testing and production environments. You can specify an endpoint URL for individual AWS services.

Service-specific endpoints can be specified in the following ways:

- 
                The command line option [--endpoint-url](./cli-configure-options.html#cli-configure-options-endpoint-url)
- 
                Environment variables: - 
                        [AWS_IGNORE_CONFIGURED_ENDPOINT_URLS](./cli-configure-envvars.html#envvars-list-AWS_IGNORE_CONFIGURED_URLS)
- 
                        [AWS_ENDPOINT_URL_<SERVICE>](./cli-configure-envvars.html#envvars-list-AWS_ENDPOINT_URL_SERVICE)`<SERVICE>`is replace with the AWS service identifier. For all service-specific variables, see[Service-specific endpoints: List of service-specific identifiers](#endpoints-service-specific-table).
 
- 
                        
- 
                `config`file:- 
                        [ignore_configure_endpoint_urls](./cli-configure-files.html#cli-config-ignore_configure_endpoint_urls)
- 
                        The [services](./cli-configure-files.html#cli-configure-files-format-services)section of the`config`file combined with the[endpoint_url](./cli-configure-files.html#cli-config-endpoint_url)
 
- 
                        

###### Service-specific endpoints topics:

### Service-specific endpoints: Environment variables

Environment variables override settings in your config file, but do not override options specified on the command line. Use environment variables if you want all profiles to use the same endpoints on your device.

The following are service-specific environment variables:

- 
                    [AWS_IGNORE_CONFIGURED_ENDPOINT_URLS](./cli-configure-envvars.html#envvars-list-AWS_IGNORE_CONFIGURED_URLS)`$``export AWS_IGNORE_CONFIGURED_ENDPOINT_URLS=``true`
- 
                    [AWS_ENDPOINT_URL_<SERVICE>](./cli-configure-envvars.html#envvars-list-AWS_ENDPOINT_URL_SERVICE)`<SERVICE>`is replaced with the AWS service identifier. For all service-specific variables, see[Service-specific endpoints: List of service-specific identifiers](#endpoints-service-specific-table).The following environment variable examples sets an endpoint for AWS Elastic Beanstalk: `$``export AWS_ENDPOINT_URL_ELASTIC_BEANSTALK=``http://localhost:4567`

For more information on setting environment variables, see [Configuring environment variables for the AWS CLI](./cli-configure-envvars.html).

### Service-specific endpoints: Shared `config` file

            In the shared `config` file, `endpoint_url` is used in multiple sections. To
                set a service-specific endpoint, use the `endpoint_url` setting nested
                under a service identifier key within a `services` section. For details
                on defining a `services` section in your shared `config` file, see [Section type: services](./cli-configure-files.html#cli-configure-files-format-services). 

The following example uses a `services` section to configure a
                service-specific endpoint URL for Amazon S3 and a custom global endpoint used for all
                other services: 

`[profile``dev1`] endpoint_url =`http://localhost:1234`services =`s3-specific`[services`testing-s3`] s3 = endpoint_url =`http://localhost:4567`

A single profile can configure endpoints for multiple services. The following example sets the service-specific endpoint URLs for Amazon S3 and AWS Elastic Beanstalk in the same profile.

For a list of all service identifier keys to use in the `services`
                section, see [List of
                    service-specific identifiers](#endpoints-service-specific-table). 

`[profile``dev1`] services =`testing-s3-and-eb`[services`testing-s3-and-eb`] s3 = endpoint_url =`http://localhost:4567`elastic_beanstalk = endpoint_url =`http://localhost:8000`

The service configuration section can be used in multiple profiles. The following
                example has two profiles use the same `services` definition: 

`[profile``dev1`] output = json services =`testing-s3`[profile`dev2`] output = text services =`testing-s3`[services`testing-s3`] s3 = endpoint_url =`https://localhost:4567`

### Service-specific endpoints: List of service-specific identifiers

The AWS service identifier is based on the API model’s `serviceId` by
                replacing all spaces with underscores and lowercasing all letters. 

The following table lists all service-specific identifiers,
                    `config` file keys, and environment variables.

| `serviceId` | Service identifier key for shared AWS `config`file | `AWS_ENDPOINT_URL_<SERVICE>`environment variable | 
|---|---|---|
| `AccessAnalyzer` | `accessanalyzer` | `AWS_ENDPOINT_URL_ACCESSANALYZER` | 
| `Account` | `account` | `AWS_ENDPOINT_URL_ACCOUNT` | 
| `ACM` | `acm` | `AWS_ENDPOINT_URL_ACM` | 
| `ACM PCA` | `acm_pca` | `AWS_ENDPOINT_URL_ACM_PCA` | 
| `Alexa For Business` | `alexa_for_business` | `AWS_ENDPOINT_URL_ALEXA_FOR_BUSINESS` | 
| `amp` | `amp` | `AWS_ENDPOINT_URL_AMP` | 
| `Amplify` | `amplify` | `AWS_ENDPOINT_URL_AMPLIFY` | 
| `AmplifyBackend` | `amplifybackend` | `AWS_ENDPOINT_URL_AMPLIFYBACKEND` | 
| `AmplifyUIBuilder` | `amplifyuibuilder` | `AWS_ENDPOINT_URL_AMPLIFYUIBUILDER` | 
| `API Gateway` | `api_gateway` | `AWS_ENDPOINT_URL_API_GATEWAY` | 
| `ApiGatewayManagementApi` | `apigatewaymanagementapi` | `AWS_ENDPOINT_URL_APIGATEWAYMANAGEMENTAPI` | 
| `ApiGatewayV2` | `apigatewayv2` | `AWS_ENDPOINT_URL_APIGATEWAYV2` | 
| `AppConfig` | `appconfig` | `AWS_ENDPOINT_URL_APPCONFIG` | 
| `AppConfigData` | `appconfigdata` | `AWS_ENDPOINT_URL_APPCONFIGDATA` | 
| `AppFabric` | `appfabric` | `AWS_ENDPOINT_URL_APPFABRIC` | 
| `Appflow` | `appflow` | `AWS_ENDPOINT_URL_APPFLOW` | 
| `AppIntegrations` | `appintegrations` | `AWS_ENDPOINT_URL_APPINTEGRATIONS` | 
| `Application Auto Scaling` | `application_auto_scaling` | `AWS_ENDPOINT_URL_APPLICATION_AUTO_SCALING` | 
| `Application Insights` | `application_insights` | `AWS_ENDPOINT_URL_APPLICATION_INSIGHTS` | 
| `ApplicationCostProfiler` | `applicationcostprofiler` | `AWS_ENDPOINT_URL_APPLICATIONCOSTPROFILER` | 
| `App Mesh` | `app_mesh` | `AWS_ENDPOINT_URL_APP_MESH` | 
| `AppRunner` | `apprunner` | `AWS_ENDPOINT_URL_APPRUNNER` | 
| `AppStream` | `appstream` | `AWS_ENDPOINT_URL_APPSTREAM` | 
| `AppSync` | `appsync` | `AWS_ENDPOINT_URL_APPSYNC` | 
| `ARC Zonal Shift` | `arc_zonal_shift` | `AWS_ENDPOINT_URL_ARC_ZONAL_SHIFT` | 
| `Artifact` | `artifact` | `AWS_ENDPOINT_URL_ARTIFACT` | 
| `Athena` | `athena` | `AWS_ENDPOINT_URL_ATHENA` | 
| `AuditManager` | `auditmanager` | `AWS_ENDPOINT_URL_AUDITMANAGER` | 
| `Auto Scaling` | `auto_scaling` | `AWS_ENDPOINT_URL_AUTO_SCALING` | 
| `Auto Scaling Plans` | `auto_scaling_plans` | `AWS_ENDPOINT_URL_AUTO_SCALING_PLANS` | 
| `b2bi` | `b2bi` | `AWS_ENDPOINT_URL_B2BI` | 
| `Backup` | `backup` | `AWS_ENDPOINT_URL_BACKUP` | 
| `Backup Gateway` | `backup_gateway` | `AWS_ENDPOINT_URL_BACKUP_GATEWAY` | 
| `BackupStorage` | `backupstorage` | `AWS_ENDPOINT_URL_BACKUPSTORAGE` | 
| `Batch` | `batch` | `AWS_ENDPOINT_URL_BATCH` | 
| `BCM Data Exports` | `bcm_data_exports` | `AWS_ENDPOINT_URL_BCM_DATA_EXPORTS` | 
| `Bedrock` | `bedrock` | `AWS_ENDPOINT_URL_BEDROCK` | 
| `Bedrock Agent` | `bedrock_agent` | `AWS_ENDPOINT_URL_BEDROCK_AGENT` | 
| `Bedrock Agent Runtime` | `bedrock_agent_runtime` | `AWS_ENDPOINT_URL_BEDROCK_AGENT_RUNTIME` | 
| `Bedrock Runtime` | `bedrock_runtime` | `AWS_ENDPOINT_URL_BEDROCK_RUNTIME` | 
| `billingconductor` | `billingconductor` | `AWS_ENDPOINT_URL_BILLINGCONDUCTOR` | 
| `Braket` | `braket` | `AWS_ENDPOINT_URL_BRAKET` | 
| `Budgets` | `budgets` | `AWS_ENDPOINT_URL_BUDGETS` | 
| `Cost Explorer` | `cost_explorer` | `AWS_ENDPOINT_URL_COST_EXPLORER` | 
| `chatbot` | `chatbot` | `AWS_ENDPOINT_URL_CHATBOT` | 
| `Chime` | `chime` | `AWS_ENDPOINT_URL_CHIME` | 
| `Chime SDK Identity` | `chime_sdk_identity` | `AWS_ENDPOINT_URL_CHIME_SDK_IDENTITY` | 
| `Chime SDK Media Pipelines` | `chime_sdk_media_pipelines` | `AWS_ENDPOINT_URL_CHIME_SDK_MEDIA_PIPELINES` | 
| `Chime SDK Meetings` | `chime_sdk_meetings` | `AWS_ENDPOINT_URL_CHIME_SDK_MEETINGS` | 
| `Chime SDK Messaging` | `chime_sdk_messaging` | `AWS_ENDPOINT_URL_CHIME_SDK_MESSAGING` | 
| `Chime SDK Voice` | `chime_sdk_voice` | `AWS_ENDPOINT_URL_CHIME_SDK_VOICE` | 
| `CleanRooms` | `cleanrooms` | `AWS_ENDPOINT_URL_CLEANROOMS` | 
| `CleanRoomsML` | `cleanroomsml` | `AWS_ENDPOINT_URL_CLEANROOMSML` | 
| `Cloud9` | `cloud9` | `AWS_ENDPOINT_URL_CLOUD9` | 
| `CloudControl` | `cloudcontrol` | `AWS_ENDPOINT_URL_CLOUDCONTROL` | 
| `CloudDirectory` | `clouddirectory` | `AWS_ENDPOINT_URL_CLOUDDIRECTORY` | 
| `CloudFormation` | `cloudformation` | `AWS_ENDPOINT_URL_CLOUDFORMATION` | 
| `CloudFront` | `cloudfront` | `AWS_ENDPOINT_URL_CLOUDFRONT` | 
| `CloudFront KeyValueStore` | `cloudfront_keyvaluestore` | `AWS_ENDPOINT_URL_CLOUDFRONT_KEYVALUESTORE` | 
| `CloudHSM` | `cloudhsm` | `AWS_ENDPOINT_URL_CLOUDHSM` | 
| `CloudHSM V2` | `cloudhsm_v2` | `AWS_ENDPOINT_URL_CLOUDHSM_V2` | 
| `CloudSearch` | `cloudsearch` | `AWS_ENDPOINT_URL_CLOUDSEARCH` | 
| `CloudSearch Domain` | `cloudsearch_domain` | `AWS_ENDPOINT_URL_CLOUDSEARCH_DOMAIN` | 
| `CloudTrail` | `cloudtrail` | `AWS_ENDPOINT_URL_CLOUDTRAIL` | 
| `CloudTrail Data` | `cloudtrail_data` | `AWS_ENDPOINT_URL_CLOUDTRAIL_DATA` | 
| `CloudWatch` | `cloudwatch` | `AWS_ENDPOINT_URL_CLOUDWATCH` | 
| `codeartifact` | `codeartifact` | `AWS_ENDPOINT_URL_CODEARTIFACT` | 
| `CodeBuild` | `codebuild` | `AWS_ENDPOINT_URL_CODEBUILD` | 
| `CodeCatalyst` | `codecatalyst` | `AWS_ENDPOINT_URL_CODECATALYST` | 
| `CodeCommit` | `codecommit` | `AWS_ENDPOINT_URL_CODECOMMIT` | 
| `CodeDeploy` | `codedeploy` | `AWS_ENDPOINT_URL_CODEDEPLOY` | 
| `CodeGuru Reviewer` | `codeguru_reviewer` | `AWS_ENDPOINT_URL_CODEGURU_REVIEWER` | 
| `CodeGuru Security` | `codeguru_security` | `AWS_ENDPOINT_URL_CODEGURU_SECURITY` | 
| `CodeGuruProfiler` | `codeguruprofiler` | `AWS_ENDPOINT_URL_CODEGURUPROFILER` | 
| `CodePipeline` | `codepipeline` | `AWS_ENDPOINT_URL_CODEPIPELINE` | 
| `CodeStar` | `codestar` | `AWS_ENDPOINT_URL_CODESTAR` | 
| `CodeStar connections` | `codestar_connections` | `AWS_ENDPOINT_URL_CODESTAR_CONNECTIONS` | 
| `codestar notifications` | `codestar_notifications` | `AWS_ENDPOINT_URL_CODESTAR_NOTIFICATIONS` | 
| `Cognito Identity` | `cognito_identity` | `AWS_ENDPOINT_URL_COGNITO_IDENTITY` | 
| `Cognito Identity Provider` | `cognito_identity_provider` | `AWS_ENDPOINT_URL_COGNITO_IDENTITY_PROVIDER` | 
| `Cognito Sync` | `cognito_sync` | `AWS_ENDPOINT_URL_COGNITO_SYNC` | 
| `Comprehend` | `comprehend` | `AWS_ENDPOINT_URL_COMPREHEND` | 
| `ComprehendMedical` | `comprehendmedical` | `AWS_ENDPOINT_URL_COMPREHENDMEDICAL` | 
| `Compute Optimizer` | `compute_optimizer` | `AWS_ENDPOINT_URL_COMPUTE_OPTIMIZER` | 
| `Config Service` | `config_service` | `AWS_ENDPOINT_URL_CONFIG_SERVICE` | 
| `Connect` | `connect` | `AWS_ENDPOINT_URL_CONNECT` | 
| `Connect Contact Lens` | `connect_contact_lens` | `AWS_ENDPOINT_URL_CONNECT_CONTACT_LENS` | 
| `ConnectCampaigns` | `connectcampaigns` | `AWS_ENDPOINT_URL_CONNECTCAMPAIGNS` | 
| `ConnectCases` | `connectcases` | `AWS_ENDPOINT_URL_CONNECTCASES` | 
| `ConnectParticipant` | `connectparticipant` | `AWS_ENDPOINT_URL_CONNECTPARTICIPANT` | 
| `ControlTower` | `controltower` | `AWS_ENDPOINT_URL_CONTROLTOWER` | 
| `Cost Optimization Hub` | `cost_optimization_hub` | `AWS_ENDPOINT_URL_COST_OPTIMIZATION_HUB` | 
| `Cost and Usage Report Service` | `cost_and_usage_report_service` | `AWS_ENDPOINT_URL_COST_AND_USAGE_REPORT_SERVICE` | 
| `Customer Profiles` | `customer_profiles` | `AWS_ENDPOINT_URL_CUSTOMER_PROFILES` | 
| `DataBrew` | `databrew` | `AWS_ENDPOINT_URL_DATABREW` | 
| `DataExchange` | `dataexchange` | `AWS_ENDPOINT_URL_DATAEXCHANGE` | 
| `Data Pipeline` | `data_pipeline` | `AWS_ENDPOINT_URL_DATA_PIPELINE` | 
| `DataSync` | `datasync` | `AWS_ENDPOINT_URL_DATASYNC` | 
| `DataZone` | `datazone` | `AWS_ENDPOINT_URL_DATAZONE` | 
| `DAX` | `dax` | `AWS_ENDPOINT_URL_DAX` | 
| `Detective` | `detective` | `AWS_ENDPOINT_URL_DETECTIVE` | 
| `Device Farm` | `device_farm` | `AWS_ENDPOINT_URL_DEVICE_FARM` | 
| `DevOps Guru` | `devops_guru` | `AWS_ENDPOINT_URL_DEVOPS_GURU` | 
| `Direct Connect` | `direct_connect` | `AWS_ENDPOINT_URL_DIRECT_CONNECT` | 
| `Application Discovery Service` | `application_discovery_service` | `AWS_ENDPOINT_URL_APPLICATION_DISCOVERY_SERVICE` | 
| `DLM` | `dlm` | `AWS_ENDPOINT_URL_DLM` | 
| `Database Migration Service` | `database_migration_service` | `AWS_ENDPOINT_URL_DATABASE_MIGRATION_SERVICE` | 
| `DocDB` | `docdb` | `AWS_ENDPOINT_URL_DOCDB` | 
| `DocDB Elastic` | `docdb_elastic` | `AWS_ENDPOINT_URL_DOCDB_ELASTIC` | 
| `drs` | `drs` | `AWS_ENDPOINT_URL_DRS` | 
| `Directory Service` | `directory_service` | `AWS_ENDPOINT_URL_DIRECTORY_SERVICE` | 
| `DynamoDB` | `dynamodb` | `AWS_ENDPOINT_URL_DYNAMODB` | 
| `DynamoDB Streams` | `dynamodb_streams` | `AWS_ENDPOINT_URL_DYNAMODB_STREAMS` | 
| `EBS` | `ebs` | `AWS_ENDPOINT_URL_EBS` | 
| `EC2` | `ec2` | `AWS_ENDPOINT_URL_EC2` | 
| `EC2 Instance Connect` | `ec2_instance_connect` | `AWS_ENDPOINT_URL_EC2_INSTANCE_CONNECT` | 
| `ECR` | `ecr` | `AWS_ENDPOINT_URL_ECR` | 
| `ECR PUBLIC` | `ecr_public` | `AWS_ENDPOINT_URL_ECR_PUBLIC` | 
| `ECS` | `ecs` | `AWS_ENDPOINT_URL_ECS` | 
| `EFS` | `efs` | `AWS_ENDPOINT_URL_EFS` | 
| `EKS` | `eks` | `AWS_ENDPOINT_URL_EKS` | 
| `EKS Auth` | `eks_auth` | `AWS_ENDPOINT_URL_EKS_AUTH` | 
| `Elastic Inference` | `elastic_inference` | `AWS_ENDPOINT_URL_ELASTIC_INFERENCE` | 
| `ElastiCache` | `elasticache` | `AWS_ENDPOINT_URL_ELASTICACHE` | 
| `Elastic Beanstalk` | `elastic_beanstalk` | `AWS_ENDPOINT_URL_ELASTIC_BEANSTALK` | 
| `Elastic Transcoder` | `elastic_transcoder` | `AWS_ENDPOINT_URL_ELASTIC_TRANSCODER` | 
| `Elastic Load Balancing` | `elastic_load_balancing` | `AWS_ENDPOINT_URL_ELASTIC_LOAD_BALANCING` | 
| `Elastic Load Balancing v2` | `elastic_load_balancing_v2` | `AWS_ENDPOINT_URL_ELASTIC_LOAD_BALANCING_V2` | 
| `EMR` | `emr` | `AWS_ENDPOINT_URL_EMR` | 
| `EMR containers` | `emr_containers` | `AWS_ENDPOINT_URL_EMR_CONTAINERS` | 
| `EMR Serverless` | `emr_serverless` | `AWS_ENDPOINT_URL_EMR_SERVERLESS` | 
| `EntityResolution` | `entityresolution` | `AWS_ENDPOINT_URL_ENTITYRESOLUTION` | 
| `Elasticsearch Service` | `elasticsearch_service` | `AWS_ENDPOINT_URL_ELASTICSEARCH_SERVICE` | 
| `EventBridge` | `eventbridge` | `AWS_ENDPOINT_URL_EVENTBRIDGE` | 
| `Evidently` | `evidently` | `AWS_ENDPOINT_URL_EVIDENTLY` | 
| `finspace` | `finspace` | `AWS_ENDPOINT_URL_FINSPACE` | 
| `finspace data` | `finspace_data` | `AWS_ENDPOINT_URL_FINSPACE_DATA` | 
| `Firehose` | `firehose` | `AWS_ENDPOINT_URL_FIREHOSE` | 
| `fis` | `fis` | `AWS_ENDPOINT_URL_FIS` | 
| `FMS` | `fms` | `AWS_ENDPOINT_URL_FMS` | 
| `forecast` | `forecast` | `AWS_ENDPOINT_URL_FORECAST` | 
| `forecastquery` | `forecastquery` | `AWS_ENDPOINT_URL_FORECASTQUERY` | 
| `FraudDetector` | `frauddetector` | `AWS_ENDPOINT_URL_FRAUDDETECTOR` | 
| `FreeTier` | `freetier` | `AWS_ENDPOINT_URL_FREETIER` | 
| `FSx` | `fsx` | `AWS_ENDPOINT_URL_FSX` | 
| `GameLift` | `gamelift` | `AWS_ENDPOINT_URL_GAMELIFT` | 
| `Glacier` | `glacier` | `AWS_ENDPOINT_URL_GLACIER` | 
| `Global Accelerator` | `global_accelerator` | `AWS_ENDPOINT_URL_GLOBAL_ACCELERATOR` | 
| `Glue` | `glue` | `AWS_ENDPOINT_URL_GLUE` | 
| `grafana` | `grafana` | `AWS_ENDPOINT_URL_GRAFANA` | 
| `Greengrass` | `greengrass` | `AWS_ENDPOINT_URL_GREENGRASS` | 
| `GreengrassV2` | `greengrassv2` | `AWS_ENDPOINT_URL_GREENGRASSV2` | 
| `GroundStation` | `groundstation` | `AWS_ENDPOINT_URL_GROUNDSTATION` | 
| `GuardDuty` | `guardduty` | `AWS_ENDPOINT_URL_GUARDDUTY` | 
| `Health` | `health` | `AWS_ENDPOINT_URL_HEALTH` | 
| `HealthLake` | `healthlake` | `AWS_ENDPOINT_URL_HEALTHLAKE` | 
| `Honeycode` | `honeycode` | `AWS_ENDPOINT_URL_HONEYCODE` | 
| `IAM` | `iam` | `AWS_ENDPOINT_URL_IAM` | 
| `identitystore` | `identitystore` | `AWS_ENDPOINT_URL_IDENTITYSTORE` | 
| `imagebuilder` | `imagebuilder` | `AWS_ENDPOINT_URL_IMAGEBUILDER` | 
| `ImportExport` | `importexport` | `AWS_ENDPOINT_URL_IMPORTEXPORT` | 
| `Inspector` | `inspector` | `AWS_ENDPOINT_URL_INSPECTOR` | 
| `Inspector Scan` | `inspector_scan` | `AWS_ENDPOINT_URL_INSPECTOR_SCAN` | 
| `Inspector2` | `inspector2` | `AWS_ENDPOINT_URL_INSPECTOR2` | 
| `InternetMonitor` | `internetmonitor` | `AWS_ENDPOINT_URL_INTERNETMONITOR` | 
| `IoT` | `iot` | `AWS_ENDPOINT_URL_IOT` | 
| `IoT Data Plane` | `iot_data_plane` | `AWS_ENDPOINT_URL_IOT_DATA_PLANE` | 
| `IoT Jobs Data Plane` | `iot_jobs_data_plane` | `AWS_ENDPOINT_URL_IOT_JOBS_DATA_PLANE` | 
| `IoT 1Click Devices Service` | `iot_1click_devices_service` | `AWS_ENDPOINT_URL_IOT_1CLICK_DEVICES_SERVICE` | 
| `IoT 1Click Projects` | `iot_1click_projects` | `AWS_ENDPOINT_URL_IOT_1CLICK_PROJECTS` | 
| `IoTAnalytics` | `iotanalytics` | `AWS_ENDPOINT_URL_IOTANALYTICS` | 
| `IotDeviceAdvisor` | `iotdeviceadvisor` | `AWS_ENDPOINT_URL_IOTDEVICEADVISOR` | 
| `IoT Events` | `iot_events` | `AWS_ENDPOINT_URL_IOT_EVENTS` | 
| `IoT Events Data` | `iot_events_data` | `AWS_ENDPOINT_URL_IOT_EVENTS_DATA` | 
| `IoTFleetHub` | `iotfleethub` | `AWS_ENDPOINT_URL_IOTFLEETHUB` | 
| `IoTFleetWise` | `iotfleetwise` | `AWS_ENDPOINT_URL_IOTFLEETWISE` | 
| `IoTSecureTunneling` | `iotsecuretunneling` | `AWS_ENDPOINT_URL_IOTSECURETUNNELING` | 
| `IoTSiteWise` | `iotsitewise` | `AWS_ENDPOINT_URL_IOTSITEWISE` | 
| `IoTThingsGraph` | `iotthingsgraph` | `AWS_ENDPOINT_URL_IOTTHINGSGRAPH` | 
| `IoTTwinMaker` | `iottwinmaker` | `AWS_ENDPOINT_URL_IOTTWINMAKER` | 
| `IoT Wireless` | `iot_wireless` | `AWS_ENDPOINT_URL_IOT_WIRELESS` | 
| `ivs` | `ivs` | `AWS_ENDPOINT_URL_IVS` | 
| `IVS RealTime` | `ivs_realtime` | `AWS_ENDPOINT_URL_IVS_REALTIME` | 
| `ivschat` | `ivschat` | `AWS_ENDPOINT_URL_IVSCHAT` | 
| `Kafka` | `kafka` | `AWS_ENDPOINT_URL_KAFKA` | 
| `KafkaConnect` | `kafkaconnect` | `AWS_ENDPOINT_URL_KAFKACONNECT` | 
| `kendra` | `kendra` | `AWS_ENDPOINT_URL_KENDRA` | 
| `Kendra Ranking` | `kendra_ranking` | `AWS_ENDPOINT_URL_KENDRA_RANKING` | 
| `Keyspaces` | `keyspaces` | `AWS_ENDPOINT_URL_KEYSPACES` | 
| `Kinesis` | `kinesis` | `AWS_ENDPOINT_URL_KINESIS` | 
| `Kinesis Video Archived Media` | `kinesis_video_archived_media` | `AWS_ENDPOINT_URL_KINESIS_VIDEO_ARCHIVED_MEDIA` | 
| `Kinesis Video Media` | `kinesis_video_media` | `AWS_ENDPOINT_URL_KINESIS_VIDEO_MEDIA` | 
| `Kinesis Video Signaling` | `kinesis_video_signaling` | `AWS_ENDPOINT_URL_KINESIS_VIDEO_SIGNALING` | 
| `Kinesis Video WebRTC Storage` | `kinesis_video_webrtc_storage` | `AWS_ENDPOINT_URL_KINESIS_VIDEO_WEBRTC_STORAGE` | 
| `Kinesis Analytics` | `kinesis_analytics` | `AWS_ENDPOINT_URL_KINESIS_ANALYTICS` | 
| `Kinesis Analytics V2` | `kinesis_analytics_v2` | `AWS_ENDPOINT_URL_KINESIS_ANALYTICS_V2` | 
| `Kinesis Video` | `kinesis_video` | `AWS_ENDPOINT_URL_KINESIS_VIDEO` | 
| `KMS` | `kms` | `AWS_ENDPOINT_URL_KMS` | 
| `LakeFormation` | `lakeformation` | `AWS_ENDPOINT_URL_LAKEFORMATION` | 
| `Lambda` | `lambda` | `AWS_ENDPOINT_URL_LAMBDA` | 
| `Launch Wizard` | `launch_wizard` | `AWS_ENDPOINT_URL_LAUNCH_WIZARD` | 
| `Lex Model Building Service` | `lex_model_building_service` | `AWS_ENDPOINT_URL_LEX_MODEL_BUILDING_SERVICE` | 
| `Lex Runtime Service` | `lex_runtime_service` | `AWS_ENDPOINT_URL_LEX_RUNTIME_SERVICE` | 
| `Lex Models V2` | `lex_models_v2` | `AWS_ENDPOINT_URL_LEX_MODELS_V2` | 
| `Lex Runtime V2` | `lex_runtime_v2` | `AWS_ENDPOINT_URL_LEX_RUNTIME_V2` | 
| `License Manager` | `license_manager` | `AWS_ENDPOINT_URL_LICENSE_MANAGER` | 
| `License Manager Linux Subscriptions` | `license_manager_linux_subscriptions` | `AWS_ENDPOINT_URL_LICENSE_MANAGER_LINUX_SUBSCRIPTIONS` | 
| `License Manager User Subscriptions` | `license_manager_user_subscriptions` | `AWS_ENDPOINT_URL_LICENSE_MANAGER_USER_SUBSCRIPTIONS` | 
| `Lightsail` | `lightsail` | `AWS_ENDPOINT_URL_LIGHTSAIL` | 
| `Location` | `location` | `AWS_ENDPOINT_URL_LOCATION` | 
| `CloudWatch Logs` | `cloudwatch_logs` | `AWS_ENDPOINT_URL_CLOUDWATCH_LOGS` | 
| `LookoutEquipment` | `lookoutequipment` | `AWS_ENDPOINT_URL_LOOKOUTEQUIPMENT` | 
| `LookoutMetrics` | `lookoutmetrics` | `AWS_ENDPOINT_URL_LOOKOUTMETRICS` | 
| `LookoutVision` | `lookoutvision` | `AWS_ENDPOINT_URL_LOOKOUTVISION` | 
| `m2` | `m2` | `AWS_ENDPOINT_URL_M2` | 
| `Machine Learning` | `machine_learning` | `AWS_ENDPOINT_URL_MACHINE_LEARNING` | 
| `Macie2` | `macie2` | `AWS_ENDPOINT_URL_MACIE2` | 
| `ManagedBlockchain` | `managedblockchain` | `AWS_ENDPOINT_URL_MANAGEDBLOCKCHAIN` | 
| `ManagedBlockchain Query` | `managedblockchain_query` | `AWS_ENDPOINT_URL_MANAGEDBLOCKCHAIN_QUERY` | 
| `Marketplace Agreement` | `marketplace_agreement` | `AWS_ENDPOINT_URL_MARKETPLACE_AGREEMENT` | 
| `Marketplace Catalog` | `marketplace_catalog` | `AWS_ENDPOINT_URL_MARKETPLACE_CATALOG` | 
| `Marketplace Deployment` | `marketplace_deployment` | `AWS_ENDPOINT_URL_MARKETPLACE_DEPLOYMENT` | 
| `Marketplace Entitlement Service` | `marketplace_entitlement_service` | `AWS_ENDPOINT_URL_MARKETPLACE_ENTITLEMENT_SERVICE` | 
| `Marketplace Commerce Analytics` | `marketplace_commerce_analytics` | `AWS_ENDPOINT_URL_MARKETPLACE_COMMERCE_ANALYTICS` | 
| `MediaConnect` | `mediaconnect` | `AWS_ENDPOINT_URL_MEDIACONNECT` | 
| `MediaConvert` | `mediaconvert` | `AWS_ENDPOINT_URL_MEDIACONVERT` | 
| `MediaLive` | `medialive` | `AWS_ENDPOINT_URL_MEDIALIVE` | 
| `MediaPackage` | `mediapackage` | `AWS_ENDPOINT_URL_MEDIAPACKAGE` | 
| `MediaPackage Vod` | `mediapackage_vod` | `AWS_ENDPOINT_URL_MEDIAPACKAGE_VOD` | 
| `MediaPackageV2` | `mediapackagev2` | `AWS_ENDPOINT_URL_MEDIAPACKAGEV2` | 
| `MediaStore` | `mediastore` | `AWS_ENDPOINT_URL_MEDIASTORE` | 
| `MediaStore Data` | `mediastore_data` | `AWS_ENDPOINT_URL_MEDIASTORE_DATA` | 
| `MediaTailor` | `mediatailor` | `AWS_ENDPOINT_URL_MEDIATAILOR` | 
| `Medical Imaging` | `medical_imaging` | `AWS_ENDPOINT_URL_MEDICAL_IMAGING` | 
| `MemoryDB` | `memorydb` | `AWS_ENDPOINT_URL_MEMORYDB` | 
| `Marketplace Metering` | `marketplace_metering` | `AWS_ENDPOINT_URL_MARKETPLACE_METERING` | 
| `Migration Hub` | `migration_hub` | `AWS_ENDPOINT_URL_MIGRATION_HUB` | 
| `mgn` | `mgn` | `AWS_ENDPOINT_URL_MGN` | 
| `Migration Hub Refactor Spaces` | `migration_hub_refactor_spaces` | `AWS_ENDPOINT_URL_MIGRATION_HUB_REFACTOR_SPACES` | 
| `MigrationHub Config` | `migrationhub_config` | `AWS_ENDPOINT_URL_MIGRATIONHUB_CONFIG` | 
| `MigrationHubOrchestrator` | `migrationhuborchestrator` | `AWS_ENDPOINT_URL_MIGRATIONHUBORCHESTRATOR` | 
| `MigrationHubStrategy` | `migrationhubstrategy` | `AWS_ENDPOINT_URL_MIGRATIONHUBSTRATEGY` | 
| `Mobile` | `mobile` | `AWS_ENDPOINT_URL_MOBILE` | 
| `mq` | `mq` | `AWS_ENDPOINT_URL_MQ` | 
| `MTurk` | `mturk` | `AWS_ENDPOINT_URL_MTURK` | 
| `MWAA` | `mwaa` | `AWS_ENDPOINT_URL_MWAA` | 
| `Neptune` | `neptune` | `AWS_ENDPOINT_URL_NEPTUNE` | 
| `Neptune Graph` | `neptune_graph` | `AWS_ENDPOINT_URL_NEPTUNE_GRAPH` | 
| `neptunedata` | `neptunedata` | `AWS_ENDPOINT_URL_NEPTUNEDATA` | 
| `Network Firewall` | `network_firewall` | `AWS_ENDPOINT_URL_NETWORK_FIREWALL` | 
| `NetworkManager` | `networkmanager` | `AWS_ENDPOINT_URL_NETWORKMANAGER` | 
| `NetworkMonitor` | `networkmonitor` | `AWS_ENDPOINT_URL_NETWORKMONITOR` | 
| `nimble` | `nimble` | `AWS_ENDPOINT_URL_NIMBLE` | 
| `OAM` | `oam` | `AWS_ENDPOINT_URL_OAM` | 
| `Omics` | `omics` | `AWS_ENDPOINT_URL_OMICS` | 
| `OpenSearch` | `opensearch` | `AWS_ENDPOINT_URL_OPENSEARCH` | 
| `OpenSearchServerless` | `opensearchserverless` | `AWS_ENDPOINT_URL_OPENSEARCHSERVERLESS` | 
| `OpsWorks` | `opsworks` | `AWS_ENDPOINT_URL_OPSWORKS` | 
| `OpsWorksCM` | `opsworkscm` | `AWS_ENDPOINT_URL_OPSWORKSCM` | 
| `Organizations` | `organizations` | `AWS_ENDPOINT_URL_ORGANIZATIONS` | 
| `OSIS` | `osis` | `AWS_ENDPOINT_URL_OSIS` | 
| `Outposts` | `outposts` | `AWS_ENDPOINT_URL_OUTPOSTS` | 
| `p8data` | `p8data` | `AWS_ENDPOINT_URL_P8DATA` | 
| `p8data` | `p8data` | `AWS_ENDPOINT_URL_P8DATA` | 
| `Panorama` | `panorama` | `AWS_ENDPOINT_URL_PANORAMA` | 
| `Payment Cryptography` | `payment_cryptography` | `AWS_ENDPOINT_URL_PAYMENT_CRYPTOGRAPHY` | 
| `Payment Cryptography Data` | `payment_cryptography_data` | `AWS_ENDPOINT_URL_PAYMENT_CRYPTOGRAPHY_DATA` | 
| `Pca Connector Ad` | `pca_connector_ad` | `AWS_ENDPOINT_URL_PCA_CONNECTOR_AD` | 
| `Personalize` | `personalize` | `AWS_ENDPOINT_URL_PERSONALIZE` | 
| `Personalize Events` | `personalize_events` | `AWS_ENDPOINT_URL_PERSONALIZE_EVENTS` | 
| `Personalize Runtime` | `personalize_runtime` | `AWS_ENDPOINT_URL_PERSONALIZE_RUNTIME` | 
| `PI` | `pi` | `AWS_ENDPOINT_URL_PI` | 
| `Pinpoint` | `pinpoint` | `AWS_ENDPOINT_URL_PINPOINT` | 
| `Pinpoint Email` | `pinpoint_email` | `AWS_ENDPOINT_URL_PINPOINT_EMAIL` | 
| `Pinpoint SMS Voice` | `pinpoint_sms_voice` | `AWS_ENDPOINT_URL_PINPOINT_SMS_VOICE` | 
| `Pinpoint SMS Voice V2` | `pinpoint_sms_voice_v2` | `AWS_ENDPOINT_URL_PINPOINT_SMS_VOICE_V2` | 
| `Pipes` | `pipes` | `AWS_ENDPOINT_URL_PIPES` | 
| `Polly` | `polly` | `AWS_ENDPOINT_URL_POLLY` | 
| `Pricing` | `pricing` | `AWS_ENDPOINT_URL_PRICING` | 
| `PrivateNetworks` | `privatenetworks` | `AWS_ENDPOINT_URL_PRIVATENETWORKS` | 
| `Proton` | `proton` | `AWS_ENDPOINT_URL_PROTON` | 
| `QBusiness` | `qbusiness` | `AWS_ENDPOINT_URL_QBUSINESS` | 
| `QConnect` | `qconnect` | `AWS_ENDPOINT_URL_QCONNECT` | 
| `QLDB` | `qldb` | `AWS_ENDPOINT_URL_QLDB` | 
| `QLDB Session` | `qldb_session` | `AWS_ENDPOINT_URL_QLDB_SESSION` | 
| `QuickSight` | `quicksight` | `AWS_ENDPOINT_URL_QUICKSIGHT` | 
| `RAM` | `ram` | `AWS_ENDPOINT_URL_RAM` | 
| `rbin` | `rbin` | `AWS_ENDPOINT_URL_RBIN` | 
| `RDS` | `rds` | `AWS_ENDPOINT_URL_RDS` | 
| `RDS Data` | `rds_data` | `AWS_ENDPOINT_URL_RDS_DATA` | 
| `Redshift` | `redshift` | `AWS_ENDPOINT_URL_REDSHIFT` | 
| `Redshift Data` | `redshift_data` | `AWS_ENDPOINT_URL_REDSHIFT_DATA` | 
| `Redshift Serverless` | `redshift_serverless` | `AWS_ENDPOINT_URL_REDSHIFT_SERVERLESS` | 
| `Rekognition` | `rekognition` | `AWS_ENDPOINT_URL_REKOGNITION` | 
| `repostspace` | `repostspace` | `AWS_ENDPOINT_URL_REPOSTSPACE` | 
| `resiliencehub` | `resiliencehub` | `AWS_ENDPOINT_URL_RESILIENCEHUB` | 
| `Resource Explorer 2` | `resource_explorer_2` | `AWS_ENDPOINT_URL_RESOURCE_EXPLORER_2` | 
| `Resource Groups` | `resource_groups` | `AWS_ENDPOINT_URL_RESOURCE_GROUPS` | 
| `Resource Groups Tagging API` | `resource_groups_tagging_api` | `AWS_ENDPOINT_URL_RESOURCE_GROUPS_TAGGING_API` | 
| `RoboMaker` | `robomaker` | `AWS_ENDPOINT_URL_ROBOMAKER` | 
| `RolesAnywhere` | `rolesanywhere` | `AWS_ENDPOINT_URL_ROLESANYWHERE` | 
| `Route 53` | `route_53` | `AWS_ENDPOINT_URL_ROUTE_53` | 
| `Route53 Recovery Cluster` | `route53_recovery_cluster` | `AWS_ENDPOINT_URL_ROUTE53_RECOVERY_CLUSTER` | 
| `Route53 Recovery Control Config` | `route53_recovery_control_config` | `AWS_ENDPOINT_URL_ROUTE53_RECOVERY_CONTROL_CONFIG` | 
| `Route53 Recovery Readiness` | `route53_recovery_readiness` | `AWS_ENDPOINT_URL_ROUTE53_RECOVERY_READINESS` | 
| `Route 53 Domains` | `route_53_domains` | `AWS_ENDPOINT_URL_ROUTE_53_DOMAINS` | 
| `Route53Resolver` | `route53resolver` | `AWS_ENDPOINT_URL_ROUTE53RESOLVER` | 
| `RUM` | `rum` | `AWS_ENDPOINT_URL_RUM` | 
| `S3` | `s3` | `AWS_ENDPOINT_URL_S3` | 
| `S3 Control` | `s3_control` | `AWS_ENDPOINT_URL_S3_CONTROL` | 
| `S3Outposts` | `s3outposts` | `AWS_ENDPOINT_URL_S3OUTPOSTS` | 
| `SageMaker` | `sagemaker` | `AWS_ENDPOINT_URL_SAGEMAKER` | 
| `SageMaker A2I Runtime` | `sagemaker_a2i_runtime` | `AWS_ENDPOINT_URL_SAGEMAKER_A2I_RUNTIME` | 
| `Sagemaker Edge` | `sagemaker_edge` | `AWS_ENDPOINT_URL_SAGEMAKER_EDGE` | 
| `SageMaker FeatureStore Runtime` | `sagemaker_featurestore_runtime` | `AWS_ENDPOINT_URL_SAGEMAKER_FEATURESTORE_RUNTIME` | 
| `SageMaker Geospatial` | `sagemaker_geospatial` | `AWS_ENDPOINT_URL_SAGEMAKER_GEOSPATIAL` | 
| `SageMaker Metrics` | `sagemaker_metrics` | `AWS_ENDPOINT_URL_SAGEMAKER_METRICS` | 
| `SageMaker Runtime` | `sagemaker_runtime` | `AWS_ENDPOINT_URL_SAGEMAKER_RUNTIME` | 
| `savingsplans` | `savingsplans` | `AWS_ENDPOINT_URL_SAVINGSPLANS` | 
| `Scheduler` | `scheduler` | `AWS_ENDPOINT_URL_SCHEDULER` | 
| `schemas` | `schemas` | `AWS_ENDPOINT_URL_SCHEMAS` | 
| `SimpleDB` | `simpledb` | `AWS_ENDPOINT_URL_SIMPLEDB` | 
| `Secrets Manager` | `secrets_manager` | `AWS_ENDPOINT_URL_SECRETS_MANAGER` | 
| `SecurityHub` | `securityhub` | `AWS_ENDPOINT_URL_SECURITYHUB` | 
| `SecurityLake` | `securitylake` | `AWS_ENDPOINT_URL_SECURITYLAKE` | 
| `ServerlessApplicationRepository` | `serverlessapplicationrepository` | `AWS_ENDPOINT_URL_SERVERLESSAPPLICATIONREPOSITORY` | 
| `Service Quotas` | `service_quotas` | `AWS_ENDPOINT_URL_SERVICE_QUOTAS` | 
| `Service Catalog` | `service_catalog` | `AWS_ENDPOINT_URL_SERVICE_CATALOG` | 
| `Service Catalog AppRegistry` | `service_catalog_appregistry` | `AWS_ENDPOINT_URL_SERVICE_CATALOG_APPREGISTRY` | 
| `ServiceDiscovery` | `servicediscovery` | `AWS_ENDPOINT_URL_SERVICEDISCOVERY` | 
| `SES` | `ses` | `AWS_ENDPOINT_URL_SES` | 
| `SESv2` | `sesv2` | `AWS_ENDPOINT_URL_SESV2` | 
| `Shield` | `shield` | `AWS_ENDPOINT_URL_SHIELD` | 
| `signer` | `signer` | `AWS_ENDPOINT_URL_SIGNER` | 
| `SimSpaceWeaver` | `simspaceweaver` | `AWS_ENDPOINT_URL_SIMSPACEWEAVER` | 
| `SMS` | `sms` | `AWS_ENDPOINT_URL_SMS` | 
| `Snow Device Management` | `snow_device_management` | `AWS_ENDPOINT_URL_SNOW_DEVICE_MANAGEMENT` | 
| `Snowball` | `snowball` | `AWS_ENDPOINT_URL_SNOWBALL` | 
| `SNS` | `sns` | `AWS_ENDPOINT_URL_SNS` | 
| `SQS` | `sqs` | `AWS_ENDPOINT_URL_SQS` | 
| `SSM` | `ssm` | `AWS_ENDPOINT_URL_SSM` | 
| `SSM Contacts` | `ssm_contacts` | `AWS_ENDPOINT_URL_SSM_CONTACTS` | 
| `SSM Incidents` | `ssm_incidents` | `AWS_ENDPOINT_URL_SSM_INCIDENTS` | 
| `Ssm Sap` | `ssm_sap` | `AWS_ENDPOINT_URL_SSM_SAP` | 
| `SSO` | `sso` | `AWS_ENDPOINT_URL_SSO` | 
| `SSO Admin` | `sso_admin` | `AWS_ENDPOINT_URL_SSO_ADMIN` | 
| `SSO OIDC` | `sso_oidc` | `AWS_ENDPOINT_URL_SSO_OIDC` | 
| `SFN` | `sfn` | `AWS_ENDPOINT_URL_SFN` | 
| `Storage Gateway` | `storage_gateway` | `AWS_ENDPOINT_URL_STORAGE_GATEWAY` | 
| `STS` | `sts` | `AWS_ENDPOINT_URL_STS` | 
| `SupplyChain` | `supplychain` | `AWS_ENDPOINT_URL_SUPPLYCHAIN` | 
| `Support` | `support` | `AWS_ENDPOINT_URL_SUPPORT` | 
| `Support App` | `support_app` | `AWS_ENDPOINT_URL_SUPPORT_APP` | 
| `SWF` | `swf` | `AWS_ENDPOINT_URL_SWF` | 
| `synthetics` | `synthetics` | `AWS_ENDPOINT_URL_SYNTHETICS` | 
| `Textract` | `textract` | `AWS_ENDPOINT_URL_TEXTRACT` | 
| `Timestream InfluxDB` | `timestream_influxdb` | `AWS_ENDPOINT_URL_TIMESTREAM_INFLUXDB` | 
| `Timestream Query` | `timestream_query` | `AWS_ENDPOINT_URL_TIMESTREAM_QUERY` | 
| `Timestream Write` | `timestream_write` | `AWS_ENDPOINT_URL_TIMESTREAM_WRITE` | 
| `tnb` | `tnb` | `AWS_ENDPOINT_URL_TNB` | 
| `Transcribe` | `transcribe` | `AWS_ENDPOINT_URL_TRANSCRIBE` | 
| `Transfer` | `transfer` | `AWS_ENDPOINT_URL_TRANSFER` | 
| `Translate` | `translate` | `AWS_ENDPOINT_URL_TRANSLATE` | 
| `TrustedAdvisor` | `trustedadvisor` | `AWS_ENDPOINT_URL_TRUSTEDADVISOR` | 
| `VerifiedPermissions` | `verifiedpermissions` | `AWS_ENDPOINT_URL_VERIFIEDPERMISSIONS` | 
| `Voice ID` | `voice_id` | `AWS_ENDPOINT_URL_VOICE_ID` | 
| `VPC Lattice` | `vpc_lattice` | `AWS_ENDPOINT_URL_VPC_LATTICE` | 
| `WAF` | `waf` | `AWS_ENDPOINT_URL_WAF` | 
| `WAF Regional` | `waf_regional` | `AWS_ENDPOINT_URL_WAF_REGIONAL` | 
| `WAFV2` | `wafv2` | `AWS_ENDPOINT_URL_WAFV2` | 
| `WellArchitected` | `wellarchitected` | `AWS_ENDPOINT_URL_WELLARCHITECTED` | 
| `Wisdom` | `wisdom` | `AWS_ENDPOINT_URL_WISDOM` | 
| `WorkDocs` | `workdocs` | `AWS_ENDPOINT_URL_WORKDOCS` | 
| `WorkLink` | `worklink` | `AWS_ENDPOINT_URL_WORKLINK` | 
| `WorkMail` | `workmail` | `AWS_ENDPOINT_URL_WORKMAIL` | 
| `WorkMailMessageFlow` | `workmailmessageflow` | `AWS_ENDPOINT_URL_WORKMAILMESSAGEFLOW` | 
| `WorkSpaces` | `workspaces` | `AWS_ENDPOINT_URL_WORKSPACES` | 
| `WorkSpaces Thin Client` | `workspaces_thin_client` | `AWS_ENDPOINT_URL_WORKSPACES_THIN_CLIENT` | 
| `WorkSpaces Web` | `workspaces_web` | `AWS_ENDPOINT_URL_WORKSPACES_WEB` | 
| `XRay` | `xray` | `AWS_ENDPOINT_URL_XRAY` | 

## Account-based endpoints

        Account-based endpoints can be specified in the following ways:

- 
                Environment variables - 
                        [AWS_ACCOUNT_ID](./cli-configure-envvars.html#envvars-list-AWS_ACCOUNT_ID)`$``export AWS_ACCOUNT_ID=``<account-id>`
- 
                        [AWS_ACCOUNT_ID_ENDPOINT_MODE](./cli-configure-envvars.html#envvars-list-AWS_ACCOUNT_ID_ENDPOINT_MODE)`preferred`,`disabled`, or`required`. Default value is`preferred`.`$``export AWS_ACCOUNT_ID_ENDPOINT_MODE=``preferred`
 
- 
                        
- 
                The `config`file:- 
                        [aws_account_id](./cli-configure-files.html#cli-config-aws_account_id)`aws_account_id =``<account-id>`
- 
                        [account_id_endpoint_mode](./cli-configure-files.html#cli-config-account_id_endpoint_mode)`preferred`,`disabled`, or`required`. Default value is preferred.`account_id_endpoint_mode =``preferred`
 
- 
                        

Account-based endpoints help ensure high performance and scalability by using your AWS account ID to streamline the routing of AWS service requests for services that support this feature. When you use a credential provider and a service that supports account-based endpoints, the AWS CLI automatically constructs and uses an account-based endpoint instead of a regional endpoint.

Account-based endpoints use the following format, where `<account-id>`
            is replaced with your AWS account ID and `<region>` is replaced with
            your AWS Region:

`https://``<account-id>`.myservice.`<region>`.amazonaws.com

By default in the AWS CLI, the account-based endpoint mode is set to
                `preferred`.

## Endpoint configuration and settings precedence

        Endpoint configuration settings are located in multiple places, such as the system or user environment variables, local AWS configuration files, or explicitly declared on the command line as a parameter. The AWS CLI endpoint configuration settings take precedence in the following order:

- 
                The [--endpoint-url](./cli-configure-options.html#cli-configure-options-endpoint-url)
- 
                If enabled, the [AWS_IGNORE_CONFIGURED_ENDPOINT_URLS](./cli-configure-envvars.html#envvars-list-AWS_IGNORE_CONFIGURED_URLS)[ignore_configure_endpoint_urls](./cli-configure-files.html#cli-config-ignore_configure_endpoint_urls)
- 
                The value provided by a service-specific environment variable [AWS_ENDPOINT_URL_<SERVICE>](./cli-configure-envvars.html#envvars-list-AWS_ENDPOINT_URL_SERVICE)`AWS_ENDPOINT_URL_DYNAMODB`.
- 
                The values provided by the [AWS_USE_DUALSTACK_ENDPOINT](./cli-configure-envvars.html#envvars-list-AWS_USE_DUALSTACK_ENDPOINT)[AWS_USE_FIPS_ENDPOINT](./cli-configure-envvars.html#envvars-list-AWS_USE_FIPS_ENDPOINT)[AWS_ENDPOINT_URL](./cli-configure-envvars.html#envvars-list-AWS_ENDPOINT_URL)
- 
                
                
                The [AWS_ACCOUNT_ID_ENDPOINT_MODE](./cli-configure-envvars.html#envvars-list-AWS_ACCOUNT_ID_ENDPOINT_MODE)`preferred`or`required`using the Account ID in the[AWS_ACCOUNT_ID](./cli-configure-envvars.html#envvars-list-AWS_ACCOUNT_ID)[aws_account_id](./cli-configure-files.html#cli-config-aws_account_id)
- 
                The service-specific endpoint value provided by the [endpoint_url](./cli-configure-files.html#cli-config-endpoint_url)`services`section of the shared`config`file.
- 
                The value provided by the [endpoint_url](./cli-configure-files.html#cli-config-endpoint_url)`profile`of the shared`config`file.
- 
                [use_dualstack_endpoint](./cli-configure-files.html#cli-config-use_dualstack_endpoint)[use_fips_endpoint](./cli-configure-files.html#cli-config-use_fips_endpoint)[endpoint_url](./cli-configure-files.html#cli-config-endpoint_url)
- 
                
                The [account_id_endpoint_mode](./cli-configure-files.html#cli-config-account_id_endpoint_mode)`preferred`or`required`using the Account ID in the[AWS_ACCOUNT_ID](./cli-configure-envvars.html#envvars-list-AWS_ACCOUNT_ID)[aws_account_id](./cli-configure-files.html#cli-config-aws_account_id)
- 
                Any default endpoint URL for the respective AWS service is used last. For a list of the standard service endpoints available in each Region, see [AWS Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html)in the*Amazon Web Services General Reference*.