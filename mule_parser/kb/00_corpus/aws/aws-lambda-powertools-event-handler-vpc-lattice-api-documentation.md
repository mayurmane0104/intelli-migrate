# aws_lambda_powertools.event_handler.vpc_lattice API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/event_handler/vpc_lattice.html](https://docs.aws.amazon.com/powertools/python/latest/api/event_handler/vpc_lattice.html)

---

# Module `aws_lambda_powertools.event_handler.vpc_lattice`

## Classes

- `class VPCLatticeResolver (cors: CORSConfig | None = None,`
 debug: bool | None = None,
 serializer: Callable[[dict], str] | None = None,
 strip_prefixes: list[str | Pattern] | None = None,
 enable_validation: bool = False)
- 
## Expand source code`class VPCLatticeResolver(ApiGatewayResolver): """VPC Lattice resolver Documentation: - https://docs.aws.amazon.com/lambda/latest/dg/services-vpc-lattice.html - https://docs.aws.amazon.com/lambda/latest/dg/services-vpc-lattice.html#vpc-lattice-receiving-events Examples -------- Simple example integrating with Tracer ```python from aws_lambda_powertools import Tracer from aws_lambda_powertools.event_handler import VPCLatticeResolver tracer = Tracer() app = VPCLatticeResolver() @app.get("/get-call") def simple_get(): return {"message": "Foo"} @app.post("/post-call") def simple_post(): post_data: dict = app.current_event.json_body return {"message": post_data} @tracer.capture_lambda_handler def lambda_handler(event, context): return app.resolve(event, context) """ current_event: VPCLatticeEvent def __init__( self, cors: CORSConfig | None = None, debug: bool | None = None, serializer: Callable[[dict], str] | None = None, strip_prefixes: list[str | Pattern] | None = None, enable_validation: bool = False, ): """Amazon VPC Lattice resolver""" super().__init__(ProxyEventType.VPCLatticeEvent, cors, debug, serializer, strip_prefixes, enable_validation) def _get_base_path(self) -> str: return ""`VPC Lattice resolver Documentation: - [https://docs.aws.amazon.com/lambda/latest/dg/services-vpc-lattice.html](https://docs.aws.amazon.com/lambda/latest/dg/services-vpc-lattice.html)-[https://docs.aws.amazon.com/lambda/latest/dg/services-vpc-lattice.html#vpc-lattice-receiving-events](https://docs.aws.amazon.com/lambda/latest/dg/services-vpc-lattice.html#vpc-lattice-receiving-events)## ExamplesSimple example integrating with Tracer ```python from aws_lambda_powertools import Tracer from aws_lambda_powertools.event_handler import VPCLatticeResolver tracer = Tracer() app = VPCLatticeResolver() @app.get("/get-call") def simple_get(): return {"message": "Foo"} @app.post("/post-call") def simple_post(): post_data: dict = app.current_event.json_body return {"message": post_data} @tracer.capture_lambda_handler def lambda_handler(event, context): return app.resolve(event, context) Amazon VPC Lattice resolver ### Ancestors- [ApiGatewayResolver](api_gateway.html#aws_lambda_powertools.event_handler.api_gateway.ApiGatewayResolver)
- [BaseRouter](api_gateway.html#aws_lambda_powertools.event_handler.api_gateway.BaseRouter)
- abc.ABC
 ### Class variables- `var current_event : VPCLatticeEvent`
 ### Inherited members
- `class VPCLatticeV2Resolver (cors: CORSConfig | None = None,`
 debug: bool | None = None,
 serializer: Callable[[dict], str] | None = None,
 strip_prefixes: list[str | Pattern] | None = None,
 enable_validation: bool = False)
- 
## Expand source code`class VPCLatticeV2Resolver(ApiGatewayResolver): """VPC Lattice resolver Documentation: - https://docs.aws.amazon.com/lambda/latest/dg/services-vpc-lattice.html - https://docs.aws.amazon.com/lambda/latest/dg/services-vpc-lattice.html#vpc-lattice-receiving-events Examples -------- Simple example integrating with Tracer ```python from aws_lambda_powertools import Tracer from aws_lambda_powertools.event_handler import VPCLatticeV2Resolver tracer = Tracer() app = VPCLatticeV2Resolver() @app.get("/get-call") def simple_get(): return {"message": "Foo"} @app.post("/post-call") def simple_post(): post_data: dict = app.current_event.json_body return {"message": post_data} @tracer.capture_lambda_handler def lambda_handler(event, context): return app.resolve(event, context) """ current_event: VPCLatticeEventV2 def __init__( self, cors: CORSConfig | None = None, debug: bool | None = None, serializer: Callable[[dict], str] | None = None, strip_prefixes: list[str | Pattern] | None = None, enable_validation: bool = False, ): """Amazon VPC Lattice resolver""" super().__init__(ProxyEventType.VPCLatticeEventV2, cors, debug, serializer, strip_prefixes, enable_validation) def _get_base_path(self) -> str: return ""`VPC Lattice resolver Documentation: - [https://docs.aws.amazon.com/lambda/latest/dg/services-vpc-lattice.html](https://docs.aws.amazon.com/lambda/latest/dg/services-vpc-lattice.html)-[https://docs.aws.amazon.com/lambda/latest/dg/services-vpc-lattice.html#vpc-lattice-receiving-events](https://docs.aws.amazon.com/lambda/latest/dg/services-vpc-lattice.html#vpc-lattice-receiving-events)## ExamplesSimple example integrating with Tracer ```python from aws_lambda_powertools import Tracer from aws_lambda_powertools.event_handler import VPCLatticeV2Resolver tracer = Tracer() app = VPCLatticeV2Resolver() @app.get("/get-call") def simple_get(): return {"message": "Foo"} @app.post("/post-call") def simple_post(): post_data: dict = app.current_event.json_body return {"message": post_data} @tracer.capture_lambda_handler def lambda_handler(event, context): return app.resolve(event, context) Amazon VPC Lattice resolver ### Ancestors- [ApiGatewayResolver](api_gateway.html#aws_lambda_powertools.event_handler.api_gateway.ApiGatewayResolver)
- [BaseRouter](api_gateway.html#aws_lambda_powertools.event_handler.api_gateway.BaseRouter)
- abc.ABC
 ### Class variables- `var current_event : VPCLatticeEventV2`
 ### Inherited members