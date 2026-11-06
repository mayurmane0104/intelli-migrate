# https://docs.aws.amazon.com/quick/latest/userguide/amazon-quicksuite-doc-release-notes.rss

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/amazon-quicksuite-doc-release-notes.rss](https://docs.aws.amazon.com/quick/latest/userguide/amazon-quicksuite-doc-release-notes.rss)

---

```
<?xml version="1.0" encoding="UTF-8"?>
<rss xmlns:atom="http://www.w3.org/2005/Atom" version="2.0">
   <channel>
      <title>Amazon Quick Documentation Release Notes</title>
      <link>https://docs.aws.amazon.com/quick/latest/userguide/</link>
      <description>A RSS feed containing the latest updates on https://docs.aws.amazon.com/quick/latest/userguide/.</description>
      <language>en-us</language>
      <atom:link href="https://docs.aws.amazon.com/quick/latest/userguide/amazon-quicksuite-doc-release-notes.rss"
                 rel="self"
                 type="application/rss+xml"/>
      <lastBuildDate>Tue, 16 Jun 2026 01:50:01 GMT</lastBuildDate>
      <item>
         <title>OneDrive knowledge base admin-managed setup</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Added admin-managed connection support for the Microsoft OneDrive
					knowledge base connector, including service credentials setup with
					AWS KMS signing, certificate-based authentication, and tenant-wide
					crawling of all users' OneDrive content. Admin-managed OneDrive
					knowledge bases always enforce document-level access control (ACL)
					with real-time verification at query time. For more information, see
					<a href="https://docs.aws.amazon.com/quicksuite/latest/userguide/onedrive-kb-admin-managed.html">Admin-managed setup</a>.</description>
         <pubDate>Mon, 1 Jun 2026 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#OneDrive_knowledge_base_admin-managed_setup_2026-06-01</guid>
      </item>
      <item>
         <title>Web search processed in-Region for Sydney and Tokyo</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Updated cross-Region web search documentation to reflect that web search queries originating in Asia Pacific (Sydney) and Asia Pacific (Tokyo) are now processed in the originating Region and are no longer routed to US East (N. Virginia). For more information, see <a href="https://docs.aws.amazon.com/quicksuite/latest/userguide/regions.html#web-search-cross-region">Cross-Region calls for web search</a>.</description>
         <pubDate>Fri, 29 May 2026 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Web_search_processed_in-Region_for_Sydney_and_Tokyo_2026-05-29</guid>
      </item>
      <item>
         <title>VPC support for MCP integration</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now connect Amazon Quick MCP integrations to private MCP
					servers that are reachable from a virtual private cloud (VPC) by
					selecting a Amazon Quick VPC connection during connector setup. The
					OAuth endpoints used by the MCP server must remain reachable over
					the public internet. Added troubleshooting guidance for connector
					creation, VPC connection issues, and Microsoft Entra ID errors. For
					more information, see <a href="https://docs.aws.amazon.com/quicksuite/latest/userguide/mcp-integration.html">Model Context Protocol (MCP)
						integration</a>.</description>
         <pubDate>Fri, 29 May 2026 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#VPC_support_for_MCP_integration_2026-05-29</guid>
      </item>
      <item>
         <title>Updated HubSpot integration documentation</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Restructured the HubSpot integration topic to follow the
					built-in action connector format. The topic now covers
					prerequisites, account verification, account configuration,
					Amazon Quick setup, and troubleshooting. The HubSpot action
					connector reads CRM data, including contacts, companies, deals,
					and tickets, and authenticates with a custom OAuth app. For more
					information, see <a href="https://docs.aws.amazon.com/quicksuite/latest/userguide/hubspot-integration.html">HubSpot integration</a>.</description>
         <pubDate>Thu, 28 May 2026 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Updated_HubSpot_integration_documentation_2026-05-28</guid>
      </item>
      <item>
         <title>Clarified IAM permissions for DeleteAccountSubscription</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Clarified that the <code class="code">DeleteAccountSubscription</code> Amazon Quick API
					requires both <code class="code">quicksight:Unsubscribe</code> and
					<code class="code">quicksight:DeleteAccountSubscription</code> IAM permissions. An explicit
					deny on either permission results in an <code class="code">AccessDeniedException</code>. Updated
					the account termination permissions list and IAM policy examples
					accordingly. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/closing-account.html">Closing your Amazon Quick account</a>.</description>
         <pubDate>Wed, 27 May 2026 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Clarified_IAM_permissions_for_DeleteAccountSubscription_2026-05-27</guid>
      </item>
      <item>
         <title>Preview extensions for Microsoft 365</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Added preview extension documentation for Excel, Word, and PowerPoint with simplified deployment through the Microsoft 365 admin center. For more information, see <a href="https://docs.aws.amazon.com/quicksuite/latest/userguide/working-with-extensions-detail.html">Connect Amazon Quick to your applications</a>.</description>
         <pubDate>Tue, 28 Apr 2026 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Preview_extensions_for_Microsoft_365_2026-04-28</guid>
      </item>
      <item>
         <title>New action connectors</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Added action connector documentation for Airtable, Dropbox, Google Analytics, Google Calendar, Google Docs, Google Drive, Google Meet, Google Sheets, Google Slides, Gmail, QuickBooks, and Zoom. Updated existing Slack and Outlook action connectors. For more information, see <a href="https://docs.aws.amazon.com/quicksuite/latest/userguide/action-integrations.html">Action connectors</a>.</description>
         <pubDate>Tue, 28 Apr 2026 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#New_action_connectors_2026-04-28</guid>
      </item>
      <item>
         <title>Free and Plus account documentation</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Added documentation for Amazon Quick Free and Plus accounts created at quick.aws.com, including signup, plans, user management, billing, and account administration. For more information, see <a href="https://docs.aws.amazon.com/quicksuite/latest/userguide/standalone-signup.html">Signing up at quick.aws.com</a> and <a href="https://docs.aws.amazon.com/quicksuite/latest/userguide/standalone-admin-guide.html">Administering Amazon Quick (Free and Plus)</a>.</description>
         <pubDate>Tue, 28 Apr 2026 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Free_and_Plus_account_documentation_2026-04-28</guid>
      </item>
      <item>
         <title>Document and visual creation</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Added documentation for creating documents and visuals including Word, Excel, PowerPoint, PDF, and infographics directly from chat conversations. For more information, see <a href="https://docs.aws.amazon.com/quicksuite/latest/userguide/document-and-visual-creation.html">Document and visual creation</a>.</description>
         <pubDate>Tue, 28 Apr 2026 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Document_and_visual_creation_2026-04-28</guid>
      </item>
      <item>
         <title>Build web applications with apps in Amazon Quick</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Added documentation for apps in Amazon Quick, a feature that lets you build, publish, and share interactive web applications using natural language. For more information, see <a href="https://docs.aws.amazon.com/quicksuite/latest/userguide/using-amazon-quick-apps.html">Build web applications with apps in Amazon Quick</a>.</description>
         <pubDate>Tue, 28 Apr 2026 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Build_web_applications_with_apps_in_Amazon_Quick_2026-04-28</guid>
      </item>
      <item>
         <title>Amazon Quick on desktop</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Added documentation for the Amazon Quick desktop application for macOS and Windows, including local file access, activity feed, scheduled agents, system tools, MCP servers, knowledge graph, and settings. For more information, see <a href="https://docs.aws.amazon.com/quicksuite/latest/userguide/amazon-quick-desktop.html">Amazon Quick on desktop</a>.</description>
         <pubDate>Tue, 28 Apr 2026 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Amazon_Quick_on_desktop_2026-04-28</guid>
      </item>
      <item>
         <title>Visier integration</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Added documentation for the Visier people analytics integration,
					which connects to Visier through MCP server connectivity. You can
					query workforce data, analyze headcount trends, assess retention
					health, and generate workforce briefings. For more information, see
						<a href="https://docs.aws.amazon.com/quicksuite/latest/userguide/visier-integration.html">Visier integration</a>.
				</description>
         <pubDate>Wed, 22 Apr 2026 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Visier_integration_2026-04-22</guid>
      </item>
      <item>
         <title>Spaces file size and storage limit increase</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Increased the file upload size limit for Spaces to 500 MB for PDF,
					Word, and PowerPoint files (50 MB for other file types), and
					increased the total space storage limit from 1 GB to 10 GB. For more
					information, see <a href="https://docs.aws.amazon.com/quicksuite/latest/userguide/working-with-spaces.html">Working with Spaces</a>.</description>
         <pubDate>Tue, 21 Apr 2026 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Spaces_file_size_and_storage_limit_increase_2026-04-21</guid>
      </item>
      <item>
         <title>Confluence knowledge base document-level access controls</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Added document-level access control (ACL) support for the
					Atlassian Confluence Cloud knowledge base connector. Includes
					Atlassian admin credentials setup, real-time permission
					verification at query time, and end-user sign-in flow. For more
					information, see <a href="https://docs.aws.amazon.com/quicksuite/latest/userguide/confluence-kb-acl.html">Document-level access controls</a>.</description>
         <pubDate>Tue, 21 Apr 2026 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Confluence_knowledge_base_document-level_access_controls_2026-04-21</guid>
      </item>
      <item>
         <title>SharePoint knowledge base admin-managed setup</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Added admin-managed connection support for the SharePoint Online
					knowledge base connector, including service credentials setup (2LO) with
					AWS KMS signing, certificate-based authentication, document-level
					access control (ACL) with real-time verification, Sites.Selected
					least-privilege permissions, and specific SharePoint path support.
					For more information, see <a href="https://docs.aws.amazon.com/quicksuite/latest/userguide/sharepoint-kb-admin-managed.html">Admin-managed setup</a>.</description>
         <pubDate>Thu, 16 Apr 2026 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#SharePoint_knowledge_base_admin-managed_setup_2026-04-16</guid>
      </item>
      <item>
         <title>Knowledge base and data source sharing</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Added support for sharing admin-managed SharePoint and Google
					Drive knowledge bases with co-owners, and sharing data source
					connections with other users. For more information, see <a href="https://docs.aws.amazon.com/quicksuite/latest/userguide/sharing-kb-datasources.html">Sharing knowledge bases and data sources</a>.</description>
         <pubDate>Thu, 16 Apr 2026 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Knowledge_base_and_data_source_sharing_2026-04-16</guid>
      </item>
      <item>
         <title>Index usage monitoring</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Added index usage logs (<code class="code">INDEX_USAGE_LOGS</code>) to
					Amazon Quick vended logs for tracking storage consumption across
					knowledge bases and Spaces. Includes CloudWatch Log Insights queries for
					building dashboards. For more information, see <a href="https://docs.aws.amazon.com/quicksuite/latest/userguide/index-usage-monitoring.html">Monitor index storage usage</a>.</description>
         <pubDate>Thu, 16 Apr 2026 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Index_usage_monitoring_2026-04-16</guid>
      </item>
      <item>
         <title>Incremental refresh support for datasets in the new data preparation experience</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now incrementally refresh SQL-based SPICE datasets
					that were created in the new data preparation experience. For more information, see
						<a href="https://docs.aws.amazon.com/quicksight/latest/user/refreshing-imported-data.html#refresh-spice-data-incremental">Incrementally refreshing a dataset</a>.</description>
         <pubDate>Wed, 15 Apr 2026 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Incremental_refresh_support_for_datasets_in_the_new_data_preparation_experience_2026-04-15</guid>
      </item>
      <item>
         <title>ServiceNow integration documentation update</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Rewrote the ServiceNow integration documentation with detailed setup
					instructions for both user authentication (OAuth authorization code) and
					service authentication (client credentials), a complete list of available
					actions derived from the ServiceNow REST API, and a new limitations and
					troubleshooting section. For more information, see
					<a href="https://docs.aws.amazon.com/quicksuite/latest/userguide/servicenow-integration.html">ServiceNow integration</a>.</description>
         <pubDate>Mon, 30 Mar 2026 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#ServiceNow_integration_documentation_update_2026-03-30</guid>
      </item>
      <item>
         <title>Fine-grained ACL support for Google Drive knowledge base</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Added admin-managed connection support for the Google Drive knowledge base
					connector, including Google Workspace configuration with 2-legged OAuth (2LO)
					and document-level access control list (ACL) crawling. For more information, see
						<a href="https://docs.aws.amazon.com/quicksuite/latest/userguide/google-drive-integration.html">Google Drive knowledge base</a>.</description>
         <pubDate>Mon, 30 Mar 2026 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Fine-grained_ACL_support_for_Google_Drive_knowledge_base_2026-03-30</guid>
      </item>
      <item>
         <title>Updated Quick Research documentation</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Updated Quick Research documentation to reflect current UI changes,
					including research mode options (Fast and Deep), updated research objective
					guidance, revised button labels, and added third-party data sources as a
					research material type. For more information, see <a href="https://docs.aws.amazon.com/quicksuite/latest/userguide/using-amazon-quick-research.html">Using Amazon Quick Research</a>.</description>
         <pubDate>Thu, 26 Mar 2026 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Updated_Quick_Research_documentation_2026-03-26</guid>
      </item>
      <item>
         <title>New Relic integration</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Added New Relic integration documentation with setup instructions,
					available actions, and troubleshooting. For more information, see <a href="https://docs.aws.amazon.com/quicksuite/latest/userguide/newrelic-integration.html">New Relic integration</a>.</description>
         <pubDate>Thu, 26 Mar 2026 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#New_Relic_integration_2026-03-26</guid>
      </item>
      <item>
         <title>Region expansion for Tokyo, Frankfurt, and London</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Updated regions documentation to reflect full Amazon Quick support in Tokyo
					(ap-northeast-1), Frankfurt (eu-central-1), and London (eu-west-2). Consolidated
					cross-Region inference (CRIS) documentation into the regions page with updated
					inference boundaries for AU-CRIS, JP-CRIS, EU-CRIS, and US-CRIS geographies,
					and added web search regional availability details. For more information, see
						<a href="https://docs.aws.amazon.com/quicksuite/latest/userguide/regions.html">Supported Regions</a>.</description>
         <pubDate>Tue, 24 Mar 2026 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Region_expansion_for_Tokyo,_Frankfurt,_and_London_2026-03-24</guid>
      </item>
      <item>
         <title>New custom permissions for Spaces and Chat Agents</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Added three new custom permission features: Create Spaces, Share Spaces,
					and Share Chat Agents. For more information,
					see <a href="https://docs.aws.amazon.com/quick/latest/userguide/create-custom-permissions-profile.html">Custom permissions</a>.</description>
         <pubDate>Tue, 24 Mar 2026 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#New_custom_permissions_for_Spaces_and_Chat_Agents_2026-03-24</guid>
      </item>
      <item>
         <title>New Amazon CloudWatch metrics for Amazon Quick index capacity</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Added two new Amazon CloudWatch metrics for monitoring Amazon Quick index billing:
					<code class="code">QuickIndexCapacityConsumedRawFileSizeInGB</code> and
					<code class="code">QuickIndexCapacityRawFileSizeLimitInGB</code>. For more information,
					see <a href="https://docs.aws.amazon.com/quicksuite/latest/userguide/monitoring-quicksight.html">Monitoring data in Amazon QuickSight</a>.</description>
         <pubDate>Tue, 24 Mar 2026 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#New_Amazon_CloudWatch_metrics_for_Amazon_Quick_index_capacity_2026-03-24</guid>
      </item>
      <item>
         <title>Google Drive integration</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Refactored the Google Drive knowledge base integration documentation</description>
         <pubDate>Fri, 20 Mar 2026 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Google_Drive_integration_2026-03-20</guid>
      </item>
      <item>
         <title>Embed custom chat agents</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Added documentation for embedding custom chat agents on external websites,
					including the process for allowing hosting domains and generating embed code. For
					more information, see <a href="https://docs.aws.amazon.com/quicksuite/latest/userguide/working-with-agents.html">Create, customize, and deploy AI-powered chat agents</a>.</description>
         <pubDate>Thu, 19 Mar 2026 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Embed_custom_chat_agents_2026-03-19</guid>
      </item>
      <item>
         <title>Custom permissions update</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Updated custom permissions documentation with new parent capabilities (Scenarios,
					Stories, Topics), new features (Edit Visual with AI, Build Calculation with AI,
					Create Executive Summary, Knowledge Base create/update and sharing), and an Action
					Connectors section documenting per-connector permissions. For more information,
					see <a href="https://docs.aws.amazon.com/quick/latest/userguide/create-custom-permissions-profile.html">Custom permissions</a>.</description>
         <pubDate>Thu, 19 Mar 2026 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Custom_permissions_update_2026-03-19</guid>
      </item>
      <item>
         <title>Quick Automate actions update</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Updated Amazon Quick Automate documentation for the Data tables, Excel, Browser, Custom
					Agent, REST API, Code, and AWS Integrations action categories.</description>
         <pubDate>Wed, 18 Mar 2026 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Quick_Automate_actions_update_2026-03-18</guid>
      </item>
      <item>
         <title>Atlassian Jira Cloud integration</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Added dedicated Atlassian Jira Cloud integration documentation with validated
					OAuth scopes and a complete actions table. For more information, see <a href="https://docs.aws.amazon.com/quicksuite/latest/userguide/jira-integration.html">Atlassian Jira Cloud integration</a>.</description>
         <pubDate>Wed, 18 Mar 2026 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Atlassian_Jira_Cloud_integration_2026-03-18</guid>
      </item>
      <item>
         <title>Atlassian Confluence Cloud integration</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Refactored the Atlassian Confluence Cloud integration documentation with shared
					Atlassian OAuth modules for a consistent setup experience.</description>
         <pubDate>Tue, 17 Mar 2026 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Atlassian_Confluence_Cloud_integration_2026-03-17</guid>
      </item>
      <item>
         <title>Namespace isolation and administrative console clarification</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Clarified the difference in permission models between the Amazon Quick end-user
					console and the administrative console for namespace isolation. For more information,
					see <a href="https://docs.aws.amazon.com/quicksuite/latest/userguide/namespaces.html">Supporting multitenancy with isolated namespaces</a>.</description>
         <pubDate>Mon, 16 Mar 2026 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Namespace_isolation_and_administrative_console_clarification_2026-03-16</guid>
      </item>
      <item>
         <title>MCP integration documentation</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Rewrote the Model Context Protocol (MCP) integration topic with an MCP protocol
					overview, OAuth discovery flow documentation (RFC 9728), and shared Dynamic Client
					Registration (DCR) concepts. For more information, see <a href="https://docs.aws.amazon.com/quicksuite/latest/userguide/mcp-integration.html">Model Context Protocol (MCP) integration</a>.</description>
         <pubDate>Mon, 16 Mar 2026 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#MCP_integration_documentation_2026-03-16</guid>
      </item>
      <item>
         <title>Web Crawler VPC support</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Added VPC support, sitemap discovery, and JavaScript navigation troubleshooting
					to the web crawler integration documentation. For more information, see <a href="https://docs.aws.amazon.com/quicksuite/latest/userguide/web-crawler-integration.html">Web Crawler integration</a>.</description>
         <pubDate>Fri, 13 Mar 2026 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Web_Crawler_VPC_support_2026-03-13</guid>
      </item>
      <item>
         <title>Managing shared folders custom permission</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Added documentation for the managing shared folders custom permission. For more
					information, see <a href="https://docs.aws.amazon.com/quick/latest/userguide/create-custom-permissions-profile.html">Custom permissions</a>.</description>
         <pubDate>Thu, 12 Mar 2026 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Managing_shared_folders_custom_permission_2026-03-12</guid>
      </item>
      <item>
         <title>Chat user preferences</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Added a user preferences section to the chat documentation for managing display
					and notification preferences in Amazon Quick. For more information, see <a href="https://docs.aws.amazon.com/quicksuite/latest/userguide/using-quick-chat.html">Ask questions, explore data, and get insights with chat</a>.</description>
         <pubDate>Wed, 11 Mar 2026 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Chat_user_preferences_2026-03-11</guid>
      </item>
      <item>
         <title>Microsoft 365 integration guides</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Rewrote the Microsoft Outlook, SharePoint, and Teams integration guides with a
					consistent structure that includes full Microsoft Entra setup instructions,
					permission tables with descriptions, and correct OAuth scopes.</description>
         <pubDate>Tue, 10 Mar 2026 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Microsoft_365_integration_guides_2026-03-10</guid>
      </item>
      <item>
         <title>Conversation retention period update</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Updated the chat conversation retention period from 30 days to 90 days. For more
					information, see <a href="https://docs.aws.amazon.com/quicksuite/latest/userguide/using-quick-chat.html">Ask questions, explore data, and get insights with chat</a>.</description>
         <pubDate>Thu, 5 Mar 2026 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Conversation_retention_period_update_2026-03-05</guid>
      </item>
      <item>
         <title>Amazon S3 ACL documentation</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Added document-level access control list (ACL) documentation for the Amazon S3
					integration and a best practices guide for managing ACLs in knowledge bases. For
					more information, see <a href="https://docs.aws.amazon.com/quicksuite/latest/userguide/s3-acl.html">Document-level ACLs</a>.</description>
         <pubDate>Mon, 2 Mar 2026 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Amazon_S3_ACL_documentation_2026-03-02</guid>
      </item>
      <item>
         <title>Asia Pacific (Malaysia) Region support</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Added the Asia Pacific (Malaysia) ap-southeast-5 Region to the list of supported
					Amazon Quick Sight Regions, including the API endpoint and IP address range. For more
					information, see <a href="https://docs.aws.amazon.com/quicksuite/latest/userguide/regions.html">Supported Regions</a>.</description>
         <pubDate>Sun, 1 Mar 2026 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Asia_Pacific_(Malaysia)_Region_support_2026-03-01</guid>
      </item>
      <item>
         <title>Quick Flows vs Quick Automate comparison</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Added a comparison section to the automations landing page to help users choose
					between Amazon Quick Flows and Amazon Quick Automate based on their workflow needs. For more information,
					see <a href="https://docs.aws.amazon.com/quicksuite/latest/userguide/flows-vs-automate.html">Choosing between Quick Flows and Quick Automate</a>.</description>
         <pubDate>Fri, 27 Feb 2026 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Quick_Flows_vs_Quick_Automate_comparison_2026-02-27</guid>
      </item>
      <item>
         <title>TLS 1.2 MySQL version requirement</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Documented the requirement for MySQL version 5.7.28 or later to support TLS 1.2
					connections for MySQL data sources.</description>
         <pubDate>Thu, 26 Feb 2026 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#TLS_1.2_MySQL_version_requirement_2026-02-26</guid>
      </item>
      <item>
         <title>ApproveFlowShareRequests custom permission</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Added the ApproveFlowShareRequests custom permission, which controls whether
					users can approve requests to share flows. For more information, see <a href="https://docs.aws.amazon.com/quick/latest/userguide/create-custom-permissions-profile.html">Custom permissions</a>.</description>
         <pubDate>Thu, 26 Feb 2026 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#ApproveFlowShareRequests_custom_permission_2026-02-26</guid>
      </item>
      <item>
         <title>Space extracted text limits</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Updated the extracted text limits for CSV and Excel files in spaces.</description>
         <pubDate>Mon, 23 Feb 2026 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Space_extracted_text_limits_2026-02-23</guid>
      </item>
      <item>
         <title>Knowledge base file size limit increase</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Increased the file size limit for standard text documents in knowledge bases from
					50 MB to 500 MB.</description>
         <pubDate>Mon, 16 Feb 2026 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Knowledge_base_file_size_limit_increase_2026-02-16</guid>
      </item>
      <item>
         <title>Automations usage metrics</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Added a section for tracking Quick Flows, Quick Automate, and Amazon Quick Research usage
					hours in the usage metrics documentation.</description>
         <pubDate>Fri, 6 Feb 2026 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Automations_usage_metrics_2026-02-06</guid>
      </item>
      <item>
         <title>SPICE capacity updates</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Updated SPICE capacity and dataset size documentation to reflect increased
					limits.</description>
         <pubDate>Mon, 2 Feb 2026 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#SPICE_capacity_updates_2026-02-02</guid>
      </item>
      <item>
         <title>Embedding and row-level security guidance</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Added security guidance for embedded analytics to warn against
					AllowedEmbeddingDomains bypass vulnerabilities. Added guidance for using row-level
					security (RLS) in multi-tenant architectures.</description>
         <pubDate>Tue, 27 Jan 2026 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Embedding_and_row-level_security_guidance_2026-01-27</guid>
      </item>
      <item>
         <title>CSV and Excel file size limits</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Updated the file size limits for CSV and Excel uploads to 10 MB.</description>
         <pubDate>Tue, 27 Jan 2026 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#CSV_and_Excel_file_size_limits_2026-01-27</guid>
      </item>
      <item>
         <title>Extension access with Okta and IAM Identity Center</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Updated extension setup instructions for Microsoft Word, Slack, and Teams to
					support Okta as an identity provider with IAM Identity Center. For more information, see <a href="https://docs.aws.amazon.com/quicksuite/latest/userguide/extension-access.html">Extension access</a>.</description>
         <pubDate>Mon, 26 Jan 2026 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Extension_access_with_Okta_and_IAM_Identity_Center_2026-01-26</guid>
      </item>
      <item>
         <title>AgentHours vended logs</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Updated Quick vended logs documentation to include the AgentHours
					log type for tracking agent usage.</description>
         <pubDate>Tue, 6 Jan 2026 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#AgentHours_vended_logs_2026-01-06</guid>
      </item>
      <item>
         <title>New integrations and PagerDuty advance</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Added individual integration pages for 10 new MCP-based services and PagerDuty
					advance integration. Updated the supported integrations table and action connector
					APIs. For more information, see <a href="https://docs.aws.amazon.com/quicksuite/latest/userguide/mcp-integration.html">Model Context Protocol (MCP) integration</a>.</description>
         <pubDate>Mon, 5 Jan 2026 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#New_integrations_and_PagerDuty_advance_2026-01-05</guid>
      </item>
      <item>
         <title>User-driven license upgrades</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Added documentation for user-driven license upgrades, which allow end users to
					request license tier changes. For more information, see <a href="https://docs.aws.amazon.com/quicksuite/latest/userguide/user-driven-upgrades.html">User-driven license upgrades</a>.</description>
         <pubDate>Mon, 29 Dec 2025 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#User-driven_license_upgrades_2025-12-29</guid>
      </item>
      <item>
         <title>Flows in browser extension</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Added documentation for using Amazon Quick Flows in the browser extension. For more
					information, see <a href="https://docs.aws.amazon.com/quicksuite/latest/userguide/flows-in-browser-extension.html">Using Amazon Quick Flows in browser extension</a>.</description>
         <pubDate>Mon, 15 Dec 2025 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Flows_in_browser_extension_2025-12-15</guid>
      </item>
      <item>
         <title>Add IAM Identity Center support for extensions</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Added documentation for adding Amazon Quick extensions to Microsoft Word, Microsoft Office, Microsoft Teams, and Slack with accounts that 
					use IAM Identity Center. For more
					information, see <a href="https://docs.aws.amazon.com/quicksuite/latest/userguide/extension-access.html">Extension access</a>.</description>
         <pubDate>Wed, 19 Nov 2025 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Add_IAM_Identity_Center_support_for_extensions_2025-11-19</guid>
      </item>
      <item>
         <title>New data preparation experience</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Added documentation for the new visual data preparation experience in Amazon Quick Sight. For more
					information, see <a href="https://docs.aws.amazon.com/quicksuite/latest/userguide/data-prep-experience-new.html">Preparing data with the new data preparation experience</a>.</description>
         <pubDate>Mon, 20 Oct 2025 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#New_data_preparation_experience_2025-10-20</guid>
      </item>
      <item>
         <title>New Amazon Quick capabilities</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Amazon Quick provides an integrated suite of AI-powered analytics, automation, and 
					research tools that transcend traditional business intelligence.</description>
         <pubDate>Thu, 9 Oct 2025 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#New_Amazon_Quick_capabilities_2025-10-09</guid>
      </item>
      <item>
         <title>Amazon QuickSight rebrands to Amazon Quick</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Amazon QuickSight has been rebranded to Amazon Quick, expanding from a standalone business 
					intelligence service to a comprehensive analytics and AI platform. QuickSight continues as 
					Amazon Quick Sight, a core component within the Quick ecosystem.</description>
         <pubDate>Thu, 9 Oct 2025 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Amazon_QuickSight_rebrands_to_Amazon_Quick_2025-10-09</guid>
      </item>
      <item>
         <title>Font customization</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Authors can now customize fonts for data labels and axes in supported charts, in addition
					to the previously supported font customizations for visual titles, subtitles, and legends, 
					as well as table and pivot table headers.</description>
         <pubDate>Mon, 6 Oct 2025 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Font_customization_2025-10-06</guid>
      </item>
      <item>
         <title>Google Sheets data source</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now create datasets using a Google Sheets data source. Admins will need to perform
				a one-time setup to enable Google Sheets as a data source.</description>
         <pubDate>Sat, 27 Sep 2025 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Google_Sheets_data_source_2025-09-27</guid>
      </item>
      <item>
         <title>Q&A null support</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Q&A now supports comprehensive support for null value handling, enabling users to
					create more sophisticated analyses and answer complex business questions.</description>
         <pubDate>Thu, 18 Sep 2025 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Q&A_null_support_2025-09-18</guid>
      </item>
      <item>
         <title>Interactive Highchart features</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Highchart visualizations now support custom actions, highlighting, and custom field color
				consistencies, allowing you to create interactive and visually cohesive charts that integrate
				seamlessly with other visuals.</description>
         <pubDate>Tue, 2 Sep 2025 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Interactive_Highchart_features_2025-09-02</guid>
      </item>
      <item>
         <title>Calculated fields limitation increase</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>The number of limits for calculated fields in an analysis has increased from 200 to 500. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/analysis-item-limits">Item limits for analyses</a>.</description>
         <pubDate>Fri, 15 Aug 2025 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Calculated_fields_limitation_increase_2025-08-15</guid>
      </item>
      <item>
         <title>Apache Impala data source</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now create datasets using an Apache Impala data source.</description>
         <pubDate>Fri, 1 Aug 2025 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Apache_Impala_data_source_2025-08-01</guid>
      </item>
      <item>
         <title>Improve Q&A accuracy with custom instructions</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Authors can now curate reponses to questions by adding domain-specific knowledge
				that cannot be captured through a topic's metadata settings. This ensures more accurate,
				relevant, and tailored answers that are better suited for business needs.</description>
         <pubDate>Fri, 18 Jul 2025 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Improve_Q&A_accuracy_with_custom_instructions_2025-07-18</guid>
      </item>
      <item>
         <title>New topic: Trusted identity propagation support with Athena data sources</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Added information about using trusted identity propagation with QuickSight and Athena. For more information, 
					see <a href="https://docs.aws.amazon.com//quicksight/latest/user/athena-trusted-identity-propagation.html">Using trusted 
						identity propagation with Athena</a>.</description>
         <pubDate>Mon, 30 Jun 2025 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#New_topic:_Trusted_identity_propagation_support_with_Athena_data_sources_2025-06-30</guid>
      </item>
      <item>
         <title>2 billion row SPICE datasets</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>QuickSight now supports SPICE datasets that contain up to 2 billion (2,000,000,000) rows. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/data-source-limits">SPICE quotas for imported data</a>.</description>
         <pubDate>Mon, 30 Jun 2025 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#2_billion_row_SPICE_datasets_2025-06-30</guid>
      </item>
      <item>
         <title>Topic Permissions</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Authors can now manage permissions for dashboards and their linked topics from a single
					location. Control topic viewer access directly from a dashboard's sharing preferences,
				eliminating the need to manage permissions in multiple locations.</description>
         <pubDate>Fri, 18 Apr 2025 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Topic_Permissions_2025-04-18</guid>
      </item>
      <item>
         <title>Sheet Highlighting</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Added the ability to highlight specific data points across visuals in a sheet. When
					you select or hover over a data point on a visual, related data across other visuals
					will stand out, while unrelated data is dimmed.</description>
         <pubDate>Fri, 11 Apr 2025 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Sheet_Highlighting_2025-04-11</guid>
      </item>
      <item>
         <title>Updated topic: Opting out of Amazon Q in Quick</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Added additional information and guidance for opting out of Amazon Q in Quick. For more
					information, see <a href="https://docs.aws.amazon.com//quicksight/latest/user/generative-bi-opt-out.html">Opting out of Amazon Q in Quick</a>.</description>
         <pubDate>Tue, 8 Apr 2025 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Updated_topic:_Opting_out_of_Amazon_Q_in_Quick_2025-04-08</guid>
      </item>
      <item>
         <title>Enable Generative BI features in embedded dashboards and consoles</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Added documentation for adding executive summaries to embedded dashboards, and
					adding executive summaries, data stories, authoring, and Q&A to embedded
					consoles. For more information, see <a href="https://docs.aws.amazon.com//quicksight/latest/user/embedded-analytics-api.html.html">Embedding with the Amazon QuickSight APIs</a>.</description>
         <pubDate>Mon, 31 Mar 2025 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Enable_Generative_BI_features_in_embedded_dashboards_and_consoles_2025-03-31</guid>
      </item>
      <item>
         <title>Customize alert emails</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Previously, the custom email template in your QuickSight account only
					affected dashboard report and pixel perfect report emails. Now, it also customizes
					alert emails. For more information, see <a href="https://docs.aws.amazon.com//quicksight/latest/user/customizing-quicksight-email-templates.html">Customizing report and alert emails</a>.</description>
         <pubDate>Mon, 31 Mar 2025 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Customize_alert_emails_2025-03-31</guid>
      </item>
      <item>
         <title>Rules Dataset flag</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>A Rules Dataset flag has been implemented to distinguish permission datasets used for
				row-level security from regular datasets.</description>
         <pubDate>Fri, 28 Mar 2025 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Rules_Dataset_flag_2025-03-28</guid>
      </item>
      <item>
         <title>Publish a previous version of a dashboard</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now revert back to a previous version of a dashboard by searching for it under
				the dashboard's <b>Version History</b> and publishing it. Each dashboard can store
				up to 1000 versions that are never deleted.</description>
         <pubDate>Fri, 28 Mar 2025 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Publish_a_previous_version_of_a_dashboard_2025-03-28</guid>
      </item>
      <item>
         <title>Scenarios general availability</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Updated the scenarios documentation to support its general availability
					release. For more information, see <a href="https://docs.aws.amazon.com//quicksight/latest/user/scenarios.html">Working with
						scenarios in Amazon QuickSight</a>.</description>
         <pubDate>Tue, 25 Mar 2025 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Scenarios_general_availability_2025-03-25</guid>
      </item>
      <item>
         <title>New Region</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Amazon QuickSight is now available in the Europe (Spain) (eu-south-2) Region.
					For more information, see <a href="https://docs.aws.amazon.com//quicksight/latest/user/regions-qs.html">Supported
						AWS Regions for Amazon QuickSight</a>.</description>
         <pubDate>Tue, 11 Mar 2025 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#New_Region_2025-03-11</guid>
      </item>
      <item>
         <title>Dashboard Q&A experience</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Amazon QuickSight authors can now to turn on the Q&A experience directly from
					their dashboards in one click without the need to create a topic in
					QuickSight. For more information, see <a href="https://docs.aws.amazon.com//quicksight/latest/user/dashboard-qa.html">Turn on the
						Dashboard Q&A experience in Amazon QuickSight</a>.</description>
         <pubDate>Fri, 31 Jan 2025 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Dashboard_Q&A_experience_2025-01-31</guid>
      </item>
      <item>
         <title>Unique key configuration</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Amazon QuickSight authors can now configure a unique key column to a
					QuickSight dataset during data preparation. For more information, see
						<a href="https://docs.aws.amazon.com//quicksight/latest/user/set-unique-key.html">Adding a unique key to an Amazon QuickSight dataset</a>.</description>
         <pubDate>Thu, 19 Dec 2024 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Unique_key_configuration_2024-12-19</guid>
      </item>
      <item>
         <title>Amazon QuickSight scenarios</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Amazon QuickSight Pro users can now use Amazon Q in Quick to create scenarios to analyze
					complex business problems with simple natural language. For more information,
					see <a href="https://docs.aws.amazon.com//quicksight/latest/user/scenarios.html">Working
						with scenarios in Amazon QuickSight</a>.</description>
         <pubDate>Wed, 4 Dec 2024 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Amazon_QuickSight_scenarios_2024-12-04</guid>
      </item>
      <item>
         <title>Augmenting Amazon QuickSight insights with Amazon Q Business</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Amazon QuickSight account admins can now connect their QuickSight account to
					Amazon Q Business to augment insights with unstructured data sources. For more
					information, see <a href="https://docs.aws.amazon.com//quicksight/latest/user/generative-bi-q-business.html">Augmenting Amazon QuickSight insights with Amazon Q Business</a>.</description>
         <pubDate>Tue, 3 Dec 2024 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Augmenting_Amazon_QuickSight_insights_with_Amazon_Q_Business_2024-12-03</guid>
      </item>
      <item>
         <title>Prompted reports</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Amazon QuickSight authors can now create prompts on pixel-perfect reports to allow
					dashboard users to filter data in on-demand and scheduled reports. For more
					information, see <a href="https://docs.aws.amazon.com//quicksight/latest/user/paginated-reports-prompts.html">Setting up prompts for pixel perfect reports</a>.</description>
         <pubDate>Fri, 22 Nov 2024 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Prompted_reports_2024-11-22</guid>
      </item>
      <item>
         <title>New visual type: layer map</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Amazon QuickSight now supports layer map visuals. For more information, see <a href="https://docs.aws.amazon.com//quicksight/latest/user/layered-maps.html">Using layer
						maps</a>.</description>
         <pubDate>Fri, 22 Nov 2024 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#New_visual_type:_layer_map_2024-11-22</guid>
      </item>
      <item>
         <title>New visual type: image component</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now add images to QuickSight dashboards and analyses with image
					component visuals in Amazon QuickSight For more information, see <a href="https://docs.aws.amazon.com//quicksight/latest/user/image-component.html">Using
						image components</a>.</description>
         <pubDate>Fri, 22 Nov 2024 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#New_visual_type:_image_component_2024-11-22</guid>
      </item>
      <item>
         <title>New visual type: Highcharts visual</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Amazon QuickSight authors can now configure Highcharts visuals in
					QuickSight. For more information, see <a href="https://docs.aws.amazon.com//quicksight/latest/user/highchart.html">Using
						Highcharts</a>.</description>
         <pubDate>Fri, 22 Nov 2024 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#New_visual_type:_Highcharts_visual_2024-11-22</guid>
      </item>
      <item>
         <title>Import visual public preview</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>(Public preview) Amazon QuickSight authors can now import QuickSight visuals
					from one dashboard or analysis to a new analysis that has access permissions.
					For more information, see <a href="https://docs.aws.amazon.com//quicksight/latest/user/import-visuals.html">Importing
						Amazon QuickSight visuals to an analysis</a>.</description>
         <pubDate>Fri, 22 Nov 2024 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Import_visual_public_preview_2024-11-22</guid>
      </item>
      <item>
         <title>Font customization</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Amazon QuickSight dashboard viewers can now schedule their own dashboard reports
					for themselves. For more information, see <a href="https://docs.aws.amazon.com//quicksight/latest/user/reader-scheduling.html">Creating a reader generated report in Amazon QuickSight</a>.</description>
         <pubDate>Fri, 22 Nov 2024 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Font_customization_2024-11-22</guid>
      </item>
      <item>
         <title>Font customization</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Amazon QuickSight authors can now customize the font, font size, and font color of
					visual titles, subtitles, legends, headers, and cells. For more information, see
						<a href="https://docs.aws.amazon.com//quicksight/latest/user/customizing-a-visual-title.html">Titles and subtitles on visual types in QuickSight</a>.</description>
         <pubDate>Fri, 22 Nov 2024 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Font_customization_2024-11-22</guid>
      </item>
      <item>
         <title>Cross-Region inference with Amazon Q in Quick</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Amazon Q in Quick now supports cross-Region inferencing. For more information, see <a href="https://docs.aws.amazon.com//quicksight/latest/user/q-cross-region-inferencing.html">Cross-Region inference with Amazon Q in Quick</a>.</description>
         <pubDate>Thu, 21 Nov 2024 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Cross-Region_inference_with_Amazon_Q_in_Quick_2024-11-21</guid>
      </item>
      <item>
         <title>Create a custom brand in Amazon QuickSight</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Amazon QuickSight account admins can now customize their application's
					branding and visual theme to align with their organization's guidelines.
					For more information, see <a href="https://docs.aws.amazon.com//quicksight/latest/user/brand-customization.html">Amazon QuickSight brand customization</a>.</description>
         <pubDate>Thu, 14 Nov 2024 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Create_a_custom_brand_in_Amazon_QuickSight_2024-11-14</guid>
      </item>
      <item>
         <title>Connect to Starburst with OAuth client credentials</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now use OAuth client credentials to connect your
					Amazon QuickSight account with Starburst through the QuickSight APIs. For more
					information, see <a href="https://docs.aws.amazon.com//quicksight/latest/user/create-connection-to-starburst-oauth.html">Creating an Amazon Quick Sight data source connection to Starburst with
							OAuth client credentials</a>.</description>
         <pubDate>Fri, 8 Nov 2024 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Connect_to_Starburst_with_OAuth_client_credentials_2024-11-08</guid>
      </item>
      <item>
         <title>Connect to Snowflake with OAuth client credentials</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now use OAuth client credentials to connect your
					Amazon QuickSight account with Snowflake through the QuickSight APIs. For more
					information, see <a href="https://docs.aws.amazon.com//quicksight/latest/user/create-connection-to-snowflake-oauth.html">Creating an Amazon QuickSight data source connection to Snowflake with
							OAuth client credentials</a>.</description>
         <pubDate>Fri, 8 Nov 2024 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Connect_to_Snowflake_with_OAuth_client_credentials_2024-11-08</guid>
      </item>
      <item>
         <title>Subfolders for restricted shared folders</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Assets that are located in a QuickSight restricted folder can now be
					moved within the restricted folder tree into one or more subfolders. For more
					information, see <a href="https://docs.aws.amazon.com//quicksight/latest/user/folders.html">Organizing assets
						into folders for Amazon QuickSight</a>.</description>
         <pubDate>Tue, 15 Oct 2024 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Subfolders_for_restricted_shared_folders_2024-10-15</guid>
      </item>
      <item>
         <title>Show an apply button</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>QuickSight authors can now add an <b>Apply</b> button to
					a Calendar, Relative date picker, or Multiselect dropdown control that delays
					visual reload until the user chooses <b>Apply</b>. For more
					information, see <a href="https://docs.aws.amazon.com//quicksight/latest/user/filter-controls.html">Adding
						filter controls to analysis sheets</a>.</description>
         <pubDate>Fri, 27 Sep 2024 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Show_an_apply_button_2024-09-27</guid>
      </item>
      <item>
         <title>Data story peronalization</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Amazon Q in Quick now leverages user location and job-related information from your IAM Identity Center
					instance to generate personalized data stories that are more relevant to authors
					and readers. For more information, see <a href="https://docs.aws.amazon.com//quicksight/latest/user/working-with-stories-personalize.html">Personalize data stories in Amazon QuickSight</a>.</description>
         <pubDate>Fri, 27 Sep 2024 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Data_story_peronalization_2024-09-27</guid>
      </item>
      <item>
         <title>Shared view for embedded dashboards</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>QuickSight developers can now use the Amazon QuickSight Embedding SDK
					(version 2.8.0 and higher) to allow readers of embedded dashboards to receive
					and distribute shareable links to their view of an embedded dashboard. For more
					information, see <a href="https://docs.aws.amazon.com//quicksight/latest/user/embedded-view-sharing.html">Share an embedded view</a>.</description>
         <pubDate>Fri, 23 Aug 2024 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Shared_view_for_embedded_dashboards_2024-08-23</guid>
      </item>
      <item>
         <title>5 new regions</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Amazon Q in Quick is now available in 5 new opt-in Regions: Asia Pacific (Mumbai), Canada
					(Central), Europe (Ireland), Europe (London), and South America (SÃ£o Paulo). For
					more information, see <a href="https://docs.aws.amazon.com//quicksight/latest/user/regions.html#regions-aqs">Supported AWS Regions for Amazon Q in Quick</a>.</description>
         <pubDate>Fri, 9 Aug 2024 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#5_new_regions_2024-08-09</guid>
      </item>
      <item>
         <title>Nested filters</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now apply nested filters to QuickSight analyses. For more
					information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/add-a-nested-filter-data-prep.html">Adding nested filters</a>.</description>
         <pubDate>Thu, 1 Aug 2024 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Nested_filters_2024-08-01</guid>
      </item>
      <item>
         <title>Joined datasets in SPICE</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>The size limit for secondary tables of joins for datasets that are stored in
						SPICE have been updated. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/joining-data.html">Joining
						data</a>.</description>
         <pubDate>Wed, 10 Jul 2024 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Joined_datasets_in_SPICE_2024-07-10</guid>
      </item>
      <item>
         <title>Advanced options for paginted reports</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now create repeating sections for pixel perfect reports in Amazon QuickSight.
					For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/qs-reports-repeat-sections.html">Create repeating sections</a>.</description>
         <pubDate>Thu, 27 Jun 2024 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Advanced_options_for_paginted_reports_2024-06-27</guid>
      </item>
      <item>
         <title>4 New Regions</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>QuickSight is now available in 4 new opt-in Regions: Europe (Milan),
					Europe (Zurich), Africa (Cape Town), and Asia Pacific (Jakarta). For more
					information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/regions.html">AWS Regions,
						websites, IP address ranges, and endpoints</a>.</description>
         <pubDate>Tue, 28 May 2024 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#4_New_Regions_2024-05-28</guid>
      </item>
      <item>
         <title>New sorting options for tables in Amazon QuickSight</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>QuickSight Authors can now configure single column, multi column, and
					off-visual sorts for tables in Amazon QuickSight. For more information, see <a href="https://docs.aws.amazon.com//quicksight/latest/user/table-sort.html">Sorting
						tables</a>.</description>
         <pubDate>Mon, 20 May 2024 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#New_sorting_options_for_tables_in_Amazon_QuickSight_2024-05-20</guid>
      </item>
      <item>
         <title>Key management in QuickSight: Updated IAM policy conditions</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>The required IAM policy permissions that grant access to AWS KMS keys in the
					QuickSight console and the QuickSight APIs have been updated. For
					more information, see <a href="https://docs.aws.amazon.com//quicksight/latest/user/iam-policy-examples.html#security_iam_id-based-policy-examples-admin-key-management-console">IAM identity-based policies for Amazon QuickSight: using the admin key
						management console</a>.</description>
         <pubDate>Thu, 16 May 2024 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Key_management_in_QuickSight:_Updated_IAM_policy_conditions_2024-05-16</guid>
      </item>
      <item>
         <title/>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>QuickSight Admins can now update and manage CMKs that are registered to
					a QuickSight account with the QuickSight APIs. For more
					information about creating and managing CMKs with the QuickSight APIs, For more
					information, see <a href="https://docs.aws.amazon.com//quicksight/latest/developerguide/cmk-operations.html">Key management operations</a>.</description>
         <pubDate>Thu, 16 May 2024 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#_2024-05-16</guid>
      </item>
      <item>
         <title>Hide SPICE capacity labels</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>QuickSight Admins can now choose to hide the account-wide
						SPICE capacity usage and remaining size labels from
					QuickSight authors. For more information, see <a href="https://docs.aws.amazon.com//quicksight/latest/user/managing-spice-capacity.html#spice-capacity-hide">Hiding SPICE capacity labels</a>.</description>
         <pubDate>Thu, 2 May 2024 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Hide_SPICE_capacity_labels_2024-05-02</guid>
      </item>
      <item>
         <title>Embed the Generative Q&A experience</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now set up an embedded Q&A that uses enhanced NLQ capabilities
					powered by LLMs. The Q&A is the recommended replacement for the embedded Q
					Search Bar and provides an updated BI expereince for users. For more
					information, see <a href="https://docs.aws.amazon.com//quicksight/latest/user/embedded-analytics-gen-bi-authenticated-users.html">Embed the Amazon Q in Quick Generative Q&A expereince</a>.</description>
         <pubDate>Tue, 30 Apr 2024 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Embed_the_Generative_Q&A_experience_2024-04-30</guid>
      </item>
      <item>
         <title>Amazon Q in Quick: New Pro roles</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Amazon Q integrates with Amazon QuickSight to give QuickSight users access to a
					suite of new generative BI capabilities. With Amazon Q in Quick, you can utilize the
					generative BI authoring experience, create executive summaries of your data, ask
					and answer questions of data, and generate data stories. To get started with
					Amazon Q in QuickSight Generative BI capabilities, upgrade your
					account's users to Admin Pro, Author Pro, or Reader Pro roles. For more
					information, see <a href="https://docs.aws.amazon.com//quicksight/latest/user/generative-bi-get-started.html">Get started with Generative BI</a>.</description>
         <pubDate>Tue, 30 Apr 2024 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Amazon_Q_in_Quick:_New_Pro_roles_2024-04-30</guid>
      </item>
      <item>
         <title>VPC endpoint restrictions</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now create VPC endpoint restrictions in Amazon QuickSight to limit access
					to your QuickSight account. For more information, see <a href="https://docs.aws.amazon.com//quicksight/latest/user/enabling-ip-restrictions.html">Turning on IP and VPC endpoint restrictions in Amazon QuickSight</a>.</description>
         <pubDate>Tue, 9 Apr 2024 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#VPC_endpoint_restrictions_2024-04-09</guid>
      </item>
      <item>
         <title>Account instances of IAM Identity Center for account management</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Amazon QuickSight now supports account instances of IAM Identity Center for identity management.
					For more information, see <a href="https://docs.aws.amazon.com//quicksight/latest/user/managing-users.html">Managing
						user access inside Amazon QuickSight</a>.</description>
         <pubDate>Tue, 9 Apr 2024 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Account_instances_of_IAM_Identity_Center_for_account_management_2024-04-09</guid>
      </item>
      <item>
         <title>Managed policy update</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Amazon QuickSight added a new managed policy to simplify Asset Bundle export
					operations. For more information, see <a href="https://docs.aws.amazon.com//aws-managed-policy/latest/reference/AWSQuickSightAssetBundleExportPolicy.html">AWS managed policy: AWSQuickSightAssetBundleExportPolicy</a>.</description>
         <pubDate>Wed, 27 Mar 2024 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Managed_policy_update_2024-03-27</guid>
      </item>
      <item>
         <title>Managed policy update</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Amazon QuickSight added a new managed policy to simplify Asset Bundle import
					operations. For more information, see <a href="https://docs.aws.amazon.com//aws-managed-policy/latest/reference/AWSQuickSightAssetBundleImportPolicy.html">AWS managed policy: AWSQuickSightAssetBundleImportPolicy</a>.</description>
         <pubDate>Wed, 27 Mar 2024 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Managed_policy_update_2024-03-27</guid>
      </item>
      <item>
         <title>New Q pane</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Amazon QuickSight users that are opted in to the Generative BI perview can now use
					the Q pane to access all relevant Generative BI features. For more information,
					see <a href="https://docs.aws.amazon.com/quicksight/latest/user/quicksight-gen-bi.html">Using Generative BI with Amazon Q in Quick</a>.</description>
         <pubDate>Mon, 25 Mar 2024 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#New_Q_pane_2024-03-25</guid>
      </item>
      <item>
         <title>New Region: China (north)</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Amazon QuickSight is now available in China (Beijing) (cn-north-1). For more
					information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/regions.html">AWS Regions,
						websites, IP address ranges, and endpoints</a>.</description>
         <pubDate>Thu, 25 Jan 2024 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#New_Region:_China_(north)_2024-01-25</guid>
      </item>
      <item>
         <title>Amazon Q Business in Amazon QuickSight</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Amazon Q Business integrates with Amazon QuickSight to give QuickSight users access
					to a suite of new generative BI capabilities. With Amazon Q in Quick, you can utilize the
					generative BI authoring experience, create executive summaries of your data, ask
					and answer questions of data, and generate data stories. For more information,
					see <a href="https://docs.aws.amazon.com//quicksight/latest/user/quicksight-gen-bi.html">Using generative BI with Amazon Q in Quick</a>.</description>
         <pubDate>Tue, 28 Nov 2023 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Amazon_Q_Business_in_Amazon_QuickSight_2023-11-28</guid>
      </item>
      <item>
         <title>Trusted identity propagation in Amazon QuickSight</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>QuickSight authors can now create data sources with trusted identity
					propagation, which allows database administrators to centrally manage data
					security in Amazon Redshift and automatically apply all data security rules to data
					consumers in QuickSight. For more information, see <a href="https://docs.aws.amazon.com//quicksight/latest/user/enabling-access-redshift.html">Enabling trusted identity propagation with Amazon Redshift</a>.</description>
         <pubDate>Sun, 26 Nov 2023 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Trusted_identity_propagation_in_Amazon_QuickSight_2023-11-26</guid>
      </item>
      <item>
         <title>Runtime filtering and theming for embedded dashboards and visuals</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>QuickSight authors can now customize filters and themes for embedded
					dashboards and visuals. For more information, see <a href="https://docs.aws.amazon.com//quicksight/latest/user/customize-and-personalize-embedded-analytics.html">Customizing embedded assets</a>.</description>
         <pubDate>Fri, 17 Nov 2023 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Runtime_filtering_and_theming_for_embedded_dashboards_and_visuals_2023-11-17</guid>
      </item>
      <item>
         <title>Custom time zones and week start days in Amazon QuickSight</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>QuickSight authors can now restrict the functionality that people can
					access in Amazon QuickSight. For more information, see <a href="https://docs.aws.amazon.com//customizing-permissions-to-the-quicksight-console">Customizing access to the Amazon QuickSight console</a>.</description>
         <pubDate>Fri, 17 Nov 2023 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Custom_time_zones_and_week_start_days_in_Amazon_QuickSight_2023-11-17</guid>
      </item>
      <item>
         <title>Custom time zones and week start days in Amazon QuickSight</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>QuickSight authors can now turn on SPICE auto capacity
					purchasing to allow Amazon QuickSight to automatically manage your QuickSight
					account's SPICE capacity. For more information, see <a href="https://docs.aws.amazon.com/managing-spice-capacity.html#spice-auto-capacity">Turning SPICE auto capacity purchasing on</a>.</description>
         <pubDate>Fri, 17 Nov 2023 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Custom_time_zones_and_week_start_days_in_Amazon_QuickSight_2023-11-17</guid>
      </item>
      <item>
         <title>Amazon EventBridge integration</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now integrate your Amazon QuickSight account with Amazon EventBridge. For more
					information, see <a href="https://docs.aws.amazon.com//quicksight/latest/user/events-integration.html">Amazon QuickSight EventBridge integration</a>.</description>
         <pubDate>Fri, 17 Nov 2023 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Amazon_EventBridge_integration_2023-11-17</guid>
      </item>
      <item>
         <title>New look for the QuickSight analysis workspace</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>We've redesigned the Amazon QuickSight analysis workspace. You might encounter
					screenshots or procedural text that doesn't reflect the new look in the
					QuickSight console. We're in the process of updating screenshots and
					procedural text. For more information on QuickSight's new look, see
						<a href="https://aws.amazon.com/blogs//business-intelligence/introducing-new-analysis-experience-on-amazon-quicksight/" rel="noopener noreferrer" target="_blank">Introducing new analysis experience on Amazon QuickSight</a>.</description>
         <pubDate>Thu, 16 Nov 2023 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#New_look_for_the_QuickSight_analysis_workspace_2023-11-16</guid>
      </item>
      <item>
         <title>Custom time zones and week start days in Amazon QuickSight</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>QuickSight authors can now set custom time zones and week start days
					for their analyses. For more information, see <a href="https://docs.aws.amazon.com//quicksight/latest/user/analysis-date-time.html">Customize date and time values of an analysis</a>.</description>
         <pubDate>Tue, 14 Nov 2023 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Custom_time_zones_and_week_start_days_in_Amazon_QuickSight_2023-11-14</guid>
      </item>
      <item>
         <title>Float decimal type</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Decimal values in calculated fields of datasets that are stored in
						SPICE can now be assigned the <code class="code">Fixed</code> or
						<code class="code">Float</code> decimal data type. For more information, see <a href="https://docs.aws.amazon.com//quicksight/latest/user/supported-data-types-and-values.html">Supported data types and values</a>.</description>
         <pubDate>Wed, 8 Nov 2023 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Float_decimal_type_2023-11-08</guid>
      </item>
      <item>
         <title>Custom total values in Amazon QuickSight</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>QuickSight authors can now define the total and subtotal aggregations
					for their table or pivot table visuals from the field wells. For more
					information, see <a href="https://docs.aws.amazon.com//quicksight/latest/user/tables-pivot-tables-custom-totals.html">Custom total values</a>.</description>
         <pubDate>Wed, 25 Oct 2023 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Custom_total_values_in_Amazon_QuickSight_2023-10-25</guid>
      </item>
      <item>
         <title>Restricted and unrestricted shared folders in Amazon QuickSight</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>QuickSight authors can now create restricted and unrestricted shared
					folders with the QuickSight CLI to help organize and manage the
					permissions of important QuickSight assets. For more information, see
						<a href="https://docs.aws.amazon.com//quicksight/latest/user/folders.html">Organizing
						assets into folders for Amazon QuickSight</a>.</description>
         <pubDate>Tue, 24 Oct 2023 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Restricted_and_unrestricted_shared_folders_in_Amazon_QuickSight_2023-10-24</guid>
      </item>
      <item>
         <title>New data source</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>QuickSight now supports connecting to a Trino data source. For more
					information, see <a href="https://docs.aws.amazon.com//quicksight/latest/user/connecting-to-trino.html">Using
						Trino with Amazon QuickSight</a>.</description>
         <pubDate>Fri, 20 Oct 2023 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#New_data_source_2023-10-20</guid>
      </item>
      <item>
         <title>New data source</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>QuickSight now supports connecting to a Starburst data source. For more
					information, see <a href="https://docs.aws.amazon.com//quicksight/latest/user/connecting-to-starburst.html">Using Starburst with Amazon QuickSight</a>.</description>
         <pubDate>Fri, 20 Oct 2023 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#New_data_source_2023-10-20</guid>
      </item>
      <item>
         <title>SageMaker AI Canvas integration</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>QuickSight authors can now export data into SageMaker AI Canvas to build ML
					models that can be sent back to QuickSight and applied to analyses and
					dashboards. For more information, see <a href="https://docs.aws.amazon.com//quicksight/latest/user/sagemaker-canvas-integration.html">Build predictive models with SageMaker AI Canvas</a>.</description>
         <pubDate>Fri, 6 Oct 2023 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#SageMaker_AI_Canvas_integration_2023-10-06</guid>
      </item>
      <item>
         <title>Managed policy update</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>The <code class="code">AWSQuickSightSageMakerPolicy</code> is updated to reflect the
					Amazon QuickSightâ€“SageMaker AI integration. For more information, see <a href="https://docs.aws.amazon.com//aws-managed-policy/latest/reference/AWSQuickSightSageMakerPolicy.html">AWS managed policy: AWSQuickSightSageMakerPolicy</a>.</description>
         <pubDate>Fri, 6 Oct 2023 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Managed_policy_update_2023-10-06</guid>
      </item>
      <item>
         <title>Amazon Redshift run-as role</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>QuickSight authors can now connect Amazon Redshift data with run as role to
					enhance data security with fine grained access policies. For more information,
					see <a href="https://docs.aws.amazon.com//quicksight/latest/user/datasource-run-as-role.html.html">Run queries as an IAM role in Amazon QuickSight</a>.</description>
         <pubDate>Fri, 6 Oct 2023 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Amazon_Redshift_run-as_role_2023-10-06</guid>
      </item>
      <item>
         <title>Generative BI public preview</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>The public preview for Generative BI is now available to users who have a
					QuickSight Q add-on subscription. For more information, see <a href="https://docs.aws.amazon.com//quicksight/latest/user/generative-bi-author-experience.html">Working with Generative BI in QuickSight Q</a>.</description>
         <pubDate>Thu, 28 Sep 2023 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Generative_BI_public_preview_2023-09-28</guid>
      </item>
      <item>
         <title>Freeze table columns in Amazon QuickSight</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now freeze single or groups of table columns in Amazon QuickSight. For more
					information, see <a href="https://docs.aws.amazon.com//quicksight/latest/user/tables-freeze-columns.html">Freeze columns to table visuals</a>.</description>
         <pubDate>Tue, 26 Sep 2023 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Freeze_table_columns_in_Amazon_QuickSight_2023-09-26</guid>
      </item>
      <item>
         <title>Enhanced KPI options in Amazon QuickSight</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>New layouts and formatting options for KPIs are now available in Amazon QuickSight.
					For more information, see <a href="https://docs.aws.amazon.com//quicksight/latest/user/kpi.html">Using
					KPIs</a>.</description>
         <pubDate>Fri, 15 Sep 2023 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Enhanced_KPI_options_in_Amazon_QuickSight_2023-09-15</guid>
      </item>
      <item>
         <title>Scaled folders in Amazon QuickSight</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can create scaled folders that can be shared with thousands of namespaces
					at once with the Amazon QuickSight APIs. For more information, see <a href="https://docs.aws.amazon.com//quicksight/latest/user/folders-scaleds.html">Creating
						scaled folders with the AWS CLI</a>.</description>
         <pubDate>Wed, 30 Aug 2023 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Scaled_folders_in_Amazon_QuickSight_2023-08-30</guid>
      </item>
      <item>
         <title>Excel format reports in Amazon QuickSight</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now create and schedule Excel snapshot reports of a dashboard in
					Amazon QuickSight. For more information, see <a href="https://docs.aws.amazon.com//quicksight/latest/user/sending-reports.html">Scheduling and sending reports by email</a>.</description>
         <pubDate>Thu, 24 Aug 2023 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Excel_format_reports_in_Amazon_QuickSight_2023-08-24</guid>
      </item>
      <item>
         <title>Add contextual row subtitles to pivot tables in Amazon QuickSight</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now add contextual row subtitles to pivot tables in Amazon QuickSight. For
					more information, see <a href="https://docs.aws.amazon.com//quicksight/latest/user/format-tables-pivot-tables-totals.html">Totals and subtotals</a>.</description>
         <pubDate>Wed, 16 Aug 2023 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Add_contextual_row_subtitles_to_pivot_tables_in_Amazon_QuickSight_2023-08-16</guid>
      </item>
      <item>
         <title>New layouts for pivot tables in Amazon QuickSight</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Amazon QuickSight now supports two types of layout for pivot tables: tabular and
					hierarchy. For more information, see <a href="https://docs.aws.amazon.com//quicksight/latest/user/create-pivot-table.html#pivot-table-layout.html">Choosing a layout</a>.</description>
         <pubDate>Fri, 11 Aug 2023 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#New_layouts_for_pivot_tables_in_Amazon_QuickSight_2023-08-11</guid>
      </item>
      <item>
         <title>Default column width Amazon QuickSight</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now set the default column width of your pivot table visuals in
					Amazon QuickSight. For more information, see <a href="https://docs.aws.amazon.com//quicksight/latest/user/format-tables-pivot-tables-resize-rows-columns.html">Row and column size in tables and pivot tables in
					Amazon QuickSight</a>.</description>
         <pubDate>Fri, 11 Aug 2023 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Default_column_width_Amazon_QuickSight_2023-08-11</guid>
      </item>
      <item>
         <title>Amazon QuickSight integration with IAM Identity Center</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now integrate your Amazon QuickSight Enterprise edition account with IAM Identity Center.
					For more information, see <a href="https://docs.aws.amazon.com//quicksight/latest/user/sec-identity-management-identity-center.html">Configure your Amazon QuickSight account with IAM Identity Center</a>.</description>
         <pubDate>Fri, 11 Aug 2023 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Amazon_QuickSight_integration_with_IAM_Identity_Center_2023-08-11</guid>
      </item>
      <item>
         <title>Embedded callback actions at runtime</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now use embedded data point callback actions to build tighter
					integrations between your SaaS application and your Amazon QuickSight embedded
					dashboards and visuals. For more information, see <a href="https://docs.aws.amazon.com//quicksight/latest/user/embedding-custom-actions-callback.html">Add embedded callback actions to at runtime in Amazon QuickSight</a>.</description>
         <pubDate>Wed, 9 Aug 2023 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Embedded_callback_actions_at_runtime_2023-08-09</guid>
      </item>
      <item>
         <title>Working with field level coloring in Amazon QuickSight</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now assign specific colors to specific field values across all visuals
					in a QuickSight analysis or dashboard. For more information, see <a href="https://docs.aws.amazon.com//quicksight/latest/user/format-field-colors.html">Working with field level coloring in Amazon QuickSight</a>.</description>
         <pubDate>Thu, 13 Jul 2023 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Working_with_field_level_coloring_in_Amazon_QuickSight_2023-07-13</guid>
      </item>
      <item>
         <title>Small multiples axis options in Amazon QuickSight</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now configure the x and y axes for each individual panel of a small
					multiples visual in Amazon QuickSight. For more information, see <a href="https://docs.aws.amazon.com//quicksight/latest/user/small-multiples-options.html">Small multiples axis options</a>.</description>
         <pubDate>Thu, 13 Jul 2023 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Small_multiples_axis_options_in_Amazon_QuickSight_2023-07-13</guid>
      </item>
      <item>
         <title>Use the analysis menu in Amazon QuickSight</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now use menu options to efficiently perform tasks without needing to
					manually navigate through your analysis in Amazon QuickSight. For more information,
					see <a href="https://docs.aws.amazon.com//quicksight/latest/user/analysis-menu.html">The
						analysis menu</a>.</description>
         <pubDate>Fri, 7 Jul 2023 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Use_the_analysis_menu_in_Amazon_QuickSight_2023-07-07</guid>
      </item>
      <item>
         <title>Advanced report scheduling options in Amazon QuickSight</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now access more advanced PDF report scheduling options in
					Amazon QuickSight. For more information, see <a href="https://docs.aws.amazon.com//quicksight/latest/user/sending-reports.html#email-reports-from-dashboard">Configuring email report settings for a dashboard in QuickSight
						Enterprise edition</a>.</description>
         <pubDate>Fri, 30 Jun 2023 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Advanced_report_scheduling_options_in_Amazon_QuickSight_2023-06-30</guid>
      </item>
      <item>
         <title>Format visual language data based on language settings in Amazon QuickSight</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now choose how your numeric data values appear in visuals so that they
					align with the regional language that you have chosen in Amazon QuickSight. For more
					information, see <a href="https://docs.aws.amazon.com//quicksight/latest/user/customizing-visual-language-preferences.html">Formatting visual numeric data based on language settings in
						Amazon QuickSight</a>.</description>
         <pubDate>Fri, 26 May 2023 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Format_visual_language_data_based_on_language_settings_in_Amazon_QuickSight_2023-05-26</guid>
      </item>
      <item>
         <title>Create geospatial heatmaps in Amazon QuickSight</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now create geospatial heatmaps in Amazon QuickSight. For more information,
					see <a href="https://docs.aws.amazon.com/quicksight/latest/user/heat-maps.html">Geospatial heatmaps in Amazon QuickSight</a>.</description>
         <pubDate>Fri, 26 May 2023 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Create_geospatial_heatmaps_in_Amazon_QuickSight_2023-05-26</guid>
      </item>
      <item>
         <title>Work with Q topics using the QuickSight CLI in Amazon QuickSight</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now work with QuickSight Q topics using the Amazon QuickSight
					command line interface (CLI). For more information, see <a href="https://docs.aws.amazon.com//quicksight/latest/user/quicksight-q-topics-cli.html">Work with QuickSight Q topics using the Amazon QuickSight
					CLI</a>.</description>
         <pubDate>Thu, 4 May 2023 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Work_with_Q_topics_using_the_QuickSight_CLI_in_Amazon_QuickSight_2023-05-04</guid>
      </item>
      <item>
         <title>Use dataset parameters in Amazon QuickSight</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now use dataset parameters in direct query to dynamically customize
					their datasets and apply reusable logic to your datasets. For more information,
					see <a href="https://docs.aws.amazon.com//quicksight/latest/user/dataset-parameters.html">Using dataset parameters in Amazon QuickSight</a>.</description>
         <pubDate>Thu, 4 May 2023 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Use_dataset_parameters_in_Amazon_QuickSight_2023-05-04</guid>
      </item>
      <item>
         <title>Enhanced options for scatter plots in Amazon QuickSight</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now plot unaggregated values on scatter plots in Amazon QuickSight. For
					more information, see <a href="https://docs.aws.amazon.com//quicksight/latest/user/scatter-plot.html">Using
						scatter plots</a>.</description>
         <pubDate>Thu, 4 May 2023 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Enhanced_options_for_scatter_plots_in_Amazon_QuickSight_2023-05-04</guid>
      </item>
      <item>
         <title>Create and update VPC connections Amazon QuickSight</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now create and update VPC connections in Amazon QuickSight. For more
					information, see <a href="https://docs.aws.amazon.com//quicksight/latest/user/working-with-aws-vpc.html">Using dataset parameters in Amazon QuickSight</a>.</description>
         <pubDate>Thu, 4 May 2023 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Create_and_update_VPC_connections_Amazon_QuickSight_2023-05-04</guid>
      </item>
      <item>
         <title>Create tag-based RLS rules using the OR condition in Amazon QuickSight</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now add the OR condition to your tag-based rules to further customize
					the way data is presented to your QuickSight account users. For more
					information, see <a href="https://docs.aws.amazon.com//quicksight/latest/user/quicksight-dev-rls-tags.html">Using row-level security (RLS) with tag-based rules to restrict access to a
						dataset when embedding dashboards for anonymous users</a>.</description>
         <pubDate>Fri, 7 Apr 2023 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Create_tag-based_RLS_rules_using_the_OR_condition_in_Amazon_QuickSight_2023-04-07</guid>
      </item>
      <item>
         <title>Threshold alerts on Table and Pivot table visuals in Amazon QuickSight</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now create threshold alerts for Table and Pivot table visuals in
					Amazon QuickSight. For more information, see <a href="https://docs.aws.amazon.com//quicksight/latest/user/threshold-alerts.html">Working
						with threshold alerts in Amazon QuickSight</a>.</description>
         <pubDate>Fri, 17 Mar 2023 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Threshold_alerts_on_Table_and_Pivot_table_visuals_in_Amazon_QuickSight_2023-03-17</guid>
      </item>
      <item>
         <title>Hide collapsed columns in Amazon QuickSight table visuals</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now customize the way Amazon QuickSight readers view pivot tables to make
					them easier to read and understand at a glance. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/format-tables-pivot-tables.html#format-tables-pivot-tables-layout-options">Pivot table layout options</a>.</description>
         <pubDate>Thu, 9 Mar 2023 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Hide_collapsed_columns_in_Amazon_QuickSight_table_visuals_2023-03-09</guid>
      </item>
      <item>
         <title>Enhanced embedding capabilities in Amazon QuickSight</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now use QuickSight's Embedding SDK (v2.0) to improve
					developer experience when embedding QuickSight in your application or
					website. For more information, see <a href="https://docs.aws.amazon.com//quicksight/latest/user/embedded-analytics-api.html">Embedding with the QuickSight APIs</a>.</description>
         <pubDate>Thu, 9 Mar 2023 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Enhanced_embedding_capabilities_in_Amazon_QuickSight_2023-03-09</guid>
      </item>
      <item>
         <title>Run queries with Amazon S3 data sources in Amazon QuickSight</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now enhance data security by using fine-grained access policies rather
					than broader permissions for data sources connected to Amazon S3 in Amazon QuickSight. For
					more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/datasource-run-as-role.html#datasource-run-as-role-s3">Run queries with Amazon S3 data sources</a>.</description>
         <pubDate>Tue, 21 Feb 2023 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Run_queries_with_Amazon_S3_data_sources_in_Amazon_QuickSight_2023-02-21</guid>
      </item>
      <item>
         <title>Radar charts in Amazon QuickSight</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now create radar charts in Amazon QuickSight. For more information, see
						<a href="https://docs.aws.amazon.com/quicksight/latest/user/radar-chart">Using radar
						charts in Amazon QuickSight</a>.</description>
         <pubDate>Mon, 30 Jan 2023 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Radar_charts_in_Amazon_QuickSight_2023-01-30</guid>
      </item>
      <item>
         <title>Data bars for tables and pivot tables in Amazon QuickSight</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now use data bars to add visual context to your table visuals in
					Amazon QuickSight. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/format-data-bars">Adding data
						bars to tables in Amazon QuickSight</a>.</description>
         <pubDate>Tue, 24 Jan 2023 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Data_bars_for_tables_and_pivot_tables_in_Amazon_QuickSight_2023-01-24</guid>
      </item>
      <item>
         <title>New question types: Boolean, Forecast, and Why</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now enter boolean, forecast, and why questions into the
					QuickSight Q search bar. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/quicksight-q-ask">Asking
						questions with Amazon QuickSight Q</a>.</description>
         <pubDate>Tue, 29 Nov 2022 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#New_question_types:_Boolean,_Forecast,_and_Why_2022-11-29</guid>
      </item>
      <item>
         <title>Automated data prep for QuickSight Q</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Amazon QuickSight Q now uses AI-enhanced data preparation to automatically create
					topics that are relevant to your end users. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/quicksight-q-topics">Working
						with Amazon QuickSight Q topics</a>.</description>
         <pubDate>Tue, 29 Nov 2022 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Automated_data_prep_for_QuickSight_Q_2022-11-29</guid>
      </item>
      <item>
         <title>Pixel perfect reporting</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now create, schedule, and share highly formatted multi-page reports in
					Amazon QuickSight. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/working-with-reports">Working
						with pixel perfect reports in Amazon QuickSight</a>.</description>
         <pubDate>Mon, 28 Nov 2022 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Pixel_perfect_reporting_2022-11-28</guid>
      </item>
      <item>
         <title>Embedding the Q search bar for anonymous (unregistered) users</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now embed the QuickSight Q search bar for anonymous
					(unregistered) users. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/embedded-analytics-q-search-bar-for-anonymous-users">Embedding the Amazon QuickSight Q search bar for anonymous (unregistered)
						users</a>.</description>
         <pubDate>Sat, 19 Nov 2022 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Embedding_the_Q_search_bar_for_anonymous_(unregistered)_users_2022-11-19</guid>
      </item>
      <item>
         <title>Asset management</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now manage all of the assets un your Amazon QuickSight account in one
					unified view. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/manage-qs-assets">Amazon QuickSight
						asset management</a>.</description>
         <pubDate>Sat, 19 Nov 2022 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Asset_management_2022-11-19</guid>
      </item>
      <item>
         <title>Text boxes</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now add static and dynamic textual content using text boxes in
					Amazon QuickSight. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/textbox">Using text
						boxes</a>.</description>
         <pubDate>Fri, 18 Nov 2022 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Text_boxes_2022-11-18</guid>
      </item>
      <item>
         <title>Small multiples</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now create small multiples in line, bar, and pie chart visuals. For
					more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/small-multiples">Using small
						multiples</a>.</description>
         <pubDate>Fri, 18 Nov 2022 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Small_multiples_2022-11-18</guid>
      </item>
      <item>
         <title>Set a reserved value in QuickSight datasets</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now set a reserved value to determine the value of the
						<b>Select all</b> value of a dataset in Amazon QuickSight. For more
					information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/parameters-set-up">Setting up
						parameters in Amazon QuickSight</a>.</description>
         <pubDate>Fri, 18 Nov 2022 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Set_a_reserved_value_in_QuickSight_datasets_2022-11-18</guid>
      </item>
      <item>
         <title>Run queries as an IAM role in Amazon QuickSight</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now enhance data security by using fine-grained access policies rather
					than broader permissions for data sources connected to Athena. For more
					information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/datasource-run-as-role">Run
						queries as an IAM role in Amazon QuickSight</a>.</description>
         <pubDate>Fri, 18 Nov 2022 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Run_queries_as_an_IAM_role_in_Amazon_QuickSight_2022-11-18</guid>
      </item>
      <item>
         <title>Pin Amazon QuickSight Q answers to your pinboard</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now pin visuals from Q for easy access to frequently asked questions.
					For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/quicksight-q-pin-board">Pinning
						visuals in Amazon QuickSight Q</a>.</description>
         <pubDate>Fri, 18 Nov 2022 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Pin_Amazon_QuickSight_Q_answers_to_your_pinboard_2022-11-18</guid>
      </item>
      <item>
         <title>Marker clustering on geospatial map visuals</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now use marker clustering to improve readability of co-located points
					on a map. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/marker-clustering-on-maps">Marker clustering on geospatial point maps in
					QuickSight</a>.</description>
         <pubDate>Fri, 18 Nov 2022 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Marker_clustering_on_geospatial_map_visuals_2022-11-18</guid>
      </item>
      <item>
         <title>Line chart customization</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now add customizations to line chart visuals to emphasize what you
					want readers to focus on: color, line style, and markers. For more information,
					see <a href="https://docs.aws.amazon.com/quicksight/latest/user/line-and-marker-styling">Line and marker styling on line charts in QuickSight</a>.</description>
         <pubDate>Fri, 18 Nov 2022 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Line_chart_customization_2022-11-18</guid>
      </item>
      <item>
         <title>Connecting Amazon QuickSight accounts to Databricks</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now use Amazon QuickSight to connect to Databricks on AWS.
					For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/quicksight-databricks">Using
						Databricks in QuickSight</a>.</description>
         <pubDate>Fri, 18 Nov 2022 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Connecting_Amazon_QuickSight_accounts_to_Databricks_2022-11-18</guid>
      </item>
      <item>
         <title>Account termination protection</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now use account termination protection to prevent someone from
					deleting a QuickSight user account accidentally or maliciously. For more
					information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/closing-account">Deleting your
						Amazon QuickSight subscription and closing your account</a>.</description>
         <pubDate>Fri, 18 Nov 2022 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Account_termination_protection_2022-11-18</guid>
      </item>
      <item>
         <title>1 billion row SPICE datasets</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Amazon QuickSight now supports SPICE datasets that contain up to 1 billion
					(1,000,000,000) rows or 1 terabyte (TB) of data. For more information, see
						<a href="https://docs.aws.amazon.com/quicksight/latest/user/data-source-limits">SPICE
						quotas for imported data</a>.</description>
         <pubDate>Fri, 18 Nov 2022 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#1_billion_row_SPICE_datasets_2022-11-18</guid>
      </item>
      <item>
         <title>Monitor SPICE consumption metrics in Amazon CloudWatch</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now monitor your QuickSight account's SPICE consumption
					metrics in Amazon CloudWatch. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/aggregate-spice-metrics">Aggregate SPICE metrics</a>.</description>
         <pubDate>Tue, 8 Nov 2022 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Monitor_SPICE_consumption_metrics_in_Amazon_CloudWatch_2022-11-08</guid>
      </item>
      <item>
         <title>Use AWS KMS to encrypt your SPICE datasets in Amazon QuickSight</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description> You can now encrypt your SPICE datasets using the keys that you have stored
					in AWS KMS. This provides you with the tools to audit access to data and satisfy
					regulatory security requirements. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/key-management">Key
						management</a>.</description>
         <pubDate>Thu, 27 Oct 2022 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Use_AWS_KMS_to_encrypt_your_SPICE_datasets_in_Amazon_QuickSight_2022-10-27</guid>
      </item>
      <item>
         <title>Add datasets that contain row-level security (RLS) to Q topics</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>QuickSight Q now supports questions for access restricted datasets that
					use Row level Security (RLS) with user based rules. Readers can now ask
					questions about Topics that contain restricted access datasets and instantly
					receive accurate and pertinent answers based on access control rules defined by
					authors in RLS settings. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/quicksight-q-topics-data.html#quicksight-q-topics-data-rls">Adding datasets with row-level security (RLS) to a topic</a>.</description>
         <pubDate>Mon, 10 Oct 2022 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Add_datasets_that_contain_row-level_security_(RLS)_to_Q_topics_2022-10-10</guid>
      </item>
      <item>
         <title>Use AWS Secrets Manager secrets instead of database credentials in Amazon QuickSight</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Amazon QuickSight administrators can grant QuickSight read-only access to
					secrets they create in AWS Secrets Manager. These secrets can be used in place of database
					credentials when creating and editing data sources using the QuickSight
					API. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/secrets-manager-integration">Using AWS Secrets Manager secrets instead of database credentials in
						Amazon QuickSight</a>.</description>
         <pubDate>Thu, 6 Oct 2022 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Use_AWS_Secrets_Manager_secrets_instead_of_database_credentials_in_Amazon_QuickSight_2022-10-06</guid>
      </item>
      <item>
         <title>Visual Embedding</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now embed visuals using a 1-click embed code or with the Amazon QuickSight
					API. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/embedding-visuals">Embedding
						visuals with the Amazon QuickSight API</a>.</description>
         <pubDate>Thu, 25 Aug 2022 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Visual_Embedding_2022-08-25</guid>
      </item>
      <item>
         <title>Undo and redo changes in Q answers</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now undo or redo any changes you make to a Q answer by choosing the
					undo or redo arrows in the Q search bar. For more information, see step six in
						<a href="https://docs.aws.amazon.com/quicksight/latest/user/quicksight-q-ask">Asking
						questions with Q</a>.</description>
         <pubDate>Mon, 22 Aug 2022 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Undo_and_redo_changes_in_Q_answers_2022-08-22</guid>
      </item>
      <item>
         <title>Updates to the sign in experience</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>The sign in experience in QuickSight has been updated. For more
					information about how to sign in, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/signing-in">Signing in to
						QuickSight</a>.</description>
         <pubDate>Thu, 21 Jul 2022 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Updates_to_the_sign_in_experience_2022-07-21</guid>
      </item>
      <item>
         <title>Bookmarks</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now bookmark views of a dashboard. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/dashboard-bookmarks">Bookmarking
						views of a dashboard</a>.</description>
         <pubDate>Thu, 21 Jul 2022 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Bookmarks_2022-07-21</guid>
      </item>
      <item>
         <title>Base Maps</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>When creating map visuals in QuickSight, you can now change map base.
					For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/base-maps">Changing base
						maps</a>.</description>
         <pubDate>Thu, 21 Jul 2022 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Base_Maps_2022-07-21</guid>
      </item>
      <item>
         <title>Q updates</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now try QuickSight Q out for free before getting the Q add-on.
					For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/quicksight-q-try">Trying
						QuickSight Q</a>.</description>
         <pubDate>Thu, 7 Jul 2022 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Q_updates_2022-07-07</guid>
      </item>
      <item>
         <title>Rolling dates in filters and parameters</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now set a rolling date on date range fiters and relative date
					parameters in analyses. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/add-a-date-filter2.html#create-date-filter-analyses">Creating range date filters in analyses</a> and <a href="https://docs.aws.amazon.com/quicksight/latest/user/parameters-set-up">Setting up
						parameters</a>.</description>
         <pubDate>Tue, 5 Jul 2022 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Rolling_dates_in_filters_and_parameters_2022-07-05</guid>
      </item>
      <item>
         <title>Calculations update</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now create level-aware calculations in QuickSight. You can
					specify at what level to group computations using level-aware calculation -
					aggregation (LAC-A) functions. You can also specify the window or partition to
					compute a calculation using level-aware calculation - window (LAC-W) functions
					(previously known as level-aware aggregations). For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/level-aware-calculations">Using
						level-aware calculations</a>.</description>
         <pubDate>Tue, 5 Jul 2022 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Calculations_update_2022-07-05</guid>
      </item>
      <item>
         <title>Allowed domains</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Developers can now add a domain at run-time to an allow list with the
						<code class="code">AllowedDomains</code> parameter of a
						<code class="code">GenerateEmbedUrlForAnonymousUser</code> or a
						<code class="code">GenerateEmbedUrlForRegisteredUser</code> API call. For more
					information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/embedding-run-time.html">Allow
						listing domains at run-time with the QuickSight API</a>.</description>
         <pubDate>Tue, 5 Jul 2022 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Allowed_domains_2022-07-05</guid>
      </item>
      <item>
         <title>Account provisioning</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now sign up for an Amazon QuickSight account with the Amazon QuickSight API. For
					more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CreateAccountSubscription.html">CreateAccountSubscription</a>.</description>
         <pubDate>Tue, 5 Jul 2022 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Account_provisioning_2022-07-05</guid>
      </item>
      <item>
         <title>Monitoring data with Amazon CloudWatch</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now monitor metrics for Amazon QuickSight dashboards, visuals, and dataset
					ingestions on Amazon CloudWatch to provide your readers with a consistent,
					high-performing, and uninterrupted experience on QuickSight. For more
					information, see <a href="https://docs.aws.amazon.com//quicksight/latest/user/monitoring-quicksight.html">Monitoring data in Amazon QuickSight</a>.</description>
         <pubDate>Wed, 22 Jun 2022 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Monitoring_data_with_Amazon_CloudWatch_2022-06-22</guid>
      </item>
      <item>
         <title>Forecast boundaries</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Authors can now set a minimum and maximum for forecasted values. For more
					information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/forecasts-and-whatifs.html">Forecasting and creating what-if scenarios </a>.</description>
         <pubDate>Thu, 16 Jun 2022 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Forecast_boundaries_2022-06-16</guid>
      </item>
      <item>
         <title>Table and pivot table enhancements</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Authors and Readers can now resize rows and columns in a table or pivot table
					visual. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/format-tables-pivot-tables.html#format-tables-pivot-tables-resize-rows-columns">Resizing rows and columns in tables and pivot tables</a>.</description>
         <pubDate>Tue, 14 Jun 2022 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Table_and_pivot_table_enhancements_2022-06-14</guid>
      </item>
      <item>
         <title>Hiding fields in pivot tables</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now hide fields in pivot table visuals. For more information, see
						<a href="https://docs.aws.amazon.com/quicksight/latest/user/hiding-pivot-table-columns.html">Showing and hiding pivot table columns</a>.</description>
         <pubDate>Tue, 14 Jun 2022 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Hiding_fields_in_pivot_tables_2022-06-14</guid>
      </item>
      <item>
         <title>ML insights and forecasting for Q</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Readers can now see key data insights and add forecasts to Q answers. For more
					information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/quicksight-q-ask.html">Asking
						questions with QuickSight Q</a>.</description>
         <pubDate>Thu, 2 Jun 2022 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#ML_insights_and_forecasting_for_Q_2022-06-02</guid>
      </item>
      <item>
         <title>What's New in QuickSight</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>To find out what's new in QuickSight, see the <a href="https://aws.amazon.com/about-aws/whats-new/analytics/?whats-new-content.sort-by=item.additionalFields.postDateTime&whats-new-content.sort-order=desc&awsf.whats-new-products=general-products%23amazon-quicksight" rel="noopener noreferrer" target="_blank">What's New</a> page. What's New posts provide a brief overview of all
					QuickSight feature announcements as they are released.</description>
         <pubDate>Wed, 1 Jun 2022 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#What's_New_in_QuickSight_2022-06-01</guid>
      </item>
      <item>
         <title>Line chart updates</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>QuickSight now supports 10,000 data points for line charts. For more
					information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/line-charts.html">Using line
						charts</a>.</description>
         <pubDate>Sun, 22 May 2022 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Line_chart_updates_2022-05-22</guid>
      </item>
      <item>
         <title>1-click public embedding</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now embed dashboards for anyone on the internet in your public
					applications with a 1-click static embed code. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/embedded-analytics-1-click-public.html">Enabling public access to dashboards with a 1-click embed
					code</a>.</description>
         <pubDate>Wed, 18 May 2022 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#1-click_public_embedding_2022-05-18</guid>
      </item>
      <item>
         <title>Creating and managing groups</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now create and manage groups in the QuickSight console. For
					more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/creating-quicksight-groups.html">Creating and managing groups in Amazon QuickSight</a>.</description>
         <pubDate>Mon, 21 Mar 2022 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Creating_and_managing_groups_2022-03-21</guid>
      </item>
      <item>
         <title>Automatic refresh controls for direct query</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>In QuickSight, filter controls are now refreshed every 24 hours for
					direct query. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/refreshing-data.html">Refreshing
						data</a>.</description>
         <pubDate>Tue, 8 Mar 2022 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Automatic_refresh_controls_for_direct_query_2022-03-08</guid>
      </item>
      <item>
         <title>Updating files in a dataset</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now update files in a dataset to get the latest version of those
					files. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/updating-file-dataset.html?icmpid=docs_quicksight_console_rssdochistory">Updating files in a dataset</a>.</description>
         <pubDate>Thu, 27 Jan 2022 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Updating_files_in_a_dataset_2022-01-27</guid>
      </item>
      <item>
         <title>Rich text formatting for titles and subtitles</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>QuickSight now offers rich text formatting for titles and subtitles,
					and the ability to add hyperlinks and parameters in titles. For more
					information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/customizing-a-visual-title.html?icmpid=docs_quicksight_console_rssdochistory">Formatting a visual title and subtitle</a>.</description>
         <pubDate>Thu, 27 Jan 2022 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Rich_text_formatting_for_titles_and_subtitles_2022-01-27</guid>
      </item>
      <item>
         <title>Comparative and cumulative date/time calculations</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Comparative and cumulative period functions, such as year-over-year and
					year-to-date, are now supported in QuickSight. For more information, see
						<a href="https://aws.amazon.com//blogs/big-data/add-comparative-and-cumulative-date-time-calculations-in-amazon-quicksight/" rel="noopener noreferrer" target="_blank">Add comparative and cumulative date/time calculations in
						QuickSight</a>.</description>
         <pubDate>Thu, 27 Jan 2022 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Comparative_and_cumulative_date/time_calculations_2022-01-27</guid>
      </item>
      <item>
         <title>Sharing dashboards</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You now have the option to grant everyone in your QuickSight account
					access to a dashboard. You can also share a link to the dashboard with anyone
					who has access to it. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/sharing-a-dashboard.html?icmpid=docs_quicksight_console_rssdochistory">Sharing dashboards</a>.</description>
         <pubDate>Tue, 23 Nov 2021 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Sharing_dashboards_2021-11-23</guid>
      </item>
      <item>
         <title>Customizing email report templates</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now customize how dashboard email reports appear and behave for
					QuickSight account users. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/customizing-quicksight-email-templates.html?icmpid=docs_quicksight_console_rssdochistory">Customizing email report templates</a>.</description>
         <pubDate>Tue, 23 Nov 2021 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Customizing_email_report_templates_2021-11-23</guid>
      </item>
      <item>
         <title>1-click enterprise embedding</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now embed dashboards for registered users in your internal
					applications with a 1-click static embed code. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/embedded-analytics-1-click.html?icmpid=docs_quicksight_console_rssdochistory">Embedding dashboards for registered users with a 1-Click embed
					code</a>.</description>
         <pubDate>Tue, 23 Nov 2021 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#1-click_enterprise_embedding_2021-11-23</guid>
      </item>
      <item>
         <title>New data source</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>QuickSight now supports connecting to an Exasol data source. For more
					information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/supported-data-sources.html?icmpid=docs_quicksight_console_rssdochistory">Supported data sources</a>.</description>
         <pubDate>Mon, 22 Nov 2021 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#New_data_source_2021-11-22</guid>
      </item>
      <item>
         <title>Dataset versioning</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>QuickSight now supports dataset versioning. For more information, see
						<a href="https://docs.aws.amazon.com/quicksight/latest/user/dataset-versioning.html?icmpid=docs_quicksight_console_rssdochistory">Reverting datasets back to previous published versions</a>.</description>
         <pubDate>Mon, 22 Nov 2021 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Dataset_versioning_2021-11-22</guid>
      </item>
      <item>
         <title>Adding datasets with RLS to Q topics</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>QuickSight Q topics now support datasets with row-level security (RLS).
					For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/quicksight-q-topics-data.html#quicksight-q-topics-data-rls?icmpid=docs_quicksight_console_rssdochistory">Adding datasets with RLS to a Q topic</a>.</description>
         <pubDate>Fri, 19 Nov 2021 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Adding_datasets_with_RLS_to_Q_topics_2021-11-19</guid>
      </item>
      <item>
         <title>Sheet change performance operations</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>QuickSight now only refreshes visuals when switching sheets if
					required. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/refreshing-visuals.html">Refreshing visuals</a>.</description>
         <pubDate>Fri, 12 Nov 2021 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Sheet_change_performance_operations_2021-11-12</guid>
      </item>
      <item>
         <title>Incrementally refresh a SQL-based dataset</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>In QuickSight Enterprise Edition, you can now refresh your SQL-based
						SPICE datasets incrementally within a look-back window of
					time. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/refreshing-imported-data.html?icmpid=docs_quicksight_console_rssdochistory">Refreshing data</a>.</description>
         <pubDate>Mon, 25 Oct 2021 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Incrementally_refresh_a_SQL-based_dataset_2021-10-25</guid>
      </item>
      <item>
         <title>Embedding the Q search bar</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now embed the Q search bar in your application for registered users of
					QuickSight. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/embedded-analytics-q-search-bar-for-authenticated-users.html?icmpid=docs_quicksight_console_rssdochistory">Embedding the QuickSight Q search bar for registered
					users</a>.</description>
         <pubDate>Fri, 22 Oct 2021 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Embedding_the_Q_search_bar_2021-10-22</guid>
      </item>
      <item>
         <title>Email syncing for federated users</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>In Enterprise Edition, QuickSight administrators can now restrict new
					users from using personal email addresses when provisioning through their
					identity provider (IdP) to QuickSight. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/jit-email-syncing.html?icmpid=docs_quicksight_console_rssdochistory">Configuring email syncing for federated users</a>.</description>
         <pubDate>Fri, 22 Oct 2021 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Email_syncing_for_federated_users_2021-10-22</guid>
      </item>
      <item>
         <title>Adding RLS tags to a dataset</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now add tag-based rules to a dataset in QuickSight when
					applying row-level security (RLS). For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/quicksight-dev-rls-tags.html?icmpid=docs_quicksight_console_rssdochistory">Using row-level security (RLS) with tag-based rules to restrict access to a
						dataset when embedding dashboards for anonymous users</a>.</description>
         <pubDate>Tue, 19 Oct 2021 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Adding_RLS_tags_to_a_dataset_2021-10-19</guid>
      </item>
      <item>
         <title>IP restrictions</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now limit access to your organization's QuickSight account to a
					predefined list of Internet Protocol (IP) ranges. For more information, see
						<a href="https://docs.aws.amazon.com/quicksight/latest/user/enabling-ip-restrictions.html">Turning on Internet Protocol (IP) restrictions in
					Amazon QuickSight</a>.</description>
         <pubDate>Mon, 18 Oct 2021 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#IP_restrictions_2021-10-18</guid>
      </item>
      <item>
         <title>New table and pivot table styling options</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now customize the look of tables and pivots tables. For more
					information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/format-tables-pivot-tables.html?icmpid=docs_quicksight_console_rssdochistory">Formatting tables and pivot tables</a>.</description>
         <pubDate>Tue, 12 Oct 2021 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#New_table_and_pivot_table_styling_options_2021-10-12</guid>
      </item>
      <item>
         <title>New SPICE quota for imported data</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>In QuickSight Enterprise edition, you can now import up to 500 million
					rows into a SPICE dataset. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/data-source-limits.html?icmpid=docs_quicksight_console_rssdochistory">Data source quotas</a>.</description>
         <pubDate>Tue, 12 Oct 2021 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#New_SPICE_quota_for_imported_data_2021-10-12</guid>
      </item>
      <item>
         <title>Links and images in tables</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now add links to tables. You can also render links as images in
					tables. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/field-styling.html?icmpid=docs_quicksight_console_rssdochistory">Field styling</a>.</description>
         <pubDate>Tue, 12 Oct 2021 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Links_and_images_in_tables_2021-10-12</guid>
      </item>
      <item>
         <title>Custom date formats</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now customize how dates are formatted in your filter and parameter
					controls. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/format-visual-date-controls.html?icmpid=docs_quicksight_console_rssdochistory">Customizing date formats</a>.</description>
         <pubDate>Fri, 8 Oct 2021 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Custom_date_formats_2021-10-08</guid>
      </item>
      <item>
         <title>QuickSight q</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now ask questions about your data in the Q bar and get answers in the
					form of visuals. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/working-with-quicksight-q.html?icmpid=docs_quicksight_console_rssdochistory">Working with QuickSight q</a>.</description>
         <pubDate>Fri, 24 Sep 2021 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#QuickSight_q_2021-09-24</guid>
      </item>
      <item>
         <title>New geospatial region</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>QuickSight now supports creating geospatial charts for India. For more
					information about creating geospatial charts, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/geospatial-charts.html?icmpid=docs_quicksight_console_rssdochistory">Using geospatial charts (maps)</a>.</description>
         <pubDate>Wed, 22 Sep 2021 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#New_geospatial_region_2021-09-22</guid>
      </item>
      <item>
         <title>Free-form layouts</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now place visuals anywhere in your dashboard using precise
					coordinates. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/customizing-dashboards-and-visuals.html?icmpid=docs_quicksight_console_rssdochistory">Customizing dashboards and visuals</a>.</description>
         <pubDate>Wed, 22 Sep 2021 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Free-form_layouts_2021-09-22</guid>
      </item>
      <item>
         <title>Passing IAM roles to QuickSight</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now pass IAM roles to QuickSight. For more information, see
						<a href="https://docs.aws.amazon.com/quicksight/latest/user/security_iam_service-with-iam.html?icmpid=docs_quicksight_console_rssdochistory">Using QuickSight with IAM</a>.</description>
         <pubDate>Wed, 15 Sep 2021 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Passing_IAM_roles_to_QuickSight_2021-09-15</guid>
      </item>
      <item>
         <title>Create datasets from existing datasets</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now create datasets from existing datasets. For more information, see
						<a href="https://docs.aws.amazon.com/quicksight/latest/user/create-a-dataset-existing-dataset.html?icmpid=docs_quicksight_console_rssdochistory">Creating a dataset using an existing dataset</a>.</description>
         <pubDate>Wed, 15 Sep 2021 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Create_datasets_from_existing_datasets_2021-09-15</guid>
      </item>
      <item>
         <title>Updated AWS managed policy</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>QuickSight updated an existing AWS managed policy. For more
					information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/security-iam-quicksight?icmpid=docs_quicksight_console_rssdochistory">Amazon QuickSight updates to AWS managed policies</a>.</description>
         <pubDate>Wed, 8 Sep 2021 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Updated_AWS_managed_policy_2021-09-08</guid>
      </item>
      <item>
         <title>New AWS managed policy</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>QuickSight added a new AWS managed policy. For more information, see
						<a href="https://docs.aws.amazon.com/quicksight/latest/user/security-iam-quicksight?icmpid=docs_quicksight_console_rssdochistory">Amazon QuickSight updates to AWS managed policies</a>.</description>
         <pubDate>Wed, 8 Sep 2021 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#New_AWS_managed_policy_2021-09-08</guid>
      </item>
      <item>
         <title>Forecast multiple measures</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now forecast up to three measures in the same chart. For more
					information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/forecasts-and-whatifs.html?icmpid=docs_quicksight_console_rssdochistory">Forecasting and creating what-if scenarios</a>.</description>
         <pubDate>Mon, 30 Aug 2021 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Forecast_multiple_measures_2021-08-30</guid>
      </item>
      <item>
         <title>Share your view of a dashboard</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now share your view of a dashboard. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/sharing-a-dashboard.html?icmpid=docs_quicksight_console_rssdochistory">Sharing dashboards</a>.</description>
         <pubDate>Fri, 20 Aug 2021 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Share_your_view_of_a_dashboard_2021-08-20</guid>
      </item>
      <item>
         <title>Hide the data zoom on a chart</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now choose to show or hide the data zoom for your charts in
					Amazon QuickSight. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/showing-hiding-axis-grid-tick.html?icmpid=docs_quicksight_console_rssdochistory">Formatting axes and Grid lines</a>.</description>
         <pubDate>Mon, 16 Aug 2021 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Hide_the_data_zoom_on_a_chart_2021-08-16</guid>
      </item>
      <item>
         <title>Row-level security with tags</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now use row-level security (RLS) with tags to specify which data your
					(unauthenticated) users can see in an embedded Amazon QuickSight dashboard depending
					on who they are. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/quicksight-dev-rls-tags.html?icmpid=docs_quicksight_console_rssdochistory">Using RLS with tags to restrict access to a dataset when embedding
						dashboards for anonymous users</a>.</description>
         <pubDate>Thu, 29 Jul 2021 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Row-level_security_with_tags_2021-07-29</guid>
      </item>
      <item>
         <title>New embedding API operations</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Amazon QuickSight has the following new API operations for embedding analytics:
						<code class="code">GenerateEmbedUrlForAnonymousUser</code> and
						<code class="code">GenerateEmbedUrlForRegisteredUser</code>. You can still use the
						<code class="code">GetDashboardEmbedUrl</code> and <code class="code">GetSessionEmbedUrl</code> API
					operations to embed dashboards and the QuickSight console, but they
					don't contain the latest embedding capabilities. For more information about
					using the new API operations, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/embedding-overview.html?icmpid=docs_quicksight_console_rssdochistory">Embedding overview</a>. For more information on using the old API
					operations, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/embedded-analytics-deprecated.html?icmpid=docs_quicksight_console_rssdochistory">Embedding analytics using the old API operations</a>.</description>
         <pubDate>Thu, 29 Jul 2021 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#New_embedding_API_operations_2021-07-29</guid>
      </item>
      <item>
         <title>Customizing charts</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now hide the sort icon and the axis or field title in charts in
					Amazon QuickSight. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/showing-hiding-axis-grid-tick.html?icmpid=docs_quicksight_console_rssdochistory">Formatting axes and Grid lines</a>.</description>
         <pubDate>Fri, 16 Jul 2021 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Customizing_charts_2021-07-16</guid>
      </item>
      <item>
         <title>Threshold alert updates</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now choose to be notified when there is no data to check your alert
					rule against in Amazon QuickSight. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/threshold-alerts.html?icmpid=docs_quicksight_console_rssdochistory">Working with threshold alerts</a>.</description>
         <pubDate>Fri, 9 Jul 2021 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Threshold_alert_updates_2021-07-09</guid>
      </item>
      <item>
         <title>New chart type: Custom visual content</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now embed webpages and online videos, forms, and images in your
					QuickSight dashboards using the custom visual content chart type. For
					more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/custom-visual-content.html?icmpid=docs_quicksight_console_rssdochistory">Using custom visual content in QuickSight</a>.</description>
         <pubDate>Tue, 29 Jun 2021 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#New_chart_type:_Custom_visual_content_2021-06-29</guid>
      </item>
      <item>
         <title>Feature improvements</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now show totals for stacked bar charts. For more information, see
						<a href="https://docs.aws.amazon.com/quicksight/latest/user/bar-charts.html?icmpid=docs_quicksight_console_rssdochistory">Using bar charts</a>.</description>
         <pubDate>Tue, 29 Jun 2021 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Feature_improvements_2021-06-29</guid>
      </item>
      <item>
         <title>Threshold alert updates</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Dataset owners can now set a threshold alert evaluation schedule for a dataset
					in Amazon QuickSight. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/threshold-alerts.html?icmpid=docs_quicksight_console_rssdochistory">Working with threshold alerts</a>.</description>
         <pubDate>Thu, 17 Jun 2021 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Threshold_alert_updates_2021-06-17</guid>
      </item>
      <item>
         <title>Duplicating analyses</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now duplicate an analysis in Amazon QuickSight. For more information, see
						<a href="https://docs.aws.amazon.com/quicksight/latest/user/duplicating-an-analysis.html?icmpid=docs_quicksight_console_rssdochistory">Duplicating an analysis</a>.</description>
         <pubDate>Thu, 17 Jun 2021 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Duplicating_analyses_2021-06-17</guid>
      </item>
      <item>
         <title>Threshold alert updates</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now choose how often you want to receive threshold alerts in
					Amazon QuickSight. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/threshold-alerts.html?icmpid=docs_quicksight_console_rssdochistory">Working with threshold alerts</a>.</description>
         <pubDate>Tue, 25 May 2021 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Threshold_alert_updates_2021-05-25</guid>
      </item>
      <item>
         <title>Wildcard search</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Amazon QuickSight now supports wildcard search. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/search-filter.html#search-filter-wildcard?icmpid=docs_quicksight_console_rssdochistory">Using wildcard search</a>.</description>
         <pubDate>Sat, 1 May 2021 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Wildcard_search_2021-05-01</guid>
      </item>
      <item>
         <title>Threshold alerts</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Amazon QuickSight now supports creating threshold alerts using KPI and Gauge
					visuals in dashboards. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/threshold-alerts.html?icmpid=docs_quicksight_console_rssdochistory">Working with threshold alerts</a>.</description>
         <pubDate>Sat, 1 May 2021 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Threshold_alerts_2021-05-01</guid>
      </item>
      <item>
         <title>Service control policies</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Amazon QuickSight now supports using service control policies (SCPs) to restrict
					how individuals in your organization can sign up for QuickSight. For more
					information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/security-scp.html?icmpid=docs_quicksight_console_rssdochistory">Using service control policies to restrict QuickSight signup
						options</a>.</description>
         <pubDate>Mon, 26 Apr 2021 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Service_control_policies_2021-04-26</guid>
      </item>
      <item>
         <title>Parameter improvements</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Amazon QuickSight now supports dynamically displaying parameter values in titles
					and descriptions throughout charts and analyses. For more information, see
						<a href="https://docs.aws.amazon.com/quicksight/latest/user/parameters-in-titles.html?icmpid=docs_quicksight_console_rssdochistory">Using parameters in titles and descriptions</a>.</description>
         <pubDate>Mon, 12 Apr 2021 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Parameter_improvements_2021-04-12</guid>
      </item>
      <item>
         <title>Feature improvements</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>QuickSight now supports selecting a time granularity for date and time
					range filters and datetime parameters. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/add-a-date-filter2.html?icmpid=docs_quicksight_console_rssdochistory">Adding a date filter</a> and <a href="https://docs.aws.amazon.com/quicksight/latest/user/parameters-set-up.html?icmpid=docs_quicksight_console_rssdochistory">Setting up parameters</a>.</description>
         <pubDate>Thu, 1 Apr 2021 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Feature_improvements_2021-04-01</guid>
      </item>
      <item>
         <title>Export to PDF</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>QuickSight now supports PDF exports of the current sheet in dashboards
					and analyses. In Enterprise edition, you can now attach a PDF to email reports.
					For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/export-dashboard-to-pdf.html?icmpid=docs_quicksight_console_rssdochistory">Exporting an analysis or dashboard as a PDF</a>.</description>
         <pubDate>Thu, 1 Apr 2021 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Export_to_PDF_2021-04-01</guid>
      </item>
      <item>
         <title>Seconds support for date fields</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>QuickSight now supports aggregating date fields at the second level.
					For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/changing-date-field-granularity.html?icmpid=docs_quicksight_console_rssdochistory">Changing date field granularity</a>.</description>
         <pubDate>Tue, 30 Mar 2021 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Seconds_support_for_date_fields_2021-03-30</guid>
      </item>
      <item>
         <title>Pivot table sorting improvements</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>QuickSight now supports sorting values in pivots tables by fields in
					the <b>Rows</b> and <b>Columns</b> field wells or by
					column headers. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/sorting-pivot-tables.html?icmpid=docs_quicksight_console_rssdochistory">Sorting pivot tables</a>.</description>
         <pubDate>Tue, 30 Mar 2021 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Pivot_table_sorting_improvements_2021-03-30</guid>
      </item>
      <item>
         <title>New feature</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Amazon QuickSight now supports customizing tooltips in visuals. For more
					information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/customizing-visual-tooltips.html?icmpid=docs_quicksight_console_rssdochistory">Customizing tooltips in a visual</a>.</description>
         <pubDate>Tue, 16 Mar 2021 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#New_feature_2021-03-16</guid>
      </item>
      <item>
         <title>Feature improvements</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>In Enterprise edition, QuickSight now supports computing anomalies for
					a time and measure field only, and computing the exact combination of fields in
					the Category field well. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/anomaly-detection-adding-anomaly-insights.html?icmpid=docs_quicksight_console_rssdochistory">Adding an ML insight to detect outliers and key drivers</a>.</description>
         <pubDate>Tue, 16 Mar 2021 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Feature_improvements_2021-03-16</guid>
      </item>
      <item>
         <title>Line chart improvements</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Amazon QuickSight now supports creating line charts with dual axes. For more
					information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/line-charts.html#dual-axis-chart?icmpid=docs_quicksight_console_rssdochistory">Creating a dual-axis line chart</a>. </description>
         <pubDate>Mon, 1 Mar 2021 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Line_chart_improvements_2021-03-01</guid>
      </item>
      <item>
         <title>New formatting options for charts</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Amazon QuickSight now supports hiding axis lines, axis labels, and grid lines, and
					also customizing the how axis labels appear in a chart. For more information,
					see <a href="https://docs.aws.amazon.com/quicksight/latest/user/showing-hiding-axis-grid-tick.html?icmpid=docs_quicksight_console_rssdochistory">Formatting axis lines, axis labels, and Grid lines</a>.</description>
         <pubDate>Fri, 5 Feb 2021 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#New_formatting_options_for_charts_2021-02-05</guid>
      </item>
      <item>
         <title>New chart type: Sankey diagrams</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Amazon QuickSight now supports creating Sankey diagrams. For more information, see
						<a href="https://docs.aws.amazon.com/quicksight/latest/user/sankey-diagram.html?icmpid=docs_quicksight_console_rssdochistory">Using sankey diagrams</a>.</description>
         <pubDate>Fri, 5 Feb 2021 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#New_chart_type:_Sankey_diagrams_2021-02-05</guid>
      </item>
      <item>
         <title>Field mapping improvements</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Amazon QuickSight now supports updating field mapping between mismatched and
					missing fields when replacing a dataset in an analysis. For more information,
					see <a href="https://docs.aws.amazon.com/quicksight/latest/user/replacing-data-sets.html?icmpid=docs_quicksight_console_rssdochistory">Replacing datasets</a>.</description>
         <pubDate>Fri, 5 Feb 2021 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Field_mapping_improvements_2021-02-05</guid>
      </item>
      <item>
         <title>Data prep enhancements</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Amazon QuickSight now supports organizing fields into folders and subfolders when
					preparing or editing datasets. For more information see, <a href="https://docs.aws.amazon.com/quicksight/latest/user/organizing-fields-folder.html?icmpid=docs_quicksight_console_rssdochistory">Organizing fields into folders</a>.</description>
         <pubDate>Fri, 5 Feb 2021 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Data_prep_enhancements_2021-02-05</guid>
      </item>
      <item>
         <title>New features</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>In Enterprise edition, QuickSight now supports displaying anomaly
					ranges and multiple anomalies when exploring anomalies. Line charts now display
					notifications when QuickSight detects an anomaly, key driver, or
					forecasting opportunity. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/anomaly-detection.html?icmpid=docs_quicksight_console_rssdochistory">Detecting outliers with ML-powered anomaly detection</a>.</description>
         <pubDate>Wed, 3 Feb 2021 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#New_features_2021-02-03</guid>
      </item>
      <item>
         <title>New region: South America (SÃ£o Paulo)</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Amazon QuickSight is now available in South America (SÃ£o Paulo) (sa-east-1). For more
					information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/regions.html?icmpid=docs_quicksight_console_rssdochistory">AWS Regions, websites, IP address ranges, and endpoints</a>.</description>
         <pubDate>Wed, 23 Dec 2020 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#New_region:_South_America_(SÃ£o_Paulo)_2020-12-23</guid>
      </item>
      <item>
         <title>New region: Canada (central)</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Amazon QuickSight is now available in Canada (Central) (ca-central-1). For
					more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/regions.html?icmpid=docs_quicksight_console_rssdochistory">AWS Regions, websites, IP address ranges, and endpoints</a>.</description>
         <pubDate>Wed, 23 Dec 2020 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#New_region:_Canada_(central)_2020-12-23</guid>
      </item>
      <item>
         <title>Define an action to open a different sheet</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>QuickSight now supports navigation actions to enable you to open a
					different sheet with the included parameter values. For more information, see
						<a href="https://docs.aws.amazon.com/quicksight/latest/user/quicksight-actions.html?icmpid=docs_quicksight_console_rssdochistory">Using custom actions for filtering and navigating</a>. </description>
         <pubDate>Mon, 21 Dec 2020 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Define_an_action_to_open_a_different_sheet_2020-12-21</guid>
      </item>
      <item>
         <title>Data source enhancement: Athena federated query</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>QuickSight now supports connecting to Athena Federated Query. For more
					information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/create-a-data-set-athena.html?icmpid=docs_quicksight_console_rssdochistory">Creating a dataset using Amazon Athena data</a>. </description>
         <pubDate>Mon, 21 Dec 2020 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Data_source_enhancement:_Athena_federated_query_2020-12-21</guid>
      </item>
      <item>
         <title>New list items sheet control type</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Amazon QuickSight now supports single and multi-select list control on dashboards.
					For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/parameters-controls.html?icmpid=docs_quicksight_console_rssdochistory">Parameter controls</a>.</description>
         <pubDate>Fri, 18 Dec 2020 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#New_list_items_sheet_control_type_2020-12-18</guid>
      </item>
      <item>
         <title>New formatting options for tables</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>In QuickSight, you can now reorder columns in table charts. For more
					information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/tabular.html?icmpid=docs_quicksight_console_rssdochistory"> Using tables as visuals</a>. </description>
         <pubDate>Thu, 17 Dec 2020 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#New_formatting_options_for_tables_2020-12-17</guid>
      </item>
      <item>
         <title>Row-level security (RLS) now supports GRANT option only</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>To streamline and simplify RLS setup, QuickSight no longer supports
					using RLS in deny-access mode. To create a new RLS configurations, use the
					explicit grant-access model. Current RLS datasets and deny-access configurations
					should continue to work as expected. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/restrict-access-to-a-data-set-using-row-level-security.html?icmpid=docs_quicksight_console_rssdochistory">Using row-level security (RLS) to restrict access to a dataset</a>.
				</description>
         <pubDate>Sun, 6 Dec 2020 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Row-level_security_(RLS)_now_supports_GRANT_option_only_2020-12-06</guid>
      </item>
      <item>
         <title>New percentile functions</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>QuickSight now supports variations on percentile calculations,
					including aggregate functions <code class="code">percentileCont</code> and
						<code class="code">percentileDisc</code> and <code class="code">OVER</code> functions
						<code class="code">percentileContOver</code> and <code class="code">percentileDiscOver</code>. You can
					use all of these functions in the calculations editor in analysis mode. For more
					information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/functions-by-category.html?icmpid=docs_quicksight_console_rssdochistory">Functions by category</a>. </description>
         <pubDate>Sun, 6 Dec 2020 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#New_percentile_functions_2020-12-06</guid>
      </item>
      <item>
         <title>Dynamic queries, plus dataset editor improvements</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>QuickSight now enables you to improve performance for visuals based on
					direct queries by specifying unique keys for joined tables. There are also
					multiple interface improvements, such as settings for optional autopreviews,
					zoom in and out of data diagrams, join recommendations, and more. For more
					information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/joining-data.html?icmpid=docs_quicksight_console_rssdochistory">Joining data</a>. </description>
         <pubDate>Sun, 6 Dec 2020 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Dynamic_queries,_plus_dataset_editor_improvements_2020-12-06</guid>
      </item>
      <item>
         <title>Developer portal for embedding</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>The Dev Portal helps you learn how to use embedding by
					example in your web site or application. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/quicksight-dev-portal.html?icmpid=docs_quicksight_console_rssdochistory"> Using the dev portal</a>. </description>
         <pubDate>Mon, 30 Nov 2020 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Developer_portal_for_embedding_2020-11-30</guid>
      </item>
      <item>
         <title>New data source: Amazon OpenSearch</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>QuickSight now supports connecting to Amazon OpenSearch. For more
					information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/connecting-to-es.html?icmpid=docs_quicksight_console_rssdochistory">Using Amazon OpenSearch with QuickSight</a>. </description>
         <pubDate>Wed, 25 Nov 2020 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#New_data_source:_Amazon_OpenSearch_2020-11-25</guid>
      </item>
      <item>
         <title>Format metrics on pie charts</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>QuickSight now supports formatting metrics on pie charts to display
					values, percentages, or both. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/customizing-visual-data-labels.html?icmpid=docs_quicksight_console_rssdochistory"> Customizing data labels</a>. </description>
         <pubDate>Wed, 25 Nov 2020 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Format_metrics_on_pie_charts_2020-11-25</guid>
      </item>
      <item>
         <title>New formatting options for tables</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>In QuickSight, you can now vertically align and wrap the text for
					headers in table charts. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/tabular.html?icmpid=docs_quicksight_console_rssdochistory"> Using tables as visuals</a>. </description>
         <pubDate>Tue, 24 Nov 2020 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#New_formatting_options_for_tables_2020-11-24</guid>
      </item>
      <item>
         <title>New chart type: Box plots</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>QuickSight now supports using box plots so you can visualize how your
					data is distributed across an axis or over time. For more information, see
						<a href="https://docs.aws.amazon.com/quicksight/latest/user/box-plots.html?icmpid=docs_quicksight_console_rssdochistory"> Box plots</a>. </description>
         <pubDate>Tue, 24 Nov 2020 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#New_chart_type:_Box_plots_2020-11-24</guid>
      </item>
      <item>
         <title>Filled maps</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>QuickSight now supports filled maps so you can visualize your data over
					a geographical area. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/filled-maps.html?icmpid=docs_quicksight_console_rssdochistory"> Filled maps</a>. </description>
         <pubDate>Tue, 24 Nov 2020 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Filled_maps_2020-11-24</guid>
      </item>
      <item>
         <title>Favorite folders</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>In QuickSight, you can now favorite your folders for easy access. For
					more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/folders.html?icmpid=docs_quicksight_console_rssdochistory"> Organizing assets into folders</a>. </description>
         <pubDate>Tue, 24 Nov 2020 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Favorite_folders_2020-11-24</guid>
      </item>
      <item>
         <title>Change in display limits</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>For parameter controls and filters, Amazon QuickSight now displays up to 1,000
					sample values. When you have more than that, you use the search box to locate a
					value. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/parameters-controls.html?icmpid=docs_quicksight_console_rssdochistory"> Using a control with a parameter</a>. </description>
         <pubDate>Mon, 16 Nov 2020 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Change_in_display_limits_2020-11-16</guid>
      </item>
      <item>
         <title>Null rendering</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>QuickSight now allows null values to be updated to a custom string. For
					more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/changing-a-field-format.html?icmpid=docs_quicksight_console_rssdochistory"> Changing a field format</a>. </description>
         <pubDate>Mon, 9 Nov 2020 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Null_rendering_2020-11-09</guid>
      </item>
      <item>
         <title>New chart type: Waterfall charts</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>QuickSight now supports using waterfall charts so you can view your
					data sequentially. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/waterfall-chart.html?icmpid=docs_quicksight_console_rssdochistory"> Waterfall charts</a>. </description>
         <pubDate>Mon, 9 Nov 2020 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#New_chart_type:_Waterfall_charts_2020-11-09</guid>
      </item>
      <item>
         <title>Embedding for everyone</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>QuickSight Enterprise edition now supports embedding for everyone. When
					you purchase session packs with capacity pricing, you can enable visitors to use
					embedded dashboards without registering them as QuickSight users. For
					more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/embedded-analytics.html?icmpid=docs_quicksight_console_rssdochistory"> Embedded analytics</a>. </description>
         <pubDate>Mon, 9 Nov 2020 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Embedding_for_everyone_2020-11-09</guid>
      </item>
      <item>
         <title>Column-level security</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>QuickSight now supports using column-level security to restrict access
					to a dataset. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/restrict-access-to-a-data-set-using-column-level-security.html?icmpid=docs_quicksight_console_rssdochistory"> Using column-level security</a>. </description>
         <pubDate>Mon, 9 Nov 2020 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Column-level_security_2020-11-09</guid>
      </item>
      <item>
         <title>Service provider initiated federation</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>QuickSight Enterprise edition now supports service provider initiated
					federation, so you can sign on directly to QuickSight using your IAM Identity Center
					login and password. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/setup-quicksight-to-idp;.html?icmpid=docs_quicksight_console_rssdochistory">Setting up service providerâ€“Initiated federation with
						QuickSight enterprise edition</a>.</description>
         <pubDate>Fri, 30 Oct 2020 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Service_provider_initiated_federation_2020-10-30</guid>
      </item>
      <item>
         <title>New chart type: Funnel charts</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>QuickSight now supports using funnel charts so you can display your
					data in a linear process. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/funnel-charts.html?icmpid=docs_quicksight_console_rssdochistory"> Funnel charts</a>. </description>
         <pubDate>Thu, 29 Oct 2020 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#New_chart_type:_Funnel_charts_2020-10-29</guid>
      </item>
      <item>
         <title>Custom sorting</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>QuickSight now enables you to apply sort options on fields outside the
					field wells. This feature is available for all charts that support sorting. For
					more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/sorting-visual-data.html?icmpid=docs_quicksight_console_rssdochistory"> Describing data</a>. </description>
         <pubDate>Thu, 29 Oct 2020 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Custom_sorting_2020-10-29</guid>
      </item>
      <item>
         <title>New region: AWS GovCloud (US-West)</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Amazon QuickSight is now available in AWS GovCloud (US-West) (gov-west-1). For
					more information, see <a href="https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-aqs.html?icmpid=docs_quicksight_console_rssdochistory">QuickSight - AWS GovCloud (US)</a>.</description>
         <pubDate>Wed, 28 Oct 2020 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#New_region:_AWS_GovCloud_(US-West)_2020-10-28</guid>
      </item>
      <item>
         <title>New data source: Oracle</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>QuickSight now supports connecting to Oracle. For more information, see
						<a href="https://docs.aws.amazon.com/quicksight/latest/user/supported-data-sources.html?icmpid=docs_quicksight_console_rssdochistory">Supported data sources</a>.</description>
         <pubDate>Fri, 23 Oct 2020 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#New_data_source:_Oracle_2020-10-23</guid>
      </item>
      <item>
         <title>Filter across datasets</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>In QuickSight, you can now create filters that apply to multiple
					datasets in an analysis. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/adding-a-filter.html?icmpid=docs_quicksight_console_rssdochistory">Filtering data</a>.</description>
         <pubDate>Fri, 23 Oct 2020 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Filter_across_datasets_2020-10-23</guid>
      </item>
      <item>
         <title>Add field descriptions to datasets</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>QuickSight now enables you to add column or field descriptions to
					datasets. This metadata is visible in both datasets and analyses, helping you
					make your data self-explanatory. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/describing-data.html?icmpid=docs_quicksight_console_rssdochistory">Describing data</a>.</description>
         <pubDate>Fri, 23 Oct 2020 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Add_field_descriptions_to_datasets_2020-10-23</guid>
      </item>
      <item>
         <title>Filter controls on analysis sheets</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>QuickSight now offers a filter control that you can add to your
					analysis with a single click. You can put filters beside dashboard visuals and
					resize them to fit. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/filter-controls.html?icmpid=docs_quicksight_console_rssdochistory">Using filter controls</a>.</description>
         <pubDate>Mon, 5 Oct 2020 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Filter_controls_on_analysis_sheets_2020-10-05</guid>
      </item>
      <item>
         <title>New data source: Amazon Timestream</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>QuickSight now supports Amazon Timestream as a data source. For more
					information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/using-data-from-timestream.html?icmpid=docs_quicksight_console_rssdochistory">Using Amazon Timestream data with QuickSight</a>.</description>
         <pubDate>Thu, 1 Oct 2020 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#New_data_source:_Amazon_Timestream_2020-10-01</guid>
      </item>
      <item>
         <title>Export to excel</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>QuickSight now supports exporting data from pivot tables and table
					charts to Microsoft Excel (.xslx) format. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/exporting-data.html?icmpid=docs_quicksight_console_rssdochistory">Exporting data</a>.</description>
         <pubDate>Mon, 14 Sep 2020 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Export_to_excel_2020-09-14</guid>
      </item>
      <item>
         <title>Duplicate sheets</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>QuickSight now supports duplicating sheets. For more information, see
						<a href="https://docs.aws.amazon.com/quicksight/latest/user/working-with-multiple-sheets.html?icmpid=docs_quicksight_console_rssdochistory">Working with multiple sheets in an QuickSight
					analysis</a>.</description>
         <pubDate>Mon, 14 Sep 2020 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Duplicate_sheets_2020-09-14</guid>
      </item>
      <item>
         <title>Customize labels of totals and subtotals</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>In QuickSight, you can now add custom text to display beside totals and
					subtotals for pivot tables and table charts. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/format-tables-pivot-tables.html">Table and pivot table formatting options in
					QuickSight</a>.</description>
         <pubDate>Mon, 14 Sep 2020 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Customize_labels_of_totals_and_subtotals_2020-09-14</guid>
      </item>
      <item>
         <title>Skipped row details</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>When you import data into QuickSight, you now get better error messages
					and row-by-row information on what caused rows to be skipped during ingestion
					into SPICE. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/troubleshooting-skipped-rows.html?icmpid=docs_quicksight_console_rssdochistory">Troubleshooting skipped rows</a>.</description>
         <pubDate>Sat, 12 Sep 2020 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Skipped_row_details_2020-09-12</guid>
      </item>
      <item>
         <title>New configuration option for multivalue lists</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>QuickSight now supports a configuration option for multivalue lists to
					start with no values selected. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/parameters-set-up.html?icmpid=docs_quicksight_console_rssdochistory">Setting up parameters in Amazon QuickSight</a>. </description>
         <pubDate>Fri, 11 Sep 2020 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#New_configuration_option_for_multivalue_lists_2020-09-11</guid>
      </item>
      <item>
         <title>Reference lines</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>QuickSight now supports using reference lines in bar, line, and combo
					charts. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/reference-lines.html?icmpid=docs_quicksight_console_rssdochistory">Reference lines</a>.</description>
         <pubDate>Thu, 3 Sep 2020 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Reference_lines_2020-09-03</guid>
      </item>
      <item>
         <title>New table calculations</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>QuickSight now supports using window functions <code class="code">firstValue</code>
					and <code class="code">lastValue</code> in analyses. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/functions-by-category.html#table-calculations?icmpid=docs_quicksight_console_rssdochistory">Table calculations</a>.</description>
         <pubDate>Tue, 25 Aug 2020 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#New_table_calculations_2020-08-25</guid>
      </item>
      <item>
         <title>Multivalue default parameters</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>QuickSight now supports dynamic default values for multi-valued
					parameters. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/parameters-set-up.html#parameters-default-values?icmpid=docs_quicksight_console_rssdochistory">Creating parameter defaults in QuickSight</a>.</description>
         <pubDate>Tue, 25 Aug 2020 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Multivalue_default_parameters_2020-08-25</guid>
      </item>
      <item>
         <title>Last active status for users</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>QuickSight administrators can now see the last date and time that
					people accessed QuickSight. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/viewing-user-details.html?icmpid=docs_quicksight_console_rssdochistory">Viewing user details</a>.</description>
         <pubDate>Tue, 25 Aug 2020 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Last_active_status_for_users_2020-08-25</guid>
      </item>
      <item>
         <title>Join SQL queries, tables, and files</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>QuickSight now supports using custom SQL queries in joins with other
					queries, tables, and files. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/joining-data.html?icmpid=docs_quicksight_console_rssdochistory">Joining data</a>.</description>
         <pubDate>Tue, 25 Aug 2020 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Join_SQL_queries,_tables,_and_files_2020-08-25</guid>
      </item>
      <item>
         <title>Calculated expressions editor</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>The enhanced editor adds ease-of-use features to help you more easily create
					calculated expressions in QuickSight. With the new full-screen editor,
					you can add functions and values directly from the menu. For more information,
					see <a href="https://docs.aws.amazon.com/quicksight/latest/user/adding-a-calculated-field-analysis.html?icmpid=docs_quicksight_console_rssdochistory">Adding a calculated field to an analysis</a>.</description>
         <pubDate>Tue, 25 Aug 2020 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Calculated_expressions_editor_2020-08-25</guid>
      </item>
      <item>
         <title>Personal and shared folders</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>QuickSight Enterprise edition now offers personal and shared folders to
					make it easier to discover, organize, share, and explore your available assets.
					For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/folders.html?icmpid=docs_quicksight_console_rssdochistory">Organizing QuickSight assets into folders</a>.</description>
         <pubDate>Wed, 5 Aug 2020 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Personal_and_shared_folders_2020-08-05</guid>
      </item>
      <item>
         <title>QuickSight support for multitenancy</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>In Enterprise edition, QuickSight now offers an additional layer of
					security to support multitenancy. By creating users and groups in a
					QuickSight namespace, you can isolate them from users and groups in other
					namespaces. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/namespaces.html?icmpid=docs_quicksight_console_rssdochistory">Supporting multitenancy with isolated namespaces</a>.</description>
         <pubDate>Thu, 23 Jul 2020 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#QuickSight_support_for_multitenancy_2020-07-23</guid>
      </item>
      <item>
         <title>Embed the QuickSight console</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>In QuickSight Enterprise edition, you can now provide the full
					dashboard authoring experience of the QuickSight console in your own
					custom-branded authoring portal. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/embedding-the-quicksight-console.html?icmpid=docs_quicksight_console_rssdochistory">Embedding the QuickSight console</a>.</description>
         <pubDate>Thu, 23 Jul 2020 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Embed_the_QuickSight_console_2020-07-23</guid>
      </item>
      <item>
         <title>Datasets with 2,000 columns</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>QuickSight now supports datasets that have up to 2,000 columns. For
					more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/data-source-limits.html?icmpid=docs_quicksight_console_rssdochistory">Data source limits</a>.</description>
         <pubDate>Thu, 23 Jul 2020 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Datasets_with_2,000_columns_2020-07-23</guid>
      </item>
      <item>
         <title>Customized permissions</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>In QuickSight Enterprise edition, you can now create custom roles to
					restrict a person from using specific functionality in the QuickSight
					console, for example to control who can manage data sources and datasets or who
					can manage or subscribe to email reports. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/customizing-permissions-to-the-quicksight-console.html?icmpid=docs_quicksight_console_rssdochistory">Customizing access to the QuickSight console</a>.</description>
         <pubDate>Thu, 23 Jul 2020 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Customized_permissions_2020-07-23</guid>
      </item>
      <item>
         <title>Customize the console</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>In QuickSight Enterprise edition, you can now choose whether to show or
					hide QuickSight startup samples and videos. You can also create and
					specify a default theme to add branding to your experience of the
					QuickSight console. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/customizing-quicksight.html?icmpid=docs_quicksight_console_rssdochistory">Customizing the QuickSight console</a>.</description>
         <pubDate>Thu, 23 Jul 2020 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Customize_the_console_2020-07-23</guid>
      </item>
      <item>
         <title>Larger SPICE datasets</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>QuickSight Enterprise edition now supports SPICE
					datasets with up to 250 million (250,000,000) rows or 500 GB. For more
					information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/data-source-limits.html?icmpid=docs_quicksight_console_rssdochistory">Data source limits</a>.</description>
         <pubDate>Thu, 9 Jul 2020 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Larger_SPICE_datasets_2020-07-09</guid>
      </item>
      <item>
         <title>Display width settings</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>In QuickSight, you can now choose between responsive and fixed layouts
					for your analyses and dashboards. You can also temporarily change your current
					view from the menu bar. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/display-settings.html?icmpid=docs_quicksight_console_rssdochistory">Display settings</a>.</description>
         <pubDate>Thu, 9 Jul 2020 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Display_width_settings_2020-07-09</guid>
      </item>
      <item>
         <title>Data refresh notifications</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>QuickSight now supports sending email to notify SPICE
					dataset owners when data refresh fails. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/refreshing-imported-data.html?icmpid=docs_quicksight_console_rssdochistory">Refreshing data</a>.</description>
         <pubDate>Thu, 9 Jul 2020 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Data_refresh_notifications_2020-07-09</guid>
      </item>
      <item>
         <title>Color settings for heat maps and tree maps</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now customize gradient colors for your heat maps and tree maps in
					QuickSight. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/changing-visual-colors.html?icmpid=docs_quicksight_console_rssdochistory"> Changing colors on heat maps and tree maps</a>. </description>
         <pubDate>Thu, 9 Jul 2020 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Color_settings_for_heat_maps_and_tree_maps_2020-07-09</guid>
      </item>
      <item>
         <title>Font choice</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now customize your theme with a font. Choose from a selection of fonts
					supported by QuickSight. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/themes-in-quicksight.html?icmpid=docs_quicksight_console_rssdochistory">Using themes in QuickSight</a>.</description>
         <pubDate>Wed, 8 Jul 2020 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Font_choice_2020-07-08</guid>
      </item>
      <item>
         <title>AWS Lake Formation</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>If you use QuickSight Enterprise edition to query Amazon Athena, you can
					simplify data access management by using AWS Lake Formation to control permissions to
					Athena. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/lake-formation.html?icmpid=docs_quicksight_console_rssdochistory">Authorizing connections through AWS Lake Formation</a>.</description>
         <pubDate>Mon, 29 Jun 2020 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#AWS_Lake_Formation_2020-06-29</guid>
      </item>
      <item>
         <title>New chart type</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>QuickSight now supports using histograms so you can display the
					distribution of values in your data. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/histogram-charts.html?icmpid=docs_quicksight_console_whatsnew">Histogram charts</a>.</description>
         <pubDate>Fri, 12 Jun 2020 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#New_chart_type_2020-06-12</guid>
      </item>
      <item>
         <title>Gauge chart update</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now add conditional formatting to gauge charts in QuickSight.
					For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/conditional-formatting-for-visuals.html?icmpid=docs_quicksight_console_whatsnew">Adding conditional formatting to visuals</a>.</description>
         <pubDate>Fri, 12 Jun 2020 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Gauge_chart_update_2020-06-12</guid>
      </item>
      <item>
         <title>Five new languages</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>QuickSight now supports Danish, Dutch, Finnish, Norwegian, and Swedish.
					These languages expand upon the existing 15 languages already available in
					QuickSight. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/choosing-a-language-in-quicksight.html?icmpid=docs_quicksight_console_whatsnew">Choosing a language in Amazon QuickSight</a>. </description>
         <pubDate>Fri, 12 Jun 2020 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Five_new_languages_2020-06-12</guid>
      </item>
      <item>
         <title>New region: Mumbai</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Amazon QuickSight is now available in Asia Pacific (Mumbai) (ap-south-1). For more
					information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/regions.html?icmpid=docs_quicksight_console_whatsnew">AWS Regions, websites, IP address ranges, and endpoints</a>.</description>
         <pubDate>Wed, 3 Jun 2020 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#New_region:_Mumbai_2020-06-03</guid>
      </item>
      <item>
         <title>New SQL editor</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>QuickSight enhanced the SQL editor that you use to create datasets from
					SQL queries. The new SQL editor supports syntax highlighting, basic
					autocomplete, autoindent, and line numbering. Also, you can use the new schema
					explorer to interactively explore schemas, tables, fields, and data types. For
					more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/adding-a-SQL-query.html?icmpid=icmpid=docs_quicksight_console_whatsnew">Using a SQL query</a>.</description>
         <pubDate>Wed, 20 May 2020 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#New_SQL_editor_2020-05-20</guid>
      </item>
      <item>
         <title>Amazon SageMaker AI integration now generally available</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>The integration of SageMaker AI with QuickSight launched in preview just before
					AWS re:Invent 2019. Now, this feature is generally available in all
					AWS Regions that are supported by QuickSight. Amazon QuickSight and SageMaker AI together
					makes it faster, easier, and more cost-effective for customers to make use of
					their machine learning models for visualization and predictions. For more
					information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/sagemaker-integration.html?icmpid=icmpid=docs_quicksight_console_whatsnew">Amazon QuickSight integration with SageMaker</a>.</description>
         <pubDate>Tue, 19 May 2020 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Amazon_SageMaker_AI_integration_now_generally_available_2020-05-19</guid>
      </item>
      <item>
         <title>Update to presto data sources</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now use nonauthenticated private Presto as a data source. For more
					information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/create-a-data-source-presto.html?icmpid=docs_quicksight_console_rssdochistory">Creating a data source using presto</a>.</description>
         <pubDate>Mon, 18 May 2020 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Update_to_presto_data_sources_2020-05-18</guid>
      </item>
      <item>
         <title>Rewrite of Amazon QuickSight VPC connection section</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Based on your feedback, we completely rewrote this documentation to better
					explain using Amazon VPC with QuickSight. It includes examples and AWS CLI
					commands to help you establish the path from Amazon QuickSight to your data source,
					even if you're using on-premises sources. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/working-with-aws-vpc.html?icmpid=docs_quicksight_console_whatsnew">QuickSight VPC connections</a>. </description>
         <pubDate>Mon, 18 May 2020 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Rewrite_of_Amazon_QuickSight_VPC_connection_section_2020-05-18</guid>
      </item>
      <item>
         <title>Use logarithmic scale with QuickSight</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now format visuals using log scale. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/changing-visual-scale-axis-range.html?icmpid=docs_quicksight_console_rssdochistory">Changing the visual scale</a>.</description>
         <pubDate>Fri, 1 May 2020 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Use_logarithmic_scale_with_QuickSight_2020-05-01</guid>
      </item>
      <item>
         <title>Severity levels for QuickSight anomaly detection insights</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now choose the level of severity for anomalies that display in your
					insight widgets. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/anomaly-detection-using.html?icmpid=docs_quicksight_console_rssdochistory">Using anomaly detection</a>.</description>
         <pubDate>Fri, 17 Apr 2020 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Severity_levels_for_QuickSight_anomaly_detection_insights_2020-04-17</guid>
      </item>
      <item>
         <title>QuickSight adds a new visual type</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>The new visual type, stacked area line charts, is similar to area charts
					except that the stacked values indicate the relationship that each value
					contributes to the whole. Using stacked area charts, you can display cumulative
					totals over time while displaying the breakdown by the chosen category. For more
					information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/line-charts.html?icmpid=docs_quicksight_console_rssdochistory">Line charts</a>.</description>
         <pubDate>Fri, 17 Apr 2020 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#QuickSight_adds_a_new_visual_type_2020-04-17</guid>
      </item>
      <item>
         <title>QuickSight activates legends by adding menus for quick feature access</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>QuickSight now supports clicking on legend items to quickly access
					features like filtering, drilling, chart colors, and custom actions for
					filtering and URLs. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/focusing-on-visual-elements.html?icmpid=docs_quicksight_console_rssdochistory">Focusing on visual elements</a> and <a href="https://docs.aws.amazon.com/quicksight/latest/user/quicksight-actions.html?icmpid=docs_quicksight_console_rssdochistory">Custom actions in QuickSight</a>.</description>
         <pubDate>Fri, 17 Apr 2020 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#QuickSight_activates_legends_by_adding_menus_for_quick_feature_access_2020-04-17</guid>
      </item>
      <item>
         <title>Improvements to visual controls in QuickSight</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>The on-visual menu can now float at the upper-right corner of the visual,
					moving inside or outside the border of the visual. Plus, you can make your
					visuals smaller and have more of them, as many as 36 across. For smaller
					visuals, the new visual controls have more viewing area for charts and insights.
					To see the new menu, choose one of your visuals. For more information, see
						<a href="https://docs.aws.amazon.com/quicksight/latest/user/working-with-visuals.html?icmpid=docs_quicksight_console_rssdochistory">Working with visuals</a>.</description>
         <pubDate>Fri, 17 Apr 2020 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Improvements_to_visual_controls_in_QuickSight_2020-04-17</guid>
      </item>
      <item>
         <title>QuickSight adds cascading filters</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now create cascading filters by adding them to custom actions in your
					analyses and dashboards. Each custom filter action can target one or more
					visuals in the same sheet, creating a cascading filter effect. For more
					information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/quicksight-actions.html?icmpid=docs_quicksight_console_rssdochistory">Custom actions in QuickSight</a>.</description>
         <pubDate>Thu, 2 Apr 2020 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#QuickSight_adds_cascading_filters_2020-04-02</guid>
      </item>
      <item>
         <title>Modulo operation available in Amazon QuickSight</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now use modulo operation to find the remainder after dividing one
					number into another. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/mod-function.html?icmpid=docs_quicksight_console_rssdochistory">mod</a>.</description>
         <pubDate>Sun, 8 Mar 2020 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Modulo_operation_available_in_Amazon_QuickSight_2020-03-08</guid>
      </item>
      <item>
         <title>Images in Amazon QuickSight narratives</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now insert images from URLs to be rendered as part of a narrative.
					Images can be resized, conditionally shown within an IF block, and also
					hyperlinked with the URL feature. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/using-narratives-expression-editor-menus.html?icmpid=docs_quicksight_console_rssdochistory">Expression editor screen and menus</a>.</description>
         <pubDate>Sun, 8 Mar 2020 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Images_in_Amazon_QuickSight_narratives_2020-03-08</guid>
      </item>
      <item>
         <title>Amazon QuickSight adds minimum and maximum dates</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now use minimum and maximum date aggregations in tables and pivot
					tables. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/max-function.html?icmpid=docs_quicksight_console_rssdochistory">max</a> and <a href="https://docs.aws.amazon.com/quicksight/latest/user/min-function.html?icmpid=docs_quicksight_console_rssdochistory">min</a>.</description>
         <pubDate>Sun, 8 Mar 2020 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Amazon_QuickSight_adds_minimum_and_maximum_dates_2020-03-08</guid>
      </item>
      <item>
         <title>Now you can customize minimum delta values to enhance QuickSight ML-powered anomaly detection</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Now you can control the minimum delta value that QuickSight uses to
					detect anomalies (also known as outliers). You can change this setting when you
					are configuring or exploring anomalies. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/anomaly-detection.html?icmpid=docs_quicksight_console_rssdochistory">Detecting outliers with ML-powered anomaly detection</a>.</description>
         <pubDate>Tue, 4 Feb 2020 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Now_you_can_customize_minimum_delta_values_to_enhance_QuickSight_ML-powered_anomaly_detection_2020-02-04</guid>
      </item>
      <item>
         <title>Improvements in the QuickSight narrative expression editor</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>QuickSight now provides a much more spacious interface for editing
					narrative expressions. The interface now has instant feedback in a preview of
					your evaluated narrative before you save any changes. Plus, narratives now
					support both static and dynamic URLs in your custom narratives for links to
					searches, apps, other dashboards, other sheets in the same dashboard, and more.
					For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/using-narratives-expression-editor.html?icmpid=docs_quicksight_console_rssdochistory">Using autonarratives</a>.</description>
         <pubDate>Tue, 4 Feb 2020 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Improvements_in_the_QuickSight_narrative_expression_editor_2020-02-04</guid>
      </item>
      <item>
         <title>SageMaker AI integration now available in more AWS Regions</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>The public preview for integrating SageMaker AI with QuickSight is now
					available in all of the AWS Regions that are supported by QuickSight. For more
					information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/sagemaker-integration.html?icmpid=docs_quicksight_console_whatsnew">Amazon QuickSight integration with SageMaker</a>.</description>
         <pubDate>Fri, 10 Jan 2020 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#SageMaker_AI_integration_now_available_in_more_AWS_Regions_2020-01-10</guid>
      </item>
      <item>
         <title>QuickSight now enables you to choose an Amazon Athena workgroup</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>By choosing an Athena workgroup, you can better manage your Athena datasets.
					Using this option, you can also allocate Athena costs to the workgroup that
					QuickSight is using, for better cost reporting. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/create-a-data-set-athena.html?icmpid=docs_quicksight_console_rssdochistory">Creating a dataset using Amazon Athena</a>.</description>
         <pubDate>Tue, 10 Dec 2019 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#QuickSight_now_enables_you_to_choose_an_Amazon_Athena_workgroup_2019-12-10</guid>
      </item>
      <item>
         <title>Private VPC support for presto in QuickSight</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Now Presto can use a VPC connection. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/working-with-aws-vpc.html#vpc-supported?icmpid=docs_quicksight_console_rssdochistory">Supported data sources for VPC</a>.</description>
         <pubDate>Tue, 10 Dec 2019 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Private_VPC_support_for_presto_in_QuickSight_2019-12-10</guid>
      </item>
      <item>
         <title>New mathematical functions in QuickSight</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Amazon QuickSight now supports functions for base 10 logarithms (<code class="code">log</code>),
					natural logarithm (<code class="code">ln</code>), absolute value (<code class="code">abs</code>), square
					root (<code class="code">sqrt</code>), and base of natural log e raised to the power of
						(<code class="code">exp</code>). For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/calculated-field-reference.html?icmpid=docs_quicksight_console_rssdochistory">Functions and operators</a>.</description>
         <pubDate>Tue, 10 Dec 2019 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#New_mathematical_functions_in_QuickSight_2019-12-10</guid>
      </item>
      <item>
         <title>New LAA functions in QuickSight</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Now you can use <code class="code">rank</code>, <code class="code">denseRank</code>, and
						<code class="code">percentileRank</code> for level-aware aggregations. For more
					information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/level-aware-calculations.html?icmpid=docs_quicksight_console_rssdochistory">Using level-aware aggregations</a>.</description>
         <pubDate>Tue, 10 Dec 2019 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#New_LAA_functions_in_QuickSight_2019-12-10</guid>
      </item>
      <item>
         <title>Integrate SageMaker AI ML models into your QuickSight analyses and dashboards</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>In this public preview, QuickSight launches the ability to integrate
					machine learning (ML) models created and trained in SageMaker AI. This new feature makes
					it easier to augment your business data with ML predictions. Add your data
					scientists' prebuilt inferences and predictions to your analysts'
					dashboards, and let the collaboration and decision-making begin. For more
					information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/sagemaker-integration.html?icmpid=docs_quicksight_console_rssdochistory">Amazon QuickSight integration with SageMaker</a>.</description>
         <pubDate>Tue, 26 Nov 2019 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Integrate_SageMaker_AI_ML_models_into_your_QuickSight_analyses_and_dashboards_2019-11-26</guid>
      </item>
      <item>
         <title>New formatting options for visuals in QuickSight</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Amazon QuickSight launches more formatting for visuals and visuals titles,
					including font sizes from extra small to extra large. In key performance
					indicators (KPIs), you can set font sizes for primary and comparison values. In
					pivot tables and tables, you can see font sizes for table headers, cells,
					totals, and subtotals. Now your visuals render better even when smaller and with
					less padding between charts. For combo charts, you can now synchronize the
					Y-axes for both bars and lines into a single axis. For more information, see
						<a href="https://docs.aws.amazon.com/quicksight/latest/user/formatting-a-visual.html?icmpid=docs_quicksight_console_rssdochistory">Formatting a visual</a>.</description>
         <pubDate>Sat, 23 Nov 2019 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#New_formatting_options_for_visuals_in_QuickSight_2019-11-23</guid>
      </item>
      <item>
         <title>QuickSight supports the now function in SPICE</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/now-function.html?icmpid=docs_quicksight_console_rssdochistory"><code class="code">now</code></a>.</description>
         <pubDate>Fri, 22 Nov 2019 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#QuickSight_supports_the_now_function_in_SPICE_2019-11-22</guid>
      </item>
      <item>
         <title>QuickSight now supports seconds in SPICE</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Seconds are now supported in SPICE datasets. Datetime fields
					are no longer truncated to minutes. Now you can use the <code class="code">SS</code> option
					for the <code class="code">period</code> parameter in date functions including
						<code class="code">addDateTime</code>, <code class="code">dateDiff</code>, <code class="code">extract</code>, and
						<code class="code">truncDate</code>. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/functions-by-category.html#date-functions.html?icmpid=docs_quicksight_console_rssdochistory">Date functions</a>.</description>
         <pubDate>Fri, 22 Nov 2019 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#QuickSight_now_supports_seconds_in_SPICE_2019-11-22</guid>
      </item>
      <item>
         <title>QuickSight now has themes</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now create a collection of themes, and apply a theme to an analysis
					and all its dashboards. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/themes-in-quicksight.html?icmpid=docs_quicksight_console_rssdochistory">Using themes in QuickSight</a>.</description>
         <pubDate>Fri, 22 Nov 2019 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#QuickSight_now_has_themes_2019-11-22</guid>
      </item>
      <item>
         <title>New QuickSight API operations</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Amazon QuickSight launches new API operations to programmatically manage your data,
					dashboards, and fine-grained access control capabilities linked with AWS Identity and Access Management
					(IAM). With new data API operations, you can create, update, and delete Amazon Quick Sight
					data sources and datasets programmatically. You can also manage data refreshes
					on your SPICE datasets with API operations. Amazon QuickSight also
					introduces templates, which store the visual configuration and data schemas
					required for a dashboard. You can transfer templates across accounts or use them
					to instantiate dashboards with the same visual presentation but different data.
					For more information, see the <a href="https://docs.aws.amazon.com/quicksight/latest/APIReference/qs-api-overview.html?icmpid=docs_quicksight_console_rssdochistory">Amazon QuickSight API reference</a>.</description>
         <pubDate>Fri, 22 Nov 2019 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#New_QuickSight_API_operations_2019-11-22</guid>
      </item>
      <item>
         <title>QuickSight now supports conditional formatting for tables, pivot tables, and key performance indicators (KPIs).</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description> For tables and pivot tables, you can set multiple conditions for fields or
					supported aggregations, along with format options to apply to a target cell. For
					KPIs, you can format the primary value based on conditions that are applied to
					any dimension in the dataset. The conditional formatting options now supported
					are text color, background color, and placement of supported icons. You can use
					icons from the provided set, or you can use Unicode icons instead. For more
					information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/conditional-formatting-for-visuals.html?icmpid=docs_quicksight_console_rssdochistory">Adding conditional formatting to visuals</a>.</description>
         <pubDate>Mon, 18 Nov 2019 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#QuickSight_now_supports_conditional_formatting_for_tables,_pivot_tables,_and_key_performance_indicators_(KPIs)._2019-11-18</guid>
      </item>
      <item>
         <title>View history for SPICE ingestion on your Amazon QuickSight datasets</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now view the ingestion history for SPICE datasets in
					Amazon QuickSight. See information like when the latest ingestion started, how long
					it took, and what its status is. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/view-history-of-spice-ingestion.html?icmpid=docs_quicksight_console_rssdochistory">View SPICE ingestion history</a>.</description>
         <pubDate>Thu, 7 Nov 2019 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#View_history_for_SPICE_ingestion_on_your_Amazon_QuickSight_datasets_2019-11-07</guid>
      </item>
      <item>
         <title>Add your own functionality to visuals with Amazon QuickSight actions</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Amazon QuickSight enables you to add to the basic functionality for visuals by
					creating your own custom actions for filtering or opening URLs. For more
					information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/quicksight-actions.html?icmpid=docs_quicksight_console_rssdochistory">Custom actions in Amazon QuickSight</a>.</description>
         <pubDate>Thu, 7 Nov 2019 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Add_your_own_functionality_to_visuals_with_Amazon_QuickSight_actions_2019-11-07</guid>
      </item>
      <item>
         <title>Amazon QuickSight now supports dynamic sheet titles</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now use parameters in sheet titles to make the context of a dashboard
					clearer to the reader. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/formatting-a-visual.html?icmpid=docs-quicksight-rssdochistory">Formatting a visual</a>.</description>
         <pubDate>Wed, 6 Nov 2019 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Amazon_QuickSight_now_supports_dynamic_sheet_titles_2019-11-06</guid>
      </item>
      <item>
         <title>Use Amazon QuickSight to join data from multiple data sources</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Amazon QuickSight now supports creating datasets that join multiple data sources.
					For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/joining-data.html?icmpid=docs_quicksight_console_rssdochistory">Joining data</a>.</description>
         <pubDate>Tue, 5 Nov 2019 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Use_Amazon_QuickSight_to_join_data_from_multiple_data_sources_2019-11-05</guid>
      </item>
      <item>
         <title>Amazon QuickSight mobile iOS update and a new Android app</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Get access to insights from your data on the fly. Download the updated iOS app
					or the new Android app. You can browse, favorite, and interact with your
					dashboards and explore your data with drilldowns and filters. You can stay ahead
					of the curve by using forecasting. You can get email alerts when unexpected
					changes happen in your data, and you can share those insights with colleagues.
					For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/using-quicksight-mobile.html?icmpid=docs_quicksight_console_rssdochistory">Amazon QuickSight mobile</a>.</description>
         <pubDate>Tue, 5 Nov 2019 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Amazon_QuickSight_mobile_iOS_update_and_a_new_Android_app_2019-11-05</guid>
      </item>
      <item>
         <title>Amazon QuickSight supports printing</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Now you can print a dashboard or an analysis. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/printing1.html?icmpid=docs_quicksight_console_rssdochistory">Printing</a>. </description>
         <pubDate>Thu, 17 Oct 2019 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Amazon_QuickSight_supports_printing_2019-10-17</guid>
      </item>
      <item>
         <title>Amazon QuickSight supports a new AWS Region</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Amazon QuickSight is now available in Asia Pacific (Seoul) (ap-northeast-2). For
					more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/regions.html?icmpid=docs-quicksight-rssdochistory">AWS Regions, websites, IP address ranges, and endpoints</a>.</description>
         <pubDate>Thu, 17 Oct 2019 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Amazon_QuickSight_supports_a_new_AWS_Region_2019-10-17</guid>
      </item>
      <item>
         <title>Amazon QuickSight now supports visual-level formatting</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Now, any formatting you apply from the field wells is applied only to the
					selected visual. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/formatting-a-visual.html?icmpid=docs-quicksight-rssdochistory">Formatting a visual</a>.</description>
         <pubDate>Thu, 17 Oct 2019 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Amazon_QuickSight_now_supports_visual-level_formatting_2019-10-17</guid>
      </item>
      <item>
         <title>Transpose tables</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>In table visuals, you can now transpose columns and rows. For more
					information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/tabular.html?icmpid=docs_quicksight_console_rssdochistory">Tables</a>.</description>
         <pubDate>Thu, 10 Oct 2019 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Transpose_tables_2019-10-10</guid>
      </item>
      <item>
         <title>Shared data sources</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Share data sources with other users and groups. For more information, see
						<a href="https://docs.aws.amazon.com/quicksight/latest/user/shared-data-sources.html?icmpid=docs_quicksight_console_rssdochistory">Shared data sources</a>. </description>
         <pubDate>Thu, 10 Oct 2019 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Shared_data_sources_2019-10-10</guid>
      </item>
      <item>
         <title>SPICE enhancements</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>SPICE dashboards now support new wildcard filters on
					dimensions. You can now filter your data using any of the available wildcard
					filters: 'contains', 'starts with', 'end with', 'equals'. Additionally,
						SPICE dashboards now support new string functions
						(<code class="code">toString</code> and <code class="code">parseDecimal</code>) and two new date
					functions (<code class="code">parseDate</code> and <code class="code">formatDate</code>). For more
					information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/calculated-field-reference.html?icmpid=docs_quicksight_console_rssdochistory">Calculated fields</a>.</description>
         <pubDate>Thu, 10 Oct 2019 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#SPICE_enhancements_2019-10-10</guid>
      </item>
      <item>
         <title>New publishing options for dashboards</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Control your user experience with more publishing options for your dashboards.
					These options include ability to toggle the filter pane, tooltips, drill
					up/down, and more. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/creating-a-dashboard.html?icmpid=docs_quicksight_console_rssdochistory">Publish a dashboard</a>. </description>
         <pubDate>Thu, 10 Oct 2019 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#New_publishing_options_for_dashboards_2019-10-10</guid>
      </item>
      <item>
         <title>New median function</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Amazon QuickSight supports median as a new aggregation. For more information, see
						<a href="https://docs.aws.amazon.com/quicksight/latest/user/median-function.html?icmpid=docs_quicksight_console_rssdochistory"><code class="code">median</code></a>.</description>
         <pubDate>Thu, 10 Oct 2019 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#New_median_function_2019-10-10</guid>
      </item>
      <item>
         <title>New filter functionality</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Amazon QuickSight now supports additional relative date filter options. For more
					information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/add-a-date-filter2.html?icmpid=docs_quicksight_console_rssdochistory">Date filters</a>.</description>
         <pubDate>Thu, 10 Oct 2019 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#New_filter_functionality_2019-10-10</guid>
      </item>
      <item>
         <title>New aggregations for fields</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now use Nth percentile, median, standard deviation, and variance in
					field wells, filters, and ML Insights. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/changing-field-aggregation.html?icmpid=docs_quicksight_console_rssdochistory">Field aggregations</a>.</description>
         <pubDate>Thu, 10 Oct 2019 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#New_aggregations_for_fields_2019-10-10</guid>
      </item>
      <item>
         <title>Filter for context</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now filter text using the following wildcard comparison types:
					contains, does not contain, begins with, and ends with. For more information,
					see <a href="https://docs.aws.amazon.com/quicksight/latest/user/add-a-text-filter-data-prep.html#add-text-filter-custom-list?icmpid=docs_quicksight_console_rssdochistory">Text filters</a>.</description>
         <pubDate>Thu, 10 Oct 2019 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Filter_for_context_2019-10-10</guid>
      </item>
      <item>
         <title>Use the power operator (^) in SPICE</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>QuickSight now supports using the power operator (<code class="code">^</code>) on
						SPICE datasets. You can use the power operator with any
					numeric field, with any valid exponent. For example, "<code class="code">revenue ^
					0.5</code>" computes the square root of the revenue field. For more information,
					see <a href="https://docs.aws.amazon.com/quicksight/latest/user/arithmetic-and-comparison-operators.html?icmpid=docs-quicksight-whatsnew">Arithmetic and comparison operators</a>.</description>
         <pubDate>Wed, 11 Sep 2019 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Use_the_power_operator_(^)_in_SPICE_2019-09-11</guid>
      </item>
      <item>
         <title>Use string functions in SPICE</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Now you can use string functions for calculated fields in your analyses based
					on SPICE datasets. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/functions-by-category.html?icmpid=docs-quicksight-whatsnew">Functions by category</a>.</description>
         <pubDate>Wed, 11 Sep 2019 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Use_string_functions_in_SPICE_2019-09-11</guid>
      </item>
      <item>
         <title>Use level-aware aggregations to control your calculations</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>QuickSight now supports level-aware aggregation calculations. Using
					this feature, you can perform aggregations at prefilter and preaggregation
					levels, before aggregations that happen in the display. This helps you explore
					more advanced query-building strategies than ever before. For more information,
					see <a href="https://docs.aws.amazon.com/quicksight/latest/user/level-aware-calculations.html#spice-limits?icmpid=docs-quicksight-whatsnew">Level-aware aggregations</a>.</description>
         <pubDate>Wed, 11 Sep 2019 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Use_level-aware_aggregations_to_control_your_calculations_2019-09-11</guid>
      </item>
      <item>
         <title>Sort your anomalies</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Now you can choose how to sort anomalies on the insight widget and in the
					anomaly exploration page. Choosing how to prioritize anomalies can help you
					identify the anomalies that are the most important to you. For more information,
					see <a href="https://docs.aws.amazon.com/quicksight/latest/user/anomaly-detection-using.html?icmpid=docs-quicksight-whatsnew">Using ML-powered anomaly detection</a>.</description>
         <pubDate>Wed, 11 Sep 2019 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Sort_your_anomalies_2019-09-11</guid>
      </item>
      <item>
         <title>Put 100 million rows into a SPICE dataset</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>We changed the SPICE dataset limit from 25GB to 100 million
					rows for Enterprise edition (and 25 million rows for Standard edition). For more
					information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/data-source-limits.html#spice-limits?icmpid=docs-quicksight-whatsnew">SPICE data source limits</a>.</description>
         <pubDate>Wed, 11 Sep 2019 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Put_100_million_rows_into_a_SPICE_dataset_2019-09-11</guid>
      </item>
      <item>
         <title>Rename your dashboard, keep your settings</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Amazon QuickSight now supports renaming your published dashboards in place. You can
					change the name and still keep your settings and subscribers. For more
					information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/creating-a-dashboard.html?icmpid=docs-quicksight-whatsnew">Publishing a dashboards</a>.</description>
         <pubDate>Fri, 6 Sep 2019 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Rename_your_dashboard,_keep_your_settings_2019-09-06</guid>
      </item>
      <item>
         <title>New visual type: Word clouds</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Amazon QuickSight supports word cloud visuals that are based on different
					aggregations over any dimension in your dataset. You can drill down, focus on
					specific data points, and apply specific colors to data points on the word
					cloud. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/word-cloud.html?icmpid=docs-quicksight-rssdochistory">Word clouds</a>.</description>
         <pubDate>Thu, 5 Sep 2019 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#New_visual_type:_Word_clouds_2019-09-05</guid>
      </item>
      <item>
         <title>Filter out the last n time periods</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Amazon QuickSight lets you exclude a specific number and type of time periods from
					a time range (after) filter. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/add-a-date-filter2.html?icmpid=docs-quicksight-rssdochistory">Adding a date filter</a>.</description>
         <pubDate>Thu, 5 Sep 2019 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Filter_out_the_last_n_time_periods_2019-09-05</guid>
      </item>
      <item>
         <title>Amazon QuickSight new feature to mark favorites</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Mark your favorite dashboards and analyses so you can come back to them
					quickly. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/using-quicksight-ui-start.html?icmpid=docs-quicksight-rssdochistory">Using the QuickSight start page</a>.</description>
         <pubDate>Thu, 5 Sep 2019 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Amazon_QuickSight_new_feature_to_mark_favorites_2019-09-05</guid>
      </item>
      <item>
         <title>Amazon QuickSight Enterprise edition adds anomaly alerts</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Your readers can subscribe themselves to anomaly alerts on dashboards to get
					the latest ML-powered anomaly detection and contribution analysis by email. For
					more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/using-dashboards.html?icmpid=docs-quicksight-rssdochistory">Using data dashboards</a>.</description>
         <pubDate>Thu, 5 Sep 2019 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Amazon_QuickSight_Enterprise_edition_adds_anomaly_alerts_2019-09-05</guid>
      </item>
      <item>
         <title>QuickSight adds custom colors for charts.</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>With the QuickSight enhanced color picker, you can choose custom colors
					for charts where color customization is supported. The enhanced color picker
					also retains the eight most recently used custom colors for easy selection
					across multiple charts. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/changing-visual-colors.html?icmpid=docs-quicksight-rssdochistory">Changing visual colors</a>.</description>
         <pubDate>Thu, 1 Aug 2019 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#QuickSight_adds_custom_colors_for_charts._2019-08-01</guid>
      </item>
      <item>
         <title>Detect anomalies with less data</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>In Amazon QuickSight Enterprise edition, we lowered the required minimum data
					points to 15 for training anomaly detection. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/ml-data-set-requirements.html?icmpid=docs-quicksight-rssdochistory">Dataset requirements for using ML insights with
					QuickSight</a>.</description>
         <pubDate>Thu, 1 Aug 2019 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Detect_anomalies_with_less_data_2019-08-01</guid>
      </item>
      <item>
         <title>Amazon QuickSight supports new AWS Regions</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Amazon QuickSight is available in Europe (London) and Europe (Frankfurt).
					Also, you can now connect to Active Directory in any AWS Region supported by
					Amazon QuickSight, except Asia Pacific (Singapore) and Asia Pacific (Sydney). For
					more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/regions.html?icmpid=docs-quicksight-rssdochistory">AWS Regions and IP address ranges</a>.</description>
         <pubDate>Thu, 1 Aug 2019 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Amazon_QuickSight_supports_new_AWS_Regions_2019-08-01</guid>
      </item>
      <item>
         <title>Embedding for Active Directory</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>In Amazon QuickSight Enterprise edition, you can now embed dashboards for users
					authenticated through Active Directory. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/embedding-dashboards.html?icmpid=docs-quicksight-rssdochistory">Embedding dashboards</a>.</description>
         <pubDate>Thu, 11 Jul 2019 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Embedding_for_Active_Directory_2019-07-11</guid>
      </item>
      <item>
         <title>Granular access control for using AWS services from Amazon QuickSight</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>In Amazon QuickSight Enterprise edition, you can scope down your security policies
					to allow specific people access to specific AWS resources. You can attach and
					detach IAM policies in the Amazon QuickSight interface, simplifying finer control
					over who can access your AWS data sources. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/controlling-access-to-aws-resources.html?icmpid=docs-quicksight-rssdochistory">Controlling access to AWS resources</a>.</description>
         <pubDate>Fri, 14 Jun 2019 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Granular_access_control_for_using_AWS_services_from_Amazon_QuickSight_2019-06-14</guid>
      </item>
      <item>
         <title>Tabs for dashboards and analyses</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Amazon QuickSight now supports multiple sheets inside of analyses and dashboards.
					You can add multiple tabs to your dashboards, utilize URL actions and on-screen
					controls to simplify navigation, and filter across all of your sheets. For more
					information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/working-with-multiple-sheets.html?icmpid=docs_quicksight_console_rssdochistory">Multiple sheets</a>.</description>
         <pubDate>Tue, 11 Jun 2019 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Tabs_for_dashboards_and_analyses_2019-06-11</guid>
      </item>
      <item>
         <title>New visual types</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now use Amazon QuickSight to chart your data on a customizable gauge and
					donut charts. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/working-with-visual-types.html?icmpid=docs_quicksight_console_rssdochistory">Visual types</a>.</description>
         <pubDate>Tue, 11 Jun 2019 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#New_visual_types_2019-06-11</guid>
      </item>
      <item>
         <title>New functions</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Amazon QuickSight now supports functions Variance and Standard Deviations as both
					aggregation and table calculation. You can create Sample and Population variants
					for both the functions. You can create these calculations through the
					calculations editor in analysis mode. <a href="https://docs.aws.amazon.com/quicksight/latest/user/functions-by-category.html?icmpid=docs_quicksight_console_rssdochistory">Functions by category</a></description>
         <pubDate>Tue, 11 Jun 2019 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#New_functions_2019-06-11</guid>
      </item>
      <item>
         <title>Hide/Show columns in table visualizations</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>In Amazon QuickSight, you can hide or show columns in visualizations that use the
						<em>table</em> visual type. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/supported-formatting-on-visual-types.html?icmpid=docs_quicksight_console_rssdochistory">Customizing a visual</a>. </description>
         <pubDate>Tue, 11 Jun 2019 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Hide/Show_columns_in_table_visualizations_2019-06-11</guid>
      </item>
      <item>
         <title>Conditional string functions on SPICE</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>We added support for <code class="code">ifelse</code> in analyses that use
						SPICE. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/ifelse-function.html?icmpid=docs_quicksight_console_rssdochistory"><code class="code">ifelse</code></a></description>
         <pubDate>Tue, 11 Jun 2019 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Conditional_string_functions_on_SPICE_2019-06-11</guid>
      </item>
      <item>
         <title>Choose period granularity for date differences</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>We added an optional parameter to <code class="code">dateDiff</code> so you can show
					differences between dates in the period you choose (years, months, and so on).
					For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/dateDiff-function.html?icmpid=docs_quicksight_console_rssdochistory"><code class="code">dateDiff</code></a>.</description>
         <pubDate>Tue, 11 Jun 2019 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Choose_period_granularity_for_date_differences_2019-06-11</guid>
      </item>
      <item>
         <title>Duplicate visuals</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>In Amazon QuickSight, you can now duplicate visuals. For more information, see
						<a href="https://docs.aws.amazon.com/quicksight/latest/user/duplicating-a-visual.html?icmpid=docs_quicksight_console_rssdochistory">Duplicating a visual</a>.</description>
         <pubDate>Tue, 21 May 2019 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Duplicate_visuals_2019-05-21</guid>
      </item>
      <item>
         <title>Angled data labels</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>In Amazon QuickSight, data labels that are too long are now angled by default on
					vertical bar, combo, and line charts. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/customizing-visual-data-labels.html?icmpid=docs_quicksight_console_rssdochistory">Customizing data labels</a>.</description>
         <pubDate>Tue, 21 May 2019 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Angled_data_labels_2019-05-21</guid>
      </item>
      <item>
         <title>New languages added</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Amazon QuickSight is now available in 10 languages: English, German, Spanish,
					French, Portuguese, Italian, Japanese, Korean, Simplified Chinese, and
					Traditional Chinese. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/choosing-a-language-in-quicksight.html?icmpid=docs_quicksight_console_rssdochistory">Choosing a language in Amazon QuickSight</a>. </description>
         <pubDate>Mon, 8 Apr 2019 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#New_languages_added_2019-04-08</guid>
      </item>
      <item>
         <title>New aggregation function</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Amazon QuickSight supports aggregating by percentile. This function helps you
					understand the distribution of your data. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/percentile-function.html?icmpid=docs_quicksight_console_rssdochistory"><code class="code">percentile</code></a>. </description>
         <pubDate>Mon, 8 Apr 2019 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#New_aggregation_function_2019-04-08</guid>
      </item>
      <item>
         <title>Customize how many data points to display</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>You can now format your visuals to display a custom number of data points or
					groups before showing the "other" category. This feature is available for bar
					charts, combo charts, line charts, pie charts, heat maps, and tree maps. For
					more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/supported-formatting-on-visual-types.html?icmpid=docs_quicksight_console_rssdochistory">Customizing a visual</a>. </description>
         <pubDate>Mon, 8 Apr 2019 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Customize_how_many_data_points_to_display_2019-04-08</guid>
      </item>
      <item>
         <title>ML-powered forecasting</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>With forecasting powered by machine learning and what-if analyses in
					Amazon QuickSight, nontechnical users can now easily forecast their key business
					metrics. No ML expertise or Microsoft Excel data modeling is required. The
					built-in ML algorithm in Amazon QuickSight is designed to handle complex real-world
					scenarios. Amazon QuickSight uses ML to provide more reliable forecasts than
					traditional means. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/forecasts-and-whatifs.html?icmpid=docs_quicksight_console_rssdochistory">Forecasts and what-ifs</a>. </description>
         <pubDate>Thu, 14 Mar 2019 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#ML-powered_forecasting_2019-03-14</guid>
      </item>
      <item>
         <title>ML-powered anomaly detection</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Amazon QuickSight uses proven Amazon technology to continuously run ML-powered
					anomaly detection on millions of metrics and billions of data points. This
					anomaly detection enables you to get deep insights that are often buried in the
					aggregates, not visible in plain sight, and not scalable with manual analysis.
					With ML-powered anomaly detection, there's no need for manual analysis,
					custom development, or ML domain expertise. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/anomaly-detection.html?icmpid=docs_quicksight_console_rssdochistory">Anomaly detection</a>. </description>
         <pubDate>Thu, 14 Mar 2019 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#ML-powered_anomaly_detection_2019-03-14</guid>
      </item>
      <item>
         <title>Automatic narratives</title>
         <link>https://docs.aws.amazon.com/quick/latest/userguide/doc-history.html</link>
         <description>Automatic narratives provide key insights in everyday language, embedded
					contextually in your dashboard, saving hours on manual analysis. With automatic
					narratives, Amazon QuickSight interprets the charts and tables in your dashboard and
					provides a number of suggested insights in natural language. Depending on the
					shape and form of your data, you might get different suggestions. For example,
					you might see what the day-over-day changes look like, what was the highest
					sales date, or what the growth rate is. Or you might see what the forecast looks
					like for the next seven days. As the author of the dashboard, you can customize
					the computations and business language for your needs. You can use automatic
					narratives to effectively tell the story of your data in plain language. For
					more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/narratives-creating.html?icmpid=docs_quicksight_console_rssdochistory">Narrative insights</a>. </description>
         <pubDate>Thu, 14 Mar 2019 19:00:00 GMT</pubDate>
         <guid isPermaLink="false">https://docs.aws.amazon.com/quick/latest/userguide/#Automatic_narratives_2019-03-14</guid>
      </item>
   </channel>
</rss>
```