# aws_lambda_powertools.logging.filters API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/logging/filters.html](https://docs.aws.amazon.com/powertools/python/latest/api/logging/filters.html)

---

# Module `aws_lambda_powertools.logging.filters`

## Classes

- `class SuppressFilter (logger: str)`
- 
## Expand source code`class SuppressFilter(logging.Filter): def __init__(self, logger: str): self.logger = logger def filter(self, record: logging.LogRecord) -> bool: # noqa: A003 """Suppress Log Records from registered logger It rejects log records from registered logger e.g. a child logger otherwise it honours log propagation from any log record created by loggers who don't have a handler. """ logger = record.name return self.logger not in logger`Filter instances are used to perform arbitrary filtering of LogRecords. Loggers and Handlers can optionally use Filter instances to filter records as desired. The base filter class only allows events which are below a certain point in the logger hierarchy. For example, a filter initialized with "A.B" will allow events logged by loggers "A.B", "A.B.C", "A.B.C.D", "A.B.D" etc. but not "A.BB", "B.A.B" etc. If initialized with the empty string, all events are passed. Initialize a filter. Initialize with the name of the logger which, together with its children, will have its events allowed through the filter. If no name is specified, allow every event. ### Ancestors- logging.Filter
 ### Methods- `def filter(self, record: logging.LogRecord) ‑> bool`
- 
## Expand source code`def filter(self, record: logging.LogRecord) -> bool: # noqa: A003 """Suppress Log Records from registered logger It rejects log records from registered logger e.g. a child logger otherwise it honours log propagation from any log record created by loggers who don't have a handler. """ logger = record.name return self.logger not in logger`Suppress Log Records from registered logger It rejects log records from registered logger e.g. a child logger otherwise it honours log propagation from any log record created by loggers who don't have a handler.