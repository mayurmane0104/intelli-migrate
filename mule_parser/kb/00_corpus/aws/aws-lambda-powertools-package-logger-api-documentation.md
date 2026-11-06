# aws_lambda_powertools.package_logger API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/package_logger.html](https://docs.aws.amazon.com/powertools/python/latest/api/package_logger.html)

---

# Module `aws_lambda_powertools.package_logger`

## Functions

- `def set_package_logger_handler(stream=None)`
- 
## Expand source code`def set_package_logger_handler(stream=None): """Sets up Powertools for AWS Lambda (Python) package logging. By default, we discard any output to not interfere with customers logging. When POWERTOOLS_DEBUG env var is set, we setup `aws_lambda_powertools` logger in DEBUG level. Parameters ---------- stream: sys.stdout log stream, stdout by default """ if powertools_debug_is_set(): return set_package_logger(stream=stream) logger = logging.getLogger("aws_lambda_powertools") logger.addHandler(logging.NullHandler()) logger.propagate = False`Sets up Powertools for AWS Lambda (Python) package logging. By default, we discard any output to not interfere with customers logging. When POWERTOOLS_DEBUG env var is set, we setup [aws_lambda_powertools](index.html)## Parameters- `stream`- `sys.stdout`
- log stream, stdout by default