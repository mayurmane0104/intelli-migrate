# Using third party data in Quick Research (IDC) - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/idc.html](https://docs.aws.amazon.com/quick/latest/userguide/idc.html)

---

The IDC Connector integrates IDC's industry-leading technology research and market intelligence directly into Amazon Quick Research, enabling business users to generate deeper, more credible insights in minutes. Through this integration, Quick Research users can securely access IDC's trusted data — including market forecasts, vendor assessments, and emerging technology analyses — alongside their own enterprise data and public web sources.

## Setting up the integration

            This integration requires a subscription to IDC. IDC will need to enable API access for your account, and someone with an Enterprise subscription to Quick (typically an admin or whomever is responsible for your organization's subscription to IDC) will need to set up the integration and knowledge base. The knowledge base can then be shared with others at your organization who should have access. The instructions below describe these steps in more detail.

###### Important

Creating an IDC knowledge base incurs storage and indexing costs. You should only create one IDC knowledge base for your organization to avoid unnecessary costs. To avoid users creating duplicate knowledge bases, we recommend not sharing the client ID and client secret with anyone else.

To use IDC in Quick, you (or someone from your organization) will need to:

- Contact IDC to enable API access at - [https://www.idc.com/amazonquickresearch](https://www.idc.com/amazonquickresearch). IDC will give you a client id and client secret.
- 
                    Create an integration for IDC: - Open the Research page and select - **New Research**.
- In the - **Research Materials**section, find- **Third party data**and select- **Browse**to display a list of supported third party data integrations.
- Find the integration in the list and select - **Connect**. This will display a pop-up with a summary of these setup steps. Select- **Continue**.
- Provide a name and description for the integration. 
- Use the client id and client secret you received from IDC. 
 
- Next, you will be prompted to create a knowledge base. This step could take several hours, depending on how much IDC data needs to be ingested and indexed. 
- To share the knowledge base with others, scroll to the top of the Integrations page, select the menu icon for IDC, and select - **Share**. You can share with individual users or groups. Make sure you only share the knowledge base with users who should have access to IDC data.

## Using the integration in Quick Research

            These instructions assume that you already set up the integration and knowledge base (see details above), or someone else did this and shared it with you.

To use this integration in Quick Research:

- Navigate to the Quick Research page and select - **New Research**.
- On the left-hand side, under - **Research Materials**, there is a section called- **Third Party Data**. Select the- **Browse**button to display a list of supported integrations.
- Select the check box for the integration you want to use.