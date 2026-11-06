# aws_lambda_powertools.utilities.data_classes.kinesis_firehose_event API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/utilities/data_classes/kinesis_firehose_event.html](https://docs.aws.amazon.com/powertools/python/latest/api/utilities/data_classes/kinesis_firehose_event.html)

---

# Module `aws_lambda_powertools.utilities.data_classes.kinesis_firehose_event`

## Classes

- `class KinesisFirehoseDataTransformationRecord (record_id: str,`
 result: "Literal['Ok', 'Dropped', 'ProcessingFailed']" = 'Ok',
 data: str = '',
 metadata:- [KinesisFirehoseDataTransformationRecordMetadata](#aws_lambda_powertools.utilities.data_classes.kinesis_firehose_event.KinesisFirehoseDataTransformationRecordMetadata)| None = None,
 json_serializer: Callable = <function dumps>,
 json_deserializer: Callable = <function loads>)
- 
## Expand source code`@dataclass(repr=False, order=False) class KinesisFirehoseDataTransformationRecord: """Record in Kinesis Data Firehose response object. Parameters ---------- record_id: str uniquely identifies this record within the current batch result: Literal["Ok", "Dropped", "ProcessingFailed"] record data transformation status, whether it succeeded, should be dropped, or failed. data: str base64-encoded payload, by default empty string. Use `data_from_text` or `data_from_json` methods to convert data if needed. metadata: KinesisFirehoseDataTransformationRecordMetadata | None Metadata associated with this record; can contain partition keys. See: https://docs.aws.amazon.com/firehose/latest/dev/dynamic-partitioning.html json_serializer: Callable function to serialize `obj` to a JSON formatted `str`, by default json.dumps json_deserializer: Callable function to deserialize `str`, `bytes`, bytearray` containing a JSON document to a Python `obj`, by default json.loads Documentation: -------------- - https://docs.aws.amazon.com/firehose/latest/dev/data-transformation.html """ _valid_result_types: ClassVar[tuple[str, str, str]] = ("Ok", "Dropped", "ProcessingFailed") record_id: str result: Literal["Ok", "Dropped", "ProcessingFailed"] = "Ok" data: str = "" metadata: KinesisFirehoseDataTransformationRecordMetadata | None = None json_serializer: Callable = json.dumps json_deserializer: Callable = json.loads def asdict(self) -> dict: if self.result not in self._valid_result_types: warnings.warn( stacklevel=1, message=f'The result "{self.result}" is not valid, Choose from "Ok", "Dropped", "ProcessingFailed"', ) record: dict[str, Any] = { "recordId": self.record_id, "result": self.result, "data": self.data, } if self.metadata: record["metadata"] = self.metadata.asdict() return record @property def data_as_bytes(self) -> bytes: """Decoded base64-encoded data as bytes""" if not self.data: return b"" return base64.b64decode(self.data) @property def data_as_text(self) -> str: """Decoded base64-encoded data as text""" if not self.data: return "" return self.data_as_bytes.decode("utf-8") @cached_property def data_as_json(self) -> dict: """Decoded base64-encoded data loaded to json""" if not self.data: return {} return self.json_deserializer(self.data_as_text)`Record in Kinesis Data Firehose response object. ## Parameters- `record_id`- `str`
- uniquely identifies this record within the current batch
- `result`- `Literal["Ok", "Dropped", "ProcessingFailed"]`
- record data transformation status, whether it succeeded, should be dropped, or failed.
- `data`- `str`
- 
base64-encoded payload, by default empty string. Use `data_from_text`or`data_from_json`methods to convert data if needed.
- `metadata`- `KinesisFirehoseDataTransformationRecordMetadata | None`
- 
Metadata associated with this record; can contain partition keys. See: [https://docs.aws.amazon.com/firehose/latest/dev/dynamic-partitioning.html](https://docs.aws.amazon.com/firehose/latest/dev/dynamic-partitioning.html)
- `json_serializer`- `Callable`
- function to serialize `obj`to a JSON formatted`str`, by default json.dumps
- `json_deserializer`- `Callable`
- function to deserialize `str`,`bytes`, bytearray`containing a JSON document to a Python`obj`, by default json.loads
 ## Documentation:### Class variables- `var data : str`
- `var metadata :`- [KinesisFirehoseDataTransformationRecordMetadata](#aws_lambda_powertools.utilities.data_classes.kinesis_firehose_event.KinesisFirehoseDataTransformationRecordMetadata)| None
- `var record_id : str`
- `var result : Literal['Ok', 'Dropped', 'ProcessingFailed']`
 ### Instance variables- `prop data_as_bytes : bytes`
- 
## Expand source code`@property def data_as_bytes(self) -> bytes: """Decoded base64-encoded data as bytes""" if not self.data: return b"" return base64.b64decode(self.data)`Decoded base64-encoded data as bytes 
- `var data_as_json : dict`
- 
## Expand source code`@cached_property def data_as_json(self) -> dict: """Decoded base64-encoded data loaded to json""" if not self.data: return {} return self.json_deserializer(self.data_as_text)`Decoded base64-encoded data loaded to json 
- `prop data_as_text : str`
- 
## Expand source code`@property def data_as_text(self) -> str: """Decoded base64-encoded data as text""" if not self.data: return "" return self.data_as_bytes.decode("utf-8")`Decoded base64-encoded data as text 
 ### Methods- `def asdict(self) ‑> dict`
- 
## Expand source code`def asdict(self) -> dict: if self.result not in self._valid_result_types: warnings.warn( stacklevel=1, message=f'The result "{self.result}" is not valid, Choose from "Ok", "Dropped", "ProcessingFailed"', ) record: dict[str, Any] = { "recordId": self.record_id, "result": self.result, "data": self.data, } if self.metadata: record["metadata"] = self.metadata.asdict() return record`
- `def json_deserializer(s,`
 *,
 cls=None,
 object_hook=None,
 parse_float=None,
 parse_int=None,
 parse_constant=None,
 object_pairs_hook=None,
 **kw)
- 
## Expand source code`def loads(s, *, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw): """Deserialize ``s`` (a ``str``, ``bytes`` or ``bytearray`` instance containing a JSON document) to a Python object. ``object_hook`` is an optional function that will be called with the result of any object literal decode (a ``dict``). The return value of ``object_hook`` will be used instead of the ``dict``. This feature can be used to implement custom decoders (e.g. JSON-RPC class hinting). ``object_pairs_hook`` is an optional function that will be called with the result of any object literal decoded with an ordered list of pairs. The return value of ``object_pairs_hook`` will be used instead of the ``dict``. This feature can be used to implement custom decoders. If ``object_hook`` is also defined, the ``object_pairs_hook`` takes priority. ``parse_float``, if specified, will be called with the string of every JSON float to be decoded. By default this is equivalent to float(num_str). This can be used to use another datatype or parser for JSON floats (e.g. decimal.Decimal). ``parse_int``, if specified, will be called with the string of every JSON int to be decoded. By default this is equivalent to int(num_str). This can be used to use another datatype or parser for JSON integers (e.g. float). ``parse_constant``, if specified, will be called with one of the following strings: -Infinity, Infinity, NaN. This can be used to raise an exception if invalid JSON numbers are encountered. To use a custom ``JSONDecoder`` subclass, specify it with the ``cls`` kwarg; otherwise ``JSONDecoder`` is used. """ if isinstance(s, str): if s.startswith('\ufeff'): raise JSONDecodeError("Unexpected UTF-8 BOM (decode using utf-8-sig)", s, 0) else: if not isinstance(s, (bytes, bytearray)): raise TypeError(f'the JSON object must be str, bytes or bytearray, ' f'not {s.__class__.__name__}') s = s.decode(detect_encoding(s), 'surrogatepass') if (cls is None and object_hook is None and parse_int is None and parse_float is None and parse_constant is None and object_pairs_hook is None and not kw): return _default_decoder.decode(s) if cls is None: cls = JSONDecoder if object_hook is not None: kw['object_hook'] = object_hook if object_pairs_hook is not None: kw['object_pairs_hook'] = object_pairs_hook if parse_float is not None: kw['parse_float'] = parse_float if parse_int is not None: kw['parse_int'] = parse_int if parse_constant is not None: kw['parse_constant'] = parse_constant return cls(**kw).decode(s)`Deserialize `s`(a`str`,`bytes`or`bytearray`instance containing a JSON document) to a Python object.`object_hook`is an optional function that will be called with the result of any object literal decode (a`dict`). The return value of`object_hook`will be used instead of the`dict`. This feature can be used to implement custom decoders (e.g. JSON-RPC class hinting).`object_pairs_hook`is an optional function that will be called with the result of any object literal decoded with an ordered list of pairs. The return value of`object_pairs_hook`will be used instead of the`dict`. This feature can be used to implement custom decoders. If`object_hook`is also defined, the`object_pairs_hook`takes priority.`parse_float`, if specified, will be called with the string of every JSON float to be decoded. By default this is equivalent to float(num_str). This can be used to use another datatype or parser for JSON floats (e.g. decimal.Decimal).`parse_int`, if specified, will be called with the string of every JSON int to be decoded. By default this is equivalent to int(num_str). This can be used to use another datatype or parser for JSON integers (e.g. float).`parse_constant`, if specified, will be called with one of the following strings: -Infinity, Infinity, NaN. This can be used to raise an exception if invalid JSON numbers are encountered.To use a custom `JSONDecoder`subclass, specify it with the`cls`kwarg; otherwise`JSONDecoder`is used.
- `def json_serializer(obj,`
 *,
 skipkeys=False,
 ensure_ascii=True,
 check_circular=True,
 allow_nan=True,
 cls=None,
 indent=None,
 separators=None,
 default=None,
 sort_keys=False,
 **kw)
- 
## Expand source code`def dumps(obj, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw): """Serialize ``obj`` to a JSON formatted ``str``. If ``skipkeys`` is true then ``dict`` keys that are not basic types (``str``, ``int``, ``float``, ``bool``, ``None``) will be skipped instead of raising a ``TypeError``. If ``ensure_ascii`` is false, then the return value can contain non-ASCII characters if they appear in strings contained in ``obj``. Otherwise, all such characters are escaped in JSON strings. If ``check_circular`` is false, then the circular reference check for container types will be skipped and a circular reference will result in an ``RecursionError`` (or worse). If ``allow_nan`` is false, then it will be a ``ValueError`` to serialize out of range ``float`` values (``nan``, ``inf``, ``-inf``) in strict compliance of the JSON specification, instead of using the JavaScript equivalents (``NaN``, ``Infinity``, ``-Infinity``). If ``indent`` is a non-negative integer, then JSON array elements and object members will be pretty-printed with that indent level. An indent level of 0 will only insert newlines. ``None`` is the most compact representation. If specified, ``separators`` should be an ``(item_separator, key_separator)`` tuple. The default is ``(', ', ': ')`` if *indent* is ``None`` and ``(',', ': ')`` otherwise. To get the most compact JSON representation, you should specify ``(',', ':')`` to eliminate whitespace. ``default(obj)`` is a function that should return a serializable version of obj or raise TypeError. The default simply raises TypeError. If *sort_keys* is true (default: ``False``), then the output of dictionaries will be sorted by key. To use a custom ``JSONEncoder`` subclass (e.g. one that overrides the ``.default()`` method to serialize additional types), specify it with the ``cls`` kwarg; otherwise ``JSONEncoder`` is used. """ # cached encoder if (not skipkeys and ensure_ascii and check_circular and allow_nan and cls is None and indent is None and separators is None and default is None and not sort_keys and not kw): return _default_encoder.encode(obj) if cls is None: cls = JSONEncoder return cls( skipkeys=skipkeys, ensure_ascii=ensure_ascii, check_circular=check_circular, allow_nan=allow_nan, indent=indent, separators=separators, default=default, sort_keys=sort_keys, **kw).encode(obj)`Serialize `obj`to a JSON formatted`str`.If `skipkeys`is true then`dict`keys that are not basic types (`str`,`int`,`float`,`bool`,`None`) will be skipped instead of raising a`TypeError`.If `ensure_ascii`is false, then the return value can contain non-ASCII characters if they appear in strings contained in`obj`. Otherwise, all such characters are escaped in JSON strings.If `check_circular`is false, then the circular reference check for container types will be skipped and a circular reference will result in an`RecursionError`(or worse).If `allow_nan`is false, then it will be a`ValueError`to serialize out of range`float`values (`nan`,`inf`,`-inf`) in strict compliance of the JSON specification, instead of using the JavaScript equivalents (`NaN`,`Infinity`,`-Infinity`).If `indent`is a non-negative integer, then JSON array elements and object members will be pretty-printed with that indent level. An indent level of 0 will only insert newlines.`None`is the most compact representation.If specified, `separators`should be an`(item_separator, key_separator)`tuple. The default is`(', ', ': ')`if*indent*is`None`and`(',', ': ')`otherwise. To get the most compact JSON representation, you should specify`(',', ':')`to eliminate whitespace.`default(obj)`is a function that should return a serializable version of obj or raise TypeError. The default simply raises TypeError.If *sort_keys*is true (default:`False`), then the output of dictionaries will be sorted by key.To use a custom `JSONEncoder`subclass (e.g. one that overrides the`.default()`method to serialize additional types), specify it with the`cls`kwarg; otherwise`JSONEncoder`is used.
 
- `class KinesisFirehoseDataTransformationRecordMetadata (partition_keys: dict[str, str] = <factory>)`
- 
## Expand source code`@dataclass(repr=False, order=False, frozen=True) class KinesisFirehoseDataTransformationRecordMetadata: """ Metadata in Firehose Data Transform Record. Parameters ---------- partition_keys: dict[str, str] A dict of partition keys/value in string format, e.g. `{"year":"2023","month":"09"}` Documentation: -------------- - https://docs.aws.amazon.com/firehose/latest/dev/dynamic-partitioning.html """ partition_keys: dict[str, str] = field(default_factory=lambda: {}) def asdict(self) -> dict: if self.partition_keys is not None: return {"partitionKeys": self.partition_keys} return {}`Metadata in Firehose Data Transform Record. ## Parameters- `partition_keys`- `dict[str, str]`
- A dict of partition keys/value in string format, e.g. `{"year":"2023","month":"09"}`
 ## Documentation:### Class variables- `var partition_keys : dict[str, str]`
 ### Methods- `def asdict(self) ‑> dict`
- 
## Expand source code`def asdict(self) -> dict: if self.partition_keys is not None: return {"partitionKeys": self.partition_keys} return {}`
 
- `class KinesisFirehoseDataTransformationResponse (records: list[`- [KinesisFirehoseDataTransformationRecord](#aws_lambda_powertools.utilities.data_classes.kinesis_firehose_event.KinesisFirehoseDataTransformationRecord)] = <factory>)
- 
## Expand source code`@dataclass(repr=False, order=False) class KinesisFirehoseDataTransformationResponse: """Kinesis Data Firehose response object Documentation: -------------- - https://docs.aws.amazon.com/firehose/latest/dev/data-transformation.html Parameters ---------- records : list[KinesisFirehoseResponseRecord] records of Kinesis Data Firehose response object, optional parameter at start. can be added later using `add_record` function. Examples -------- **Transforming data records** ```python from aws_lambda_powertools.utilities.data_classes import ( KinesisFirehoseDataTransformationRecord, KinesisFirehoseDataTransformationResponse, KinesisFirehoseEvent, ) from aws_lambda_powertools.utilities.serialization import base64_from_json from aws_lambda_powertools.utilities.typing import LambdaContext def lambda_handler(event: dict, context: LambdaContext): firehose_event = KinesisFirehoseEvent(event) result = KinesisFirehoseDataTransformationResponse() for record in firehose_event.records: payload = record.data_as_text # base64 decoded data as str ## generate data to return transformed_data = {"tool_used": "powertools_dataclass", "original_payload": payload} processed_record = KinesisFirehoseDataTransformationRecord( record_id=record.record_id, data=base64_from_json(transformed_data), ) result.add_record(processed_record) # return transformed records return result.asdict() ``` """ records: list[KinesisFirehoseDataTransformationRecord] = field(default_factory=list) def add_record(self, record: KinesisFirehoseDataTransformationRecord): self.records.append(record) def asdict(self) -> dict: if not self.records: raise ValueError("Amazon Kinesis Data Firehose doesn't accept empty response") return {"records": [record.asdict() for record in self.records]}`Kinesis Data Firehose response object ## Documentation:## Parameters- `records`- `list[KinesisFirehoseResponseRecord]`
- records of Kinesis Data Firehose response object,
optional parameter at start. can be added later using `add_record`function.
 ## Examples**Transforming data records**`from aws_lambda_powertools.utilities.data_classes import ( KinesisFirehoseDataTransformationRecord, KinesisFirehoseDataTransformationResponse, KinesisFirehoseEvent, ) from aws_lambda_powertools.utilities.serialization import base64_from_json from aws_lambda_powertools.utilities.typing import LambdaContext def lambda_handler(event: dict, context: LambdaContext): firehose_event = KinesisFirehoseEvent(event) result = KinesisFirehoseDataTransformationResponse() for record in firehose_event.records: payload = record.data_as_text # base64 decoded data as str ## generate data to return transformed_data = {"tool_used": "powertools_dataclass", "original_payload": payload} processed_record = KinesisFirehoseDataTransformationRecord( record_id=record.record_id, data=base64_from_json(transformed_data), ) result.add_record(processed_record) # return transformed records return result.asdict()`### Class variables- `var records : list[`- [KinesisFirehoseDataTransformationRecord](#aws_lambda_powertools.utilities.data_classes.kinesis_firehose_event.KinesisFirehoseDataTransformationRecord)]
 ### Methods- `def add_record(self,`
 record:- [KinesisFirehoseDataTransformationRecord](#aws_lambda_powertools.utilities.data_classes.kinesis_firehose_event.KinesisFirehoseDataTransformationRecord))
- 
## Expand source code`def add_record(self, record: KinesisFirehoseDataTransformationRecord): self.records.append(record)`
- `def asdict(self) ‑> dict`
- 
## Expand source code`def asdict(self) -> dict: if not self.records: raise ValueError("Amazon Kinesis Data Firehose doesn't accept empty response") return {"records": [record.asdict() for record in self.records]}`
 
- `class KinesisFirehoseEvent (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class KinesisFirehoseEvent(DictWrapper): """Kinesis Data Firehose event Documentation: -------------- - https://docs.aws.amazon.com/lambda/latest/dg/services-kinesisfirehose.html """ @property def invocation_id(self) -> str: """Unique ID for for Lambda invocation""" return self["invocationId"] @property def delivery_stream_arn(self) -> str: """ARN of the Firehose Data Firehose Delivery Stream""" return self["deliveryStreamArn"] @property def source_kinesis_stream_arn(self) -> str | None: """ARN of the Kinesis Stream; present only when Kinesis Stream is source""" return self.get("sourceKinesisStreamArn") @property def region(self) -> str: """AWS region where the event originated eg: us-east-1""" return self["region"] @property def records(self) -> Iterator[KinesisFirehoseRecord]: for record in self["records"]: yield KinesisFirehoseRecord(data=record, json_deserializer=self._json_deserializer)`Kinesis Data Firehose event ## Documentation:## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop delivery_stream_arn : str`
- 
## Expand source code`@property def delivery_stream_arn(self) -> str: """ARN of the Firehose Data Firehose Delivery Stream""" return self["deliveryStreamArn"]`ARN of the Firehose Data Firehose Delivery Stream 
- `prop invocation_id : str`
- 
## Expand source code`@property def invocation_id(self) -> str: """Unique ID for for Lambda invocation""" return self["invocationId"]`Unique ID for for Lambda invocation 
- `prop records : Iterator[`- [KinesisFirehoseRecord](#aws_lambda_powertools.utilities.data_classes.kinesis_firehose_event.KinesisFirehoseRecord)]
- 
## Expand source code`@property def records(self) -> Iterator[KinesisFirehoseRecord]: for record in self["records"]: yield KinesisFirehoseRecord(data=record, json_deserializer=self._json_deserializer)`
- `prop region : str`
- 
## Expand source code`@property def region(self) -> str: """AWS region where the event originated eg: us-east-1""" return self["region"]`AWS region where the event originated eg: us-east-1 
- `prop source_kinesis_stream_arn : str | None`
- 
## Expand source code`@property def source_kinesis_stream_arn(self) -> str | None: """ARN of the Kinesis Stream; present only when Kinesis Stream is source""" return self.get("sourceKinesisStreamArn")`ARN of the Kinesis Stream; present only when Kinesis Stream is source 
 ### Inherited members
- `class KinesisFirehoseRecord (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class KinesisFirehoseRecord(DictWrapper): @property def approximate_arrival_timestamp(self) -> int: """The approximate time that the record was inserted into the delivery stream""" return self["approximateArrivalTimestamp"] @property def record_id(self) -> str: """Record ID; uniquely identifies this record within the current batch""" return self["recordId"] @property def data(self) -> str: """The data blob, base64-encoded""" return self["data"] @property def metadata(self) -> KinesisFirehoseRecordMetadata | None: """Optional: metadata associated with this record; present only when Kinesis Stream is source""" return KinesisFirehoseRecordMetadata(self._data) if self.get("kinesisRecordMetadata") else None @property def data_as_bytes(self) -> bytes: """Decoded base64-encoded data as bytes""" return base64.b64decode(self.data) @property def data_as_text(self) -> str: """Decoded base64-encoded data as text""" return self.data_as_bytes.decode("utf-8") @cached_property def data_as_json(self) -> dict: """Decoded base64-encoded data loaded to json""" return self._json_deserializer(self.data_as_text) def build_data_transformation_response( self, result: Literal["Ok", "Dropped", "ProcessingFailed"] = "Ok", data: str = "", metadata: KinesisFirehoseDataTransformationRecordMetadata | None = None, ) -> KinesisFirehoseDataTransformationRecord: """Create a KinesisFirehoseResponseRecord directly using the record_id and given values Parameters ---------- result : Literal["Ok", "Dropped", "ProcessingFailed"] processing result, supported value: Ok, Dropped, ProcessingFailed data : str, optional data blob, base64-encoded, optional at init. Allows pass in base64-encoded data directly or use either function like `data_from_text`, `data_from_json` to populate data metadata: KinesisFirehoseResponseRecordMetadata, optional Metadata associated with this record; can contain partition keys - https://docs.aws.amazon.com/firehose/latest/dev/dynamic-partitioning.html """ return KinesisFirehoseDataTransformationRecord( record_id=self.record_id, result=result, data=data, metadata=metadata, )`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop approximate_arrival_timestamp : int`
- 
## Expand source code`@property def approximate_arrival_timestamp(self) -> int: """The approximate time that the record was inserted into the delivery stream""" return self["approximateArrivalTimestamp"]`The approximate time that the record was inserted into the delivery stream 
- `prop data : str`
- 
## Expand source code`@property def data(self) -> str: """The data blob, base64-encoded""" return self["data"]`The data blob, base64-encoded 
- `prop data_as_bytes : bytes`
- 
## Expand source code`@property def data_as_bytes(self) -> bytes: """Decoded base64-encoded data as bytes""" return base64.b64decode(self.data)`Decoded base64-encoded data as bytes 
- `var data_as_json : dict`
- 
## Expand source code`@cached_property def data_as_json(self) -> dict: """Decoded base64-encoded data loaded to json""" return self._json_deserializer(self.data_as_text)`Decoded base64-encoded data loaded to json 
- `prop data_as_text : str`
- 
## Expand source code`@property def data_as_text(self) -> str: """Decoded base64-encoded data as text""" return self.data_as_bytes.decode("utf-8")`Decoded base64-encoded data as text 
- `prop metadata :`- [KinesisFirehoseRecordMetadata](#aws_lambda_powertools.utilities.data_classes.kinesis_firehose_event.KinesisFirehoseRecordMetadata)| None
- 
## Expand source code`@property def metadata(self) -> KinesisFirehoseRecordMetadata | None: """Optional: metadata associated with this record; present only when Kinesis Stream is source""" return KinesisFirehoseRecordMetadata(self._data) if self.get("kinesisRecordMetadata") else None`Optional: metadata associated with this record; present only when Kinesis Stream is source 
- `prop record_id : str`
- 
## Expand source code`@property def record_id(self) -> str: """Record ID; uniquely identifies this record within the current batch""" return self["recordId"]`Record ID; uniquely identifies this record within the current batch 
 ### Methods- `def build_data_transformation_response(self,`
 result: "Literal['Ok', 'Dropped', 'ProcessingFailed']" = 'Ok',
 data: str = '',
 metadata:- [KinesisFirehoseDataTransformationRecordMetadata](#aws_lambda_powertools.utilities.data_classes.kinesis_firehose_event.KinesisFirehoseDataTransformationRecordMetadata)| None = None) ‑>- [KinesisFirehoseDataTransformationRecord](#aws_lambda_powertools.utilities.data_classes.kinesis_firehose_event.KinesisFirehoseDataTransformationRecord)
- 
## Expand source code`def build_data_transformation_response( self, result: Literal["Ok", "Dropped", "ProcessingFailed"] = "Ok", data: str = "", metadata: KinesisFirehoseDataTransformationRecordMetadata | None = None, ) -> KinesisFirehoseDataTransformationRecord: """Create a KinesisFirehoseResponseRecord directly using the record_id and given values Parameters ---------- result : Literal["Ok", "Dropped", "ProcessingFailed"] processing result, supported value: Ok, Dropped, ProcessingFailed data : str, optional data blob, base64-encoded, optional at init. Allows pass in base64-encoded data directly or use either function like `data_from_text`, `data_from_json` to populate data metadata: KinesisFirehoseResponseRecordMetadata, optional Metadata associated with this record; can contain partition keys - https://docs.aws.amazon.com/firehose/latest/dev/dynamic-partitioning.html """ return KinesisFirehoseDataTransformationRecord( record_id=self.record_id, result=result, data=data, metadata=metadata, )`Create a KinesisFirehoseResponseRecord directly using the record_id and given values ## Parameters- `result`- `Literal["Ok", "Dropped", "ProcessingFailed"]`
- processing result, supported value: Ok, Dropped, ProcessingFailed
- `data`- `str`, optional
- data blob, base64-encoded, optional at init. Allows pass in base64-encoded data directly or
use either function like `data_from_text`,`data_from_json`to populate data
- `metadata`- `KinesisFirehoseResponseRecordMetadata`, optional
- Metadata associated with this record; can contain partition keys
- [https://docs.aws.amazon.com/firehose/latest/dev/dynamic-partitioning.html](https://docs.aws.amazon.com/firehose/latest/dev/dynamic-partitioning.html)
 
 ### Inherited members
- `class KinesisFirehoseRecordMetadata (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class KinesisFirehoseRecordMetadata(DictWrapper): @property def _metadata(self) -> dict: """Optional: metadata associated with this record; present only when Kinesis Stream is source""" return self["kinesisRecordMetadata"] # could raise KeyError @property def shard_id(self) -> str: """Kinesis stream shard ID; present only when Kinesis Stream is source""" return self._metadata["shardId"] @property def partition_key(self) -> str: """Kinesis stream partition key; present only when Kinesis Stream is source""" return self._metadata["partitionKey"] @property def approximate_arrival_timestamp(self) -> int: """Kinesis stream approximate arrival ISO timestamp; present only when Kinesis Stream is source""" return self._metadata["approximateArrivalTimestamp"] @property def sequence_number(self) -> str: """Kinesis stream sequence number; present only when Kinesis Stream is source""" return self._metadata["sequenceNumber"] @property def subsequence_number(self) -> int: """Kinesis stream sub-sequence number; present only when Kinesis Stream is source Note: this will only be present for Kinesis streams using record aggregation """ return self._metadata["subsequenceNumber"]`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop approximate_arrival_timestamp : int`
- 
## Expand source code`@property def approximate_arrival_timestamp(self) -> int: """Kinesis stream approximate arrival ISO timestamp; present only when Kinesis Stream is source""" return self._metadata["approximateArrivalTimestamp"]`Kinesis stream approximate arrival ISO timestamp; present only when Kinesis Stream is source 
- `prop partition_key : str`
- 
## Expand source code`@property def partition_key(self) -> str: """Kinesis stream partition key; present only when Kinesis Stream is source""" return self._metadata["partitionKey"]`Kinesis stream partition key; present only when Kinesis Stream is source 
- `prop sequence_number : str`
- 
## Expand source code`@property def sequence_number(self) -> str: """Kinesis stream sequence number; present only when Kinesis Stream is source""" return self._metadata["sequenceNumber"]`Kinesis stream sequence number; present only when Kinesis Stream is source 
- `prop shard_id : str`
- 
## Expand source code`@property def shard_id(self) -> str: """Kinesis stream shard ID; present only when Kinesis Stream is source""" return self._metadata["shardId"]`Kinesis stream shard ID; present only when Kinesis Stream is source 
- `prop subsequence_number : int`
- 
## Expand source code`@property def subsequence_number(self) -> int: """Kinesis stream sub-sequence number; present only when Kinesis Stream is source Note: this will only be present for Kinesis streams using record aggregation """ return self._metadata["subsequenceNumber"]`Kinesis stream sub-sequence number; present only when Kinesis Stream is source Note: this will only be present for Kinesis streams using record aggregation 
 ### Inherited members