# Collaboration with shared spaces - Amazon SageMaker AI

**Source:** [https://docs.aws.amazon.com/sagemaker/latest/dg/domain-space.html](https://docs.aws.amazon.com/sagemaker/latest/dg/domain-space.html)

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

An Amazon SageMaker Studio Classic shared space consists of a shared JupyterServer application and a shared directory. A JupyterLab shared space consists of a shared JupyterLab application and a shared directory within Amazon SageMaker Studio. All user profiles in a domain have access to all shared spaces in the domain. Amazon SageMaker AI automatically scopes resources in a shared space within the context of the Amazon SageMaker Studio Classic application that you launch in that shared space. Resources in a shared space include notebooks, files, experiments, and models. Use shared spaces to collaborate with other users in real-time using features like automatic tagging, real time co-editing of notebooks, and customization.

Shared spaces are available in:

Amazon SageMaker Studio Classic

JupyterLab

A Studio Classic shared space only supports Studio Classic and KernelGateway applications. A shared space only
    supports the use of a JupyterLab 3 image Amazon Resource Name (ARN). For more information, see
      [JupyterLab Versioning in Amazon SageMaker Studio Classic](./studio-jl.html).

Amazon SageMaker AI automatically tags all SageMaker AI resources that you create within the scope of a shared space. You can use these tags to monitor costs and plan budgets using tools, such as AWS Budgets.

A shared space uses the same VPC settings as the domain that it's created in.

Shared spaces do not support the use of Amazon SageMaker Data Wrangler or Amazon EMR cross-account clusters.

    **Automatic tagging**
  

All resources created in a shared space are automatically tagged with a domain ARN tag and shared space ARN tag. The domain ARN tag is based on the domain ID, while the shared space ARN tag is based on the shared space name.

 You can use these tags to monitor AWS CloudTrail usage. For more information,
      see [Log
      Amazon SageMaker API Calls with AWS CloudTrail](https://docs.aws.amazon.com//sagemaker/latest/dg/logging-using-cloudtrail.html). 

 You can also use these tags to monitor costs with AWS Billing and Cost Management. For
    more information, see [Using AWS cost allocation
      tags](https://docs.aws.amazon.com//awsaccountbilling/latest/aboutv2/cost-alloc-tags.html). 

    **Real time co-editing of notebooks**
  

A key benefit of a shared space is that it facilitates collaboration between members of the shared space in real time. Users collaborating in a workspace get access to a shared Studio Classic application where they can access, read, and edit their notebooks in real time. Real time collaboration is only supported for JupyterServer applications within a shared space.

Users with access to a shared space can simultaneously open, view, edit, and execute Jupyter notebooks in the shared Studio Classic or JupyterLab application in that space.

The notebook indicates each co-editing user with a different cursor that shows the user profile name. While multiple users can view the same notebook, co-editing is best suited for small groups of two to five users.

To track changes being made by multiple users, we strongly recommended using Studio Classic's built-in Git-based version control.

    **JupyterServer 2**
  

To use shared spaces in Studio Classic, Jupyter Server version 2 is required. Certain JupyterLab extensions and packages can forcefully downgrade Jupyter Server to version 1. This prevents the use of shared space. Run the following from the command prompt to change the version number and continue using shared spaces.

```
conda activate studio
pip install jupyter-server==2.0.0rc3
```
    **Customize a shared space**
  

To attach a lifecycle configuration or custom image to a shared space, you must use the
    AWS CLI. For more information about creating and attaching lifecycle configurations, see [Create and Associate a Lifecycle Configuration with Amazon SageMaker Studio Classic](./studio-lcc-create.html). For more information about
    creating and attaching custom images, see [Custom Images in Amazon SageMaker Studio Classic](./studio-byoi.html).

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

EMR Studio Workspaces enable notebook creation, S3 storage, Git repos, EC2 security groups, auto-termination cluster cleanup.

Organize SQL queries, add Markdown cells, share, export .ipynb, import .sql files, save versions.

Configure channel outputs sharing video encodes across multiple outputs or cloning unique instances.

Fully managed ML service enables building, training, deploying models; renamed SageMaker AI December 2024.

Administrators configure unified AWS data, AI, ML analytics platform managing users, access, governance, generative AI development.

SageMaker built-in algorithms support tabular, text, image, time-series supervised unsupervised ML tasks.