# Implementation Errors | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/anypoint-code-builder/troubleshoot-implementation-errors](https://docs.mulesoft.com/anypoint-code-builder/troubleshoot-implementation-errors)

---

![Fragment folder in the Explorer view](_images/troubleshoot-imp-scaff.png) 

# Implementation Errors

You might encounter problems when implementing an API.

## Something Failed While Scaffolding an API

Anypoint Code Builder supports scaffolding these schema fragment files if they’re referenced from API specs:

| Avro | JSON | RAML | |
|---|---|---|---|
| 
 | Yes | Yes | No | 
| 
 | No | No | Yes | 
| 
 | No | No | Yes | 
| 
 | No | No | Yes | 
| 
 | No | No | Yes | 

If you add a fragment that isn’t supported, the scaffolder doesn’t add these fragments as project dependencies when you import the spec from Exchange. However, you can scaffold schemas that are specified inline within the spec.

If you attempt to scaffold an API that references these types of fragments, you see a message like the following:

**Something failed while scaffolding API**

The scaffold fails and the flows and other elements aren’t created. To see scaffolding errors, select **Mule DX Server: Scaffolding** from the list in the output panel.

If you use the iterative approach to scaffold the API (using [multi-root workspaces](imp-implement-local-apis#scaffold-spec-into-project)),
the implementation project folder structure is not created.

To work around this issue, before scaffolding the API:

- 
Add the fragment directly to a folder in your API spec project, such as `fragments`:![Fragment folder in the Explorer view](_images/troubleshoot-imp-scaff.png)  
- 
Change the path to the fragment from Exchange to the local folder, for example: - 
Reference Local OAS Fragment 
- 
Reference OAS Fragment on Exchange 
 `$ref: fragments/frag-defs.yaml#/components/examples/flightsList`YAML`$ref: exchange_modules/e91cab06-650b-4634-9c6f-5bc4f4fc4d17/frag-defs/1.0.0/frag-defs.yaml#/components/examples/flightsList`YAML
- 
- 
Re-scaffold the API.