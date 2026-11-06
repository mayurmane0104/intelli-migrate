# Export and import automations - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/export-import-automations.html](https://docs.aws.amazon.com/quick/latest/userguide/export-import-automations.html)

---

You can use the import and export feature in Amazon Quick Automate to share and migrate automation versions across automation groups, AWS accounts, and AWS Regions. Use this feature to promote automations from development to production environments, create backups, or share automations with other teams.

When you export an automation version, Amazon Quick Automate packages it into a secure, encrypted link that you can use to transfer the automation between environments. The export bundle contains the following:

- The automation workflow 
- Runtime configuration settings 
- Process step descriptions and metadata 

###### Note

Dependencies such as action connectors, credentials, and task queue configurations are not included in the export bundle. You must configure these separately in the destination environment.

## Use cases

        The import and export feature supports the following use cases:

- Move tested automations from development to production accounts. 
- Deploy automations across different AWS Regions. 
- Create point-in-time snapshots of automation versions for disaster recovery. 
- Share automation versions across different automation groups within the same account. 

## Prerequisites

        Before you import or export automations, make sure that you have the following:

- Access to Amazon Quick Automate. 
- Appropriate permissions to create and manage automations in both the source and destination environments. 
- Amazon Quick Automate enabled in both the source and destination AWS accounts (for cross-account transfers). 

## Export an automation

        To export an automation version, complete the following steps.

- Navigate to your automation in - **Amazon Quick Automate**.
- Choose the actions menu (⋮) next to - **Edit automation**.
- Choose - **Export version**.
- Choose the version from the dropdown list and wait for the link to be generated. 
- Choose - **Copy link**or copy the link manually.

Amazon Quick Automate generates a secure, pre-signed download link for your automation. Amazon Quick Automate encrypts the bundle by using AWS KMS with envelope encryption to protect your automation content.

### Export link validity

Export links are valid for 12 hours from the time of creation. After this period, the link expires and you must generate a new export link. You can reuse the same export link multiple times within the 12-hour window without creating a new export.

## Import an automation

        To import an automation version, complete the following steps.

- Navigate to the destination automation group and create a blank automation. 
- Choose the actions menu (⋮) next to - **Edit automation**.
- Choose - **Import version**.
- Paste the exported link (the pre-signed URL that you received during export). 
- Choose - **Start**.

## Considerations

        - You can export one automation version per operation. 
- Action connectors, credentials, and other dependencies are not included in the export. You must configure these separately in the destination environment. 
- For cross-account transfers, both the source and destination accounts must have Amazon Quick Automate enabled.