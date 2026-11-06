# aws_lambda_powertools.logging.utils API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/logging/utils.html](https://docs.aws.amazon.com/powertools/python/latest/api/logging/utils.html)

---

# Module `aws_lambda_powertools.logging.utils`

## Functions

- `def copy_config_to_registered_loggers(source_logger: Logger,`
 log_level: int | str | None = None,
 ignore_log_level=False,
 exclude: set[str] | None = None,
 include: set[str] | None = None) ‑> None
- 
## Expand source code`def copy_config_to_registered_loggers( source_logger: Logger, log_level: int | str | None = None, ignore_log_level=False, exclude: set[str] | None = None, include: set[str] | None = None, ) -> None: """Copies source Logger level and handler to all registered loggers for consistent formatting. Parameters ---------- ignore_log_level source_logger : Logger Powertools for AWS Lambda (Python) Logger to copy configuration from log_level : int | str, optional Logging level to set to registered loggers, by default uses source_logger logging level ignore_log_level: bool Whether to not touch log levels for discovered loggers. log_level param is disregarded when this is set. include : set[str] | None, optional List of logger names to include, by default all registered loggers are included exclude : set[str] | None, optional List of logger names to exclude, by default None """ level = log_level or source_logger.log_level # Assumptions: Only take parent loggers not children (dot notation rule) # Steps: # 1. Default operation: Include all registered loggers # 2. Only include set? Only add Loggers in the list and ignore all else # 3. Include and exclude set? Add Logger if it’s in include and not in exclude # 4. Only exclude set? Ignore Logger in the excluding list # Exclude source and Powertools for AWS Lambda (Python) package logger by default # If source logger is a child ensure we exclude parent logger to not break child logger # from receiving/pushing updates to keys being added/removed source_logger_name = source_logger.name.split(".")[0] if exclude: exclude.update([source_logger_name, PACKAGE_LOGGER]) else: exclude = {source_logger_name, PACKAGE_LOGGER} # Prepare loggers set if include: loggers = include.difference(exclude) filter_func = _include_registered_loggers_filter else: loggers = exclude filter_func = _exclude_registered_loggers_filter registered_loggers = _find_registered_loggers(loggers=loggers, filter_func=filter_func) for logger in registered_loggers: _configure_logger(source_logger=source_logger, logger=logger, level=level, ignore_log_level=ignore_log_level)`Copies source Logger level and handler to all registered loggers for consistent formatting. ## Parameters- `ignore_log_level`
- `source_logger`- `Logger`
- Powertools for AWS Lambda (Python) Logger to copy configuration from
- `log_level`- `int | str`, optional
- Logging level to set to registered loggers, by default uses source_logger logging level
- `ignore_log_level`- `bool`
- Whether to not touch log levels for discovered loggers. log_level param is disregarded when this is set.
- `include`- `set[str] | None`, optional
- List of logger names to include, by default all registered loggers are included
- `exclude`- `set[str] | None`, optional
- List of logger names to exclude, by default None