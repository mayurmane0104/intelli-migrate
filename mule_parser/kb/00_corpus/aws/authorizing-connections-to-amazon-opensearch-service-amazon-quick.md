# Authorizing connections to Amazon OpenSearch Service - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/opensearch.html](https://docs.aws.amazon.com/quick/latest/userguide/opensearch.html)

---

| Applies
                    to:Enterprise Edition | 

| Intended audience: System administrators | 

Before you can use OpenSearch in a Amazon Quick Sight dataset, there are a few tasks for the Quick administrator to complete with the cooperation of a person who has access to the OpenSearch console.

To get started, identify each OpenSearch domain that you want to connect to. Then gather the following information for each domain:

- 
                The name of the OpenSearch domain. 
- 
                The OpenSearch version used by this domain. 
- 
                The Amazon Resource Name (ARN) of the OpenSearch domain. 
- 
                The HTTPS endpoint. 
- 
                The OpenSearch Dashboards URL, if you use Dashboards. You can extrapolate the Dashboards URL by appending " `/dashboards/`" to an endpoint.
- 
                If the domain has a VPC endpoint, gather all the related information on the VPC tab of the OpenSearch Service console: - 
                        The VPC ID 
- 
                        The VPC security groups 
- 
                        The associated IAM role or roles 
- 
                        The associated Availability Zones 
- 
                        The associated subnets 
 
- 
                        
- 
                If the domain has a regular endpoint (not a VPC endpoint), note that it uses the public network. 
- 
                The start hour for the daily automated snapshot (if your users want to know). 

Before you proceed, the Amazon Quick administrator enables authorized connections from Amazon Quick to OpenSearch Service. This process is required for every AWS service that you connect to from Amazon Quick. You need to do this only once per AWS account for each AWS service that you use as a data source.

For OpenSearch Service, the authorization process adds the AWS managed policy
                `AWSQuickSightOpenSearchPolicy` to your AWS account.
            

###### Important

Make sure that the IAM policy for your OpenSearch domain doesn't conflict with
                the permissions in `AWSQuickSightOpenSearchPolicy`. You can find the
                domain access policy in the OpenSearch Service console. For more information, see [Configuring access policies](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ac.html#ac-creating) in the
                    *Amazon OpenSearch Service Developer Guide*.

###### To turn on or turn off connections from Amazon Quick to OpenSearch Service

- 
                Within Amazon Quick, choose **Administrator**and**Manage Amazon Quick**.
- 
                Choose **Security & permissions**,**Add or remove**.
- 
                To enable connections, select the **Amazon OpenSearch Service**check box.To disable connections, clear the **Amazon OpenSearch Service**check box.
- 
                Choose **Update**to confirm your choices.

If needed, use the topics below to configure a OpenSearch VPC connection and permissions for Amazon Quick to access OpenSearch.

## Using a VPC connection

            In some cases, your OpenSearch domain is in a virtual private cloud (VPC) based on
                the Amazon VPC service. If so, make sure to determine if Amazon Quick is already
                connected to the VPC ID that the OpenSearch domain uses. You can reuse an existing
                VPC connection. If you're not sure if it's working, you can test it. For more
                information, see [Testing the connection to your Amazon VPC data
                source](https://docs.aws.amazon.com/quicksight/latest/user/vpc-creating-a-quicksight-data-source-profile.html).

If a connection isn't already defined in Amazon Quick for the VPC that you want to
                use, you can create one. This task is a multistep process that you need to complete
                before you proceed. To learn how to add Amazon Quick to a VPC and add a connection
                from Amazon Quick to the VPC, see [Connecting to a Amazon VPC with Amazon Quick](https://docs.aws.amazon.com/quicksight/latest/user/working-with-aws-vpc.html).

## Using OpenSearch permissions

            
            After you configure Amazon Quick to connect to OpenSearch Service, you might need to enable permissions in OpenSearch. For this part of the setup process, you can use the OpenSearch Dashboards link for each OpenSearch domain. Use the following list to help determine what permissions you need:

- 
                    For domains that use fine-grained access control, configure permissions in the form of a role. This process is similar to using scoped-down policies in Amazon Quick. 
- 
                    For each domain that you create a role for, add a role mapping. 

For more information, see following.

If your OpenSearch domain has [fine-grained
                    access control](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/fgac.html) enabled, there are some permissions to configure so the
                domain is accessible from Amazon Quick. Perform these steps for each domain that you
                want to use. 

The following procedure uses OpenSearch Dashboards, which is an open-source tool that works with OpenSearch. You can find the link to Dashboards on the domain dashboard on the OpenSearch Service console.

###### To add permissions to a domain to allow access from Amazon Quick

- 
                    Open OpenSearch Dashboards for the OpenSearch domain that you want to work with. The URL is `opensearch-domain-endpoint`/dashboards/
- 
                    Choose **Security**from the navigation pane.If you don't see the navigation pane, open it by using the menu icon at upper left. To keep the menu open, choose **Dock navigation**at lower left.
- 
                    Choose **Roles**,**Create role**.
- 
                    Name the role `quicksight_role`.You can choose a different name, but we recommend this one because we use it in our documentation and it's thus easier to support. 
- 
                    Under **Cluster permissions**, add the following permissions:- 
                            `cluster:monitor/main`
- 
                            `cluster:monitor/health`
- 
                            `cluster:monitor/state`
- 
                            `indices:data/read/scroll`
- 
                            `indices:data/read/scroll/clear`,
 
- 
                            
- 
                    Under **Index permissions**specify`*`as the index pattern.
- 
                    For **Index permissions**, add the following permissions:- 
                            `indices:admin/get`
- 
                            `indices:admin/mappings/get`
- 
                            `indices:admin/mappings/fields/get*`
- 
                            `indices:data/read/search*`
- 
                            `indices:monitor/settings/get`
 
- 
                            
- 
                    Choose **Create**.
- 
                    Repeat this procedure for each OpenSearch domain that you're planning to use. 

Use the following procedure to add a role mapping for the permissions that you added in the previous procedure. You might find it more efficient to add the permissions and the role mapping as part of a single process. These instructions are separate for clarity.

###### To create a role mapping for the IAM role you added

- 
                    Open OpenSearch Dashboards for the OpenSearch domain that you want to work with. The URL is `opensearch-domain-endpoint`/dashboards/
- 
                    Choose **Security**from the navigation pane.
- 
                    Search for and open `quicksight_role`from the list.
- 
                    On the **Mapped users**tab, choose**Manage mapping**.
- 
                    In the **Backend roles**section, enter the ARN of the AWS-managed IAM role for Amazon Quick. Following is an example.`arn:``aws`:iam::`AWS-ACCOUNT-ID`:role/service-role/`aws-quicksight-service-role-v0`
- 
                    Choose **Map**.
- 
                    Repeat this procedure for each OpenSearch domain that you want to use.