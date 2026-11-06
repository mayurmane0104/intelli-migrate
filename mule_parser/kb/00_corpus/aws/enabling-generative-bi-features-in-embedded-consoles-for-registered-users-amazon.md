# Enabling Generative BI features in embedded consoles for registered users - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/embedding-consoles-genbi.html](https://docs.aws.amazon.com/quick/latest/userguide/embedding-consoles-genbi.html)

---

| Applies
                    to:Enterprise Edition | 

| Intended audience: Amazon Quick developers | 

You can enable the following Generative BI features in your embedded console:

- 
            Executive summaries: When enabled, registered Author Pro and Reader Pro users can generate executive summaries that provide a summary of all insights that Amazon Quick Sight has generated for the dashboard to easily discover key insights. 
- 
            Authoring: When enabled, Author Pro users can use Generative BI to build calculated fields and build and refine visuals. 
- 
            Q&A: When enabled, Author Pro and Reader Pro users can use the AI-powered Q&A to both suggest and answer questions related their data. 
- 
            Data stories: When enabled, Author Pro and Reader Pro users can provide details to quickly generate a first draft of their data story. 

###### To enable Generative BI features in embedded consoles for registered users

- 
            Follow the steps in [Embedding the full functionality of the Amazon Quick Sight console for registered users](https://docs.aws.amazon.com/quicksight/latest/user/embedded-analytics-full-console-for-authenticated-users.html)to embed a console with the following changes:- 
                    When generating the URL in Step 2, set `Enabled: true`in the`FeatureConfigurations`parameter for each of the features you want to enable in the[GenerateEmbedUrlForRegisteredUser](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_GenerateEmbedUrlForRegisteredUser.html)or[GenerateEmbedUrlForRegisteredUserWithIdentity](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_GenerateEmbedUrlForRegisteredUserWithIdentity.html)APIs, as shown in the following example. If no configuration is provided, the features are disabled by default.`ExperienceConfiguration: { QuickSightConsole: { InitialPath: "``initial_path`", AmazonQInQuickSight: { FeatureConfigurations: {`COMMENT: Enable executive summaries`ExecutiveSummary: { Enabled: true },`COMMENT: Enable Generative BI authoring`GenerativeAuthoring: { Enabled: true },`COMMENT: Enable Q&A`DataQnA: { Enabled: true },`COMMENT: Enable data stories`DataStories: { Enabled: true } } } } } }
- 
                    When embedding the console URL with the Amazon Quick Sight Embedding SDK in Step 3, set the values in the following example as desired. If no configuration is provided, the features are disabled by default. ###### NoteThere is no SDK option for enabling data stories. If data stories are enabled with the API as shown in the previous step, they will be available to registered users. `const contentOptions = { toolbarOptions: { executiveSummary: true, // Enable executive summaries buildVisual: true, // Enable Generative BI authoring dataQnA: true // Enable Q&A } };`
 
-