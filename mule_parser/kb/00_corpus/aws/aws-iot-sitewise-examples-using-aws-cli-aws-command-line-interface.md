# AWS IoT SiteWise examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_iotsitewise_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_iotsitewise_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with AWS IoT SiteWise.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `associate-assets`.

- **AWS CLI**
- 
            
                    **To associate a child asset to a parent asset**The following `associate-assets`example associates a wind turbine asset to a wind farm asset, where the wind turbine asset model exists as a hierarchy in the wind farm asset model.`aws iotsitewise associate-assets \ --asset-id``a1b2c3d4-5678-90ab-cdef-44444EXAMPLE`\ --hierarchy-id`a1b2c3d4-5678-90ab-cdef-77777EXAMPLE`\ --child-asset-id`a1b2c3d4-5678-90ab-cdef-33333EXAMPLE`This command produces no output. For more information, see [Associating assets](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/add-associated-assets.html)in the*AWS IoT SiteWise User Guide*.- 
                    For API details, see [AssociateAssets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/associate-assets.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `batch-associate-project-assets`.

- **AWS CLI**
- 
            
                    **To associate an asset to a project**The following `batch-associate-project-assets`example associates a wind farm asset to a project.`aws iotsitewise batch-associate-project-assets \ --project-id``a1b2c3d4-5678-90ab-cdef-eeeeeEXAMPLE`\ --asset-ids`a1b2c3d4-5678-90ab-cdef-44444EXAMPLE`This command produces no output. For more information, see [Adding assets to projects](https://docs.aws.amazon.com/iot-sitewise/latest/appguide/add-assets-to-projects-sd.html)in the*AWS IoT SiteWise Monitor Application Guide*.- 
                    For API details, see [BatchAssociateProjectAssets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/batch-associate-project-assets.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `batch-disassociate-project-assets`.

- **AWS CLI**
- 
            
                    **To disassociate an asset from a project**The following `batch-disassociate-project-assets`example disassociates a wind farm asset from a project.`aws iotsitewise batch-disassociate-project-assets \ --project-id``a1b2c3d4-5678-90ab-cdef-eeeeeEXAMPLE`\ --asset-ids`a1b2c3d4-5678-90ab-cdef-44444EXAMPLE`This command produces no output. For more information, see [Adding assets to projects](https://docs.aws.amazon.com/iot-sitewise/latest/appguide/add-assets-to-projects-sd.html)in the*AWS IoT SiteWise Monitor Application Guide*.- 
                    For API details, see [BatchDisassociateProjectAssets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/batch-disassociate-project-assets.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `batch-put-asset-property-value`.

- **AWS CLI**
- 
            
                    **To send data to asset properties**The following `batch-put-asset-property-value`example sends power and temperature data to the asset properties identified by property aliases.`aws iotsitewise batch-put-asset-property-value \ --cli-input-json``file://batch-put-asset-property-value.json`Contents of `batch-put-asset-property-value.json`:`{ "entries": [ { "entryId": "1575691200-company-windfarm-3-turbine-7-power", "propertyAlias": "company-windfarm-3-turbine-7-power", "propertyValues": [ { "value": { "doubleValue": 4.92 }, "timestamp": { "timeInSeconds": 1575691200 }, "quality": "GOOD" } ] }, { "entryId": "1575691200-company-windfarm-3-turbine-7-temperature", "propertyAlias": "company-windfarm-3-turbine-7-temperature", "propertyValues": [ { "value": { "integerValue": 38 }, "timestamp": { "timeInSeconds": 1575691200 } } ] } ] }`Output: `{ "errorEntries": [] }`For more information, see [Ingesting data using the AWS IoT SiteWise API](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/ingest-api.html)in the*AWS IoT SiteWise User Guide*.- 
                    For API details, see [BatchPutAssetPropertyValue](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/batch-put-asset-property-value.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-access-policy`.

- **AWS CLI**
- 
            
                    **Example 1: To grant a user administrative access to a portal**The following `create-access-policy`example creates an access policy that grants a user administrative access to a web portal for a wind farm company.`aws iotsitewise create-access-policy \ --cli-input-json``file://create-portal-administrator-access-policy.json`Contents of `create-portal-administrator-access-policy.json`:`{ "accessPolicyIdentity": { "user": { "id": "a1b2c3d4e5-a1b2c3d4-5678-90ab-cdef-bbbbbEXAMPLE" } }, "accessPolicyPermission": "ADMINISTRATOR", "accessPolicyResource": { "portal": { "id": "a1b2c3d4-5678-90ab-cdef-aaaaaEXAMPLE" } } }`Output: `{ "accessPolicyId": "a1b2c3d4-5678-90ab-cdef-cccccEXAMPLE", "accessPolicyArn": "arn:aws:iotsitewise:us-west-2:123456789012:access-policy/a1b2c3d4-5678-90ab-cdef-cccccEXAMPLE" }`For more information, see [Adding or removing portal administrators](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/administer-portals.html#portal-change-admins)in the*AWS IoT SiteWise User Guide*.**Example 2: To grant a user read-only access to a project**The following `create-access-policy`example creates an access policy that grants a user read-only access to a wind farm project.`aws iotsitewise create-access-policy \ --cli-input-json``file://create-project-viewer-access-policy.json`Contents of `create-project-viewer-access-policy.json`:`{ "accessPolicyIdentity": { "user": { "id": "a1b2c3d4e5-a1b2c3d4-5678-90ab-cdef-bbbbbEXAMPLE" } }, "accessPolicyPermission": "VIEWER", "accessPolicyResource": { "project": { "id": "a1b2c3d4-5678-90ab-cdef-eeeeeEXAMPLE" } } }`Output: `{ "accessPolicyId": "a1b2c3d4-5678-90ab-cdef-dddddEXAMPLE", "accessPolicyArn": "arn:aws:iotsitewise:us-west-2:123456789012:access-policy/a1b2c3d4-5678-90ab-cdef-dddddEXAMPLE" }`For more information, see [Assigning project viewers](https://docs.aws.amazon.com/iot-sitewise/latest/appguide/assign-project-viewers.html)in the*AWS IoT SiteWise Monitor Application Guide*.- 
                    For API details, see [CreateAccessPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/create-access-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-asset-model`.

- **AWS CLI**
- 
            
                    **To create an asset model**The following `create-asset-model`example creates an asset model that defines a wind turbine with the following properties:Serial number - The serial number of a wind turbineGenerated power - The generated power data stream from a wind turbineTemperature C - The temperature data stream from a wind turbine in CelsiusTemperature F - The mapped temperature data points from Celsius to Fahrenheit `aws iotsitewise create-asset-model \ --cli-input-json``file://create-wind-turbine-model.json`Contents of `create-wind-turbine-model.json`:`{ "assetModelName": "Wind Turbine Model", "assetModelDescription": "Represents a wind turbine", "assetModelProperties": [ { "name": "Serial Number", "dataType": "STRING", "type": { "attribute": {} } }, { "name": "Generated Power", "dataType": "DOUBLE", "unit": "kW", "type": { "measurement": {} } }, { "name": "Temperature C", "dataType": "DOUBLE", "unit": "Celsius", "type": { "measurement": {} } }, { "name": "Temperature F", "dataType": "DOUBLE", "unit": "Fahrenheit", "type": { "transform": { "expression": "temp_c * 9 / 5 + 32", "variables": [ { "name": "temp_c", "value": { "propertyId": "Temperature C" } } ] } } }, { "name": "Total Generated Power", "dataType": "DOUBLE", "unit": "kW", "type": { "metric": { "expression": "sum(power)", "variables": [ { "name": "power", "value": { "propertyId": "Generated Power" } } ], "window": { "tumbling": { "interval": "1h" } } } } } ] }`Output: `{ "assetModelId": "a1b2c3d4-5678-90ab-cdef-11111EXAMPLE", "assetModelArn": "arn:aws:iotsitewise:us-west-2:123456789012:asset-model/a1b2c3d4-5678-90ab-cdef-11111EXAMPLE", "assetModelStatus": { "state": "CREATING" } }`For more information, see [Defining asset models](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/define-models.html)in the*AWS IoT SiteWise User Guide*.- 
                    For API details, see [CreateAssetModel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/create-asset-model.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-asset`.

- **AWS CLI**
- 
            
                    **To create an asset**The following `create-asset`example creates a wind turbine asset from a wind turbine asset model.`aws iotsitewise create-asset \ --asset-model-id``a1b2c3d4-5678-90ab-cdef-11111EXAMPLE`\ --asset-name`"Wind Turbine 1"`Output: `{ "assetId": "a1b2c3d4-5678-90ab-cdef-33333EXAMPLE", "assetArn": "arn:aws:iotsitewise:us-west-2:123456789012:asset/a1b2c3d4-5678-90ab-cdef-33333EXAMPLE", "assetStatus": { "state": "CREATING" } }`For more information, see [Creating assets](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/create-assets.html)in the*AWS IoT SiteWise User Guide*.- 
                    For API details, see [CreateAsset](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/create-asset.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-dashboard`.

- **AWS CLI**
- 
            
                    **To create a dashboard**The following `create-dashboard`example creates a dashboard with a line chart that displays total generated power for a wind farm.`aws iotsitewise create-dashboard \ --project-id``a1b2c3d4-5678-90ab-cdef-eeeeeEXAMPLE`\ --dashboard-name`"Wind Farm"`\ --dashboard-definition`file://create-wind-farm-dashboard.json`Contents of `create-wind-farm-dashboard.json`:`{ "widgets": [ { "type": "monitor-line-chart", "title": "Generated Power", "x": 0, "y": 0, "height": 3, "width": 3, "metrics": [ { "label": "Power", "type": "iotsitewise", "assetId": "a1b2c3d4-5678-90ab-cdef-44444EXAMPLE", "propertyId": "a1b2c3d4-5678-90ab-cdef-99999EXAMPLE" } ] } ] }`Output: `{ "dashboardId": "a1b2c3d4-5678-90ab-cdef-fffffEXAMPLE", "dashboardArn": "arn:aws:iotsitewise:us-west-2:123456789012:dashboard/a1b2c3d4-5678-90ab-cdef-fffffEXAMPLE" }`For more information, see [Creating dashboards (CLI)](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/create-dashboards-using-aws-cli.html)in the*AWS IoT SiteWise User Guide*.- 
                    For API details, see [CreateDashboard](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/create-dashboard.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-gateway`.

- **AWS CLI**
- 
            
                    **To create a gateway**The following `create-gateway`example creates a gateway that runs on AWS IoT Greengrass.`aws iotsitewise create-gateway \ --gateway-name``ExampleCorpGateway`\ --gateway-platform`greengrass={groupArn=arn:aws:greengrass:us-west-2:123456789012:/greengrass/groups/a1b2c3d4-5678-90ab-cdef-1b1b1EXAMPLE}`Output: `{ "gatewayId": "a1b2c3d4-5678-90ab-cdef-1a1a1EXAMPLE", "gatewayArn": "arn:aws:iotsitewise:us-west-2:123456789012:gateway/a1b2c3d4-5678-90ab-cdef-1a1a1EXAMPLE" }`For more information, see [Configuring a gateway](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/configure-gateway.html)in the*AWS IoT SiteWise User Guide*.- 
                    For API details, see [CreateGateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/create-gateway.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-portal`.

- **AWS CLI**
- 
            
                    **To create a portal**The following `create-portal`example creates a web portal for a wind farm company. You can create portals only in the same Region where you enabled AWS Single Sign-On.`aws iotsitewise create-portal \ --portal-name``WindFarmPortal`\ --portal-description`"A portal that contains wind farm projects for Example Corp."`\ --portal-contact-email`support@example.com`\ --role-arn`arn:aws:iam::123456789012:role/service-role/MySiteWiseMonitorServiceRole`Output: `{ "portalId": "a1b2c3d4-5678-90ab-cdef-aaaaaEXAMPLE", "portalArn": "arn:aws:iotsitewise:us-west-2:123456789012:portal/a1b2c3d4-5678-90ab-cdef-aaaaaEXAMPLE", "portalStartUrl": "https://a1b2c3d4-5678-90ab-cdef-aaaaaEXAMPLE.app.iotsitewise.aws", "portalStatus": { "state": "CREATING" }, "ssoApplicationId": "ins-a1b2c3d4-EXAMPLE" }`For more information, see [Getting started with AWS IoT SiteWise Monitor](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/monitor-getting-started.html)in the*AWS IoT SiteWise User Guide*and[Enabling AWS SSO](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/monitor-getting-started.html#monitor-enable-sso)in the*AWS IoT SiteWise User Guide*..- 
                    For API details, see [CreatePortal](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/create-portal.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-project`.

- **AWS CLI**
- 
            
                    **To create a project**The following `create-project`example creates a wind farm project.`aws iotsitewise create-project \ --portal-id``a1b2c3d4-5678-90ab-cdef-aaaaaEXAMPLE`\ --project-name`"Wind Farm 1"`\ --project-description`"Contains asset visualizations for Wind Farm #1 for Example Corp."`Output: `{ "projectId": "a1b2c3d4-5678-90ab-cdef-eeeeeEXAMPLE", "projectArn": "arn:aws:iotsitewise:us-west-2:123456789012:project/a1b2c3d4-5678-90ab-cdef-eeeeeEXAMPLE" }`For more information, see [Creating projects](https://docs.aws.amazon.com/iot-sitewise/latest/appguide/create-projects.html)in the*AWS IoT SiteWise Monitor Application Guide*.- 
                    For API details, see [CreateProject](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/create-project.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-access-policy`.

- **AWS CLI**
- 
            
                    **To revoke a user's access to a project or portal**The following `delete-access-policy`example deletes an access policy that grants a user administrative access to a portal.`aws iotsitewise delete-access-policy \ --access-policy-id``a1b2c3d4-5678-90ab-cdef-cccccEXAMPLE`This command produces no output. For more information, see [Adding or removing portal administrators](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/administer-portals.html#portal-change-admins)in the*AWS IoT SiteWise User Guide*.- 
                    For API details, see [DeleteAccessPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/delete-access-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-asset-model`.

- **AWS CLI**
- 
            
                    **To delete an asset model**The following `delete-asset-model`example deletes a wind turbine asset model.`aws iotsitewise delete-asset-model \ --asset-model-id``a1b2c3d4-5678-90ab-cdef-11111EXAMPLE`Output: `{ "assetModelStatus": { "state": "DELETING" } }`For more information, see [Deleting asset models](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/delete-assets-and-models.html#delete-asset-models)in the*AWS IoT SiteWise User Guide*.- 
                    For API details, see [DeleteAssetModel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/delete-asset-model.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-asset`.

- **AWS CLI**
- 
            
                    **To delete an asset**The following `delete-asset`example deletes a wind turbine asset.`aws iotsitewise delete-asset \ --asset-id``a1b2c3d4-5678-90ab-cdef-33333EXAMPLE`Output: `{ "assetStatus": { "state": "DELETING" } }`For more information, see [Deleting assets](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/delete-assets-and-models.html#delete-assets)in the*AWS IoT SiteWise User Guide*.- 
                    For API details, see [DeleteAsset](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/delete-asset.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-dashboard`.

- **AWS CLI**
- 
            
                    **To delete a dashboard**The following `delete-dashboard`example deletes a wind turbine dashboard.`aws iotsitewise delete-dashboard \ --dashboard-id``a1b2c3d4-5678-90ab-cdef-fffffEXAMPLE`This command produces no output. For more information, see [Deleting dashboards](https://docs.aws.amazon.com/iot-sitewise/latest/appguide/delete-dashboards.html)in the*AWS IoT SiteWise Monitor Application Guide*.- 
                    For API details, see [DeleteDashboard](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/delete-dashboard.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-gateway`.

- **AWS CLI**
- 
            
                    **To delete a gateway**The following `delete-gateway`example deletes a gateway.`aws iotsitewise delete-gateway \ --gateway-id``a1b2c3d4-5678-90ab-cdef-1a1a1EXAMPLE`This command produces no output. For more information, see [Ingesting data using a gateway](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/gateways.html)in the*AWS IoT SiteWise User Guide*.- 
                    For API details, see [DeleteGateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/delete-gateway.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-portal`.

- **AWS CLI**
- 
            
                    **To delete a portal**The following `delete-portal`example deletes a web portal for a wind farm company.`aws iotsitewise delete-portal \ --portal-id``a1b2c3d4-5678-90ab-cdef-aaaaaEXAMPLE`Output: `{ "portalStatus": { "state": "DELETING" } }`For more information, see [Deleting a portal](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/administer-portals.html#portal-delete-portal)in the*AWS IoT SiteWise User Guide*.- 
                    For API details, see [DeletePortal](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/delete-portal.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-project`.

- **AWS CLI**
- 
            
                    **To delete a project**The following `delete-project`example deletes a wind farm project.`aws iotsitewise delete-project \ --project-id``a1b2c3d4-5678-90ab-cdef-eeeeeEXAMPLE`This command produces no output. For more information, see [Deleting projects](https://docs.aws.amazon.com/iot-sitewise/latest/appguide/delete-projects.html)in the*AWS IoT SiteWise Monitor Application Guide*.- 
                    For API details, see [DeleteProject](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/delete-project.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-access-policy`.

- **AWS CLI**
- 
            
                    **To describe an access policy**The following `describe-access-policy`example describes an access policy that grants a user administrative access to a web portal for a wind farm company.`aws iotsitewise describe-access-policy \ --access-policy-id``a1b2c3d4-5678-90ab-cdef-cccccEXAMPLE`Output: `{ "accessPolicyId": "a1b2c3d4-5678-90ab-cdef-cccccEXAMPLE", "accessPolicyArn": "arn:aws:iotsitewise:us-west-2:123456789012:access-policy/a1b2c3d4-5678-90ab-cdef-cccccEXAMPLE", "accessPolicyIdentity": { "user": { "id": "a1b2c3d4e5-a1b2c3d4-5678-90ab-cdef-bbbbbEXAMPLE" } }, "accessPolicyResource": { "portal": { "id": "a1b2c3d4-5678-90ab-cdef-aaaaaEXAMPLE" } }, "accessPolicyPermission": "ADMINISTRATOR", "accessPolicyCreationDate": "2020-02-20T22:35:15.552880124Z", "accessPolicyLastUpdateDate": "2020-02-20T22:35:15.552880124Z" }`For more information, see [Adding or removing portal administrators](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/administer-portals.html#portal-change-admins)in the*AWS IoT SiteWise User Guide*.- 
                    For API details, see [DescribeAccessPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/describe-access-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-asset-model`.

- **AWS CLI**
- 
            
                    **To describe an asset model**The following `describe-asset-model`example describes a wind farm asset model.`aws iotsitewise describe-asset-model \ --asset-model-id``a1b2c3d4-5678-90ab-cdef-22222EXAMPLE`Output: `{ "assetModelId": "a1b2c3d4-5678-90ab-cdef-22222EXAMPLE", "assetModelArn": "arn:aws:iotsitewise:us-west-2:123456789012:asset-model/a1b2c3d4-5678-90ab-cdef-22222EXAMPLE", "assetModelName": "Wind Farm Model", "assetModelDescription": "Represents a wind farm that comprises many wind turbines", "assetModelProperties": [ { "id": "a1b2c3d4-5678-90ab-cdef-99999EXAMPLE", "name": "Total Generated Power", "dataType": "DOUBLE", "unit": "kW", "type": { "metric": { "expression": "sum(power)", "variables": [ { "name": "power", "value": { "propertyId": "a1b2c3d4-5678-90ab-cdef-66666EXAMPLE", "hierarchyId": "a1b2c3d4-5678-90ab-cdef-77777EXAMPLE" } } ], "window": { "tumbling": { "interval": "1h" } } } } }, { "id": "a1b2c3d4-5678-90ab-cdef-88888EXAMPLE", "name": "Region", "dataType": "STRING", "type": { "attribute": { "defaultValue": " " } } } ], "assetModelHierarchies": [ { "id": "a1b2c3d4-5678-90ab-cdef-77777EXAMPLE", "name": "Wind Turbines", "childAssetModelId": "a1b2c3d4-5678-90ab-cdef-11111EXAMPLE" } ], "assetModelCreationDate": 1575671284.0, "assetModelLastUpdateDate": 1575671988.0, "assetModelStatus": { "state": "ACTIVE" } }`For more information, see [Describing a specific asset model](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/discover-asset-resources.html#describe-asset-model)in the*AWS IoT SiteWise User Guide*.- 
                    For API details, see [DescribeAssetModel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/describe-asset-model.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-asset-property`.

- **AWS CLI**
- 
            
                    **To describe an asset property**The following `describe-asset-property`example describes a wind farm asset's total generated power property.`aws iotsitewise describe-asset-property \ --asset-id``a1b2c3d4-5678-90ab-cdef-44444EXAMPLE`\ --property-id`a1b2c3d4-5678-90ab-cdef-99999EXAMPLE`Output: `{ "assetId": "a1b2c3d4-5678-90ab-cdef-44444EXAMPLE", "assetName": "Wind Farm 1", "assetModelId": "a1b2c3d4-5678-90ab-cdef-22222EXAMPLE", "assetProperty": { "id": "a1b2c3d4-5678-90ab-cdef-99999EXAMPLE", "name": "Total Generated Power", "notification": { "topic": "$aws/sitewise/asset-models/a1b2c3d4-5678-90ab-cdef-22222EXAMPLE/assets/a1b2c3d4-5678-90ab-cdef-44444EXAMPLE/properties/a1b2c3d4-5678-90ab-cdef-99999EXAMPLE", "state": "DISABLED" }, "dataType": "DOUBLE", "unit": "kW", "type": { "metric": { "expression": "sum(power)", "variables": [ { "name": "power", "value": { "propertyId": "a1b2c3d4-5678-90ab-cdef-66666EXAMPLE", "hierarchyId": "a1b2c3d4-5678-90ab-cdef-77777EXAMPLE" } } ], "window": { "tumbling": { "interval": "1h" } } } } } }`For more information, see [Describing a specific asset property](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/discover-asset-resources.html#describe-asset-property)in the*AWS IoT SiteWise User Guide*.- 
                    For API details, see [DescribeAssetProperty](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/describe-asset-property.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-asset`.

- **AWS CLI**
- 
            
                    **To describe an asset**The following `describe-asset`example describes a wind farm asset.`aws iotsitewise describe-asset \ --asset-id``a1b2c3d4-5678-90ab-cdef-44444EXAMPLE`Output: `{ "assetId": "a1b2c3d4-5678-90ab-cdef-44444EXAMPLE", "assetArn": "arn:aws:iotsitewise:us-west-2:123456789012:asset/a1b2c3d4-5678-90ab-cdef-44444EXAMPLE", "assetName": "Wind Farm 1", "assetModelId": "a1b2c3d4-5678-90ab-cdef-22222EXAMPLE", "assetProperties": [ { "id": "a1b2c3d4-5678-90ab-cdef-88888EXAMPLE", "name": "Region", "dataType": "STRING" }, { "id": "a1b2c3d4-5678-90ab-cdef-99999EXAMPLE", "name": "Total Generated Power", "dataType": "DOUBLE", "unit": "kW" } ], "assetHierarchies": [ { "id": "a1b2c3d4-5678-90ab-cdef-77777EXAMPLE", "name": "Wind Turbines" } ], "assetCreationDate": 1575672453.0, "assetLastUpdateDate": 1575672453.0, "assetStatus": { "state": "ACTIVE" } }`For more information, see [Describing a specific asset](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/discover-asset-resources.html#describe-asset)in the*AWS IoT SiteWise User Guide*.- 
                    For API details, see [DescribeAsset](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/describe-asset.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-dashboard`.

- **AWS CLI**
- 
            
                    **To describe a dashboard**The following `describe-dashboard`example describes the specified wind farm dashboard.`aws iotsitewise describe-dashboard \ --dashboard-id``a1b2c3d4-5678-90ab-cdef-fffffEXAMPLE`Output: `{ "dashboardId": "a1b2c3d4-5678-90ab-cdef-fffffEXAMPLE", "dashboardArn": "arn:aws:iotsitewise:us-west-2:123456789012:dashboard/a1b2c3d4-5678-90ab-cdef-fffffEXAMPLE", "dashboardName": "Wind Farm", "projectId": "a1b2c3d4-5678-90ab-cdef-eeeeeEXAMPLE", "dashboardDefinition": "{\"widgets\":[{\"type\":\"monitor-line-chart\",\"title\":\"Generated Power\",\"x\":0,\"y\":0,\"height\":3,\"width\":3,\"metrics\":[{\"label\":\"Power\",\"type\":\"iotsitewise\",\"assetId\":\"a1b2c3d4-5678-90ab-cdef-44444EXAMPLE\",\"propertyId\":\"a1b2c3d4-5678-90ab-cdef-99999EXAMPLE\"}]}]}", "dashboardCreationDate": "2020-05-01T20:32:12.228476348Z", "dashboardLastUpdateDate": "2020-05-01T20:32:12.228476348Z" }`For more information, see [Viewing dashboards](https://docs.aws.amazon.com/iot-sitewise/latest/appguide/view-dashboards.html)in the*AWS IoT SiteWise Monitor Application Guide*.- 
                    For API details, see [DescribeDashboard](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/describe-dashboard.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-gateway-capability-configuration`.

- **AWS CLI**
- 
            
                    **To describe a gateway capability**The following `describe-gateway-capability-configuration`example describes an OPC-UA source capability.`aws iotsitewise describe-gateway-capability-configuration \ --gateway-id``a1b2c3d4-5678-90ab-cdef-1a1a1EXAMPLE`\ --capability-namespace`"iotsitewise:opcuacollector:1"`Output: `{ "gatewayId": "a1b2c3d4-5678-90ab-cdef-1a1a1EXAMPLE", "capabilityNamespace": "iotsitewise:opcuacollector:1", "capabilityConfiguration": "{\"sources\":[{\"name\":\"Wind Farm #1\",\"endpoint\":{\"certificateTrust\":{\"type\":\"TrustAny\"},\"endpointUri\":\"opc.tcp://203.0.113.0:49320\",\"securityPolicy\":\"BASIC256\",\"messageSecurityMode\":\"SIGN_AND_ENCRYPT\",\"identityProvider\":{\"type\":\"Username\",\"usernameSecretArn\":\"arn:aws:secretsmanager:us-east-1:123456789012:secret:greengrass-factory1-auth-3QNDmM\"},\"nodeFilterRules\":[]},\"measurementDataStreamPrefix\":\"\"}]}", "capabilitySyncStatus": "IN_SYNC" }`For more information, see [Configuring data sources](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/configure-sources.html)in the*AWS IoT SiteWise User Guide*.- 
                    For API details, see [DescribeGatewayCapabilityConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/describe-gateway-capability-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-gateway`.

- **AWS CLI**
- 
            
                    **To describe a gateway**The following `describe-gateway`example describes a gateway.`aws iotsitewise describe-gateway \ --gateway-id``a1b2c3d4-5678-90ab-cdef-1a1a1EXAMPLE`Output: `{ "gatewayId": "a1b2c3d4-5678-90ab-cdef-1a1a1EXAMPLE", "gatewayName": "ExampleCorpGateway", "gatewayArn": "arn:aws:iotsitewise:us-west-2:123456789012:gateway/a1b2c3d4-5678-90ab-cdef-1a1a1EXAMPLE", "gatewayPlatform": { "greengrass": { "groupArn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/groups/a1b2c3d4-5678-90ab-cdef-1b1b1EXAMPLE" } }, "gatewayCapabilitySummaries": [ { "capabilityNamespace": "iotsitewise:opcuacollector:1", "capabilitySyncStatus": "IN_SYNC" } ], "creationDate": 1588369971.457, "lastUpdateDate": 1588369971.457 }`For more information, see [Ingesting data using a gateway](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/gateways.html)in the*AWS IoT SiteWise User Guide*.- 
                    For API details, see [DescribeGateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/describe-gateway.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-logging-options`.

- **AWS CLI**
- 
            
                    **To retrieve the current AWS IoT SiteWise logging options**The following `describe-logging-options`example retrieves the current AWS IoT SiteWise logging options for your AWS account in the current Region.`aws iotsitewise describe-logging-options`Output: `{ "loggingOptions": { "level": "INFO" } }`For more information, see [Monitoring AWS IoT SiteWise with Amazon CloudWatch Logs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/monitor-cloudwatch-logs.html)in the*AWS IoT SiteWise User Guide*.- 
                    For API details, see [DescribeLoggingOptions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/describe-logging-options.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-portal`.

- **AWS CLI**
- 
            
                    **To describe a portal**The following `describe-portal`example describes a web portal for a wind farm company.`aws iotsitewise describe-portal \ --portal-id``a1b2c3d4-5678-90ab-cdef-aaaaaEXAMPLE`Output: `{ "portalId": "a1b2c3d4-5678-90ab-cdef-aaaaaEXAMPLE", "portalArn": "arn:aws:iotsitewise:us-west-2:123456789012:portal/a1b2c3d4-5678-90ab-cdef-aaaaaEXAMPLE", "portalName": "WindFarmPortal", "portalDescription": "A portal that contains wind farm projects for Example Corp.", "portalClientId": "E-a1b2c3d4e5f6_a1b2c3d4e5f6EXAMPLE", "portalStartUrl": "https://a1b2c3d4-5678-90ab-cdef-aaaaaEXAMPLE.app.iotsitewise.aws", "portalContactEmail": "support@example.com", "portalStatus": { "state": "ACTIVE" }, "portalCreationDate": "2020-02-04T23:01:52.90248068Z", "portalLastUpdateDate": "2020-02-04T23:01:52.90248078Z", "roleArn": "arn:aws:iam::123456789012:role/MySiteWiseMonitorServiceRole" }`For more information, see [Administering your portals](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/administer-portals.html)in the*AWS IoT SiteWise User Guide*.- 
                    For API details, see [DescribePortal](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/describe-portal.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-project`.

- **AWS CLI**
- 
            
                    **To describe a project**The following `describe-project`example describes a wind farm project.`aws iotsitewise describe-project \ --project-id``a1b2c3d4-5678-90ab-cdef-eeeeeEXAMPLE`Output: `{ "projectId": "a1b2c3d4-5678-90ab-cdef-eeeeeEXAMPLE", "projectArn": "arn:aws:iotsitewise:us-west-2:123456789012:project/a1b2c3d4-5678-90ab-cdef-eeeeeEXAMPLE", "projectName": "Wind Farm 1", "portalId": "a1b2c3d4-5678-90ab-cdef-aaaaaEXAMPLE", "projectDescription": "Contains asset visualizations for Wind Farm #1 for Example Corp.", "projectCreationDate": "2020-02-20T21:58:43.362246001Z", "projectLastUpdateDate": "2020-02-20T21:58:43.362246095Z" }`For more information, see [Viewing project details](https://docs.aws.amazon.com/iot-sitewise/latest/appguide/view-project-details.html)in the*AWS IoT SiteWise Monitor Application Guide*.- 
                    For API details, see [DescribeProject](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/describe-project.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disassociate-assets`.

- **AWS CLI**
- 
            
                    **To disassociate a child asset from a parent asset**The following `disassociate-assets`example disassociates a wind turbine asset from a wind farm asset.`aws iotsitewise disassociate-assets \ --asset-id``a1b2c3d4-5678-90ab-cdef-44444EXAMPLE`\ --hierarchy-id`a1b2c3d4-5678-90ab-cdef-77777EXAMPLE`\ --child-asset-id`a1b2c3d4-5678-90ab-cdef-33333EXAMPLE`This command produces no output. For more information, see [Associating assets](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/add-associated-assets.html)in the*AWS IoT SiteWise User Guide*.- 
                    For API details, see [DisassociateAssets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/disassociate-assets.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-asset-property-aggregates`.

- **AWS CLI**
- 
            
                    **To retrieve an asset property's aggregated average and count values**The following `get-asset-property-aggregates`example retrieves a wind turbine asset's average total power and count of total power data points for a 1 hour period in time.`aws iotsitewise get-asset-property-aggregates \ --asset-id``a1b2c3d4-5678-90ab-cdef-33333EXAMPLE`\ --property-id`a1b2c3d4-5678-90ab-cdef-66666EXAMPLE`\ --start-date`1580849400`\ --end-date`1580853000`\ --aggregate-types`AVERAGE``COUNT`\ --resolution`1h`Output: `{ "aggregatedValues": [ { "timestamp": 1580850000.0, "quality": "GOOD", "value": { "average": 8723.46538886233, "count": 12.0 } } ] }`For more information, see [Querying asset property aggregates](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/query-industrial-data.html#aggregates)in the*AWS IoT SiteWise User Guide*.- 
                    For API details, see [GetAssetPropertyAggregates](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/get-asset-property-aggregates.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-asset-property-value-history`.

- **AWS CLI**
- 
            
                    **To retrieve an asset property's historical values**The following `get-asset-property-value-history`example retrieves a wind turbine asset's total power values for a 20 minute period in time.`aws iotsitewise get-asset-property-value-history \ --asset-id``a1b2c3d4-5678-90ab-cdef-33333EXAMPLE`\ --property-id`a1b2c3d4-5678-90ab-cdef-66666EXAMPLE`\ --start-date`1580851800`\ --end-date`1580853000`Output: `{ "assetPropertyValueHistory": [ { "value": { "doubleValue": 7217.787046814844 }, "timestamp": { "timeInSeconds": 1580852100, "offsetInNanos": 0 }, "quality": "GOOD" }, { "value": { "doubleValue": 6941.242811875451 }, "timestamp": { "timeInSeconds": 1580852400, "offsetInNanos": 0 }, "quality": "GOOD" }, { "value": { "doubleValue": 6976.797662266717 }, "timestamp": { "timeInSeconds": 1580852700, "offsetInNanos": 0 }, "quality": "GOOD" }, { "value": { "doubleValue": 6890.8677520453875 }, "timestamp": { "timeInSeconds": 1580853000, "offsetInNanos": 0 }, "quality": "GOOD" } ] }`For more information, see [Querying historical asset property values](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/query-industrial-data.html#historical-values)in the*AWS IoT SiteWise User Guide*.- 
                    For API details, see [GetAssetPropertyValueHistory](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/get-asset-property-value-history.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-asset-property-value`.

- **AWS CLI**
- 
            
                    **To retrieve an asset property's current value**The following `get-asset-property-value`example retrieves a wind turbine asset's current total power.`aws iotsitewise get-asset-property-value \ --asset-id``a1b2c3d4-5678-90ab-cdef-33333EXAMPLE`\ --property-id`a1b2c3d4-5678-90ab-cdef-66666EXAMPLE`Output: `{ "propertyValue": { "value": { "doubleValue": 6890.8677520453875 }, "timestamp": { "timeInSeconds": 1580853000, "offsetInNanos": 0 }, "quality": "GOOD" } }`For more information, see [Querying current asset property values](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/query-industrial-data.html#current-values)in the*AWS IoT SiteWise User Guide*.- 
                    For API details, see [GetAssetPropertyValue](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/get-asset-property-value.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-access-policies`.

- **AWS CLI**
- 
            
                    **To list all access policies**The following `list-access-policies`example lists all access policies for a user who is a portal administrator.`aws iotsitewise list-access-policies \ --identity-type``USER`\ --identity-id`a1b2c3d4e5-a1b2c3d4-5678-90ab-cdef-bbbbbEXAMPLE`Output: `{ "accessPolicySummaries": [ { "id": "a1b2c3d4-5678-90ab-cdef-cccccEXAMPLE", "identity": { "user": { "id": "a1b2c3d4e5-a1b2c3d4-5678-90ab-cdef-bbbbbEXAMPLE" } }, "resource": { "portal": { "id": "a1b2c3d4-5678-90ab-cdef-aaaaaEXAMPLE" } }, "permission": "ADMINISTRATOR" } ] }`For more information, see [Administering your portals](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/administer-portals.html)in the*AWS IoT SiteWise User Guide*.- 
                    For API details, see [ListAccessPolicies](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/list-access-policies.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-asset-models`.

- **AWS CLI**
- 
            
                    **To list all asset models**The following `list-asset-models`example lists all asset models that are defined in your AWS account in the current Region.`aws iotsitewise list-asset-models`Output: `{ "assetModelSummaries": [ { "id": "a1b2c3d4-5678-90ab-cdef-22222EXAMPLE", "arn": "arn:aws:iotsitewise:us-west-2:123456789012:asset-model/a1b2c3d4-5678-90ab-cdef-22222EXAMPLE", "name": "Wind Farm Model", "description": "Represents a wind farm that comprises many wind turbines", "creationDate": 1575671284.0, "lastUpdateDate": 1575671988.0, "status": { "state": "ACTIVE" } }, { "id": "a1b2c3d4-5678-90ab-cdef-11111EXAMPLE", "arn": "arn:aws:iotsitewise:us-west-2:123456789012:asset-model/a1b2c3d4-5678-90ab-cdef-11111EXAMPLE", "name": "Wind Turbine Model", "description": "Represents a wind turbine manufactured by Example Corp", "creationDate": 1575671207.0, "lastUpdateDate": 1575686273.0, "status": { "state": "ACTIVE" } } ] }`For more information, see [Listing all asset models](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/discover-asset-resources.html#list-asset-models)in the*AWS IoT SiteWise User Guide*.- 
                    For API details, see [ListAssetModels](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/list-asset-models.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-assets`.

- **AWS CLI**
- 
            
                    **Example 1: To list all top-level assets**The following `list-assets`example lists all assets that are top-level in the asset hierarchy tree and defined in your AWS account in the current Region.`aws iotsitewise list-assets \ --filter``TOP_LEVEL`Output: `{ "assetSummaries": [ { "id": "a1b2c3d4-5678-90ab-cdef-44444EXAMPLE", "arn": "arn:aws:iotsitewise:us-west-2:123456789012:asset/a1b2c3d4-5678-90ab-cdef-44444EXAMPLE", "name": "Wind Farm 1", "assetModelId": "a1b2c3d4-5678-90ab-cdef-22222EXAMPLE", "creationDate": 1575672453.0, "lastUpdateDate": 1575672453.0, "status": { "state": "ACTIVE" }, "hierarchies": [ { "id": "a1b2c3d4-5678-90ab-cdef-77777EXAMPLE", "name": "Wind Turbines" } ] } ] }`For more information, see [Listing assets](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/discover-asset-resources.html#list-assets)in the*AWS IoT SiteWise User Guide*.**Example 2: To list all assets based on an asset model**The following `list-assets`example lists all assets based on an asset model and defined in your AWS account in the current Region.`aws iotsitewise list-assets \ --asset-model-id``a1b2c3d4-5678-90ab-cdef-11111EXAMPLE`Output: `{ "assetSummaries": [ { "id": "a1b2c3d4-5678-90ab-cdef-33333EXAMPLE", "arn": "arn:aws:iotsitewise:us-west-2:123456789012:asset/a1b2c3d4-5678-90ab-cdef-33333EXAMPLE", "name": "Wind Turbine 1", "assetModelId": "a1b2c3d4-5678-90ab-cdef-11111EXAMPLE", "creationDate": 1575671550.0, "lastUpdateDate": 1575686308.0, "status": { "state": "ACTIVE" }, "hierarchies": [] } ] }`For more information, see [Listing assets](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/discover-asset-resources.html#list-assets)in the*AWS IoT SiteWise User Guide*.- 
                    For API details, see [ListAssets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/list-assets.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-associated-assets`.

- **AWS CLI**
- 
            
                    **To list all assets associated to an asset in a specific hierarchy**The following `list-associated-assets`example lists all wind turbine assets associated to the specified wind farm asset.`aws iotsitewise list-associated-assets \ --asset-id``a1b2c3d4-5678-90ab-cdef-44444EXAMPLE`\ --hierarchy-id`a1b2c3d4-5678-90ab-cdef-77777EXAMPLE`Output: `{ "assetSummaries": [ { "id": "a1b2c3d4-5678-90ab-cdef-33333EXAMPLE", "arn": "arn:aws:iotsitewise:us-west-2:123456789012:asset/a1b2c3d4-5678-90ab-cdef-33333EXAMPLE", "name": "Wind Turbine 1", "assetModelId": "a1b2c3d4-5678-90ab-cdef-11111EXAMPLE", "creationDate": 1575671550.0, "lastUpdateDate": 1575686308.0, "status": { "state": "ACTIVE" }, "hierarchies": [] } ] }`For more information, see [Listing assets associated to a specific asset](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/discover-asset-resources.html#list-associated-assets)in the*AWS IoT SiteWise User Guide*.- 
                    For API details, see [ListAssociatedAssets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/list-associated-assets.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-dashboards`.

- **AWS CLI**
- 
            
                    **To list all dashboards in a project**The following `list-dashboards`example lists all dashboards that are defined in a project.`aws iotsitewise list-dashboards \ --project-id``a1b2c3d4-5678-90ab-cdef-eeeeeEXAMPLE`Output: `{ "dashboardSummaries": [ { "id": "a1b2c3d4-5678-90ab-cdef-fffffEXAMPLE", "name": "Wind Farm", "creationDate": "2020-05-01T20:32:12.228476348Z", "lastUpdateDate": "2020-05-01T20:32:12.228476348Z" } ] }`For more information, see [Viewing dashboards](https://docs.aws.amazon.com/iot-sitewise/latest/appguide/view-dashboards.html)in the*AWS IoT SiteWise Monitor Application Guide*.- 
                    For API details, see [ListDashboards](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/list-dashboards.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-gateways`.

- **AWS CLI**
- 
            
                    **To list all gateways**The following `list-gateways`example lists all gateways that are defined in your AWS account in the current Region.`aws iotsitewise list-gateways`Output: `{ "gatewaySummaries": [ { "gatewayId": "a1b2c3d4-5678-90ab-cdef-1a1a1EXAMPLE", "gatewayName": "ExampleCorpGateway", "gatewayCapabilitySummaries": [ { "capabilityNamespace": "iotsitewise:opcuacollector:1", "capabilitySyncStatus": "IN_SYNC" } ], "creationDate": 1588369971.457, "lastUpdateDate": 1588369971.457 } ] }`For more information, see [Ingesting data using a gateway](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/gateways.html)in the*AWS IoT SiteWise User Guide*.- 
                    For API details, see [ListGateways](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/list-gateways.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-portals`.

- **AWS CLI**
- 
            
                    **To list all portals**The following `list-portals`example lists all portals that are defined in your AWS account in the current Region.`aws iotsitewise list-portals`Output: `{ "portalSummaries": [ { "id": "a1b2c3d4-5678-90ab-cdef-aaaaaEXAMPLE", "name": "WindFarmPortal", "description": "A portal that contains wind farm projects for Example Corp.", "startUrl": "https://a1b2c3d4-5678-90ab-cdef-aaaaaEXAMPLE.app.iotsitewise.aws", "creationDate": "2020-02-04T23:01:52.90248068Z", "lastUpdateDate": "2020-02-04T23:01:52.90248078Z", "roleArn": "arn:aws:iam::123456789012:role/service-role/MySiteWiseMonitorServiceRole" } ] }`For more information, see [Administering your portals](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/administer-portals.html)in the*AWS IoT SiteWise User Guide*.- 
                    For API details, see [ListPortals](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/list-portals.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-project-assets`.

- **AWS CLI**
- 
            
                    **To list all assets associated to a project**The following `list-project-assets`example lists all assets that are associated to a wind farm project.`aws iotsitewise list-project-assets \ --project-id``a1b2c3d4-5678-90ab-cdef-eeeeeEXAMPLE`Output: `{ "assetIds": [ "a1b2c3d4-5678-90ab-cdef-44444EXAMPLE" ] }`For more information, see [Adding assets to projects](https://docs.aws.amazon.com/iot-sitewise/latest/appguide/add-assets-to-projects-sd.html)in the*AWS IoT SiteWise Monitor Application Guide*.- 
                    For API details, see [ListProjectAssets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/list-project-assets.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-projects`.

- **AWS CLI**
- 
            
                    **To list all projects in a portal**The following `list-projects`example lists all projects that are defined in a portal.`aws iotsitewise list-projects \ --portal-id``a1b2c3d4-5678-90ab-cdef-aaaaaEXAMPLE`Output: `{ "projectSummaries": [ { "id": "a1b2c3d4-5678-90ab-cdef-eeeeeEXAMPLE", "name": "Wind Farm 1", "description": "Contains asset visualizations for Wind Farm #1 for Example Corp.", "creationDate": "2020-02-20T21:58:43.362246001Z", "lastUpdateDate": "2020-02-20T21:58:43.362246095Z" } ] }`For more information, see [Viewing project details](https://docs.aws.amazon.com/iot-sitewise/latest/appguide/view-project-details.html)in the*AWS IoT SiteWise Monitor Application Guide*.- 
                    For API details, see [ListProjects](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/list-projects.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-tags-for-resource`.

- **AWS CLI**
- 
            
                    **To list all tags for a resource**The following `list-tags-for-resource`example lists all tags for a wind turbine asset.`aws iotsitewise list-tags-for-resource \ --resource-arn``arn:aws:iotsitewise:us-west-2:123456789012:asset/a1b2c3d4-5678-90ab-cdef-33333EXAMPLE`Output: `{ "tags": { "Owner": "richard-roe" } }`For more information, see [Tagging your resources](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html)in the*AWS IoT SiteWise User Guide*.- 
                    For API details, see [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/list-tags-for-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-logging-options`.

- **AWS CLI**
- 
            
                    **To specify the level of logging**The following `put-logging-options`example enables`INFO`level logging in AWS IoT SiteWise. Other levels include`DEBUG`and`OFF`.`aws iotsitewise put-logging-options \ --logging-options``level=INFO`This command produces no output. For more information, see [Monitoring AWS IoT SiteWise with Amazon CloudWatch Logs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/monitor-cloudwatch-logs.html)in the*AWS IoT SiteWise User Guide*.- 
                    For API details, see [PutLoggingOptions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/put-logging-options.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag-resource`.

- **AWS CLI**
- 
            
                    **To add a tag to a resource**The following `tag-resource`example adds an owner tag to a wind turbine asset. This lets you control access to the asset based on who owns it.`aws iotsitewise tag-resource \ --resource-arn``arn:aws:iotsitewise:us-west-2:123456789012:asset/a1b2c3d4-5678-90ab-cdef-33333EXAMPLE`\ --tags`Owner=richard-roe`This command produces no output. For more information, see [Tagging your resources](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html)in the*AWS IoT SiteWise User Guide*.- 
                    For API details, see [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/tag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag-resource`.

- **AWS CLI**
- 
            
                    **To remove a tag from a resource**The following `untag-resource`example removes an owner tag from a wind turbine asset.`aws iotsitewise untag-resource \ --resource-arn``arn:aws:iotsitewise:us-west-2:123456789012:asset/a1b2c3d4-5678-90ab-cdef-33333EXAMPLE`\ --tag-keys`Owner`This command produces no output. For more information, see [Tagging your resources](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html)in the*AWS IoT SiteWise User Guide*.- 
                    For API details, see [UntagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/untag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-access-policy`.

- **AWS CLI**
- 
            
                    **To grant a project viewer ownership of a project**The following `update-access-policy`example updates an access policy that grants a project viewer ownership of a project.`aws iotsitewise update-access-policy \ --access-policy-id``a1b2c3d4-5678-90ab-cdef-dddddEXAMPLE`\ --cli-input-json`file://update-project-viewer-access-policy.json`Contents of `update-project-viewer-access-policy.json`:`{ "accessPolicyIdentity": { "user": { "id": "a1b2c3d4e5-a1b2c3d4-5678-90ab-cdef-bbbbbEXAMPLE" } }, "accessPolicyPermission": "ADMINISTRATOR", "accessPolicyResource": { "project": { "id": "a1b2c3d4-5678-90ab-cdef-eeeeeEXAMPLE" } } }`This command produces no output. For more information, see [Assigning project owners](https://docs.aws.amazon.com/iot-sitewise/latest/appguide/assign-project-owners.html)in the*AWS IoT SiteWise Monitor Application Guide*.- 
                    For API details, see [UpdateAccessPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/update-access-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-asset-model`.

- **AWS CLI**
- 
            
                    **To update an asset model**The following `update-asset-model`example updates a wind farm asset model's description. This example includes the model's existing IDs and definitions, because`update-asset-model`overwrites the existing model with the new model.`aws iotsitewise update-asset-model \ --cli-input-json``file://update-wind-farm-model.json`Contents of `update-wind-farm-model.json`:`{ "assetModelName": "Wind Farm Model", "assetModelDescription": "Represents a wind farm that comprises many wind turbines", "assetModelProperties": [ { "id": "a1b2c3d4-5678-90ab-cdef-88888EXAMPLE", "name": "Region", "dataType": "STRING", "type": { "attribute": {} } }, { "id": "a1b2c3d4-5678-90ab-cdef-99999EXAMPLE", "name": "Total Generated Power", "dataType": "DOUBLE", "unit": "kW", "type": { "metric": { "expression": "sum(power)", "variables": [ { "name": "power", "value": { "hierarchyId": "a1b2c3d4-5678-90ab-cdef-77777EXAMPLE", "propertyId": "a1b2c3d4-5678-90ab-cdef-66666EXAMPLE" } } ], "window": { "tumbling": { "interval": "1h" } } } } } ], "assetModelHierarchies": [ { "id": "a1b2c3d4-5678-90ab-cdef-77777EXAMPLE", "name": "Wind Turbines", "childAssetModelId": "a1b2c3d4-5678-90ab-cdef-11111EXAMPLE" } ] }`Output: `{ "assetModelId": "a1b2c3d4-5678-90ab-cdef-22222EXAMPLE", "assetModelArn": "arn:aws:iotsitewise:us-west-2:123456789012:asset-model/a1b2c3d4-5678-90ab-cdef-22222EXAMPLE", "assetModelStatus": { "state": "CREATING" } }`For more information, see [Updating asset models](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/update-assets-and-models.html#update-asset-models)in the*AWS IoT SiteWise User Guide*.- 
                    For API details, see [UpdateAssetModel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/update-asset-model.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-asset-property`.

- **AWS CLI**
- 
            
                    **Example 1: To update an asset property's alias**The following `update-asset-property`example updates a wind turbine asset's power property alias.`aws iotsitewise update-asset-property \ --asset-id``a1b2c3d4-5678-90ab-cdef-33333EXAMPLE`\ --property-id`a1b2c3d4-5678-90ab-cdef-55555EXAMPLE`\ --property-alias`"/examplecorp/windfarm/1/turbine/1/power"`\ --property-notification-state`DISABLED`This command produces no output. For more information, see [Mapping industrial data streams to asset properties](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/connect-data-streams.html)in the*AWS IoT SiteWise User Guide*.**Example 2: To enable asset property notifications**The following `update-asset-property`example enables asset property update notifications for a wind turbine asset's power property. Property value updates are published to the MQTT topic`$aws/sitewise/asset-models/<assetModelId>/assets/<assetId>/properties/<propertyId>`, where each ID is replaced by the property, asset, and model ID of the asset property.`aws iotsitewise update-asset-property \ --asset-id``a1b2c3d4-5678-90ab-cdef-33333EXAMPLE`\ --property-id`a1b2c3d4-5678-90ab-cdef-66666EXAMPLE`\ --property-notification-state`ENABLED`\ --property-alias`"/examplecorp/windfarm/1/turbine/1/power"`This command produces no output. For more information, see [Interacting with other services](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/interact-with-other-services.html)in the*AWS IoT SiteWise User Guide*.- 
                    For API details, see [UpdateAssetProperty](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/update-asset-property.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-asset`.

- **AWS CLI**
- 
            
                    **To update an asset's name**The following `update-asset`example updates a wind turbine asset's name.`aws iotsitewise update-asset \ --asset-id``a1b2c3d4-5678-90ab-cdef-33333EXAMPLE`\ --asset-name`"Wind Turbine 2"`Output: `{ "assetStatus": { "state": "UPDATING" } }`For more information, see [Updating assets](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/update-assets-and-models.html#update-assets)in the*AWS IoT SiteWise User Guide*.- 
                    For API details, see [UpdateAsset](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/update-asset.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-dashboard`.

- **AWS CLI**
- 
            
                    **To update a dashboard**The following `update-dashboard`example changes the title of a dashboard's line chart that displays total generated power for a wind farm.`aws iotsitewise update-dashboard \ --dashboard-id``a1b2c3d4-5678-90ab-cdef-fffffEXAMPLE`\ --dashboard-name`"Wind Farm"`\ --dashboard-definition`file://update-wind-farm-dashboard.json`Contents of `update-wind-farm-dashboard.json`:`{ "widgets": [ { "type": "monitor-line-chart", "title": "Total Generated Power", "x": 0, "y": 0, "height": 3, "width": 3, "metrics": [ { "label": "Power", "type": "iotsitewise", "assetId": "a1b2c3d4-5678-90ab-cdef-44444EXAMPLE", "propertyId": "a1b2c3d4-5678-90ab-cdef-99999EXAMPLE" } ] } ] }`This command produces no output. For more information, see [Creating dashboards (CLI)](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/create-dashboards-using-aws-cli.html)in the*AWS IoT SiteWise User Guide*.- 
                    For API details, see [UpdateDashboard](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/update-dashboard.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-gateway-capability-configuration`.

- **AWS CLI**
- 
            
                    **To update a gateway capability**The following `update-gateway-capability-configuration`example configures an OPC-UA source with the following properties:Trusts any certificate.Uses the Basic256 algorithm to secure messages.Uses the SignAndEncrypt mode to secure connections.Uses authentication credentials stored in an AWS Secrets Manager secret. `aws iotsitewise update-gateway-capability-configuration \ --gateway-id``a1b2c3d4-5678-90ab-cdef-1a1a1EXAMPLE`\ --capability-namespace`"iotsitewise:opcuacollector:1"`\ --capability-configuration`file://opc-ua-capability-configuration.json`Contents of `opc-ua-capability-configuration.json`:`{ "sources": [ { "name": "Wind Farm #1", "endpoint": { "certificateTrust": { "type": "TrustAny" }, "endpointUri": "opc.tcp://203.0.113.0:49320", "securityPolicy": "BASIC256", "messageSecurityMode": "SIGN_AND_ENCRYPT", "identityProvider": { "type": "Username", "usernameSecretArn": "arn:aws:secretsmanager:us-west-2:123456789012:secret:greengrass-windfarm1-auth-1ABCDE" }, "nodeFilterRules": [] }, "measurementDataStreamPrefix": "" } ] }`Output: `{ "capabilityNamespace": "iotsitewise:opcuacollector:1", "capabilitySyncStatus": "OUT_OF_SYNC" }`For more information, see [Configuring data sources](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/configure-sources.html)in the*AWS IoT SiteWise User Guide*.- 
                    For API details, see [UpdateGatewayCapabilityConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/update-gateway-capability-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-gateway`.

- **AWS CLI**
- 
            
                    **To update a gateway's name**The following `update-gateway`example updates a gateway's name.`aws iotsitewise update-gateway \ --gateway-id``a1b2c3d4-5678-90ab-cdef-1a1a1EXAMPLE`\ --gateway-name`ExampleCorpGateway1`This command produces no output. For more information, see [Ingesting data using a gateway](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/gateways.html)in the*AWS IoT SiteWise User Guide*.- 
                    For API details, see [UpdateGateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/update-gateway.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-portal`.

- **AWS CLI**
- 
            
                    **To update a portal's details**The following `update-portal`example updates a web portal for a wind farm company.`aws iotsitewise update-portal \ --portal-id``a1b2c3d4-5678-90ab-cdef-aaaaaEXAMPLE`\ --portal-name`WindFarmPortal`\ --portal-description`"A portal that contains wind farm projects for Example Corp."`\ --portal-contact-email`support@example.com`\ --role-arn`arn:aws:iam::123456789012:role/MySiteWiseMonitorServiceRole`Output: `{ "portalStatus": { "state": "UPDATING" } }`For more information, see [Administering your portals](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/administer-portals.html)in the*AWS IoT SiteWise User Guide*.- 
                    For API details, see [UpdatePortal](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/update-portal.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-project`.

- **AWS CLI**
- 
            
                    **To update a project's details**The following `update-project`example updates a wind farm project.`aws iotsitewise update-project \ --project-id``a1b2c3d4-5678-90ab-cdef-eeeeeEXAMPLE`\ --project-name`"Wind Farm 1"`\ --project-description`"Contains asset visualizations for Wind Farm #1 for Example Corp."`This command produces no output. For more information, see [Changing project details](https://docs.aws.amazon.com/iot-sitewise/latest/appguide/edit-project-details.html)in the*AWS IoT SiteWise Monitor Application Guide*.- 
                    For API details, see [UpdateProject](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/update-project.html)in*AWS CLI Command Reference*.
 
-