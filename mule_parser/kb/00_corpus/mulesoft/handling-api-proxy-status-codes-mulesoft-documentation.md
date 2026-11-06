# Handling API Proxy Status Codes | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/api-manager/latest/wsdl-raml-http-proxy-reference](https://docs.mulesoft.com/api-manager/latest/wsdl-raml-http-proxy-reference)

---

# Handling API Proxy Status Codes

In Mule 4, WSDL, RAML, HTTP, and HTTPS proxies handle errors and requests as described in the following tables. Mule 4 returns different error codes, depending on the proxy type, or no error code in response to problematic requests. This table shows whether or not Mule returns a 504, 400, or 404 error code when your WSDL, RAML, HTTP, and HTTPS proxy receives a problematic request.

| Error Code | WSDL | RAML | OAS | HTTP | HTTPS | 
|---|---|---|---|---|---|
| 504: request timeout | yes | yes | yes | yes | yes | 
| 400: bad request (validation result) | yes | no | yes | no | no | 
| 404: resource not found | no | yes | yes | no | no | 
| 405: method not allowed in API spec | no | no | yes | no | no |