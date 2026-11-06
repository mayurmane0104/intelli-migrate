# Create an API Specification with the Text Editor | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/design-center/design-create-publish-api-raml-editor](https://docs.mulesoft.com/design-center/design-create-publish-api-raml-editor)

---

# Create an API Specification with the Text Editor

You can use API Designer’s text editor to create API specifications directly in RAML 0.8, RAML 1.0, OAS 2.0, OAS 3.0, AsyncAPI 2.6, and AsyncAPI 2.0. You can create OAS and AsyncAPI API specifications as JSON or YAML files.

## Before You Begin

Within Anypoint Platform, your user ID must be assigned the *Design Center Developer* permission.

## Procedure

- 
On the **Projects**page in Design Center, click**Create new**.
- 
Select **New API Specification**to create a REST API or**New AsyncAPI**to create an AsyncAPI.
- 
In the **New API Specification**or**New AsyncAPI**dialog, name your project.You can change the name (but not the extension) later, if you want to. 
- 
To start creating a REST API specification: - 
Select the **I’m comfortable designing it on my own**option.
- 
Choose either the RAML or OAS specification. API Designer creates the stubs of your API specification using the specification type and version you choose. By default, API Designer creates a RAML 1.0 file. You can change the file to RAML 0.8 or OAS after the project is created. Projects for creating API specifications can contain a mix of RAML, OAS, and other types of files. 
 
- 
- 
To start creating an AsyncAPI specification: - 
Select either YAML or JSON as the project language. 
 
- 

The text editor opens.

The API Designer text editor is divided into panels:

- 
The left panel lists the files and dependencies in your project. The stub specification file is listed and set as the root file of the project. You can change the name (but not the extension) of this file by clicking the overflow menu icon ( ![Screenshot of the overflow menu icon manage dependency versions design center 018a5](_images/manage-dependency-versions-design-center-018a5.png) ) beside the specification name and selecting ) beside the specification name and selecting**Rename**.The left panel also lists the file `exchange.json`, which is a file that contains metadata required by Anypoint Exchange at the time that you publish your project to Exchange. This file is read-only.You can create more than one API specification or related file in a single project. Click the plus sign in the Files panel to create a new file. If you do create more than one specification file, you must specify one of them as the root file of your project. For more information about adding Exchange dependencies, see "Adding Dependencies to an API-Specification Project", which is linked to from the **See also**section at the end of this topic.
- 
The middle panel displays the editor in which you create the API specification. Appearing in the editor when you create a project or start a new API specification are the first two lines of an API specification file, depending on which type of specification you select when you created the project. You can change these lines (as well as the file extension) if you want to switch from RAML to OAS or vice-versa. 
- 
The right panel lists the types and resources that are in the API specification that is in the middle panel. 
- 
The bottom panel expands to show any project errors. The **Project Errors**panel shows any functional errors for your API specifications and any conformance messages if you are using API Governance and the API specification you are editing has rulesets applied to it as dependencies.

## The Editor

While working in the editor, you can use a large number of commands to navigate through and manipulate the content of your API specification. Press **F1** to see a list of these commands, along with keyboard shortcuts for most of the commands.

You can also perform these tasks:

- 
**Import files and API fragments into your project**You can import either separate files or files bundled in .zip files. The files can be on your computer or you can specify a URL for them if they are located online. For more information about importing files and steps for how to import them, see "Import Files into an API Project", which is linked to from the **See also**section at the end of this topic.For information about adding API fragments to your project, see "Add a RAML API Fragment to an API-Specification Project as a Dependency", which is linked to from the **See also**section at the end of this topic.

| File uploads are restricted to supported formats. | 

- 
**Simulate calls to your API**When you draft a REST API specification, you can simulate calls to the specified endpoints. For more information, view the topic "Simulate Calls to an API", which is linked to from the **See also**section at the end of this topic.
- 
**Export your API project or specification**At any time, you can export your project as a ZIP file. Click the gear icon in the top-right corner of the text editor and select **Download Project**.
- 
**Download files**Click the dots to the right of the file name and select **Download**.
- 
**Download files in a different format**Click the dots to the right of the file name of a specification and select **Download as**. You can download your specification in one of the other supported formats. If your specification is in RAML, you can download it in OAS YAML or in OAS JSON. If your specification is in OAS, you can download it in RAML 0.8 or in RAML 1.0.The files downloaded through this option are not guaranteed to be valid. This option is intended to provide the basis for the development of a new specification or the continuation of the development of the original specification in a new format. 

## What to Do Next

If you are satisfied with your API specification, you can publish it to Exchange. See [Publish an API Specification](design-publish).