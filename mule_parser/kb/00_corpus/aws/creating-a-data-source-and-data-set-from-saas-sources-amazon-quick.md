# Creating a data source and data set from SaaS sources - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/connecting-to-saas-data-sources.html](https://docs.aws.amazon.com/quick/latest/userguide/connecting-to-saas-data-sources.html)

---

To analyze and report on data from software as a service (SaaS) applications, you can use SaaS connectors to access your data directly from Quick Sight. The SaaS connectors simplify accessing third-party application sources using OAuth, without any need to export the data to an intermediate data store.

You can use either a cloud-based or server-based instance of a SaaS application. To connect to an SaaS application that is running on your corporate network, make sure that Quick Sight can access the application's Domain Name System (DNS) name over the network. If Quick Sight can't access the SaaS application, it generates an unknown host error.

Here are examples of some ways that you can use SaaS data:

- 
                Engineering teams who use Jira to track issues and bugs can report on developer efficiency and bug burndown. 
- 
                Marketing organizations can integrate Quick Sight with Adobe Analytics to build consolidated dashboards to visualize their online and web marketing data. 

Use the following procedure to create a data source and dataset by connecting to sources available through Software as a Service (SaaS). In this procedure, we use a connection to GitHub as an example. Other SaaS data sources follow the same process, although the screens—especially the SaaS screens—might look different.

###### To create a data source and dataset by connecting to sources through SaaS

- 
                On the Quick start page, choose **Data**.
- 
                On the **Data**page, choose**Create**then choose**New dataset**.
- 
                Choose the icon that represents the SaaS source that you want to use. For example, you might choose Adobe Analytics or GitHub. For sources using OAuth, the connector takes you to the SaaS site to authorize the connection before you can create the data source. 
- 
                Choose a name for the data source, and enter that. If there are more screen prompts, enter the appropriate information. Then choose **Create data source**.
- 
                If you are prompted to do so, enter your credentials on the SaaS login page. 
- 
                When prompted, authorize the connection between your SaaS data source and Quick Sight. The following example shows the authorization for Quick Sight to access the GitHub account for the Quick Sight documentation. ###### NoteQuick Sight documentation is now available on GitHub. If you want to make changes to this user guide, you can use GitHub to edit it directly. (Optional) If your SaaS account is part of an organizational account, you might be asked to request organization access as part of authorizing Quick Sight. If you want to do this, follow the prompts on your SaaS screen, then choose to authorize Quick Sight. 
- 
                After authorization is complete, choose a table or object to connect to. Then choose **Select**.
- 
                On the **Finish data set creation**screen, choose one of these options:- 
                        To save the data source and dataset, choose **Edit/Preview data**. Then choose**Save**from the top menu bar.
- 
                        To create a dataset and an analysis using the data as-is, choose **Visualize**. This option automatically saves the data source and the dataset.You can also choose **Edit/Preview data**to prepare the data before creating an analysis. This opens the data preparation screen. For more information about data preparation, see[Preparing dataset examples](./preparing-data-sets.html).
 
- 
                        

The following constraints apply:

- 
                The SaaS source must support REST API operations for Quick Sight to connect to it. 
- 
                If you are connecting to Jira, the URL must be public address. 
- 
                If you don't have enough [SPICE](./spice.html)capacity, choose**Edit/Preview data**. In the data preparation screen, you can remove fields from the dataset to decrease its size or apply a filter that reduces the number of rows returned. For more information about data preparation, see[Preparing dataset examples](./preparing-data-sets.html).