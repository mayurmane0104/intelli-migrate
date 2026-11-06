# aws_lambda_powertools.utilities.idempotency.hook API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/utilities/idempotency/hook.html](https://docs.aws.amazon.com/powertools/python/latest/api/utilities/idempotency/hook.html)

---

# Module `aws_lambda_powertools.utilities.idempotency.hook`

## Classes

- `class IdempotentHookFunction (*args, **kwargs)`
- 
## Expand source code`class IdempotentHookFunction(Protocol): """ The IdempotentHookFunction. This class defines the calling signature for IdempotentHookFunction callbacks. """ def __call__(self, response: Any, idempotent_data: DataRecord) -> Any: ...`The IdempotentHookFunction. This class defines the calling signature for IdempotentHookFunction callbacks. ### Ancestors- typing.Protocol
- typing.Generic