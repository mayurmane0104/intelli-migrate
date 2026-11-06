# https://docs.mulesoft.com/release-notes/code-builder/acb-release-notes.md

**Source:** [https://docs.mulesoft.com/release-notes/code-builder/acb-release-notes.md](https://docs.mulesoft.com/release-notes/code-builder/acb-release-notes.md)

---

```
# Anypoint Code Builder Release Notes
> For the full documentation index, see: https://docs.mulesoft.com/llms.txt
![logo cloud IDE](../../_/img/logos/deployment-cloud-ide.png "Cloud IDE") Cloud IDE
![logo desktop IDE](../../_/img/logos/deployment-desktop-ide.png "Desktop IDE") Desktop IDE
**Open Beta Release**: The **cloud IDE is in open beta**. Any use of Anypoint Code Builder in its
beta state is subject to the applicable beta services terms and conditions, available from the IDE.
Use the Anypoint Code Builder integrated development environment (IDE) for your API designs,
implementations, and integration development. Work locally with Anypoint Code Builder for Desktop on
Microsoft Visual Studio Code (VS Code) or from your browser with Anypoint Code Builder on Anypoint
Platform. The IDEs support the development lifecycle:
- API specification design (AsyncAPI, gRPC, OAS, and RAML), a mocking service for testing, source
  control, and publication to Anypoint Exchange
- API implementation features for importing supported API specifications (AsyncAPI, GraphQL, gRPC,
  OAS, and RAML) and autogenerating interfaces (scaffolding) for flows and error handlers within a
  Mule application
- Integration development to connect systems, transform data to required formats, and provide
  business logic to manage messages and events programmatically within a Mule application
## June 11, 2026
Anypoint Code Builder releases this version in the Anypoint Extension Pack.
- Extension pack version: 1.21.1
  To use this extension pack in the desktop IDE, see
  [Set up the Desktop IDE](../../anypoint-code-builder/start-acb#set-up-desktop).
  To learn about hardware and storage requirements for the desktop IDE, see
  [Desktop IDE Hardware and Storage Requirements](../../anypoint-code-builder/start-acb#hardware-storage-requirements).
For extension versions, see the
[Change Log](https://marketplace.visualstudio.com/items/salesforce.mule-dx-extension-pack/changelog)
in the VS Code Marketplace.
For more information, see [Compatibility](#compatibility).
### Fixed Issues
<table><colgroup><col> <col></colgroup><thead><tr><th>Issue Resolution</th><th>ID</th></tr></thead><tbody><tr><td><div><div><p>MCP tools now display correctly across supported IDEs. The connectivity MCP server can appear without registered tools in this release, which is the expected behavior.</p></div></div></td><td><div><div><p>W-22854860</p></div></div></td></tr></tbody></table>
## May 26, 2026
Anypoint Code Builder releases this version in the Anypoint Extension Pack.
- Extension pack version: 1.20.1
  To use this extension pack in the desktop IDE, see
  [Set up the Desktop IDE](../../anypoint-code-builder/start-acb#set-up-desktop).
To learn about hardware and storage requirements for the desktop IDE, see
[Desktop IDE Hardware and Storage Requirements](../../anypoint-code-builder/start-acb#hardware-storage-requirements).
For extension versions, see the
[Change Log](https://marketplace.visualstudio.com/items/salesforce.mule-dx-extension-pack/changelog)
in the VS Code Marketplace.
For more information, see [Compatibility](#compatibility).
### Fixed Issues
<table><colgroup><col> <col></colgroup><thead><tr><th>Issue Resolution</th><th>ID</th></tr></thead><tbody><tr><td><div><div><p>Anypoint Code Builder no longer shows duplicate or triplicate items when selecting a project for testing.</p></div></div></td><td><div><div><p>W-22565928</p></div></div></td></tr></tbody></table>
## May 19, 2026
Anypoint Code Builder releases this version in the Anypoint Extension Pack.
- Extension pack version: 1.19.2
  To use this extension pack in the desktop IDE, see
  [Set up the Desktop IDE](../../anypoint-code-builder/start-acb#set-up-desktop).
  To learn about hardware and storage requirements for the desktop IDE, see
  [Desktop IDE Hardware and Storage Requirements](../../anypoint-code-builder/start-acb#hardware-storage-requirements).
For extension versions, see the
[Change Log](https://marketplace.visualstudio.com/items/salesforce.mule-dx-extension-pack/changelog)
in the VS Code Marketplace.
For more information, see [Compatibility](#compatibility).
### Whatâ€™s New
This release introduces these features.
- [Auto-Scroll Canvas During Debugging](#auto-scroll-canvas-debugging-may-2026)
- [Enhanced Breakpoint Visualization](#breakpoint-highlighting-may-2026)
- [MuleSoft Vibes Updates](#vibes-updates-may-2026)
- [Deprecation of the Develop the American Flights App Tutorial](#american-flights-tutorial-deprecated-may-2026)
### Auto-Scroll Canvas During Debugging
The canvas now automatically scrolls to and centers the active component when you step through your
application during debugging. For more information, see
[Canvas Behavior While Debugging](../../anypoint-code-builder/int-debug-mule-apps#canvas-execution-indicators).
### Enhanced Breakpoint Visualization
Active breakpoints during debugging now display with a yellow outline on the canvas, making it easy
to identify which component execution has paused at. For more information, see
[Debugging Mule Applications](../../anypoint-code-builder/int-debug-mule-apps).
### MuleSoft Vibes Updates
#### Manage Default Skills
Default Skills in MuleSoft Vibes give agents preloaded, reusable instructions for common Mule
development tasks such as project work, connector setup, and dependency resolution. For more
information, see
[Manage Default Skills in MuleSoft Vibes](../../anypoint-code-builder/vibes-skills#manage-default-skills).
#### Run Multiple Integration Projects Locally
Run multiple integration projects locally in one runtime to validate service-to-service behavior
before deployment. Use MuleSoft Vibes to automatically create and run a reusable multi-project run
configuration, including run and debug scenarios. You can also run saved configurations from the
standard **Run and Debug** panel. For more information, see
[Running Multiple Local Integration Projects with MuleSoft Vibes](../../anypoint-code-builder/vibes-run-multiple-integration-projects-locally).
#### Modernize Development with the New Descriptive UI
MuleSoft Vibes now features a vertical canvas that uses AI to generate plain-language descriptions
for every component in your flow. Build, modify, and document integrations using natural language
commands or direct UI interactions. For more information, see
[Descriptive UI in MuleSoft Vibes](../../anypoint-code-builder/vibes-get-started#vibes-descriptive-ui).
### Deprecation of the Develop the American Flights App Tutorial
The **Develop the American Flights App** tutorial is deprecated. For an alternative tutorial, see
[Tutorial: Build an API from Start to Finish](../../general/api-led-overview).
### Fixed Issues
<table><colgroup><col> <col></colgroup><thead><tr><th>Issue Resolution</th><th>ID</th></tr></thead><tbody><tr><td><div><div><p>The debugger now focuses on the correct file as expected when debugging multiple files simultaneously.</p></div></div></td><td><div><div><p>W-20493459</p></div></div></td></tr><tr><td><div><div><p>Sample data specified in custom metadata examples now loads correctly in the transformation window.</p></div></div></td><td><div><div><p>W-21314835</p></div></div></td></tr><tr><td><div><div><p>Sample data displayed in <strong>Expression Builder</strong> now matches the persisted sample data as expected.</p></div></div></td><td><div><div><p>W-21319134</p></div></div></td></tr><tr><td><div><div><p>Type propagation now resolves correctly without unexpected failure errors.</p></div></div></td><td><div><div><p>W-21485471</p></div></div></td></tr><tr><td><div><div><p>The debugger now displays <strong>Mule Message</strong> component values correctly for non-Java data types.</p></div></div></td><td><div><div><p>W-21707026</p></div></div></td></tr><tr><td><div><div><p>Copying JSON from a Mule event in debug mode now works as expected without errors.</p></div></div></td><td><div><div><p>W-21707258</p></div></div></td></tr><tr><td><div><div><p>Type propagation no longer fails when component location returns null values.</p></div></div></td><td><div><div><p>W-21735935</p></div></div></td></tr><tr><td><div><div><p>Variable value updates in the debugger now work as expected during debugging sessions.</p></div></div></td><td><div><div><p>W-21936302</p></div></div></td></tr><tr><td><div><div><p>Error breakpoint exception messages now provide clearer and more actionable information.</p></div></div></td><td><div><div><p>W-21957772</p></div></div></td></tr><tr><td><div><div><p>Breakpoint icons on the canvas now correctly display their muted state.</p></div></div></td><td><div><div><p>W-21986288</p></div></div></td></tr><tr><td><div><div><p>Signing in now works as expected for all users.</p></div></div></td><td><div><div><p>W-22000712</p></div></div></td></tr><tr><td><div><div><p>Document identifiers now propagate correctly across all batch steps in the <strong>Batch Processing</strong> connector.</p></div></div></td><td><div><div><p>W-22002465</p></div></div></td></tr><tr><td><div><div><p>The <strong>Go To Flow</strong> navigation feature no longer has intermittent failures.</p></div></div></td><td><div><div><p>W-22043908</p></div></div></td></tr><tr><td><div><div><p>Error objects are now visible in the <strong>VARIABLES</strong> panel when debugging inside error handler scopes.</p></div></div></td><td><div><div><p>W-22099074</p></div></div></td></tr><tr><td><div><div><p>Mapping icons now work correctly when variables are present in scripts.</p></div></div></td><td><div><div><p>W-22100547</p></div></div></td></tr><tr><td><div><div><p>MuleSoft Vibes no longer shows <strong>ValidationException</strong> errors for large prompts or PII context window connection errors.</p></div></div></td><td><div><div><p>W-22107257</p></div></div></td></tr><tr><td><div><div><p>MuleSoft Vibes MCP server connections now succeed for servers that donâ€™t support resources or prompts.</p></div></div></td><td><div><div><p>W-22116159</p></div></div></td></tr><tr><td><div><div><p>The <strong>MimeType</strong> attributes no longer incorrectly show expression mode as supported.</p></div></div></td><td><div><div><p>W-22164971</p></div></div></td></tr><tr><td><div><div><p>Project artifact IDs can now be directly inherited in parent POMs.</p></div></div></td><td><div><div><p>W-22166146</p></div></div></td></tr><tr><td><div><div><p>The undo command now executes on the first invocation instead of requiring two attempts.</p></div></div></td><td><div><div><p>W-22170160</p></div></div></td></tr><tr><td><div><div><p>The debugger can now introspect <code>ImmutableBatchJobResult</code> objects in the <strong>On Complete</strong> phase.</p></div></div></td><td><div><div><p>W-22177315</p></div></div></td></tr><tr><td><div><div><p>Token refresh no longer enters an infinite loop due to <code>setTimeout</code> overflow.</p></div></div></td><td><div><div><p>W-22251798</p></div></div></td></tr><tr><td><div><div><p>The <strong>Apply</strong> button in the <strong>HTTP Listener Global Element</strong> configuration now works as expected.</p></div></div></td><td><div><div><p>W-22321659</p></div></div></td></tr><tr><td><div><div><p>The debugger now processes files within nested folders when debugging as expected.</p></div></div></td><td><div><div><p>W-22349447</p></div></div></td></tr></tbody></table>
## April 27, 2026
Anypoint Code Builder releases these patch versions in the Anypoint Extension Pack and the Cloud
IDE.
- Extension pack version: 1.18.1
  To use this extension pack in the desktop IDE, see
  [Set up the Desktop IDE](../../anypoint-code-builder/start-acb#set-up-desktop).
  To learn more about hardware and storage requirements for the desktop IDE, see
  [Desktop IDE Hardware and Storage Requirements](../../anypoint-code-builder/start-acb#hardware-storage-requirements).
- Cloud IDE version: 1.18.3
  This cloud IDE version runs the 1.18.3 extension pack.
### Fixed Issues
<table><colgroup><col> <col></colgroup><thead><tr><th>Issue Resolution</th><th>ID</th></tr></thead><tbody><tr><td><div><div><p>Applying policies with required schema properties that have default values in Agent Networks no longer causes failures.</p></div></div></td><td><div><div><p>W-22170170</p></div></div></td></tr></tbody></table>
## April 20, 2026
Anypoint Code Builder releases these versions in the Anypoint Extension Pack and the Cloud IDE.
- Extension pack version: 1.18.0
  To use this extension pack in the desktop IDE, see
  [Set up the Desktop IDE](../../anypoint-code-builder/start-acb#set-up-desktop).
  To learn about hardware and storage requirements for the desktop IDE, see
  [Desktop IDE Hardware and Storage Requirements](../../anypoint-code-builder/start-acb#hardware-storage-requirements).
- Cloud IDE version: 1.18.1
  This cloud IDE version runs the 1.18.0 extension pack.
### Whatâ€™s New
This release introduces these features.
- [Canvas Actions](#canvas-actions-april-2026)
- [Namespaces in DataWeave Scripts](#namespaces-in-dw-scripts)
- [MuleSoft Vibes Updates](#mulesoft-vibes-updates-april-20-2026)
- [Centralized Errors and Warnings](#acb-logs-centralized-panel-april-2026)
### Canvas Actions
You can now refactor flows directly from the canvas, including moving, copying, and extracting
components into new flows or subflows. Fore more information, see
[Refactor Flows Using Canvas Actions](../../anypoint-code-builder/int-configure-components#canvas-actions).
### Namespaces in DataWeave Scripts
Anypoint Code Builder now supports metadata containing namespace URIs. For more information, see
[Namespaces in Generated DataWeave](../../anypoint-code-builder/int-configure-dw-expressions#namespaces-in-generated-dataweave).
### MuleSoft Vibes Updates
MuleSoft Vibes now supports custom metadata and reusable instructions with skills.
#### Custom Metadata Full Support
Create, delete, fetch, or edit custom metadata across these metadata types: csv, copybook, excel,
fixed width, flat file, json, java, simple type, and xml. For more information, see
[Custom metadata in MuleSoft Vibes](../../anypoint-code-builder/int-manage-custom-metadata#custom-metadata-vibes).
#### Reusable Instructions with Skills
Create and reuse instructions with MuleSoft Vibes Skills. Save instructions as skills to easily
apply them across multiple conversations and projects, ensuring consistency and efficiency in your
interactions. For more information, see
[Using Skills with MuleSoft Vibes](../../anypoint-code-builder/vibes-skills).
### Centralized Errors and Warnings
The new **ACB Logs** tab provides a single, table-based view of warnings and errors from every
Anypoint Code Builder extension, so you can scan, filter, and search without switching between
channels. You can filter by log level, source extension, date range, and project name. Expand an
entry for full details such as stack traces and include Anypoint Code Builder Logs automatically
when you export troubleshooting information. For full raw log streams from one channel at a time,
keep using the **Output** panel (for example, **Mule DX Server** or **Mule DX Server:
Scaffolding**). For more information, see
[Viewing Logs and Errors](../../anypoint-code-builder/start-open-output-panel).
### Fixed Issues
<table><colgroup><col> <col></colgroup><thead><tr><th>Issue Resolution</th><th>ID</th></tr></thead><tbody><tr><td><div><div><p><strong>Enum option</strong> lists now appear as expected inside arrays in the configuration UI.</p></div></div></td><td><div><div><p>W-20031362</p></div></div></td></tr><tr><td><div><div><p>Publishing a project to Anypoint Exchange no longer creates an example project unexpectedly.</p></div></div></td><td><div><div><p>W-20969183</p></div></div></td></tr><tr><td><div><div><p>Opening a project no longer takes more time than expected to load XML.</p></div></div></td><td><div><div><p>W-21154541</p></div></div></td></tr><tr><td><div><div><p>Opening a project or XML file again on Windows no longer takes an excessive amount of time.</p></div></div></td><td><div><div><p>W-21239937</p></div></div></td></tr><tr><td><div><div><p>Importing a project without sources no longer produces poor error handling.</p></div></div></td><td><div><div><p>W-21284401</p></div></div></td></tr><tr><td><div><div><p>Anypoint Code Builder AI no longer suggests an outdated Salesforce connector version.</p></div></div></td><td><div><div><p>W-21290906</p></div></div></td></tr><tr><td><div><div><p>The <strong>Transform Message</strong> component now shows the output tree for an inner field as expected.</p></div></div></td><td><div><div><p>W-21309692</p></div></div></td></tr><tr><td><div><div><p>Drag-and-drop mapping now works as expected for nested objects in flat file formats.</p></div></div></td><td><div><div><p>W-21310967</p></div></div></td></tr><tr><td><div><div><p>Metadata validation errors now work as expected for JMS and AS2 elements with Mule runtime 4.11.0.</p></div></div></td><td><div><div><p>W-21314344</p></div></div></td></tr><tr><td><div><div><p>DataWeave data preview works as expected on failure and shows log output.</p></div></div></td><td><div><div><p>W-21324741</p></div></div></td></tr><tr><td><div><div><p>The editor and workspace no longer show an unsaved file warning after saving all changes.</p></div></div></td><td><div><div><p>W-21327302</p></div></div></td></tr><tr><td><div><div><p>Importing a new API from Anypoint Exchange from the command palette no longer requires a reload to show changes.</p></div></div></td><td><div><div><p>W-21341100</p></div></div></td></tr><tr><td><div><div><p>Opening a file in a non-Mule project no longer raises nested project errors.</p></div></div></td><td><div><div><p>W-21341353</p></div></div></td></tr><tr><td><div><div><p>Field concatenation no longer fails across arrays and different sources in DataWeave.</p></div></div></td><td><div><div><p>W-21346401</p></div></div></td></tr><tr><td><div><div><p>Breakpoints in a source now stop execution as expected.</p></div></div></td><td><div><div><p>W-21352232</p></div></div></td></tr><tr><td><div><div><p>Sample generation no longer fails after changing custom metadata for the first time in the transformation window.</p></div></div></td><td><div><div><p>W-21421249</p></div></div></td></tr><tr><td><div><div><p>Progressive mapping now extends existing mappings as expected instead of replacing them.</p></div></div></td><td><div><div><p>W-21462334</p></div></div></td></tr><tr><td><div><div><p>The factory now handles the <strong>object-store-caching-strategy</strong> component as expected.</p></div></div></td><td><div><div><p>W-21467904</p></div></div></td></tr><tr><td><div><div><p>Large log files no longer slow down error logging.</p></div></div></td><td><div><div><p>W-21469432</p></div></div></td></tr><tr><td><div><div><p>The Mule::p function reference now resolves as expected.</p></div></div></td><td><div><div><p>W-21472817</p></div></div></td></tr><tr><td><div><div><p>Incorrect underline placement for DataWeave expressions in set-variable XML is fixed.</p></div></div></td><td><div><div><p>W-21473016</p></div></div></td></tr><tr><td><div><div><p>Verifying a test connection no longer randomly breaks.</p></div></div></td><td><div><div><p>W-21473880</p></div></div></td></tr><tr><td><div><div><p>A stack overflow in <code>SimpleReferenceType.metadataConstraints</code> in the DataWeave editor is fixed.</p></div></div></td><td><div><div><p>W-21485285</p></div></div></td></tr><tr><td><div><div><p>DataWeave editor no longer shows inconsistent counts of errors and warnings on the <strong>Problems</strong> tab.</p></div></div></td><td><div><div><p>W-21530956</p></div></div></td></tr><tr><td><div><div><p>The resolution of the <code>p()</code> function in DataWeave now works as expected.</p></div></div></td><td><div><div><p>W-21533179</p></div></div></td></tr><tr><td><div><div><p>Embedded documents now regenerate in DataWeave as expected.</p></div></div></td><td><div><div><p>W-21549247</p></div></div></td></tr><tr><td><div><div><p>The message reference now resolves in DataWeave as expected.</p></div></div></td><td><div><div><p>W-21550252</p></div></div></td></tr><tr><td><div><div><p>A StatusLogger format or conversion error in the design service is fixed.</p></div></div></td><td><div><div><p>W-21552602</p></div></div></td></tr><tr><td><div><div><p>Missing icons for date fields in DataWeave transforms are fixed.</p></div></div></td><td><div><div><p>W-21560510</p></div></div></td></tr><tr><td><div><div><p>Tests that affected reliability of the test suite are now stabilized and working as expected.</p></div></div></td><td><div><div><p>W-21575885</p></div></div></td></tr><tr><td><div><div><p>DataWeave syntax errors are now highlighted in configuration XML as expected.</p></div></div></td><td><div><div><p>W-21627864</p></div></div></td></tr><tr><td><div><div><p>POM.xml now resolves as expected when using a relative path.</p></div></div></td><td><div><div><p>W-21629880</p></div></div></td></tr><tr><td><div><div><p>An unexpected child element error in <strong>DefaultContainerProcessor</strong> in the DataWeave editor is fixed.</p></div></div></td><td><div><div><p>W-21631829</p></div></div></td></tr><tr><td><div><div><p>MUnit files now resolve in the workspace as expected.</p></div></div></td><td><div><div><p>W-21631910</p></div></div></td></tr><tr><td><div><div><p>Spacing around the <strong>Transform Message</strong> workspace in the DataWeave UI is tightened.</p></div></div></td><td><div><div><p>W-21638610</p></div></div></td></tr><tr><td><div><div><p>Saving files now persists changes as expected.</p></div></div></td><td><div><div><p>W-21642439</p></div></div></td></tr><tr><td><div><div><p>Clearing search on the Metadata tab now works as expected.</p></div></div></td><td><div><div><p>W-21642458</p></div></div></td></tr><tr><td><div><div><p>The canvas no longer fails to load.</p></div></div></td><td><div><div><p>W-21666326</p></div></div></td></tr><tr><td><div><div><p>Null pointer errors in the DataWeave virtual file system are fixed.</p></div></div></td><td><div><div><p>W-21667508 / W-21770880</p></div></div></td></tr><tr><td><div><div><p>The HTTP port is released as expected after use.</p></div></div></td><td><div><div><p>W-21706607</p></div></div></td></tr><tr><td><div><div><p>The restarts now pick up your latest changes as expected.</p></div></div></td><td><div><div><p>W-21706655</p></div></div></td></tr><tr><td><div><div><p>New components are no longer occasionally inserted inside a nested body instead of after it on the canvas.</p></div></div></td><td><div><div><p>W-21707238</p></div></div></td></tr><tr><td><div><div><p>Error messages now appear in the Mule event view as expected.</p></div></div></td><td><div><div><p>W-21707484</p></div></div></td></tr><tr><td><div><div><p>Intermittent socket timeout errors from Anypoint Exchange search are fixed.</p></div></div></td><td><div><div><p>W-21709965</p></div></div></td></tr><tr><td><div><div><p>A stack overflow in <strong>SimpleReferenceType.metadataConstraints</strong> caused by a self-referencing variable is fixed.</p></div></div></td><td><div><div><p>W-21712344</p></div></div></td></tr><tr><td><div><div><p>Contained element content now overrides the parent operationâ€™s general content on the canvas as expected.</p></div></div></td><td><div><div><p>W-21712983</p></div></div></td></tr><tr><td><div><div><p>The first multi-selected canvas node (Shift+click) no longer opens the configuration UI unexpectedly.</p></div></div></td><td><div><div><p>W-21780098</p></div></div></td></tr><tr><td><div><div><p>The <strong>Project Properties</strong> header now shows the project name instead of the path.</p></div></div></td><td><div><div><p>W-21804043</p></div></div></td></tr><tr><td><div><div><p>Mapping editor errors caused by VFS initialization failures are fixed.</p></div></div></td><td><div><div><p>W-21809434</p></div></div></td></tr><tr><td><div><div><p>Corrupted JDK downloads no longer report success.</p></div></div></td><td><div><div><p>W-21841815</p></div></div></td></tr><tr><td><div><div><p>Autocompletion now works as expected in customer projects.</p></div></div></td><td><div><div><p>W-21850315</p></div></div></td></tr><tr><td><div><div><p>The <strong>Extract To</strong> form now shows the correct projectâ€™s file name in the drop-down.</p></div></div></td><td><div><div><p>W-21869137</p></div></div></td></tr><tr><td><div><div><p>The <strong>Extract To</strong> form now hides non-extractable nodes when multiple nodes are selected.</p></div></div></td><td><div><div><p>W-21869146</p></div></div></td></tr><tr><td><div><div><p>The <strong>Extract To</strong> form no longer appears for nodes that canâ€™t be extracted.</p></div></div></td><td><div><div><p>W-21869157</p></div></div></td></tr><tr><td><div><div><p>The <strong>Extract To</strong> form now selects the current file by default as the extraction target.</p></div></div></td><td><div><div><p>W-21873522</p></div></div></td></tr><tr><td><div><div><p>Transform mapping data is no longer overwritten when variables are declared in the header.</p></div></div></td><td><div><div><p>W-21886152</p></div></div></td></tr><tr><td><div><div><p>Signing out of Anypoint Code Builder now works as expected.</p></div></div></td><td><div><div><p>W-21892267</p></div></div></td></tr><tr><td><div><div><p>Creating MUnit tests from a flow now works as expected.</p></div></div></td><td><div><div><p>W-21950086</p></div></div></td></tr><tr><td><div><div><p>Library configuration changes are now saved as expected when a shared library already exists in the POM.</p></div></div></td><td><div><div><p>W-21966352</p></div></div></td></tr><tr><td><div><div><p>Log files no longer use an incorrect file extension.</p></div></div></td><td><div><div><p>W-21978917</p></div></div></td></tr></tbody></table>
## March 20, 2026
Anypoint Code Builder releases these patch versions in the Anypoint Extension Pack and the Cloud
IDE.
- Extension pack version: 1.17.2
  To use this extension pack in the desktop IDE, see
  [Set up the Desktop IDE](../../anypoint-code-builder/start-acb#set-up-desktop).
- Cloud IDE version: 1.17.3
  This cloud IDE version runs the 1.17.3 extension pack.
### Fixed Issues
<table><colgroup><col> <col></colgroup><thead><tr><th>Issue Resolution</th><th>ID</th></tr></thead><tbody><tr><td><div><div><p>Opening multiple projects no longer causes errors during the initialization of the embedded DataWeave language server.</p></div></div></td><td><div><div><p>W-21618731</p></div></div></td></tr><tr><td><div><div><p>The file picker for DataWeave transformation configurations now opens as expected on Windows.</p></div></div></td><td><div><div><p>W-21651056</p></div></div></td></tr><tr><td><div><div><p>API governance validations no longer fail and display a "Validation failed: try again later" error message on Windows.</p></div></div></td><td><div><div><p>W-21568869</p></div></div></td></tr></tbody></table>
## March 16, 2026
Anypoint Code Builder releases these versions in the Anypoint Extension Pack and the Cloud IDE.
- Extension pack version: 1.17.0
  To use this extension pack in the desktop IDE, see
  [Set up the Desktop IDE](../../anypoint-code-builder/start-acb#set-up-desktop).
- Cloud IDE version: 1.17.2
  This cloud IDE version runs the 1.17.2 extension pack.
### Whatâ€™s New
This release introduces these features.
- [Anypoint Code Builder Support for gRPC](#anypoint-code-builder-grpc-support)
- [Use More MIME Types in the DataWeave Transformer](#more-mime-types-dataweave-transformer)
- [Export Mule Project Enhancements](#export-mule-project-unified)
- [MuleSoft Vibes Updates](#mulesoft-vibes-updates-march-16-2026)
- [MuleSoft MCP Server Project Updates](#mulesoft-mcp-server-project-updates)
- [Expanded MIME Type Support in DataWeave Transform](#dataweave-transform-mime-type)
- [Removal of Code Snippets Feature](#code-snippets-removal)
### Anypoint Code Builder Support for gRPC
Anypoint Code Builder now supports gRPC for API specification design, scaffolding, and
implementation. Create and import gRPC API specifications in Protocol Buffers (proto) format,
scaffold Mule projects based on those specifications, and implement the generated flows using the
Anypoint Code Builder. For more information, see
[Designing a gRPC API Specification with Anypoint Code Builder](../../anypoint-code-builder/des-design-grpc-api-spec).
### Use More MIME Types in the DataWeave Transformer
Map and transform data using any MIME type supported by the Mule platform. The **DataWeave
Transformer** component now supports all Mule runtime MIME types, moving beyond the previous
JSON-only limitation. These improvements ensure parity with the Mule runtime and enable you to build
diverse integrations without workarounds.
### Export Mule Project Enhancements
Export a Mule project as a shareable or deployable JAR using a single action in the context menu and
command palette. You can optionally include project sources for deployable JARs so the JAR can be
opened in the IDE and used for deployment. For more information, see
[Exporting Mule Projects](../../anypoint-code-builder/int-export-mule-project).
### MuleSoft Vibes Updates
Build and manage integrations more efficiently with support for adding images to your conversation,
using templates, and generating applications that include your private Exchange assets. These
updates allow you to use a wider variety of assets for application generation while tracking your
resource usage.
#### Add Files to Prompts with Multi-modal Support
Drag and drop images directly into the prompt window to provide context for your tasks. You can add
up to 10 files per conversation to help MuleSoft Vibes understand your specific requirements. For
more information, see
[Add Files to Messages with Multi-Modal Support](../../anypoint-code-builder/vibes-get-started#vibes-multimodal-file-prompts).
#### Generate Applications from Templates
Use local templates from Anypoint Exchange as the foundation for your generated applications. This
ensures that new integrations follow your organizationâ€™s established patterns and best practices.
For more information, see
[Generate Applications from Exchange Templates](../../anypoint-code-builder/vibes-create-integrations#vibes-generate-apps-from-templates).
#### Include Custom Connectors in Generated Applications
Generate applications that use custom connectors published to your private Anypoint Exchange. This
update allows you to integrate with internal or specialized systems during the automated generation
process. For more information, see
[Include Custom Connectors in Generated Applications](../../anypoint-code-builder/vibes-create-integrations#vibes-custom-connectors-generated-apps).
#### Invoke Exchange APIs Using REST Connectors
Generate applications that call APIs published to Anypoint Exchange. MuleSoft Vibes now uses REST
connectors to invoke these APIs, making it easier to reuse existing assets across your landscape.
For more information, see
[Invoke Exchange APIs Using REST Connectors](../../anypoint-code-builder/vibes-create-integrations#vibes-exchange-apis-rest-connectors).
#### Monitor Token Consumption in MuleSoft Vibes
Track the number of tokens consumed for each request and task directly within the Vibes window. This
visibility helps you manage your usage and understand the resource cost of your generation tasks.
For more information, see
[Monitor Token Consumption in MuleSoft Vibes](../../anypoint-code-builder/vibes-get-started#vibes-token-consumption-monitoring).
### MuleSoft MCP Server Project Updates
MuleSoft MCP Server includes tool updates. For more information, see
[MuleSoft MCP Server Release Notes](../mulesoft-mcp-server/mulesoft-mcp-server-release-notes#new-features-mcp-server-mar16-26).
### Expanded MIME Type Support in DataWeave Transform
DataWeave Transform in Anypoint Code Builder now expands support for MIME types across the Transform
mapper. The component automatically adjusts DataWeave script headers based on the selected metadata
and improves preview capabilities across additional formats, including Excel (XLSX) and CSV files
with custom separators. These improvements help ensure that generated transformations remain
consistent with Mule runtime behavior across a wider range of data formats.
### Removal of Code Snippets Feature
Anypoint Code Builder deprecates the code snippets feature.
### Fixed Issues
<table><colgroup><col> <col></colgroup><thead><tr><th>Issue Resolution</th><th>ID</th></tr></thead><tbody><tr><td><div><div><p>The <strong>Open Project</strong> tool no longer closes the current workspace when opening a project folder during application generation.</p></div></div></td><td><div><div><p>W-21351774</p></div></div></td></tr><tr><td><div><div><p>Core models for the Mule runtime are now correctly cached. This change prevents the design service from starting unnecessarily and improves startup performance.</p></div></div></td><td><div><div><p>W-21354463</p></div></div></td></tr><tr><td><div><div><p>Workspaces now open correctly when you create an integration project from a template.</p></div></div></td><td><div><div><p>W-21414040</p></div></div></td></tr><tr><td><div><div><p>Integration projects created from a template now correctly include <strong>JavaSpecifications</strong> in the <strong>mule-artifact.json</strong> file.</p></div></div></td><td><div><div><p>W-21439730</p></div></div></td></tr><tr><td><div><div><p><strong>Project Properties</strong> now correctly reflect the JDK version immediately after it is downloaded.</p></div></div></td><td><div><div><p>W-21514611</p></div></div></td></tr><tr><td><div><div><p>Login now works as expected on VDI machines after a previous logout.</p></div></div></td><td><div><div><p>W-21145337</p></div></div></td></tr><tr><td><div><div><p>Applications now correctly inherit characteristics from the parent pom file.</p></div></div></td><td><div><div><p>W-21368450</p></div></div></td></tr><tr><td><div><div><p>Instantiate a Mule framework instance using plugins without encountering <strong>NoSuchMethodException</strong>.</p></div></div></td><td><div><div><p>W-20922748</p></div></div></td></tr><tr><td><div><div><p>Project-specific connector operations now display correctly in the canvas without requiring you to reopen the file.</p></div></div></td><td><div><div><p>W-21582912</p></div></div></td></tr></tbody></table>
## February 24, 2026
Anypoint Code Builder releases these patch versions in the Anypoint Extension Pack and the Cloud
IDE.
- Extension pack version: 1.16.1
  To use this extension pack in the desktop IDE, see
  [Set up the Desktop IDE](../../anypoint-code-builder/start-acb#set-up-desktop).
- Cloud IDE version: 1.16.2
  This cloud IDE version runs the 1.16.2 extension pack.
### Fixed Issues
<table><colgroup><col> <col></colgroup><thead><tr><th>Issue Resolution</th><th>ID</th></tr></thead><tbody><tr><td><div><div><p>The bundled Mule runtime is no longer copied empty in the Web IDE.</p></div></div></td><td><div><div><p>W-21314634</p></div></div></td></tr><tr><td><div><div><p>Mule projects located outside of the Anypoint Studio workspace folder now import correctly into the Anypoint Code Builder workspace.</p></div></div></td><td><div><div><p>W-21294903</p></div></div></td></tr><tr><td><div><div><p>Fixed an issue where project deployment to CloudHub 2.0 failed because the system looked for an incorrect JAR file name after a successful package operation.</p></div></div></td><td><div><div><p>W-21304545</p></div></div></td></tr><tr><td><div><div><p>The custom metadata UI now loads correctly for projects with paths that contain spaces.</p></div></div></td><td><div><div><p>W-21308475</p></div></div></td></tr></tbody></table>
## February 17, 2026
Anypoint Code Builder releases this version in the Anypoint Extension Pack and the Cloud IDE.
- Extension pack version: 1.16.0
  To use this extension pack in the desktop IDE, see
  [Set up the Desktop IDE](../../anypoint-code-builder/start-acb#set-up-desktop).
- Cloud IDE version: 1.16.0
  This cloud IDE version runs the 1.16.0 extension pack.
### Whatâ€™s New
This release introduces these features.
- [External Library Configuration for Mule Projects](#external-libraries-mule-projects-feb17-26)
- [Custom Metadata Support](#custom-metadata-support-feb17-26)
- [AI-Powered Auto Mapping with Enhanced Error Feedback](#ai-powered-auto-mapping-feb17-26)
- [Bundled Runtimes for Instant Project Editing](#bundled-runtimes-feb17-26)
- [Workspace Validation for Mule Projects](#workspace-validation-feb17-26)
### External Library Configuration for Mule Projects
You can now add and manage external libraries for Mule projects directly from Anypoint Code Builder.
This lets you configure project-level dependencies using recommended libraries, Maven dependencies,
or local files. Configured libraries are added to the project POM and applied to all components that
require them. You can also edit or remove libraries from the same configuration interface.
### Custom Metadata Support
You can now define and assign your own custom metadata within the canvas UI to accurately visualize
and test your organizationâ€™s data structures for your integration projects. By using a dedicated tab
in the configuration panel, you can create metadata for inputs and outputs using common formats like
CSV, JSON, and XML to make sure your data transformations are accurate. For more information see
[Managing Custom Metadata](../../anypoint-code-builder/int-manage-custom-metadata).
### AI-Powered Auto Mapping with Enhanced Error Feedback
You can now better debug your transformations with comprehensive error feedback for GenAI
actionsâ€”including authorization, metadata, and request limitsâ€”ensuring a more reliable and guided
mapping experience. The **Transformation Builder** now provides categorized error guidance to help
you troubleshoot authorization issues, metadata problems, and request limit errors, making it easier
to diagnose and resolve issues when using AI-assisted transformations and mapping features.
### Bundled Runtimes for Instant Project Editing
You can now open and edit projects instantly without downloading separate Mule runtime versions.
Anypoint Code Builder now ships bundled runtimes used for editing and metadata discovery
(DataSense). You must download the exact runtime versions if running or debugging your app.
### Workspace Validation for Mule Projects
Anypoint Code Builder now validates your project structure and provides guidance when a Mule project
isnâ€™t configured correctly. When creating new projects, you can select **Create in workspace** to
organize multiple projects in a multi-root workspace. You can also import and validate existing
Anypoint Studio workspaces and use MuleSoft Vibes to switch between workspaces using natural
language. For more information, see
[Working with Workspaces](../../anypoint-code-builder/start-workspaces).
### MuleSoft MCP Server Project Updates
MuleSoft MCP Server includes tool updates. For more information, see
[MuleSoft MCP Server Release Notes](../mulesoft-mcp-server/mulesoft-mcp-server-release-notes#new-features-mcp-server-feb17-26).
### Fixed Issues
<table><colgroup><col> <col></colgroup><thead><tr><th>Issue Resolution</th><th>ID</th></tr></thead><tbody><tr><td><div><div><p>Duplicate runtime arguments from <code>run</code> and <code>debug</code> commands are removed, and arguments are now passed correctly without redundancy in the execution string.</p></div></div></td><td><div><div><p>W-20293482</p></div></div></td></tr><tr><td><div><div><p>Standalone DataWeave library projects in Anypoint Code Builder now execute correctly across all workspace configurations.</p></div></div></td><td><div><div><p>W-20334373</p></div></div></td></tr><tr><td><div><div><p>Error handling logic now works as expected and provides uniform behavior and messaging consistency across the IDE.</p></div></div></td><td><div><div><p>W-20364853</p></div></div></td></tr><tr><td><div><div><p>Project properties and connection lists now display correctly and are no longer hidden or empty.</p></div></div></td><td><div><div><p>W-20531631</p></div></div></td></tr><tr><td><div><div><p>Mule Maven plugin dependencies now resolve correctly in clean .m2 repositories without manual intervention.</p></div></div></td><td><div><div><p>W-20825706</p></div></div></td></tr><tr><td><div><div><p>Processors can now be added as expected to the beginning of existing components within the <strong>Process Record</strong> section of a <strong>Batch Job</strong> component.</p></div></div></td><td><div><div><p>W-20926265</p></div></div></td></tr><tr><td><div><div><p>Components are now placed in the correct location during drag operations on the UI canvas.</p></div></div></td><td><div><div><p>W-20926514</p></div></div></td></tr><tr><td><div><div><p>The <strong>Transform Message</strong> component content is now visible without the requirement of CDATA tags.</p></div></div></td><td><div><div><p>W-21146025</p></div></div></td></tr><tr><td><div><div><p>Database connection configurations in the global configuration page now update the XML source correctly.</p></div></div></td><td><div><div><p>W-21147450</p></div></div></td></tr><tr><td><div><div><p>Socket timeout exceptions no longer occur when loading connector operators.</p></div></div></td><td><div><div><p>W-20201721</p></div></div></td></tr></tbody></table>
## February 6, 2026
Anypoint Code Builder releases this version in the Anypoint Extension Pack and the Cloud IDE.
- Extension pack version: 1.15.0
  To use this extension pack in the desktop IDE, see
  [Set up the Desktop IDE](../../anypoint-code-builder/start-acb#set-up-desktop).
- Cloud IDE version: 1.15.0
  This cloud IDE version runs the 1.15.0 extension pack.
### Whatâ€™s New
This release introduces these features.
### Support for Mule Runtime 4.11.0
Anypoint Code Builder now supports Mule runtime 4.11.0 for creating and managing Mule projects.
Create new projects with Mule runtime 4.11.0 or update existing projects to use this runtime version
in project properties.
### Agent Network Project Updates
Agent networks now support these authentication types:
- OAuth 2.0 OBO Credential Injection using OAuth 2.0 Token Exchange or Microsoft Entra ID
  On-Behalf-Of protocols
- In-Task Authorization Code
For more information about these types, see the
[Agent Network YAML File Reference](../../anypoint-code-builder/af-project-files#authentication-types).
### MuleSoft MCP Server Project Updates
MuleSoft MCP Server includes tool updates. For more information, see
[MuleSoft MCP Server Release Notes](../mulesoft-mcp-server/mulesoft-mcp-server-release-notes#new-features-mcp-server-feb6-26).
### Scaffold and Implement APIs with Vibes
MuleSoft Vibes can now scaffold and implement API specifications on your local machine or from
Anypoint Exchange. This ensures accurate project structures and a seamless transition from
scaffolding to adding application logic, reducing manual configuration and preventing project
errors.
### Fixed Issues
<table><colgroup><col> <col></colgroup><thead><tr><th>Issue Resolution</th><th>ID</th></tr></thead><tbody><tr><td><div><div><p>The <code>command 'mule-dx-mule-dev.runMuleProject'</code> error no longer occurs when selecting <strong>Run Mule Project</strong> in the <strong>Mule</strong> option.</p></div></div></td><td><div><div><p>W-20978630</p></div></div></td></tr><tr><td><div><div><p>You can now edit nested connections from different XML files as expected.</p></div></div></td><td><div><div><p>W-20898437</p></div></div></td></tr><tr><td><div><div><p>The Exchange search filter is no longer breaking search results.</p></div></div></td><td><div><div><p>W-21018002</p></div></div></td></tr></tbody></table>
## January 15, 2026
Anypoint Code Builder releases this patch version in the Anypoint Extension Pack and the Cloud IDE.
- Extension pack version: 1.14.1
  To use this extension pack in the desktop IDE, see
  [Set up the Desktop IDE](../../anypoint-code-builder/start-acb#set-up-desktop).
- Cloud IDE version: 1.14.1
  This cloud IDE version runs the 1.14.1 extension pack.
### Whatâ€™s New
This release introduces these features.
### DataWeave Mapping Enhancements
- **Advanced nested array mapping**: **DataWeave Transform** now supports dragging fields within
  nested objects and arrays more intuitively. When mapping fields into an existing `map` function,
  the UI automatically resolves the correct scope and variables to generate accurate DataWeave
  scripts.
- **Automated hierarchical array mapping**: **DataWeave Transform** now intelligently handles
  mapping between different array levels. When dragging a top-level source array to a nested target
  array, the tool automatically generates the required parent-to-child wrapping and map functions to
  maintain the correct output structure.
- **Intelligent scalar-to-object refactoring**: **DataWeave Transform** now automatically handles
  the transition from scalar assignments to nested object structures. When you map nested fields
  within an object node, Anypoint Code Builder refactors the script to ensure a valid hierarchy
  without requiring manual code cleanup.
### Canvas Loading Status Indicator
A loading status indicator now shows while the canvas initializes. This enhancement provides more
visible and integrated feedback during project loading and synchronization tasks, improving the
overall responsiveness of the design experience.
### Optimized Canvas Connectors
The design of flow edges and connectors is improved to increase visual density. This update allows
for a more compact representation of integration flows, enabling users to view more content and
steps within the canvas.
#### Agent Network Project Creation
You can now create Agent Network projects directly from the project creation flow. The project
creation interface includes Agent Network configurations for setting up advanced project
environments within the Anypoint Code Builder workspace.
#### Refined API Specification Selection
The project creation form is now clearer and more intuitive when starting new Mule projects based on
existing API definitions.
#### Centralized Dependency Error Reporting
The dependency-related errors are now shown in the **PROBLEMS** tab so that you can identify and
resolve Maven resolution or library conflicts more efficiently without searching through background
logs.
#### MuleSoft MCP Server Project Updates
MuleSoft MCP Server includes three new tools:
- `implement_api_spec`
- `generate_munit_test`
- `modify_munit_test`
For more information about these tools, see
[MuleSoft MCP Server Release Notes](../mulesoft-mcp-server/mulesoft-mcp-server-release-notes#new-features-mcp-server-jan15-26).
#### Agent Network Project Updates
- Agent network now supports Gemini models. Specify these parameters in the LLM section of the
  `agent-network.yml` file.
  - `thinkingBudget`: Sets a token budget for the reasoning phase. (Applies only to Gemini 2.5
    series.)
  - `thinkingLevel`: Controls the depth of the reasoning process. (Applies only to Gemini 3 series.)
  - `temperature`: Controls randomness.
  - `topP`: Nucleus sampling parameter.
  - `responseLogprobs`: Whether to return log probabilities.
  - `maxOutputTokens`: Maximum number of tokens that can be generated in the response.
    For more information about these parameters, see the
    [Agent Network YAML File Reference](../../anypoint-code-builder/af-project-files#agent-network-yaml).
- The agent broker is now aware of which LLM model you select and uses the appropriate API. For
  example, if youâ€™re using an OpenAI model, the broker now uses function calling rather than sending
  the system prompt, broker instructions, tools, and history as one prompt.
### Cleaner Project Context Menus
Project context menus are now consistent across root and multi-root workspaces for supported Mule
project types. Anypoint Code Builder actions are shown only when they apply to the selected project
or folder, and related actions are grouped more clearly to improve discoverability.
### Cleaner Command Palette Actions
The Command Palette now shows a cleaner and more consistent set of Anypoint Code Builder commands
across single-root and multi-root workspaces. Commands are clearly named, consistently prefixed with
MuleSoft, and organized using descriptive categories such as API, Mule, and Agent Network.  
Only actions that initiate complete workflows appear in the Command Palette. Context-specific
commands are available only when the required project context is active.
### Fixed Issues
<table><colgroup><col> <col></colgroup><thead><tr><th>Issue Resolution</th><th>ID</th></tr></thead><tbody><tr><td><div><div><p>Fixed an issue where switching between factory configurations in a JMS publish component caused XML corruption.</p></div></div></td><td><div><div><p>W-20159060</p></div></div></td></tr><tr><td><div><div><p>Fixed an issue in the Java module <strong>New</strong> operation where the error icon remained visible after the <strong>Constructor</strong> value is successfully configured. The UI now correctly clears the error state after valid configuration data is provided.</p></div></div></td><td><div><div><p>W-20117914</p></div></div></td></tr><tr><td><div><div><p>Fixed an issue in <strong>DataWeave Transform</strong> where mapping fields from a nested source to a nested target sometimes resulted in incorrect script nesting. The UI now accurately maintains the nested structure and context when multiple fields are mapped to the same target path.</p></div></div></td><td><div><div><p>W-20208318</p></div></div></td></tr><tr><td><div><div><p>Fixed an issue where creating a new API project inside a nested workspace folder prevented the project from opening or being added to the current workspace. Projects now open correctly regardless of their folder depth within the workspace.</p></div></div></td><td><div><div><p>W-20212604</p></div></div></td></tr><tr><td><div><div><p>Drag actions in <strong>Transform Builder</strong> no longer occasionally result in a UI error state.</p></div></div></td><td><div><div><p>W-20222649</p></div></div></td></tr><tr><td><div><div><p>Anypoint Code Builder now correctly shows an error message when you open a project located outside the root folder or within the current workspace.</p></div></div></td><td><div><div><p>W-20249789</p></div></div></td></tr><tr><td><div><div><p>The canvas now accurately identifies and displays synthetic routes within connectors.</p></div></div></td><td><div><div><p>W-20332947</p></div></div></td></tr><tr><td><div><div><p>Anypoint Code Builder now displays an error related to project properties when your project fails to initialize correctly.</p></div></div></td><td><div><div><p>W-20481957</p></div></div></td></tr><tr><td><div><div><p>The editor now correctly uses UTF-8 encoding across all platforms to ensure that consistent data is displayed in the <strong>Transformation Builder</strong> input and output windows.</p></div></div></td><td><div><div><p>W-20494670</p></div></div></td></tr><tr><td><div><div><p>Fixed an issue with MCP tools that took no input arguments.</p></div></div></td><td><div><div><p>W-20474172</p></div></div></td></tr><tr><td><div><div><p>The DataWeave editor no longer becomes slow or unresponsive when working with large transformations, including freezes triggered by auto-save.</p></div></div></td><td><div><div><p>W-19966256</p></div></div></td></tr><tr><td><div><div><p>DataWeave scripts no longer lose their formatting or collapse into a single line when you edit connection configurations or make unrelated project changes.</p></div></div></td><td><div><div><p>W-20082580</p></div></div></td></tr><tr><td><div><div><p>The canvas no longer gets stuck in an infinite loading state.</p></div></div></td><td><div><div><p>W-20214677</p></div></div></td></tr><tr><td><div><div><p>The HTTP Request component no longer reverts header or body values back to <code>payload</code> when editing them in the canvas UI.</p></div></div></td><td><div><div><p>W-20581927</p></div></div></td></tr><tr><td><div><div><p>DataWeave mappings no longer drop type casting when concatenating expressions.</p></div></div></td><td><div><div><p>W-20582971</p></div></div></td></tr></tbody></table>
## December 18, 2025
Anypoint Code Builder releases this patch version in the Anypoint Extension Pack and the Cloud IDE.
- Extension pack version: 1.13.1
  To use this extension pack in the desktop IDE, see
  [Set up the Desktop IDE](../../anypoint-code-builder/start-acb#set-up-desktop).
- Cloud IDE version: 1.13.1
  This cloud IDE version runs the 1.13.1 extension pack.
### Fixed Issues
<table><colgroup><col> <col></colgroup><thead><tr><th>Issue Resolution</th><th>ID</th></tr></thead><tbody><tr><td><div><div><p>CLI for Agent Fabric Plugin is updated to the latest version to address reported security vulnerabilities.</p></div></div></td><td><div><div><p>W-20573569</p></div></div></td></tr></tbody></table>
## December 12, 2025
Anypoint Code Builder releases this version in the Cloud IDE.
- Cloud IDE version: 1.13.0
  This cloud IDE version runs the 1.13.0 extension pack.
For a complete list of the features and fixed issues included in this release, see the
[December 11, 2025](#Dec11-2025), Anypoint Code Builder release notes.
## December 11, 2025
Anypoint Code Builder releases new features in the Anypoint Extension Pack.
- Extension pack version: 1.13.0
  To use this extension pack in the desktop IDE, see
  [Set up the Desktop IDE](../../anypoint-code-builder/start-acb#set-up-desktop).
### Whatâ€™s New
This release introduces these features.
#### New Enhancements to the DataWeave Transform Component
This update includes several improvements to UI stability and the generative AI experience, such as
optimized behavior in the **Transform Message** component UI and more responsive error handling for
AI-powered actions.
#### Stability Enhancements
##### Improved MCP Config Reference Editing
The Inference Connector configuration panel now reliably allows the added client to be edited when
configuring an MCP config reference field.
##### Stabilized Audience Settings for MCP Listener
Configuration of the audience field within the responses group of the MCP Tool Listener is now
reliable and consistent, ensuring that the field appears correctly, even when imported from an XML
file.
#### Agent Network Project Updates
- The
  [Agent Network YAML File Reference](../../anypoint-code-builder/af-project-files#agent-network-yaml)
  now includes all available parameters for each section.
- The `agent-network.yml` file now exposes new parameters from OpenAI.
  Specify these parameters in the `llm` section settings for OpenAI.
  - `reasoningEffort`: Constrains reasoning effort for reasoning models.
  - `temperature`: Controls randomness in the output.
  - `topP`: Nucleus sampling parameter.
  - `topLogprobs`: Number of most likely tokens to return at each position.
  - `maxOutputTokens`: Maximum number of tokens to generate.
  For more information about these parameters, see the
  [Agent Network YAML File Reference](../../anypoint-code-builder/af-project-files#agent-network-yaml)
  and [OpenAI Platform API Reference](https://platform.openai.com/docs/api-reference/introduction).
- These agent network dependencies are updated:
  - OpenAI SDK version is updated to 4.8.0.
  - Mule HTTP Connector version is updated to 1.11.0.
  - A2A Connector version is updated to 0.4.0-BETA.
  - A2A SDK version is updated to 0.3.3-final.
  - MCP Connector version is updated to 1.3.0.
  - Caffeine version is updated to 3.2.3.
  - JaCoCo version is updated to 0.8.11.
  - `aspectj` version is updated to 1.9.22.1.
  - Common text version is updated to 1.14.0.
#### Git Installation No Longer Required
- You no longer need to install git as part of the Anypoint Code Builder installation process.
### Fixed Issues
<table><colgroup><col> <col></colgroup><thead><tr><th>Issue Resolution</th><th>ID</th></tr></thead><tbody><tr><td><div><div><p>The <strong>Autodiscovery</strong> element no longer appears in the <strong>Add Component</strong> panel.</p></div></div></td><td><div><div><p>W-16891052</p></div></div></td></tr><tr><td><div><div><p>Users now receive a notification after successful deployment to CloudHub as expected.</p></div></div></td><td><div><div><p>W-18079627</p></div></div></td></tr><tr><td><div><div><p>DataWeave output metadata is now correct in component fields.</p></div></div></td><td><div><div><p>W-18553945</p></div></div></td></tr><tr><td><div><div><p>The canvas now correctly reflects unsaved changes.</p></div></div></td><td><div><div><p>W-18657386</p></div></div></td></tr><tr><td><div><div><p>CloudHub redeployment no longer fails intermittently.</p></div></div></td><td><div><div><p>W-18727013</p></div></div></td></tr><tr><td><div><div><p>The <strong>Transformation Builder</strong> window for DataWeave no longer shows an error in the input sample on Windows systems.</p></div></div></td><td><div><div><p>W-18911593</p></div></div></td></tr><tr><td><div><div><p>The flow configuration UI attribute for enabling default events is now correctly written in the XML file.</p></div></div></td><td><div><div><p>W-19117758</p></div></div></td></tr><tr><td><div><div><p>The configuration UI no longer shows a default value for data types when no default value exists in the metadata.</p></div></div></td><td><div><div><p>W-19175333</p></div></div></td></tr><tr><td><div><div><p>Errors updating XML no longer occur on the canvas when updating auto closed tags.</p></div></div></td><td><div><div><p>W-19211738</p></div></div></td></tr><tr><td><div><div><p>Editing metadata in the <strong>Transform Message</strong> component now works correctly if the source is a DataWeave file.</p></div></div></td><td><div><div><p>W-19273485</p></div></div></td></tr><tr><td><div><div><p>The <code>M2_REPO</code> variable is now used to populate the repository at startup.</p></div></div></td><td><div><div><p>W-19476167</p></div></div></td></tr><tr><td><div><div><p>The debugger now correctly pauses in the main flow and sub-flow after using <strong>Step into</strong>.</p></div></div></td><td><div><div><p>W-19547488</p></div></div></td></tr><tr><td><div><div><p>Toggling between <strong>INLINE</strong> or <strong>Bean</strong> mode to <strong>None</strong> now works correctly in the configuration panel.</p></div></div></td><td><div><div><p>W-19623905</p></div></div></td></tr><tr><td><div><div><p>You can now input text for <code>Operations</code> in MuleSoft Vectors Connector as expected.</p></div></div></td><td><div><div><p>W-19637694</p></div></div></td></tr><tr><td><div><div><p>Validation now shows errors as expected for missing fields in the <strong>Database</strong> component.</p></div></div></td><td><div><div><p>W-19679369</p></div></div></td></tr><tr><td><div><div><p>The debugger now shows the breakpoint information as expected if <strong>Step into</strong> is used on a flow reference pointing to a flow in the configuration of a sub-folder.</p></div></div></td><td><div><div><p>W-19679780</p></div></div></td></tr><tr><td><div><div><p>Unauthorized errors no longer occur when the token expires.</p></div></div></td><td><div><div><p>W-19971283</p></div></div></td></tr><tr><td><div><div><p><strong>A2A Connector</strong> configurations now appear in version 0.4.0-BETA as expected.</p></div></div></td><td><div><div><p>W-20004568</p></div></div></td></tr><tr><td><div><div><p>If deployment to CloudHub 2.0 fails, the user now gets an error notification.</p></div></div></td><td><div><div><p>W-20030018</p></div></div></td></tr><tr><td><div><div><p><strong>Transformation Builder</strong> no longer closes unexpectedly on Windows systems when pressing Ctrl+Backspace.</p></div></div></td><td><div><div><p>W-20031151</p></div></div></td></tr><tr><td><div><div><p>Error messages no longer repeatedly pop up for the same error during dependency resolution.</p></div></div></td><td><div><div><p>W-20036183</p></div></div></td></tr><tr><td><div><div><p>A path traversal vulnerability in MuleSoft MCP Server tools is now fixed.</p></div></div></td><td><div><div><p>W-20039005</p></div></div></td></tr><tr><td><div><div><p>Intermittent corruption of the JDK installation no longer occurs.</p></div></div></td><td><div><div><p>W-20052935</p></div></div></td></tr><tr><td><div><div><p>A server-side template injection vulnerability in MCP flow generation tools is now fixed.</p></div></div></td><td><div><div><p>W-20053148</p></div></div></td></tr><tr><td><div><div><p>The Dev Agent web fetch tool timeout is increased from 10 to 30 seconds to support slow-loading URLs.</p></div></div></td><td><div><div><p>W-20084547</p></div></div></td></tr><tr><td><div><div><p><strong>Expression Builder</strong> no longer breaks or displays incorrectly if the DataWeave transformation contains a long script.</p></div></div></td><td><div><div><p>W-20086693</p></div></div></td></tr><tr><td><div><div><p>The configuration UI in the Java module now successfully loads the <strong>Method</strong> field values.</p></div></div></td><td><div><div><p>W-20112957</p></div></div></td></tr><tr><td><div><div><p>Misleading stack traces from the Design Service logs that appeared when loading custom connectors are removed.</p></div></div></td><td><div><div><p>W-20131222</p></div></div></td></tr><tr><td><div><div><p>The <strong>HTTP Listener</strong> component now secures the password during TLS setup as expected.</p></div></div></td><td><div><div><p>W-20135822</p></div></div></td></tr><tr><td><div><div><p>The <strong>Anypoint Code Builder Integration Extension</strong> now uses the correct version of <code>org.mule.weave</code> dependencies instead of using the 2.6.1. version.</p></div></div></td><td><div><div><p>W-20159499</p></div></div></td></tr><tr><td><div><div><p>The <strong>Anypoint Code Builder Platform Extension</strong> version 5.9.7 no longer breaks in Windows systems.</p></div></div></td><td><div><div><p>W-20192341</p></div></div></td></tr><tr><td><div><div><p>The <strong>Expression Builder</strong> gear icon is now clickable as expected.</p></div></div></td><td><div><div><p>W-20203410</p></div></div></td></tr><tr><td><div><div><p>The <strong>Audience</strong> field in the MCP tool listener configuration no longer intermittently fails to display.</p></div></div></td><td><div><div><p>W-19127724</p></div></div></td></tr><tr><td><div><div><p>The MCP configuration reference field in the <strong>Inference Connector</strong> can now be edited as expected.</p></div></div></td><td><div><div><p>W-20018055</p></div></div></td></tr><tr><td><div><div><p>The internal platform jar socket is now restricted to listening on localhost only, mitigating a potential Remote Code Execution (RCE) vulnerability.</p></div></div></td><td><div><div><p>W-20194553</p></div></div></td></tr><tr><td><div><div><p>Object group element attributes now update correctly in the UI, and inconsistent behavior related to empty element deletion in the <strong>Transform script</strong> field no longer occurs.</p></div></div></td><td><div><div><p>W-20244840</p></div></div></td></tr><tr><td><div><div><p>Custom metadata now shows as expected in the <strong>Output</strong> column of the mapping window for transform components.</p></div></div></td><td><div><div><p>W-20062856</p></div></div></td></tr><tr><td><div><div><p>SAP Connector test connection no longer fails.</p></div></div></td><td><div><div><p>W-19124681</p></div></div></td></tr><tr><td><div><div><p>The scaffolding process no longer fails when the project ID used for scaffolding doesnâ€™t match the project ID that was created.</p></div></div></td><td><div><div><p>W-20201660</p></div></div></td></tr><tr><td><div><div><p>Projects that are inherited from a Parent POM that use Mavenâ€™s CI-friendly version properties no longer incorrectly report that the parent POM canâ€™t be found.</p></div></div></td><td><div><div><p>W-20272484</p></div></div></td></tr><tr><td><div><div><p>The <strong>Connectors</strong> tab in <strong>Project Properties</strong> no longer fails to load when an incompatible connector version causes the Mule framework introspection to fail.</p></div></div></td><td><div><div><p>W-19284941</p></div></div></td></tr><tr><td><div><div><p>The code editor of a component is now resizable and shows line numbers.</p></div></div></td><td><div><div><p>W-20060203</p></div></div></td></tr><tr><td><div><div><p>The drag and drop action for simple <strong>Transform</strong> components no longer breaks the canvas view and flow XML on Windows systems.</p></div></div></td><td><div><div><p>W-20439430</p></div></div></td></tr><tr><td><div><div><p>The MuleSoft Dev Agent stream no longer intermittently throws an incorrect <code>ValidationException</code> error embedded within stream chunks.</p></div></div></td><td><div><div><p>W-20068043</p></div></div></td></tr><tr><td><div><div><p>MuleSoft Dev Agent no longer fails due to streaming errors or server timeouts during operations.</p></div></div></td><td><div><div><p>W-20023190</p></div></div></td></tr><tr><td><div><div><p>MuleSoft Dev Agent no longer experiences a five-second delay before making the first API call after being opened.</p></div></div></td><td><div><div><p>W-20077965</p></div></div></td></tr><tr><td><div><div><p>The <strong>Map with AI</strong> feature in <strong>Transformation Builder</strong> now correctly displays user access errors when they occur.</p></div></div></td><td><div><div><p>W-20276613</p></div></div></td></tr><tr><td><div><div><p>The <strong>Edit Sample Data File</strong> icon is no longer disabled in the <strong>Map with AI</strong> feature in <strong>Transformation Builder</strong>. Also, the default call when opening the Transform UI is removed, and the UI now shows a message instead of a spinning icon when the GenAI API call fails.</p></div></div></td><td><div><div><p>W-20276613</p></div></div></td></tr><tr><td><div><div><p>Anypoint Code Builder no longer fails to render all configuration parameters, such as the HTTP Requestor parameter, for the RosettaNet Connector in the Configuration UI.</p></div></div></td><td><div><div><p>W-20190237</p></div></div></td></tr><tr><td><div><div><p>Anypoint Code Builder no longer displays an incorrect compatibility error message when a project dependency is missing in the current Exchange environment.</p></div></div></td><td><div><div><p>W-19750194</p></div></div></td></tr><tr><td><div><div><p>The Import global element now recognizes flows defined within the imported plugin as expected.</p></div></div></td><td><div><div><p>W-19986168</p></div></div></td></tr><tr><td><div><div><p>The Visual Designer no longer fails to show and recognize shared configuration components when theyâ€™re inherited from a Parent POM.</p></div></div></td><td><div><div><p>W-20178132</p></div></div></td></tr><tr><td><div><div><p>Keyboard shortcuts, such as Command+C and Command+V, now work as expected when selecting and editing text in the DataWeave Editor.</p></div></div></td><td><div><div><p>W-20162326</p></div></div></td></tr></tbody></table>
This release addresses the following issue with agent network projects:
<table><colgroup><col> <col></colgroup><thead><tr><th>Issue Resolution</th><th>ID</th></tr></thead><tbody><tr><td><div><div><p>The distributed trace now correctly includes LLM calls for an agent broker.</p></div></div></td><td><div><div><p>W-19825674</p></div></div></td></tr></tbody></table>
## November 12, 2025
Anypoint Code Builder releases this patch version in the Anypoint Extension Pack and the Cloud IDE.
- Extension pack version: 1.12.2
  To use this extension pack in the desktop IDE, see
  [Set up the Desktop IDE](../../anypoint-code-builder/start-acb#set-up-desktop).
- Cloud IDE version: 1.12.2
  This cloud IDE version runs the 1.12.2 extension pack.
### Fixed Issues
<table><colgroup><col> <col></colgroup><thead><tr><th>Issue Resolution</th><th>ID</th></tr></thead><tbody><tr><td><div><div><p>Anypoint Code Builder Platform Extension no longer fails on Windows systems.</p></div></div></td><td><div><div><p>W-20192341</p></div></div></td></tr></tbody></table>
## November 10, 2025
Anypoint Code Builder releases this patch version in the Anypoint Extension Pack and the Cloud IDE.
- Extension pack version: 1.12.1
  To use this extension pack in the desktop IDE, see
  [Set up the Desktop IDE](../../anypoint-code-builder/start-acb#set-up-desktop).
- Cloud IDE version: 1.12.1
  This cloud IDE version runs the 1.12.1 extension pack.
### Fixed Issues
<table><colgroup><col> <col></colgroup><thead><tr><th>Issue Resolution</th><th>ID</th></tr></thead><tbody><tr><td><div><div><p>Some dependencies are updated to address reported vulnerabilities.</p></div></div></td><td><div><div><p>W-20115973</p></div></div></td></tr></tbody></table>
## November 4, 2025
Anypoint Code Builder releases new features in the Anypoint Extension Pack.
- Extension pack version: 1.12.0
  To use this extension pack in the desktop IDE, see
  [Set up the Desktop IDE](../../anypoint-code-builder/start-acb#set-up-desktop).
- Cloud IDE version: 1.12.0
  This cloud IDE version runs the 1.12.0 extension pack.
For extension versions, see the
[Change Log](https://marketplace.visualstudio.com/items/salesforce.mule-dx-extension-pack/changelog)
in the VS Code Marketplace.
For more information, see [Known Issues](#known-issues) and [Compatibility](#compatibility).
### Whatâ€™s New
This release introduces these features:
- [Support for Maven Multi-Module Projects and Parent POM Files](#multi-module)
- [Map with AI Now Detects and Applies Existing Metadata MIME Types](#dw-metadata-mime-types)
- [Agent Network Project Updates](#agent-networks-nov-25)
- [Support for Connection Configurations Defined in Dependencies](#dependency-connection-configs)
#### Support for Maven Multi-Module Projects and Parent POM Files
Anypoint Code Builder now supports Maven multi-module projects and parent POM file functionality.
Define properties, dependencies, and versions once and share them across multiple projects,
guaranteeing consistency and eliminating version drift. For more information, see
[Importing Projects into the IDE](../../anypoint-code-builder/int-import-mule-project).
#### Map with AI Now Detects and Applies Existing Metadata MIME Types
The **Map with AI** tool is now enhanced to automatically detect and apply the existing metadata
MIME types (such as `application/json`, `application/xml`, and `application/java`) defined in your
projectâ€™s flow. When generating a DataWeave script, **Map with AI** now reads the input and output
formats from the surrounding connectors and correctly applies those types to the generated scriptâ€™s
directives.
#### Agent Network Project Updates
The agent broker now dynamically adapts when any downstream AI asset changes its contract because
the MCP and A2A metadata automatically refreshes every hour.
#### Support for Connection Configurations Defined in Dependencies
Anypoint Code Builder now detects and loads connection configurations that are defined in external
project dependencies. The tool scans all import statements in your Mule flows, locates the related
files inside dependency JARs, and extracts the connection configurations they define. These
configurations appear in both the XML view and the canvas view.
### Fixed Issues
<table><colgroup><col> <col></colgroup><thead><tr><th>Issue Resolution</th><th>ID</th></tr></thead><tbody><tr><td><div><div><p>Anypoint Code Builder now correctly resolves Maven settings and configurations against the <strong>settings.xml</strong> file and no longer creates a temporary <strong>acb_settings.xml</strong> file.</p></div></div></td><td><div><div><p>W-19128433</p></div></div></td></tr><tr><td><div><div><p>The canvas now refreshes automatically after updating the runtime version in project properties.</p></div></div></td><td><div><div><p>W-19285759</p></div></div></td></tr><tr><td><div><div><p>Pasting a component after a disabled component no longer breaks the canvas UI or prevents the flow from rendering.</p></div></div></td><td><div><div><p>W-19719169</p></div></div></td></tr><tr><td><div><div><p>The <strong>Error Handler</strong> configuration now displays all applicable error types based on the components used in the flow as expected.</p></div></div></td><td><div><div><p>W-19788055</p></div></div></td></tr><tr><td><div><div><p>The Agent Fabric flag is now correctly enabled when switching from the Control Plane to EU Cloud in the desktop IDE.</p></div></div></td><td><div><div><p>W-19810833</p></div></div></td></tr><tr><td><div><div><p>The context menu no longer appears for nodes in the read-only Agent Fabric Authoring canvas.</p></div></div></td><td><div><div><p>W-19840137</p></div></div></td></tr><tr><td><div><div><p>The auto approval for tool execution in the Dev Agent chat window now works as expected.</p></div></div></td><td><div><div><p>W-19842516</p></div></div></td></tr><tr><td><div><div><p>Java processes no longer remain active after closing Anypoint Code Builder.</p></div></div></td><td><div><div><p>W-19849557</p></div></div></td></tr><tr><td><div><div><p>The local .m2 repository is now populated correctly at startup.</p></div></div></td><td><div><div><p>W-19860834</p></div></div></td></tr><tr><td><div><div><p>Dev Agent no longer becomes unresponsive.</p></div></div></td><td><div><div><p>W-20051611</p></div></div></td></tr><tr><td><div><div><p>Validation decorators now appear correctly in the canvas after adding a new connector or updating dependencies in the project <code>pom.xml</code> file.</p></div></div></td><td><div><div><p>W-18741926</p></div></div></td></tr><tr><td><div><div><p>The Java debug server that started automatically when running Mule apps is now disabled by default to prevent unauthorized access.</p></div></div></td><td><div><div><p>W-18968450</p></div></div></td></tr><tr><td><div><div><p>Anypoint Code Builder now loads the Maven <strong>settings.xml</strong> file at startup to correctly generate the <strong>acb_settings.xml</strong> file with the userâ€™s configuration.</p></div></div></td><td><div><div><p>W-19128433</p></div></div></td></tr><tr><td><div><div><p>MUnit configurations defined in the parent <code>pom.xml</code> file are now correctly inherited by child projects.</p></div></div></td><td><div><div><p>W-19284704</p></div></div></td></tr><tr><td><div><div><p>The <code>minMuleVersion</code> value in the <code>mule-artifact.json</code> file is no longer overwritten by Anypoint Code Builder. Runtime feature toggles are now decoupled from this property.</p></div></div></td><td><div><div><p>W-19374653</p></div></div></td></tr><tr><td><div><div><p>Anypoint Code Builder no longer becomes unresponsive or stuck on the loading screen when adding components to a flow in customer projects.</p></div></div></td><td><div><div><p>W-19525162</p></div></div></td></tr><tr><td><div><div><p>The canvas now opens the correct configuration panel when selecting components.</p></div></div></td><td><div><div><p>W-19687980</p></div></div></td></tr><tr><td><div><div><p>Disabled components can now be copied and pasted successfully without triggering errors during node duplication.</p></div></div></td><td><div><div><p>W-19760175</p></div></div></td></tr><tr><td><div><div><p>DataWeave actions now appear in the correct position within the context menu.</p></div></div></td><td><div><div><p>W-19883653</p></div></div></td></tr><tr><td><div><div><p>Anypoint Code Builder now defaults to the US production environment when the <code>ANYPOINT_ENV</code> variable is set to an unrecognized value.</p></div></div></td><td><div><div><p>W-20003674</p></div></div></td></tr><tr><td><div><div><p>Exchange search now correctly returns the <strong>Inference</strong> connector when using Mule runtime 4.9.10 or later.</p></div></div></td><td><div><div><p>W-20054759</p></div></div></td></tr><tr><td><div><div><p>The correct message is now displayed when attribute and variable samples are empty in the configuration panel.</p></div></div></td><td><div><div><p>W-20057018</p></div></div></td></tr><tr><td><div><div><p>Error messages related to connector dependencies now include a clickable <code>pom.xml</code> link.</p></div></div></td><td><div><div><p>W-15813306</p></div></div></td></tr></tbody></table>
This release addresses the following issues with agent network projects:
<table><colgroup><col> <col></colgroup><thead><tr><th>Issue Resolution</th><th>ID</th></tr></thead><tbody><tr><td><div><div><p>Agent brokers now maintain conversation context during multi-turn interactions.</p></div></div></td><td><div><div><p>W-19825674</p></div></div></td></tr><tr><td><div><div><p>Agent brokers now return properly formatted text content in input-required responses instead of empty strings.</p></div></div></td><td><div><div><p>W-19880599</p></div></div></td></tr></tbody></table>
## October 24, 2025
Anypoint Code Builder releases new features in the Anypoint Extension Pack.
- Extension pack version: 1.11.6
  To use this extension pack in the desktop IDE, see
  [Set up the Desktop IDE](../../anypoint-code-builder/start-acb#set-up-desktop).
- Cloud IDE version: 1.11.5
  This cloud IDE version runs the 1.11.6 extension pack.
For extension versions, see
[Change Log](https://marketplace.visualstudio.com/items/salesforce.mule-dx-extension-pack/changelog)
in the VS Code Marketplace.
For more information, see [Known Issues](#known-issues) and [Compatibility](#compatibility).
### Fixed Issues
<table><colgroup><col> <col></colgroup><thead><tr><th>Issue Resolution</th><th>ID</th></tr></thead><tbody><tr><td><div><div><p>Auto-approval for safe commands is now disabled in MuleSoft Dev Agent. Command execution now always requires explicit user approval, unless <strong>Execute all commands</strong> is enabled, preventing potential prompt injection exploits.</p></div></div></td><td><div><div><p>W-19853225</p></div></div></td></tr><tr><td><div><div><p>Editing VS Code configuration files (<code>.vscode/ and *.code-workspace</code>) now requires explicit approval.</p></div></div></td><td><div><div><p>W-19853255</p></div></div></td></tr><tr><td><div><div><p>Editing the MCP configuration file (<code>a4d_mcp_settings.json</code>) now requires explicit approval in MuleSoft Dev Agent.</p></div></div></td><td><div><div><p>W-19853247</p></div></div></td></tr></tbody></table>
## October 14, 2025
Anypoint Code Builder releases new features in the Anypoint Extension Pack.
- Extension pack version: 1.11.5
  To use this extension pack in the desktop IDE, see
  [Set up the Desktop IDE](../../anypoint-code-builder/start-acb#set-up-desktop).
For extension versions, see the
[Change Log](https://marketplace.visualstudio.com/items/salesforce.mule-dx-extension-pack/changelog)
in the VS Code Marketplace.
For more information, see [Known Issues](#known-issues) and [Compatibility](#compatibility).
### Fixed Issues
<table><colgroup><col> <col></colgroup><thead><tr><th>Issue Resolution</th><th>ID</th></tr></thead><tbody><tr><td><div><div><p>Core capabilities in the Design Service, including <strong>Test Connection</strong> and <strong>Run and Debug</strong>, function as expected on slow machines.</p></div></div></td><td><div><div><p>W-19864902</p></div></div></td></tr><tr><td><div><div><p>Data streaming issues are fixed now and responses from Model API no longer fail.</p></div></div></td><td><div><div><p>W-19845839</p></div></div></td></tr></tbody></table>
## October 8, 2025
Anypoint Code Builder releases new features in the Anypoint Extension Pack and the Cloud IDE.
- Extension pack version: 1.11.4
  To use this extension pack in the desktop IDE, see
  [Set up the Desktop IDE](../../anypoint-code-builder/start-acb#set-up-desktop).
- Cloud IDE version: 1.11.4
  This cloud IDE version runs the 1.11.4 extension pack.
For extension versions, see the
[Change Log](https://marketplace.visualstudio.com/items/salesforce.mule-dx-extension-pack/changelog)
in the VS Code Marketplace.
For more information, see [Known Issues](#known-issues) and [Compatibility](#compatibility).
### Whatâ€™s New
This version contains internal bug fixes and performance improvements.
## October 3, 2025
Anypoint Code Builder releases new features in the Anypoint Extension Pack and the Cloud IDE.
- Extension pack version: 1.11.1
  To use this extension pack in the desktop IDE, see
  [Set up the Desktop IDE](../../anypoint-code-builder/start-acb#set-up-desktop).
- Cloud IDE version: 1.11.0
  This cloud IDE version runs the 1.11.0 extension pack.
For extension versions, see
[Change Log](https://marketplace.visualstudio.com/items/salesforce.mule-dx-extension-pack/changelog)
in the VS Code Marketplace.
For more information, see [Known Issues](#known-issues) and [Compatibility](#compatibility).
### Whatâ€™s New
This release introduces these features:
- [Agent Fabric](#agent-fabric)
- [MuleSoft Dev Agent](#dev-agent)
- [Batch Processing Support](#batch-process-support)
- [Duplicate Flows in Canvas](#duplicate-flows)
- [Copy and Paste Components in Canvas](#copy-paste-components)
- [Stability and Usability enhancements](#stability-usability-enhancements)
- [Mule Runtime Support](#mule-runtime-4-10-0-support)
- [Einstein Features and Free Trial Orgs](#einstein-and-free-trials)
- [More Agentic Integration Development with the Embedded MuleSoft Model Context Protocol (MCP) Server](#mcp-server)
#### Agent Fabric
Use Anypoint Code Builder to create, publish, and deploy agent networks as part of the Agent Fabric
solution. Agent Fabric is a unified solution for governing and monitoring AI agents built anywhere,
making it possible to build a collaborative digital workforce across any system or app. For more
information, see
[Building Agent Networks for Agent Fabric](../../anypoint-code-builder/af-agent-networks).
#### MuleSoft Dev Agent
The Agentforce panel in Anypoint Code Builder has been updated with MuleSoft Dev Agent. MuleSoft Dev
Agent is an integrated assistant that enables developers to use natural language prompts to design,
develop, and manage applications directly within Anypoint Code Builder.
Dev Agent unifies all generative AI capabilities into a single experience:
- Create and edit flows
- Generate and refine API specifications
- Configure connections and projects
- Deploy applications
Dev Agent can read and write directly to project files, and supports tools provided by embedded MCP
servers.
For more information, see:
- [Creating API Specs with MuleSoft Vibes](../../anypoint-code-builder/vibes-api-ai-create-spec)
- [Developing Integrations Using MuleSoft Vibes](../../anypoint-code-builder/int-ai-developing-integrations)
#### Batch Processing Support
Create and configure batch jobs for processing large volumes of records asynchronously, in parallel,
and in chunks to optimize performance and resource utilization. For more information, see
[Batch Job (<batch:job/>)](../../anypoint-code-builder/acb-component-batch).
#### Duplicate Flows in Canvas
Duplicate flows in the canvas to create copies of existing flows with their components and
configurations. For more information, see
[Duplicate a Flow](../../anypoint-code-builder/int-configure-components#duplicate-a-flow).
#### Copy and Paste Components in Canvas
You can now copy components in your flow and paste them in the same or a different flow, while
retaining their configuration. For more information, see
[Copy Components](../../anypoint-code-builder/int-configure-components#copy-components).
#### Stability and Usability enhancements
##### Object Store in Global Configuration
Streamline your development with an improved visual and guided experience for configuring object
stores in any component and reduce the need for manual XML coding.
##### Special Characters Support
You can now use special characters in flow names, password fields, connection configurations, and
global elements.
##### Multiple Versions of a Connector Within a Project
You can now use multiple versions of a connector in your projects.
##### Multi level Connection Configurations
Easily manage and structure complex connection setups by layering connection configurations within
each other directly from the UI.
##### Flow Error Handler Configuration
New configuration options for handling errors in your Mule project flow.
##### Go to Flow Keyboard Shortcut
You can now quickly open a referenced flow by pressing Ctrl+Alt+g (Windows) or Cmd+Option+g (macOS)
while the `Flow ref` component is selected.
For more information, see
[Navigate to Referenced Flows](../../anypoint-code-builder/int-configure-components#navigate-to-referenced-flows).
##### Notifications with Project Context
Notifications now provide specific context about which projects are causing errors within a
workspace.
##### Design Service Connection on Non-English Computers
Users can now connect to the design service on a computer with a non-English language setting.
##### Initial pom.xml Template Update
The initial **pom.xml** template is updated to use HTTPS for Maven XSD to enhance its security.
##### Projects Open in Current Window
Projects created using the **Implement an API** option now open in the current window instead of a
new one.
##### Map and Transform with AI Improvements
The **Map and Transform with AI** feature now shows specific messaging when there is an error. Input
and output metadata is no longer required for this feature.
##### Variable and Attribute Configuration in Transformations
You can now edit and configure variables and attributes within transformations from the UI.
#### Mule Runtime Support
Support for Mule runtime engine version 4.10.0 Edge with Java version 17. See
[Compatibility](#compatibility).
#### Einstein Features and Free Trial Orgs
Einstein features are no longer be available on free trial Salesforce orgs. Users must link to their
own Salesforce org to use these features. For more information, see
[Managing your Anypoint Platform Account](../../access-management/managing-your-account).
#### More Agentic Integration Development with the Embedded MuleSoft Model Context Protocol (MCP) Server
Use natural language interaction to build Agent Fabric agent networks, manage governance rulesets,
and more. Any agent can execute MuleSoft MCP Server tools. MCP provides extensibility for a wide
array of agent types. For more information, see
[MuleSoft MCP Server Release Notes](../../mulesoft-mcp-server/mulesoft-mcp-server-release-notes).
### Fixed Issues
<table><colgroup><col> <col></colgroup><thead><tr><th>Issue Resolution</th><th>ID</th></tr></thead><tbody><tr><td><div><div><p>When setting up HTTP request headers, the IDE no longer incorrectly adds an empty array symbol #[] in the headers expression section of the flow XML code.</p></div></div></td><td><div><div><p>W-19152657</p></div></div></td></tr><tr><td><div><div><p>The inference connector no longer fails to retrieve and show dynamic data for the value provider field.</p></div></div></td><td><div><div><p>W-19084301</p></div></div></td></tr><tr><td><div><div><p>The IDE now correctly generates the default XML code snippets for nested fields, including arrays, objects, and unions.</p></div></div></td><td><div><div><p>W-19144806</p></div></div></td></tr><tr><td><div><div><p>In the Salesforce Connector, the parameters for the "Salesforce - Query" connector no longer disappear after clicking on it from the "Set variable" connector.</p></div></div></td><td><div><div><p>W-18836813</p></div></div></td></tr><tr><td><div><div><p>The Agent Conductor module now displays correctly.</p></div></div></td><td><div><div><p>W-19094498</p></div></div></td></tr><tr><td><div><div><p>The paths for certain container route types, such as scatter-gather and first successful, no longer overlap with each other.</p></div></div></td><td><div><div><p>W-19094528</p></div></div></td></tr><tr><td><div><div><p>The connection test for the Kafka connector is now working as expected.</p></div></div></td><td><div><div><p>W-12553536</p></div></div></td></tr><tr><td><div><div><p>The XML code is now generated in the correct order in the A2A Connector.</p></div></div></td><td><div><div><p>W-19105944</p></div></div></td></tr><tr><td><div><div><p>The MIME type parameters are shown as expected in the user interface.</p></div></div></td><td><div><div><p>W-18106124</p></div></div></td></tr><tr><td><div><div><p>DataWeave data and functions no longer return empty if adding a new project to an existing workspace.</p></div></div></td><td><div><div><p>W-18824864</p></div></div></td></tr><tr><td><div><div><p>The agent conductor data now loads properly in the user interface.</p></div></div></td><td><div><div><p>W-19154866</p></div></div></td></tr><tr><td><div><div><p>Setting breakpoints on flow control nodes is now working as expected.</p></div></div></td><td><div><div><p>W-18838355</p></div></div></td></tr><tr><td><div><div><p>The debugger tool no longer disappears unexpectedly.</p></div></div></td><td><div><div><p>W-19145809</p></div></div></td></tr><tr><td><div><div><p>The flow name updates as expected if you close the panel right after changing the flow name.</p></div></div></td><td><div><div><p>W-19147834</p></div></div></td></tr><tr><td><div><div><p>The error message <code>java.lang.NoClassDefFoundError: org/mule.apikit.ApiParser</code> no longer appears when the design service starts.</p></div></div></td><td><div><div><p>W-18195261</p></div></div></td></tr><tr><td><div><div><p>The output of a DataWeave mapping for non-transform components is no longer incorrect.</p></div></div></td><td><div><div><p>W-18566031</p></div></div></td></tr><tr><td><div><div><p>The startup error no longer occurs in specific customer project.</p></div></div></td><td><div><div><p>W-19337637</p></div></div></td></tr><tr><td><div><div><p>The output variable of a DataWeave mapping is now correct.</p></div></div></td><td><div><div><p>W-18566025</p></div></div></td></tr><tr><td><div><div><p>Dynamic control data is no longer overridden if you switch nodes.</p></div></div></td><td><div><div><p>W-19280291</p></div></div></td></tr><tr><td><div><div><p>Adding a <code>Raise error</code> component no longer breaks DataSense for the entire flow.</p></div></div></td><td><div><div><p>W-19404195</p></div></div></td></tr><tr><td><div><div><p>Validation issues in the XML file are fixed when using the batch component.</p></div></div></td><td><div><div><p>W-19136911</p></div></div></td></tr><tr><td><div><div><p>DataSense resolution errors no longer occur with certain components.</p></div></div></td><td><div><div><p>W-19367638</p></div></div></td></tr><tr><td><div><div><p>Sample data persistence calls for some nodes no longer fail.</p></div></div></td><td><div><div><p>W-19145325</p></div></div></td></tr><tr><td><div><div><p>Debug sessions are no longer killed on slower machines.</p></div></div></td><td><div><div><p>W-19183938</p></div></div></td></tr><tr><td><div><div><p>The <code>Flow Ref</code> component now correctly gets the flow list even if a flow is disabled.</p></div></div></td><td><div><div><p>W-19248177</p></div></div></td></tr><tr><td><div><div><p>Breakpoints set in one file are no longer incorrectly shown in another fileâ€™s canvas.</p></div></div></td><td><div><div><p>W-19302452</p></div></div></td></tr><tr><td><div><div><p>DataWeave expressions used within a <code>variable</code> of a <code>Transform Message</code> component are no longer lost.</p></div></div></td><td><div><div><p>W-19336241</p></div></div></td></tr><tr><td><div><div><p>Custom names for flows and error handlers are now correctly updated in the flow canvas.</p></div></div></td><td><div><div><p>W-19121648</p></div></div></td></tr><tr><td><div><div><p>The error state for connector routes is now displayed correctly.</p></div></div></td><td><div><div><p>W-19388454</p></div></div></td></tr><tr><td><div><div><p>The <strong>Export Shareable Jar</strong> command on Windows no longer includes unwanted folders.</p></div></div></td><td><div><div><p>W-19461974</p></div></div></td></tr><tr><td><div><div><p><strong>NullPointerException</strong> no longer occurs if invoking <code>'getElementName()</code>.</p></div></div></td><td><div><div><p>W-18727157</p></div></div></td></tr><tr><td><div><div><p>The <strong>Go to Flow</strong> command now correctly finds a sub-flow in a second file.</p></div></div></td><td><div><div><p>W-19013755</p></div></div></td></tr><tr><td><div><div><p>The <strong>Map and Transform with AI</strong> feature is now working as expected.</p></div></div></td><td><div><div><p>W-19134821</p></div></div></td></tr></tbody></table>
## September 3, 2025
Anypoint Code Builder releases new features in the Anypoint Extension Pack and the Cloud IDE.
- Extension pack version: 1.10.2
  To use this extension pack in the desktop IDE, see
  [Set up the Desktop IDE](../../anypoint-code-builder/start-acb#set-up-desktop).
- Cloud IDE version: 1.10.2
  This cloud IDE version runs the 1.10.2 extension pack.
For extension versions, see
[Change Log](https://marketplace.visualstudio.com/items/salesforce.mule-dx-extension-pack/changelog)
in the VS Code Marketplace.
For more information, see [Known Issues](#known-issues) and [Compatibility](#compatibility).
### Whatâ€™s New
- Support for Mule runtime engine version 4.9.9 LTS with Java version 17. See
  [Compatibility](#compatibility).
### Fixed Issues
<table><colgroup><col> <col></colgroup><thead><tr><th>Issue Resolution</th><th>ID</th></tr></thead><tbody><tr><td><div><div><p>The platform extension pack is updated to version 5.7.2 to fix a compatibility issue with Intel Mac machines.</p></div></div></td><td><div><div><p>W-19359467</p></div></div></td></tr></tbody></table>
## August 19, 2025
Anypoint Code Builder releases this patch version in the Anypoint Extension Pack and the Cloud IDE.
- Extension pack version: 1.10.1
  To use this extension pack in the desktop IDE, see
  [Set up the Desktop IDE](../../anypoint-code-builder/start-acb#set-up-desktop).
- Cloud IDE version: 1.10.1
  This cloud IDE version runs the 1.10.1 extension pack.
For extension versions, see
[Change Log](https://marketplace.visualstudio.com/items/salesforce.mule-dx-extension-pack/changelog)
in the VS Code Marketplace.
For more information, see [Known Issues](#known-issues) and [Compatibility](#compatibility).
## August 11, 2025
Anypoint Code Builder releases new features in the Anypoint Extension Pack and the Cloud IDE.
- Extension pack version: 1.10.0
  To use this extension pack in the desktop IDE, see
  [Set up the Desktop IDE](../../anypoint-code-builder/start-acb#set-up-desktop).
- Cloud IDE version: 1.10.0
  This cloud IDE version runs the 1.10.0 extension pack.
For extension versions, see
[Change Log](https://marketplace.visualstudio.com/items/salesforce.mule-dx-extension-pack/changelog)
in the VS Code Marketplace.
For more information, see [Known Issues](#known-issues) and [Compatibility](#compatibility).
### Whatâ€™s New
This release introduces this feature:
- Agentic Integration Development with the Embedded MuleSoft Model Context Protocol (MCP) Server
  With agentic integration development, build and manage your integration with natural language
  interaction, not code. Any agent can execute MuleSoft MCP Server tools to create, test, debug, and
  deploy Mule applications. MCP provides extensibility for a wide array of agent types. For more
  information, see [MuleSoft MCP Server Overview](../../mulesoft-mcp-server/).
## July 21, 2025
Anypoint Code Builder releases new features in the Anypoint Extension Pack and the Cloud IDE.
- Extension pack version: 1.9.2
  To use this extension pack in the desktop IDE, see
  [Set up the Desktop IDE](../../anypoint-code-builder/start-acb#set-up-desktop).
- Cloud IDE version: 1.9.2
  This cloud IDE version runs the 1.9.2 extension pack.
For extension versions, see
[Change Log](https://marketplace.visualstudio.com/items/salesforce.mule-dx-extension-pack/changelog)
in the Visual Studio Code Marketplace.
For more information, see [Known Issues](#known-issues) and [Compatibility](#compatibility).
### Whatâ€™s New
- Support for Mule runtime engine version 4.9.7 LTS with Java version 17. See
  [Compatibility](#compatibility).
## July 4, 2025
Anypoint Code Builder releases new features in the Anypoint Extension Pack and the Cloud IDE.
- Extension pack version: 1.9.0
  To use this extension pack in the desktop IDE, see
  [Set up the Desktop IDE](../../anypoint-code-builder/start-acb#set-up-desktop).
- Cloud IDE version: 1.9.0
  This cloud IDE version runs the 1.9.0 extension pack.
For extension versions, see
[Change Log](https://marketplace.visualstudio.com/items/salesforce.mule-dx-extension-pack/changelog)
in the Visual Studio Code Marketplace.
For more information, see [Known Issues](#known-issues) and [Compatibility](#compatibility).
### Whatâ€™s New
This release introduces these features:
- [Map Fields in DataWeave Expressions with AI](#dataweave-transform-map)
- [Generate DataWeave Transformations with AI](#dataweave-transform-map-transform)
- [Design API Specs with AI](#api-design)
- [Use A2A Connector (Beta) with Anypoint Code Builder](#a2a-connector)
- [Use MCP Connector 1.0 (Generally Available) with Anypoint Code Builder](#mcp-connector)
- [Create MUnit Test from Flow](#munit-flow)
- [Scope MUnit Tests to Specific Processors from UI](#munit-processor)
- [Comment Out Components in Canvas](#comment-out-canvas)
- [Navigate to Flows from Connectors](#navigate-to-flows)
- [Review Scaffolding Errors in Output Panel](#scaffolding-errors)
- [Open Projects in Canvas by Default](#canvas-default)
- [Enter Properties as Values in Fields in UI](#properties-in-fields)
- [Check Java and Mule Runtime Compatibility for All Connectors in Your Project](#connector-compatibility)
- [Use Anypoint Code Builder with Windows 11](#windows-11)
- [Agentforce Command Removed](#command-removed)
- [Fixed Issues](#july-25-fixed-issues)
#### Map Fields in DataWeave Expressions with AI
Automatically generate field-to-field mappings based on input and output metadata with the
assistance of AI.
For more information, see
[Map with AI](../../anypoint-code-builder/int-configure-dw-expressions#map-with-ai).
#### Generate DataWeave Transformations with AI
Generate full DataWeave transformations from input and output sample data with the assistance of AI.
For more information, see
[Map and Transform with AI](../../anypoint-code-builder/int-configure-dw-expressions#map-and-transform-with-ai).
#### Design API Specs with AI
Use Einstein generative AI to generate API specs from a conversation.
For more information, see [Designing API Specs with AI](../../anypoint-code-builder/mulesoft-vibes).
#### Use A2A Connector (Beta) with Anypoint Code Builder
This release introduces support for Anypoint Connector for Agent2Agent (A2A Connector) (beta). A2A
Connector (beta) facilitates inter-agent communication for Large Language Model (LLM) agents and
other applications by implementing the A2A protocol. This enables agents to interact and delegate
specialized tasks to other agents. See
[Built-In Connectors](../../anypoint-code-builder/ref-connectors).
_A2A Connector is a beta connector that is subject to the Beta Services Terms at
[Agreements - Salesforce.com](https://www.salesforce.com/company/legal/agreements/) or a written
Unified Pilot Agreement if executed by Customer, and the Non-GA Gen AI and Non-GA Credit Consumption
terms in the
[Product Terms Directory](https://ptd.salesforce.com/?_ga=2.247987783.1372150065.1709219475-629000709.1639001992).
Use of this beta connector with external systems or services consumes Mule messages and is at the
Customerâ€™s sole discretion._
#### Use MCP Connector 1.0 (Generally Available) with Anypoint Code Builder
This release introduces support for the generally available version of Anypoint Connector for MCP
(MCP Connector). Previously, Anypoint Code Builder supported the beta version of MCP Connector. If
you used the beta version of MCP Connector, remove `-Dmule.http.service.implementation=NETTY` from
Runtime: Default Arguments in MuleSoft Settings. Also, the Design Service: System Properties setting
is removed from MuleSoft Settings.
MCP Connector helps you expose your Mule application as a tool that any AI client supporting Model
Context Protocol (MCP) can use to perform real-world actions. See
[Built-In Connectors](../../anypoint-code-builder/ref-connectors).
#### Create MUnit Test from Flow
Create MUnit tests for your Mule project directly from the context menu of a flow.
For more information, see
[Create a Test from a Flow](../../anypoint-code-builder/int-test-munit#create-test-from-flow).
#### Scope MUnit Tests to Specific Processors from UI
Select the processors and attributes in a Mule flow from the UI for testing to iâ€‹ncrease precision,
identify issues faster, and create tests more efficiently.
For more information, see
[Targeting Specific Processors and Attributes in Your Test](../../anypoint-code-builder/int-test-munit#targeting-specific-processors-and-attributes-in-your-test).
#### Comment Out Components in Canvas
Comment out components directly in Anypoint Code Builder canvas. Disabled components can also be
deleted in bulk for cleanup purposes.
#### Navigate to Flows from Connectors
You can now open the target flow referenced by a connector, using the **Go to Flow** option in the
context menu for application flows and MUnit test flows to trace and manage application logic across
modular flows.
#### Review Scaffolding Errors in Output Panel
Now itâ€™s even easier to troubleshoot errors when creating a project. In the Output panel, thereâ€™s a
new **MuleDX Server - Scaffolding** option. Select that option to show the MuleDX Server log content
thatâ€™s related to scaffolding only.
![Output panel with Mule DX Server: Scaffolding selected](../_images/code-builder/scaffolding.png)
For more information, see
[Viewing Logs and Errors](../../anypoint-code-builder/start-open-output-panel).
#### Open Projects in Canvas by Default
Anypoint Code Builder now opens projects in the canvas by default. You can save and debug your
applications directly from the UI without switching views, streamlining your low-code experience.
#### Enter Properties as Values in Fields in UI
Property mode `{}` now makes it possible to enter properties in number and boolean fields in the UI.
Previously, it was possible only in the code editor.
![Create parent directories field with Property mode enabled](../_images/code-builder/bracket.png)
#### Check Java and Mule Runtime Compatibility for All Connectors in Your Project
Verify that your local and Anypoint Exchange connectors are compatible with your Java and Mule
runtime version for your projects. Project Properties now tells you about incompatible versions and
lets you fix them right away, accelerating development and reducing blockers, especially when
importing projects. Previously, Project Properties verified compatibility of Anypoint Exchange
connectors only.
For more information, see
[Version Settings for Mule, Java, and Connectors](../../anypoint-code-builder/int-versions).
#### Use Anypoint Code Builder with Windows 11
Anypoint Code Builder Desktop IDE now supports Windows 11.
For more information, see [Compatibility](#compatibility).
#### Agentforce Command Removed
The **MuleSoft: Open Agentforce** command is removed from the Command Palette. You can use the
toolbar button to access the Agentforce panel when available.
### Fixed Issues
<table><colgroup><col> <col></colgroup><thead><tr><th>Issue Resolution</th><th>ID</th></tr></thead><tbody><tr><td><div><div><p>When you define a DataWeave multiline expression, code highlighting now works as expected.</p></div></div></td><td><div><div><p>W-11492623</p></div></div></td></tr></tbody></table>
## May 27, 2025
Anypoint Code Builder releases new features in the Anypoint Extension Pack and the Cloud IDE.
- Extension pack version: 1.8.2
  To use this extension pack in the desktop IDE, see
  [Set up the Desktop IDE](../../anypoint-code-builder/start-acb#set-up-desktop).
- Cloud IDE version: 1.8.3
  This cloud IDE version runs the 1.8.2 extension pack.
For extension versions, see
[Change Log](https://marketplace.visualstudio.com/items/salesforce.mule-dx-extension-pack/changelog)
in the VS Code Marketplace.
For more information, see [Known Issues](#known-issues) and [Compatibility](#compatibility).
### Whatâ€™s New
- Authentication support for Cursor, Trae, and Windsurf.
- Support for Mule runtime engine version 4.9.4 LTS with Java version 17. See
  [Compatibility](#compatibility).
## April 29, 2025
Anypoint Code Builder releases new features in the Anypoint Extension Pack and the Cloud IDE.
- Extension pack version: 1.8.1
  To use this extension pack in the desktop IDE, see
  [Set up the Desktop IDE](../../anypoint-code-builder/start-acb#set-up-desktop).
- Cloud IDE version: 1.8.3
  This cloud IDE version runs the 1.8.1 extension pack.
For extension versions, see
[Change Log](https://marketplace.visualstudio.com/items/salesforce.mule-dx-extension-pack/changelog)
in the VS Code Marketplace.
For more information, see [Known Issues](#known-issues) and [Compatibility](#compatibility).
### Whatâ€™s New
This release introduces support for Anypoint Connector for MCP (MCP Connector) (beta). MCP Connector
(beta) helps you expose your Mule application as a tool that any AI client supporting Model Context
Protocol (MCP) can use to perform real-world actions. For example, your MCP client can trigger a
process, look up data, or transform records. See
[Built-In Connectors](../../anypoint-code-builder/ref-connectors).
_MCP Connector is a beta connector that is subject to the Beta Services Terms at
[Agreements - Salesforce.com](https://www.salesforce.com/company/legal/agreements/) or a written
Unified Pilot Agreement if executed by Customer, and the Non-GA Gen AI and Non-GA Credit Consumption
terms in the
[Product Terms Directory](https://ptd.salesforce.com/?_ga=2.247987783.1372150065.1709219475-629000709.1639001992).
Use of this beta connector with external systems or services consumes Mule messages and is at the
Customerâ€™s sole discretion._
## March 21, 2025
Anypoint Code Builder releases new features in the Anypoint Extension Pack and the Cloud IDE.
- Extension pack version: 1.8.0
  To use this extension pack in the desktop IDE, see
  [Set up the Desktop IDE](../../anypoint-code-builder/start-acb#set-up-desktop).
- Cloud IDE version: 1.8.0
  This cloud IDE version runs the 1.8.0 extension pack.
For extension versions, see
[Change Log](https://marketplace.visualstudio.com/items/salesforce.mule-dx-extension-pack/changelog)
in the VS Code Marketplace.
For more information, see [Known Issues](#known-issues) and [Compatibility](#compatibility).
### Whatâ€™s New
This release introduces these features:
- New DataWeave Transformation Builder Tool.
  Transform your message payload, attributes, and variables to the required output format and data
  structure with DataWeave Transformation Builder. See
  [Open Transformation Builder](../../anypoint-code-builder/int-configure-dw-expressions#open-transformation-builder).
- Refine your flows through natural language interactions.
  Anypoint Code Builder dynamically updates your flow code based on your latest instructions,
  ensuring an easy and efficient workflow. Plus, access your chat history to track changes.
- Validate and publish your API project to Anypoint Exchange through a new intuitive user interface.
  See
  [Publishing API Projects to Exchange](../../anypoint-code-builder/des-publish-api-spec-to-exchange).
- Build Agentforce integrations using Agentforce Connector 1.0.1 and Einstein AI Connector 1.1.1.
  See [Built-In Connectors](../../anypoint-code-builder/ref-connectors).
- Agentforce for Anypoint Code Builder Generative Flows is now available on these Anypoint Platform
  instances on Hyperforce: [Canada Cloud](https://ca1.platform.mulesoft.com) and
  [Japan Cloud](https://jp1.platform.mulesoft.com).
- New documentation to help you migrate your Anypoint Studio Mule projects to Anypoint Code Builder.
  Learn how to import your Mule projects into Anypoint Code Builder to unlock a modern development
  experience with faster startup times, streamlined collaboration, and the integration of MuleSoft
  for Agentforce: Topic Center to enable API projects for topics and agents. See
  [Migrate Your Mule Project from Anypoint Studio to Anypoint Code Builder](../../anypoint-code-builder/int-migrate-studio-to-acb).
- The Einstein generative flow feature is now called the Agentforce generative flow feature.
### Fixed Issues
<table><colgroup><col> <col></colgroup><thead><tr><th>Issue Resolution</th><th>ID</th></tr></thead><tbody><tr><td><div><div><p>DataSense now works as expected when a tag spans multiple lines.</p></div></div></td><td><div><div><p>W-12482310</p></div></div></td></tr><tr><td><div><div><p>DataSense now works as expected when you create a project with Mule runtime version 4.4 and no other runtime versions are downloaded.</p></div></div></td><td><div><div><p>W-16117373</p></div></div></td></tr></tbody></table>
## February 6, 2025
Anypoint Code Builder releases new features in the Anypoint Extension Pack and the Cloud IDE.
- Extension pack version: 1.7.0
  To use this extension pack in the desktop IDE, see
  [Set up the Desktop IDE](../../anypoint-code-builder/start-acb#set-up-desktop).
- Cloud IDE version: 1.7.1
  This cloud IDE version runs the 1.7.0 extension pack.
For extension versions, see
[Change Log](https://marketplace.visualstudio.com/items/salesforce.mule-dx-extension-pack/changelog)
in the VS Code Marketplace.
For more information, see [Known Issues](#known-issues) and [Compatibility](#compatibility).
### Whatâ€™s New
This release introduces these features:
- Support for
  [MuleSoft for Agentforce: Topic Center](../../anypoint-code-builder/ai-enabling-api-project-topic-center).
  - Use the visual editor when you design an API to enable your API specifications for topics and
    agents.
  - Make your topic and action-enabled APIs available in Salesforce using Salesforce API Catalog.
  - Augment agent functionality by assigning topics to Agentforce agents in Agent Builder.
  - Use the provided governance rules to validate that your API is ready to generate agent actions
    and topics in Salesforce.
- Run MUnit tests from the canvas. See
  [Testing Projects with MUnit](../../anypoint-code-builder/int-test-munit#run-tests-from-the-canvas).
- Configure proxy settings. See
  [Using a Proxy in Anypoint Code Builder](../../anypoint-code-builder/ref-proxy-settings).
- Streamline productivity with performance enhancements for DataSense, flow canvas rendering, and
  connector configuration testing.
- Support for Mule runtime engine version 4.9 LTS with Java version 17. See
  [Compatibility](#compatibility).
### Fixed Issues
<table><colgroup><col> <col></colgroup><thead><tr><th>Issue Resolution</th><th>ID</th></tr></thead><tbody><tr><td><div><div><p>A notification now appears after you change the region in the <code>settings.json</code> file.</p></div></div></td><td><div><div><p>W-13184670</p></div></div></td></tr><tr><td><div><div><p>XML formatting is no longer corrupted when you add or update a connection configuration, or when you use the <strong>Format Document</strong> menu option.</p></div></div></td><td><div><div><p>W-16850099</p></div></div></td></tr><tr><td><div><div><p>Avro suggestions now appear when you define an Avro schema and declare a record inside a record property.</p></div></div></td><td><div><div><p>W-16814386</p></div></div></td></tr><tr><td><div><div><p>Correct suggestions now display for inline Avro schema payloads. The issue occurred inside maps that contained arrays.</p></div></div></td><td><div><div><p>W-16809972</p></div></div></td></tr><tr><td><div><div><p>Correct suggestions now display for values in fields of type map.</p></div></div></td><td><div><div><p>W-16814887</p></div></div></td></tr><tr><td><div><div><p>Syntax errors in DataWeave expressions in projects imported from Studio no longer occur. Anypoint Code Builder now automatically fetches the required dependencies when the project loads.</p></div></div></td><td><div><div><p>W-14037343</p></div></div></td></tr><tr><td><div><div><p>When you use a proxy, the Mule runtime options now appear in the UI form for creating a new integration project. You can click <strong>Create Project</strong> to create the project.</p></div></div></td><td><div><div><p>None</p></div></div></td></tr></tbody></table>
## December 9, 2024
Anypoint Code Builder releases a new feature in the Anypoint Extension Pack.
- Extension pack version: 1.6.0
  To use this extension pack in the desktop IDE, see
  [Set up the Desktop IDE](../../anypoint-code-builder/start-acb#set-up-desktop).
For extension versions, see
[Change Log](https://marketplace.visualstudio.com/items/salesforce.mule-dx-extension-pack/changelog)
in the VS Code Marketplace.
For more information, see [Known Issues](#known-issues) and [Compatibility](#compatibility).
### Whatâ€™s New
- This product is now available on Hyperforce.
  Anypoint Platform instances on the Hyperforce infrastructure are:
  - [Canada Cloud](https://ca1.platform.mulesoft.com)
  - [Japan Cloud](https://jp1.platform.mulesoft.com)
    Exceptions:
    - Einstein for Anypoint Code Builder Generative Flows is available only on US and EU cloud
      hosts. Canada and Japan cloud hosts are currently not supported.
    - Cloud IDE is available only on US and EU cloud hosts. Canada and Japan cloud hosts are
      currently not supported.
- â€œDesign Centerâ€ UI labels are renamed to â€œMuleSoft VCSâ€.
### Fixed Issues
<table><colgroup><col> <col></colgroup><thead><tr><th>Issue Resolution</th><th>ID</th></tr></thead><tbody><tr><td><div><div><p>Anypoint Connector for Zoom (Zoom Connector) component configuration view now correctly displays relevant options.</p></div></div></td><td><div><div><p>W-17148078</p></div></div></td></tr><tr><td><div><div><p>Adding a transform connector no longer incorrectly inserts <code>#[]</code> in script fields.</p></div><div><p>Previous: <code><![CDATA[#["test"]]]></code></p></div><div><p>New: <code><![CDATA["test"]]></code></p></div></div></td><td><div><div><p>W-17199037</p></div></div></td></tr></tbody></table>
## November 4, 2024
Anypoint Code Builder releases a new feature in the Anypoint Extension Pack and the cloud IDE.
- Extension pack version: 1.5.0
  To use this extension pack in the desktop IDE, see
  [Set up the Desktop IDE](../../anypoint-code-builder/start-acb#set-up-desktop).
- Cloud IDE version: 1.5.0
  This cloud IDE version runs the 1.5.0 extension pack.
For extension versions, see
[Change Log](https://marketplace.visualstudio.com/items/salesforce.mule-dx-extension-pack/changelog)
in the VS Code Marketplace.
For more information, see [Known Issues](#known-issues) and [Compatibility](#compatibility).
### Whatâ€™s New
The release introduces the following feature:
- The Einstein for Anypoint Code Builder Generative Flows feature is now enabled and managed in
  Anypoint Platform Access Management.
  For more information, see
  [Enabling Einstein for Anypoint Platform](../../access-management/enabling-agentforce).
### Fixed Issues
<table><colgroup><col> <col></colgroup><thead><tr><th>Issue Resolution</th><th>ID</th></tr></thead><tbody><tr><td><div><div><p>JMS Connector connections can now be validated with the <strong>Test Connection</strong> button.</p></div></div></td><td><div><div><p>W-16983063</p></div></div></td></tr></tbody></table>
## October 8, 2024
Anypoint Code Builder releases new features in the Anypoint Extension Pack and the cloud IDE.
- Extension pack version: 1.4.1
  To use this extension pack in the desktop IDE, see
  [Set up the Desktop IDE](../../anypoint-code-builder/start-acb#set-up-desktop).
- Cloud IDE version: 1.4.6
  This cloud IDE version runs the 1.4.1 extension pack.
For extension versions, see
[Change Log](https://marketplace.visualstudio.com/items/salesforce.mule-dx-extension-pack/changelog)
in the VS Code Marketplace.
For more information, see [Known Issues](#known-issues) and [Compatibility](#compatibility).
### Whatâ€™s New
This release introduces these features:
- [Advanced Data Types](#data-types-advanced)
- [Connection Configurations from the UI](#connection-configurations)
- [Code Coverage Reports](#code-coverage-munit)
- [Deploy to CloudHub 2.0](#cloudhub-2-deployments)
- [Publish Mule Projects to Anypoint Exchange](#app-publish-exchange)
- [AsyncAPI Specification Design and Governance](#asyncapi-design)
- [AsyncAPI Support for Avro Schema Fragments](#asyncapi-avro)
- [AsyncAPI Implementation Support for Solace PubSub+ and Salesforce Platform Events Connectors](#solace-platform-support)
- [Support for Mule Version 4.8](#runtime-version-support)
- [Enhanced API Auto-Completion](#api-autocompletion)
- [API Autodiscovery](#api-autodiscovery)
- [Enhanced Debugging](#visual-debugger)
- [Custom Connector Support](#custom-connector-support)
#### Advanced Data Types
The connection configuration panel in the canvas UI adds support for configuring connections,
objects, arrays of non-primitive types, and multi-level dynamic lists. In the previous release, the
configuration panel supported unions, arrays of primitive types, file selectors, and password
fields.
For more information, see
[Adding a Component to Your Project](../../anypoint-code-builder/int-configure-components-add).
#### Connection Configurations from the UI
Connection configurations are global configurations that more than one component in a project can
use. Anypoint Code Builder improves workflow by enabling you to check for components that use the
connection through the UI.
For more information, see
[Adding a Component to Your Project](../../anypoint-code-builder/int-configure-components-add).
#### Code Coverage Reports
Anypoint Code Builder adds code coverage reports for testing integration and implementation projects
with MUnit.
For more information, see
[Running MUnit Tests with Coverage](../../anypoint-code-builder/int-test-munit#run-coverage).
Additionally, you can now run MUnit tests in Anypoint Code Builder without setting your credentials
in Maven.
#### Deploy to CloudHub 2.0
In addition to supporting deployments of your integrations to CloudHub, Anypoint Code Builder adds
support for deployments to CloudHub 2.0.
For more information, see
[Deploying Mule Apps to CloudHub and CloudHub 2.0](../../anypoint-code-builder/int-deploy-mule-apps).
#### Publish Mule Projects to Anypoint Exchange
Anypoint Code Builder adds functionality for publishing project templates and project examples to
Anypoint Exchange. Publishing to Exchange enables your team to reuse your applications.
For more information, see
[Publishing a Mule Project to Exchange](../../anypoint-code-builder/int-export-mule-project#publishable).
#### AsyncAPI Specification Design and Governance
Anypoint Code Builder now supports creating, designing, and governing AsyncAPI 2.6 specifications.
For more information, see:
- [Creating and Importing AsyncAPI API Specifications](../../anypoint-code-builder/des-create-asyncapi-api-specs)
- [Validating API Specifications Against Governance Rulesets](../../anypoint-code-builder/des-govern-api)
#### AsyncAPI Support for Avro Schema Fragments
Anypoint Code Builder adds support for creating and designing Apache Avro schema fragments. Ensure
data consistency and interoperability in distributed systems by defining Avro schemas with
structured data, including data types and fields.
For more information, see
[Creating and Using API Spec Fragments](../../anypoint-code-builder/des-create-api-fragments)
#### AsyncAPI Implementation Support for Solace PubSub+ and Salesforce Platform Events Connectors
Anypoint Code Builder adds support for Solace PubSub+ and Salesforce platform events connectors.
Expand your integration capabilities and streamline event-driven architectures. For more
information, see
[Supported Message Brokers](../../apikit/latest/apikit-asyncapi-module-reference#supported-message-brokers).
Implementing AsyncAPI specifications using DataSense for Avro schemas requires Mule 4.8 or later.
#### Support for Mule Version 4.8
Anypoint Code Builder adds support for Mule version 4.8 with Java versions 11 and 17. For more
information, see [Mule and Java version support](#versions-mule-jdk).
#### Enhanced API Auto-Completion
Anypoint Code Builder introduces enhanced API auto-completion. Instead of typing Ctrl+Space to
activate the auto-completion menu in your API spec, you can place your cursor at the location in
your API spec file where you require suggestions. If the line has some content, press Tab, press
Space, or start typing after the content on the line to launch the menu. To close the
auto-completion menu, press Escape.
- [Mule > Editor > Auto-completion: Enablement](../../anypoint-code-builder/ref-mule-settings#setting-auto-complete)
  This setting is disabled by default.
- [Mule > Editor > Auto-completion: Trigger Delay](../../anypoint-code-builder/ref-mule-settings#setting-auto-complete)
For more information on using auto-complete, see
[Use Auto-Complete in the Editors](../../anypoint-code-builder/start-discover-ui#use-autocomplete).
#### API Autodiscovery
Anypoint Code Builder supports configuring Mule apps for tracking requests with Autodiscovery.
Configure a Mule app to send request data to an API running on a Mule Gateway runtime in API
Manager. The API tracks this data in charts in API Manager.
For more information, see
[Tracking Requests with Autodiscovery](../../anypoint-code-builder/int-autodiscovery-config).
#### Enhanced Debugging
Anypoint Code Builder adds breakpoint indicators in the canvas UI for components that have one or
more breakpoints in the configuration XML. Indicators also display when stepping through a flow
while debugging.
Additionally, you can add and remove breakpoints on components in the canvas UI.
For more information, see
[Debugging Mule Applications](../../anypoint-code-builder/int-debug-mule-apps).
#### Custom Connector Support
Anypoint Code Builder now supports custom connectors that are locally bundled or published to
Exchange.
For locally bundled connectors, add the dependency to your integration project by referencing the
Maven dependency in your `pom.xml` file.
For connectors published to Exchange, add the component from the **Add Component** panel using the
**Search in Exchange** toggle.
### Fixed Issues
<table><colgroup><col> <col></colgroup><thead><tr><th>Issue Resolution</th><th>ID</th></tr></thead><tbody><tr><td><div><div><p>The <strong>Governance Rulesets</strong> and <strong>Governance Results</strong> panels now update as expected when more than one project folder is open in a VS Code workspace.</p></div></div></td><td><div><div><p>W-15677742</p></div></div></td></tr><tr><td><div><div><p>After iteratively scaffolding an API spec into an implementation project, the <strong>Data</strong> and <strong>Functions</strong> tabs in the expression builder no longer display the "loading" animation.</p></div></div></td><td><div><div><p>W-15828343</p></div></div></td></tr></tbody></table>
## August 17, 2024
Anypoint Code Builder releases a new feature in the Anypoint Extension Pack and the cloud IDE.
- Extension pack version: 1.3.0
  To use this extension pack in the desktop IDE, see
  [Set up the Desktop IDE](../../anypoint-code-builder/start-acb#set-up-desktop).
- Cloud IDE version: 1.3.0
  This cloud IDE version runs the 1.3.0 extension pack.
For extension versions, see
[Change Log](https://marketplace.visualstudio.com/items/salesforce.mule-dx-extension-pack/changelog)
in the VS Code Marketplace.
For more information, see [Known Issues](#known-issues) and [Compatibility](#compatibility).
### Whatâ€™s New
The release introduces the following feature:
- You can now use the Einstein for Anypoint Code Builder Generative Flows feature to jumpstart your
  integration development by generating flows for you. For more information about this feature, see
  [Developing Integrations Using MuleSoft Vibes](../../anypoint-code-builder/int-ai-developing-integrations).
### Fixed Issues
<table><colgroup><col> <col></colgroup><thead><tr><th>Issue Resolution</th><th>ID</th></tr></thead><tbody><tr><td><div><div><p>The <strong>Governance Rulesets</strong> and <strong>Governance Results</strong> now update as expected when more than one folder is open in a VS Code workspace.</p></div></div></td><td><div><div><p>W-15677742</p></div></div></td></tr><tr><td><div><div><p>The <strong>Preview</strong> tab in the expression builder UI no longer produces an <code>Internal Error</code> message when you configure an attribute of a componentâ€™s child element in the XML editor <em>and</em> that attribute accepts DataWeave expressions. This issue affected all components with child attributes that accept expressions. The following example displays a child element with an attribute that contains a DataWeave expression:</p></div><div><div><img src="../_images/code-builder/ki-w-15906886-june24.png" alt="Attribute with an expression in nested element of a component"></div></div></div></td><td><div><div><p>W-15906886</p></div></div></td></tr></tbody></table>
## July 2, 2024
This patch release addresses Anypoint Code Builder issues.
### Fixed Issues
<table><colgroup><col> <col></colgroup><thead><tr><th>Issue Resolution</th><th>ID</th></tr></thead><tbody><tr><td><div><div><p>You no longer have to update the runtime version when deploying a Mule application with Mule runtime version 4.6 or 4.7. This issue occurred when deploying to CloudHub from the IDE.</p></div></div></td><td><div><div><p>W-15902597</p></div></div></td></tr><tr><td><div><div><p>A tooling client error no longer appears after creating a Java class, adding a New operation from the Java Module to a flow, selecting the class, and then refreshing Constructor.</p></div></div></td><td><div><div><p>W-15877062</p></div></div></td></tr><tr><td><div><div><p>The XML now reflects changes after configuring the Send operation of Anypoint Connector for Email (Email Connector) from the component configuration panel.</p></div></div></td><td><div><div><p>W-15906937</p></div></div></td></tr><tr><td><div><div><p>After changing the class setting in the <strong>Class</strong> field, you no longer have to refresh the <strong>Method</strong> field before selecting from the list of methods in the class. This issue occurred when updating the Invoke, Invoke Static, or New operations from the Java Module in the configuration panel.</p></div></div></td><td><div><div><p>W-15111695</p></div></div></td></tr><tr><td><div><div><p>To import DataWeave libraries when using functions outside of the Core library, you no longer have to use the <strong>Quick Fix</strong> option. The DataWeave libraries are now imported automatically.</p></div></div></td><td><div><div><p>W-15673127</p></div></div></td></tr><tr><td><div><div><p>The feedback button for the open beta of AsyncAPI support to implement event-driven architecture now consistently appears in the canvas.</p></div></div></td><td><div><div><p>W-16084084</p></div></div></td></tr></tbody></table>
Patching the desktop IDE extensions requires a manual update or installation of the Anypoint
Extension Pack. The cloud IDE is updated automatically.
- Extension pack version: 1.2.2
  To use this extension pack in the desktop IDE, see
  [Set up the Desktop IDE](../../anypoint-code-builder/start-acb#set-up-desktop).
- Cloud IDE version: 1.2.4
  This cloud IDE version runs the 1.2.2 extension pack.
For extension versions, see
[Change Log](https://marketplace.visualstudio.com/items/salesforce.mule-dx-extension-pack/changelog)
in the VS Code Marketplace.
For more information, see [Known Issues](#known-issues) and [Compatibility](#compatibility).
## June 24, 2024
AsyncAPI Beta: AsyncAPI 2.6 and 2.0 implementation features are now available for use in Anypoint
Code Builder. The minimum Mule runtime engine requirement for this feature is Mule 4.6.
Before you can use these features, your Anypoint Platform organization administrator must accept the
Beta terms and conditions from the Anypoint Code Builder landing page in Anypoint Platform. For
guidance, see [Implementing AsyncAPI Specifications](../../anypoint-code-builder/imp-asyncapi).
Anypoint Extension Pack has not changed since the [June 4, 2024 release](#jun-2024). If you
installed or upgraded your extensions on the desktop IDE in that release, no installation or upgrade
is required. The cloud IDE was updated automatically in that release.
To learn about the AsyncAPI journey, see
[AsyncAPI Support to Implement Event-Driven Architecture](../platform/event-driven-api).
For more information, see [Known Issues](#known-issues) and [Compatibility](#compatibility).
## June 4, 2024
Anypoint Code Builder releases new features in the Anypoint Extension Pack and the cloud IDE.
- Extension pack version: 1.2.1
  To use this extension pack in the desktop IDE, see
  [Set up the Desktop IDE](../../anypoint-code-builder/start-acb#set-up-desktop).
- Cloud IDE version: 1.2.1
  This cloud IDE version runs the 1.2.1 extension pack.
For extension versions, see
[Change Log](https://marketplace.visualstudio.com/items/salesforce.mule-dx-extension-pack/changelog)
in the VS Code Marketplace.
### Whatâ€™s New
The release introduces the following features:
- [DataWeave Expression Builder](#dw-expression-builder)
- [Component Configuration Enhancements](#component-config-ui)
- [Support for Multiple Mule Runtime Versions with Java 17 or 11](#multiruntime)
- [Custom Java Classes and Code](#java-custom)
- [Maven Settings](#maven)
- [MUnit Support](#munit)
- [API Governance for REST APIs](#governance)
For more information, see [Known Issues](#known-issues) and [Compatibility](#compatibility).
#### DataWeave Expression Builder
Use the DataWeave expression builder when configuring your integrations and implementations from the
UI.
DataWeave is a programming language designed for transforming data. Most components in Mule
application flows use DataWeave expressions to select and transform messages (payload and
attributes) or Mule variables.
The DataWeave expression builder helps you configure fields of components that accept expressions
(**fx** fields). For each expression field, the feature provides an extra panel with the following
tabs:
- **Data** for selecting a value (payload, attributes, or a Mule variables)
- **Functions** for selecting DataWeave functions to use in your expressions
  Function documentation is available from this tab by mousing over a function and getting details,
  including parameter descriptions and examples.
- **Preview** for running the expression on sample data
In addition, you can use autocomplete from an expression (**fx**) field for a component to select
DataWeave functions from the Core module and other values accepted in this field.
For details, see
[Using DataWeave Expressions and Transformations in Anypoint Code Builder](../../anypoint-code-builder/int-configure-dw-expressions).
For more information about DataWeave and the Mule event structure, see
[DataWeave Overview](../../dataweave/latest/) and
[Mule Event Structure](../../mule-runtime/latest/about-mule-event).
#### Component Configuration Enhancements
Configure more of your integrations and implementations from the canvas UI. The configuration panel
for components adds:
- An **Input/Output** tab to existing tabs (**General**, **Advanced**, and **Notes**) for Mule event
  metadata from the payload, attributes, Mule variables
- Support for additional data types in the configuration fields:
  - File selectors
  - Passwords
  - Array (primitive types only)
  - Union for some configurable data sets
For examples, see
[Using DataWeave Expressions and Transformations in Anypoint Code Builder](../../anypoint-code-builder/int-configure-dw-expressions).
#### Support for Multiple Mule Runtime Versions with Java 17 or 11
Anypoint Code Builder now supports Mule runtime versions 4.4, 4.6, and 4.7 and compatible Java
versions (Java 11 or Java 17) to run Mule apps for your implementation and integration projects (see
[supported Mule and Java versions](#versions-mule-jdk)). In addition, when you create an integration
project from a template or example project in Anypoint Exchange, the asset search displays assets
set to use Mule 4.4 or higher, instead of 4.4 only.
Select the versions to run when creating or importing Mule applications in Anypoint Code Builder and
when scaffolding an API specification into an implementation project.
The following settings are new in this release:
- **Mule > Application: Default Mule Runtime And Java Versions**: Sets default Mule and Java
  versions for all projects.
- **Project Properties** tabs for setting and changing Mule runtime, Java, and connector versions in
  an implementation or integration project.
  This feature is useful for updating to the latest minor version or when importing projects that
  use unsupported versions.
- **Mule: Home Directory**: Set the home directory for Mule runtime and Java downloads.
  This setting replaces the runtime settings **Mule > Runtime: Mule Home** and **Mule > Runtime:
  Mule Runtimes Directory**, which are no longer present in the **Settings** tab. In addition, the
  IDE no longer uses the directory `${user.home}/muleRuntimes/` to store Mule runtime versions.
Anypoint Code Builder - Mule Runtime Extension (`salesforce.mule-dx-mule-runtime`) is removed from
Anypoint Extension Pack in this release. Instead of supplying a bundled runtime, the IDE provides an
interface for downloading and installing runtime versions to use in your projects.
To remove the runtime extension from VS Code, open the **Extensions** panel, click **Anypoint Code
Builder - Mule Runtime Extension**, and select **Uninstall**.
See [Version Settings for Mule, Java, and Connectors](../../anypoint-code-builder/int-versions) for
project and default version settings.
#### Custom Java Classes and Code
The Java module is now bundled into Anypoint Code Builder.
When you create a new Java class in a project, Anypoint Code Builder automatically adds the
necessary dependencies to the projectâ€™s `pom.xml` and the namespace and schema locations to the
configuration XML for the project.
New integration and implementation projects now add the directories `src/main/java` and
`/src/test/java` for your custom Java work.
For documentation, see
[Configure the Java Module Using Anypoint Code Builder](../../java-module/latest/configure-java-module-acb).
To use auto-complete from the application XML to find module configuration options and to display
lists of available Java classes and methods in a selected class, install
[Extension Pack for Java](https://marketplace.visualstudio.com/items?itemName=vscjava.vscode-java-pack)
from Microsoft to the IDE.
#### Maven Settings
To avoid changing any of your preferred Maven settings in `settings.xml`, Anypoint Code Builder now
creates a separate settings file, `acb_settings.xml`.
The setting **Mule: Home Directory**, in the **Settings** tab, configures the location of this file.
By default, the full path to the file is `{user.home}/AnypointCodeBuilder/maven/acb_settings.xml`.
For details, see
[Maven Settings in Anypoint Code Builder](../../anypoint-code-builder/ref-acb-maven).
#### MUnit Support
Anypoint Code Builder introduces limited support for testing with MUnit.
Run, modify, and create MUnit tests for your implementation and integration projects in Anypoint
Code Builder. Import projects that contain MUnit test files. Test configuration is supported through
the XML editor only at this time. For more information, see
[Testing Projects with MUnit](../../anypoint-code-builder/int-test-munit).
Some MUnit features supported by Anypoint Studio are not supported by Anypoint Code Builder in this
release.
#### API Governance for REST APIs
Anypoint Code Builder now supports API Governance for REST APIs:
- Check conformance status of a project.
- Add rulesets to your project.
  You can also remove rulesets, change ruleset versions, and review ruleset configurations.
- Run and re-run validations against your API specifications.
  For supported specifications, see [Compatibility](#compatibility).
- Monitor the progress of a validation.
- Fix conformance issues.
See
[Validating API Specifications Against Governance Rulesets](../../anypoint-code-builder/des-govern-api).
## April 19, 2024
Anypoint Code Builder updates the built-in Mule runtime engine to patch version `4.4.0-20240408`.
The Mule version is updated automatically in the cloud IDE but requires a manual update or
installation of the Anypoint Extension Pack in the desktop IDE.
- Extension pack version: 1.0.8
  To use this extension pack in the desktop IDE, see
  [Set up the Desktop IDE](../../anypoint-code-builder/start-acb#set-up-desktop).
- Cloud IDE version: 1.1.4
  This cloud IDE version runs the 1.0.8 extension pack.
For extension versions, see
[Change Log](https://marketplace.visualstudio.com/items/salesforce.mule-dx-extension-pack/changelog)
in the VS Code Marketplace.
For more information, see [Known Issues](#known-issues) and [Compatibility](#compatibility).
## February 14, 2024
Anypoint Code Builder releases new features in the Anypoint Extension Pack and the cloud IDE.
- Extension pack version: 1.0.7
  To use this extension pack in the desktop IDE, see
  [Set up the Desktop IDE](../../anypoint-code-builder/start-acb#set-up-desktop).
- Cloud IDE version: 1.1.3
  This cloud IDE version runs the 1.0.7 extension pack.
For extension versions, see
[Change Log](https://marketplace.visualstudio.com/items/salesforce.mule-dx-extension-pack/changelog)
in the VS Code Marketplace.
### Whatâ€™s New
The release introduces the following features:
- [Component Configuration Panel in the UI](#component-ui)
- [Integration Project Creation from Templates and Examples](#project-import)
- [API Design Project Improvements](#api-design-change)
- [Configuration XML File Creation Enhancement](#config-xml-creation)
#### Component Configuration Panel in the UI
Anypoint Code Builder introduces a configuration panel in the UI for components, such as connector
operations, within integration and implementation projects. This feature simplifies component
configuration.
The component configuration panel provides configuration options that are also available through the
configuration XML files for your projects. Some components and fields continue to require
configuration through the XML in this release. Continue to use XML for complex fields, identified as
read-only fields in the UI, and for global configurations, such as connection configurations.
You can open the configuration panel from the canvas or from a configuration XML file within your
project. See
[Add a Component to Your Project](../../anypoint-code-builder/int-create-integrations#add-components)
and
[Open a Component in the Canvas from the XML Editors](../../anypoint-code-builder/int-create-integrations#open-component-from-xml).
#### Integration Project Creation from Templates and Examples
Anypoint Code Builder adds the ability to import a template or example from Anypoint Exchange into
an integration project within Anypoint Code Builder. After importing, you can continue to develop
your integration. For information about templates and examples in Exchange, see
[Asset Types](../../exchange/asset-types).
For guidance with importing from Exchange, click the tab **Start with a Project Template or
Example** in the procedure
[Create an Integration Project](../../anypoint-code-builder/int-create-integrations#anchor-for-rns).
#### API Design Project Improvements
This release introduces improvements and simplifications to the design process:
- Import API design projects from Design Center into Anypoint Code Builder. For details, see
  [Import an API Specification from Design Center](../../anypoint-code-builder/des-create-api-specs#import-spec).
- Publish your API specifications and fragments to Anypoint Exchange without first syncing your code
  changes with the Anypoint source control management (SCM) system.
  Creating an API design project from scratch in Anypoint Code Builder no longer spawns a
  corresponding design project in Design Center or creates a connection to the Anypoint SCM. For
  details, see
  [Source Control for API Design Projects](../../anypoint-code-builder/des-designing-api-specs#anypoint-scm).
- Set a business group for your API design project when you publish to Exchange instead of when you
  create the design project. For example, see the steps in
  [Publish an API Spec to Exchange](../../anypoint-code-builder/des-publish-api-spec-to-exchange#publish-spec).
#### Configuration XML File Creation Enhancement
Anypoint Code Builder enables you to create one or more additional configuration XML files from
within your integration or implementation projects. This feature is useful for adding an
implementation for an interface. The feature also enables you to split complex project code into
more manageable pieces. For more information, see
[Create an Additional Configuration XML File](../../anypoint-code-builder/int-create-integrations#create-new-config).
For more information, see [Known Issues](#known-issues) and [Compatibility](#compatibility).
## December 6, 2023
Anypoint Code Builder releases a patch to Anypoint Extension Pack and the cloud IDE.
- Extension pack version: 1.0.6
  To use this extension pack in the desktop IDE, see
  [Set up the Desktop IDE](../../anypoint-code-builder/start-acb#set-up-desktop).
- Cloud IDE version: 1.0.3
  This cloud IDE version runs on the 1.0.6 extension pack.
The patch addresses the following issues:
<table><colgroup><col> <col></colgroup><thead><tr><th>Description</th><th>Issue</th></tr></thead><tbody><tr><td><div><div><p>When you open the IDE, the exception <code>dw-lang-server-language-0" java.lang.NoClassDefFoundError: org/jboss/shrinkwrap/resolver/api/maven/Maven</code> in the <strong>Mule DX Server</strong> logs no longer occurs because of an open workspace that contains a non-Mule project, such as an API spec project or other folders or files.</p></div></div></td><td><div><div><p>W-14268344</p></div></div></td></tr><tr><td><div><div><p>The issue <code>java.io.FileNotFoundException</code> no longer occurs due to attempted parsing of files that do not exist.</p></div></div></td><td><div><div><p>W-14254505</p></div></div></td></tr><tr><td><div><div><p>After scaffolding an API spec into an interface within an implementation project, the IDE no longer produces the syntax validation issue <code>Configuration type reference is not compatible (INVALID_CONFIG_REFERENCE)</code> within the configuration XML for <code>config-ref</code> attribute-value pairs. Previously affected components include <code><http:listener/></code>, <code><apikit:router/></code>, and <code><apikit:console/></code>.</p></div></div></td><td><div><div><p>W-14243529</p></div></div></td></tr><tr><td><div><div><p>A test connection no longer fails with the error <code>'Invalid Connection ElementDeclaration is declaring an extension: 'HTTP' that is not part of the session: '[]'</code> after you copy and paste an HTTP Listener configuration (<code><http:listener-config/></code>) into a new project.</p></div></div></td><td><div><div><p>W-14252415</p></div></div></td></tr></tbody></table>
For more information, see [Known Issues](#known-issues) and [Compatibility](#compatibility).
## October 19, 2023
Anypoint Code Builder releases a patch to the cloud IDE:
- 1.0.2 (Cloud IDE): The cloud IDE removes the proxy for security purposes. URLs that trigger flows
  in the cloud IDE through the proxy no longer work. To trigger locally hosted flows that use an
  HTTP listener, see
  [Triggering Flows in Your Development Environment](../../anypoint-code-builder/int-trigger-flows).
There are no changes to the desktop IDE, which remains version 1.0.5.
## October 16, 2023
Anypoint Code Builder releases these versions:
- 1.0.5 (Desktop IDE): Anypoint Code Builder for Desktop (desktop IDE) is generally available (GA)
  in this release.
- 1.0.1 (Cloud IDE): The cloud IDE for Anypoint Code Builder remains in open beta:
  > [!IMPORTANT] Any use of an Anypoint Code Builder IDE in its beta state is subject to the
  > applicable beta services terms and conditions, available from the cloud IDE.
The desktop IDE version 1.0.5 and cloud IDE version 1.0.1 both run on the same versions of the
Anypoint Code Builder extensions, described in
[Change Log](https://marketplace.visualstudio.com/items/salesforce.mule-dx-extension-pack/changelog),
and provide the same features.
To set up and gain access to the IDEs, see
[Getting Started with Anypoint Code Builder](../../anypoint-code-builder/start-acb).
### Whatâ€™s New
This release introduces:
- Anypoint Extension Pack version 1.0.5 for the desktop IDE on
  [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=salesforce.mule-dx-extension-pack)
- API fragment support for JSON Schema
  See
  [Supported Specification Languages for API Fragments](../../anypoint-code-builder/des-designing-api-specs#supported-fragment-languages).
## Open Beta
Prior to the Oct 16, 2023 release, MuleSoft released these open beta versions of Anypoint Code
Builder:
- [September 2023 (Open Beta)](#sept-2023)
- [August 2023 (Open Beta)](#aug-2023)
- [June 2023 (Open Beta)](#june-2023)
- [April 24, 2023 (Open Beta)](#april-24-2023)
- [April 2023 (Open Beta)](#april-2023)
### September 2023 (Open Beta)
This update to the open beta introduces Anypoint Code Builder for Desktop on Windows and new
features for desktop and cloud IDEs.
- Windows support on the desktop IDE. See [Compatibility](#compatibility).
- Hot deployments are supported for debugging Mule applications. See
  [Hot Deploy When Debugging](../../anypoint-code-builder/int-debug-mule-apps#hot-deploy).
- New export commands for packaging Mule applications within shareable and deployable JAR files. See
  [Exporting Mule Projects](../../anypoint-code-builder/int-export-mule-project).
### August 2023 (Open Beta)
This update to the open beta introduces Anypoint Code Builder for Desktop on MacOS and a new feature
for desktop and cloud IDEs.
- Anypoint Extension Pack on
  [Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=salesforce.mule-dx-extension-pack)
  to support API specification design (OAS 3 and RAML), API implementation, and integration
  development
  Install the _pre-release_version. Attempting to install the \_release_ version produces an error.
- Support for the Mac operating system running on Intel or ARM processors (see
  [Compatibility](#compatibility))
- Desktop and cloud IDE support for the following features:
  - Secure configuration properties in your integrations and API implementations (see
    [Defining and Securing Properties for a Mule Application](../../anypoint-code-builder/int-create-secure-configs))
  - Improvements to avoid reloading the IDE when unpacking the runtime for the first time
### June 2023 (Open Beta)
The update to the open beta for the web-based IDE introduces these features and improvements:
- Support for EU Cloud: EU Cloud users of Anypoint Platform can now use Anypoint Code Builder from
  their management plane.
  See [Getting Started with Anypoint Code Builder](../../anypoint-code-builder/start-acb) for more
  information.
- Synchronization between a local API specification and Mule project: You can now work on your API
  specification and its Mule project implementation simultaneously.
  Anypoint Code Builder enables you to scaffold your API specification into a Mule project without
  publishing it to Exchange. You can work on your Mule project, then edit the API specification, and
  re-scaffold it to reflect your new changes. Both API design and API implementation tasks are now
  synchronized. You can then publish your API specification and deploy your Mule project from there.
  See
  [Iteratively Design and Implement an API Specification](../../anypoint-code-builder/tut-local-api-specification)
  for more information.
- Updated UI canvas and code snippet support:
  - Directly import connectors from the canvas instead of using the dedicated command.
  - Use code snippets. See
    [Configuring Components](../../anypoint-code-builder/int-configure-components) for more
    information.
### April 24, 2023 (Open Beta)
The update to the open beta for the cloud IDE introduces a number of features and improvements:
- Anypoint Code Builder migrated to a new underlying architecture.
- The URL for your cloud IDE instance changed. You can get the new URL by launching the cloud IDE
  from the central page or checking the IDE details.
- Your session cookie changed, so you must update it when
  [pinging a locally deployed application](../../anypoint-code-builder/int-trigger-flows) from a
  REST client.
### April 2023 (Open Beta)
The update to the open beta for the cloud IDE introduces these features and improvements:
- Business group support enables you to control access to resources when working with assets from
  Anypoint Exchange.
- Search filters enable you to refine your search results when looking for an API asset from
  Anypoint Exchange. See
  [Filtering Search Results](../../anypoint-code-builder/imp-filter-search-results) for more
  information.
- The canvas UI enables you to add components to flows in your integration.
## Compatibility
<table><colgroup><col> <col> <col></colgroup><thead><tr><th>Application/Service</th><th>IDE</th><th>Version</th></tr></thead><tbody><tr><td><p>Anypoint Platform</p></td><td><p>Desktop IDE</p></td><td><p>US clouds, EU clouds, and these Anypoint Platform instances on Hyperforce: <a href="https://ca1.platform.mulesoft.com">Canada Cloud</a> and <a href="https://jp1.platform.mulesoft.com">Japan Cloud</a>. (Not supported by MuleSoft Government Cloud or Anypoint Platform PCE)</p></td></tr><tr><td><p>Anypoint Platform</p></td><td><p>Cloud IDE</p></td><td><p>US and EU clouds only</p></td></tr><tr><td><p>Anypoint Platform</p></td><td><p>Both IDEs-Agentforce for Anypoint Code Builder Generative Flows</p></td><td><p>US clouds, EU clouds, and these Anypoint Platform instances on Hyperforce: <a href="https://ca1.platform.mulesoft.com">Canada Cloud</a> and <a href="https://jp1.platform.mulesoft.com">Japan Cloud</a></p></td></tr><tr><td><p>API Governance</p></td><td><p>Both IDEs</p></td><td><p>Validations for REST API and AsyncAPI specs</p></td></tr><tr><td><p>CloudHub</p></td><td><p>Both IDEs</p></td><td><p>1.0 and 2.0 (for deployments to the Sandbox environment)</p></td></tr><tr><td><p>code-server</p></td><td><p>Cloud IDE</p></td><td><p>v4.17.1 (built-in)</p></td></tr><tr><td><p>DataWeave</p></td><td><p>Both IDEs</p></td><td><p>Bundled with Mule runtime engine (built-in)</p></td></tr><tr><td><p>Java</p></td><td><p>Both IDEs</p></td><td><p>Multiple versions supported. See <a href="#versions-mule-jdk">supported Mule and Java versions</a>.</p></td></tr><tr><td><p>Maven</p></td><td><p>Both IDEs</p></td><td><p>3.9.4 (built-in)</p></td></tr><tr><td><p>Mule runtime engine</p></td><td><p>Both IDEs</p></td><td><p>Multiple versions supported. See <a href="#versions-mule-jdk">supported Mule and Java versions</a>.</p></td></tr><tr><td><p>Operating system</p></td><td><p>Desktop IDE</p></td><td><p>Windows 11, Windows 10, macOS Intel and ARM (M1 or M2)</p></td></tr><tr><td><p>Visual Studio Code</p></td><td><p>Desktop IDE</p></td><td><div><div><p>Minimum version: 1.99.3<br>Tested versions:</p></div><div><ul><li><p>1.99.3 or later (macOS)</p></li><li><p>1.99.3 or later (Windows)</p></li></ul></div></div></td></tr><tr><td><p>Web browser</p></td><td><p>Both IDEs</p></td><td><p><a href="../../general/browser-support">Browser Support for Anypoint Platform</a></p></td></tr></tbody></table>
In Anypoint Code Builder, Mule applications for your implementation and integration projects are
compatible with the following Mule runtime engine (Mule) and Java versions:
Supported Mule and Java versions:
<table><colgroup><col> <col></colgroup><thead><tr><th>Mule runtime version</th><th>Java version</th></tr></thead><tbody><tr><td><p>Mule 4.11.x Edge</p></td><td><p>Java 17</p></td></tr><tr><td><p>Mule 4.10.x Edge</p></td><td><p>Java 17</p></td></tr><tr><td><p>Mule 4.9.x LTS</p></td><td><p>Java 17</p></td></tr><tr><td><p>Mule 4.8 Edge</p></td><td><p>Java 11, Java 17</p></td></tr><tr><td><p>Mule 4.6.x LTS</p></td><td><p>Java 11, Java 17</p></td></tr><tr><td><p>Mule 4.4</p></td><td><p>Java 11</p></td></tr></tbody></table>
Minor and major version changes to Mule require a manual update to your projects. Periodic Mule
patch updates (such as from Mule 4.8.2 to 4.8.3) to Mule versions already downloaded to your IDE
occur automatically when you log in to Anypoint Platform from the IDE.
> [!IMPORTANT] Starting May 18, 2026, publishing connectors and Mule plugins to Exchange requires
> `mule-extension-plugin` 1.9.0 or later. Update your plugin version before publishing new connector
> versions.
## Known Issues
For new known issues and workarounds for the February 6, 2025 release and later, see
[Salesforce Known Issues](https://help.salesforce.com/s/issues).
These known issues and workarounds from the December 9, 2024 release still apply to this release:
<table><colgroup><col> <col></colgroup><thead><tr><th>Limitation</th><th>ID</th></tr></thead><tbody><tr><td><div><div><p>When the desktop IDE launches for the first time, a corrupted dependency (<code>.m2\repository\net\minidev\accessors-smart\1.2\accessors-smart-1.2.pom</code>) can block the Anypoint Code Builder - Integration Extension when extracting the Mule runtime operation.<br><br>Workaround: Delete the dependency from <code>.m2\repository\net\minidev\accessors-smart</code>, and re-launch the IDE.</p></div></div></td><td><p>W-14047707</p></td></tr><tr><td><div><div><p>When launching the cloud IDE for the first time from Anypoint Code Builder, you must allow popups.</p></div></div></td><td><p>None</p></td></tr><tr><td><div><div><p>Previously configured sample data is overridden when selecting a component in the canvas UI.</p></div></div></td><td><p>W-16270847</p></td></tr><tr><td><div><div><p>There is no command to delete dependencies related to assets that you import from Exchange to an API design project.<br><br>Workaround: Remove the dependency from the <code>dependencies</code> node in the <code>exchange.json</code> file.</p></div></div></td><td><p>W-13822075</p></td></tr><tr><td><div><div><p>Moving the editors while searching for components from the UI canvas causes your search to be canceled.<br><br>Workaround:<br>Avoid rearranging your editors when using the component palette in the canvas.</p></div></div></td><td><p>W-13172200</p></td></tr><tr><td><div><div><p>Using autocompletion to create a parameter for the <code>value</code> field in the XML adds an extra <code>#[]</code> statement.</p></div></div></td><td><p>W-12444650</p></td></tr><tr><td><div><div><p>Autocompletion does not work properly when more than one connector has the same prefix.</p></div></div></td><td><p>W-10667510</p></td></tr><tr><td><div><div><p>Anypoint Connector for Apache Kafka (Apache Kafka Connector) does not display the <strong>Test Connection</strong> option.</p></div></div></td><td><p>W-12553536<a id="import-issues"></a></p></td></tr><tr><td><div><div><p>DataSense doesnâ€™t identify functions provided by a connector.</p></div></div></td><td><p>W-12448776</p></td></tr><tr><td><div><div><p>DataSense doesnâ€™t reflect array structures at the payloadâ€™s root level.</p></div></div></td><td><p>W-12263085</p></td></tr><tr><td><div><div><p>DataWeave doesnâ€™t recognize the larger context to which samples belong. So DataWeave requests sample data for all scripts within a single component.</p></div></div></td><td><p>None</p></td></tr><tr><td><div><div><p>DataWeave validations to produce <code>Invalid input</code> errors on some multiline scripts because Anypoint Code Builder does not decode Unicode characters for new lines in XML (<code>&#10;</code>). This limitation does not interrupt the correct execution of your Mule application.</p></div></div></td><td><p>W-11750473</p></td></tr><tr><td><div><div><p>Updates to metadata in one component donâ€™t trigger metadata validation in subsequent components. This issue causes Anypoint Code Builder to display potential issues in the subsequent components.</p></div></div></td><td><p>W-12215165</p></td></tr><tr><td><div><div><p>The Batch Job processor is not supported by the UI canvas or through auto-complete in the configuration XML.</p></div></div></td><td><p>None</p></td></tr><tr><td><div><div><p>When scaffolding a GraphQL or AsyncAPI specification on Windows, an empty Mule configuration file with the name of the project is created in addition to the <code>flows.xml</code> file.<br><br>Workaround: Delete the empty file.</p></div></div></td><td><p>W-15757808</p></td></tr><tr><td><div><div><p>When source validation is enabled, AsyncAPI messages are invalid if <code>mediaType</code> doesnâ€™t match the specification.</p></div></div></td><td><p>W-16663560</p></td></tr><tr><td><div><div><p>When source validation is disabled, AsyncAPI messages are sent downstream without transforming <code>mediaType</code>.</p></div></div></td><td><p>W-16663585</p></td></tr><tr><td><div><div><p>Source validation is not working with the Salesforce platform events <code>application/xml</code> content type.</p></div></div></td><td><p>W-16756836</p></td></tr></tbody></table>
## See Also
- [Salesforce Help](https://help.salesforce.com)
- [MuleSoft Services](https://www.mulesoft.com/support-and-services)
- [Product Versioning and Back Support Policy](https://www.mulesoft.com/legal/versioning-back-support-policy)
- [CloudHub](../../cloudhub/)
```