# Track and organize work with issues in CodeCatalyst - Amazon CodeCatalyst

**Source:** [https://docs.aws.amazon.com/codecatalyst/latest/userguide/issues](https://docs.aws.amazon.com/codecatalyst/latest/userguide/issues)

---

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](./migration.html).

In CodeCatalyst, you can monitor features, bugs, and any other work involved in your
    project. Each piece of work is kept in a distinct record called an *issue*. 
    You can break up an issue into smaller objectives by adding a checklist of tasks to it. 
    Each issue can have a description, assignee, status, and other properties, which you can search
    for, group, and filter on.  You can view your issues using the default views, or you can create 
    your own views with custom filtering, sorting, or grouping. For more information about concepts related 
    to issues, see [Issues concepts](./issues-concepts.html). To learn how to create your first issue, see [Creating an issue in CodeCatalyst](./issues-create-issue.html). 

Here is one possible workflow for a team using issues:

Jorge Souza is a developer working in a project. He and his fellow project members
    Li Juan, Mateo Jackson, and Wang Xiulan collaborate to determine what work
    needs to be done. Every day, he and his fellow developers hold a sync-up meeting, led by
    Wang Xiulan. They pull up the board by navigating to one of their teams views of the board. By creating views, 
    users and teams can save filters, groupings, and sorting of issues to easily view issues that meet their 
    specified criteria. Their view contains issues grouped by **Assignee** and sorted by **Priority** to show the 
    most important issues and status of the issues for each developer. As Jorge is assigned tasks to complete, he plans his work by creating an issue
    for each task. When creating issues, Jorge can choose the appropriate **Status**, 
    **Priority**, and work **Estimation** effort. For larger issues, Jorge 
    adds tasks to the issue, to break the work into smaller objectives. Jorge creates his issues with 
    a draft status, such as **backlog**, as he doesn't plan to start on them immediately. 
    Issues in a draft status appear on the **Drafts** view where they are to be planned 
    and prioritized. Once Jorge is ready to start the work, he moves the corresponding issue to the board by updating its 
    status to a status in another category (**Not Started**, **Started**, or
    **Completed**). As each task is being worked on, the team can filter by the
    title, status, assignee, label, priority, and estimation to find a specific issue or similar
    issues that match the specified parameter. Using the board, Jorge and his team can see the number of tasks completed for 
    each issue, and track the day-to-day progress by dragging each issue from one status
    to the next until the task is complete. As the project progresses, finished issues accumulate in
    the **Completed** status. Wang Xiulan decides to remove them from view by
    archiving them using the quick archive button, so that the developers can focus on the issues that are related to current and
    upcoming work.

When planning their work, the developers working on the project choose **Sort
      by** and **Group by** to find the issues they want to move from the backlog to the board. They might
    choose to add issues to the board based on the highest priority customer requests, so they group the board by a 
    **Customer request** label and sort by **Priority**. They might also sort by
    estimate to ensure that they're taking on a volume of work they can achieve. The project
    manager, Saanvi Sarkar, regularly reviews and grooms the backlog to help ensure that the
    priority accurately reflects the importance of each issue to the success of the project.