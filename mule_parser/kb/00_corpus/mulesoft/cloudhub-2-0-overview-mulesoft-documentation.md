# CloudHub 2.0 Overview | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/cloudhub-2](https://docs.mulesoft.com/cloudhub-2)

---

# CloudHub 2.0 Overview

CloudHub 2.0 is a fully managed, containerized integration platform as a service (iPaaS) where you can deploy APIs and integrations as lightweight containers in the cloud.

## Why Deploy on CloudHub 2.0?

CloudHub 2.0:

- 
Provides for deployments across 12 regions globally. 
- 
Dynamically scales infrastructure and built-in services up or down to support elastic transaction volumes. 
- 
Builds in security policies, protecting your services and sensitive data with encrypted secrets, firewall controls, and restricted shell access. 
- 
Encrypts certificates, passwords, and other sensitive configuration data at rest and in transit within Anypoint Platform. 
- 
Provides a standardized isolation boundary by running each Mule instance and service as a separate container. 

For CloudHub 2.0 pricing information, contact either your account executive or your account development representative.

## CloudHub 2.0 Features by Control Plane

All CloudHub 2.0 features are supported across all control planes, with a few exceptions that vary by deployment region:

- 
Deleting the default egress traffic route (0.0.0.0) can cause Anypoint Monitoring to fail in CloudHub 2.0. 
- 
The endpoint URL format requires the region suffix or not before `cloudhub.io`.

| CloudHub 2.0 Features | US Cloud | EU Cloud | Canada Cloud | Japan Cloud | 
|---|---|---|---|---|
| Deleting the Default Route | Available | Available | Not Available | Not Available | 
| Endpoints URL Format | No region suffix:  | Needs region suffix:  | Needs region suffix:  | Needs region suffix:  | 

| URL formats vary by control plane: 
 |