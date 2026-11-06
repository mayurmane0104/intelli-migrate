# Schema - Powertools for AWS Lambda (Python)

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api_doc/feature_flags/schema](https://docs.aws.amazon.com/powertools/python/latest/api_doc/feature_flags/schema)

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

A dictionary with each rule and their conditions that a feature might have.
The value MIGHT be present, and when defined it MUST contain the following members:

when_match: bool | JSONType. Defines value to return when context matches conditions

conditions: list[dict]. Conditions object. This MUST be present

1 2 3 4 5 6 7 8 9101112131415161718192021

{"my_feature":{"default":true,"rules":{"tenant id equals 345345435":{"when_match":false,"conditions":[]}}},"my_non_boolean_feature":{"default":{"group":"read-only"},"boolean_type":false,"rules":{"tenant id equals 345345435":{"when_match":{"group":"admin"},"conditions":[]}}}}

Conditions object

A list of dictionaries containing conditions for a given rule.
The value MUST contain the following members:

action: str. Operation to perform to match a key and value.
The value MUST be either EQUALS, STARTSWITH, ENDSWITH,
KEY_IN_VALUE KEY_NOT_IN_VALUE VALUE_IN_KEY VALUE_NOT_IN_KEY

key: str. Key in given context to perform operation

value: Any. Value in given context that should match action operation.

1 2 3 4 5 6 7 8 91011121314151617

{"my_feature":{"default":true,"rules":{"tenant id equals 345345435":{"when_match":false,"conditions":[{"action":"EQUALS","key":"tenant_id","value":"345345435",}]}}}}

Source code in aws_lambda_powertools/utilities/feature_flags/schema.py

201202203204205206207208

def__init__(self,schema:dict[str,Any],logger:logging.Logger|Logger|None=None):self.schema=schemaself.logger=loggerorLOGGER# Validators are designed for modular testing# therefore we link the custom logger with global LOGGER# so custom validators can use them when necessarySchemaValidator._link_global_logger(self.logger)