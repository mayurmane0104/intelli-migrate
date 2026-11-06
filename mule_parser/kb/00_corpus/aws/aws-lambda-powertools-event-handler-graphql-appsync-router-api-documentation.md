# aws_lambda_powertools.event_handler.graphql_appsync.router API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/event_handler/graphql_appsync/router.html](https://docs.aws.amazon.com/powertools/python/latest/api/event_handler/graphql_appsync/router.html)

---

# Module `aws_lambda_powertools.event_handler.graphql_appsync.router`

## Classes

- `class Router`
- 
## Expand source code`class Router(BaseRouter): context: dict current_batch_event: list[AppSyncResolverEvent] = [] current_event: AppSyncResolverEvent | None = None lambda_context: LambdaContext | None = None def __init__(self): self.context = {} # early init as customers might add context before event resolution self._resolver_registry = ResolverRegistry() self._batch_resolver_registry = ResolverRegistry() self._async_batch_resolver_registry = ResolverRegistry() def resolver(self, type_name: str = "*", field_name: str | None = None) -> Callable: return self._resolver_registry.register(field_name=field_name, type_name=type_name) def batch_resolver( self, type_name: str = "*", field_name: str | None = None, raise_on_error: bool = False, aggregate: bool = True, ) -> Callable: return self._batch_resolver_registry.register( field_name=field_name, type_name=type_name, raise_on_error=raise_on_error, aggregate=aggregate, ) def async_batch_resolver( self, type_name: str = "*", field_name: str | None = None, raise_on_error: bool = False, aggregate: bool = True, ) -> Callable: return self._async_batch_resolver_registry.register( field_name=field_name, type_name=type_name, raise_on_error=raise_on_error, aggregate=aggregate, ) def append_context(self, **additional_context): """Append key=value data as routing context""" self.context.update(**additional_context) def clear_context(self): """Resets routing context""" self.context.clear()`Abstract base class for Router (resolvers) ### Ancestors- [BaseRouter](base.html#aws_lambda_powertools.event_handler.graphql_appsync.base.BaseRouter)
- abc.ABC
 ### Subclasses### Class variables- `var context : dict`
- `var current_batch_event : list[AppSyncResolverEvent]`
- `var current_event : AppSyncResolverEvent | None`
- `var lambda_context : LambdaContext | None`
 ### Methods- `def append_context(self, **additional_context)`
- 
## Expand source code`def append_context(self, **additional_context): """Append key=value data as routing context""" self.context.update(**additional_context)`Append key=value data as routing context 
- `def clear_context(self)`
- 
## Expand source code`def clear_context(self): """Resets routing context""" self.context.clear()`Resets routing context 
 ### Inherited members