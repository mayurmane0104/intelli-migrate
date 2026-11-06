# CloudWatch Network Monitoring examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_networkmonitor_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_networkmonitor_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with CloudWatch Network Monitoring.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `create-monitor`.

- **AWS CLI**
- 
            
                    **Example 1: To create a network monitor with an aggregation period**The following `create-monitor`example creates a monitor named`Example_NetworkMonitor`with an`aggregationPeriod`set to`30`seconds. The initial`state`of the monitor will be`INACTIVE`because there are no probes associated with it. The state changes to`ACTIVE`only when probes are added. You can use the[update-monitor](https://docs.aws.amazon.com/cli/latest/reference/networkmonitor/update-monitor.html)or[create-probe](https://docs.aws.amazon.com/cli/latest/reference/networkmonitor/create-probe.html)commands to add probes to this monitor.`aws networkmonitor create-monitor \ --monitor-name``Example_NetworkMonitor`\ --aggregation-period`30`Output: `{ "monitorArn": "arn:aws:networkmonitor:region:111122223333:monitor/Example_NetworkMonitor", "monitorName": "Example_NetworkMonitor", "state": "INACTIVE", "aggregationPeriod": 30, "tags": {} }`For more information, see [How Amazon CloudWatch Network Monitor Works](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/nw-monitor-how-it-works.html)in the*Amazon CloudWatch User Guide*.**Example 2: To create a network monitor with a probe using TCP and also includes tags**The following `create-monitor`example creates a monitor named`Example_NetworkMonitor`. The command also creates one probe that uses the`ICMP`protocol and includes tags. Since no`aggregationPeriod`is passed in the request,`60`seconds is set as the default. The`state`of the monitor with the probe will be`PENDING`until the monitor is`ACTIVE`. This might take several minutes, at which point the`state`will change to`ACTIVE`, and you can start viewing CloudWatch metrics.`aws networkmonitor create-monitor \ --monitor-name``Example_NetworkMonitor`\ --probes`sourceArn=arn:aws:ec2:region:111122223333:subnet/subnet-id,destination=10.0.0.100,destinationPort=80,protocol=TCP,packetSize=56,probeTags={Name=Probe1}`\ --tags`Monitor=Monitor1`Output: `{ "monitorArn": "arn:aws:networkmonitor:region111122223333:monitor/Example_NetworkMonitor", "monitorName": "Example_NetworkMonitor", "state": "PENDING", "aggregationPeriod": 60, "tags": { "Monitor": "Monitor1" } }`For more information, see [How Amazon CloudWatch Network Monitor Works](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/nw-monitor-how-it-works.html)in the*Amazon CloudWatch User Guide*.**Example 3: To create a network monitor with a probe using ICMP and also includes tags**The following `create-monitor`example creates a monitor named`Example_NetworkMonitor`with an`aggregationPeriod`of`30`seconds. The command also creates one probe that uses the`ICMP`protocol and includes tags. Since no`aggregationPeriod`is passed in the request,`60`seconds is set as the default. The`state`of the monitor with the probe will be`PENDING`until the monitor is`ACTIVE`. This might take several minutes, at which point the`state`will change to`ACTIVE`, and you can start viewing CloudWatch metrics.`aws networkmonitor create-monitor \ --monitor-name``Example_NetworkMonitor`\ --aggregation-period`30`\ --probes`sourceArn=arn:aws:ec2:region111122223333:subnet/subnet-id,destination=10.0.0.100,protocol=ICMP,packetSize=56,probeTags={Name=Probe1}`\ --tags`Monitor=Monitor1`Output: `{ "monitorArn": "arn:aws:networkmonitor:region:111122223333:monitor/Example_NetworkMonitor", "monitorName": "Example_NetworkMonitor", "state": "PENDING", "aggregationPeriod": 30, "tags": { "Monitor": "Monitor1" } }`For more information, see [How Amazon CloudWatch Network Monitor Works](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/nw-monitor-how-it-works.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [CreateMonitor](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmonitor/create-monitor.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-probe`.

- **AWS CLI**
- 
            
                    **Example 1: To create a probe that uses TCP and add it to a network monitor**The following `create-probe`example creates a probe that uses the`TCP``protocol`and adds the probe to a monitor named`Example_NetworkMonitor`. Once created, the`state`of the monitor with the probe will be`PENDING`until the monitor is`ACTIVE`. This might take several minutes, at which point the state will change to`ACTIVE`, and you can start viewing CloudWatch metrics.`aws networkmonitor create-probe \ --monitor-name``Example_NetworkMonitor`\ --probe`sourceArn=arn:aws:ec2:region:111122223333:subnet/subnet-id,destination=10.0.0.100,destinationPort=80,protocol=TCP,packetSize=56,tags={Name=Probe1}`Output: `{ "probeId": "probe-12345", "probeArn": "arn:aws:networkmonitor:region:111122223333:probe/probe-12345", "destination": "10.0.0.100", "destinationPort": 80, "packetSize": 56, "addressFamily": "IPV4", "vpcId": "vpc-12345", "state": "PENDING", "createdAt": "2024-03-29T12:41:57.314000-04:00", "modifiedAt": "2024-03-29T12:41:57.314000-04:00", "tags": { "Name": "Probe1" } }`**Example 2: To create a probe that uses probe using ICMP and add it to a network monitor**The following `create-probe`example creates a probe that uses the`ICMP``protocol`and adds the probe to a monitor named`Example_NetworkMonitor`. Once created, the`state`of the monitor with the probe will be`PENDING`until the monitor is`ACTIVE`. This might take several minutes, at which point the state will change to`ACTIVE`, and you can start viewing CloudWatch metrics.`aws networkmonitor create-probe \ --monitor-name``Example_NetworkMonitor`\ --probe`sourceArn=arn:aws:ec2:region:012345678910:subnet/subnet-id,destination=10.0.0.100,protocol=ICMP,packetSize=56,tags={Name=Probe1}`Output: `{ "probeId": "probe-12345", "probeArn": "arn:aws:networkmonitor:region:111122223333:probe/probe-12345", "destination": "10.0.0.100", "packetSize": 56, "addressFamily": "IPV4", "vpcId": "vpc-12345", "state": "PENDING", "createdAt": "2024-03-29T12:44:02.452000-04:00", "modifiedAt": "2024-03-29T12:44:02.452000-04:00", "tags": { "Name": "Probe1" } }`For more information, see [How Amazon CloudWatch Network Monitor Works](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/nw-monitor-how-it-works.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [CreateProbe](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmonitor/create-probe.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-monitor`.

- **AWS CLI**
- 
            
                    **To delete a monitor**The following `delete-monitor`example deletes a monitor named`Example_NetworkMonitor`.`aws networkmonitor delete-monitor \ --monitor-name``Example_NetworkMonitor`This command produces no output. For more information, see [How Amazon CloudWatch Network Monitor Works](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/nw-monitor-how-it-works.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [DeleteMonitor](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmonitor/delete-monitor.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-probe`.

- **AWS CLI**
- 
            
                    **To delete a probe**The following `delete-probe`example deletes a probe with the ID`probe-12345`from a network monitor named`Example_NetworkMonitor`.`aws networkmonitor delete-probe \ --monitor-name``Example_NetworkMonitor`\ --probe-id`probe-12345`This command produces no output. For more information, see [How Amazon CloudWatch Network Monitor Works](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/nw-monitor-how-it-works.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [DeleteProbe](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmonitor/delete-probe.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-monitor`.

- **AWS CLI**
- 
            
                    **To get monitor information**The following `get-monitor`example gets information about a monitor named`Example_NetworkMonitor`.`aws networkmonitor get-monitor \ --monitor-name``Example_NetworkMonitor`Output: `{ "monitorArn": "arn:aws:networkmonitor:region:012345678910:monitor/Example_NetworkMonitor", "monitorName": "Example_NetworkMonitor", "state": "ACTIVE", "aggregationPeriod": 60, "tags": {}, "probes": [], "createdAt": "2024-04-01T17:58:07.211000-04:00", "modifiedAt": "2024-04-01T17:58:07.211000-04:00" }`For more information, see [How Amazon CloudWatch Network Monitor Works](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/nw-monitor-how-it-works.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [GetMonitor](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmonitor/get-monitor.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-probe`.

- **AWS CLI**
- 
            
                    **To view probe details**The following `get-probe`example returns details about a probe with the`probeID``probe-12345`that's associated with a monitor named`Example_NetworkMonitor`.`aws networkmonitor get-probe \ --monitor-name``Example_NetworkMonitor`\ --probe-id`probe-12345`Output: `{ "probeId": "probe-12345", "probeArn": "arn:aws:networkmonitor:region:012345678910:probe/probe-12345", "sourceArn": "arn:aws:ec2:region:012345678910:subnet/subnet-12345", "destination": "10.0.0.100", "destinationPort": 80, "protocol": "TCP", "packetSize": 56, "addressFamily": "IPV4", "vpcId": "vpc-12345", "state": "ACTIVE", "createdAt": "2024-03-29T12:41:57.314000-04:00", "modifiedAt": "2024-03-29T12:42:28.610000-04:00", "tags": { "Name": "Probe1" } }`For more information, see [How Amazon CloudWatch Network Monitor Works](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/nw-monitor-how-it-works.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [GetProbe](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmonitor/get-probe.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-monitors`.

- **AWS CLI**
- 
            
                    **Example 1: To list all monitors (single monitor)**The following `list-monitors`example returns a list of only a single monitor. The monitor's`state`is`ACTIVE`and it has an`aggregationPeriod`of 60 seconds.`aws networkmonitor list-monitors`Output: `{ "monitors": [{ "monitorArn": "arn:aws:networkmonitor:region:012345678910:monitor/Example_NetworkMonitor", "monitorName": "Example_NetworkMonitor", "state": "ACTIVE", "aggregationPeriod": 60, "tags": { "Monitor": "Monitor1" } } ] }`For more information, see [How Amazon CloudWatch Network Monitor Works](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/nw-monitor-how-it-works.html)in the*Amazon CloudWatch User Guide*.**Example 2: To list all monitors (multiple monitors)**The following `list-monitors`example returns a list of three monitors. The`state`of one monitor is`ACTIVE`and generating CloudWatch metrics. The states of the other two monitors are`INACTIVE`and not generating CloudWatch metrics. All three monitors use an`aggregationPeriod`of 60 seconds.`aws networkmonitor list-monitors`Output: `{ "monitors": [ { "monitorArn": "arn:aws:networkmonitor:us-east-1:111122223333:monitor/Example_NetworkMonitor", "monitorName": "Example_NetworkMonitor", "state": "INACTIVE", "aggregationPeriod": 60, "tags": {} }, { "monitorArn": "arn:aws:networkmonitor:us-east-1:111122223333:monitor/Example_NetworkMonitor2", "monitorName": "Example_NetworkMonitor2", "state": "ACTIVE", "aggregationPeriod": 60, "tags": { "Monitor": "Monitor1" } }, { "monitorArn": "arn:aws:networkmonitor:us-east-1:111122223333:monitor/TestNetworkMonitor_CLI", "monitorName": "TestNetworkMonitor_CLI", "state": "INACTIVE", "aggregationPeriod": 60, "tags": {} } ] }`For more information, see [How Amazon CloudWatch Network Monitor Works](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/nw-monitor-how-it-works.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [ListMonitors](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmonitor/list-monitors.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-tags-for-resource`.

- **AWS CLI**
- 
            
                    **To list tags for a resource**The following `list-tags-for-resource`example returns a list of the tags for a monitor named`Example_NetworkMonitor`.`aws networkmonitor list-tags-for-resource \ --resource-arn``arn:aws:networkmonitor:region:012345678910:monitor/Example_NetworkMonitor`Output: `{ "tags": { "Environment": "Dev", "Application": "PetStore" } }`For more information, see [How Amazon CloudWatch Network Monitor Works](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/nw-monitor-how-it-works.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmonitor/list-tags-for-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag-resource`.

- **AWS CLI**
- 
            
                    **To tag a resource**The following `tag-resource`example tags a monitor named`Example_NetworkMonitor`with`Environment=Dev`and`Application=PetStore`tags.`aws networkmonitor tag-resource \ --resource-arn``arn:aws:networkmonitor:region:012345678910:monitor/Example_NetworkMonitor`\ --tags`Environment=Dev,Application=PetStore`This command produces no output. For more information, see [How Amazon CloudWatch Network Monitor Works](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/nw-monitor-how-it-works.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmonitor/tag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag-resource`.

- **AWS CLI**
- 
            
                    **To untag a resource**The following `untag-resource`example removes a`tag-keys`parameter with the key-value pair of`Environment Application`from its association with a monitor named`Example_NetworkMonitor`.`aws networkmonitor untag-resource \ --resource-arn``arn:aws:networkmonitor:region:012345678910:monitor/Example_NetworkMonitor`\ --tag-keys`Environment``Application`This command produces no output. For more information, see [How Amazon CloudWatch Network Monitor Works](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/nw-monitor-how-it-works.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [UntagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmonitor/untag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-monitor`.

- **AWS CLI**
- 
            
                    **To update a monitor**The following `update-monitor`example changes a monitor's`aggregationPeriod`from`60`seconds to`30`seconds.`aws networkmonitor update-monitor \ --monitor-name``Example_NetworkMonitor`\ --aggregation-period`30`Output: `{ "monitorArn": "arn:aws:networkmonitor:region:012345678910:monitor/Example_NetworkMonitor", "monitorName": "Example_NetworkMonitor", "state": "PENDING", "aggregationPeriod": 30, "tags": { "Monitor": "Monitor1" } }`For more information, see [How Amazon CloudWatch Network Monitor Works](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/nw-monitor-how-it-works.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [UpdateMonitor](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmonitor/update-monitor.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-probe`.

- **AWS CLI**
- 
            
                    **To update a probe**The following `update-probe`example updates a probe's original`destination`IP address and also updates the`packetSize`to`60`.`aws networkmonitor update-probe \ --monitor-name``Example_NetworkMonitor`\ --probe-id`probe-12345`\ --destination`10.0.0.150`\ --packet-size`60`Output: `{ "probeId": "probe-12345", "probeArn": "arn:aws:networkmonitor:region:012345678910:probe/probe-12345", "sourceArn": "arn:aws:ec2:region:012345678910:subnet/subnet-12345", "destination": "10.0.0.150", "destinationPort": 80, "protocol": "TCP", "packetSize": 60, "addressFamily": "IPV4", "vpcId": "vpc-12345", "state": "PENDING", "createdAt": "2024-03-29T12:41:57.314000-04:00", "modifiedAt": "2024-03-29T13:52:23.115000-04:00", "tags": { "Name": "Probe1" } }`For more information, see [How Amazon CloudWatch Network Monitor Works](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/nw-monitor-how-it-works.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [UpdateProbe](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmonitor/update-probe.html)in*AWS CLI Command Reference*.
 
-