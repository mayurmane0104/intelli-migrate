# Creating parameter defaults in Amazon Quick - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/parameters-default-values.html](https://docs.aws.amazon.com/quick/latest/userguide/parameters-default-values.html)

---

Use this section to learn more about the types of parameter defaults that are available, and how to set up each of them.

Each field can have a parameter and a control associated with it. When someone views a dashboard or email report, any sheet control that has a static default value configured uses the static default. The default value can change how data is filtered, how custom actions behave, and what text displays in a dynamic sheet title. Email reports also support dynamic defaults.

The simplest default is a static (unchanging) default, which shows the same value to
            everyone. As the designer of the dashboard, you choose the default value. It can't
            be changed by the person using the dashboard. However, that person can choose any value
            from the controls. Setting a default doesn't change this. To restrict the values
            that a person can select, consider using row-level security. For more information, see
                [Using row-level security with user-based rules to restrict access to a dataset](./restrict-access-to-a-data-set-using-row-level-security.html). 

###### To create or edit a static default value that applies to everyone's dashboard view

- 
                Choose the context menu ( `v`) by the parameter that you want to edit, or create a new parameter by following the steps in[Setting up parameters in Amazon Quick](./parameters-set-up.html).
- 
                Enter a value for **Static default value**to set a static default.

To display a different default depending on who is viewing the dashboard, you create a dynamic default parameter (DDP). Using dynamic defaults involves some preparation to map people to their assigned defaults. First, you need to create a database query or a data file that contains information about the people, the fields, and the default values to display. You add this to a dataset, then add the dataset to your analysis. Following, you can find procedures that you can use to gather information, create the dataset, and add the dynamic default to the parameter.

Use the following guidelines when creating a dataset for dynamic default values:

- 
                We recommend that you use a single dataset to contain all dynamic default definitions for a logical grouping of users or groups. If you can, maintain them in a single table or file. 
- 
                We also recommend that the fields in your dataset have names that closely match the field names in the analysis. Not all dataset fields need to be part of the analysis, for example if you're using the same dataset for the defaults in multiple dashboards. The fields can be in any order. 
- 
                We don't recommend that you combine both user and group names in the same column or even in the same dataset. This kind of configuration is more work to maintain and troubleshoot. 
- 
                If you use a comma-delimited file to create your dataset, make sure to remove any space between values in the file. The following example shows the correct comma-separated value (CSV) format. Enclose text (strings) that include nonalphanumeric characters—like spaces, apostrophes, and so on—in single or double quotation marks. You can enclose fields that are dates or times in quotation marks, but it isn't required. You can enclose numeric fields in quotation marks, for example if the numbers contain special characters, as shown following. `"Value includes spaces","Field contains ' other characters",12345.6789,"20200808" ValueWithoutSpaces,"1000,67","Value 3",2020-AUG-08`
- 
                After you create the dataset, make sure to double-check the data types that Quick selects for the fields. 

Before you begin, you need a list of the user or group names for the people who are
            going to have dynamic defaults. To generate a list of users or groups, you can use the
            AWS CLI to get the information. To run CLI commands, make sure that you have the AWS CLI
            installed and configured. For more information, see [Installing the
                AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html) in the *AWS CLI User Guide*. 

This is just one example of how to get a list of user or group names. Use whatever method works best for you.

###### To identify people for a dynamic default parameter (DDP)

- 
                
                List either individual user names or group names: - 
                        To list individual user names, include a column that identifies the people for your DDP. This column should contain each person's system user name that they use to connect from your identity provider to Quick. This user name is often the same as a person's email alias before the @ sign, but not always. To get a list of users, use the [ListUsers](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListUsers.html)Quick API operation or AWS CLI command. The CLI command is shown in the following example. Specify the AWS Region for your identity provider, for example`us-east-1`.`awsacct1="``111111111111`" namespace="`default`" region="`us-east-1`" aws quicksight list-users --aws-account-id`$awsacct1`--namespace`$namespace`**--region**`$region`The following example alters the previous command by adding a query that limits the results to active users. `awsacct1="``111111111111`" namespace="`default`" region="`us-east-1`" aws quicksight list-users --aws-account-id`$awsacct1`--namespace`$namespace`**--region**--query 'UserList[?Active==`true`]'`$region`The result set looks similar to the following sample. This example is an excerpt from JSON output ( `--output json`). People who have federated user names have principal IDs that start with the word`federated`.`[ { "Arn": "arn:aws:quicksight:us-east-1:111111111111:user/default/anacasilva", "UserName": "anacarolinasilva", "Email": "anacasilva@example.com", "Role": "ADMIN", "Active": true, "PrincipalId": "`**federated**/iam/AIDAJ64EIEIOPX5CEIEIO" }, { "Arn": "arn:aws:quicksight:us-east-1:111111111111:user/default/Reader/liujie-stargate", "UserName": "Reader/liujie-stargate", "Role": "READER", "Active": true, "PrincipalId": "**federated**/iam/AROAIJSEIEIOMXTZEIEIO:liujie-stargate" }, { "Arn": "arn:aws:quicksight:us-east-1:111111111111:user/default/embedding/cxoportal", "UserName": "embedding/cxoportal", "Email": "saanvisarkar@example.com", "Role": "AUTHOR", "Active": true, "PrincipalId": "**federated**/iam/AROAJTGEIEIOWB6BEIEIO:cxoportal" }, { "Arn": "arn:aws:quicksight:us-east-1:111111111111:user/default/zhangwei@example.com", "UserName": "zhangwei@example.com", "Email": "zhangwei@example.com", "Role": "AUTHOR", "Active": true, "PrincipalId": "**user**/d-96123-example-id-1123" } ]
- 
                        To list group names, include a column that identifies the groups containing the user names for your DDP. This column should contain the system group names that are used to connect from your identity provider to Quick. To identify groups that you can add to the dataset, use one or more of the following Quick API operations or CLI commands: - 
                                [ListGroups](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListGroups.html)– Lists Quick groups by AWS account ID and namespace for the AWS Region that contains your identity provider.
- 
                                [ListGroupMemberships](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListGroupMemberships.html)– Lists the users in the specified Quick group.
- 
                                [ListUserGroups](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListUserGroups.html)– Lists the Quick groups that a Quick user is a member of.
 Or you can ask your network administrator to query your identity provider to get this information. 
- 
                                
 
- 
                        

The next two procedures provide instructions on how to finish creating a dataset for dynamic default values. The first procedure is for creating a dataset for a single-value DDP. The second one is for creating a dataset for a multivalue DDP.

###### To create a dataset for a single-value DDP

- 
                Create dataset columns with single-value parameters. The first column in the query or file should be for the people using the dashboard. This field can contain user names or group names. However, support for groups is only available in Quick Enterprise edition. 
- 
                For each field that displays a dynamic default for a single-value parameter, add a column to the dataset. The name of the column doesn't matter—you can use the same name as the field or parameter. Single-value parameters only work as specified if the combination of user entity and dynamic default is unique for that parameter's field. If there are multiple values a default field for a user entity, the single-value control for that field displays the static default instead. If no static default is defined, the control doesn't display a default value. Be careful if you use group names, because some user names can be members of multiple groups. If those groups have different default values, then this type of user name functions as a duplicate entry. The following example shows a table that appears to contain two single-value parameters. We make this assumption because no user name is paired with multiple default values. To make this table easier to understand, we add the word `'default'`in front of the field names from the analysis. Thus, you can read the table by making the following statement, changing the values for each row: When viewed by`anacarolinasilva`, the controls display a default region`NorthEast`and a default segment`SMB`.Viewed-by Default-region Default-segment anacarolinasilva NorthEast SMB liujie SouthEast SMB saanvisarkar NorthCentral SMB zhangwei SouthCentral SMB 
- 
                Import this data into Quick, and save it as a new dataset. 
- 
                In your analysis, add the dataset that you created. The analysis needs to use at least one other dataset that matches the columns you defined for the defaults. For more information, see [Adding a dataset to an analysis](./adding-a-data-set-to-an-analysis.html).

###### To create a dataset for a multivalue DDP

- 
                Create dataset columns with multivalue parameters. The first column in the query or file should be for the people using the dashboard. This field can contain user names or group names. However, support for groups is only available in Quick Enterprise edition. 
- 
                For each field that displays a dynamic default for a multivalue parameter, add a column to the dataset. The name of the column doesn't matter—you can use the same name as the field or parameter. Unlike single-value parameters, multivalue parameters allow multiple values in the field that's associated with the parameter. The following example shows a table that appears to contain a single-value parameter and a multivalue parameter. We can make this assumption because each user name has a unique value in one column, and some user names have multiple values in the other column. To make this table easier to understand, we add the word `'default'`in front of the field names from the analysis. Thus, you can read the table by making the following statement, changing the values for each row: When`viewed-by`is`liujie`, the controls display a`default-region`value of`SouthEast`, and a`default-city`value of`Atlanta`. And if we read ahead one row, we see that`liujie`also has`Raleigh`in`default-city`.Viewed-by Default-region Default-city anacarolinasilva NorthEast New York liujie SouthEast Atlanta liujie SouthEast Raleigh saanvisarkar NorthCentral Chicago zhangwei SouthCentral Dallas zhangwei SouthCentral Kansas City In this example, the parameter that we apply `default-region`to works correctly whether it's a single-value or multivalue parameter. If it's a single-value parameter, two entries work for one user because both entries are the same value,`SouthEast`. If it's a multivalue parameter, it still works, except that only one value is selected by default. However, if we change the parameter that's using`default-city`as its default from a multivalue to a single-value parameter, we don't see these defaults selected. Instead, the parameter uses the static default, if there is one defined. For example, if the static default is set to`Atlanta`,`liujie`has`Atlanta`selected in that control, but not`Raleigh`.In some cases, your static default value might also be used as a dynamic default. If so, make sure to test the control for a user name that doesn't use a default value that can be both. If a user name belongs to multiple groups, the named user sees a set of default values that is a union of the two groups' default values. 
- 
                Import this data into Quick, and save it as a new dataset. 
- 
                In your analysis, add the dataset that you created. The analysis needs to use at least one other dataset that matches the columns you defined for the defaults. For more information, see [Adding a dataset to an analysis](./adding-a-data-set-to-an-analysis.html).

Use the following procedure to add a dynamic default parameter to your analysis. Before you begin, make sure that you have a dataset that contains the dynamic defaults for each user name or group name. Also make sure that your analysis is using this dataset. For help with these requirements, see the procedures preceding.

###### To add a DDP to your analysis

- 
                In the Quick console, choose the **Parameters**icon at the top of the page and choose an existing parameter. Choose**Edit parameter**from the parameter's menu. To add a new parameter, choose the plus (`+`) sign near**Parameters**.
- 
                Choose **Set a dynamic default**.
- 
                Configure the following options with your settings: - 
                        **Dataset with default values and user information**– Choose the dataset that you created and added to your analysis.
- 
                        **User name column**– To create defaults that are based on user names, choose the column in the dataset that contains the user names.
- 
                        **Group name column**– To create defaults that are based on group names, choose the column in the dataset that contains the group names.
- 
                        **Column for default value**– Choose the column that contains default values for this parameter.
 
- 
                        
- 
                Choose **Apply**to save your setting changes, and then choose**Update**to save the parameter changes. To exit without saving changes, choose**Cancel**instead.
- 
                Add a filter for each field that contains dynamic defaults to make the defaults work. To learn more about using filters with parameters, see [Using filters with parameters in Amazon Quick](./parameters-filtering-by.html)Amazon Quick uses the static default value for anyone whose user name doesn't exist in the dataset, doesn't have a default assigned, or doesn't have a unique default. Each person can have only one set of defaults. If you don't want to use dynamic defaults, you can set a static default instead.