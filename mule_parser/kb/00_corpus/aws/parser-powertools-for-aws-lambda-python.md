# Parser - Powertools for AWS Lambda (Python)

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api_doc/parser](https://docs.aws.amazon.com/powertools/python/latest/api_doc/parser)

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

The Parser utility simplifies data parsing and validation using Pydantic. It allows you to define data models
in pure Python classes, parse and validate incoming events, and extract only the data you need.

@lambda_handler_decoratordefevent_parser(handler:Callable[...,EventParserReturnType],event:dict[str,Any],context:LambdaContext,model:type[T]|None=None,envelope:type[Envelope]|None=None,**kwargs:Any,)->EventParserReturnType:"""Lambda handler decorator to parse & validate events using Pydantic models It requires a model that implements Pydantic BaseModel to parse & validate the event. When an envelope is given, it'll use the following logic: 1. Parse the event against the envelope model first e.g. EnvelopeModel(**event) 2. Envelope will extract a given key to be parsed against the model e.g. event.detail This is useful when you need to confirm event wrapper structure, and b) selectively extract a portion of your payload for parsing & validation. NOTE: If envelope is omitted, the complete event is parsed to match the model parameter definition. Example ------- **Lambda handler decorator to parse & validate event** class Order(BaseModel): id: int description: str ... @event_parser(model=Order) def handler(event: Order, context: LambdaContext): ... **Lambda handler decorator to parse & validate event - using built-in envelope** class Order(BaseModel): id: int description: str ... @event_parser(model=Order, envelope=envelopes.EVENTBRIDGE) def handler(event: Order, context: LambdaContext): ... Parameters ---------- handler: Callable Method to annotate on event: dict Lambda event to be parsed & validated context: LambdaContext Lambda context object model: type[T] | None Your data model that will replace the event. envelope: Envelope Optional envelope to extract the model from Raises ------ ValidationError When input event does not conform with the provided model InvalidModelTypeError When the model given does not implement BaseModel, is not provided InvalidEnvelopeError When envelope given does not implement BaseEnvelope """ifmodelisNone:# The first parameter of a Lambda function is always the event.# Get the first parameter's type by using typing.get_type_hints.type_hints=typing.get_type_hints(handler)iftype_hints:model=list(type_hints.values())[0]ifmodelisNone:raiseInvalidModelTypeError("The model must be provided either as the `model` argument to `event_parser`""or as the type hint of `event` in the handler that it wraps",)ifenvelope:parsed_event=parse(event=event,model=model,envelope=envelope)else:parsed_event=parse(event=event,model=model)logger.debug(f"Calling handler {handler.__name__}")# ty: ignore[unresolved-attribute]returnhandler(parsed_event,context,**kwargs)

defparse(event:dict[str,Any],model:type[T],envelope:type[Envelope]|None=None):"""Standalone function to parse & validate events using Pydantic models Typically used when you need fine-grained control over error handling compared to event_parser decorator. Example ------- **Lambda handler decorator to parse & validate event** from aws_lambda_powertools.utilities.parser import ValidationError class Order(BaseModel): id: int description: str ... def handler(event: Order, context: LambdaContext): try: parse(model=Order) except ValidationError: ... **Lambda handler decorator to parse & validate event - using built-in envelope** class Order(BaseModel): id: int description: str ... def handler(event: Order, context: LambdaContext): try: parse(model=Order, envelope=envelopes.EVENTBRIDGE) except ValidationError: ... Parameters ---------- event: dict Lambda event to be parsed & validated model: Model Your data model that will replace the event envelope: Envelope Optional envelope to extract the model from Raises ------ ValidationError When input event does not conform with model provided InvalidModelTypeError When model given does not implement BaseModel InvalidEnvelopeError When envelope given does not implement BaseEnvelope """ifenvelopeandcallable(envelope):try:logger.debug(f"Parsing and validating event model with envelope={envelope}")returnenvelope().parse(data=event,model=model)exceptAttributeErrorasexc:raiseInvalidEnvelopeError(f"Error: {str(exc)}. Please ensure that both the Input model and the Envelope inherits from BaseModel,\n"# noqa E501"and your payload adheres to the specified Input model structure.\n"f"Envelope={envelope}\nModel={model}",)fromexctry:adapter=_retrieve_or_set_model_from_cache(model=model)logger.debug("Parsing and validating event model; no envelope used")return_parse_and_validate_event(data=event,adapter=adapter)# Pydantic raises PydanticSchemaGenerationError when the model is not a Pydantic model# This is seen in the tests where we pass a non-Pydantic model type to the parser or# when we pass a data structure that does not match the model (trying to parse a true/false/etc into a model)exceptPydanticSchemaGenerationErrorasexc:raiseInvalidModelTypeError(f"The event supplied is unable to be validated into {type(model)}")fromexcexceptAttributeErrorasexc:raiseInvalidModelTypeError(f"Error: {str(exc)}. Please ensure the Input model inherits from BaseModel,\n""and your payload adheres to the specified Input model structure.\n"f"Model={model}",)fromexc