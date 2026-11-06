# Amazon GameLift Servers examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_gamelift_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_gamelift_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Amazon GameLift Servers.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `create-build`.

- **AWS CLI**
- 
            
                    **Example1: To create a game build from files in an S3 bucket**The following `create-build`example creates a custom game build resource. It uses zipped files that are stored in an S3 location in an AWS account that you control. This example assumes that you've already created an IAM role that gives Amazon GameLift permission to access the S3 location. Since the request does not specify an operating system, the new build resource defaults to WINDOWS_2012.`aws gamelift create-build \ --storage-location``file://storage-loc.json`\ --name`MegaFrogRaceServer.NA`\ --build-version`12345.678`Contents of `storage-loc.json`:`{ "Bucket":"MegaFrogRaceServer_NA_build_files" "Key":"MegaFrogRaceServer_build_123.zip" "RoleArn":"arn:aws:iam::123456789012:role/gamelift" }`Output: `{ "Build": { "BuildArn": "arn:aws:gamelift:us-west-2::build/build-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "BuildId": "build-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "CreationTime": 1496708916.18, "Name": "MegaFrogRaceServer.NA", "OperatingSystem": "WINDOWS_2012", "SizeOnDisk": 479303, "Status": "INITIALIZED", "Version": "12345.678" }, "StorageLocation": { "Bucket": "MegaFrogRaceServer_NA_build_files", "Key": "MegaFrogRaceServer_build_123.zip" } }`**Example2: To create a game build resource for manually uploading files to GameLift**The following `create-build`example creates a new build resource. It also gets a storage location and temporary credentials that allow you to manually upload your game build to the GameLift location in Amazon S3. Once you've successfully uploaded your build, the GameLift service validates the build and updates the new build's status.`aws gamelift create-build \ --name``MegaFrogRaceServer.NA`\ --build-version`12345.678`\ --operating-system`AMAZON_LINUX`Output: `{ "Build": { "BuildArn": "arn:aws:gamelift:us-west-2::build/build-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "BuildId": "build-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "CreationTime": 1496708916.18, "Name": "MegaFrogRaceServer.NA", "OperatingSystem": "AMAZON_LINUX", "SizeOnDisk": 0, "Status": "INITIALIZED", "Version": "12345.678" }, "StorageLocation": { "Bucket": "gamelift-builds-us-west-2", "Key": "123456789012/build-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111" }, "UploadCredentials": { "AccessKeyId": "AKIAIOSFODNN7EXAMPLE", "SecretAccessKey": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY", "SessionToken": "AgoGb3JpZ2luENz...EXAMPLETOKEN==" } }`For more information, see [Upload a Custom Server Build to GameLift](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-build-cli-uploading.html)in the*Amazon GameLift Developer Guide*.- 
                    For API details, see [CreateBuild](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/create-build.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-fleet`.

- **AWS CLI**
- 
            
                    **Example 1: To create a basic Linux fleet**The following `create-fleet`example creates a minimally configured fleet of on-demand Linux instances to host a custom server build. You can complete the configuration by using`update-fleet`.`aws gamelift create-fleet \ --name``MegaFrogRaceServer.NA.v2`\ --description '`Hosts for v2 North America`' \ --build-id`build-1111aaaa-22bb-33cc-44dd-5555eeee66ff`\ --certificate-configuration '`CertificateType=GENERATED`' \ --ec2-instance-type`c4.large`\ --fleet-type`ON_DEMAND`\ --runtime-configuration '`ServerProcesses=[{LaunchPath=/local/game/release-na/MegaFrogRace_Server.exe,ConcurrentExecutions=1}]`'Output: `{ "FleetAttributes": { "BuildId": "build-1111aaaa-22bb-33cc-44dd-5555eeee66ff", "CertificateConfiguration": { "CertificateType": "GENERATED" }, "CreationTime": 1496365885.44, "Description": "Hosts for v2 North America", "FleetArn": "arn:aws:gamelift:us-west-2:444455556666:fleet/fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa", "FleetId": "fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa", "FleetType": "ON_DEMAND", "InstanceType": "c4.large", "MetricGroups": ["default"], "Name": "MegaFrogRace.NA.v2", "NewGameSessionProtectionPolicy": "NoProtection", "OperatingSystem": "AMAZON_LINUX", "ServerLaunchPath": "/local/game/release-na/MegaFrogRace_Server.exe", "Status": "NEW" } }`**Example 2: To create a basic Windows fleet**The following `create-fleet`example creates a minimally configured fleet of spot Windows instances to host a custom server build. You can complete the configuration by using`update-fleet`.`aws gamelift create-fleet \ --name``MegaFrogRace.NA.v2`\ --description '`Hosts for v2 North America`' \ --build-id`build-2222aaaa-33bb-44cc-55dd-6666eeee77ff`\ --certificate-configuration '`CertificateType=GENERATED`' \ --ec2-instance-type`c4.large`\ --fleet-type`SPOT`\ --runtime-configuration '`ServerProcesses=[{LaunchPath=C:\game\Bin64.Release.Dedicated\MegaFrogRace_Server.exe,ConcurrentExecutions=1}]`'Output: `{ "FleetAttributes": { "BuildId": "build-2222aaaa-33bb-44cc-55dd-6666eeee77ff", "CertificateConfiguration": { "CertificateType": "GENERATED" }, "CreationTime": 1496365885.44, "Description": "Hosts for v2 North America", "FleetArn": "arn:aws:gamelift:us-west-2:444455556666:fleet/fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa", "FleetId": "fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa", "FleetType": "SPOT", "InstanceType": "c4.large", "MetricGroups": ["default"], "Name": "MegaFrogRace.NA.v2", "NewGameSessionProtectionPolicy": "NoProtection", "OperatingSystem": "WINDOWS_2012", "ServerLaunchPath": "C:\game\Bin64.Release.Dedicated\MegaFrogRace_Server.exe", "Status": "NEW" } }`**Example 3: To create a fully configured fleet**The following `create-fleet`example creates a fleet of Spot Windows instances for a custom server build, with most commonly used configuration settings provided.`aws gamelift create-fleet \ --name``MegaFrogRace.NA.v2`\ --description '`Hosts for v2 North America`' \ --build-id`build-2222aaaa-33bb-44cc-55dd-6666eeee77ff`\ --certificate-configuration '`CertificateType=GENERATED`' \ --ec2-instance-type`c4.large`\ --ec2-inbound-permissions '`FromPort=33435,ToPort=33435,IpRange=10.24.34.0/23,Protocol=UDP`' \ --fleet-type`SPOT`\ --new-game-session-protection-policy`FullProtection`\ --runtime-configuration`file://runtime-config.json`\ --metric-groups`default`\ --instance-role-arn '`arn:aws:iam::444455556666:role/GameLiftS3Access`'Contents of `runtime-config.json`:`GameSessionActivationTimeoutSeconds=300, MaxConcurrentGameSessionActivations=2, ServerProcesses=[ {LaunchPath=C:\game\Bin64.Release.Dedicated\MegaFrogRace_Server.exe,Parameters=-debug,ConcurrentExecutions=1}, {LaunchPath=C:\game\Bin64.Release.Dedicated\MegaFrogRace_Server.exe,ConcurrentExecutions=1}]`Output: `{ "FleetAttributes": { "InstanceRoleArn": "arn:aws:iam::444455556666:role/GameLiftS3Access", "Status": "NEW", "InstanceType": "c4.large", "FleetArn": "arn:aws:gamelift:us-west-2:444455556666:fleet/fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa", "FleetId": "fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa", "Description": "Hosts for v2 North America", "FleetType": "SPOT", "OperatingSystem": "WINDOWS_2012", "Name": "MegaFrogRace.NA.v2", "CreationTime": 1569309011.11, "MetricGroups": [ "default" ], "BuildId": "build-2222aaaa-33bb-44cc-55dd-6666eeee77ff", "ServerLaunchParameters": "abc", "ServerLaunchPath": "C:\\game\\Bin64.Release.Dedicated\\MegaFrogRace_Server.exe", "NewGameSessionProtectionPolicy": "FullProtection", "CertificateConfiguration": { "CertificateType": "GENERATED" } } }`**Example 4: To create a Realtime Servers fleet**The following `create-fleet`example creates a fleet of Spot instances with a Realtime configuration script that has been uploaded to Amazon GameLift. All Realtime servers are deployed onto Linux machines. For the purposes of this example, assume that the uploaded Realtime script includes multiple script files, with the`Init()`function located in the script file called`MainScript.js`. As shown, this file is identified as the launch script in the runtime configuration.`aws gamelift create-fleet \ --name``MegaFrogRace.NA.realtime`\ --description '`Mega Frog Race Realtime fleet`' \ --script-id`script-1111aaaa-22bb-33cc-44dd-5555eeee66ff`\ --ec2-instance-type`c4.large`\ --fleet-type`SPOT`\ --certificate-configuration '`CertificateType=GENERATED`' --runtime-configuration '`ServerProcesses=[{LaunchPath=/local/game/MainScript.js,Parameters=+map Winter444,ConcurrentExecutions=5}]`'Output: `{ "FleetAttributes": { "FleetId": "fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa", "Status": "NEW", "CreationTime": 1569310745.212, "InstanceType": "c4.large", "NewGameSessionProtectionPolicy": "NoProtection", "CertificateConfiguration": { "CertificateType": "GENERATED" }, "Name": "MegaFrogRace.NA.realtime", "ScriptId": "script-1111aaaa-22bb-33cc-44dd-5555eeee66ff", "FleetArn": "arn:aws:gamelift:us-west-2:444455556666:fleet/fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa", "FleetType": "SPOT", "MetricGroups": [ "default" ], "Description": "Mega Frog Race Realtime fleet", "OperatingSystem": "AMAZON_LINUX" } }`- 
                    For API details, see [CreateFleet](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/create-fleet.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-game-session-queue`.

- **AWS CLI**
- 
            
                    **Example1: To set up an ordered game session queue**The following `create-game-session-queue`example creates a new game session queue with destinations in two regions. It also configures the queue so that game session requests time out after waiting 10 minutes for placement. Since no latency policies are defined, GameLift attempts to place all game sessions with the first destination listed.`aws gamelift create-game-session-queue \ --name``MegaFrogRaceServer-NA`\ --destinations`file://destinations.json`\ --timeout-in-seconds`600`Contents of `destinations.json`:`{ "Destinations": [ {"DestinationArn": "arn:aws:gamelift:us-west-2::fleet/fleet-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111" }, {"DestinationArn": "arn:aws:gamelift:us-west-1::fleet/fleet-a1b2c3d4-5678-90ab-cdef-EXAMPLE22222" } ] }`Output: `{ "GameSessionQueues": [ { "Name": "MegaFrogRaceServer-NA", "GameSessionQueueArn": "arn:aws:gamelift:us-west-2:123456789012:gamesessionqueue/MegaFrogRaceServer-NA", "TimeoutInSeconds": 600, "Destinations": [ {"DestinationArn": "arn:aws:gamelift:us-west-2::fleet/fleet-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"}, {"DestinationArn": "arn:aws:gamelift:us-west-1::fleet/fleet-a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"} ] } ] }`**Example2: To set up a game session queue with player latency policies**The following `create-game-session-queue`example creates a new game session queue with two player latency policies. The first policy sets a 100ms latency cap that is enforced during the first minute of a game session placement attempt. The second policy raises the latency cap to 200ms until the placement request times out at 3 minutes.`aws gamelift create-game-session-queue \ --name``MegaFrogRaceServer-NA`\ --destinations`file://destinations.json`\ --player-latency-policies`file://latency-policies.json`\ --timeout-in-seconds`180`Contents of `destinations.json`:`{ "Destinations": [ { "DestinationArn": "arn:aws:gamelift:us-west-2::fleet/fleet-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111" }, { "DestinationArn": "arn:aws:gamelift:us-east-1::fleet/fleet-a1b2c3d4-5678-90ab-cdef-EXAMPLE22222" } ] }`Contents of `latency-policies.json`:`{ "PlayerLatencyPolicies": [ {"MaximumIndividualPlayerLatencyMilliseconds": 200}, {"MaximumIndividualPlayerLatencyMilliseconds": 100, "PolicyDurationSeconds": 60} ] }`Output: `{ "GameSessionQueue": { "Name": "MegaFrogRaceServer-NA", "GameSessionQueueArn": "arn:aws:gamelift:us-west-2:111122223333:gamesessionqueue/MegaFrogRaceServer-NA", "TimeoutInSeconds": 600, "PlayerLatencyPolicies": [ { "MaximumIndividualPlayerLatencyMilliseconds": 100, "PolicyDurationSeconds": 60 }, { "MaximumIndividualPlayerLatencyMilliseconds": 200 } ] "Destinations": [ {"DestinationArn": "arn:aws:gamelift:us-west-2::fleet/fleet-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"}, {"DestinationArn": "arn:aws:gamelift:us-east-1::fleet/fleet-a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"} ], } }`For more information, see [Create a Queue](https://docs.aws.amazon.com/gamelift/latest/developerguide/queues-creating.html#queues-creating-cli)in the*Amazon GameLift Developer Guide*.- 
                    For API details, see [CreateGameSessionQueue](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/create-game-session-queue.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-build`.

- **AWS CLI**
- 
            
                    **To delete a custom game build**The following `delete-build`example removes a build from your Amazon GameLift account. After the build is deleted, you cannot use it to create new fleets. This operation cannot be undone.`aws gamelift delete-build \ --build-id``build-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`This command produces no output. - 
                    For API details, see [DeleteBuild](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/delete-build.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-fleet`.

- **AWS CLI**
- 
            
                    **To delete a fleet that is no longer in use**The following `delete-fleet`example removes a fleet that has been scaled down to zero instances. If the fleet capacity is greater than zero, the request fails with an HTTP 400 error.`aws gamelift delete-fleet \ --fleet-id``fleet-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`This command produces no output. For more information, see [Manage GameLift Fleets](https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-editing.html)in the*Amazon GameLift Developer Guide*.- 
                    For API details, see [DeleteFleet](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/delete-fleet.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-game-session-queue`.

- **AWS CLI**
- 
            
                    **To delete a game session queue**The following `delete-game-session-queue`example deletes a specified game session queue.`aws gamelift delete-game-session-queue \ --name``MegaFrogRace-NA`This command produces no output. - 
                    For API details, see [DeleteGameSessionQueue](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/delete-game-session-queue.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-build`.

- **AWS CLI**
- 
            
                    **To get information on a custom game build**The following `describe-build`example retrieves properties for a game server build resource.`aws gamelift describe-build \ --build-id``build-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`Output: `{ "Build": { "BuildArn": "arn:aws:gamelift:us-west-2::build/build-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "BuildId": "build-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "CreationTime": 1496708916.18, "Name": "My_Game_Server_Build_One", "OperatingSystem": "AMAZON_LINUX", "SizeOnDisk": 1304924, "Status": "READY", "Version": "12345.678" } }`For more information, see [Upload a Custom Server Build to GameLift](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-build-cli-uploading.html#gamelift-build-cli-uploading-builds)in the*Amazon GameLift Developer Guide*.- 
                    For API details, see [DescribeBuild](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-build.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-ec2-instance-limits`.

- **AWS CLI**
- 
            
                    **To retrieve service limits for an EC2 instance type**The following `describe-ec2-instance-limits`example displays the maximum allowed instances and current instances in use for the specified EC2 instance type in the current Region. The result indicates that only five of the allowed twenty instances are being used.`aws gamelift describe-ec2-instance-limits \ --ec2-instance-type``m5.large`Output: `{ "EC2InstanceLimits": [ { "EC2InstanceType": ""m5.large", "CurrentInstances": 5, "InstanceLimit": 20 } ] }`For more information, see [Choose Computing Resources](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-ec2-instances.html)in the*Amazon GameLift Developer Guide*.- 
                    For API details, see [DescribeEc2InstanceLimits](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-ec2-instance-limits.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-fleet-attributes`.

- **AWS CLI**
- 
            
                    **Example1: To view attributes for a list of fleets**The following `describe-fleet-attributes`example retrieves fleet attributes for two specified fleets. As shown, the requested fleets are deployed with the same build, one for On-Demand instances and one for Spot instances, with some minor configuration differences.`aws gamelift describe-fleet-attributes \ --fleet-ids``arn:aws:gamelift:us-west-2::fleet/fleet-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111``fleet-a1b2c3d4-5678-90ab-cdef-EXAMPLE22222`Output: `{ "FleetAttributes": [ { "FleetId": "fleet-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "FleetArn": "arn:aws:gamelift:us-west-2::fleet/fleet-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "FleetType": "ON_DEMAND", "InstanceType": "c4.large", "Description": "On-demand hosts for v2 North America", "Name": "MegaFrogRaceServer.NA.v2-od", "CreationTime": 1568836191.995, "Status": "ACTIVE", "BuildId": "build-a1b2c3d4-5678-90ab-cdef-EXAMPLE33333", "BuildArn": "arn:aws:gamelift:us-west-2::build/build-a1b2c3d4-5678-90ab-cdef-EXAMPLE33333", "ServerLaunchPath": "C:\\game\\MegaFrogRace_Server.exe", "ServerLaunchParameters": "+gamelift_start_server", "NewGameSessionProtectionPolicy": "NoProtection", "OperatingSystem": "WINDOWS_2012", "MetricGroups": [ "default" ], "CertificateConfiguration": { "CertificateType": "DISABLED" } }, { "FleetId": "fleet-a1b2c3d4-5678-90ab-cdef-EXAMPLE22222", "FleetArn": "arn:aws:gamelift:us-west-2::fleet/fleet-a1b2c3d4-5678-90ab-cdef-EXAMPLE22222", "FleetType": "SPOT", "InstanceType": "c4.large", "Description": "On-demand hosts for v2 North America", "Name": "MegaFrogRaceServer.NA.v2-spot", "CreationTime": 1568838275.379, "Status": "ACTIVATING", "BuildId": "build-a1b2c3d4-5678-90ab-cdef-EXAMPLE33333", "BuildArn": "arn:aws:gamelift:us-west-2::build/build-a1b2c3d4-5678-90ab-cdef-EXAMPLE33333", "ServerLaunchPath": "C:\\game\\MegaFrogRace_Server.exe", "NewGameSessionProtectionPolicy": "NoProtection", "OperatingSystem": "WINDOWS_2012", "MetricGroups": [ "default" ], "CertificateConfiguration": { "CertificateType": "GENERATED" } } ] }`**Example2: To request attributes for all fleets**The following `describe-fleet-attributes`returns fleet attributes for all fleets with any status. This example illustrates the use of pagination parameters to return one fleet at a time.`aws gamelift describe-fleet-attributes \ --limit``1`Output: `{ "FleetAttributes": [ { "FleetId": "fleet-a1b2c3d4-5678-90ab-cdef-EXAMPLE22222", "FleetArn": "arn:aws:gamelift:us-west-2::fleet/fleet-a1b2c3d4-5678-90ab-cdef-EXAMPLE22222", "FleetType": "SPOT", "InstanceType": "c4.large", "Description": "On-demand hosts for v2 North America", "Name": "MegaFrogRaceServer.NA.v2-spot", "CreationTime": 1568838275.379, "Status": "ACTIVATING", "BuildId": "build-a1b2c3d4-5678-90ab-cdef-EXAMPLE33333", "BuildArn": "arn:aws:gamelift:us-west-2::build/build-a1b2c3d4-5678-90ab-cdef-EXAMPLE33333", "ServerLaunchPath": "C:\\game\\MegaFrogRace_Server.exe", "NewGameSessionProtectionPolicy": "NoProtection", "OperatingSystem": "WINDOWS_2012", "MetricGroups": [ "default" ], "CertificateConfiguration": { "CertificateType": "GENERATED" } } ], "NextToken": "eyJhd3NBY2NvdW50SWQiOnsicyI6IjMwMjc3NjAxNjM5OCJ9LCJidWlsZElkIjp7InMiOiJidWlsZC01NWYxZTZmMS1jY2FlLTQ3YTctOWI5ZS1iYjFkYTQwMjEXAMPLE2" }`The output includes a `NextToken`value that you can use when you call the command a second time. Pass the value to the`--next-token`parameter to specify where to pick up the output. The following command returns the second result in the output.`aws gamelift describe-fleet-attributes \ --limit``1`\ --next-token`eyJhd3NBY2NvdW50SWQiOnsicyI6IjMwMjc3NjAxNjM5OCJ9LCJidWlsZElkIjp7InMiOiJidWlsZC01NWYxZTZmMS1jY2FlLTQ3YTctOWI5ZS1iYjFkYTQwMjEXAMPLE1`Repeat until the response doesn't include a `NextToken`value.For more information, see [Setting Up GameLift Fleets](https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-intro.html)in the*Amazon GameLift Developer Guide*.- 
                    For API details, see [DescribeFleetAttributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-fleet-attributes.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-fleet-capacity`.

- **AWS CLI**
- 
            
                    **To view capacity status for a list of fleets**The following `describe-fleet-capacity`example retrieves current capacity for two specified fleets.`aws gamelift describe-fleet-capacity \ --fleet-ids``arn:aws:gamelift:us-west-2::fleet/fleet-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111``fleet-a1b2c3d4-5678-90ab-cdef-EXAMPLE22222`Output: `{ "FleetCapacity": [ { "FleetId": "fleet-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "InstanceType": "c5.large", "InstanceCounts": { "DESIRED": 10, "MINIMUM": 1, "MAXIMUM": 20, "PENDING": 0, "ACTIVE": 10, "IDLE": 3, "TERMINATING": 0 } }, { "FleetId": "fleet-a1b2c3d4-5678-90ab-cdef-EXAMPLE22222", "InstanceType": "c5.large", "InstanceCounts": { "DESIRED": 13, "MINIMUM": 1, "MAXIMUM": 20, "PENDING": 0, "ACTIVE": 15, "IDLE": 2, "TERMINATING": 2 } } ] }`For more information, see [GameLift Metrics for Fleets](https://docs.aws.amazon.com/gamelift/latest/developerguide/monitoring-cloudwatch.html#gamelift-metrics-fleet)in the*Amazon GameLift Developer Guide*.- 
                    For API details, see [DescribeFleetCapacity](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-fleet-capacity.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-fleet-events`.

- **AWS CLI**
- 
            
                    **To request events for a specified time span**The following `describe-fleet-events`example displays details of all fleet-related events that occurred during the specified time span.`aws gamelift describe-fleet-events \ --fleet-id``arn:aws:gamelift:us-west-2::fleet/fleet-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`\ --start-time`1579647600`\ --end-time`1579649400`\ --limit`5`Output: `{ "Events": [ { "EventId": "a37b6892-5d07-4d3b-8b47-80244ecf66b9", "ResourceId": "fleet-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "EventCode": "FLEET_STATE_ACTIVE", "Message": "Fleet fleet-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111 changed state to ACTIVE", "EventTime": 1579649342.191 }, { "EventId": "67da4ec9-92a3-4d95-886a-5d6772c24063", "ResourceId": "fleet-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "EventCode": "FLEET_STATE_ACTIVATING", "Message": "Fleet fleet-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111 changed state to ACTIVATING", "EventTime": 1579649321.427 }, { "EventId": "23813a46-a9e6-4a53-8847-f12e6a8381ac", "ResourceId": "fleet-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "EventCode": "FLEET_STATE_BUILDING", "Message": "Fleet fleet-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111 changed state to BUILDING", "EventTime": 1579649321.243 }, { "EventId": "3bf217d0-1d44-42f9-9202-433ed475d2e8", "ResourceId": "fleet-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "EventCode": "FLEET_STATE_VALIDATING", "Message": "Fleet fleet-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111 changed state to VALIDATING", "EventTime": 1579649197.449 }, { "EventId": "2ecd0130-5986-44eb-99a7-62df27741084", "ResourceId": "fleet-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "EventCode": "FLEET_VALIDATION_LAUNCH_PATH_NOT_FOUND", "Message": "Failed to find a valid path", "EventTime": 1569319075.839, "PreSignedLogUrl": "https://gamelift-event-logs-prod-us-west-2.s3.us-west-2.amazonaws.com/logs/fleet-83422059-8329-42a2-a4d6-c4444386a6f8/events/2ecd0130-5986-44eb-99a7-62df27741084/FLEET_VALIDATION_LAUNCH_PATH_NOT_FOUND.txt?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB8aCXVzLXdlc3QtMiJHMEUCIHV5K%2FLPx8h310D%2FAvx0%2FZxsDy5XA3cJOwPdu3T0eBa%2FAiEA1yovokcZYy%2FV4CWW6l26aFyiSHO%2Bxz%2FBMAhEHYHMQNcqkQMImP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw3NDEwNjE1OTIxNzEiDI8rsZtzLzlwEDQhXSrlAtl5Ae%2Fgo6FCIzqXPbXfBOnSvFYqeDlriZarEpKqKrUt8mXQv9iqHResqCph9AKo49lwgSYTT2QoSxnrD7%2FUgv%2BZm2pVuczvuKtUA0fcx6s0GxpjIAzdIE%2F5P%2FB7B9M%2BVZ%2F9KF82hbJi0HTE6Y7BjKsEgFCvk4UXILhfjtan9iQl8%2F21ZTurAcJbm7Y5tuLF9SWSK3%2BEa7VXOcCK4D4O1sMjmdRm0q0CKZ%2FIaXoHkNvg0RVTa0hIqdvpaDQlsSBNdqTXbjHTu6fETE9Y9Ky%2BiJK5KiUG%2F59GjCpDcvS1FqKeLUEmKT7wysGmvjMc2n%2Fr%2F9VxQfte7w9srXwlLAQuwhiXAAyI5ICMZ5JvzjzQwTqD4CHTVKUUDwL%2BRZzbuuqkJObZml02CkRGp%2B74RTAzLbWptVqZTIfzctiCTmWxb%2FmKyELRYsVLrwNJ%2BGJ7%2BCrN0RC%2FjlgfLYIZyeAqjPgAu5HjgX%2BM7jCo9M7wBTrnAXKOFQuf9dvA84SuwXOJFp17LYGjrHMKv0qC3GfbTMrZ6kzeNV9awKCpXB2Gnx9z2KvIlJdqirWVpvHVGwKCmJBCesDzjJHrae3neogI1uW%2F9C6%2B4jIZPME3jXmZcEHqqw5uvAVF7aeIavtUZU8pxpDIWT0YE4p3Kriy2AA7ziCRKtVfjV839InyLk8LUjsioWK2qlpg2HXKFLpAXw1QsQyxYmFMB9sGKOUlbL7Jdkk%2BYUq8%2FDTlLxqj1S%2FiO4TI0Wo7ilAo%2FKKWWF4guuNDexj8EOOynSp1yImB%2BZf2Fua3O44W4eEXAMPLE33333&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20170621T231808Z&X-Amz-SignedHeaders=host&X-Amz-Expires=900&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE%2F20170621%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Signature=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY" } ], "NextToken": "eyJhd3NBY2NvdW50SWQiOnsicyI6IjMwMjc3NjAxNjM5OCJ9LCJidWlsZElkIjp7InMiOiJidWlsZC01NWYxZTZmMS1jY2FlLTQ3YTctOWI5ZS1iYjFkYTQwMjEXAMPLE2" }`For more information, see [Debug GameLift Fleet Issues](https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-creating-debug.html)in the*Amazon GameLift Developer Guide*.- 
                    For API details, see [DescribeFleetEvents](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-fleet-events.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-fleet-port-settings`.

- **AWS CLI**
- 
            
                    **To view inbound connection permissions for a fleet**The following `describe-fleet-port-settings`example retrieves connection settings for a specified fleet.`aws gamelift describe-fleet-port-settings \ --fleet-id``arn:aws:gamelift:us-west-2::fleet/fleet-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`Output: `{ "InboundPermissions": [ { "FromPort": 33400, "ToPort": 33500, "IpRange": "0.0.0.0/0", "Protocol": "UDP" }, { "FromPort": 1900, "ToPort": 2000, "IpRange": "0.0.0.0/0", "Protocol": "TCP" } ] }`For more information, see [Setting Up GameLift Fleets](https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-intro.html)in the*Amazon GameLift Developer Guide*.- 
                    For API details, see [DescribeFleetPortSettings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-fleet-port-settings.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-fleet-utilization`.

- **AWS CLI**
- 
            
                    **Example1: To view usage data for a list of fleets**The following `describe-fleet-utilization`example retrieves current usage information for one specified fleet.`aws gamelift describe-fleet-utilization \ --fleet-ids``arn:aws:gamelift:us-west-2::fleet/fleet-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`Output: `{ "FleetUtilization": [ { "FleetId": "fleet-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "ActiveServerProcessCount": 100, "ActiveGameSessionCount": 62, "CurrentPlayerSessionCount": 329, "MaximumPlayerSessionCount": 1000 } ] }`**Example2: To request usage data for all fleets**The following `describe-fleet-utilization`returns fleet usage data for all fleets with any status. This example uses pagination parameters to return data for two fleets at a time.`aws gamelift describe-fleet-utilization \ --limit``2`Output: `{ "FleetUtilization": [ { "FleetId": "fleet-1111aaaa-22bb-33cc-44dd-5555eeee66ff", "ActiveServerProcessCount": 100, "ActiveGameSessionCount": 13, "CurrentPlayerSessionCount": 98, "MaximumPlayerSessionCount": 1000 }, { "FleetId": "fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa", "ActiveServerProcessCount": 100, "ActiveGameSessionCount": 62, "CurrentPlayerSessionCount": 329, "MaximumPlayerSessionCount": 1000 } ], "NextToken": "eyJhd3NBY2NvdW50SWQiOnsicyI6IjMwMjc3NjAxNjM5OCJ9LCJidWlsZElkIjp7InMiOiJidWlsZC01NWYxZTZmMS1jY2FlLTQ3YTctOWI5ZS1iYjFkYTQwMjEXAMPLE2" }`Call the command a second time, passing the `NextToken`value as the argument to the`--next-token`parameter to see the next two results.`aws gamelift describe-fleet-utilization \ --limit``2`\ --next-token`eyJhd3NBY2NvdW50SWQiOnsicyI6IjMwMjc3NjAxNjM5OCJ9LCJidWlsZElkIjp7InMiOiJidWlsZC01NWYxZTZmMS1jY2FlLTQ3YTctOWI5ZS1iYjFkYTQwMjEXAMPLE2`Repeat until the response no longer includes a `NextToken`value in the output.For more information, see [GameLift Metrics for Fleets](https://docs.aws.amazon.com/gamelift/latest/developerguide/monitoring-cloudwatch.html#gamelift-metrics-fleet)in the*Amazon GameLift Developer Guide*.- 
                    For API details, see [DescribeFleetUtilization](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-fleet-utilization.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-game-session-queues`.

- **AWS CLI**
- 
            
                    **To view game session queues**The following `describe-game-session-queues`example retrieves properties for two specified queues.`aws gamelift describe-game-session-queues \ --names``MegaFrogRace-NA``MegaFrogRace-EU`Output: `{ "GameSessionQueues": [{ "Destinations": [{ "DestinationArn": "arn:aws:gamelift:us-west-2::fleet/fleet-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111" }, { "DestinationArn": "arn:aws:gamelift:us-west-2::fleet/fleet-a1b2c3d4-5678-90ab-cdef-EXAMPLE22222" } ], "Name": "MegaFrogRace-NA", "TimeoutInSeconds": 600, "GameSessionQueueArn": "arn:aws:gamelift:us-west-2::gamesessionqueue/MegaFrogRace-NA", "PlayerLatencyPolicies": [{ "MaximumIndividualPlayerLatencyMilliseconds": 200 }, { "MaximumIndividualPlayerLatencyMilliseconds": 100, "PolicyDurationSeconds": 60 } ], "FilterConfiguration": { "AllowedLocations": ["us-west-2", "ap-south-1", "us-east-1"] }, "PriorityConfiguration": { "PriorityOrder": ["LOCATION", "FLEET_TYPE", "DESTINATION"], "LocationOrder": ["us-west-2", "ap-south-1", "us-east-1"] } }, { "Destinations": [{ "DestinationArn": "arn:aws:gamelift:eu-west-3::fleet/fleet-a1b2c3d4-5678-90ab-cdef-EXAMPLE22222" }], "Name": "MegaFrogRace-EU", "TimeoutInSeconds": 600, "GameSessionQueueArn": "arn:aws:gamelift:us-west-2::gamesessionqueue/MegaFrogRace-EU" } ] }`For more information, see [Using Multi-Region Queues](https://docs.aws.amazon.com/gamelift/latest/developerguide/queues-intro.html)in the*Amazon GameLift Developer Guide*.- 
                    For API details, see [DescribeGameSessionQueues](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-game-session-queues.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-runtime-configuration`.

- **AWS CLI**
- 
            
                    **To request the runtime configuration for a fleet**The following `describe-runtime-configuration`example retrieves details about the current runtime configuration for a specified fleet.`aws gamelift describe-runtime-configuration \ --fleet-id``fleet-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`Output: `{ "RuntimeConfiguration": { "ServerProcesses": [ { "LaunchPath": "C:\game\Bin64.Release.Dedicated\MegaFrogRace_Server.exe", "Parameters": "+gamelift_start_server", "ConcurrentExecutions": 3 }, { "LaunchPath": "C:\game\Bin64.Release.Dedicated\MegaFrogRace_Server.exe", "Parameters": "+gamelift_start_server +debug", "ConcurrentExecutions": 1 } ], "MaxConcurrentGameSessionActivations": 2147483647, "GameSessionActivationTimeoutSeconds": 300 } }`For more information, see [Run Multiple Processes on a Fleet](https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-multiprocess.html)in the*Amazon GameLift Developer Guide*.- 
                    For API details, see [DescribeRuntimeConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-runtime-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-builds`.

- **AWS CLI**
- 
            
                    **Example1: To get a list of custom game builds**The following `list-builds`example retrieves properties for all game server builds in the current Region. The sample request illustrates how to use the pagination parameters,`Limit`and`NextToken`, to retrieve the results in sequential sets. The first command retrieves the first two builds. Because there are more than two available, the response includes a`NextToken`to indicate that more results are available.`aws gamelift list-builds \ --limit``2`Output: `{ "Builds": [ { "BuildArn": "arn:aws:gamelift:us-west-2::build/build-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "BuildId": "build-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "CreationTime": 1495664528.723, "Name": "My_Game_Server_Build_One", "OperatingSystem": "WINDOWS_2012", "SizeOnDisk": 8567781, "Status": "READY", "Version": "12345.678" }, { "BuildArn": "arn:aws:gamelift:us-west-2::build/build-a1b2c3d4-5678-90ab-cdef-EXAMPLE22222", "BuildId": "build-a1b2c3d4-5678-90ab-cdef-EXAMPLE22222", "CreationTime": 1495528748.555, "Name": "My_Game_Server_Build_Two", "OperatingSystem": "AMAZON_LINUX_2", "SizeOnDisk": 8567781, "Status": "FAILED", "Version": "23456.789" } ], "NextToken": "eyJhd3NBY2NvdW50SWQiOnsicyI6IjMwMjc3NjAxNjM5OCJ9LCJidWlsZElkIjp7InMiOiJidWlsZC01NWYxZTZmMS1jY2FlLTQ3YTctOWI5ZS1iYjFkYTQwMjJEXAMPLE=" }`You can then call the command again with the `--next-token`parameter as follows to see the next two builds.`aws gamelift list-builds \ --limit``2`--next-token`eyJhd3NBY2NvdW50SWQiOnsicyI6IjMwMjc3NjAxNjM5OCJ9LCJidWlsZElkIjp7InMiOiJidWlsZC01NWYxZTZmMS1jY2FlLTQ3YTctOWI5ZS1iYjFkYTQwMjJEXAMPLE=`Repeat until the response doesn't include a `NextToken`value.**Example2: To get a list of custom game builds in failure status**The following `list-builds`example retrieves properties for all game server builds in the current region that currently have status FAILED.`aws gamelift list-builds \ --status``FAILED`Output: `{ "Builds": [ { "BuildArn": "arn:aws:gamelift:us-west-2::build/build-a1b2c3d4-5678-90ab-cdef-EXAMPLE22222", "BuildId": "build-a1b2c3d4-5678-90ab-cdef-EXAMPLE22222", "CreationTime": 1495528748.555, "Name": "My_Game_Server_Build_Two", "OperatingSystem": "AMAZON_LINUX_2", "SizeOnDisk": 8567781, "Status": "FAILED", "Version": "23456.789" } ] }`- 
                    For API details, see [ListBuilds](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/list-builds.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-fleets`.

- **AWS CLI**
- 
            
                    **Example1: To get a list of all fleets in a Region**The following `list-fleets`example displays the fleet IDs of all fleets in the current Region. This example uses pagination parameters to retrieve two fleet IDs at a time. The response includes a`next-token`attribute, which indicates that there are more results to retrieve.`aws gamelift list-fleets \ --limit``2`Output: `{ "FleetIds": [ "fleet-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "fleet-a1b2c3d4-5678-90ab-cdef-EXAMPLE22222" ], "NextToken": "eyJhd3NBY2NvdW50SWQiOnsicyI6IjMwMjc3NjAxNjM5OCJ9LCJidWlsZElkIjp7InMiOiJidWlsZC01NWYxZTZmMS1jY2FlLTQ3YTctOWI5ZS1iYjFkYTQwMjJEXAMPLE=" }`You can pass the `NextToken`value from the previous response in the next command, as shown here to get the next two results.`aws gamelift list-fleets \ --limit``2`\ --next-token`eyJhd3NBY2NvdW50SWQiOnsicyI6IjMwMjc3NjAxNjM5OCJ9LCJidWlsZElkIjp7InMiOiJidWlsZC00NDRlZjQxZS1hM2I1LTQ2NDYtODJmMy0zYzI4ZTgxNjVjEXAMPLE=`**Example2: To get a list of all fleets in a Region with a specific build or script**The following `list-builds`example retrieves the IDs of fleets that are deployed with the specified game build. If you're working with Realtime Servers, you can provide a script ID in place of a build ID. Because this example does not specify the limit parameter, the results can include up to 16 fleet IDs.`aws gamelift list-fleets \ --build-id``build-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`Output: `{ "FleetIds": [ "fleet-a1b2c3d4-5678-90ab-cdef-EXAMPLE22222", "fleet-a1b2c3d4-5678-90ab-cdef-EXAMPLE33333", "fleet-a1b2c3d4-5678-90ab-cdef-EXAMPLE44444" ] }`- 
                    For API details, see [ListFleets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/list-fleets.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `request-upload-credentials`.

- **AWS CLI**
- 
            
                    **To refresh access credentials for uploading a build**The following `create-build`example obtains new, valid access credentials for uploading a GameLift build file to an Amazon S3 location. Credentials have a limited life span. You get the build ID from the response to the original`CreateBuild`request.`aws gamelift request-upload-credentials \ --build-id``build-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`Output: `{ "StorageLocation": { "Bucket": "gamelift-builds-us-west-2", "Key": "123456789012/build-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111" }, "UploadCredentials": { "AccessKeyId": "AKIAIOSFODNN7EXAMPLE", "SecretAccessKey": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY", "SessionToken": "AgoGb3JpZ2luENz...EXAMPLETOKEN==" } }`For more information, see [Upload a Custom Server Build to GameLift](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-build-cli-uploading.html)in the*Amazon GameLift Developer Guide*.- 
                    For API details, see [RequestUploadCredentials](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/request-upload-credentials.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-fleet-actions`.

- **AWS CLI**
- 
            
                    **To restart fleet automatic scaling activity**The following `start-fleet-actions`example resumes the use of all scaling policies that are defined for the specified fleet but were stopped by calling``stop-fleet-actions``. After starting, the scaling policies immediately begin tracking their respective metrics.`aws gamelift start-fleet-actions \ --fleet-id``fleet-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`\ --actions`AUTO_SCALING`This command produces no output. - 
                    For API details, see [StartFleetActions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/start-fleet-actions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `stop-fleet-actions`.

- **AWS CLI**
- 
            
                    **To stop a fleet's automatic scaling activity**The following `stop-fleet-actions`example stops the use of all scaling policies that are defined for the specified fleet. After the policies are suspended, fleet capacity remains at the same active instance count unless you adjust it manually.`aws gamelift start-fleet-actions \ --fleet-id``fleet-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`\ --actions`AUTO_SCALING`This command produces no output. - 
                    For API details, see [StopFleetActions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/stop-fleet-actions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-build`.

- **AWS CLI**
- 
            
                    **To update a custom game build**The following `update-build`example changes the name and version information that is associated with a specified build resource. The returned build object verifies that the changes were made successfully.`aws gamelift update-build \ --build-id``build-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`\ --name`MegaFrogRaceServer.NA.east`\ --build-version`12345.east`Output: `{ "Build": { "BuildArn": "arn:aws:gamelift:us-west-2::build/build-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "BuildId": "build-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "CreationTime": 1496708916.18, "Name": "MegaFrogRaceServer.NA.east", "OperatingSystem": "AMAZON_LINUX_2", "SizeOnDisk": 1304924, "Status": "READY", "Version": "12345.east" } }`For more information, see [Update Your Build Files](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-build-cli-uploading.html#gamelift-build-cli-uploading-update-build-files)in the*Amazon GameLift Developer Guide*.- 
                    For API details, see [UpdateBuild](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/update-build.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-game-session-queue`.

- **AWS CLI**
- 
            
                    **To update a game session queue configuration**The following `update-game-session-queue`example adds a new destination and updates the player latency policies for an existing game session queue.`aws gamelift update-game-session-queue \ --name``MegaFrogRace-NA`\ --destinations`file://destinations.json`\ --player-latency-policies`file://latency-policies.json`Contents of `destinations.json`:`{ "Destinations": [ {"DestinationArn": "arn:aws:gamelift:us-west-2::fleet/fleet-1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d"}, {"DestinationArn": "arn:aws:gamelift:us-east-1::fleet/fleet-5c6d3c4d-5e6f-7a8b-9c0d-1e2f3a4b5a2b"}, {"DestinationArn": "arn:aws:gamelift:us-east-1::alias/alias-11aa22bb-3c4d-5e6f-000a-1111aaaa22bb"} ] }`Contents of `latency-policies.json`:`{ "PlayerLatencyPolicies": [ {"MaximumIndividualPlayerLatencyMilliseconds": 200}, {"MaximumIndividualPlayerLatencyMilliseconds": 150, "PolicyDurationSeconds": 120}, {"MaximumIndividualPlayerLatencyMilliseconds": 100, "PolicyDurationSeconds": 120} ] }`Output: `{ "GameSessionQueue": { "Destinations": [ {"DestinationArn": "arn:aws:gamelift:us-west-2::fleet/fleet-1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d"}, {"DestinationArn": "arn:aws:gamelift:us-east-1::fleet/fleet-5c6d3c4d-5e6f-7a8b-9c0d-1e2f3a4b5a2b"}, {"DestinationArn": "arn:aws:gamelift:us-east-1::alias/alias-11aa22bb-3c4d-5e6f-000a-1111aaaa22bb"} ], "GameSessionQueueArn": "arn:aws:gamelift:us-west-2:111122223333:gamesessionqueue/MegaFrogRace-NA", "Name": "MegaFrogRace-NA", "TimeoutInSeconds": 600, "PlayerLatencyPolicies": [ {"MaximumIndividualPlayerLatencyMilliseconds": 200}, {"MaximumIndividualPlayerLatencyMilliseconds": 150, "PolicyDurationSeconds": 120}, {"MaximumIndividualPlayerLatencyMilliseconds": 100, "PolicyDurationSeconds": 120} ] } }`For more information, see [Using Multi-Region Queues](https://docs.aws.amazon.com/gamelift/latest/developerguide/queues-intro.html)in the*Amazon GameLift Developer Guide*.- 
                    For API details, see [UpdateGameSessionQueue](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/update-game-session-queue.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `upload-build`.

- **AWS CLI**
- 
            
                    **Example1: To upload a Linux game server build**The following `upload-build`example uploads Linux game server build files from a file directory to the GameLift service and creates a build resource.`aws gamelift upload-build \ --name``MegaFrogRaceServer.NA`\ --build-version`2.0.1`\ --build-root`~/MegaFrogRace_Server/release-na`\ --operating-system`AMAZON_LINUX_2`--server-sdk-version`4.0.2`Output: `Uploading ~/MegaFrogRace_Server/release-na: 16.0 KiB / 74.6 KiB (21.45%) Uploading ~/MegaFrogRace_Server/release-na: 32.0 KiB / 74.6 KiB (42.89%) Uploading ~/MegaFrogRace_Server/release-na: 48.0 KiB / 74.6 KiB (64.34%) Uploading ~/MegaFrogRace_Server/release-na: 64.0 KiB / 74.6 KiB (85.79%) Uploading ~/MegaFrogRace_Server/release-na: 74.6 KiB / 74.6 KiB (100.00%) Successfully uploaded ~/MegaFrogRace_Server/release-na to AWS GameLift Build ID: build-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`**Example2: To upload a Windows game server build**The following `upload-build`example uploads Windows game server build files from a directory to the GameLift service and creates a build record.`aws gamelift upload-build \ --name``MegaFrogRaceServer.NA`\ --build-version`2.0.1`\ --build-root C:\MegaFrogRace_Server\release-na \ --operating-system`WINDOWS_2012`--server-sdk-version`4.0.2`Output: `Uploading C:\MegaFrogRace_Server\release-na: 16.0 KiB / 74.6 KiB (21.45%) Uploading C:\MegaFrogRace_Server\release-na: 32.0 KiB / 74.6 KiB (42.89%) Uploading C:\MegaFrogRace_Server\release-na: 48.0 KiB / 74.6 KiB (64.34%) Uploading C:\MegaFrogRace_Server\release-na: 64.0 KiB / 74.6 KiB (85.79%) Uploading C:\MegaFrogRace_Server\release-na: 74.6 KiB / 74.6 KiB (100.00%) Successfully uploaded C:\MegaFrogRace_Server\release-na to AWS GameLift Build ID: build-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`For more information, see [Upload a Custom Server Build to GameLift](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-build-cli-uploading.html)in the*Amazon GameLift Developer Guide*.- 
                    For API details, see [UploadBuild](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/upload-build.html)in*AWS CLI Command Reference*.
 
-