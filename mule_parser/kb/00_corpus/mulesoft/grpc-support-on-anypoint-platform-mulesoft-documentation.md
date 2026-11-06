# gRPC Support on Anypoint Platform | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/release-notes/platform/grpc-support](https://docs.mulesoft.com/release-notes/platform/grpc-support)

---

Design Specs

# gRPC Support on Anypoint Platform

Implement and consume gRPC APIs as part of your API-led strategy using gRPC support in Anypoint Platform. gRPC is a high-performance, open-source framework for remote procedure calls (RPCs) that uses Protocol Buffers (protobuf) as the interface definition language. gRPC uses HTTP/2 for transport and is well-suited for server-to-server communication and microservices architectures.

Anypoint Platform supports gRPC in the following products and stages:

| API-Led Journey Stage | Product | Versions Supported | Learn More | 
|---|---|---|---|
| Anypoint Code Builder | Protobuf 3 | Design your gRPC specs (API Type: gRPC API, Protobuf 3) in  | |
| Govern Specs | Anypoint API Governance | Protobuf 3 | Validate your gRPC API specs against governance rulesets during the design phase. After you publish the specs to Exchange, govern them using  | 
| Publish Specs | Anypoint Exchange | Protobuf 3 | Publish your gRPC API specs to  | 
| Implement APIs | Anypoint Code Builder | Protobuf 3 | Scaffold and implement gRPC specs in a Mule project using  | 
| APIkit for gRPC | Protobuf 3 | Scaffold and implement gRPC APIs in a Mule project from a .proto file using  | |
| Deploy | Runtime Fabric | Protobuf 3 | Deploy your gRPC API to  | 
| Manage APIs | Anypoint API Manager | Protobuf 3 | 
 | 
| Omni Gateway | Protobuf 3 | Manage and govern your external gRPC services using  | |
| Connect to gRPC Services | Anypoint Connector for gRPC (gRPC Connector) | Protobuf 3 | Call external gRPC services from your Mule applications using  | 

## History of gRPC Support

Following is a history of support for gRPC in Anypoint Platform.

### March 18, 2026

- 
Anypoint Platform supports gRPC in the following products and capabilities: - 
Anypoint Connector for gRPC (gRPC Connector) for connecting to gRPC services from Mule applications 
 
- 

### March 17, 2026

- 
Anypoint Platform supports gRPC in the following products and capabilities: - 
Anypoint Code Builder for designing gRPC API specifications (Protobuf 3) 
- 
Anypoint Code Builder for implementing and scaffolding gRPC APIs 
- 
APIkit for gRPC for scaffolding gRPC APIs from .proto specifications 
- 
Anypoint Exchange for publishing and discovering gRPC API specifications 
- 
Anypoint API Manager for managing gRPC API instances and applying policies 
- 
Flex Gateway for managing external gRPC services 
- 
Runtime Fabric and Hybrid Standalone (self-hosted deployments) for deploying gRPC APIs (HTTP/2 ingress; Mule runtime 4.11 or later required) 
- 
Anypoint API Governance for governing gRPC API specifications 
 
- 

## See Also

- 
[gRPC documentation at grpc.io](https://grpc.io/docs/)