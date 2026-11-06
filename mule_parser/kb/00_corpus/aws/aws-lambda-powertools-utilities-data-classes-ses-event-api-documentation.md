# aws_lambda_powertools.utilities.data_classes.ses_event API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/utilities/data_classes/ses_event.html](https://docs.aws.amazon.com/powertools/python/latest/api/utilities/data_classes/ses_event.html)

---

# Module `aws_lambda_powertools.utilities.data_classes.ses_event`

## Classes

- `class SESEvent (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class SESEvent(DictWrapper): """Amazon SES to receive message event trigger NOTE: There is a 30-second timeout on RequestResponse invocations. Documentation: -------------- - https://docs.aws.amazon.com/lambda/latest/dg/services-ses.html - https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-action-lambda.html """ @property def records(self) -> Iterator[SESEventRecord]: for record in self["Records"]: yield SESEventRecord(record) @property def record(self) -> SESEventRecord: return next(self.records) @property def mail(self) -> SESMail: return self.record.ses.mail @property def receipt(self) -> SESReceipt: return self.record.ses.receipt`Amazon SES to receive message event trigger NOTE: There is a 30-second timeout on RequestResponse invocations. ## Documentation:- [https://docs.aws.amazon.com/lambda/latest/dg/services-ses.html](https://docs.aws.amazon.com/lambda/latest/dg/services-ses.html)
- [https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-action-lambda.html](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-action-lambda.html)
 ## Parameters- `data`- `dict[str, Any]`
- Lambda Event Source Event payload
- `json_deserializer`- `Callable`, optional
- function to deserialize `str`,`bytes`,`bytearray`containing a JSON document to a Python`obj`, by default json.loads
 ### Ancestors- [DictWrapper](common.html#aws_lambda_powertools.utilities.data_classes.common.DictWrapper)
- collections.abc.Mapping
- collections.abc.Collection
- collections.abc.Sized
- collections.abc.Iterable
- collections.abc.Container
- typing.Generic
 ### Instance variables- `prop mail :`- [SESMail](#aws_lambda_powertools.utilities.data_classes.ses_event.SESMail)
- 
## Expand source code`@property def mail(self) -> SESMail: return self.record.ses.mail`
- `prop receipt :`- [SESReceipt](#aws_lambda_powertools.utilities.data_classes.ses_event.SESReceipt)
- 
## Expand source code`@property def receipt(self) -> SESReceipt: return self.record.ses.receipt`
- `prop record :`- [SESEventRecord](#aws_lambda_powertools.utilities.data_classes.ses_event.SESEventRecord)
- 
## Expand source code`@property def record(self) -> SESEventRecord: return next(self.records)`
- `prop records : Iterator[`- [SESEventRecord](#aws_lambda_powertools.utilities.data_classes.ses_event.SESEventRecord)]
- 
## Expand source code`@property def records(self) -> Iterator[SESEventRecord]: for record in self["Records"]: yield SESEventRecord(record)`
 ### Inherited members
- `class SESEventRecord (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class SESEventRecord(DictWrapper): @property def event_source(self) -> str: """The AWS service from which the SES event record originated. For SES, this is aws:ses""" return self["eventSource"] @property def event_version(self) -> str: """The eventVersion key value contains a major and minor version in the form <major>.<minor>.""" return self["eventVersion"] @property def ses(self) -> SESMessage: return SESMessage(self._data)`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
- Lambda Event Source Event payload
- `json_deserializer`- `Callable`, optional
- function to deserialize `str`,`bytes`,`bytearray`containing a JSON document to a Python`obj`, by default json.loads
 ### Ancestors- [DictWrapper](common.html#aws_lambda_powertools.utilities.data_classes.common.DictWrapper)
- collections.abc.Mapping
- collections.abc.Collection
- collections.abc.Sized
- collections.abc.Iterable
- collections.abc.Container
- typing.Generic
 ### Instance variables- `prop event_source : str`
- 
## Expand source code`@property def event_source(self) -> str: """The AWS service from which the SES event record originated. For SES, this is aws:ses""" return self["eventSource"]`The AWS service from which the SES event record originated. For SES, this is aws:ses 
- `prop event_version : str`
- 
## Expand source code`@property def event_version(self) -> str: """The eventVersion key value contains a major and minor version in the form <major>.<minor>.""" return self["eventVersion"]`The eventVersion key value contains a major and minor version in the form . . 
- `prop ses :`- [SESMessage](#aws_lambda_powertools.utilities.data_classes.ses_event.SESMessage)
- 
## Expand source code`@property def ses(self) -> SESMessage: return SESMessage(self._data)`
 ### Inherited members
- `class SESMail (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class SESMail(DictWrapper): @property def timestamp(self) -> str: """String that contains the time at which the email was received, in ISO8601 format.""" return self["timestamp"] @property def source(self) -> str: """String that contains the email address (specifically, the envelope MAIL FROM address) that the email was sent from.""" return self["source"] @property def message_id(self) -> str: """String that contains the unique ID assigned to the email by Amazon SES. If the email was delivered to Amazon S3, the message ID is also the Amazon S3 object key that was used to write the message to your Amazon S3 bucket.""" return self["messageId"] @property def destination(self) -> list[str]: """A complete list of all recipient addresses (including To: and CC: recipients) from the MIME headers of the incoming email.""" return self["destination"] @property def headers_truncated(self) -> bool: """String that specifies whether the headers were truncated in the notification, which will happen if the headers are larger than 10 KB. Possible values are true and false.""" return bool(self["headersTruncated"]) @property def headers(self) -> Iterator[SESMailHeader]: """A list of Amazon SES headers and your custom headers. Each header in the list has a name field and a value field""" for header in self["headers"]: yield SESMailHeader(header) @property def common_headers(self) -> SESMailCommonHeaders: """A list of headers common to all emails. Each header in the list is composed of a name and a value.""" return SESMailCommonHeaders(self["commonHeaders"])`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
- Lambda Event Source Event payload
- `json_deserializer`- `Callable`, optional
- function to deserialize `str`,`bytes`,`bytearray`containing a JSON document to a Python`obj`, by default json.loads
 ### Ancestors- [DictWrapper](common.html#aws_lambda_powertools.utilities.data_classes.common.DictWrapper)
- collections.abc.Mapping
- collections.abc.Collection
- collections.abc.Sized
- collections.abc.Iterable
- collections.abc.Container
- typing.Generic
 ### Instance variables- `prop common_headers :`- [SESMailCommonHeaders](#aws_lambda_powertools.utilities.data_classes.ses_event.SESMailCommonHeaders)
- 
## Expand source code`@property def common_headers(self) -> SESMailCommonHeaders: """A list of headers common to all emails. Each header in the list is composed of a name and a value.""" return SESMailCommonHeaders(self["commonHeaders"])`A list of headers common to all emails. Each header in the list is composed of a name and a value. 
- `prop destination : list[str]`
- 
## Expand source code`@property def destination(self) -> list[str]: """A complete list of all recipient addresses (including To: and CC: recipients) from the MIME headers of the incoming email.""" return self["destination"]`A complete list of all recipient addresses (including To: and CC: recipients) from the MIME headers of the incoming email. 
- `prop headers : Iterator[`- [SESMailHeader](#aws_lambda_powertools.utilities.data_classes.ses_event.SESMailHeader)]
- 
## Expand source code`@property def headers(self) -> Iterator[SESMailHeader]: """A list of Amazon SES headers and your custom headers. Each header in the list has a name field and a value field""" for header in self["headers"]: yield SESMailHeader(header)`A list of Amazon SES headers and your custom headers. Each header in the list has a name field and a value field 
- `prop headers_truncated : bool`
- 
## Expand source code`@property def headers_truncated(self) -> bool: """String that specifies whether the headers were truncated in the notification, which will happen if the headers are larger than 10 KB. Possible values are true and false.""" return bool(self["headersTruncated"])`String that specifies whether the headers were truncated in the notification, which will happen if the headers are larger than 10 KB. Possible values are true and false. 
- `prop message_id : str`
- 
## Expand source code`@property def message_id(self) -> str: """String that contains the unique ID assigned to the email by Amazon SES. If the email was delivered to Amazon S3, the message ID is also the Amazon S3 object key that was used to write the message to your Amazon S3 bucket.""" return self["messageId"]`String that contains the unique ID assigned to the email by Amazon SES. If the email was delivered to Amazon S3, the message ID is also the Amazon S3 object key that was used to write the message to your Amazon S3 bucket. 
- `prop source : str`
- 
## Expand source code`@property def source(self) -> str: """String that contains the email address (specifically, the envelope MAIL FROM address) that the email was sent from.""" return self["source"]`String that contains the email address (specifically, the envelope MAIL FROM address) that the email was sent from. 
- `prop timestamp : str`
- 
## Expand source code`@property def timestamp(self) -> str: """String that contains the time at which the email was received, in ISO8601 format.""" return self["timestamp"]`String that contains the time at which the email was received, in ISO8601 format. 
 ### Inherited members
- `class SESMailCommonHeaders (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class SESMailCommonHeaders(DictWrapper): @property def return_path(self) -> str: """The values in the Return-Path header of the email.""" return self["returnPath"] @property def get_from(self) -> list[str]: """The values in the From header of the email.""" # Note: this name conflicts with existing python builtins return self["from"] @property def date(self) -> str: """The date and time when Amazon SES received the message.""" return self["date"] @property def to(self) -> list[str]: """The values in the To header of the email.""" return self["to"] @property def message_id(self) -> str: """The ID of the original message.""" return str(self["messageId"]) @property def subject(self) -> str: """The value of the Subject header for the email.""" return str(self["subject"]) @property def cc(self) -> list[str]: """The values in the CC header of the email.""" return self.get("cc") or [] @property def bcc(self) -> list[str]: """The values in the BCC header of the email.""" return self.get("bcc") or [] @property def sender(self) -> list[str]: """The values in the Sender header of the email.""" return self.get("sender") or [] @property def reply_to(self) -> list[str]: """The values in the replyTo header of the email.""" return self.get("replyTo") or []`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
- Lambda Event Source Event payload
- `json_deserializer`- `Callable`, optional
- function to deserialize `str`,`bytes`,`bytearray`containing a JSON document to a Python`obj`, by default json.loads
 ### Ancestors- [DictWrapper](common.html#aws_lambda_powertools.utilities.data_classes.common.DictWrapper)
- collections.abc.Mapping
- collections.abc.Collection
- collections.abc.Sized
- collections.abc.Iterable
- collections.abc.Container
- typing.Generic
 ### Instance variables- `prop bcc : list[str]`
- 
## Expand source code`@property def bcc(self) -> list[str]: """The values in the BCC header of the email.""" return self.get("bcc") or []`The values in the BCC header of the email. 
- `prop cc : list[str]`
- 
## Expand source code`@property def cc(self) -> list[str]: """The values in the CC header of the email.""" return self.get("cc") or []`The values in the CC header of the email. 
- `prop date : str`
- 
## Expand source code`@property def date(self) -> str: """The date and time when Amazon SES received the message.""" return self["date"]`The date and time when Amazon SES received the message. 
- `prop get_from : list[str]`
- 
## Expand source code`@property def get_from(self) -> list[str]: """The values in the From header of the email.""" # Note: this name conflicts with existing python builtins return self["from"]`The values in the From header of the email. 
- `prop message_id : str`
- 
## Expand source code`@property def message_id(self) -> str: """The ID of the original message.""" return str(self["messageId"])`The ID of the original message. 
- `prop reply_to : list[str]`
- 
## Expand source code`@property def reply_to(self) -> list[str]: """The values in the replyTo header of the email.""" return self.get("replyTo") or []`The values in the replyTo header of the email. 
- `prop return_path : str`
- 
## Expand source code`@property def return_path(self) -> str: """The values in the Return-Path header of the email.""" return self["returnPath"]`The values in the Return-Path header of the email. 
- `prop sender : list[str]`
- 
## Expand source code`@property def sender(self) -> list[str]: """The values in the Sender header of the email.""" return self.get("sender") or []`The values in the Sender header of the email. 
- `prop subject : str`
- 
## Expand source code`@property def subject(self) -> str: """The value of the Subject header for the email.""" return str(self["subject"])`The value of the Subject header for the email. 
- `prop to : list[str]`
- 
## Expand source code`@property def to(self) -> list[str]: """The values in the To header of the email.""" return self["to"]`The values in the To header of the email. 
 ### Inherited members
- `class SESMailHeader (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class SESMailHeader(DictWrapper): @property def name(self) -> str: return self["name"] @property def value(self) -> str: return self["value"]`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
- Lambda Event Source Event payload
- `json_deserializer`- `Callable`, optional
- function to deserialize `str`,`bytes`,`bytearray`containing a JSON document to a Python`obj`, by default json.loads
 ### Ancestors- [DictWrapper](common.html#aws_lambda_powertools.utilities.data_classes.common.DictWrapper)
- collections.abc.Mapping
- collections.abc.Collection
- collections.abc.Sized
- collections.abc.Iterable
- collections.abc.Container
- typing.Generic
 ### Instance variables- `prop name : str`
- 
## Expand source code`@property def name(self) -> str: return self["name"]`
- `prop value : str`
- 
## Expand source code`@property def value(self) -> str: return self["value"]`
 ### Inherited members
- `class SESMessage (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class SESMessage(DictWrapper): @property def mail(self) -> SESMail: return SESMail(self["ses"]["mail"]) @property def receipt(self) -> SESReceipt: return SESReceipt(self["ses"]["receipt"])`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
- Lambda Event Source Event payload
- `json_deserializer`- `Callable`, optional
- function to deserialize `str`,`bytes`,`bytearray`containing a JSON document to a Python`obj`, by default json.loads
 ### Ancestors- [DictWrapper](common.html#aws_lambda_powertools.utilities.data_classes.common.DictWrapper)
- collections.abc.Mapping
- collections.abc.Collection
- collections.abc.Sized
- collections.abc.Iterable
- collections.abc.Container
- typing.Generic
 ### Instance variables- `prop mail :`- [SESMail](#aws_lambda_powertools.utilities.data_classes.ses_event.SESMail)
- 
## Expand source code`@property def mail(self) -> SESMail: return SESMail(self["ses"]["mail"])`
- `prop receipt :`- [SESReceipt](#aws_lambda_powertools.utilities.data_classes.ses_event.SESReceipt)
- 
## Expand source code`@property def receipt(self) -> SESReceipt: return SESReceipt(self["ses"]["receipt"])`
 ### Inherited members
- `class SESReceipt (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class SESReceipt(DictWrapper): @property def timestamp(self) -> str: """String that specifies the date and time at which the action was triggered, in ISO 8601 format.""" return self["timestamp"] @property def processing_time_millis(self) -> int: """String that specifies the period, in milliseconds, from the time Amazon SES received the message to the time it triggered the action.""" return int(self["processingTimeMillis"]) @property def recipients(self) -> list[str]: """A list of recipients (specifically, the envelope RCPT TO addresses) that were matched by the active receipt rule. The addresses listed here may differ from those listed by the destination field in the mail object.""" return self["recipients"] @property def spam_verdict(self) -> SESReceiptStatus: """Object that indicates whether the message is spam.""" return SESReceiptStatus(self["spamVerdict"]) @property def virus_verdict(self) -> SESReceiptStatus: """Object that indicates whether the message contains a virus.""" return SESReceiptStatus(self["virusVerdict"]) @property def spf_verdict(self) -> SESReceiptStatus: """Object that indicates whether the Sender Policy Framework (SPF) check passed.""" return SESReceiptStatus(self["spfVerdict"]) @property def dkim_verdict(self) -> SESReceiptStatus: """Object that indicates whether the DomainKeys Identified Mail (DKIM) check passed""" return SESReceiptStatus(self["dkimVerdict"]) @property def dmarc_verdict(self) -> SESReceiptStatus: """Object that indicates whether the Domain-based Message Authentication, Reporting & Conformance (DMARC) check passed.""" return SESReceiptStatus(self["dmarcVerdict"]) @property def dmarc_policy(self) -> str | None: """Indicates the Domain-based Message Authentication, Reporting & Conformance (DMARC) settings for the sending domain. This field only appears if the message fails DMARC authentication. Possible values for this field are: none, quarantine, reject""" return self.get("dmarcPolicy") @property def action(self) -> SESReceiptAction: """Object that encapsulates information about the action that was executed.""" return SESReceiptAction(self["action"])`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
- Lambda Event Source Event payload
- `json_deserializer`- `Callable`, optional
- function to deserialize `str`,`bytes`,`bytearray`containing a JSON document to a Python`obj`, by default json.loads
 ### Ancestors- [DictWrapper](common.html#aws_lambda_powertools.utilities.data_classes.common.DictWrapper)
- collections.abc.Mapping
- collections.abc.Collection
- collections.abc.Sized
- collections.abc.Iterable
- collections.abc.Container
- typing.Generic
 ### Instance variables- `prop action :`- [SESReceiptAction](#aws_lambda_powertools.utilities.data_classes.ses_event.SESReceiptAction)
- 
## Expand source code`@property def action(self) -> SESReceiptAction: """Object that encapsulates information about the action that was executed.""" return SESReceiptAction(self["action"])`Object that encapsulates information about the action that was executed. 
- `prop dkim_verdict :`- [SESReceiptStatus](#aws_lambda_powertools.utilities.data_classes.ses_event.SESReceiptStatus)
- 
## Expand source code`@property def dkim_verdict(self) -> SESReceiptStatus: """Object that indicates whether the DomainKeys Identified Mail (DKIM) check passed""" return SESReceiptStatus(self["dkimVerdict"])`Object that indicates whether the DomainKeys Identified Mail (DKIM) check passed 
- `prop dmarc_policy : str | None`
- 
## Expand source code`@property def dmarc_policy(self) -> str | None: """Indicates the Domain-based Message Authentication, Reporting & Conformance (DMARC) settings for the sending domain. This field only appears if the message fails DMARC authentication. Possible values for this field are: none, quarantine, reject""" return self.get("dmarcPolicy")`Indicates the Domain-based Message Authentication, Reporting & Conformance (DMARC) settings for the sending domain. This field only appears if the message fails DMARC authentication. Possible values for this field are: none, quarantine, reject 
- `prop dmarc_verdict :`- [SESReceiptStatus](#aws_lambda_powertools.utilities.data_classes.ses_event.SESReceiptStatus)
- 
## Expand source code`@property def dmarc_verdict(self) -> SESReceiptStatus: """Object that indicates whether the Domain-based Message Authentication, Reporting & Conformance (DMARC) check passed.""" return SESReceiptStatus(self["dmarcVerdict"])`Object that indicates whether the Domain-based Message Authentication, Reporting & Conformance (DMARC) check passed. 
- `prop processing_time_millis : int`
- 
## Expand source code`@property def processing_time_millis(self) -> int: """String that specifies the period, in milliseconds, from the time Amazon SES received the message to the time it triggered the action.""" return int(self["processingTimeMillis"])`String that specifies the period, in milliseconds, from the time Amazon SES received the message to the time it triggered the action. 
- `prop recipients : list[str]`
- 
## Expand source code`@property def recipients(self) -> list[str]: """A list of recipients (specifically, the envelope RCPT TO addresses) that were matched by the active receipt rule. The addresses listed here may differ from those listed by the destination field in the mail object.""" return self["recipients"]`A list of recipients (specifically, the envelope RCPT TO addresses) that were matched by the active receipt rule. The addresses listed here may differ from those listed by the destination field in the mail object. 
- `prop spam_verdict :`- [SESReceiptStatus](#aws_lambda_powertools.utilities.data_classes.ses_event.SESReceiptStatus)
- 
## Expand source code`@property def spam_verdict(self) -> SESReceiptStatus: """Object that indicates whether the message is spam.""" return SESReceiptStatus(self["spamVerdict"])`Object that indicates whether the message is spam. 
- `prop spf_verdict :`- [SESReceiptStatus](#aws_lambda_powertools.utilities.data_classes.ses_event.SESReceiptStatus)
- 
## Expand source code`@property def spf_verdict(self) -> SESReceiptStatus: """Object that indicates whether the Sender Policy Framework (SPF) check passed.""" return SESReceiptStatus(self["spfVerdict"])`Object that indicates whether the Sender Policy Framework (SPF) check passed. 
- `prop timestamp : str`
- 
## Expand source code`@property def timestamp(self) -> str: """String that specifies the date and time at which the action was triggered, in ISO 8601 format.""" return self["timestamp"]`String that specifies the date and time at which the action was triggered, in ISO 8601 format. 
- `prop virus_verdict :`- [SESReceiptStatus](#aws_lambda_powertools.utilities.data_classes.ses_event.SESReceiptStatus)
- 
## Expand source code`@property def virus_verdict(self) -> SESReceiptStatus: """Object that indicates whether the message contains a virus.""" return SESReceiptStatus(self["virusVerdict"])`Object that indicates whether the message contains a virus. 
 ### Inherited members
- `class SESReceiptAction (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class SESReceiptAction(DictWrapper): @property def get_type(self) -> str: """String that indicates the type of action that was executed. Possible values are S3, SNS, Bounce, Lambda, Stop, and WorkMail """ # Note: this name conflicts with existing python builtins return self["type"] @property def topic_arn(self) -> str | None: """String that contains the Amazon Resource Name (ARN) of the Amazon SNS topic to which the notification was published.""" return self.get("topicArn") @property def function_arn(self) -> str: """String that contains the ARN of the Lambda function that was triggered. Present only for the Lambda action type.""" return self["functionArn"] @property def invocation_type(self) -> str: """String that contains the invocation type of the Lambda function. Possible values are RequestResponse and Event. Present only for the Lambda action type.""" return self["invocationType"]`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
- Lambda Event Source Event payload
- `json_deserializer`- `Callable`, optional
- function to deserialize `str`,`bytes`,`bytearray`containing a JSON document to a Python`obj`, by default json.loads
 ### Ancestors- [DictWrapper](common.html#aws_lambda_powertools.utilities.data_classes.common.DictWrapper)
- collections.abc.Mapping
- collections.abc.Collection
- collections.abc.Sized
- collections.abc.Iterable
- collections.abc.Container
- typing.Generic
 ### Instance variables- `prop function_arn : str`
- 
## Expand source code`@property def function_arn(self) -> str: """String that contains the ARN of the Lambda function that was triggered. Present only for the Lambda action type.""" return self["functionArn"]`String that contains the ARN of the Lambda function that was triggered. Present only for the Lambda action type. 
- `prop get_type : str`
- 
## Expand source code`@property def get_type(self) -> str: """String that indicates the type of action that was executed. Possible values are S3, SNS, Bounce, Lambda, Stop, and WorkMail """ # Note: this name conflicts with existing python builtins return self["type"]`String that indicates the type of action that was executed. Possible values are S3, SNS, Bounce, Lambda, Stop, and WorkMail 
- `prop invocation_type : str`
- 
## Expand source code`@property def invocation_type(self) -> str: """String that contains the invocation type of the Lambda function. Possible values are RequestResponse and Event. Present only for the Lambda action type.""" return self["invocationType"]`String that contains the invocation type of the Lambda function. Possible values are RequestResponse and Event. Present only for the Lambda action type. 
- `prop topic_arn : str | None`
- 
## Expand source code`@property def topic_arn(self) -> str | None: """String that contains the Amazon Resource Name (ARN) of the Amazon SNS topic to which the notification was published.""" return self.get("topicArn")`String that contains the Amazon Resource Name (ARN) of the Amazon SNS topic to which the notification was published. 
 ### Inherited members
- `class SESReceiptStatus (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class SESReceiptStatus(DictWrapper): @property def status(self) -> str: """Receipt status Possible values: 'PASS', 'FAIL', 'GRAY', 'PROCESSING_FAILED', 'DISABLED' """ return str(self["status"])`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
- Lambda Event Source Event payload
- `json_deserializer`- `Callable`, optional
- function to deserialize `str`,`bytes`,`bytearray`containing a JSON document to a Python`obj`, by default json.loads
 ### Ancestors- [DictWrapper](common.html#aws_lambda_powertools.utilities.data_classes.common.DictWrapper)
- collections.abc.Mapping
- collections.abc.Collection
- collections.abc.Sized
- collections.abc.Iterable
- collections.abc.Container
- typing.Generic
 ### Instance variables- `prop status : str`
- 
## Expand source code`@property def status(self) -> str: """Receipt status Possible values: 'PASS', 'FAIL', 'GRAY', 'PROCESSING_FAILED', 'DISABLED' """ return str(self["status"])`Receipt status Possible values: 'PASS', 'FAIL', 'GRAY', 'PROCESSING_FAILED', 'DISABLED' 
 ### Inherited members