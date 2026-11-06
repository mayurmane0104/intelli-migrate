# Elastic Beanstalk examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_elastic-beanstalk_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_elastic-beanstalk_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Elastic Beanstalk.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `abort-environment-update`.

- **AWS CLI**
- 
            
                    **To abort a deployment**The following command aborts a running application version deployment for an environment named `my-env`:`aws elasticbeanstalk abort-environment-update --environment-name``my-env`- 
                    For API details, see [AbortEnvironmentUpdate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/abort-environment-update.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `check-dns-availability`.

- **AWS CLI**
- 
            
                    **To check the availability of a CNAME**The following command checks the availability of the subdomain `my-cname.elasticbeanstalk.com`:`aws elasticbeanstalk check-dns-availability --cname-prefix``my-cname`Output: `{ "Available": true, "FullyQualifiedCNAME": "my-cname.elasticbeanstalk.com" }`- 
                    For API details, see [CheckDnsAvailability](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/check-dns-availability.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-application-version`.

- **AWS CLI**
- 
            
                    **To create a new application version**The following command creates a new version, "v1" of an application named "MyApp": `aws elasticbeanstalk create-application-version --application-name``MyApp`--version-label`v1`--description`MyAppv1`--source-bundle S3Bucket="amzn-s3-demo-bucket",S3Key="sample.war" --auto-create-applicationThe application will be created automatically if it does not already exist, due to the auto-create-application option. The source bundle is a .war file stored in an s3 bucket named "amzn-s3-demo-bucket" that contains the Apache Tomcat sample application. Output: `{ "ApplicationVersion": { "ApplicationName": "MyApp", "VersionLabel": "v1", "Description": "MyAppv1", "DateCreated": "2015-02-03T23:01:25.412Z", "DateUpdated": "2015-02-03T23:01:25.412Z", "SourceBundle": { "S3Bucket": "amzn-s3-demo-bucket", "S3Key": "sample.war" } } }`- 
                    For API details, see [CreateApplicationVersion](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/create-application-version.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-application`.

- **AWS CLI**
- 
            
                    **To create a new application**The following command creates a new application named "MyApp": `aws elasticbeanstalk create-application --application-name``MyApp`--description`"my application"`The `create-application`command only configures the application's name and description. To upload source code for the application, create an initial version of the application using`create-application-version`.`create-application-version`also has an`auto-create-application`option that lets you create the application and the application version in one step.Output: `{ "Application": { "ApplicationName": "MyApp", "ConfigurationTemplates": [], "DateUpdated": "2015-02-12T18:32:21.181Z", "Description": "my application", "DateCreated": "2015-02-12T18:32:21.181Z" } }`- 
                    For API details, see [CreateApplication](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/create-application.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-configuration-template`.

- **AWS CLI**
- 
            
                    **To create a configuration template**The following command creates a configuration template named `my-app-v1`from the settings applied to an environment with the id`e-rpqsewtp2j`:`aws elasticbeanstalk create-configuration-template --application-name``my-app`--template-name`my-app-v1`--environment-id`e-rpqsewtp2j`Output: `{ "ApplicationName": "my-app", "TemplateName": "my-app-v1", "DateCreated": "2015-08-12T18:40:39Z", "DateUpdated": "2015-08-12T18:40:39Z", "SolutionStackName": "64bit Amazon Linux 2015.03 v2.0.0 running Tomcat 8 Java 8" }`- 
                    For API details, see [CreateConfigurationTemplate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/create-configuration-template.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-environment`.

- **AWS CLI**
- 
            
                    **To create a new environment for an application**The following command creates a new environment for version "v1" of a java application named "my-app": `aws elasticbeanstalk create-environment --application-name``my-app`--environment-name`my-env`--cname-prefix`my-app`--version-label`v1`--solution-stack-name`"64bit Amazon Linux 2015.03 v2.0.0 running Tomcat 8 Java 8"`Output: `{ "ApplicationName": "my-app", "EnvironmentName": "my-env", "VersionLabel": "v1", "Status": "Launching", "EnvironmentId": "e-izqpassy4h", "SolutionStackName": "64bit Amazon Linux 2015.03 v2.0.0 running Tomcat 8 Java 8", "CNAME": "my-app.elasticbeanstalk.com", "Health": "Grey", "Tier": { "Type": "Standard", "Name": "WebServer", "Version": " " }, "DateUpdated": "2015-02-03T23:04:54.479Z", "DateCreated": "2015-02-03T23:04:54.479Z" }``v1`is the label of an application version previously uploaded with create-application-version.**To specify a JSON file to define environment configuration options**The following `create-environment`command specifies that a JSON file with the name`myoptions.json`should be used to override values obtained from the solution stack or the configuration template:`aws elasticbeanstalk create-environment --environment-name``sample-env`--application-name`sampleapp`--option-settings`file://myoptions.json``myoptions.json`is a JSON object defining several settings:`[ { "Namespace": "aws:elb:healthcheck", "OptionName": "Interval", "Value": "15" }, { "Namespace": "aws:elb:healthcheck", "OptionName": "Timeout", "Value": "8" }, { "Namespace": "aws:elb:healthcheck", "OptionName": "HealthyThreshold", "Value": "2" }, { "Namespace": "aws:elb:healthcheck", "OptionName": "UnhealthyThreshold", "Value": "3" } ]`For more information, see Option Values in the *AWS Elastic Beanstalk Developer Guide*.- 
                    For API details, see [CreateEnvironment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/create-environment.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-storage-location`.

- **AWS CLI**
- 
            
                    **To create a storage location**The following command creates a storage location in Amazon S3: `aws elasticbeanstalk create-storage-location`Output: `{ "S3Bucket": "elasticbeanstalk-us-west-2-0123456789012" }`- 
                    For API details, see [CreateStorageLocation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/create-storage-location.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-application-version`.

- **AWS CLI**
- 
            
                    **To delete an application version**The following command deletes an application version named `22a0-stage-150819_182129`for an application named`my-app`:`aws elasticbeanstalk delete-application-version --version-label``22a0-stage-150819_182129`--application-name`my-app`- 
                    For API details, see [DeleteApplicationVersion](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/delete-application-version.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-application`.

- **AWS CLI**
- 
            
                    **To delete an application**The following command deletes an application named `my-app`:`aws elasticbeanstalk delete-application --application-name``my-app`- 
                    For API details, see [DeleteApplication](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/delete-application.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-configuration-template`.

- **AWS CLI**
- 
            
                    **To delete a configuration template**The following command deletes a configuration template named `my-template`for an application named`my-app`:`aws elasticbeanstalk delete-configuration-template --template-name``my-template`--application-name`my-app`- 
                    For API details, see [DeleteConfigurationTemplate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/delete-configuration-template.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-environment-configuration`.

- **AWS CLI**
- 
            
                    **To delete a draft configuration**The following command deletes a draft configuration for an environment named `my-env`:`aws elasticbeanstalk delete-environment-configuration --environment-name``my-env`--application-name`my-app`- 
                    For API details, see [DeleteEnvironmentConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/delete-environment-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-application-versions`.

- **AWS CLI**
- 
            
                    **To view information about an application version**The following command retrieves information about an application version labeled `v2`:`aws elasticbeanstalk describe-application-versions --application-name``my-app`--version-label`"v2"`Output: `{ "ApplicationVersions": [ { "ApplicationName": "my-app", "VersionLabel": "v2", "Description": "update cover page", "DateCreated": "2015-07-23T01:32:26.079Z", "DateUpdated": "2015-07-23T01:32:26.079Z", "SourceBundle": { "S3Bucket": "elasticbeanstalk-us-west-2-015321684451", "S3Key": "my-app/5026-stage-150723_224258.war" } }, { "ApplicationName": "my-app", "VersionLabel": "v1", "Description": "initial version", "DateCreated": "2015-07-23T22:26:10.816Z", "DateUpdated": "2015-07-23T22:26:10.816Z", "SourceBundle": { "S3Bucket": "elasticbeanstalk-us-west-2-015321684451", "S3Key": "my-app/5026-stage-150723_222618.war" } } ] }`- 
                    For API details, see [DescribeApplicationVersions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/describe-application-versions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-applications`.

- **AWS CLI**
- 
            
                    **To view a list of applications**The following command retrieves information about applications in the current region: `aws elasticbeanstalk describe-applications`Output: `{ "Applications": [ { "ApplicationName": "ruby", "ConfigurationTemplates": [], "DateUpdated": "2015-08-13T21:05:44.376Z", "Versions": [ "Sample Application" ], "DateCreated": "2015-08-13T21:05:44.376Z" }, { "ApplicationName": "pythonsample", "Description": "Application created from the EB CLI using \"eb init\"", "Versions": [ "Sample Application" ], "DateCreated": "2015-08-13T19:05:43.637Z", "ConfigurationTemplates": [], "DateUpdated": "2015-08-13T19:05:43.637Z" }, { "ApplicationName": "nodejs-example", "ConfigurationTemplates": [], "DateUpdated": "2015-08-06T17:50:02.486Z", "Versions": [ "add elasticache", "First Release" ], "DateCreated": "2015-08-06T17:50:02.486Z" } ] }`- 
                    For API details, see [DescribeApplications](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/describe-applications.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-configuration-options`.

- **AWS CLI**
- 
            
                    **To view configuration options for an environment**The following command retrieves descriptions of all available configuration options for an environment named `my-env`:`aws elasticbeanstalk describe-configuration-options --environment-name``my-env`--application-name`my-app`Output (abbreviated): `{ "Options": [ { "Name": "JVMOptions", "UserDefined": false, "DefaultValue": "Xms=256m,Xmx=256m,XX:MaxPermSize=64m,JVM Options=", "ChangeSeverity": "RestartApplicationServer", "Namespace": "aws:cloudformation:template:parameter", "ValueType": "KeyValueList" }, { "Name": "Interval", "UserDefined": false, "DefaultValue": "30", "ChangeSeverity": "NoInterruption", "Namespace": "aws:elb:healthcheck", "MaxValue": 300, "MinValue": 5, "ValueType": "Scalar" }, ... { "Name": "LowerThreshold", "UserDefined": false, "DefaultValue": "2000000", "ChangeSeverity": "NoInterruption", "Namespace": "aws:autoscaling:trigger", "MinValue": 0, "ValueType": "Scalar" }, { "Name": "ListenerEnabled", "UserDefined": false, "DefaultValue": "true", "ChangeSeverity": "Unknown", "Namespace": "aws:elb:listener", "ValueType": "Boolean" } ] }`Available configuration options vary per platform and configuration version. For more information about namespaces and supported options, see Option Values in the *AWS Elastic Beanstalk Developer Guide*.- 
                    For API details, see [DescribeConfigurationOptions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/describe-configuration-options.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-configuration-settings`.

- **AWS CLI**
- 
            
                    **To view configurations settings for an environment**The following command retrieves configuration settings for an environment named `my-env`:`aws elasticbeanstalk describe-configuration-settings --environment-name``my-env`--application-name`my-app`Output (abbreviated): `{ "ConfigurationSettings": [ { "ApplicationName": "my-app", "EnvironmentName": "my-env", "Description": "Environment created from the EB CLI using \"eb create\"", "DeploymentStatus": "deployed", "DateCreated": "2015-08-13T19:16:25Z", "OptionSettings": [ { "OptionName": "Availability Zones", "ResourceName": "AWSEBAutoScalingGroup", "Namespace": "aws:autoscaling:asg", "Value": "Any" }, { "OptionName": "Cooldown", "ResourceName": "AWSEBAutoScalingGroup", "Namespace": "aws:autoscaling:asg", "Value": "360" }, ... { "OptionName": "ConnectionDrainingTimeout", "ResourceName": "AWSEBLoadBalancer", "Namespace": "aws:elb:policies", "Value": "20" }, { "OptionName": "ConnectionSettingIdleTimeout", "ResourceName": "AWSEBLoadBalancer", "Namespace": "aws:elb:policies", "Value": "60" } ], "DateUpdated": "2015-08-13T23:30:07Z", "SolutionStackName": "64bit Amazon Linux 2015.03 v2.0.0 running Tomcat 8 Java 8" } ] }`For more information about namespaces and supported options, see Option Values in the *AWS Elastic Beanstalk Developer Guide*.- 
                    For API details, see [DescribeConfigurationSettings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/describe-configuration-settings.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-environment-health`.

- **AWS CLI**
- 
            
                    **To view environment health**The following command retrieves overall health information for an environment named `my-env`:`aws elasticbeanstalk describe-environment-health --environment-name``my-env`--attribute-names`All`Output: `{ "Status": "Ready", "EnvironmentName": "my-env", "Color": "Green", "ApplicationMetrics": { "Duration": 10, "Latency": { "P99": 0.004, "P75": 0.002, "P90": 0.003, "P95": 0.004, "P85": 0.003, "P10": 0.001, "P999": 0.004, "P50": 0.001 }, "RequestCount": 45, "StatusCodes": { "Status3xx": 0, "Status2xx": 45, "Status5xx": 0, "Status4xx": 0 } }, "RefreshedAt": "2015-08-20T21:09:18Z", "HealthStatus": "Ok", "InstancesHealth": { "Info": 0, "Ok": 1, "Unknown": 0, "Severe": 0, "Warning": 0, "Degraded": 0, "NoData": 0, "Pending": 0 }, "Causes": [] }`Health information is only available for environments with enhanced health reporting enabled. For more information, see Enhanced Health Reporting and Monitoring in the *AWS Elastic Beanstalk Developer Guide*.- 
                    For API details, see [DescribeEnvironmentHealth](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/describe-environment-health.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-environment-resources`.

- **AWS CLI**
- 
            
                    **To view information about the AWS resources in your environment**The following command retrieves information about resources in an environment named `my-env`:`aws elasticbeanstalk describe-environment-resources --environment-name``my-env`Output: `{ "EnvironmentResources": { "EnvironmentName": "my-env", "AutoScalingGroups": [ { "Name": "awseb-e-qu3fyyjyjs-stack-AWSEBAutoScalingGroup-QSB2ZO88SXZT" } ], "Triggers": [], "LoadBalancers": [ { "Name": "awseb-e-q-AWSEBLoa-1EEPZ0K98BIF0" } ], "Queues": [], "Instances": [ { "Id": "i-0c91c786" } ], "LaunchConfigurations": [ { "Name": "awseb-e-qu3fyyjyjs-stack-AWSEBAutoScalingLaunchConfiguration-1UUVQIBC96TQ2" } ] } }`- 
                    For API details, see [DescribeEnvironmentResources](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/describe-environment-resources.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-environments`.

- **AWS CLI**
- 
            
                    **To view information about an environment**The following command retrieves information about an environment named `my-env`:`aws elasticbeanstalk describe-environments --environment-names``my-env`Output: `{ "Environments": [ { "ApplicationName": "my-app", "EnvironmentName": "my-env", "VersionLabel": "7f58-stage-150812_025409", "Status": "Ready", "EnvironmentId": "e-rpqsewtp2j", "EndpointURL": "awseb-e-w-AWSEBLoa-1483140XB0Q4L-109QXY8121.us-west-2.elb.amazonaws.com", "SolutionStackName": "64bit Amazon Linux 2015.03 v2.0.0 running Tomcat 8 Java 8", "CNAME": "my-env.elasticbeanstalk.com", "Health": "Green", "AbortableOperationInProgress": false, "Tier": { "Version": " ", "Type": "Standard", "Name": "WebServer" }, "DateUpdated": "2015-08-12T18:16:55.019Z", "DateCreated": "2015-08-07T20:48:49.599Z" } ] }`- 
                    For API details, see [DescribeEnvironments](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/describe-environments.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-events`.

- **AWS CLI**
- 
            
                    **To view events for an environment**The following command retrieves events for an environment named `my-env`:`aws elasticbeanstalk describe-events --environment-name``my-env`Output (abbreviated): `{ "Events": [ { "ApplicationName": "my-app", "EnvironmentName": "my-env", "Message": "Environment health has transitioned from Info to Ok.", "EventDate": "2015-08-20T07:06:53.535Z", "Severity": "INFO" }, { "ApplicationName": "my-app", "EnvironmentName": "my-env", "Severity": "INFO", "RequestId": "b7f3960b-4709-11e5-ba1e-07e16200da41", "Message": "Environment update completed successfully.", "EventDate": "2015-08-20T07:06:02.049Z" }, ... { "ApplicationName": "my-app", "EnvironmentName": "my-env", "Severity": "INFO", "RequestId": "ca8dfbf6-41ef-11e5-988b-651aa638f46b", "Message": "Using elasticbeanstalk-us-west-2-012445113685 as Amazon S3 storage bucket for environment data.", "EventDate": "2015-08-13T19:16:27.561Z" }, { "ApplicationName": "my-app", "EnvironmentName": "my-env", "Severity": "INFO", "RequestId": "cdfba8f6-41ef-11e5-988b-65638f41aa6b", "Message": "createEnvironment is starting.", "EventDate": "2015-08-13T19:16:26.581Z" } ] }`- 
                    For API details, see [DescribeEvents](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/describe-events.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-instances-health`.

- **AWS CLI**
- 
            
                    **To view environment health**The following command retrieves health information for instances in an environment named `my-env`:`aws elasticbeanstalk describe-instances-health --environment-name``my-env`--attribute-names`All`Output: `{ "InstanceHealthList": [ { "InstanceId": "i-08691cc7", "ApplicationMetrics": { "Duration": 10, "Latency": { "P99": 0.006, "P75": 0.002, "P90": 0.004, "P95": 0.005, "P85": 0.003, "P10": 0.0, "P999": 0.006, "P50": 0.001 }, "RequestCount": 48, "StatusCodes": { "Status3xx": 0, "Status2xx": 47, "Status5xx": 0, "Status4xx": 1 } }, "System": { "LoadAverage": [ 0.0, 0.02, 0.05 ], "CPUUtilization": { "SoftIRQ": 0.1, "IOWait": 0.2, "System": 0.3, "Idle": 97.8, "User": 1.5, "IRQ": 0.0, "Nice": 0.1 } }, "Color": "Green", "HealthStatus": "Ok", "LaunchedAt": "2015-08-13T19:17:09Z", "Causes": [] } ], "RefreshedAt": "2015-08-20T21:09:08Z" }`Health information is only available for environments with enhanced health reporting enabled. For more information, see Enhanced Health Reporting and Monitoring in the *AWS Elastic Beanstalk Developer Guide*.- 
                    For API details, see [DescribeInstancesHealth](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/describe-instances-health.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-available-solution-stacks`.

- **AWS CLI**
- 
            
                    **To view solution stacks**The following command lists solution stacks for all currently available platform configurations and any that you have used in the past: `aws elasticbeanstalk list-available-solution-stacks`Output (abbreviated): `{ "SolutionStacks": [ "64bit Amazon Linux 2015.03 v2.0.0 running Node.js", "64bit Amazon Linux 2015.03 v2.0.0 running PHP 5.6", "64bit Amazon Linux 2015.03 v2.0.0 running PHP 5.5", "64bit Amazon Linux 2015.03 v2.0.0 running PHP 5.4", "64bit Amazon Linux 2015.03 v2.0.0 running Python 3.4", "64bit Amazon Linux 2015.03 v2.0.0 running Python 2.7", "64bit Amazon Linux 2015.03 v2.0.0 running Python", "64bit Amazon Linux 2015.03 v2.0.0 running Ruby 2.2 (Puma)", "64bit Amazon Linux 2015.03 v2.0.0 running Ruby 2.2 (Passenger Standalone)", "64bit Amazon Linux 2015.03 v2.0.0 running Ruby 2.1 (Puma)", "64bit Amazon Linux 2015.03 v2.0.0 running Ruby 2.1 (Passenger Standalone)", "64bit Amazon Linux 2015.03 v2.0.0 running Ruby 2.0 (Puma)", "64bit Amazon Linux 2015.03 v2.0.0 running Ruby 2.0 (Passenger Standalone)", "64bit Amazon Linux 2015.03 v2.0.0 running Ruby 1.9.3", "64bit Amazon Linux 2015.03 v2.0.0 running Tomcat 8 Java 8", "64bit Amazon Linux 2015.03 v2.0.0 running Tomcat 7 Java 7", "64bit Amazon Linux 2015.03 v2.0.0 running Tomcat 7 Java 6", "64bit Windows Server Core 2012 R2 running IIS 8.5", "64bit Windows Server 2012 R2 running IIS 8.5", "64bit Windows Server 2012 running IIS 8", "64bit Windows Server 2008 R2 running IIS 7.5", "64bit Amazon Linux 2015.03 v2.0.0 running Docker 1.6.2", "64bit Amazon Linux 2015.03 v2.0.0 running Multi-container Docker 1.6.2 (Generic)", "64bit Debian jessie v2.0.0 running GlassFish 4.1 Java 8 (Preconfigured - Docker)", "64bit Debian jessie v2.0.0 running GlassFish 4.0 Java 7 (Preconfigured - Docker)", "64bit Debian jessie v2.0.0 running Go 1.4 (Preconfigured - Docker)", "64bit Debian jessie v2.0.0 running Go 1.3 (Preconfigured - Docker)", "64bit Debian jessie v2.0.0 running Python 3.4 (Preconfigured - Docker)", ], "SolutionStackDetails": [ { "PermittedFileTypes": [ "zip" ], "SolutionStackName": "64bit Amazon Linux 2015.03 v2.0.0 running Node.js" }, ... ] }`- 
                    For API details, see [ListAvailableSolutionStacks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/list-available-solution-stacks.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `rebuild-environment`.

- **AWS CLI**
- 
            
                    **To rebuild an environment**The following command terminates and recreates the resources in an environment named `my-env`:`aws elasticbeanstalk rebuild-environment --environment-name``my-env`- 
                    For API details, see [RebuildEnvironment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/rebuild-environment.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `request-environment-info`.

- **AWS CLI**
- 
            
                    **To request tailed logs**The following command requests logs from an environment named `my-env`:`aws elasticbeanstalk request-environment-info --environment-name``my-env`--info-type`tail`After requesting logs, retrieve their location with retrieve-environment-info. - 
                    For API details, see [RequestEnvironmentInfo](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/request-environment-info.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `restart-app-server`.

- **AWS CLI**
- 
            
                    **To restart application servers**The following command restarts application servers on all instances in an environment named `my-env`:`aws elasticbeanstalk restart-app-server --environment-name``my-env`- 
                    For API details, see [RestartAppServer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/restart-app-server.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `retrieve-environment-info`.

- **AWS CLI**
- 
            
                    **To retrieve tailed logs**The following command retrieves a link to logs from an environment named `my-env`:`aws elasticbeanstalk retrieve-environment-info --environment-name``my-env`--info-type`tail`Output: `{ "EnvironmentInfo": [ { "SampleTimestamp": "2015-08-20T22:23:17.703Z", "Message": "https://elasticbeanstalk-us-west-2-0123456789012.s3.amazonaws.com/resources/environments/logs/tail/e-fyqyju3yjs/i-09c1c867/TailLogs-1440109397703.out?AWSAccessKeyId=AKGPT4J56IAJ2EUBL5CQ&Expires=1440195891&Signature=n%2BEalOV6A2HIOx4Rcfb7LT16bBM%3D", "InfoType": "tail", "Ec2InstanceId": "i-09c1c867" } ] }`View the link in a browser. Prior to retrieval, logs must be requested with request-environment-info. - 
                    For API details, see [RetrieveEnvironmentInfo](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/retrieve-environment-info.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `swap-environment-cnames`.

- **AWS CLI**
- 
            
                    **To swap environment CNAMES**The following command swaps the assigned subdomains of two environments: `aws elasticbeanstalk swap-environment-cnames --source-environment-name``my-env-blue`--destination-environment-name`my-env-green`- 
                    For API details, see [SwapEnvironmentCnames](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/swap-environment-cnames.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `terminate-environment`.

- **AWS CLI**
- 
            
                    **To terminate an environment**The following command terminates an Elastic Beanstalk environment named `my-env`:`aws elasticbeanstalk terminate-environment --environment-name``my-env`Output: `{ "ApplicationName": "my-app", "EnvironmentName": "my-env", "Status": "Terminating", "EnvironmentId": "e-fh2eravpns", "EndpointURL": "awseb-e-f-AWSEBLoa-1I9XUMP4-8492WNUP202574.us-west-2.elb.amazonaws.com", "SolutionStackName": "64bit Amazon Linux 2015.03 v2.0.0 running Tomcat 8 Java 8", "CNAME": "my-env.elasticbeanstalk.com", "Health": "Grey", "AbortableOperationInProgress": false, "Tier": { "Version": " ", "Type": "Standard", "Name": "WebServer" }, "DateUpdated": "2015-08-12T19:05:54.744Z", "DateCreated": "2015-08-12T18:52:53.622Z" }`- 
                    For API details, see [TerminateEnvironment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/terminate-environment.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-application-version`.

- **AWS CLI**
- 
            
                    **To change an application version's description**The following command updates the description of an application version named `22a0-stage-150819_185942`:`aws elasticbeanstalk update-application-version --version-label``22a0-stage-150819_185942`--application-name`my-app`--description`"new description"`Output: `{ "ApplicationVersion": { "ApplicationName": "my-app", "VersionLabel": "22a0-stage-150819_185942", "Description": "new description", "DateCreated": "2015-08-19T18:59:17.646Z", "DateUpdated": "2015-08-20T22:53:28.871Z", "SourceBundle": { "S3Bucket": "elasticbeanstalk-us-west-2-0123456789012", "S3Key": "my-app/22a0-stage-150819_185942.war" } } }`- 
                    For API details, see [UpdateApplicationVersion](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/update-application-version.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-application`.

- **AWS CLI**
- 
            
                    **To change an application's description**The following command updates the description of an application named `my-app`:`aws elasticbeanstalk update-application --application-name``my-app`--description`"my Elastic Beanstalk application"`Output: `{ "Application": { "ApplicationName": "my-app", "Description": "my Elastic Beanstalk application", "Versions": [ "2fba-stage-150819_234450", "bf07-stage-150820_214945", "93f8", "fd7c-stage-150820_000431", "22a0-stage-150819_185942" ], "DateCreated": "2015-08-13T19:15:50.449Z", "ConfigurationTemplates": [], "DateUpdated": "2015-08-20T22:34:56.195Z" } }`- 
                    For API details, see [UpdateApplication](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/update-application.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-configuration-template`.

- **AWS CLI**
- 
            
                    **To update a configuration template**The following command removes the configured CloudWatch custom health metrics configuration `ConfigDocument`from a saved configuration template named`my-template`:`aws elasticbeanstalk update-configuration-template --template-name``my-template`--application-name`my-app`--options-to-remove`Namespace=aws:elasticbeanstalk:healthreporting:system,OptionName=ConfigDocument`Output: `{ "ApplicationName": "my-app", "TemplateName": "my-template", "DateCreated": "2015-08-20T22:39:31Z", "DateUpdated": "2015-08-20T22:43:11Z", "SolutionStackName": "64bit Amazon Linux 2015.03 v2.0.0 running Tomcat 8 Java 8" }`For more information about namespaces and supported options, see Option Values in the *AWS Elastic Beanstalk Developer Guide*.- 
                    For API details, see [UpdateConfigurationTemplate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/update-configuration-template.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-environment`.

- **AWS CLI**
- 
            
                    **To update an environment to a new version**The following command updates an environment named "my-env" to version "v2" of the application to which it belongs: `aws elasticbeanstalk update-environment --environment-name``my-env`--version-label`v2`This command requires that the "my-env" environment already exists and belongs to an application that has a valid application version with the label "v2". Output: `{ "ApplicationName": "my-app", "EnvironmentName": "my-env", "VersionLabel": "v2", "Status": "Updating", "EnvironmentId": "e-szqipays4h", "EndpointURL": "awseb-e-i-AWSEBLoa-1RDLX6TC9VUAO-0123456789.us-west-2.elb.amazonaws.com", "SolutionStackName": "64bit Amazon Linux running Tomcat 7", "CNAME": "my-env.elasticbeanstalk.com", "Health": "Grey", "Tier": { "Version": " ", "Type": "Standard", "Name": "WebServer" }, "DateUpdated": "2015-02-03T23:12:29.119Z", "DateCreated": "2015-02-03T23:04:54.453Z" }`**To set an environment variable**The following command sets the value of the "PARAM1" variable in the "my-env" environment to "ParamValue": `aws elasticbeanstalk update-environment --environment-name``my-env`--option-settings`Namespace=aws:elasticbeanstalk:application:environment,OptionName=PARAM1,Value=ParamValue`The `option-settings`parameter takes a namespace in addition to the name and value of the variable. Elastic Beanstalk supports several namespaces for options in addition to environment variables.**To configure option settings from a file**The following command configures several options in the `aws:elb:loadbalancer`namespace from a file:`aws elasticbeanstalk update-environment --environment-name``my-env`--option-settings`file://options.json``options.json`is a JSON object defining several settings:`[ { "Namespace": "aws:elb:healthcheck", "OptionName": "Interval", "Value": "15" }, { "Namespace": "aws:elb:healthcheck", "OptionName": "Timeout", "Value": "8" }, { "Namespace": "aws:elb:healthcheck", "OptionName": "HealthyThreshold", "Value": "2" }, { "Namespace": "aws:elb:healthcheck", "OptionName": "UnhealthyThreshold", "Value": "3" } ]`Output: `{ "ApplicationName": "my-app", "EnvironmentName": "my-env", "VersionLabel": "7f58-stage-150812_025409", "Status": "Updating", "EnvironmentId": "e-wtp2rpqsej", "EndpointURL": "awseb-e-w-AWSEBLoa-14XB83101Q4L-104QXY80921.sa-east-1.elb.amazonaws.com", "SolutionStackName": "64bit Amazon Linux 2015.03 v2.0.0 running Tomcat 8 Java 8", "CNAME": "my-env.elasticbeanstalk.com", "Health": "Grey", "AbortableOperationInProgress": true, "Tier": { "Version": " ", "Type": "Standard", "Name": "WebServer" }, "DateUpdated": "2015-08-12T18:15:23.804Z", "DateCreated": "2015-08-07T20:48:49.599Z" }`For more information about namespaces and supported options, see Option Values in the *AWS Elastic Beanstalk Developer Guide*.- 
                    For API details, see [UpdateEnvironment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/update-environment.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `validate-configuration-settings`.

- **AWS CLI**
- 
            
                    **To validate configuration settings**The following command validates a CloudWatch custom metrics config document: `aws elasticbeanstalk validate-configuration-settings --application-name``my-app`--environment-name`my-env`--option-settings`file://options.json``options.json`is a JSON document that includes one or more configuration settings to validate:`[ { "Namespace": "aws:elasticbeanstalk:healthreporting:system", "OptionName": "ConfigDocument", "Value": "{\"CloudWatchMetrics\": {\"Environment\": {\"ApplicationLatencyP99.9\": null,\"InstancesSevere\": 60,\"ApplicationLatencyP90\": 60,\"ApplicationLatencyP99\": null,\"ApplicationLatencyP95\": 60,\"InstancesUnknown\": 60,\"ApplicationLatencyP85\": 60,\"InstancesInfo\": null,\"ApplicationRequests2xx\": null,\"InstancesDegraded\": null,\"InstancesWarning\": 60,\"ApplicationLatencyP50\": 60,\"ApplicationRequestsTotal\": null,\"InstancesNoData\": null,\"InstancesPending\": 60,\"ApplicationLatencyP10\": null,\"ApplicationRequests5xx\": null,\"ApplicationLatencyP75\": null,\"InstancesOk\": 60,\"ApplicationRequests3xx\": null,\"ApplicationRequests4xx\": null},\"Instance\": {\"ApplicationLatencyP99.9\": null,\"ApplicationLatencyP90\": 60,\"ApplicationLatencyP99\": null,\"ApplicationLatencyP95\": null,\"ApplicationLatencyP85\": null,\"CPUUser\": 60,\"ApplicationRequests2xx\": null,\"CPUIdle\": null,\"ApplicationLatencyP50\": null,\"ApplicationRequestsTotal\": 60,\"RootFilesystemUtil\": null,\"LoadAverage1min\": null,\"CPUIrq\": null,\"CPUNice\": 60,\"CPUIowait\": 60,\"ApplicationLatencyP10\": null,\"LoadAverage5min\": null,\"ApplicationRequests5xx\": null,\"ApplicationLatencyP75\": 60,\"CPUSystem\": 60,\"ApplicationRequests3xx\": 60,\"ApplicationRequests4xx\": null,\"InstanceHealth\": null,\"CPUSoftirq\": 60}},\"Version\": 1}" } ]`If the options that you specify are valid for the specified environment, Elastic Beanstalk returns an empty Messages array: `{ "Messages": [] }`If validation fails, the response will include information about the error: `{ "Messages": [ { "OptionName": "ConfigDocumet", "Message": "Invalid option specification (Namespace: 'aws:elasticbeanstalk:healthreporting:system', OptionName: 'ConfigDocumet'): Unknown configuration setting.", "Namespace": "aws:elasticbeanstalk:healthreporting:system", "Severity": "error" } ] }`For more information about namespaces and supported options, see Option Values in the *AWS Elastic Beanstalk Developer Guide*.- 
                    For API details, see [ValidateConfigurationSettings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/validate-configuration-settings.html)in*AWS CLI Command Reference*.
 
-