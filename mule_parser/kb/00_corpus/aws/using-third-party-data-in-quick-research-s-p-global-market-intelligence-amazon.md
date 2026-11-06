# Using third party data in Quick Research (S&P Global Market Intelligence) - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/spgi-market-intelligence.html](https://docs.aws.amazon.com/quick/latest/userguide/spgi-market-intelligence.html)

---

Using S&P Global's MCP Server for the Kensho LLM-Ready API, customers can unlock S&P Global's trusted data and insights using natural language queries, enabling financial professionals to answer complex financial questions and get fast, reliable answers grounded in reliable data from S&P Global.

Query a comprehensive range of S&P Global datasets, including S&P Capital IQ Financials, Market Data, earnings call transcripts, and global securities information. This powerful connector is specifically designed to save time and resources for engineering, product, and business teams in financial services by streamlining access to critical company information, detailed financial statements, historical market data, and comprehensive global securities coverage.

Key capabilities include:

- **Compare Company Financials:**Analyze and benchmark financial performance across companies and time periods. Example: "Compare the gross margins and EBITDA trends for Amazon, Google, and Meta over the past 5 years" to identify competitive positioning and operational efficiency trends.
- **Summarize Earnings Calls:**Extract key insights from earnings transcripts and management commentary. Example: "Summarize the key takeaways from Apple's latest earnings call, focusing on guidance and capital allocation" to quickly understand strategic direction and financial priorities.
- **Deep Financial Research Reports:**Generate comprehensive competitive analysis and market research reports. Example: "Generate a comp table for software companies with $1B+ revenue and 20%+ growth rates" to identify investment opportunities and market positioning.
- **Develop Due Diligence Briefs:**Develop a due diligence brief in a fraction of the time it would normally take – pulling key financials, generating comps tables, benchmarking peers, and flagging risks in minutes. Example: "Pull key financials for Tesla, generate a peer benchmark analysis, and flag potential risks for an investment committee presentation" to support informed decision-making.

## Setting up the integration

            This integration requires a subscription to S&P Global Market Intelligence. S&P will need to authorize your account and someone with an Enterprise subscription to Quick (typically an admin or whomever is responsible for your organization's access to this data) will need to set up the integration. The instructions below describe these steps in more detail.

To use S&P Global Market Intelligence in Quick, you (or someone from your organization) will need to:

- Contact S&P Global to ensure your organization subscribes to S&P Global Market Intelligence data. To learn more about how to access S&P Global data via the Kensho LLM-ready API, email - [commercial@kensho.com](mailto:commercial@kensho.com)for free trials and pricing, or read more- [here](https://docs.kensho.com/llmreadyapi/overview).
- 
                    Create a Quick integration for S&P Global Market Intelligence. - Open the Research page and select - **New Research**.
- In the - **Research Materials**section, find- **Third party data**and select- **Browse**to display a list of supported third party data integrations.
- Find the integration in the list and select - **Connect**. This will display a pop-up with a summary of these setup steps. Select- **Continue**.
- Provide a name and description for the integration. You can enter anything you like here to help you identify the integration. 
 
- Share the integration with anyone else at your organization who should have access. 

## Using the integration in Quick Research

            These instructions assume that you already set up the integration (see details above), or someone at your organization set up the integration and shared it with you.

To use this integration in Quick Research:

- Navigate to the Quick Research page and select - **New Research**.
- On the left-hand side, under - **Research Materials**, there is a section called- **Third Party Data**. Select the- **Browse**button to display a list of supported integrations.
- If you need to sign in, there will be a - **Sign In**button in the status column. Selecting this button will open a new tab where you can sign in. After you have signed in, navigate back to the tab with Quick Research.
- Select the check box for the integration you want to use.