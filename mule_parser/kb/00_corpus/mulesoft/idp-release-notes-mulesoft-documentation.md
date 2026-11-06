# IDP Release Notes | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/release-notes/idp/idp-release-notes](https://docs.mulesoft.com/release-notes/idp/idp-release-notes)

---

For the **emails** field in Purchase Order and Invoice actions, IDP now returns `null` instead of an empty array `[]` in the execution response after reviewing the associated task.

# IDP Release Notes

MuleSoft Intelligent Document Processing (IDP) enables you to read invoices, purchase orders, and other unstructured or semi-structured documents and then analyze and refine the extracted content using AI capabilities to create a structured response.

## June 5, 2026

## What’s New

- 
You can now use Claude Sonnet 4.6 to analyze your documents. For additional details on model support and performance, see [Supported Models](../../idp/supported-models).
- 
You can now view published document action versions. Open earlier versions of your document actions to review their configuration without making changes. For additional details and instructions, see [View Published Document Action Versions](../../idp/publishing-document-actions#view-published-versions).

## May 5, 2026

## What’s New

- 
You can now use OpenAI GPT 5.1 and 5.2 to analyze your documents. For additional details on model support and performance, see [Supported Models](../../idp/supported-models).
- 
You can now search and filter document actions in the **Document Actions**page.

## April 2, 2026

## What’s New

- 
Updated OpenAI model names. - 
Einstein OpenAI GPT-4o Mini 0718 is now Einstein OpenAI GPT-4o Mini. 
- 
Einstein OpenAI GPT-4o 0806 is now Einstein OpenAI GPT-4o. 
 
- 

## March 20, 2026

## What’s New

- 
Removed Gemini 3 model support. This feature isn’t quite ready, so we’re removing it for now. We’ll let you know when it’s back up. 

## March 10, 2026

## What’s New

- 
You can now enable location callouts in Generic document actions with customized schemas. For additional details about supported models and limitations, see [Configure Document Action Settings](../../idp/creating-document-actions#document-action-settings)
- 
You can now select Google’s GEMINI-3.0 Flash (Beta) model to analyze your documents. For additional usage details and considerations about this model, see [Supported Models](../../idp/supported-models)

## October 29, 2025

## What’s New

- 
You can now select Google’s GEMINI-2.5 Flash model to analyze your documents. 

## June 3, 2025

## What’s New

- 
You can now rotate documents in the document action builder preview and review task preview. The rotation is for visual assistance and does not modify the original file. 

## Fixed Issues

| Issue Resolution | ID | 
|---|---|
| W-17330495 | 

## May 20, 2025

## What’s New

- 
You can now **Submit**review tasks without having to scroll to the end of the fields list, improving accessibility.

## May 8, 2025

## What’s New

- 
You can now enable image recognition in your document actions. To enable this feature, see [Configure Document Action Settings](../../idp/analyzing-documents-with-einstein#settings).
- 
You can now select Google’s GEMINI-2.0 Flash 001 model to analyze your documents. To select the model to use, see [Configure Document Action Settings](../../idp/analyzing-documents-with-einstein#settings).For additional information about supported models, see [Supported Models](../../idp/supported-models)
- 
Einstein prompts now support up to 128,000 input tokens per request. For additional details about token consumption, see [Token Usage and Estimation](../../idp/quotas-and-limits#tokens).
- 
Data retention policies are updated: - 
For all successful executions, IDP now retains the data for 24 hours. 
- 
IDP now retains any incomplete tasks for 30 days. 
 
- 

## February 5, 2025

## What’s New

- 
You can now analyze any type of document and fully customize the output structure by creating a Generic document action and enabling **Customize Schema**.For more information, see [Analyzing Documents With Custom User-Defined Schemas](../../idp/analyzing-documents-with-einstein).- 
Generic document actions now support using non-English characters for prompt instructions when **Customize Schema**is enabled.
 
- 
- 
New document actions now support the `GPT-4o (gpt-4o-2024-08-06)`and`GPT-4o Mini (gpt-4o-mini-2024-07-18)`LLM Models.
- 
New document actions now support masking any personally identifiable information from your documents before sending it to the predictive model. 
- 
The API portal documentation for IDP assets published to Exchange now includes the `valueOnly`query parameter.
- 
You can now upload files in Base64 encoding for versioned action executions. For an example API call, see [Upload a Base64-encoded File](../../idp/automate-document-processing-with-the-idp-api#upload-base64-file).
- 
IDP can now detect signatures in document actions that use Einstein. 

## Fixed Issues

| Issue Resolution | ID | 
|---|---|
| Completed executions no longer stay in status  | W-17064164 | 
| Failed executions that include Einstein prompts no longer show status  | W-17465241 | 
| Required table columns are now shown in the corresponding page during reviews. | W-17485449 | 

## November 20, 2024

## What’s New

- 
IDP now fully supports analyzing documents in French, Italian, and Portuguese. 
- 
Organizations with Salesforce Einstein enabled now use Einstein as the default option for answering prompts. 
- 
IDP now supports non-latin characters in the file preview during document action creation. 

## November 7, 2024

## What’s New

- 
You can now analyze your documents with Salesforce Einstein. Use Einstein to analyze documents that don’t use a standard format or are difficult to read without performing a complex analysis of the extracted data. See [Analyze Documents with Einstein](../../idp/creating-document-actions#einstein)for information about configuring Einstein in your document actions.

## October 2, 2024

## What’s New

- 
IDP now supports analyzing TIFF files. 

## September 26, 2024

## What’s New

- 
Invoice and Purchase Order data extraction accuracy is improved for all supported languages. 
- 
Invoice and Purchase Order document actions now support extracting VAT and VAT Rate from tables. 

## August 22, 2024

## What’s New

- 
IDP now fully supports analyzing documents in Spanish and German. 

## May 8, 2024

## What’s New

- 
You can now define a callback URL for your executions. See [Define a Callback URL](../../idp/automate-document-processing-with-the-idp-api#callback-url)for details and configuration instructions.

## April 29, 2024

## What’s New

- 
MuleSoft announces the release of Intelligent Document Processing (IDP). 

## See Also

- 
[Salesforce Help](https://help.salesforce.com)
- 
[MuleSoft Services](https://www.mulesoft.com/support-and-services)