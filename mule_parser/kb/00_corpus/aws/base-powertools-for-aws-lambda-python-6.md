# Base - Powertools for AWS Lambda (Python)

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api_doc/tracer/base](https://docs.aws.amazon.com/powertools/python/latest/api_doc/tracer/base)

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

Source code in aws_lambda_powertools/tracing/base.py

888990919293949596979899

@abc.abstractmethod@contextmanagerdefin_subsegment(self,name=None,**kwargs)->Generator[BaseSegment,None,None]:"""Return a subsegment context manger. Parameters ---------- name: str Subsegment name kwargs: dict | None Optional parameters to be propagated to segment """

Source code in aws_lambda_powertools/tracing/base.py

101102103104105106107108109110111112

@abc.abstractmethod@contextmanagerdefin_subsegment_async(self,name=None,**kwargs)->Generator[BaseSegment,None,None]:"""Return a subsegment async context manger. Parameters ---------- name: str Subsegment name kwargs: dict | None Optional parameters to be propagated to segment """

Source code in aws_lambda_powertools/tracing/base.py

144145146147148149150151152

@abc.abstractmethoddefpatch(self,modules:Sequence[str])->None:"""Instrument a set of supported libraries Parameters ---------- modules: set[str] Set of modules to be patched """

Source code in aws_lambda_powertools/tracing/base.py

114115116117118119120121122123124125126

@abc.abstractmethoddefput_annotation(self,key:str,value:str|numbers.Number|bool)->None:"""Annotate current active trace entity with a key-value pair. Note: Annotations will be indexed for later search query. Parameters ---------- key: str Metadata key value: str | numbers.Number | bool Annotation value """

Source code in aws_lambda_powertools/tracing/base.py

128129130131132133134135136137138139140141142

@abc.abstractmethoddefput_metadata(self,key:str,value:Any,namespace:str="default")->None:"""Add metadata to the current active trace entity. Note: Metadata is not indexed but can be later retrieved by BatchGetTraces API. Parameters ---------- key: str Metadata key value: Any Any object that can be serialized into a JSON string namespace: set[str] Metadata namespace, by default 'default' """

Source code in aws_lambda_powertools/tracing/base.py

707172737475767778798081828384

@abc.abstractmethoddefadd_exception(self,exception:BaseException,stack:list[traceback.StackSummary],remote:bool=False):"""Add an exception to trace entities. Parameters ---------- exception: Exception Caught exception stack: list[traceback.StackSummary] List of traceback summaries Output from `traceback.extract_stack()`. remote: bool Whether it's a client error (False) or downstream service error (True), by default False """

Source code in aws_lambda_powertools/tracing/base.py

22232425262728293031

@abc.abstractmethoddefclose(self,end_time:int|None=None):"""Close the trace entity by setting `end_time` and flip the in progress flag to False. Parameters ---------- end_time: int Time in epoch seconds, by default current time will be used. """

Source code in aws_lambda_powertools/tracing/base.py

41424344454647484950515253

@abc.abstractmethoddefput_annotation(self,key:str,value:str|numbers.Number|bool)->None:"""Annotate segment or subsegment with a key-value pair. Note: Annotations will be indexed for later search query. Parameters ---------- key: str Metadata key value: str | numbers.Number | bool Annotation value """

Source code in aws_lambda_powertools/tracing/base.py

5556575859606162636465666768

@abc.abstractmethoddefput_metadata(self,key:str,value:Any,namespace:str="default")->None:"""Add metadata to segment or subsegment. Metadata is not indexed but can be later retrieved by BatchGetTraces API. Parameters ---------- key: str Metadata key value: Any Any object that can be serialized into a JSON string namespace: set[str] Metadata namespace, by default 'default' """