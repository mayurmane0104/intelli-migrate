# Document history for the Amazon Quick User Guide - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html](https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html)

---

This page describes changes to the *Quick User Guide*. For
		notifications about these documentation changes, subscribe to the RSS feed using the link
		near the top of this page. 

To find out what's new in Quick, see [What's New with Analytics](https://aws.amazon.com/about-aws/whats-new/analytics/?whats-new-content.sort-by=item.additionalFields.postDateTime&whats-new-content.sort-order=desc&awsf.whats-new-products=general-products%23amazon-quicksight). To find out about changes to the Quick
		service, sign up for the 

[Quick newsletter](https://pages.awscloud.com/NewsletterSignup.html).

New Amazon Quick releases appear in different AWS Regions over a period of time,
		beginning with the first Region on the initial release date. Documentation is released in
		coordination with this process. If you have questions, contact [AWS Support](https://aws.amazon.com//premiumsupport/) or your technical account
		manager. 

###### Note

The following table describes important changes in each *Amazon Quick User Guide* release since March 4, 2019. 

| Change | Description | Date | 
|---|---|---|
| OneDrive knowledge base admin-managed setup | Added admin-managed connection support for the Microsoft OneDrive
					knowledge base connector, including service credentials setup with
					AWS KMS signing, certificate-based authentication, and tenant-wide
					crawling of all users' OneDrive content. Admin-managed OneDrive
					knowledge bases always enforce document-level access control (ACL)
					with real-time verification at query time. For more information, see
					 | June 1, 2026 | 
| Web search processed in-Region for Sydney and Tokyo | Updated cross-Region web search documentation to reflect that web search queries originating in Asia Pacific (Sydney) and Asia Pacific (Tokyo) are now processed in the originating Region and are no longer routed to US East (N. Virginia). For more information, see  | May 29, 2026 | 
| VPC support for MCP integration | You can now connect Amazon Quick MCP integrations to private MCP
					servers that are reachable from a virtual private cloud (VPC) by
					selecting a Amazon Quick VPC connection during connector setup. The
					OAuth endpoints used by the MCP server must remain reachable over
					the public internet. Added troubleshooting guidance for connector
					creation, VPC connection issues, and Microsoft Entra ID errors. For
					more information, see  | May 29, 2026 | 
| Updated HubSpot integration documentation | Restructured the HubSpot integration topic to follow the
					built-in action connector format. The topic now covers
					prerequisites, account verification, account configuration,
					Amazon Quick setup, and troubleshooting. The HubSpot action
					connector reads CRM data, including contacts, companies, deals,
					and tickets, and authenticates with a custom OAuth app. For more
					information, see  | May 28, 2026 | 
| Clarified IAM permissions for DeleteAccountSubscription | Clarified that the  | May 27, 2026 | 
| Preview extensions for Microsoft 365 | Added preview extension documentation for Excel, Word, and PowerPoint with simplified deployment through the Microsoft 365 admin center. For more information, see  | April 28, 2026 | 
| New action connectors | Added action connector documentation for Airtable, Dropbox, Google Analytics, Google Calendar, Google Docs, Google Drive, Google Meet, Google Sheets, Google Slides, Gmail, QuickBooks, and Zoom. Updated existing Slack and Outlook action connectors. For more information, see  | April 28, 2026 | 
| Free and Plus account documentation | Added documentation for Amazon Quick Free and Plus accounts created at quick.aws.com, including signup, plans, user management, billing, and account administration. For more information, see  | April 28, 2026 | 
| Document and visual creation | Added documentation for creating documents and visuals including Word, Excel, PowerPoint, PDF, and infographics directly from chat conversations. For more information, see  | April 28, 2026 | 
| Build web applications with apps in Amazon Quick | Added documentation for apps in Amazon Quick, a feature that lets you build, publish, and share interactive web applications using natural language. For more information, see  | April 28, 2026 | 
| Amazon Quick on desktop | Added documentation for the Amazon Quick desktop application for macOS and Windows, including local file access, activity feed, scheduled agents, system tools, MCP servers, knowledge graph, and settings. For more information, see  | April 28, 2026 | 
| Visier integration | Added documentation for the Visier people analytics integration,
					which connects to Visier through MCP server connectivity. You can
					query workforce data, analyze headcount trends, assess retention
					health, and generate workforce briefings. For more information, see
						 | April 22, 2026 | 
| Spaces file size and storage limit increase | Increased the file upload size limit for Spaces to 500 MB for PDF,
					Word, and PowerPoint files (50 MB for other file types), and
					increased the total space storage limit from 1 GB to 10 GB. For more
					information, see  | April 21, 2026 | 
| Confluence knowledge base document-level access controls | Added document-level access control (ACL) support for the
					Atlassian Confluence Cloud knowledge base connector. Includes
					Atlassian admin credentials setup, real-time permission
					verification at query time, and end-user sign-in flow. For more
					information, see  | April 21, 2026 | 
| SharePoint knowledge base admin-managed setup | Added admin-managed connection support for the SharePoint Online
					knowledge base connector, including service credentials setup (2LO) with
					AWS KMS signing, certificate-based authentication, document-level
					access control (ACL) with real-time verification, Sites.Selected
					least-privilege permissions, and specific SharePoint path support.
					For more information, see  | April 16, 2026 | 
| Knowledge base and data source sharing | Added support for sharing admin-managed SharePoint and Google
					Drive knowledge bases with co-owners, and sharing data source
					connections with other users. For more information, see  | April 16, 2026 | 
| Index usage monitoring | Added index usage logs ( | April 16, 2026 | 
| Incremental refresh support for datasets in the new data preparation experience | You can now incrementally refresh SQL-based SPICE datasets
					that were created in the new data preparation experience. For more information, see
						 | April 15, 2026 | 
| ServiceNow integration documentation update | Rewrote the ServiceNow integration documentation with detailed setup
					instructions for both user authentication (OAuth authorization code) and
					service authentication (client credentials), a complete list of available
					actions derived from the ServiceNow REST API, and a new limitations and
					troubleshooting section. For more information, see
					 | March 30, 2026 | 
| Fine-grained ACL support for Google Drive knowledge base | Added admin-managed connection support for the Google Drive knowledge base
					connector, including Google Workspace configuration with 2-legged OAuth (2LO)
					and document-level access control list (ACL) crawling. For more information, see
						 | March 30, 2026 | 
| Updated Quick Research documentation | Updated Quick Research documentation to reflect current UI changes,
					including research mode options (Fast and Deep), updated research objective
					guidance, revised button labels, and added third-party data sources as a
					research material type. For more information, see  | March 26, 2026 | 
| New Relic integration | Added New Relic integration documentation with setup instructions,
					available actions, and troubleshooting. For more information, see  | March 26, 2026 | 
| Region expansion for Tokyo, Frankfurt, and London | Updated regions documentation to reflect full Amazon Quick support in Tokyo
					(ap-northeast-1), Frankfurt (eu-central-1), and London (eu-west-2). Consolidated
					cross-Region inference (CRIS) documentation into the regions page with updated
					inference boundaries for AU-CRIS, JP-CRIS, EU-CRIS, and US-CRIS geographies,
					and added web search regional availability details. For more information, see
						 | March 24, 2026 | 
| New custom permissions for Spaces and Chat Agents | Added three new custom permission features: Create Spaces, Share Spaces,
					and Share Chat Agents. For more information,
					see  | March 24, 2026 | 
| New Amazon CloudWatch metrics for Amazon Quick index capacity | Added two new Amazon CloudWatch metrics for monitoring Amazon Quick index billing:
					 | March 24, 2026 | 
| Google Drive integration | Refactored the Google Drive knowledge base integration documentation | March 20, 2026 | 
| Embed custom chat agents | Added documentation for embedding custom chat agents on external websites,
					including the process for allowing hosting domains and generating embed code. For
					more information, see  | March 19, 2026 | 
| Custom permissions update | Updated custom permissions documentation with new parent capabilities (Scenarios,
					Stories, Topics), new features (Edit Visual with AI, Build Calculation with AI,
					Create Executive Summary, Knowledge Base create/update and sharing), and an Action
					Connectors section documenting per-connector permissions. For more information,
					see  | March 19, 2026 | 
| Quick Automate actions update | Updated Amazon Quick Automate documentation for the Data tables, Excel, Browser, Custom Agent, REST API, Code, and AWS Integrations action categories. | March 18, 2026 | 
| Atlassian Jira Cloud integration | Added dedicated Atlassian Jira Cloud integration documentation with validated
					OAuth scopes and a complete actions table. For more information, see  | March 18, 2026 | 
| Atlassian Confluence Cloud integration | Refactored the Atlassian Confluence Cloud integration documentation with shared Atlassian OAuth modules for a consistent setup experience. | March 17, 2026 | 
| Namespace isolation and administrative console clarification | Clarified the difference in permission models between the Amazon Quick end-user
					console and the administrative console for namespace isolation. For more information,
					see  | March 16, 2026 | 
| MCP integration documentation | Rewrote the Model Context Protocol (MCP) integration topic with an MCP protocol
					overview, OAuth discovery flow documentation (RFC 9728), and shared Dynamic Client
					Registration (DCR) concepts. For more information, see  | March 16, 2026 | 
| Web Crawler VPC support | Added VPC support, sitemap discovery, and JavaScript navigation troubleshooting
					to the web crawler integration documentation. For more information, see  | March 13, 2026 | 
| Managing shared folders custom permission | Added documentation for the managing shared folders custom permission. For more
					information, see  | March 12, 2026 | 
| Chat user preferences | Added a user preferences section to the chat documentation for managing display
					and notification preferences in Amazon Quick. For more information, see  | March 11, 2026 | 
| Microsoft 365 integration guides | Rewrote the Microsoft Outlook, SharePoint, and Teams integration guides with a consistent structure that includes full Microsoft Entra setup instructions, permission tables with descriptions, and correct OAuth scopes. | March 10, 2026 | 
| Conversation retention period update | Updated the chat conversation retention period from 30 days to 90 days. For more
					information, see  | March 5, 2026 | 
| Amazon S3 ACL documentation | Added document-level access control list (ACL) documentation for the Amazon S3
					integration and a best practices guide for managing ACLs in knowledge bases. For
					more information, see  | March 2, 2026 | 
| Asia Pacific (Malaysia) Region support | Added the Asia Pacific (Malaysia) ap-southeast-5 Region to the list of supported
					Amazon Quick Sight Regions, including the API endpoint and IP address range. For more
					information, see  | March 1, 2026 | 
| Quick Flows vs Quick Automate comparison | Added a comparison section to the automations landing page to help users choose
					between Amazon Quick Flows and Amazon Quick Automate based on their workflow needs. For more information,
					see  | February 27, 2026 | 
| TLS 1.2 MySQL version requirement | Documented the requirement for MySQL version 5.7.28 or later to support TLS 1.2 connections for MySQL data sources. | February 26, 2026 | 
| ApproveFlowShareRequests custom permission | Added the ApproveFlowShareRequests custom permission, which controls whether
					users can approve requests to share flows. For more information, see  | February 26, 2026 | 
| Space extracted text limits | Updated the extracted text limits for CSV and Excel files in spaces. | February 23, 2026 | 
| Knowledge base file size limit increase | Increased the file size limit for standard text documents in knowledge bases from 50 MB to 500 MB. | February 16, 2026 | 
| Automations usage metrics | Added a section for tracking Quick Flows, Quick Automate, and Amazon Quick Research usage hours in the usage metrics documentation. | February 6, 2026 | 
| SPICE capacity updates | Updated SPICE capacity and dataset size documentation to reflect increased limits. | February 2, 2026 | 
| Embedding and row-level security guidance | Added security guidance for embedded analytics to warn against AllowedEmbeddingDomains bypass vulnerabilities. Added guidance for using row-level security (RLS) in multi-tenant architectures. | January 27, 2026 | 
| CSV and Excel file size limits | Updated the file size limits for CSV and Excel uploads to 10 MB. | January 27, 2026 | 
| Extension access with Okta and IAM Identity Center | Updated extension setup instructions for Microsoft Word, Slack, and Teams to
					support Okta as an identity provider with IAM Identity Center. For more information, see  | January 26, 2026 | 
| AgentHours vended logs | Updated Quick vended logs documentation to include the AgentHours log type for tracking agent usage. | January 6, 2026 | 
| New integrations and PagerDuty advance | Added individual integration pages for 10 new MCP-based services and PagerDuty
					advance integration. Updated the supported integrations table and action connector
					APIs. For more information, see  | January 5, 2026 | 
| User-driven license upgrades | Added documentation for user-driven license upgrades, which allow end users to
					request license tier changes. For more information, see  | December 29, 2025 | 
| Flows in browser extension | Added documentation for using Amazon Quick Flows in the browser extension. For more
					information, see  | December 15, 2025 | 
| Add IAM Identity Center support for extensions | Added documentation for adding Amazon Quick extensions to Microsoft Word, Microsoft Office, Microsoft Teams, and Slack with accounts that 
					use IAM Identity Center. For more
					information, see  | November 19, 2025 | 
| New data preparation experience | Added documentation for the new visual data preparation experience in Amazon Quick Sight. For more
					information, see  | October 20, 2025 | 
| New Amazon Quick capabilities | Amazon Quick provides an integrated suite of AI-powered analytics, automation, and research tools that transcend traditional business intelligence. 
 
 
 
 
 
 
 
 
 
 | October 9, 2025 | 
| Amazon QuickSight rebrands to Amazon Quick | Amazon QuickSight has been rebranded to Amazon Quick, expanding from a standalone business intelligence service to a comprehensive analytics and AI platform. QuickSight continues as Amazon Quick Sight, a core component within the Quick ecosystem. Amazon Quick Sight retains existing functionality including interactive data visualization, SPICE in-memory analytics, embedded analytics, and dashboard sharing. All existing QuickSight APIs, SDKs, and integrations continue to work without changes. | October 9, 2025 | 
| Font customization | Authors can now customize fonts for data labels and axes in supported charts, in addition to the previously supported font customizations for visual titles, subtitles, and legends, as well as table and pivot table headers. | October 6, 2025 | 
| Google Sheets data source | You can now create datasets using a Google Sheets data source. Admins will need to perform a one-time setup to enable Google Sheets as a data source. | September 27, 2025 | 
| Q&A null support | Q&A now supports comprehensive support for null value handling, enabling users to create more sophisticated analyses and answer complex business questions. | September 18, 2025 | 
| Interactive Highchart features | Highchart visualizations now support custom actions, highlighting, and custom field color consistencies, allowing you to create interactive and visually cohesive charts that integrate seamlessly with other visuals. | September 2, 2025 | 
| Calculated fields limitation increase | The number of limits for calculated fields in an analysis has increased from 200 to 500. For more information, see  | August 15, 2025 | 
| Apache Impala data source | You can now create datasets using an Apache Impala data source. | August 1, 2025 | 
| Improve Q&A accuracy with custom instructions | Authors can now curate reponses to questions by adding domain-specific knowledge that cannot be captured through a topic's metadata settings. This ensures more accurate, relevant, and tailored answers that are better suited for business needs. | July 18, 2025 | 
| New topic: Trusted identity propagation support with Athena data sources | Added information about using trusted identity propagation with QuickSight and Athena. For more information, 
					see  | June 30, 2025 | 
| 2 billion row SPICE datasets | QuickSight now supports SPICE datasets that contain up to 2 billion (2,000,000,000) rows. For more information, see  | June 30, 2025 | 
| Topic Permissions | Authors can now manage permissions for dashboards and their linked topics from a single location. Control topic viewer access directly from a dashboard's sharing preferences, eliminating the need to manage permissions in multiple locations. | April 18, 2025 | 
| Sheet Highlighting | Added the ability to highlight specific data points across visuals in a sheet. When you select or hover over a data point on a visual, related data across other visuals will stand out, while unrelated data is dimmed. | April 11, 2025 | 
| Updated topic: Opting out of Amazon Q in Quick | Added additional information and guidance for opting out of Amazon Q in Quick. For more
					information, see  | April 8, 2025 | 
| Enable Generative BI features in embedded dashboards and consoles | Added documentation for adding executive summaries to embedded dashboards, and
					adding executive summaries, data stories, authoring, and Q&A to embedded
					consoles. For more information, see  | March 31, 2025 | 
| Customize alert emails | Previously, the custom email template in your QuickSight account only
					affected dashboard report and pixel perfect report emails. Now, it also customizes
					alert emails. For more information, see  | March 31, 2025 | 
| Rules Dataset flag | A Rules Dataset flag has been implemented to distinguish permission datasets used for row-level security from regular datasets. | March 28, 2025 | 
| Publish a previous version of a dashboard | You can now revert back to a previous version of a dashboard by searching for it under
				the dashboard's  | March 28, 2025 | 
| Scenarios general availability | Updated the scenarios documentation to support its general availability
					release. For more information, see  | March 25, 2025 | 
| New Region | Amazon QuickSight is now available in the Europe (Spain) (eu-south-2) Region.
					For more information, see  | March 11, 2025 | 
| Dashboard Q&A experience | Amazon QuickSight authors can now to turn on the Q&A experience directly from
					their dashboards in one click without the need to create a topic in
					QuickSight. For more information, see  | January 31, 2025 | 
| Unique key configuration | Amazon QuickSight authors can now configure a unique key column to a
					QuickSight dataset during data preparation. For more information, see
						 | December 19, 2024 | 
| Amazon QuickSight scenarios | Amazon QuickSight Pro users can now use Amazon Q in Quick to create scenarios to analyze
					complex business problems with simple natural language. For more information,
					see  | December 4, 2024 | 
| Augmenting Amazon QuickSight insights with Amazon Q Business | Amazon QuickSight account admins can now connect their QuickSight account to
					Amazon Q Business to augment insights with unstructured data sources. For more
					information, see  | December 3, 2024 | 
| Prompted reports | Amazon QuickSight authors can now create prompts on pixel-perfect reports to allow
					dashboard users to filter data in on-demand and scheduled reports. For more
					information, see  | November 22, 2024 | 
| New visual type: layer map | Amazon QuickSight now supports layer map visuals. For more information, see  | November 22, 2024 | 
| New visual type: image component | You can now add images to QuickSight dashboards and analyses with image
					component visuals in Amazon QuickSight For more information, see  | November 22, 2024 | 
| New visual type: Highcharts visual | Amazon QuickSight authors can now configure Highcharts visuals in
					QuickSight. For more information, see  | November 22, 2024 | 
| Import visual public preview | (Public preview) Amazon QuickSight authors can now import QuickSight visuals
					from one dashboard or analysis to a new analysis that has access permissions.
					For more information, see  | November 22, 2024 | 
| Font customization | Amazon QuickSight dashboard viewers can now schedule their own dashboard reports
					for themselves. For more information, see  | November 22, 2024 | 
| Font customization | Amazon QuickSight authors can now customize the font, font size, and font color of
					visual titles, subtitles, legends, headers, and cells. For more information, see
						 | November 22, 2024 | 
| Cross-Region inference with Amazon Q in Quick | Amazon Q in Quick now supports cross-Region inferencing. For more information, see  | November 21, 2024 | 
| Create a custom brand in Amazon QuickSight | Amazon QuickSight account admins can now customize their application's
					branding and visual theme to align with their organization's guidelines.
					For more information, see  | November 14, 2024 | 
| Connect to Starburst with OAuth client credentials | You can now use OAuth client credentials to connect your
					Amazon QuickSight account with Starburst through the QuickSight APIs. For more
					information, see  | November 8, 2024 | 
| Connect to Snowflake with OAuth client credentials | You can now use OAuth client credentials to connect your
					Amazon QuickSight account with Snowflake through the QuickSight APIs. For more
					information, see  | November 8, 2024 | 
| Subfolders for restricted shared folders | Assets that are located in a QuickSight restricted folder can now be
					moved within the restricted folder tree into one or more subfolders. For more
					information, see  | October 15, 2024 | 
| Show an apply button | QuickSight authors can now add an  | September 27, 2024 | 
| Data story peronalization | Amazon Q in Quick now leverages user location and job-related information from your IAM Identity Center
					instance to generate personalized data stories that are more relevant to authors
					and readers. For more information, see  | September 27, 2024 | 
| Shared view for embedded dashboards | QuickSight developers can now use the Amazon QuickSight Embedding SDK
					(version 2.8.0 and higher) to allow readers of embedded dashboards to receive
					and distribute shareable links to their view of an embedded dashboard. For more
					information, see  | August 23, 2024 | 
| 5 new regions | Amazon Q in Quick is now available in 5 new opt-in Regions: Asia Pacific (Mumbai), Canada
					(Central), Europe (Ireland), Europe (London), and South America (São Paulo). For
					more information, see  | August 9, 2024 | 
| Nested filters | You can now apply nested filters to QuickSight analyses. For more
					information, see  | August 1, 2024 | 
| Joined datasets in SPICE | The size limit for secondary tables of joins for datasets that are stored in
						SPICE have been updated. For more information, see  | July 10, 2024 | 
| Advanced options for paginted reports | You can now create repeating sections for pixel perfect reports in Amazon QuickSight.
					For more information, see  | June 27, 2024 | 
| 4 New Regions | QuickSight is now available in 4 new opt-in Regions: Europe (Milan),
					Europe (Zurich), Africa (Cape Town), and Asia Pacific (Jakarta). For more
					information, see  | May 28, 2024 | 
| New sorting options for tables in Amazon QuickSight | QuickSight Authors can now configure single column, multi column, and
					off-visual sorts for tables in Amazon QuickSight. For more information, see  | May 20, 2024 | 
| Key management in QuickSight: Updated IAM policy conditions | The required IAM policy permissions that grant access to AWS KMS keys in the
					QuickSight console and the QuickSight APIs have been updated. For
					more information, see  | May 16, 2024 | 
| Document history for the Amazon Quick User Guide | QuickSight Admins can now update and manage CMKs that are registered to
					a QuickSight account with the QuickSight APIs. For more
					information about creating and managing CMKs with the QuickSight APIs, For more
					information, see  | May 16, 2024 | 
| Hide SPICE capacity labels | QuickSight Admins can now choose to hide the account-wide
						SPICE capacity usage and remaining size labels from
					QuickSight authors. For more information, see  | May 2, 2024 | 
| Embed the Generative Q&A experience | You can now set up an embedded Q&A that uses enhanced NLQ capabilities
					powered by LLMs. The Q&A is the recommended replacement for the embedded Q
					Search Bar and provides an updated BI expereince for users. For more
					information, see  | April 30, 2024 | 
| Amazon Q in Quick: New Pro roles | Amazon Q integrates with Amazon QuickSight to give QuickSight users access to a
					suite of new generative BI capabilities. With Amazon Q in Quick, you can utilize the
					generative BI authoring experience, create executive summaries of your data, ask
					and answer questions of data, and generate data stories. To get started with
					Amazon Q in QuickSight Generative BI capabilities, upgrade your
					account's users to Admin Pro, Author Pro, or Reader Pro roles. For more
					information, see  | April 30, 2024 | 
| VPC endpoint restrictions | You can now create VPC endpoint restrictions in Amazon QuickSight to limit access
					to your QuickSight account. For more information, see  | April 9, 2024 | 
| Account instances of IAM Identity Center for account management | Amazon QuickSight now supports account instances of IAM Identity Center for identity management.
					For more information, see  | April 9, 2024 | 
| Managed policy update | Amazon QuickSight added a new managed policy to simplify Asset Bundle export
					operations. For more information, see  | March 27, 2024 | 
| Managed policy update | Amazon QuickSight added a new managed policy to simplify Asset Bundle import
					operations. For more information, see  | March 27, 2024 | 
| New Q pane | Amazon QuickSight users that are opted in to the Generative BI perview can now use
					the Q pane to access all relevant Generative BI features. For more information,
					see  | March 25, 2024 | 
| New Region: China (north) | Amazon QuickSight is now available in China (Beijing) (cn-north-1). For more
					information, see  | January 25, 2024 | 
| Amazon Q Business in Amazon QuickSight | Amazon Q Business integrates with Amazon QuickSight to give QuickSight users access
					to a suite of new generative BI capabilities. With Amazon Q in Quick, you can utilize the
					generative BI authoring experience, create executive summaries of your data, ask
					and answer questions of data, and generate data stories. For more information,
					see  | November 28, 2023 | 
| Trusted identity propagation in Amazon QuickSight | QuickSight authors can now create data sources with trusted identity
					propagation, which allows database administrators to centrally manage data
					security in Amazon Redshift and automatically apply all data security rules to data
					consumers in QuickSight. For more information, see  | November 26, 2023 | 
| Runtime filtering and theming for embedded dashboards and visuals | QuickSight authors can now customize filters and themes for embedded
					dashboards and visuals. For more information, see  | November 17, 2023 | 
| Custom time zones and week start days in Amazon QuickSight | QuickSight authors can now restrict the functionality that people can
					access in Amazon QuickSight. For more information, see  | November 17, 2023 | 
| Custom time zones and week start days in Amazon QuickSight | QuickSight authors can now turn on SPICE auto capacity
					purchasing to allow Amazon QuickSight to automatically manage your QuickSight
					account's SPICE capacity. For more information, see  | November 17, 2023 | 
| Amazon EventBridge integration | You can now integrate your Amazon QuickSight account with Amazon EventBridge. For more
					information, see  | November 17, 2023 | 
| New look for the QuickSight analysis workspace | We've redesigned the Amazon QuickSight analysis workspace. You might encounter
					screenshots or procedural text that doesn't reflect the new look in the
					QuickSight console. We're in the process of updating screenshots and
					procedural text. For more information on QuickSight's new look, see
						 | November 16, 2023 | 
| Custom time zones and week start days in Amazon QuickSight | QuickSight authors can now set custom time zones and week start days
					for their analyses. For more information, see  | November 14, 2023 | 
| Float decimal type | Decimal values in calculated fields of datasets that are stored in
						SPICE can now be assigned the  | November 8, 2023 | 
| Custom total values in Amazon QuickSight | QuickSight authors can now define the total and subtotal aggregations
					for their table or pivot table visuals from the field wells. For more
					information, see  | October 25, 2023 | 
| Restricted and unrestricted shared folders in Amazon QuickSight | QuickSight authors can now create restricted and unrestricted shared
					folders with the QuickSight CLI to help organize and manage the
					permissions of important QuickSight assets. For more information, see
						 | October 24, 2023 | 
| New data source | QuickSight now supports connecting to a Trino data source. For more
					information, see  | October 20, 2023 | 
| New data source | QuickSight now supports connecting to a Starburst data source. For more
					information, see  | October 20, 2023 | 
| SageMaker AI Canvas integration | QuickSight authors can now export data into SageMaker AI Canvas to build ML
					models that can be sent back to QuickSight and applied to analyses and
					dashboards. For more information, see  | October 6, 2023 | 
| Managed policy update | The  | October 6, 2023 | 
| Amazon Redshift run-as role | QuickSight authors can now connect Amazon Redshift data with run as role to
					enhance data security with fine grained access policies. For more information,
					see  | October 6, 2023 | 
| Generative BI public preview | The public preview for Generative BI is now available to users who have a
					QuickSight Q add-on subscription. For more information, see  | September 28, 2023 | 
| Freeze table columns in Amazon QuickSight | You can now freeze single or groups of table columns in Amazon QuickSight. For more
					information, see  | September 26, 2023 | 
| Enhanced KPI options in Amazon QuickSight | New layouts and formatting options for KPIs are now available in Amazon QuickSight.
					For more information, see  | September 15, 2023 | 
| Scaled folders in Amazon QuickSight | You can create scaled folders that can be shared with thousands of namespaces
					at once with the Amazon QuickSight APIs. For more information, see  | August 30, 2023 | 
| Excel format reports in Amazon QuickSight | You can now create and schedule Excel snapshot reports of a dashboard in
					Amazon QuickSight. For more information, see  | August 24, 2023 | 
| Add contextual row subtitles to pivot tables in Amazon QuickSight | You can now add contextual row subtitles to pivot tables in Amazon QuickSight. For
					more information, see  | August 16, 2023 | 
| New layouts for pivot tables in Amazon QuickSight | Amazon QuickSight now supports two types of layout for pivot tables: tabular and
					hierarchy. For more information, see  | August 11, 2023 | 
| Default column width Amazon QuickSight | You can now set the default column width of your pivot table visuals in
					Amazon QuickSight. For more information, see  | August 11, 2023 | 
| Amazon QuickSight integration with IAM Identity Center | You can now integrate your Amazon QuickSight Enterprise edition account with IAM Identity Center.
					For more information, see  | August 11, 2023 | 
| Embedded callback actions at runtime | You can now use embedded data point callback actions to build tighter
					integrations between your SaaS application and your Amazon QuickSight embedded
					dashboards and visuals. For more information, see  | August 9, 2023 | 
| Working with field level coloring in Amazon QuickSight | You can now assign specific colors to specific field values across all visuals
					in a QuickSight analysis or dashboard. For more information, see  | July 13, 2023 | 
| Small multiples axis options in Amazon QuickSight | You can now configure the x and y axes for each individual panel of a small
					multiples visual in Amazon QuickSight. For more information, see  | July 13, 2023 | 
| Use the analysis menu in Amazon QuickSight | You can now use menu options to efficiently perform tasks without needing to
					manually navigate through your analysis in Amazon QuickSight. For more information,
					see  | July 7, 2023 | 
| Advanced report scheduling options in Amazon QuickSight | You can now access more advanced PDF report scheduling options in
					Amazon QuickSight. For more information, see  | June 30, 2023 | 
| Format visual language data based on language settings in Amazon QuickSight | You can now choose how your numeric data values appear in visuals so that they
					align with the regional language that you have chosen in Amazon QuickSight. For more
					information, see  | May 26, 2023 | 
| Create geospatial heatmaps in Amazon QuickSight | You can now create geospatial heatmaps in Amazon QuickSight. For more information,
					see  | May 26, 2023 | 
| Work with Q topics using the QuickSight CLI in Amazon QuickSight | You can now work with QuickSight Q topics using the Amazon QuickSight
					command line interface (CLI). For more information, see  | May 4, 2023 | 
| Use dataset parameters in Amazon QuickSight | You can now use dataset parameters in direct query to dynamically customize
					their datasets and apply reusable logic to your datasets. For more information,
					see  | May 4, 2023 | 
| Enhanced options for scatter plots in Amazon QuickSight | You can now plot unaggregated values on scatter plots in Amazon QuickSight. For
					more information, see  | May 4, 2023 | 
| Create and update VPC connections Amazon QuickSight | You can now create and update VPC connections in Amazon QuickSight. For more
					information, see  | May 4, 2023 | 
| Create tag-based RLS rules using the OR condition in Amazon QuickSight | You can now add the OR condition to your tag-based rules to further customize
					the way data is presented to your QuickSight account users. For more
					information, see  | April 7, 2023 | 
| Threshold alerts on Table and Pivot table visuals in Amazon QuickSight | You can now create threshold alerts for Table and Pivot table visuals in
					Amazon QuickSight. For more information, see  | March 17, 2023 | 
| Hide collapsed columns in Amazon QuickSight table visuals | You can now customize the way Amazon QuickSight readers view pivot tables to make
					them easier to read and understand at a glance. For more information, see  | March 9, 2023 | 
| Enhanced embedding capabilities in Amazon QuickSight | You can now use QuickSight's Embedding SDK (v2.0) to improve
					developer experience when embedding QuickSight in your application or
					website. For more information, see  | March 9, 2023 | 
| Run queries with Amazon S3 data sources in Amazon QuickSight | You can now enhance data security by using fine-grained access policies rather
					than broader permissions for data sources connected to Amazon S3 in Amazon QuickSight. For
					more information, see  | February 21, 2023 | 
| Radar charts in Amazon QuickSight | You can now create radar charts in Amazon QuickSight. For more information, see
						 | January 30, 2023 | 
| Data bars for tables and pivot tables in Amazon QuickSight | You can now use data bars to add visual context to your table visuals in
					Amazon QuickSight. For more information, see  | January 24, 2023 | 
| New question types: Boolean, Forecast, and Why | You can now enter boolean, forecast, and why questions into the
					QuickSight Q search bar. For more information, see  | November 29, 2022 | 
| Automated data prep for QuickSight Q | Amazon QuickSight Q now uses AI-enhanced data preparation to automatically create
					topics that are relevant to your end users. For more information, see  | November 29, 2022 | 
| Pixel perfect reporting | You can now create, schedule, and share highly formatted multi-page reports in
					Amazon QuickSight. For more information, see  | November 28, 2022 | 
| Embedding the Q search bar for anonymous (unregistered) users | You can now embed the QuickSight Q search bar for anonymous
					(unregistered) users. For more information, see  | November 19, 2022 | 
| Asset management | You can now manage all of the assets un your Amazon QuickSight account in one
					unified view. For more information, see  | November 19, 2022 | 
| Text boxes | You can now add static and dynamic textual content using text boxes in
					Amazon QuickSight. For more information, see  | November 18, 2022 | 
| Small multiples | You can now create small multiples in line, bar, and pie chart visuals. For
					more information, see  | November 18, 2022 | 
| Set a reserved value in QuickSight datasets | You can now set a reserved value to determine the value of the
						 | November 18, 2022 | 
| Run queries as an IAM role in Amazon QuickSight | You can now enhance data security by using fine-grained access policies rather
					than broader permissions for data sources connected to Athena. For more
					information, see  | November 18, 2022 | 
| Pin Amazon QuickSight Q answers to your pinboard | You can now pin visuals from Q for easy access to frequently asked questions.
					For more information, see  | November 18, 2022 | 
| Marker clustering on geospatial map visuals | You can now use marker clustering to improve readability of co-located points
					on a map. For more information, see  | November 18, 2022 | 
| Line chart customization | You can now add customizations to line chart visuals to emphasize what you
					want readers to focus on: color, line style, and markers. For more information,
					see  | November 18, 2022 | 
| Connecting Amazon QuickSight accounts to Databricks | You can now use Amazon QuickSight to connect to Databricks on AWS.
					For more information, see  | November 18, 2022 | 
| Account termination protection | You can now use account termination protection to prevent someone from
					deleting a QuickSight user account accidentally or maliciously. For more
					information, see  | November 18, 2022 | 
| 1 billion row SPICE datasets | Amazon QuickSight now supports SPICE datasets that contain up to 1 billion
					(1,000,000,000) rows or 1 terabyte (TB) of data. For more information, see
						 | November 18, 2022 | 
| Monitor SPICE consumption metrics in Amazon CloudWatch | You can now monitor your QuickSight account's SPICE consumption
					metrics in Amazon CloudWatch. For more information, see  | November 8, 2022 | 
| Use AWS KMS to encrypt your SPICE datasets in Amazon QuickSight |  You can now encrypt your SPICE datasets using the keys that you have stored
					in AWS KMS. This provides you with the tools to audit access to data and satisfy
					regulatory security requirements. For more information, see  | October 27, 2022 | 
| Add datasets that contain row-level security (RLS) to Q topics | QuickSight Q now supports questions for access restricted datasets that
					use Row level Security (RLS) with user based rules. Readers can now ask
					questions about Topics that contain restricted access datasets and instantly
					receive accurate and pertinent answers based on access control rules defined by
					authors in RLS settings. For more information, see  | October 10, 2022 | 
| Use AWS Secrets Manager secrets instead of database credentials in Amazon QuickSight | Amazon QuickSight administrators can grant QuickSight read-only access to
					secrets they create in AWS Secrets Manager. These secrets can be used in place of database
					credentials when creating and editing data sources using the QuickSight
					API. For more information, see  | October 6, 2022 | 
| Visual Embedding | You can now embed visuals using a 1-click embed code or with the Amazon QuickSight
					API. For more information, see  | August 25, 2022 | 
| Undo and redo changes in Q answers | You can now undo or redo any changes you make to a Q answer by choosing the
					undo or redo arrows in the Q search bar. For more information, see step six in
						 | August 22, 2022 | 
| Updates to the sign in experience | The sign in experience in QuickSight has been updated. For more
					information about how to sign in, see  | July 21, 2022 | 
| Bookmarks | You can now bookmark views of a dashboard. For more information, see  | July 21, 2022 | 
| Base Maps | When creating map visuals in QuickSight, you can now change map base.
					For more information, see  | July 21, 2022 | 
| Q updates | You can now try QuickSight Q out for free before getting the Q add-on.
					For more information, see  | July 7, 2022 | 
| Rolling dates in filters and parameters | You can now set a rolling date on date range fiters and relative date
					parameters in analyses. For more information, see  | July 5, 2022 | 
| Calculations update | You can now create level-aware calculations in QuickSight. You can
					specify at what level to group computations using level-aware calculation -
					aggregation (LAC-A) functions. You can also specify the window or partition to
					compute a calculation using level-aware calculation - window (LAC-W) functions
					(previously known as level-aware aggregations). For more information, see  | July 5, 2022 | 
| Allowed domains | Developers can now add a domain at run-time to an allow list with the
						 | July 5, 2022 | 
| Account provisioning | You can now sign up for an Amazon QuickSight account with the Amazon QuickSight API. For
					more information, see  | July 5, 2022 | 
| Monitoring data with Amazon CloudWatch | You can now monitor metrics for Amazon QuickSight dashboards, visuals, and dataset
					ingestions on Amazon CloudWatch to provide your readers with a consistent,
					high-performing, and uninterrupted experience on QuickSight. For more
					information, see  | June 22, 2022 | 
| Forecast boundaries | Authors can now set a minimum and maximum for forecasted values. For more
					information, see  | June 16, 2022 | 
| Table and pivot table enhancements | Authors and Readers can now resize rows and columns in a table or pivot table
					visual. For more information, see  | June 14, 2022 | 
| Hiding fields in pivot tables | You can now hide fields in pivot table visuals. For more information, see
						 | June 14, 2022 | 
| ML insights and forecasting for Q | Readers can now see key data insights and add forecasts to Q answers. For more
					information, see  | June 2, 2022 | 
| What's New in QuickSight | To find out what's new in QuickSight, see the  | June 1, 2022 | 
| Line chart updates | QuickSight now supports 10,000 data points for line charts. For more
					information, see  | May 22, 2022 | 
| 1-click public embedding | You can now embed dashboards for anyone on the internet in your public
					applications with a 1-click static embed code. For more information, see  | May 18, 2022 | 
| Creating and managing groups | You can now create and manage groups in the QuickSight console. For
					more information, see  | March 21, 2022 | 
| Automatic refresh controls for direct query | In QuickSight, filter controls are now refreshed every 24 hours for
					direct query. For more information, see  | March 8, 2022 | 
| Updating files in a dataset | You can now update files in a dataset to get the latest version of those
					files. For more information, see  | January 27, 2022 | 
| Rich text formatting for titles and subtitles | QuickSight now offers rich text formatting for titles and subtitles,
					and the ability to add hyperlinks and parameters in titles. For more
					information, see  | January 27, 2022 | 
| Comparative and cumulative date/time calculations | Comparative and cumulative period functions, such as year-over-year and
					year-to-date, are now supported in QuickSight. For more information, see
						 | January 27, 2022 | 
| Sharing dashboards | You now have the option to grant everyone in your QuickSight account
					access to a dashboard. You can also share a link to the dashboard with anyone
					who has access to it. For more information, see  | November 23, 2021 | 
| Customizing email report templates | You can now customize how dashboard email reports appear and behave for
					QuickSight account users. For more information, see  | November 23, 2021 | 
| 1-click enterprise embedding | You can now embed dashboards for registered users in your internal
					applications with a 1-click static embed code. For more information, see  | November 23, 2021 | 
| New data source | QuickSight now supports connecting to an Exasol data source. For more
					information, see  | November 22, 2021 | 
| Dataset versioning | QuickSight now supports dataset versioning. For more information, see
						 | November 22, 2021 | 
| Adding datasets with RLS to Q topics | QuickSight Q topics now support datasets with row-level security (RLS).
					For more information, see  | November 19, 2021 | 
| Sheet change performance operations | QuickSight now only refreshes visuals when switching sheets if
					required. For more information, see  | November 12, 2021 | 
| Incrementally refresh a SQL-based dataset | In QuickSight Enterprise Edition, you can now refresh your SQL-based
						SPICE datasets incrementally within a look-back window of
					time. For more information, see  | October 25, 2021 | 
| Embedding the Q search bar | You can now embed the Q search bar in your application for registered users of
					QuickSight. For more information, see  | October 22, 2021 | 
| Email syncing for federated users | In Enterprise Edition, QuickSight administrators can now restrict new
					users from using personal email addresses when provisioning through their
					identity provider (IdP) to QuickSight. For more information, see  | October 22, 2021 | 
| Adding RLS tags to a dataset | You can now add tag-based rules to a dataset in QuickSight when
					applying row-level security (RLS). For more information, see  | October 19, 2021 | 
| IP restrictions | You can now limit access to your organization's QuickSight account to a
					predefined list of Internet Protocol (IP) ranges. For more information, see
						 | October 18, 2021 | 
| New table and pivot table styling options | You can now customize the look of tables and pivots tables. For more
					information, see  | October 12, 2021 | 
| New SPICE quota for imported data | In QuickSight Enterprise edition, you can now import up to 500 million
					rows into a SPICE dataset. For more information, see  | October 12, 2021 | 
| Links and images in tables | You can now add links to tables. You can also render links as images in
					tables. For more information, see  | October 12, 2021 | 
| Custom date formats | You can now customize how dates are formatted in your filter and parameter
					controls. For more information, see  | October 8, 2021 | 
| QuickSight q | You can now ask questions about your data in the Q bar and get answers in the
					form of visuals. For more information, see  | September 24, 2021 | 
| New geospatial region | QuickSight now supports creating geospatial charts for India. For more
					information about creating geospatial charts, see  | September 22, 2021 | 
| Free-form layouts | You can now place visuals anywhere in your dashboard using precise
					coordinates. For more information, see  | September 22, 2021 | 
| Passing IAM roles to QuickSight | You can now pass IAM roles to QuickSight. For more information, see
						 | September 15, 2021 | 
| Create datasets from existing datasets | You can now create datasets from existing datasets. For more information, see
						 | September 15, 2021 | 
| Updated AWS managed policy | QuickSight updated an existing AWS managed policy. For more
					information, see  | September 8, 2021 | 
| New AWS managed policy | QuickSight added a new AWS managed policy. For more information, see
						 | September 8, 2021 | 
| Forecast multiple measures | You can now forecast up to three measures in the same chart. For more
					information, see  | August 30, 2021 | 
| Share your view of a dashboard | You can now share your view of a dashboard. For more information, see  | August 20, 2021 | 
| Hide the data zoom on a chart | You can now choose to show or hide the data zoom for your charts in
					Amazon QuickSight. For more information, see  | August 16, 2021 | 
| Row-level security with tags | You can now use row-level security (RLS) with tags to specify which data your
					(unauthenticated) users can see in an embedded Amazon QuickSight dashboard depending
					on who they are. For more information, see  | July 29, 2021 | 
| New embedding API operations | Amazon QuickSight has the following new API operations for embedding analytics:
						 | July 29, 2021 | 
| Customizing charts | You can now hide the sort icon and the axis or field title in charts in
					Amazon QuickSight. For more information, see  | July 16, 2021 | 
| Threshold alert updates | You can now choose to be notified when there is no data to check your alert
					rule against in Amazon QuickSight. For more information, see  | July 9, 2021 | 
| New chart type: Custom visual content | You can now embed webpages and online videos, forms, and images in your
					QuickSight dashboards using the custom visual content chart type. For
					more information, see  | June 29, 2021 | 
| Feature improvements | You can now show totals for stacked bar charts. For more information, see
						 | June 29, 2021 | 
| Threshold alert updates | Dataset owners can now set a threshold alert evaluation schedule for a dataset
					in Amazon QuickSight. For more information, see  | June 17, 2021 | 
| Duplicating analyses | You can now duplicate an analysis in Amazon QuickSight. For more information, see
						 | June 17, 2021 | 
| Threshold alert updates | You can now choose how often you want to receive threshold alerts in
					Amazon QuickSight. For more information, see  | May 25, 2021 | 
| Wildcard search | Amazon QuickSight now supports wildcard search. For more information, see  | May 1, 2021 | 
| Threshold alerts | Amazon QuickSight now supports creating threshold alerts using KPI and Gauge
					visuals in dashboards. For more information, see  | May 1, 2021 | 
| Service control policies | Amazon QuickSight now supports using service control policies (SCPs) to restrict
					how individuals in your organization can sign up for QuickSight. For more
					information, see  | April 26, 2021 | 
| Parameter improvements | Amazon QuickSight now supports dynamically displaying parameter values in titles
					and descriptions throughout charts and analyses. For more information, see
						 | April 12, 2021 | 
| Feature improvements | QuickSight now supports selecting a time granularity for date and time
					range filters and datetime parameters. For more information, see  | April 1, 2021 | 
| Export to PDF | QuickSight now supports PDF exports of the current sheet in dashboards
					and analyses. In Enterprise edition, you can now attach a PDF to email reports.
					For more information, see  | April 1, 2021 | 
| Seconds support for date fields | QuickSight now supports aggregating date fields at the second level.
					For more information, see  | March 30, 2021 | 
| Pivot table sorting improvements | QuickSight now supports sorting values in pivots tables by fields in
					the  | March 30, 2021 | 
| New feature | Amazon QuickSight now supports customizing tooltips in visuals. For more
					information, see  | March 16, 2021 | 
| Feature improvements | In Enterprise edition, QuickSight now supports computing anomalies for
					a time and measure field only, and computing the exact combination of fields in
					the Category field well. For more information, see  | March 16, 2021 | 
| Line chart improvements | Amazon QuickSight now supports creating line charts with dual axes. For more
					information, see  | March 1, 2021 | 
| New formatting options for charts | Amazon QuickSight now supports hiding axis lines, axis labels, and grid lines, and
					also customizing the how axis labels appear in a chart. For more information,
					see  | February 5, 2021 | 
| New chart type: Sankey diagrams | Amazon QuickSight now supports creating Sankey diagrams. For more information, see
						 | February 5, 2021 | 
| Field mapping improvements | Amazon QuickSight now supports updating field mapping between mismatched and
					missing fields when replacing a dataset in an analysis. For more information,
					see  | February 5, 2021 | 
| Data prep enhancements | Amazon QuickSight now supports organizing fields into folders and subfolders when
					preparing or editing datasets. For more information see,  | February 5, 2021 | 
| New features | In Enterprise edition, QuickSight now supports displaying anomaly
					ranges and multiple anomalies when exploring anomalies. Line charts now display
					notifications when QuickSight detects an anomaly, key driver, or
					forecasting opportunity. For more information, see  | February 3, 2021 | 
| New region: South America (São Paulo) | Amazon QuickSight is now available in South America (São Paulo) (sa-east-1). For more
					information, see  | December 23, 2020 | 
| New region: Canada (central) | Amazon QuickSight is now available in Canada (Central) (ca-central-1). For
					more information, see  | December 23, 2020 | 
| Define an action to open a different sheet | QuickSight now supports navigation actions to enable you to open a
					different sheet with the included parameter values. For more information, see
						 | December 21, 2020 | 
| Data source enhancement: Athena federated query | QuickSight now supports connecting to Athena Federated Query. For more
					information, see  | December 21, 2020 | 
| New list items sheet control type | Amazon QuickSight now supports single and multi-select list control on dashboards.
					For more information, see  | December 18, 2020 | 
| New formatting options for tables | In QuickSight, you can now reorder columns in table charts. For more
					information, see  | December 17, 2020 | 
| Row-level security (RLS) now supports GRANT option only | To streamline and simplify RLS setup, QuickSight no longer supports
					using RLS in deny-access mode. To create a new RLS configurations, use the
					explicit grant-access model. Current RLS datasets and deny-access configurations
					should continue to work as expected. For more information, see  | December 6, 2020 | 
| New percentile functions | QuickSight now supports variations on percentile calculations,
					including aggregate functions  | December 6, 2020 | 
| Dynamic queries, plus dataset editor improvements | QuickSight now enables you to improve performance for visuals based on
					direct queries by specifying unique keys for joined tables. There are also
					multiple interface improvements, such as settings for optional autopreviews,
					zoom in and out of data diagrams, join recommendations, and more. For more
					information, see  | December 6, 2020 | 
| Developer portal for embedding | The Dev Portal helps you learn how to use embedding by
					example in your web site or application. For more information, see  | November 30, 2020 | 
| New data source: Amazon OpenSearch | QuickSight now supports connecting to Amazon OpenSearch. For more
					information, see  | November 25, 2020 | 
| Format metrics on pie charts | QuickSight now supports formatting metrics on pie charts to display
					values, percentages, or both. For more information, see  | November 25, 2020 | 
| New formatting options for tables | In QuickSight, you can now vertically align and wrap the text for
					headers in table charts. For more information, see  | November 24, 2020 | 
| New chart type: Box plots | QuickSight now supports using box plots so you can visualize how your
					data is distributed across an axis or over time. For more information, see
						 | November 24, 2020 | 
| Filled maps | QuickSight now supports filled maps so you can visualize your data over
					a geographical area. For more information, see  | November 24, 2020 | 
| Favorite folders | In QuickSight, you can now favorite your folders for easy access. For
					more information, see  | November 24, 2020 | 
| Change in display limits | For parameter controls and filters, Amazon QuickSight now displays up to 1,000
					sample values. When you have more than that, you use the search box to locate a
					value. For more information, see  | November 16, 2020 | 
| Null rendering | QuickSight now allows null values to be updated to a custom string. For
					more information, see  | November 9, 2020 | 
| New chart type: Waterfall charts | QuickSight now supports using waterfall charts so you can view your
					data sequentially. For more information, see  | November 9, 2020 | 
| Embedding for everyone | QuickSight Enterprise edition now supports embedding for everyone. When
					you purchase session packs with capacity pricing, you can enable visitors to use
					embedded dashboards without registering them as QuickSight users. For
					more information, see  | November 9, 2020 | 
| Column-level security | QuickSight now supports using column-level security to restrict access
					to a dataset. For more information, see  | November 9, 2020 | 
| Service provider initiated federation | QuickSight Enterprise edition now supports service provider initiated
					federation, so you can sign on directly to QuickSight using your IAM Identity Center
					login and password. For more information, see  | October 30, 2020 | 
| New chart type: Funnel charts | QuickSight now supports using funnel charts so you can display your
					data in a linear process. For more information, see  | October 29, 2020 | 
| Custom sorting | QuickSight now enables you to apply sort options on fields outside the
					field wells. This feature is available for all charts that support sorting. For
					more information, see  | October 29, 2020 | 
| New region: AWS GovCloud (US-West) | Amazon QuickSight is now available in AWS GovCloud (US-West) (gov-west-1). For
					more information, see  | October 28, 2020 | 
| New data source: Oracle | QuickSight now supports connecting to Oracle. For more information, see
						 | October 23, 2020 | 
| Filter across datasets | In QuickSight, you can now create filters that apply to multiple
					datasets in an analysis. For more information, see  | October 23, 2020 | 
| Add field descriptions to datasets | QuickSight now enables you to add column or field descriptions to
					datasets. This metadata is visible in both datasets and analyses, helping you
					make your data self-explanatory. For more information, see  | October 23, 2020 | 
| Filter controls on analysis sheets | QuickSight now offers a filter control that you can add to your
					analysis with a single click. You can put filters beside dashboard visuals and
					resize them to fit. For more information, see  | October 5, 2020 | 
| New data source: Amazon Timestream | QuickSight now supports Amazon Timestream as a data source. For more
					information, see  | October 1, 2020 | 
| Export to excel | QuickSight now supports exporting data from pivot tables and table
					charts to Microsoft Excel (.xslx) format. For more information, see  | September 14, 2020 | 
| Duplicate sheets | QuickSight now supports duplicating sheets. For more information, see
						 | September 14, 2020 | 
| Customize labels of totals and subtotals | In QuickSight, you can now add custom text to display beside totals and
					subtotals for pivot tables and table charts. For more information, see  | September 14, 2020 | 
| Skipped row details | When you import data into QuickSight, you now get better error messages
					and row-by-row information on what caused rows to be skipped during ingestion
					into SPICE. For more information, see  | September 12, 2020 | 
| New configuration option for multivalue lists | QuickSight now supports a configuration option for multivalue lists to
					start with no values selected. For more information, see  | September 11, 2020 | 
| Reference lines | QuickSight now supports using reference lines in bar, line, and combo
					charts. For more information, see  | September 3, 2020 | 
| New table calculations | QuickSight now supports using window functions  | August 25, 2020 | 
| Multivalue default parameters | QuickSight now supports dynamic default values for multi-valued
					parameters. For more information, see  | August 25, 2020 | 
| Last active status for users | QuickSight administrators can now see the last date and time that
					people accessed QuickSight. For more information, see  | August 25, 2020 | 
| Join SQL queries, tables, and files | QuickSight now supports using custom SQL queries in joins with other
					queries, tables, and files. For more information, see  | August 25, 2020 | 
| Calculated expressions editor | The enhanced editor adds ease-of-use features to help you more easily create
					calculated expressions in QuickSight. With the new full-screen editor,
					you can add functions and values directly from the menu. For more information,
					see  | August 25, 2020 | 
| Personal and shared folders | QuickSight Enterprise edition now offers personal and shared folders to
					make it easier to discover, organize, share, and explore your available assets.
					For more information, see  | August 5, 2020 | 
| QuickSight support for multitenancy | In Enterprise edition, QuickSight now offers an additional layer of
					security to support multitenancy. By creating users and groups in a
					QuickSight namespace, you can isolate them from users and groups in other
					namespaces. For more information, see  | July 23, 2020 | 
| Embed the QuickSight console | In QuickSight Enterprise edition, you can now provide the full
					dashboard authoring experience of the QuickSight console in your own
					custom-branded authoring portal. For more information, see  | July 23, 2020 | 
| Datasets with 2,000 columns | QuickSight now supports datasets that have up to 2,000 columns. For
					more information, see  | July 23, 2020 | 
| Customized permissions | In QuickSight Enterprise edition, you can now create custom roles to
					restrict a person from using specific functionality in the QuickSight
					console, for example to control who can manage data sources and datasets or who
					can manage or subscribe to email reports. For more information, see  | July 23, 2020 | 
| Customize the console | In QuickSight Enterprise edition, you can now choose whether to show or
					hide QuickSight startup samples and videos. You can also create and
					specify a default theme to add branding to your experience of the
					QuickSight console. For more information, see  | July 23, 2020 | 
| Larger SPICE datasets | QuickSight Enterprise edition now supports SPICE
					datasets with up to 250 million (250,000,000) rows or 500 GB. For more
					information, see  | July 9, 2020 | 
| Display width settings | In QuickSight, you can now choose between responsive and fixed layouts
					for your analyses and dashboards. You can also temporarily change your current
					view from the menu bar. For more information, see  | July 9, 2020 | 
| Data refresh notifications | QuickSight now supports sending email to notify SPICE
					dataset owners when data refresh fails. For more information, see  | July 9, 2020 | 
| Color settings for heat maps and tree maps | You can now customize gradient colors for your heat maps and tree maps in
					QuickSight. For more information, see  | July 9, 2020 | 
| Font choice | You can now customize your theme with a font. Choose from a selection of fonts
					supported by QuickSight. For more information, see  | July 8, 2020 | 
| AWS Lake Formation | If you use QuickSight Enterprise edition to query Amazon Athena, you can
					simplify data access management by using AWS Lake Formation to control permissions to
					Athena. For more information, see  | June 29, 2020 | 
| New chart type | QuickSight now supports using histograms so you can display the
					distribution of values in your data. For more information, see  | June 12, 2020 | 
| Gauge chart update | You can now add conditional formatting to gauge charts in QuickSight.
					For more information, see  | June 12, 2020 | 
| Five new languages | QuickSight now supports Danish, Dutch, Finnish, Norwegian, and Swedish.
					These languages expand upon the existing 15 languages already available in
					QuickSight. For more information, see  | June 12, 2020 | 
| New region: Mumbai | Amazon QuickSight is now available in Asia Pacific (Mumbai) (ap-south-1). For more
					information, see  | June 3, 2020 | 
| New SQL editor | QuickSight enhanced the SQL editor that you use to create datasets from
					SQL queries. The new SQL editor supports syntax highlighting, basic
					autocomplete, autoindent, and line numbering. Also, you can use the new schema
					explorer to interactively explore schemas, tables, fields, and data types. For
					more information, see  | May 20, 2020 | 
| Amazon SageMaker AI integration now generally available | The integration of SageMaker AI with QuickSight launched in preview just before
					AWS re:Invent 2019. Now, this feature is generally available in all
					AWS Regions that are supported by QuickSight. Amazon QuickSight and SageMaker AI together
					makes it faster, easier, and more cost-effective for customers to make use of
					their machine learning models for visualization and predictions. For more
					information, see  | May 19, 2020 | 
| Update to presto data sources | You can now use nonauthenticated private Presto as a data source. For more
					information, see  | May 18, 2020 | 
| Rewrite of Amazon QuickSight VPC connection section | Based on your feedback, we completely rewrote this documentation to better
					explain using Amazon VPC with QuickSight. It includes examples and AWS CLI
					commands to help you establish the path from Amazon QuickSight to your data source,
					even if you're using on-premises sources. For more information, see  | May 18, 2020 | 
| Use logarithmic scale with QuickSight | You can now format visuals using log scale. For more information, see  | May 1, 2020 | 
| Severity levels for QuickSight anomaly detection insights | You can now choose the level of severity for anomalies that display in your
					insight widgets. For more information, see  | April 17, 2020 | 
| QuickSight adds a new visual type | The new visual type, stacked area line charts, is similar to area charts
					except that the stacked values indicate the relationship that each value
					contributes to the whole. Using stacked area charts, you can display cumulative
					totals over time while displaying the breakdown by the chosen category. For more
					information, see  | April 17, 2020 | 
| QuickSight activates legends by adding menus for quick feature access | QuickSight now supports clicking on legend items to quickly access
					features like filtering, drilling, chart colors, and custom actions for
					filtering and URLs. For more information, see  | April 17, 2020 | 
| Improvements to visual controls in QuickSight | The on-visual menu can now float at the upper-right corner of the visual,
					moving inside or outside the border of the visual. Plus, you can make your
					visuals smaller and have more of them, as many as 36 across. For smaller
					visuals, the new visual controls have more viewing area for charts and insights.
					To see the new menu, choose one of your visuals. For more information, see
						 | April 17, 2020 | 
| QuickSight adds cascading filters | You can now create cascading filters by adding them to custom actions in your
					analyses and dashboards. Each custom filter action can target one or more
					visuals in the same sheet, creating a cascading filter effect. For more
					information, see  | April 2, 2020 | 
| Modulo operation available in Amazon QuickSight | You can now use modulo operation to find the remainder after dividing one
					number into another. For more information, see  | March 8, 2020 | 
| Images in Amazon QuickSight narratives | You can now insert images from URLs to be rendered as part of a narrative.
					Images can be resized, conditionally shown within an IF block, and also
					hyperlinked with the URL feature. For more information, see  | March 8, 2020 | 
| Amazon QuickSight adds minimum and maximum dates | You can now use minimum and maximum date aggregations in tables and pivot
					tables. For more information, see  | March 8, 2020 | 
| Now you can customize minimum delta values to enhance QuickSight ML-powered anomaly detection | Now you can control the minimum delta value that QuickSight uses to
					detect anomalies (also known as outliers). You can change this setting when you
					are configuring or exploring anomalies. For more information, see  | February 4, 2020 | 
| Improvements in the QuickSight narrative expression editor | QuickSight now provides a much more spacious interface for editing
					narrative expressions. The interface now has instant feedback in a preview of
					your evaluated narrative before you save any changes. Plus, narratives now
					support both static and dynamic URLs in your custom narratives for links to
					searches, apps, other dashboards, other sheets in the same dashboard, and more.
					For more information, see  | February 4, 2020 | 
| SageMaker AI integration now available in more AWS Regions | The public preview for integrating SageMaker AI with QuickSight is now
					available in all of the AWS Regions that are supported by QuickSight. For more
					information, see  | January 10, 2020 | 
| QuickSight now enables you to choose an Amazon Athena workgroup | By choosing an Athena workgroup, you can better manage your Athena datasets.
					Using this option, you can also allocate Athena costs to the workgroup that
					QuickSight is using, for better cost reporting. For more information, see  | December 10, 2019 | 
| Private VPC support for presto in QuickSight | Now Presto can use a VPC connection. For more information, see  | December 10, 2019 | 
| New mathematical functions in QuickSight | Amazon QuickSight now supports functions for base 10 logarithms ( | December 10, 2019 | 
| New LAA functions in QuickSight | Now you can use  | December 10, 2019 | 
| Integrate SageMaker AI ML models into your QuickSight analyses and dashboards | In this public preview, QuickSight launches the ability to integrate
					machine learning (ML) models created and trained in SageMaker AI. This new feature makes
					it easier to augment your business data with ML predictions. Add your data
					scientists' prebuilt inferences and predictions to your analysts'
					dashboards, and let the collaboration and decision-making begin. For more
					information, see  | November 26, 2019 | 
| New formatting options for visuals in QuickSight | Amazon QuickSight launches more formatting for visuals and visuals titles,
					including font sizes from extra small to extra large. In key performance
					indicators (KPIs), you can set font sizes for primary and comparison values. In
					pivot tables and tables, you can see font sizes for table headers, cells,
					totals, and subtotals. Now your visuals render better even when smaller and with
					less padding between charts. For combo charts, you can now synchronize the
					Y-axes for both bars and lines into a single axis. For more information, see
						 | November 23, 2019 | 
| QuickSight supports the now function in SPICE | For more information, see  | November 22, 2019 | 
| QuickSight now supports seconds in SPICE | Seconds are now supported in SPICE datasets. Datetime fields
					are no longer truncated to minutes. Now you can use the  | November 22, 2019 | 
| QuickSight now has themes | You can now create a collection of themes, and apply a theme to an analysis
					and all its dashboards. For more information, see  | November 22, 2019 | 
| New QuickSight API operations | Amazon QuickSight launches new API operations to programmatically manage your data,
					dashboards, and fine-grained access control capabilities linked with AWS Identity and Access Management
					(IAM). With new data API operations, you can create, update, and delete Amazon Quick Sight
					data sources and datasets programmatically. You can also manage data refreshes
					on your SPICE datasets with API operations. Amazon QuickSight also
					introduces templates, which store the visual configuration and data schemas
					required for a dashboard. You can transfer templates across accounts or use them
					to instantiate dashboards with the same visual presentation but different data.
					For more information, see the  | November 22, 2019 | 
| QuickSight now supports conditional formatting for tables, pivot tables, and key performance indicators (KPIs). |  For tables and pivot tables, you can set multiple conditions for fields or
					supported aggregations, along with format options to apply to a target cell. For
					KPIs, you can format the primary value based on conditions that are applied to
					any dimension in the dataset. The conditional formatting options now supported
					are text color, background color, and placement of supported icons. You can use
					icons from the provided set, or you can use Unicode icons instead. For more
					information, see  | November 18, 2019 | 
| View history for SPICE ingestion on your Amazon QuickSight datasets | You can now view the ingestion history for SPICE datasets in
					Amazon QuickSight. See information like when the latest ingestion started, how long
					it took, and what its status is. For more information, see  | November 7, 2019 | 
| Add your own functionality to visuals with Amazon QuickSight actions | Amazon QuickSight enables you to add to the basic functionality for visuals by
					creating your own custom actions for filtering or opening URLs. For more
					information, see  | November 7, 2019 | 
| Amazon QuickSight now supports dynamic sheet titles | You can now use parameters in sheet titles to make the context of a dashboard
					clearer to the reader. For more information, see  | November 6, 2019 | 
| Use Amazon QuickSight to join data from multiple data sources | Amazon QuickSight now supports creating datasets that join multiple data sources.
					For more information, see  | November 5, 2019 | 
| Amazon QuickSight mobile iOS update and a new Android app | Get access to insights from your data on the fly. Download the updated iOS app
					or the new Android app. You can browse, favorite, and interact with your
					dashboards and explore your data with drilldowns and filters. You can stay ahead
					of the curve by using forecasting. You can get email alerts when unexpected
					changes happen in your data, and you can share those insights with colleagues.
					For more information, see  | November 5, 2019 | 
| Amazon QuickSight supports printing | Now you can print a dashboard or an analysis. For more information, see  | October 17, 2019 | 
| Amazon QuickSight supports a new AWS Region | Amazon QuickSight is now available in Asia Pacific (Seoul) (ap-northeast-2). For
					more information, see  | October 17, 2019 | 
| Amazon QuickSight now supports visual-level formatting | Now, any formatting you apply from the field wells is applied only to the
					selected visual. For more information, see  | October 17, 2019 | 
| Transpose tables | In table visuals, you can now transpose columns and rows. For more
					information, see  | October 10, 2019 | 
| Shared data sources | Share data sources with other users and groups. For more information, see
						 | October 10, 2019 | 
| SPICE enhancements | SPICE dashboards now support new wildcard filters on
					dimensions. You can now filter your data using any of the available wildcard
					filters: 'contains', 'starts with', 'end with', 'equals'. Additionally,
						SPICE dashboards now support new string functions
						( | October 10, 2019 | 
| New publishing options for dashboards | Control your user experience with more publishing options for your dashboards.
					These options include ability to toggle the filter pane, tooltips, drill
					up/down, and more. For more information, see  | October 10, 2019 | 
| New median function | Amazon QuickSight supports median as a new aggregation. For more information, see
						 | October 10, 2019 | 
| New filter functionality | Amazon QuickSight now supports additional relative date filter options. For more
					information, see  | October 10, 2019 | 
| New aggregations for fields | You can now use Nth percentile, median, standard deviation, and variance in
					field wells, filters, and ML Insights. For more information, see  | October 10, 2019 | 
| Filter for context | You can now filter text using the following wildcard comparison types:
					contains, does not contain, begins with, and ends with. For more information,
					see  | October 10, 2019 | 
| Use the power operator (^) in SPICE | QuickSight now supports using the power operator ( | September 11, 2019 | 
| Use string functions in SPICE | Now you can use string functions for calculated fields in your analyses based
					on SPICE datasets. For more information, see  | September 11, 2019 | 
| Use level-aware aggregations to control your calculations | QuickSight now supports level-aware aggregation calculations. Using
					this feature, you can perform aggregations at prefilter and preaggregation
					levels, before aggregations that happen in the display. This helps you explore
					more advanced query-building strategies than ever before. For more information,
					see  | September 11, 2019 | 
| Sort your anomalies | Now you can choose how to sort anomalies on the insight widget and in the
					anomaly exploration page. Choosing how to prioritize anomalies can help you
					identify the anomalies that are the most important to you. For more information,
					see  | September 11, 2019 | 
| Put 100 million rows into a SPICE dataset | We changed the SPICE dataset limit from 25GB to 100 million
					rows for Enterprise edition (and 25 million rows for Standard edition). For more
					information, see  | September 11, 2019 | 
| Rename your dashboard, keep your settings | Amazon QuickSight now supports renaming your published dashboards in place. You can
					change the name and still keep your settings and subscribers. For more
					information, see  | September 6, 2019 | 
| New visual type: Word clouds | Amazon QuickSight supports word cloud visuals that are based on different
					aggregations over any dimension in your dataset. You can drill down, focus on
					specific data points, and apply specific colors to data points on the word
					cloud. For more information, see  | September 5, 2019 | 
| Filter out the last n time periods | Amazon QuickSight lets you exclude a specific number and type of time periods from
					a time range (after) filter. For more information, see  | September 5, 2019 | 
| Amazon QuickSight new feature to mark favorites | Mark your favorite dashboards and analyses so you can come back to them
					quickly. For more information, see  | September 5, 2019 | 
| Amazon QuickSight Enterprise edition adds anomaly alerts | Your readers can subscribe themselves to anomaly alerts on dashboards to get
					the latest ML-powered anomaly detection and contribution analysis by email. For
					more information, see  | September 5, 2019 | 
| QuickSight adds custom colors for charts. | With the QuickSight enhanced color picker, you can choose custom colors
					for charts where color customization is supported. The enhanced color picker
					also retains the eight most recently used custom colors for easy selection
					across multiple charts. For more information, see  | August 1, 2019 | 
| Detect anomalies with less data | In Amazon QuickSight Enterprise edition, we lowered the required minimum data
					points to 15 for training anomaly detection. For more information, see  | August 1, 2019 | 
| Amazon QuickSight supports new AWS Regions | Amazon QuickSight is available in Europe (London) and Europe (Frankfurt).
					Also, you can now connect to Active Directory in any AWS Region supported by
					Amazon QuickSight, except Asia Pacific (Singapore) and Asia Pacific (Sydney). For
					more information, see  | August 1, 2019 | 
| Embedding for Active Directory | In Amazon QuickSight Enterprise edition, you can now embed dashboards for users
					authenticated through Active Directory. For more information, see  | July 11, 2019 | 
| Granular access control for using AWS services from Amazon QuickSight | In Amazon QuickSight Enterprise edition, you can scope down your security policies
					to allow specific people access to specific AWS resources. You can attach and
					detach IAM policies in the Amazon QuickSight interface, simplifying finer control
					over who can access your AWS data sources. For more information, see  | June 14, 2019 | 
| Tabs for dashboards and analyses | Amazon QuickSight now supports multiple sheets inside of analyses and dashboards.
					You can add multiple tabs to your dashboards, utilize URL actions and on-screen
					controls to simplify navigation, and filter across all of your sheets. For more
					information, see  | June 11, 2019 | 
| New visual types | You can now use Amazon QuickSight to chart your data on a customizable gauge and
					donut charts. For more information, see  | June 11, 2019 | 
| New functions | Amazon QuickSight now supports functions Variance and Standard Deviations as both
					aggregation and table calculation. You can create Sample and Population variants
					for both the functions. You can create these calculations through the
					calculations editor in analysis mode.  | June 11, 2019 | 
| Hide/Show columns in table visualizations | In Amazon QuickSight, you can hide or show columns in visualizations that use the
						 | June 11, 2019 | 
| Conditional string functions on SPICE | We added support for  | June 11, 2019 | 
| Choose period granularity for date differences | We added an optional parameter to  | June 11, 2019 | 
| Duplicate visuals | In Amazon QuickSight, you can now duplicate visuals. For more information, see
						 | May 21, 2019 | 
| Angled data labels | In Amazon QuickSight, data labels that are too long are now angled by default on
					vertical bar, combo, and line charts. For more information, see  | May 21, 2019 | 
| New languages added | Amazon QuickSight is now available in 10 languages: English, German, Spanish,
					French, Portuguese, Italian, Japanese, Korean, Simplified Chinese, and
					Traditional Chinese. For more information, see  | April 8, 2019 | 
| New aggregation function | Amazon QuickSight supports aggregating by percentile. This function helps you
					understand the distribution of your data. For more information, see  | April 8, 2019 | 
| Customize how many data points to display | You can now format your visuals to display a custom number of data points or
					groups before showing the "other" category. This feature is available for bar
					charts, combo charts, line charts, pie charts, heat maps, and tree maps. For
					more information, see  | April 8, 2019 | 
| ML-powered forecasting | With forecasting powered by machine learning and what-if analyses in
					Amazon QuickSight, nontechnical users can now easily forecast their key business
					metrics. No ML expertise or Microsoft Excel data modeling is required. The
					built-in ML algorithm in Amazon QuickSight is designed to handle complex real-world
					scenarios. Amazon QuickSight uses ML to provide more reliable forecasts than
					traditional means. For more information, see  | March 14, 2019 | 
| ML-powered anomaly detection | Amazon QuickSight uses proven Amazon technology to continuously run ML-powered
					anomaly detection on millions of metrics and billions of data points. This
					anomaly detection enables you to get deep insights that are often buried in the
					aggregates, not visible in plain sight, and not scalable with manual analysis.
					With ML-powered anomaly detection, there's no need for manual analysis,
					custom development, or ML domain expertise. For more information, see  | March 14, 2019 | 
| Automatic narratives | Automatic narratives provide key insights in everyday language, embedded
					contextually in your dashboard, saving hours on manual analysis. With automatic
					narratives, Amazon QuickSight interprets the charts and tables in your dashboard and
					provides a number of suggested insights in natural language. Depending on the
					shape and form of your data, you might get different suggestions. For example,
					you might see what the day-over-day changes look like, what was the highest
					sales date, or what the growth rate is. Or you might see what the forecast looks
					like for the next seven days. As the author of the dashboard, you can customize
					the computations and business language for your needs. You can use automatic
					narratives to effectively tell the story of your data in plain language. For
					more information, see  | March 14, 2019 | 

## Previous updates

		The following table describes the important changes in each release of the *Amazon Quick User Guide* before March 4, 2019.

| Change | Description | Date changed | 
|---|---|---|
| New features | Using custom window functions, you can calculate any aggregation
								for a defined window at the point of selection. You can define the
								window interval before and after any point in time. You can also do
								calculations for that window using the  Send email reports with data tailored to each of your users and
								groups. You can now create email reports for datasets that use
								row-level security. Amazon QuickSight generates a custom email snapshot
								for each user or group based on their data permission that is
								defined in the dashboard. RLS for email reports works for both
								scheduled and ad hoc emails. For more information, see  Amazon QuickSight now supports unbounded cardinality. That means you
								can have more than 10,000 values in your control or filter. For more
								information, see  You can create a datetime parameter that has no static default
								value. Filters on these parameters become active after you choose a
								value. For more information, see  | March 4, 2019 | 
| New features | There are new table calculations available: | February 7, 2019 | 
| New features | Amazon QuickSight supports emailing reports that use row-level security, using controls with unbounded cardinality, and creating datetime parameters with no default values. For more information, see the following: | January 22, 2019 | 
| New features | We added conditional aggregations, including  Pivot tables now support infinite scrolling through millions of rows. You can add up to 20 fields for columns, and 20 fields for rows. Plus, you can add subtotals and totals to rows and columns. For more information, see the following: | January 10, 2019 | 
| New feature | We enhanced the join editor to increase usability and functionality. You can now add tables from one or more schemas on the same data source, or add the same table twice. For more information, see  | January 3, 2019 | 
| New SDK | You can embed dashboards and manage users or groups by using the
								Amazon QuickSight SDKs. For more information, see  | November 27, 2018 | 
| New features | You can use groups with row-level security (RLS), and you can add cascading controls for parameters. For more information, see the following: | November 20, 2018 | 
| Function renamed | We renamed the percentile function to make it more intuitive. Its
								new name is  | November 12, 2018 | 
| New features | Use a top and bottom filter to show the top or bottom n for the
								field you choose, based on values in another field. For example, you
								could choose to show the top five sales people based on revenue. For
								more information, see  Use cascading controls to limit the values displayed in the
								controls, so they only show values that are relevant to what is
								selected in other controls. For more information, see  | November 1, 2018 | 
| New feature | Use JSON native data types with  | October 30, 2018 | 
| New features | Use date functions to find out what quarter a date is in: Add parameters to URLs. For more information see,  | September 10, 2018 | 
| New features | You can sort strings in SPICE datasets. For more
								information on these features, see  | August 20, 2018 | 
| New features | You can schedule emailed reports, and add data labels to your visuals. For more information on these features, see the following sections: | August 15, 2018 | 
| New features | You can create table calculations, using aggregated measures to discover how dimensions influence measures or each other. Also, you can visualize time data at granularities as low as one minute. For more information on these features, see the following sections: | August 8, 2018 | 
| New features | You can replace datasets, customize labels, and format dimensions that are aggregated with count and count distinct. Also, new visuals start out smaller in size. For more information on these features, see the following sections: | June 21, 2018 | 
| New features and a new AWS Region | You can upgrade your Amazon QuickSight subscription from Standard edition to Enterprise edition. In Enterprise edition, Amazon QuickSight supports usage-based pricing for users in the reader role, sharing dashboards with all users in the reader role, and hourly refresh of datasets. Amazon QuickSight also supports private connections to data in a VPC with a private subnet in Enterprise edition. In both editions, Amazon QuickSight supports parameters with on-sheet controls, dashboard co-ownership, custom URL actions, and 25-GB SPICE datasets. Also, Amazon QuickSight is available in Asia Pacific (Tokyo). For more information on these features, see the following sections: 
 | May 30, 2018 | 
| New feature | Amazon QuickSight supports quick sorting from axis labels, duplicating datasets, and showing or hiding totals on tabular reports. Also, you can add custom SQL to a dataset earlier in the creation workflow. For more information on these features, see the following sections: | May 25, 2018 | 
| New features | You can use Amazon QuickSight to connect to Software as a Service
								(SaaS) providers. For more information, see  You can import JSON files to Amazon QuickSight. For more information,
								see  | April 9, 2018 | 
| New feature | You can use Amazon QuickSight with Amazon S3 files that are in a different
								AWS account. For more information, see  | November 20, 2017 | 
| New visual types | You can create visuals using maps. You can also view tabular data
								in a visual. For more information on preparing geospatial data for
								use in a visual, see  | November 20, 2017 | 
| New features | Amazon QuickSight can support 1000 columns in a dataset. For more
							information, see [Data source quotas](https://docs.aws.amazon.com/quicksight/latest/user/data-source-limits.html). Calculated fields
							are supported in SPICE datasets. For more information,
							see[Adding calculated fields](https://docs.aws.amazon.com/quicksight/latest/user/adding-a-calculated-field-analysis.html). Also, high
							cardinality values, which often display as a long tail on a visual, are
							placed into a category calledother. For more
							information, see[Visual types in Amazon QuickSight](https://docs.aws.amazon.com/quicksight/latest/user/working-with-visual-types.html). | November 20, 2017 | 
| New feature | In Enterprise edition, you can restrict access to a dataset by
								adding row-level security. To learn more, see  | October 20, 2017 | 
| New visual type | You can create visuals using combo charts. To learn more about
								combo charts, see  | October 20, 2017 | 
| New features | Amazon QuickSight supports creating custom aggregations for calculated
							fields in analyses, custom date formats, and copies of dashboards. For
							more information on aggregating calculated fields, see [Aggregate functions](https://docs.aws.amazon.com/quicksight/latest/user/calculated-field-aggregations.html). For more
							information on using unsupported dates by creating a custom date format,
							see[Using unsupported or custom dates](https://docs.aws.amazon.com/quicksight/latest/user/using-unsupported-dates.html). For
							more information on duplicating dashboards, see[Copying an QuickSight dashboard](https://docs.aws.amazon.com/quicksight/latest/user/copying-a-dashboard.html). | September 25, 2017 | 
| New feature | You can combine multiple filters using the And/Or operators. To
								learn more about filter groups, see  | August 31, 2017 | 
| New data source | Amazon QuickSight supports Amazon S3 Analytics. | August 31, 2017 | 
| New Features | Amazon QuickSight supports importing ZIP files from Amazon S3. There is also a
							new search feature, to simplify finding analyses, datasets, and
							dashboards. For more information on the search feature, see [Using the QuickSight
							console](https://docs.aws.amazon.com/quicksight/latest/user/using-the-quicksight-console.html). | August 31, 2017 | 
| New AWS Regions | Amazon QuickSight is now available in Asia Pacific (Singapore) and Asia Pacific (Sydney). | August 8, 2017 | 
| New feature | Amazon QuickSight supports Snowflake cloud data warehouse. | July 31, 2017 | 
| New feature | Amazon QuickSight added a new aggregation: Count Distinct. To learn
								more, see  | July 19, 2017 | 
| New feature | Amazon QuickSight supports exploring Amazon S3 analytics data from an
								Amazon QuickSight dashboard that you reach from the AWS Management
								Console. To learn more, see  | July 5, 2017 | 
| New feature | Amazon QuickSight supports Federated Single Sign-On (IAM Identity Center) in
								Enterprise Edition. To learn more, see  | May 25, 2017 | 
| New feature | Amazon QuickSight supports Amazon Redshift Spectrum. To learn more, see  | May 25, 2017 | 
| New feature | Amazon QuickSight supports Federated Single Sign-On (IAM Identity Center) in Standard
								Edition. To learn more, see  | May 25, 2017 | 
| New feature | Amazon QuickSight supports just-in-time (JIT) user provisioning through
								the following policy actions:  | May 25, 2017 | 
| New feature | Amazon QuickSight supports direct connections to Teradata 14.0 and later. | May 25, 2017 | 
| New feature | Amazon QuickSight added relative date filters for datasets and visuals.
								To learn more, see  | May 25, 2017 | 
| New feature | Amazon QuickSight supports connecting to Apache Spark and Presto. To
								learn more, see  | May 3, 2017 | 
| New feature | Amazon QuickSight supports operational logging with AWS CloudTrail. To learn
								more, see  | April 28, 2017 | 
| New feature |  Amazon QuickSight is available in US East (Ohio). To learn more
								about AWS Regions, see  | April 11, 2017 | 
| New feature | 
 | April 6, 2017 | 
| New feature |  You can now export to a comma-separated value (CSV) format file
								using Amazon QuickSight. To learn more, see  | March 21, 2017 | 
| New feature |  You can now schedule data refreshes for SPICE
								datasets. To learn more, see  | February 14, 2017 | 
| New feature |  You can now connect to Amazon Athena databases and use them as data
								sources in Amazon QuickSight. To learn more, see  | December 22, 2016 | 
| New edition |  Amazon QuickSight now offers an Enterprise edition as well as a
								Standard edition. Both editions offer a full set of features for
								creating and sharing data visualizations, and Enterprise edition
								additionally offers encryption at rest and Active Directory
								integration. When you choose to use Enterprise edition, you select a
								Microsoft Active Directory directory in Directory Service and use that active
								directory to identify and manage your Amazon QuickSight users and
								administrators. To learn more, see  | December 15, 2016 | 
| New guide |  This is the first release of  | November 15, 2016 |