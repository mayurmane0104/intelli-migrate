# Creating an Amazon Quick Sight scenario - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/scenarios-create.html](https://docs.aws.amazon.com/quick/latest/userguide/scenarios-create.html)

---

Amazon Quick Pro users can create scenarios from Quick Sight dashboards, or from the
                **Scenarios** section on the Quick Sight home page. Users can
            create as many scenarios as they need. Each user can have up to 3 active scenarios at a
            time. Each Quick Sight account supports up to 10 active scenarios at a time. Use the
            following procedure to create a scenario in Amazon Quick Sight.

###### Create a new scenario

- 
	Open the [Quick console](https://quicksight.aws.amazon.com/).
- 
                Perform one of the following actions: - 
                        Open any dashboard, and look for one of the following: - 
                                Choose **Analyze this dashboard in a Scenario**, if available, at the top of the dashboard.
- 
                                From a visual on the dashboard, open the drop-down menu and choose **Explore scenario**.
- 
                                Choose **Build**, and then choose**Scenario**.
 
- 
                                
- 
                        On the Quick home page, choose **Scenarios**. On the**Scenarios**, choose**New Scenario**.
 
- 
                        
- 
                The new scenario appears. In the text box, describe the problem that you want to solve. This input is the starting point for all of the data pivots and manipulations that will occur in the scenario. The description that you provide can be as broad or as specific as you want, for example "analyze usage trends" or “compute month-over-month and year-over-year changes in usage based on last month's data." 
- 
                Add the data that you want to use in the scenario. You can choose data from Quick Sight dashboards, or you can upload files from your computer. When you choose data from a dashboard, a preview of the selected data is generated for you to review. For more information about previewing and editing data in Quick Sight scenarios, see [Working with data in an Amazon Quick Sight scenario](./scenarios-data.html).The following limits apply to the data that is used in a scenario: - 
                        You can add up to 10 data sources to a scenario. 
- 
                        Up to 20 visuals can be selected from a dashboard at a time. 
- 
                        Uploaded files must be in `.xlsx`or`.csv`format and can't exceed 1 GB.
- 
                        Data sources can have up to 200 columns. 
 If you don't add data to the scenario, Amazon Q automatically searches your Quick Sight dashboards to find data related to your problem statement from the previous step. 
- 
                        
- 
                Choose **Start analysis**.

When you start an analysis in a Quick Sight scenario, Quick Sight prepares your data
            for analysis and returns a new *thread*. The thread contains
            generated prompts that can be used to solve the problem that you described in the
            scenario. A thread is a turn based contextual conversation that consists of user prompts
            and Amazon Q responses that you can use to drill down on a specific scenario. You can use
            threads to write prompts that assume that Amazon Q remembers what was previously discussed in
            the thread. You can choose a prompt to continue the thread, or you can choose the plus
            sign (+) above the thread to start a new thread. The new thread uses a different
            prompt than the first thread that you created. For more information about working with
            threads, see [Working with threads in an Amazon Quick Sight scenario](./scenarios-threads.html).