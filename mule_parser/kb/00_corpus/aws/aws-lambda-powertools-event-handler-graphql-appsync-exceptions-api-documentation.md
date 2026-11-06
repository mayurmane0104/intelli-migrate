# aws_lambda_powertools.event_handler.graphql_appsync.exceptions API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/event_handler/graphql_appsync/exceptions.html](https://docs.aws.amazon.com/powertools/python/latest/api/event_handler/graphql_appsync/exceptions.html)

---

# Module `aws_lambda_powertools.event_handler.graphql_appsync.exceptions`

## Classes

- `class InvalidBatchResponse (*args, **kwargs)`
- 
## Expand source code`class InvalidBatchResponse(Exception): """ When a batch response something different from a List """`When a batch response something different from a List ### Ancestors- builtins.Exception
- builtins.BaseException
 
- `class ResolverNotFoundError (*args, **kwargs)`
- 
## Expand source code`class ResolverNotFoundError(Exception): """ When a resolver is not found during a lookup. """`When a resolver is not found during a lookup. ### Ancestors- builtins.Exception
- builtins.BaseException