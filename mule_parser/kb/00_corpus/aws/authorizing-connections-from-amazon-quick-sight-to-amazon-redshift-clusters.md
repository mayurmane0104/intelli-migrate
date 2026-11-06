# Authorizing connections from Amazon Quick Sight to Amazon Redshift clusters - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/enabling-access-redshift.html](https://docs.aws.amazon.com/quick/latest/userguide/enabling-access-redshift.html)

---

| Applies
                    to:Enterprise Edition and Standard Edition | 

| Intended audience: System administrators | 

You can provide access to Amazon Redshift data using three authentication methods: trusted identity propagation, run-as IAM role, or Amazon Redshift database credentials.

With trusted identity propagation, a user's identity is passed to Amazon Redshift with single sign-on that is managed by IAM Identity Center. A user that accesses a dashboard in Amazon Quick Sight has their identity propagated to Amazon Redshift. In Amazon Redshift, fine grained data permissions are applied on the data before the data is presented in a Amazon Quick asset to the user. Amazon Quick authors can also connect to Amazon Redshift data sources without a password input or IAM role. If Amazon Redshift Spectrum is used, all permission management is centralized in Amazon Redshift. Trusted identity propagation is supported when Amazon Quick and Amazon Redshift use the same organization instance of IAM Identity Center. Trusted identity propagation is not currently supported for the following features.

- 
                SPICE datasets 
- 
                Custom SQL on data sources 
- 
                Alerts 
- 
                Email reports 
- 
                Amazon Quick Q 
- 
                CSV, Excel, and PDF exports 
- 
                Anomaly detection 

For Amazon Quick to connect to an Amazon Redshift instance, you must create a new security group
            for that instance. This security group contains an inbound rule that authorizes access
            from the appropriate IP address range for the Amazon Quick servers in that AWS Region.
            To learn more about authorizing Amazon Quick connections, see [Manually
                enabling access to an Amazon Redshift cluster in a VPC](https://docs.aws.amazon.com/quicksight/latest/user/redshift-vpc-access.html).

Enabling connection from Amazon Quick servers to your cluster is just one of several
            prerequisites for creating a data set based on an AWS database data source. For more
            information about what is required, see [Creating a dataset from a database](https://docs.aws.amazon.com/quicksuite/latest/userguide/create-a-database-data-set.html).

###### Topics

## Enabling trusted identity propagation with Amazon Redshift

            Trusted identity propagation authenticates the end user in Amazon Redshift when they access Amazon Quick assets that leverage a trusted identity propagation enabled data source. When an author creates a data source with trusted identity propagation, the identity of the data source consumers in Amazon Quick Sight is propagated and logged in CloudTrail. This allows database administrators to centrally manage data security in Amazon Redshift and automatically apply all data security rules to data consumers in Amazon Quick. With other authentication methods, the data permissions of the author who created the data source are applied to all data source consumers. The data source author can choose to apply additional row and column level security to the data sources that they create in Amazon Quick Sight.

Trusted identity propagation data sources are supported only in Direct Query datasets. SPICE datasets do not currently support trusted identity propagation.

###### Topics

### Prerequisites

Before you get started, make sure that you have all of the required prerequisites ready.

- 
                        Trusted identity propagation is only supported for Amazon Quick accounts that are integrated with IAM Identity Center. For more information, see [Configure your Amazon Quick account with IAM Identity Center](https://docs.aws.amazon.com/quicksight/latest/user/sec-identity-management-identity-center.html).
- 
                        An Amazon Redshift application that is integrated with IAM Identity Center. The Amazon Redshift cluster that you use must be in the same organization in AWS Organizations as the Amazon Quick account that you want to use. The cluster must also be configured with the same organization instance in IAM Identity Center that your Amazon Quick account is configured to. For more information about configuring a Amazon Redshift cluster, see [Integrating IAM Identity Center](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-idp-connect.html).

### Enabling trusted identity propagation in Amazon Quick Sight

To configure Amazon Quick Sight to connect to Amazon Redshift data sources with trusted identity propagation, configure Amazon Redshift OAuth scopes to your Amazon Quick account.

To add a scope that allows Amazon Quick to authorize identity propagation to
                    Amazon Redshift, specify the AWS account ID of the Amazon Quick account and the service
                    that you want to authorize identity propagation with, in this case
                        `'REDSHIFT'`.

Specify the IAM Identity Center application ARN of the Amazon Redshift cluster that you are authorizing Amazon Quick to propagate user identities to. This information can be found in the Amazon Redshift console. If you don't specify authorized targets for the Amazon Redshift scope, Amazon Quick authorizes users from any Amazon Redshift cluster that share the same IAM Identity Center instance. The example below configures Amazon Quick to connect to Amazon Redshift data sources with trusted identity propagation.

`aws quicksight update-identity-propagation-config --aws-account-id "``AWSACCOUNTID`" --service "REDSHIFT" --authorized-targets "arn:aws:sso::`XXXXXXXXXXXX`:application/ssoins-`XXXXXXXXXXXX`/apl-`XXXXXXXXXXXX`" "arn:aws:sso::`XXXXXXXXXXXX`:application/ssoins-`XXXXXXXXXXXX`/apl-`XXXXXXXXXXXX`"

The following example deletes OAuth scopes from a Amazon Quick account.

`aws quicksight delete-identity-propagation-config --aws-account-id "``AWSACCOUNTID`" --service "REDSHIFT" --authorized-targets "`arn:aws:sso::`"arn:aws:sso::`XXXXXXXXXXXX`:application/ssoins-`XXXXXXXXXXXX`apl-`XXXXXXXXXXXX``XXXXXXXXXXXX`:application/ssoins-`XXXXXXXXXXXX`/apl-`XXXXXXXXXXXX`"

The following example lists all OAuth scopes that are currently on a Amazon Quick account.

`aws quicksight list-identity-propagation-configs --aws-account-id "``AWSACCOUNTID`"

### Connecting to Amazon Redshift with trusted identity propagation

Use the procedure below to connect to Amazon Redshift trusted identity propagation.

###### To connect to Amazon Redshift with trusted identity propagation

- 
                        Create a new dataset in Amazon Quick. For more information about creating a dataset, see [Creating datasets](https://docs.aws.amazon.com/quicksight/latest/user/creating-data-sets.html).
- 
                        Choose Amazon Redshift as the data source for the new dataset. ###### NoteThe authentication type of an existing data source can't be changed to trusted identity propagation 
- 
                        Choose IAM Identity Center as the identity option for the data source, and then choose **Create data source**.

## Manually enabling access to an Amazon Redshift cluster in a VPC

            | Applies
                    to:Enterprise Edition | 

Use the following procedure to enable Amazon Quick Sight access to an Amazon Redshift cluster in a VPC.

###### To enable Amazon Quick Sight access to an Amazon Redshift cluster in a VPC

- Sign in to the AWS Management Console and open the Amazon Redshift console at - [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/).
- 
                    Navigate to the cluster that you want to make available in Amazon Quick. 
- 
                    In the **Cluster Properties**section, find**Port**. Note the**Port**value.
- 
                    In the **Cluster Properties**section, find**VPC ID**and note the**VPC ID**value. Choose**VPC ID**to open the Amazon VPC console.
- 
                    On the Amazon VPC console, choose **Security Groups**in the navigation pane.
- 
                    Choose **Create Security Group**.
- 
                    On the **Create Security Group**page, enter the security group information as follows:- 
                            For **Security group name**, enter`redshift-security-group`.
- 
                            For **Description**, enter`redshift-security-group`.
- 
                            For **VPC**, choose the VPC for your Amazon Redshift cluster. This is the VPC with the VPC ID that you noted.
 
- 
                            
- 
                    Choose **Create security group**.Your new security group should appear on the screen. 
- 
                    Create a second security group with the following properties. - 
                            For **Security group name**, enter`quicksight-security-group`.
- 
                            For **Description**, enter`quicksight-security-group`.
- 
                            For **VPC**, choose the VPC for your Amazon Redshift cluster. This is the VPC with the VPC ID that you noted.
 
- 
                            
- 
                    Choose **Create security group**.
- 
                    After you create the new security groups, create inbound rules for the new groups. Choose the new `redshift-security-group`security group, and input the following values.- 
                            For **Type**, choose**Amazon Redshift**.
- 
                            For **Protocol**, choose**TCP**.
- 
                            For **Port Range**, enter the port number of the Amazon Redshift cluster to which you are providing access. This is the port number that you noted in an earlier step.
- 
                            For **Source**, enter the security group ID of`quicksight-security-group`.
 
- 
                            
- 
                    Choose **Save rules**to save your new inbound rule.
- 
                    Repeat the previous step for `quicksight-security-group`and enter the following values.- 
                            For **Type**, choose**All traffic**.
- 
                            For **Protocol**, choose**All**.
- 
                            For **Port Range**, choose**All**.
- 
                            For **Source**, enter the security group ID of`redshift-security-group`.
 
- 
                            
- 
                    Choose **Save rules**to save your new inbound rule.
- 
                    In Amazon Quick, navigate to the **Manage Amazon Quick**menu.
- 
                    Choose **Manage VPC connections**, and then choose**Add VPC connection**.
- 
                    Configure the new VPC connection with the following values. - 
                            For **VPC connection name**, choose a meaningful name for the VPC connection.
- 
                            For **VPC ID**, choose the VPC in which the Amazon Redshift cluster exists.
- 
                            For **Subnet ID**, choose the subnet for the Availability Zone (AZ) that is used for Amazon Redshift.
- 
                            For **Security group id**, copy and paste the security group ID for`quicksight-security-group`.
 
- 
                            
- 
                    Choose **Create**. It might take several minutes for the new VPC to generate.
- 
                    In the Amazon Redshift console, navigate to the Amazon Redshift cluster that `redshift-security-group`is configured to. Choose**Properties**. under**Network and security settings**, enter the name of the security group.
- 
                    In Amazon Quick, choose **Datasets**, and then choose**New dataset**. Create a new dataset with the following values.- 
                            For **Data source**, choose**Amazon Redshift Auto-discovered**.
- 
                            Give the data source a meaningful name. 
- 
                            The instance ID should auto populate with the VPC connection that you created in Amazon Quick. If the instance ID doesn't auto populate, choose the VPC that you created from the dropdown list. 
- 
                            Enter the database credentials. If your Amazon Quick account uses trusted identity propagation, choose **Single sign-on**.
 
- 
                            
- 
                    Validate the connection, and then choose **Create data source**.

If you want to restrict the default outbound rules further, update the outbound
                rule of `quicksight-security-group` to allow only Amazon Redshift traffic to
                    `redshift-security-group`. You can also delete the outbound rule
                that's located in the `redshift-security-group`.

## Enabling access to Amazon Redshift Spectrum

            Using Amazon Redshift Spectrum, you can connect Amazon Quick to an external catalog with Amazon Redshift. For example, you can access the Amazon Athena catalog . You can then query unstructured data on your Amazon S3 data lake using an Amazon Redshift cluster instead of the Athena query engine.

You can also combine data sets that include data stored in Amazon Redshift and in S3. Then you can access them using the SQL syntax in Amazon Redshift.

After you've registered your data catalog (for Athena) or external schema (for a
                    [Hive metastore](https://aws.amazon.com/blogs/big-data/migrate-external-table-definitions-from-a-hive-metastore-to-amazon-athena/)), you can use Amazon Quick to choose the external schema
                and Amazon Redshift Spectrum tables. This process works just as for any other Amazon Redshift tables in
                your cluster. You don't need to load or transform your data. 

For more information on using Amazon Redshift Spectrum, see [Using Amazon Redshift Spectrum to query external
                    data](https://docs.aws.amazon.com/redshift/latest/dg/c-using-spectrum.html) in the *Amazon Redshift Database Developer Guide.*

To connect using Redshift Spectrum, do the following:

- 
                    Create or identify an IAM role associated with the Amazon Redshift cluster. 
- 
                    Add the IAM policies `AmazonS3ReadOnlyAccess`and`AmazonAthenaFullAccess`to the IAM role.
- 
                    Register an external schema or data catalog for the tables that you plan to use. 

Redshift Spectrum lets you separate storage from compute, so you can scale them separately. You only pay for the queries that you run.

To connect to Redshift Spectrum tables, you don't need to grant Amazon Quick access to Amazon S3 or
                Athena. Amazon Quick needs access only to the Amazon Redshift cluster. For full details on
                configuring Redshift Spectrum, see [Getting started with
                    Amazon Redshift Spectrum](https://docs.aws.amazon.com/redshift/latest/dg/c-getting-started-using-spectrum.html) in the *Amazon Redshift Database Developer
                Guide*.