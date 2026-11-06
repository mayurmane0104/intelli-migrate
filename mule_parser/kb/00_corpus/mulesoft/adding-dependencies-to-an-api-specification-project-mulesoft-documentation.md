# Adding Dependencies to an API-Specification Project | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/design-center/design-add-api-dependency](https://docs.mulesoft.com/design-center/design-add-api-dependency)

---

# Adding Dependencies to an API-Specification Project

In projects for API specifications or API fragments, you can add dependencies of either RAML fragments, OAS components, JSON schemas, or rulesets. Because the dependencies are referenced in Anypoint Exchange, you cannot directly edit them in your projects.

If you export your project or someone downloads your project as RAML from Exchange, the resulting ZIP file contains the referenced dependencies.

| You must not edit the referenced dependencies in an editor other than the API Designer editor. If you export your project to work on it in another editor, edit the referenced dependencies,
and then try to import the project back into the text editor, the import fails. Studio does not support OAS 3.0 fragments. | 

## Add Dependencies to an API-Specification Project

| You can add up to 100 dependencies(Fragments and Rulesets) per project. | 

To add dependencies to an API-specification project:

- 
In the text editor navigation menu, click the **Exchange dependencies**icon (![Exchange Dependencies icon manage dependency versions design center d96c7](_images/manage-dependency-versions-design-center-d96c7.png) ). ).
- 
Click the add icon (+) for the dependency type that you want to add. 
- 
To filter the list of dependencies you can: - 
Select an organization 
- 
Search by keyword 
- 
Select **Include versions in Development**
 
- 
- 
Select the dependency versions you want to add: - 
To use a version of a dependency other than latest, select the version for that dependency in the **Version**drop-down.
- 
To view only the dependencies you’ve selected, click **Show selected only**.
- 
You can see the format of the fragment (RAML, OAS, or JSON schema) next to each fragment’s name. 
 
- 
- 
Click **Add dependency**.

| API Designer supports a maximum of 1,000 files for dependencies, with a total file size no greater than 300 MB. | 

## View Dependency Contents

To view the contents of a dependency, click the more options menu icon (![Three vertical dots overflow menu icon](_images/overflow-menu-icon.png) ) for that dependency and then select

) for that dependency and then select **Show in Files** or **Open in Exchange**.

| If you select Show in Files, theFilessection expands and the dependencies are shown in the`exchange_modules`section. The subsections correspond to the URI for the referenced dependency, which is its asset identifier, or GAV (group ID, asset ID, and version), in Exchange. | 

When you are ready to continue work on your API project, click **Files** > API project file name.

## Ruleset Dependencies

If your API has been identified as governed through centralized API governance, a dot or warning icon appears on the **Exchange dependencies** icon to indicate you need to take action on the dependencies for this project. Click the **Exchange dependencies** icon to view and follow the interactive instructions to add rulesets as dependencies to your project.

Even if your projects have not been identified as requiring action, you can proactively check the conformance of your APIs by adding published rulesets as dependencies to your API project.

If your API fails to conform to the rulesets that your organization validates against, you get an email notification.
You can click **Code in Design Center** to open API Designer, or click **API Details in Exchange** to be redirected to the API asset Conformance Status page.

- 
If the asset version has an editable branch in API Designer, a pop-up appears where you can see the missing rulesets filtered by tags, category, and lifecycle state. To edit those filters, click **Edit criteria**. When you are done, click**Add all rulesets**.
 *Result*: The rulesets are added to your project.
- 
If the asset version doesn’t have an editable branch in API designer, you can either select an editable branch of your project or create a new branch from your current version. You can then add the missing rulesets to that editable branch. When you have your branch, a pop-up appears where you can see the missing ruleset filtered by tags, category, and lifecycle state. To edit those filters, click **Edit criteria**. When you are done, click**Add all rulesets**.
 *Result*: The rulesets are added to your project.

## Improving Ruleset Validation

When you add rulesets as dependencies, the rulesets are automatically validated by default. The complexity of the API and rulesets might increase the number of diagnostics being computed and trigger multiple automatic validations.

The validation takes more time if:

- 
Your API is modularized, has complex recursive types, or has circular references. 
- 
You add multiple ruleset dependencies to an API project. 
- 
You are consuming a significant amount of browser resources. 

To improve ruleset validation times:

- 
Close unnecessary browser tabs or applications. 
- 
Ensure your device is running efficiently and has enough memory and CPU resources. 
- 
Switch to manual validation. This runs a single validation for each ruleset rather than triggering multiple automatic validations that might exhaust your available resources. 

If the validation process takes too long, a warning message appears informing you that auto-validation is disabled for that project.

- 
To change to manual mode, click **Ok**.
- 
To continue using auto-validation, click **Cancel**. Note that if the auto-validation of rulesets still takes too long, you get the warning message again.

You can switch between auto-validation and manual validation in your API project. This changes the validation setting for that specification only.

To turn on manual validation of your rulesets:

- 
In the **Project Errors**section of the text editor, select the**Governance**tab.
- 
Click the **Governance auto-validation**icon (![Governance auto-validation green governance auto validation](_images/green-governance-auto-validation.png) ) to disable auto-validation. ) to disable auto-validation.
- 
Click the **Validate for governance**icon (![Validate for governance validate for governance](_images/validate-for-governance.png) ) to enable manual validation. ) to enable manual validation.This runs a single validation for each ruleset rather than triggering multiple automatic validations that might exhaust your available resources. 

To enable auto-validation again:

- 
In the **Project Errors**section of the text editor, select the**Governance**tab.
- 
Click the auto-validation icon ( ![Governance auto-validation red governance auto validation](_images/red-governance-auto-validation.png) ) to enable auto-validation again. ) to enable auto-validation again.

| If the auto-validation still takes too long, you get the warning message again. | 

## Fix Governance Conformance Issues

After you add the rulesets as dependencies, you can view the conformance messages in the **Project Errors** section of the text editor. Use the provided information to fix any conformance issues and then republish your API specification.