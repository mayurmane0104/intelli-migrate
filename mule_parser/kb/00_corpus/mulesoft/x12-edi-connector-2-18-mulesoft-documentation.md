# X12 EDI Connector 2.18 | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/x12-edi-connector/latest](https://docs.mulesoft.com/x12-edi-connector/latest)

---

# X12 EDI Connector 2.18

Support Category: [Premium](https://www.salesforce.com/en-us/wp-content/uploads/sites/4/documents/legal/Agreements/versioning-back-support-policy.pdf)

Anypoint Connector for X12 EDI (X12 EDI Connector) enables you to convert X12 messages to and from DataWeave-compatible representations by using lists and maps.
All of the schema definitions you need for [supported X12 standard transaction sets](x12-edi-versions-x12) are included. For complete information about schemas, see [X12 EDI Schema Language Reference](x12-edi-schema-language-reference).

Many Health Insurance Portability and Accountability Act (HIPAA) document versions are also supported, as listed separately in the [Supported HIPAA Versions](x12-edi-versions-hipaa). For more information about HIPAA usage, refer to [Connector HIPAA Standards](x12-edi-connector-hipaa).

## Prerequisites

To use this connector, you must be familiar with:

- 
Anypoint Connectors 
- 
Mule runtime engine (Mule) 
- 
Elements and global elements in a Mule flow 
- 
Creating a Mule app using Anypoint Studio or Anypoint Code Builder 

Before creating an app, you must have:

- 
Purchased a MuleSoft license for X12 EDI Connector. Contact your Account Representative about purchasing a license. 
- 
Anypoint Studio or Anypoint Code Builder 

| X12 EDI Connector supports files of up to 15 MB in size, and the memory requirement is approximately 40 to 1. For example, a 1 MB file requires up to 40 MB of memory to process, so it’s important to consider this memory requirement in conjunction with your Transactions Per Second (TPS) needs for large X12 files. This is not an exact figure; the value varies according to the complexity of the mapping instructions. | 

## Exchange Templates and Examples

[Anypoint Exchange](https://www.mulesoft.com/exchange/) provides templates
that you can use as starting points for your apps and examples that illustrate a complete solution.

### X12 EDI Connector Templates in Exchange

X12 EDI Connector templates provide starting points that help you:

- 
[Map application messages to outbound X12 transactions](https://www.mulesoft.com/exchange/org.mule.examples/template-b2b-edi-outbound-x12-map/minor/1.0/)
- 
[Map inbound X12 transactions to the application message format](https://www.mulesoft.com/exchange/org.mule.examples/template-b2b-edi-inbound-x12-map/minor/1.0/)
- 
[Set up your Partner Manager content storage](https://www.anypoint.mulesoft.com/exchange/com.mulesoft.b2b/partner-manager-content-storage-service-s3/minor/1.0/)

### X12 EDI Connector Examples in Exchange

X12 EDI Connector examples in Exchange enable you to:

- 
[Customize an X12 EDI schema for B2B integrations](https://www.mulesoft.com/exchange/works.integration/b2b-x12-custom-schema-example/minor/1.0/)
- 
[Transform outbound purchase order XML messages to X12 850 transactions](https://www.mulesoft.com/exchange/org.mule.examples/example-b2b-nto-outbound-purchase-order-01/minor/1.0/)
- 
[Transform inbound X12 850 transactions to JSON purchase orders](https://www.mulesoft.com/exchange/org.mule.examples/example-b2b-mythical-inbound-purchase-order-01/minor/1.0/)
- 
[Transform outbound XML messages into X12 purchase orders, inbound X12 purchase orders into JSON, and generate a functional acknowledgement](https://www.mulesoft.com/exchange/org.mule.examples/b2b-demo-x12-transform/)
- 
[Implement an end-to-end order to cash workflow from the perspective of a seller](https://www.mulesoft.com/exchange/com.mulesoft.muleesb.modules/b2b-order-to-cash-mapping/minor/1.0/)
- 
[Implement an end-to-end B2B procure to pay workflow from the perspective of a buyer](https://www.mulesoft.com/exchange/com.mulesoft.muleesb.modules/b2b-procure-to-pay-mappings/minor/1.0/)

## Next Step

After you complete the prerequisites, you are ready to create your own app and configure the connector using [Anypoint Studio](x12-edi-connector-studio).

## See Also

[Salesforce Help](https://help.salesforce.com)