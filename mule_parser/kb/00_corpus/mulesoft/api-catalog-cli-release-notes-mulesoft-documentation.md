# API Catalog CLI Release Notes | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/release-notes/api-catalog/api-catalog-release-notes](https://docs.mulesoft.com/release-notes/api-catalog/api-catalog-release-notes)

---

api-catalog autocomplete

# API Catalog CLI Release Notes

MuleSoft announces the release of Anypoint API Catalog CLI.

API Catalog CLI enables you to discover and catalog your API definitions, documentation files, and associated metadata by running commands at a command prompt or as part of your automation tools, such as a CI/CD pipeline or custom scripts.

## 1.1.2

**March 06, 2024**

### Fixed Issues

| Issue Resolution | ID | 
|---|---|
| API Catalog now shows a detailed error message when the publication of an asset fails. | W-15084821 | 

## 1.1.1

**October 31, 2023**

### What’s New

- 
Certain dependencies are updated. 

## 1.1.0

**April 1, 2023**

### What’s New

- 
You can now use API Catalog CLI with a Network Proxy. For more information, see [Using API Catalog CLI with a Network Proxy.](../../exchange/apicat-use-proxy)
- 
You can now authenticate to API Catalog with the new environment variable `ANYPOINT_CERTIFICATE`. This variable adds CAcert certificates to API Catalog CLI.

### Fixed Issues

| Issue Resolution | ID | 
|---|---|
| API Catalog now successfully publishes ASSETs when running behind a proxy. | W-12353992 | 

## 1.0.2

**July 23, 2022**

### Fixed Issues

| Issue | ID | 
|---|---|
| API Catalog now successfully creates the documentation page when defining references between markdown files. | W-11133763 | 

## 1.0.1

May 17, 2022

### What’s New

This release includes the following changes:

- 
Improvements to the documentation in the `api-catalog-tool`Github repository and the`api-catalog-cli`npm page

## 1.0.0

May 16, 2022

### What’s New

You can autocatalog your APIs using the API Catalog CLI commands as follows:

- 
Run the API Catalog `create-descriptor`command to identify and create descriptor information for all API assets in your API project directory structure.
- 
Run the API Catalog `update-descriptor`command to identify new and changed APIs and update the descriptor information.
- 
Reference the descriptor file in the API Catalog `publish-asset`command to publish the API assets to Exchange either at a command prompt or as part of your CI/CD pipelines or custom scripts.

You can control the API information to publish using the descriptor file as follows:

- 
Add descriptor information that cannot be automatically generated, such as version strategies and tags. 
- 
Add descriptor conditions and pass parameters to the publish command to determine whether all or some of the APIs are published. 
- 
Add descriptor conditions and pass parameters to the publish command to control the version strategy of the APIs that are published. 

### Commands

| Command | Description | 
|---|---|
| Configures autocompletion for API Catalog commands | |
| api-catalog conf | Creates or deletes a credentials configuration file | 
| api-catalog create-descriptor | Creates a descriptor file | 
| api-catalog update-descriptor | Updates a descriptor file | 
| api-catalog publish-asset | Publishes assets to Exchange | 

### Documentation

For details, see the [API Catalog CLI documentation](../../exchange/apicat-about-api-catalog-cli).

### See Also

- 
[Salesforce Help](https://help.salesforce.com)
- 
[MuleSoft Services](https://www.mulesoft.com/support-and-services)