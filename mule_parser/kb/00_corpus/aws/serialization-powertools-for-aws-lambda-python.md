# Serialization - Powertools for AWS Lambda (Python)

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api_doc/idempotency/serialization](https://docs.aws.amazon.com/powertools/python/latest/api_doc/idempotency/serialization)

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

Creates an instance of a serializer based on a provided model type.
In case the model_type is unknown, None will be sent as model_type.
It's on the implementer to verify that:
- None is handled correctly
- A model type not matching the expected types is handled

Source code in aws_lambda_powertools/utilities/idempotency/serialization/base.py

303132333435363738394041424344454647484950

@classmethod@abstractmethoddefinstantiate(cls,model_type:Any)->BaseIdempotencySerializer:""" Creates an instance of a serializer based on a provided model type. In case the model_type is unknown, None will be sent as `model_type`. It's on the implementer to verify that: - None is handled correctly - A model type not matching the expected types is handled Parameters ---------- model_type: Any The model type to instantiate the class for Returns ------- BaseIdempotencySerializer Instance of the serializer class """pass

Source code in aws_lambda_powertools/utilities/idempotency/serialization/custom_dict.py

1213141516171819202122

def__init__(self,to_dict:Callable[[Any],dict],from_dict:Callable[[dict],Any]):""" Parameters ---------- to_dict: Callable[[Any], dict] A function capable of transforming the saved data object representation into a dictionary from_dict: Callable[[dict], Any] A function capable of transforming the saved dictionary into the original data object representation """self.__to_dict:Callable[[Any],dict]=to_dictself.__from_dict:Callable[[dict],Any]=from_dict

A serializer class for transforming data between dataclass objects and dictionaries.

Source code in aws_lambda_powertools/utilities/idempotency/serialization/dataclass.py

2425262728293031

def__init__(self,model:type[DataClass]):""" Parameters ---------- model: type[DataClass] A dataclass type to be used for serialization and deserialization """self.__model:type[DataClass]=model

Extract the actual type from a potentially Optional or Union type.
This function handles types that may be wrapped in Optional or Union,
including the Python 3.10+ Union syntax (Type | None).

PARAMETER

DESCRIPTION

model_type

The type to analyze. Can be a simple type, Optional[Type], BaseModel, dataclass

defget_actual_type(model_type:Any)->Any:""" Extract the actual type from a potentially Optional or Union type. This function handles types that may be wrapped in Optional or Union, including the Python 3.10+ Union syntax (Type | None). Parameters ---------- model_type: Any The type to analyze. Can be a simple type, Optional[Type], BaseModel, dataclass Returns ------- The actual type without Optional or Union wrappers. Raises: IdempotencyModelTypeError: If the type specification is invalid (e.g., Union with multiple non-None types). """# Get the origin of the type (e.g., Union, Optional)origin=get_origin(model_type)# Check if type is Union, Optional, or UnionType (Python 3.10+)iforiginin(Union,Optional)or(sys.version_info>=(3,10)andoriginin(Union,UnionType)):# Get type argumentsargs=get_args(model_type)# Filter out NoneTypeactual_type=_extract_non_none_types(args)# Ensure only one non-None type existsiflen(actual_type)!=1:raiseIdempotencyModelTypeError("Invalid type: expected a single type, optionally wrapped in Optional or Union with None.",)returnactual_type[0]# If not a Union/Optional type, return original typereturnmodel_type

Source code in aws_lambda_powertools/utilities/idempotency/serialization/pydantic.py

2122232425262728

def__init__(self,model:type[BaseModel]):""" Parameters ---------- model: Model Pydantic model to be used for serialization """self.__model:type[BaseModel]=model