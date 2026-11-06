# RStudio on Amazon SageMaker AI - Amazon SageMaker AI

**Source:** [https://docs.aws.amazon.com/sagemaker/latest/dg/rstudio.html](https://docs.aws.amazon.com/sagemaker/latest/dg/rstudio.html)

---

[Disaggregated Prefill and Decode for HyperPod inference](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-model-deployment-dpd.html)

*13 June 2026*

We use essential cookies and similar tools that are necessary to provide our site and services. We use performance cookies to collect anonymous statistics, so we can understand how customers use our site and make improvements. Essential cookies cannot be deactivated, but you can choose “Customize” or “Decline” to decline performance cookies. 

 If you agree, AWS and approved third parties will also use cookies to provide useful site features, remember your preferences, and display relevant content, including relevant advertising. To accept or decline all non-essential cookies, choose “Accept” or “Decline.” To make more detailed choices, choose “Customize.”

Essential cookies are necessary to provide our site and services and cannot be deactivated. They are usually set in response to your actions on the site, such as setting your privacy preferences, signing in, or filling in forms.

Performance cookies provide anonymous statistics about how customers navigate our site so we can improve site experience and performance. Approved third parties may perform analytics on our behalf, but they cannot use the data for their own purposes.

Functional cookies help us provide useful site features, remember your preferences, and display relevant content. Approved third parties may set these cookies to provide certain site features. If you do not allow these cookies, then some or all of these services may not function properly.

Advertising cookies may be set through our site by us or our advertising partners and help us deliver relevant marketing content. If you do not allow these cookies, you will experience less relevant advertising.

Blocking some types of cookies may impact your experience of our sites. You may review and change your choices at any time by selecting Cookie preferences in the footer of this site. We and selected third-parties use cookies or similar technologies as specified in the [AWS Cookie Notice](https://aws.amazon.com/legal/cookies/).

We will only store essential cookies at this time, because we were unable to save your cookie preferences.

If you want to change your cookie preferences, try again later using the link in the AWS console footer, or contact support if the problem persists.

RStudio is an integrated development environment for R, with a console, syntax-highlighting
    editor that supports direct code execution, and tools for plotting, history, debugging and
    workspace management. Amazon SageMaker AI supports RStudio as a fully-managed integrated development
    environment (IDE) integrated with Amazon SageMaker AI domain through Posit Workbench. RStudio allows
    customers to create data science insights using an R environment. With RStudio integration, you
    can launch an RStudio environment in the domain to run your RStudio workflows on SageMaker AI
    resources. For more information about Posit Workbench, see the [Posit website](https://posit.co/products/enterprise/workbench/). This page gives
    information about important RStudio concepts.

SageMaker AI integrates RStudio through the creation of a RStudioServerPro app.

The following are supported by RStudio on SageMaker AI.

R developers use the RStudio IDE interface with popular developer tools from the R ecosystem. Users can launch new RStudio sessions, write R code, install dependencies from RStudio Package Manager, and publish Shiny apps using RStudio Connect.

R developers can quickly scale underlying compute resources to run large scale data processing and statistical analysis.

Platform administrators can set up user identities, authorization, networking, storage, and security for their data science teams through AWS IAM Identity Center and AWS Identity and Access Management integration. This includes connection to private Amazon Virtual Private Cloud (Amazon VPC) resources and internet-free mode with AWS PrivateLink.

Integration with AWS License Manager.

 For information on the onboarding steps to create a domain with RStudio enabled,
        see [Amazon SageMaker AI domain overview](./gs-studio-onboard.html).

The following table gives information about the AWS Regions that RStudio on SageMaker AI is supported in.

| Region name | Region | 
|---|---|
| US East (Ohio) | us-east-2 | 
| US East (N. Virginia) | us-east-1 | 
| US West (N. California) | us-west-1 | 
| US West (Oregon) | us-west-2 | 
| Asia Pacific (Mumbai) | ap-south-1 | 
| Asia Pacific (Seoul) | ap-northeast-2 | 
| Asia Pacific (Singapore) | ap-southeast-1 | 
| Asia Pacific (Sydney) | ap-southeast-2 | 
| Asia Pacific (Tokyo) | ap-northeast-1 | 
| Canada (Central) | ca-central-1 | 
| Europe (Frankfurt) | eu-central-1 | 
| Europe (Ireland) | eu-west-1 | 
| Europe (London) | eu-west-2 | 
| Europe (Paris) | eu-west-3 | 
| Europe (Stockholm) | eu-north-1 | 
| South America (São Paulo) | sa-east-1 | 

*RStudioServerPro*: The RStudioServerPro app is a multiuser app
          that is a shared resource among all user profiles in the domain. Once an RStudio app
          is created in a domain, the admin can give permissions to users in the domain.  

*RStudio user*: RStudio users are users within the domain that
          are authorized to use the RStudio license.

*RStudio admin*: An RStudio on Amazon SageMaker AI admin can access the
          RStudio administrative dashboard. RStudio on Amazon SageMaker AI admins differ from "stock" Posit
          Workbench admins because they do not have root access to the instance running the
          RStudioServerPro app and can't modify the RStudio configuration file.

*RStudio Server*: The RStudio Server instance is responsible for
          serving the RStudio UI to all authorized Users. This instance is launched on an Amazon SageMaker AI
          instance.

*RSession*: An RSession is a browser-based interface to the RStudio
          IDE running on an Amazon SageMaker AI instance. Users can create and interact with their RStudio projects through
          the RSession.

*RSessionGateway*: The RSessionGateway app is used to support an
          RSession. 

*RStudio administrative dashboard*: This dashboard gives
          information on the RStudio users in the Amazon SageMaker AI domain and their sessions. This dashboard
          can only be accessed by users that have RStudio admin authorization.

RStudio on Amazon SageMaker AI has some significant differences from [Posit Workbench](https://posit.co/products/enterprise/workbench/).

When using RStudio on SageMaker AI, users don’t have access to the RStudio configuration files. Amazon SageMaker AI manages the configuration file and sets defaults. You can modify the RStudio Connect and RStudio Package Manager URLs when creating your RStudio-enabled Amazon SageMaker AI domain.

Project sharing, realtime collaboration, and Job Launcher are not currently supported when using RStudio on Amazon SageMaker AI.

When using RStudio on SageMaker AI, the RStudio IDE runs on Amazon SageMaker AI instances for on-demand containerized compute resources.

RStudio on SageMaker AI only supports the RStudio IDE and does not support other IDEs supported by a Posit Workbench installation.

RStudio on SageMaker AI only supports the RStudio version specified in [RStudio Versioning](./rstudio-version.html).

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

Key limitations: workgroup upgrades blocked, cross-engine views incompatible, SageMaker AI integration replaces console notebooks.

Fully managed ML service enables building, training, deploying models; renamed SageMaker AI December 2024.

Administrators configure unified AWS data, AI, ML analytics platform managing users, access, governance, generative AI development.

SageMaker built-in algorithms support tabular, text, image, time-series supervised unsupervised ML tasks.