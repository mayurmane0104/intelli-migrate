# aws_lambda_powertools.event_handler.exceptions API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/event_handler/exceptions.html](https://docs.aws.amazon.com/powertools/python/latest/api/event_handler/exceptions.html)

---

# Module `aws_lambda_powertools.event_handler.exceptions`

## Classes

- `class BadRequestError (msg: str)`
- 
## Expand source code`class BadRequestError(ServiceError): """API Gateway and ALB Bad Request Error (400)""" def __init__(self, msg: str): super().__init__(HTTPStatus.BAD_REQUEST, msg)`API Gateway and ALB Bad Request Error (400) ## Parameters- `status_code`- `int`
- Http status code
- `msg`- `str`
- Error message
 ### Ancestors- [ServiceError](#aws_lambda_powertools.event_handler.exceptions.ServiceError)
- builtins.Exception
- builtins.BaseException
 
- `class InternalServerError (message: str)`
- 
## Expand source code`class InternalServerError(ServiceError): """API Gateway and ALB Internal Server Error (500)""" def __init__(self, message: str): super().__init__(HTTPStatus.INTERNAL_SERVER_ERROR, message)`API Gateway and ALB Internal Server Error (500) ## Parameters- `status_code`- `int`
- Http status code
- `msg`- `str`
- Error message
 ### Ancestors- [ServiceError](#aws_lambda_powertools.event_handler.exceptions.ServiceError)
- builtins.Exception
- builtins.BaseException
 
- `class NotFoundError (msg: str = 'Not found')`
- 
## Expand source code`class NotFoundError(ServiceError): """API Gateway and ALB Not Found Error (404)""" def __init__(self, msg: str = "Not found"): super().__init__(HTTPStatus.NOT_FOUND, msg)`API Gateway and ALB Not Found Error (404) ## Parameters- `status_code`- `int`
- Http status code
- `msg`- `str`
- Error message
 ### Ancestors- [ServiceError](#aws_lambda_powertools.event_handler.exceptions.ServiceError)
- builtins.Exception
- builtins.BaseException
 
- `class ServiceError (status_code: int, msg: str)`
- 
## Expand source code`class ServiceError(Exception): """API Gateway and ALB HTTP Service Error""" def __init__(self, status_code: int, msg: str): """ Parameters ---------- status_code: int Http status code msg: str Error message """ self.status_code = status_code self.msg = msg`API Gateway and ALB HTTP Service Error ## Parameters- `status_code`- `int`
- Http status code
- `msg`- `str`
- Error message
 ### Ancestors- builtins.Exception
- builtins.BaseException
 ### Subclasses
- 
## Expand source code`class UnauthorizedError(ServiceError): """API Gateway and ALB Unauthorized Error (401)""" def __init__(self, msg: str): super().__init__(HTTPStatus.UNAUTHORIZED, msg)`API Gateway and ALB Unauthorized Error (401) ## Parameters- `status_code`- `int`
- Http status code
- `msg`- `str`
- Error message
 ### Ancestors- [ServiceError](#aws_lambda_powertools.event_handler.exceptions.ServiceError)
- builtins.Exception
- builtins.BaseException