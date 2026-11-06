# Validating API Specifications Against Governance Rulesets | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/anypoint-code-builder/des-govern-api](https://docs.mulesoft.com/anypoint-code-builder/des-govern-api)

---

- 
The specification has this markup: `#%RAML 1.0 title: my-des-with-governance protocols: - HTTP`yaml
- 
The design project for the specification applies these rulesets: - 
HTTPS Enforcement 
- 
Anypoint Best Practices 
 
- 

# Validating API Specifications Against Governance Rulesets

Test your API specifications in Anypoint Code Builder design projects against rules in governance rulesets, and fix conformance issues that result.

For information about rulesets and governance, see [Anypoint API Governance Concepts](../api-governance/#anypoint-api-governance-concepts).

## Before You Begin

You must have an API design project with a supported specification in Anypoint Code Builder:

## Workflows and tasks

A typical workflow consists of one or more of the following tasks:

- 
Add one or more rulesets to an API design project: 
- 
Run rules in the rulesets to determine if your API specification conforms with the rules: 
- 
Fix any conformance issues in the specification: 

## Add Rulesets to a Project

Add governance rulesets as dependencies to your API design project in Anypoint Code Builder.

Rulesets are hosted on Exchange. MuleSoft provides a number of public rulesets that you can find from Anypoint Code Builder or review directly on [Exchange](https://anypoint.mulesoft.com/exchange/?type=ruleset&show=mulesoft&sort=last&view=grid). For example, the ruleset [Anypoint Best Practices](https://anypoint.mulesoft.com/exchange/68ef9520-24e9-4cf2-b2f5-620025690913/anypoint-best-practices/minor/1.6/) provides documentation and examples. Your team can also create and publish rulesets for your organization to Exchange (see [Creating Custom Governance Rulesets](../api-governance/create-custom-rulesets)).

- 
Open your API design project in Anypoint Code Builder. 
- 
From the **Explorer**, expand the**Governance Rulesets**panel in your project.If the panel is not in the **Explorer**, activate the panel from the**Views and More Actions…**(**…**) menu in the**Explorer**.
- 
Add a ruleset: - 
If the panel does not contain any rulesets, click **Add Rulesets**. For example:![Governance Rulesets panel](_images/gov-rulesets-add-panel.png) 
- 
If the panel contains rulesets, you can hover over the panel and click ![](_images/icon-gov-ruleset-add.png) ( (**Add Governance Rulesets**) to add another ruleset. For example:![Add ruleset icon](_images/gov-rulesets-add-panel-not-empty.png) 
 
- 
- 
If prompted, sign in to Anypoint Platform. 
- 
Search for the ruleset, and click **Add Rulesets**. For example:![All Available Rulesets](_images/gov-rulesets-search-add.png) You can also narrow your search to specific organizations from the **Any organization**menu, and you can select a different version of a ruleset if more than one version is available.
- 
Proceed to [Run Rules Against Your API Specification](#run-rules).

## Centralized Rulesets for Topics and Agents

If you enable your API project for topics and agents, the **SF API Topic and Action Enablement** centralized ruleset is added to your topic-enabled API project automatically.

For more information, see [Topic and Agent Governance Rulesets](ai-enabling-api-project-topic-center#governance-rulesets).

## Run Rules Against Your API Specification

Determine whether your API specification conforms with rules in governance rulesets.

- 
Open your API design project in Anypoint Code Builder. 
- 
From the **Explorer**, expand the**Governance Rulesets**panel to check for rulesets in your project.- 
If any rulesets are present and you don’t intend to add more, proceed to the next step. ![Add ruleset icon](_images/gov-rulesets-add-panel-not-empty.png) 
- 
If no rulesets are present or if you intend to add more rulesets, go to [Add Rulesets to a Project](#add-rulesets).![Governance Rulesets panel](_images/gov-rulesets-add-panel.png) 
 
- 
- 
Run rules from the **Governance Rulesets**panel.You can run rulesets at multiple levels: - 
All rules in all rulesets ![Clicking icon to run all rulesets](_images/gov-rulesets-run-all.png) 
- 
All rules in a single ruleset ![Clicking icon to run a rulesets](_images/gov-rulesets-run-ruleset.png) 
- 
A single rule in a ruleset ![Clicking icon to run a rule](_images/gov-rulesets-run-rule.png) You can monitor the rules as they run. For example: ![Rules running in the panel](_images/gov-rulesets-running.png) 
 
- 
- 
If any rules return an error ( ![](_images/icon-gov-rule-error.png) ) or a warning ( ) or a warning (![](_images/icon-gov-rule-warning.png) ), proceed to ), proceed to[Fix Conformance Issues](#fix-issues).For example, this ruleset returns a warning on some rules: ![Ruleset with warnings in API Governance panel](_images/gov-rulesets-warning.png) Execution times displayed for a ruleset (such as 19.25s) represent the sum of time it takes to run each rule. Due to parallel execution of rules on machines with multiple cores, the execution time displayed for a ruleset is likely to be greater than the actual time to complete the execution. The **Governance Results**panel also identifies any warnings or errors. For example:![Ruleset with warnings in Governance Results panel](_images/gov-rulesets-warning-output.png) 

## Fix Conformance Issues

To address rules that return errors or warnings, fix the specification to comply with the rules. Then re-run the rules to ensure that the fix is effective.

### Example

To illustrate the process for addressing issues, the example in this procedure starts with a partial RAML specification and some rulesets:

![Re-running HTTPs rule](_images/gov-example-prefix.png)


## Full Example

### Fix Conformance Issues

To fix errors (![](_images/icon-gov-rule-error.png) ) and warnings (

) and warnings (![](_images/icon-gov-rule-warning.png) ):

):

- 
Run the rulesets in your project. For guidances, see [Run Rules Against Your API Specification](#run-rules).
- 
Review any resulting errors and warnings in the **Governance Results**panel. For example:![Error and Warnings in Governance Rulesets](_images/gov-example-postrun-issues.png) **Governance Results**lists the corresponding issues. For example:![Error and Warnings in Governance Results](_images/gov-example-postrun-issues-output.png) - 
`Error: [HTTPS Enforcement] Only use https protocol scheme.`
- 
`Warning: [Anypoint Best Practices] Provide the documentation for the API.`
- 
`Warning: [Anypoint Best Practices] Provide the description for the API.`
 
- 
- 
Address errors in the specification. For instance, fix the **HTTPS Enforcement**error in the[specification example](#example)by changing`HTTP`to`HTTPS`:`#%RAML 1.0 title: my-des-with-governance protocols: - HTTPS`yaml
- 
Re-run the failing rule to ensure that the error is fixed. For instance, after fixing the `protocols`error in the[specification example](#example), run**use-https-for-scheme-protocol**from the**Governance Rulesets**panel. For example:![Re-running HTTPs rule](_images/gov-example-run-fixed-error-https.png) Notice that the error no longer appears in **Governance Rulesets**. For example:![Fixed HTTPs rule](_images/gov-example-error-fixed-https.png) In addition, the **Governance Results**panel no longer lists the issue.
- 
Address warnings, as needed. For instance: - 
Address the warning `Provide the description for the API`by adding a`description`to the[specification example](#example). For example:`#%RAML 1.0 title: my-des-with-governance description: my description protocols: - HTTPS`yamlThe description is between `title`and`protocols`.
- 
Re-run the rule **api-must-have-description**, and notice that the specification now conforms to the rule.![Fixed description](_images/gov-example-warning-fixed-description.png) The ruleset continues to identify a warning because a different rule in the ruleset has a warning. 
 
- 
- 
Address any remaining issues that you intend to fix. For instance, for the warning `Provide the documentation for the API`in the[example](#example), add and save`documentation`markup to the specification:`#%RAML 1.0 title: my-des-with-governance description: my description documentation: - title: My Title content: | Welcome to my API documentation. - title: Legal content: | This is my legal documentation. protocols: - HTTPS`yaml
- 
Re-run the corresponding rule from the **Governance Rulesets**panel.For example, re-run **api-must-have-documentation**, and notice that the specification now conforms to the rule.![Fixed documentation](_images/gov-example-warning-fixed-all.png) 

The specification has no more errors or warnings. For example:

![Panel displaying rulesets validate](_images/gov-example-error-fixed-all.png)


## Remove a Ruleset from a Project

- 
In the **Governance Ruleset**panel, hover over a ruleset to display the**More actions**(**…**) menu.
- 
In the **More actions**menu, click**Remove Ruleset…**.

You can also use the command **MuleSoft: Remove Governance Ruleset…** from the command palette for this purpose.

## Open a Ruleset YAML File

To examine the configuration of a ruleset’s YAML file:

- 
In the **Governance Ruleset**panel, hover over a ruleset to display its**More actions**(**…**) menu.
- 
Click **Show in Files**to open the YAML file in a**ruleset.yaml**tab in the IDE.

The following example shows version 1.6.1 of the HTTPS Enforcement YAML file:

```
#%Validation Profile 1.0
profile: HTTPS enforcement
description: This ruleset helps ensure the use of HTTPS across URLs in API
  definitions, both in the base server URL and in any callbacks optionally
  defined.
violation:
  - use-https-for-callbacks
  - use-https-for-scheme-protocol
  - use-https-for-urls
tags:
  - security
validations:
  use-https-for-callbacks:
    message: "{{apiContract.expression}} must use https as it is a callback url"
    targetClass: apiContract.Callback
    propertyConstraints:
      apiContract.expression:
        pattern: ^https://
    examples:
      valid: |
        openapi: "3.0.0"
        info:
          title: example API
          version: "1.0.0"
        paths:
          /subscribe:
            post:
              responses:
                '201':
                  description: Webhook created
              callbacks:
                myEvent:
                  'https://{$request.body#/callbackUrl}'
      invalid: |
        openapi: "3.0.0"
        info:
          title: example API
          version: "1.0.0"
        paths:
          /subscribe:
            post:
              responses:
                '201':
                  description: Webhook created
              callbacks:
                myEvent:
                  'http://{$request.body#/callbackUrl}'
  use-https-for-scheme-protocol:
    message: Only use https protocol scheme
    targetClass: apiContract.WebAPI
    not:
      propertyConstraints:
        apiContract.scheme:
          containsSome:
            - HTTP
            - http
    examples:
      valid: |
        #%RAML 1.0
        protocols:
          - HTTPS
      invalid: |
        #%RAML 1.0
        protocols:
          - HTTP
  use-https-for-urls:
    message: "{{core.urlTemplate}} should use https"
    targetClass: apiContract.Server
    propertyConstraints:
      core.urlTemplate:
        pattern: ^https://
    examples:
      valid: |
        openapi: "3.0.0"
        servers:
          - url: "https://mySecureEndpoint"
            description: "My endpoint that uses HTTPS"
      invalid: |
        openapi: "3.0.0"
        servers:
          - url: "http://myNotSoSecureEndpoint"
            description: "My endpoint that uses HTTP"
```
YAML## Open a Ruleset in Exchange

In Exchange, rulesets list all rules and can provide documentation with examples.

To open the ruleset in Exchange:

- 
In the **Governance Ruleset**panel, hover over a ruleset to display its**More actions**(**…**) menu.
- 
Click **Open in Exchange**.

## Change a Ruleset Version

To select a different version of a ruleset:

- 
In the **Governance Ruleset**panel, hover over a ruleset to display its**More actions**(**…**) menu.
- 
Click **Change Version…**.
- 
Select a different version from the **Change Version**menu that opens.