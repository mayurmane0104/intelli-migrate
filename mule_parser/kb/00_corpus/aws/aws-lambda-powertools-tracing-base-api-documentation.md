# aws_lambda_powertools.tracing.base API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/tracing/base.html](https://docs.aws.amazon.com/powertools/python/latest/api/tracing/base.html)

---

# Module `aws_lambda_powertools.tracing.base`

## Classes

- `class BaseProvider`
- 
## Expand source code`class BaseProvider(abc.ABC): @abc.abstractmethod @contextmanager def in_subsegment(self, name=None, **kwargs) -> Generator[BaseSegment, None, None]: """Return a subsegment context manger. Parameters ---------- name: str Subsegment name kwargs: dict | None Optional parameters to be propagated to segment """ @abc.abstractmethod @contextmanager def in_subsegment_async(self, name=None, **kwargs) -> Generator[BaseSegment, None, None]: """Return a subsegment async context manger. Parameters ---------- name: str Subsegment name kwargs: dict | None Optional parameters to be propagated to segment """ @abc.abstractmethod def put_annotation(self, key: str, value: str | numbers.Number | bool) -> None: """Annotate current active trace entity with a key-value pair. Note: Annotations will be indexed for later search query. Parameters ---------- key: str Metadata key value: str | numbers.Number | bool Annotation value """ @abc.abstractmethod def put_metadata(self, key: str, value: Any, namespace: str = "default") -> None: """Add metadata to the current active trace entity. Note: Metadata is not indexed but can be later retrieved by BatchGetTraces API. Parameters ---------- key: str Metadata key value: Any Any object that can be serialized into a JSON string namespace: set[str] Metadata namespace, by default 'default' """ @abc.abstractmethod def patch(self, modules: Sequence[str]) -> None: """Instrument a set of supported libraries Parameters ---------- modules: set[str] Set of modules to be patched """ @abc.abstractmethod def patch_all(self) -> None: """Instrument all supported libraries"""`Helper class that provides a standard way to create an ABC using inheritance. ### Ancestors- abc.ABC
 ### Methods- `def in_subsegment(self, name=None, **kwargs) ‑> Generator[`- [BaseSegment](#aws_lambda_powertools.tracing.base.BaseSegment), None, None]
- 
## Expand source code`@abc.abstractmethod @contextmanager def in_subsegment(self, name=None, **kwargs) -> Generator[BaseSegment, None, None]: """Return a subsegment context manger. Parameters ---------- name: str Subsegment name kwargs: dict | None Optional parameters to be propagated to segment """`Return a subsegment context manger. ## Parameters- `name`- `str`
- Subsegment name
- `kwargs`- `dict | None`
- Optional parameters to be propagated to segment
 
- `def in_subsegment_async(self, name=None, **kwargs) ‑> Generator[`- [BaseSegment](#aws_lambda_powertools.tracing.base.BaseSegment), None, None]
- 
## Expand source code`@abc.abstractmethod @contextmanager def in_subsegment_async(self, name=None, **kwargs) -> Generator[BaseSegment, None, None]: """Return a subsegment async context manger. Parameters ---------- name: str Subsegment name kwargs: dict | None Optional parameters to be propagated to segment """`Return a subsegment async context manger. ## Parameters- `name`- `str`
- Subsegment name
- `kwargs`- `dict | None`
- Optional parameters to be propagated to segment
 
- `def patch(self, modules: Sequence[str]) ‑> None`
- 
## Expand source code`@abc.abstractmethod def patch(self, modules: Sequence[str]) -> None: """Instrument a set of supported libraries Parameters ---------- modules: set[str] Set of modules to be patched """`Instrument a set of supported libraries ## Parameters- `modules`- `set[str]`
- Set of modules to be patched
 
- `def patch_all(self) ‑> None`
- 
## Expand source code`@abc.abstractmethod def patch_all(self) -> None: """Instrument all supported libraries"""`Instrument all supported libraries 
- `def put_annotation(self, key: str, value: str | numbers.Number | bool) ‑> None`
- 
## Expand source code`@abc.abstractmethod def put_annotation(self, key: str, value: str | numbers.Number | bool) -> None: """Annotate current active trace entity with a key-value pair. Note: Annotations will be indexed for later search query. Parameters ---------- key: str Metadata key value: str | numbers.Number | bool Annotation value """`Annotate current active trace entity with a key-value pair. Note: Annotations will be indexed for later search query. ## Parameters- `key`- `str`
- Metadata key
- `value`- `str | numbers.Number | bool`
- Annotation value
 
- `def put_metadata(self, key: str, value: Any, namespace: str = 'default') ‑> None`
- 
## Expand source code`@abc.abstractmethod def put_metadata(self, key: str, value: Any, namespace: str = "default") -> None: """Add metadata to the current active trace entity. Note: Metadata is not indexed but can be later retrieved by BatchGetTraces API. Parameters ---------- key: str Metadata key value: Any Any object that can be serialized into a JSON string namespace: set[str] Metadata namespace, by default 'default' """`Add metadata to the current active trace entity. Note: Metadata is not indexed but can be later retrieved by BatchGetTraces API. ## Parameters- `key`- `str`
- Metadata key
- `value`- `Any`
- Any object that can be serialized into a JSON string
- `namespace`- `set[str]`
- Metadata namespace, by default 'default'
 
 
- `class BaseSegment`
- 
## Expand source code`class BaseSegment(abc.ABC): """Holds common properties and methods on segment and subsegment.""" @abc.abstractmethod def close(self, end_time: int | None = None): """Close the trace entity by setting `end_time` and flip the in progress flag to False. Parameters ---------- end_time: int Time in epoch seconds, by default current time will be used. """ @abc.abstractmethod def add_subsegment(self, subsegment: Any): """Add input subsegment as a child subsegment.""" @abc.abstractmethod def remove_subsegment(self, subsegment: Any): """Remove input subsegment from child subsegments.""" @abc.abstractmethod def put_annotation(self, key: str, value: str | numbers.Number | bool) -> None: """Annotate segment or subsegment with a key-value pair. Note: Annotations will be indexed for later search query. Parameters ---------- key: str Metadata key value: str | numbers.Number | bool Annotation value """ @abc.abstractmethod def put_metadata(self, key: str, value: Any, namespace: str = "default") -> None: """Add metadata to segment or subsegment. Metadata is not indexed but can be later retrieved by BatchGetTraces API. Parameters ---------- key: str Metadata key value: Any Any object that can be serialized into a JSON string namespace: set[str] Metadata namespace, by default 'default' """ @abc.abstractmethod def add_exception(self, exception: BaseException, stack: list[traceback.StackSummary], remote: bool = False): """Add an exception to trace entities. Parameters ---------- exception: Exception Caught exception stack: list[traceback.StackSummary] List of traceback summaries Output from `traceback.extract_stack()`. remote: bool Whether it's a client error (False) or downstream service error (True), by default False """`Holds common properties and methods on segment and subsegment. ### Ancestors- abc.ABC
 ### Methods- `def add_exception(self,`
 exception: BaseException,
 stack: list[traceback.StackSummary],
 remote: bool = False)
- 
## Expand source code`@abc.abstractmethod def add_exception(self, exception: BaseException, stack: list[traceback.StackSummary], remote: bool = False): """Add an exception to trace entities. Parameters ---------- exception: Exception Caught exception stack: list[traceback.StackSummary] List of traceback summaries Output from `traceback.extract_stack()`. remote: bool Whether it's a client error (False) or downstream service error (True), by default False """`Add an exception to trace entities. ## Parameters- `exception`- `Exception`
- Caught exception
- `stack`- `list[traceback.StackSummary]`
- 
List of traceback summaries Output from `traceback.extract_stack()`.
- `remote`- `bool`
- Whether it's a client error (False) or downstream service error (True), by default False
 
- `def add_subsegment(self, subsegment: Any)`
- 
## Expand source code`@abc.abstractmethod def add_subsegment(self, subsegment: Any): """Add input subsegment as a child subsegment."""`Add input subsegment as a child subsegment. 
- `def close(self, end_time: int | None = None)`
- 
## Expand source code`@abc.abstractmethod def close(self, end_time: int | None = None): """Close the trace entity by setting `end_time` and flip the in progress flag to False. Parameters ---------- end_time: int Time in epoch seconds, by default current time will be used. """`Close the trace entity by setting `end_time`and flip the in progress flag to False.## Parameters- `end_time`- `int`
- Time in epoch seconds, by default current time will be used.
 
- `def put_annotation(self, key: str, value: str | numbers.Number | bool) ‑> None`
- 
## Expand source code`@abc.abstractmethod def put_annotation(self, key: str, value: str | numbers.Number | bool) -> None: """Annotate segment or subsegment with a key-value pair. Note: Annotations will be indexed for later search query. Parameters ---------- key: str Metadata key value: str | numbers.Number | bool Annotation value """`Annotate segment or subsegment with a key-value pair. Note: Annotations will be indexed for later search query. ## Parameters- `key`- `str`
- Metadata key
- `value`- `str | numbers.Number | bool`
- Annotation value
 
- `def put_metadata(self, key: str, value: Any, namespace: str = 'default') ‑> None`
- 
## Expand source code`@abc.abstractmethod def put_metadata(self, key: str, value: Any, namespace: str = "default") -> None: """Add metadata to segment or subsegment. Metadata is not indexed but can be later retrieved by BatchGetTraces API. Parameters ---------- key: str Metadata key value: Any Any object that can be serialized into a JSON string namespace: set[str] Metadata namespace, by default 'default' """`Add metadata to segment or subsegment. Metadata is not indexed but can be later retrieved by BatchGetTraces API. ## Parameters- `key`- `str`
- Metadata key
- `value`- `Any`
- Any object that can be serialized into a JSON string
- `namespace`- `set[str]`
- Metadata namespace, by default 'default'
 
- `def remove_subsegment(self, subsegment: Any)`
- 
## Expand source code`@abc.abstractmethod def remove_subsegment(self, subsegment: Any): """Remove input subsegment from child subsegments."""`Remove input subsegment from child subsegments.