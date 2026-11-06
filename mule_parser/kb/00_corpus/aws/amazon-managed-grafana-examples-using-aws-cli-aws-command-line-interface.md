# Amazon Managed Grafana examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_grafana_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_grafana_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Amazon Managed Grafana.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `list-workspaces`.

- **AWS CLI**
- 
            
                    **To list workspaces for the account in the Region specified by the user credential**The following `list-workspaces`example lists Grafana workspaces for the account's Region.`aws grafana list-workspaces`Output: `{ "workspaces": [ { "authentication": { "providers": [ "AWS_SSO" ] }, "created": "2022-04-04T16:20:21.796000-07:00", "description": "to test tags", "endpoint": "g-949e7b44df.grafana-workspace.us-east-1.amazonaws.com", "grafanaVersion": "8.2", "id": "g-949e7b44df", "modified": "2022-04-04T16:20:21.796000-07:00", "name": "testtag2", "notificationDestinations": [ "SNS" ], "status": "ACTIVE" }, { "authentication": { "providers": [ "AWS_SSO" ] }, "created": "2022-04-20T10:22:15.115000-07:00", "description": "ww", "endpoint": "g-bffa51ed1b.grafana-workspace.us-east-1.amazonaws.com", "grafanaVersion": "8.2", "id": "g-bffa51ed1b", "modified": "2022-04-20T10:22:15.115000-07:00", "name": "ww", "notificationDestinations": [ "SNS" ], "status": "ACTIVE" } ] }`- 
                    For API details, see [ListWorkspaces](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/grafana/list-workspaces.html)in*AWS CLI Command Reference*.
 
-