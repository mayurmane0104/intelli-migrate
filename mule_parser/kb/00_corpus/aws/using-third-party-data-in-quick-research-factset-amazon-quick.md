# Using third party data in Quick Research (FactSet) - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/factset.html](https://docs.aws.amazon.com/quick/latest/userguide/factset.html)

---

Access FactSet's trusted equity prices, fundamentals, events, news, transcripts, pricing and consensus estimates - delivered seamlessly for AI-driven insights. With comprehensive coverage and reliable data, FactSet empowers smarter financial analysis, decision-making, and innovation.

- **Global Prices**- End-of-day pricing data, returns, corporate actions, dividends, and shares outstanding for global equities
- **Fundamentals**- Company financial statements, ratios, and business/geographic segment data from regulatory filings
- **Consensus Estimates**- Earnings estimates, surprise data, and buy/hold/sell ratings consensus
- **Transcripts**– Corporate event data and corresponding transcripts
- **StreetAccount News**– Curated, real-time market-moving news and summaries

## Setting up the integration

            This integration requires a subscription to FactSet. FactSet will need to authorize your account and someone with an Enterprise subscription to Quick (typically an admin or whomever is responsible for your organization's subscription to FactSet data) will need to set up the integration.

The integration can then be shared with others at your organization who should have access. The instructions below describe these steps in more detail.

To use FactSet in Quick, you (or someone from your organization) will need to:

- Contact FactSet to get access at - [AWS.QR.Partnership@factset.com](mailto:AWS.QR.Partnership@factset.com).
- 
                    Create a Quick integration for FactSet. - Open the Research page and select - **New Research**.
- In the - **Research Materials**section, find- **Third party data**and select- **Browse**to display a list of supported third party data integrations.
- Find the integration in the list and select - **Connect**. This will display a pop-up with a summary of these setup steps. Select- **Continue**.
- Enter a name and description. 
- For the client ID, provide the client ID you got from FactSet. 
- For the other authentication-related fields you can use the suggestions visible below each input field. 
 
- Share the integration with anyone else at your organization who should have access. 

## Using the integration in Quick Research

            These instructions assume that you already set up the integration (see details above), or someone at your organization set up the integration and shared it with you.

To use this integration in Quick Research:

- Navigate to the Quick Research page and select - **New Research**.
- On the left-hand side, under - **Research Materials**, there is a section called- **Third Party Data**. Select the- **Browse**button to display a list of supported integrations.
- If you need to sign in, there will be a - **Sign In**button in the status column. Selecting this button will open a new tab where you can sign in. After you have signed in, navigate back to the tab with Quick Research.
- Select the check box for the integration you want to use.