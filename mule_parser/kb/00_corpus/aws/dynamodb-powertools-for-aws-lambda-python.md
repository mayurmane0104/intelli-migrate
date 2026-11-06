# DynamoDB - Powertools for AWS Lambda (Python)

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api_doc/parameters/dynamodb](https://docs.aws.amazon.com/powertools/python/latest/api_doc/parameters/dynamodb)

---

We use essential cookies and similar tools that are necessary to provide our site and services. We use performance cookies to collect anonymous statistics, so we can understand how customers use our site and make improvements. Essential cookies cannot be deactivated, but you can choose “Customize” or “Decline” to decline performance cookies.

If you agree, AWS and approved third parties will also use cookies to provide useful site features, remember your preferences, and display relevant content, including relevant advertising. To accept or decline all non-essential cookies, choose “Accept” or “Decline.” To make more detailed choices, choose “Customize.”

Customize cookie preferences

We use cookies and similar tools (collectively, "cookies") for the following purposes.

Essential

Essential cookies are necessary to provide our site and services and cannot be deactivated. They are usually set in response to your actions on the site, such as setting your privacy preferences, signing in, or filling in forms.

Allowed

Performance

Performance cookies provide anonymous statistics about how customers navigate our site so we can improve site experience and performance. Approved third parties may perform analytics on our behalf, but they cannot use the data for their own purposes.

Allowed

Functional

Functional cookies help us provide useful site features, remember your preferences, and display relevant content. Approved third parties may set these cookies to provide certain site features. If you do not allow these cookies, then some or all of these services may not function properly.

Allowed

Advertising

Advertising cookies may be set through our site by us or our advertising partners and help us deliver relevant marketing content. If you do not allow these cookies, you will experience less relevant advertising.

Allowed

Blocking some types of cookies may impact your experience of our sites. You may review and change your choices at any time by selecting Cookie preferences in the footer of this site. We and selected third-parties use cookies or similar technologies as specified in the AWS Cookie Notice.

Your privacy choices

We and our advertising partners (“we”) may use information we collect from or about you to show you ads on other websites and online services. Under certain laws, this activity is referred to as “cross-context behavioral advertising” or “targeted advertising.”

To opt out of our use of cookies or similar technologies to engage in these activities, select “Opt out of cross-context behavioral ads” and “Save preferences” below. If you clear your browser cookies or visit this site from a different device or browser, you will need to make your selection again. For more information about cookies and how we use them, read our Cookie Notice.

To opt out of the use of other identifiers, such as contact information, for these activities, fill out the form here.

For more information about how AWS handles your information, read the AWS Privacy Notice.

Unable to save cookie preferences

We will only store essential cookies at this time, because we were unable to save your cookie preferences.

If you want to change your cookie preferences, try again later using the link in the AWS console footer, or contact support if the problem persists.

Botocore configuration to pass during client initialization

TYPE:Config | NoneDEFAULT:None

boto3_session

1

Boto3 session to create a boto3_client from

TYPE:SessionDEFAULT:None

boto3_client

1

Boto3 DynamoDB Resource Client to use; boto3_session will be ignored if both are provided

TYPE:DynamoDBServiceResource | NoneDEFAULT:None

Example

Retrieves a parameter value from a DynamoDB table

In this example, the DynamoDB table uses id as hash key and stores the value in the value
attribute. The parameter item looks like this:

123456789

{ "id": "my-parameters", "value": "Parameter value a" }
>>> from aws_lambda_powertools.utilities.parameters import DynamoDBProvider
>>> ddb_provider = DynamoDBProvider("ParametersTable")
>>>
>>> value = ddb_provider.get("my-parameter")
>>>
>>> print(value)
My parameter value

Retrieves a parameter value from a DynamoDB table that has custom attribute names

1 2 3 4 5 6 7 8 91011

>>> from aws_lambda_powertools.utilities.parameters import DynamoDBProvider
>>> ddb_provider = DynamoDBProvider(
... "ParametersTable",
... key_attr="my-id",
... value_attr="my-value"
... )
>>>
>>> value = ddb_provider.get("my-parameter")
>>>
>>> print(value)
My parameter value

Retrieves a parameter value from a DynamoDB table in another AWS region

1 2 3 4 5 6 7 8 910

>>> from botocore.config import Config
>>> from aws_lambda_powertools.utilities.parameters import DynamoDBProvider
>>>
>>> config = Config(region_name="us-west-1")
>>> ddb_provider = DynamoDBProvider("ParametersTable", config=config)
>>>
>>> value = ddb_provider.get("my-parameter")
>>>
>>> print(value)
My parameter value

Retrieves a parameter value from a DynamoDB table passing options to the SDK call

1234567

>>> from aws_lambda_powertools.utilities.parameters import DynamoDBProvider
>>> ddb_provider = DynamoDBProvider("ParametersTable")
>>>
>>> value = ddb_provider.get("my-parameter", ConsistentRead=True)
>>>
>>> print(value)
My parameter value

Retrieves multiple values from a DynamoDB table

In this case, the provider will use a sort key to retrieve multiple values using a query under
the hood. This expects that the sort key is named sk. The DynamoDB table contains three items
looking like this:

1 2 3 4 5 6 7 8 91011121314

{ "id": "my-parameters", "sk": "a", "value": "Parameter value a" }
{ "id": "my-parameters", "sk": "b", "value": "Parameter value b" }
{ "id": "my-parameters", "sk": "c", "value": "Parameter value c" }
>>> from aws_lambda_powertools.utilities.parameters import DynamoDBProvider
>>> ddb_provider = DynamoDBProvider("ParametersTable")
>>>
>>> values = ddb_provider.get_multiple("my-parameters")
>>>
>>> for key, value in values.items():
... print(key, value)
a Parameter value a
b Parameter value b
c Parameter value c

Retrieves multiple values from a DynamoDB table that has custom attribute names

In this case, the provider will use a sort key to retrieve multiple values using a query under
the hood.

1 2 3 4 5 6 7 8 9101112131415

>>> from aws_lambda_powertools.utilities.parameters import DynamoDBProvider
>>> ddb_provider = DynamoDBProvider(
... "ParametersTable",
... key_attr="my-id",
... sort_attr="my-sort-key",
... value_attr="my-value"
... )
>>>
>>> values = ddb_provider.get_multiple("my-parameters")
>>>
>>> for key, value in values.items():
... print(key, value)
a Parameter value a
b Parameter value b
c Parameter value c

Retrieves multiple values from a DynamoDB table passing options to the SDK calls

1 2 3 4 5 6 7 8 910

>>> from aws_lambda_powertools.utilities.parameters import DynamoDBProvider
>>> ddb_provider = DynamoDBProvider("ParametersTable")
>>>
>>> values = ddb_provider.get_multiple("my-parameters", ConsistentRead=True)
>>>
>>> for key, value in values.items():
... print(key, value)
a Parameter value a
b Parameter value b
c Parameter value c

Source code in aws_lambda_powertools/utilities/parameters/dynamodb.py

def__init__(self,table_name:str,key_attr:str="id",sort_attr:str="sk",value_attr:str="value",endpoint_url:str|None=None,config:Config|None=None,boto_config:Config|None=None,boto3_session:boto3.session.Session|None=None,boto3_client:DynamoDBServiceResource|None=None,):""" Initialize the DynamoDB client """ifconfig:warnings.warn(message="The 'config' parameter is deprecated in V3 and will be removed in V4. ""Please use 'boto_config' instead.",category=PowertoolsDeprecationWarning,stacklevel=2,)ifboto3_clientisNone:boto3_session=boto3_sessionorboto3.session.Session()boto3_client=boto3_session.resource("dynamodb",config=boto_configorconfig,endpoint_url=endpoint_url)self.table=boto3_client.Table(table_name)self.key_attr=key_attrself.sort_attr=sort_attrself.value_attr=value_attrsuper().__init__(resource=boto3_client)