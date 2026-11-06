# Configuring an HTTPS Endpoint | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/api-manager/latest/https-reference](https://docs.mulesoft.com/api-manager/latest/https-reference)

---

# Configuring an HTTPS Endpoint

You can automatically deploy an API proxy using an HTTP listener (inbound HTTP endpoint) with minimal setup. You can use this approach if you do not foresee any security concerns in your Anypoint Platform API setup. Otherwise, you must configure your API proxy with an HTTPs listener (inbound HTTPS endpoint), instead of an HTTP listener.

MuleSoft requires that you provide your own certificate when configuring your HTTPs setup. The certificate you use can be:

- 
A self-signed certificate to be used for demo purposes 
- 
A custom TLS certificate with validity within your organization 
- 
A trusted Certificate Authority (CA) certificate 

If your backend uses HTTPS with a self-signed certificate or custom TLS certificate, you must configure the API proxy requester with the corresponding certificate.

Depending on your business use case, you can use any of the following recommended ways to configure your API proxy:

- 
[Use a certificate configured through the UI by leveraging Secrets Manager](building-https-proxy):Upload your certificate to a secure vault within API Platform, make it available when you configure the proxy through the secrets manager, and then deploy the secure API proxy to the target runtime, such as CloudHub, Runtime Fabric, or on-premises deployment. 
- 
[Use a certificate defined in already deployed Mule domain](proxy-domain-support)Configure the certificate in the domain so that the API proxy HTTPS Listener references it, and then deploy the secure API proxy to the target Runtime Fabric, or on-premises target. (CloudHub is not supported with this approach because it does not support Mule domains.) 
- 
Use a certificate configured with Anypoint Studio For this approach, download the API proxy, open it in Anypoint Studio, and [manually configure HTTPS](../../mule-runtime/latest/build-an-https-service). You can then deploy the proxy to the target runtime, such as CloudHub, Runtime Fabric, or on-premises deployment. (If the target runtime is on CloudHub, use port 8082 when working with HTTPs.)