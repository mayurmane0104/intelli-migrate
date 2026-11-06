# Mission control - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/mission-control-desktop.html](https://docs.aws.amazon.com/quick/latest/userguide/mission-control-desktop.html)

---

Mission control is a centralized command center in the Amazon Quick desktop application that gives you full visibility and management capabilities over all your agents in one place. You can monitor agent activity, review outputs, manage schedules, and track performance metrics – eliminating the need to check on agents individually.

## Why use mission control

        As you scale your use of agents – running recurring checks, background tasks, and automated workflows – keeping track of everything becomes complex. Mission control provides the following benefits.

- 
                **Centralized visibility**– View all agent activity without switching between conversations or agents.
- 
                **Faster unblocking**– Agents that need your input are clearly surfaced so you can respond quickly.
- 
                **Operational awareness**– KPIs and run history give you confidence that your agents are working correctly.
- 
                **Efficiency at scale**– Whether you have 2 agents or 20, mission control keeps you in control.

## Capabilities

        Mission control provides the following capabilities for managing your agents.

| Capability | Description | 
|---|---|
| Monitor all agent activity | View a unified list of what every agent has done across all runs. | 
| Filter by agent name | Drill into a specific agent's history and access its outputs. | 
| Unblock agents | Filter on agents that need your input and provide it directly. | 
| View running agents | See which agents are currently active and monitor their progress. | 
| Manage schedules | View and edit schedules for all agents in one place. | 
| Track KPIs | Understand error rates, active agents, completed tasks, and total runs. | 

### Schedules

Mission control lets you view and manage automated agents that run on a
                recurring schedule. Each schedule has four configuration tabs: Schedule,
                Capabilities, and Task objectives & model. For more information about
                scheduled agents, see [Skills and agents](./skills-and-agents-desktop.html).

###### Important

Scheduled agents run locally on your computer. Your computer must be turned on and the Amazon Quick desktop application must be running for scheduled agents to execute at their configured times.

## Working with agent runs

        Mission control organizes agent activity into runs. Depending on the state of a run, you can take different actions.

###### Completed runs

For a completed run, you can perform the following actions.

- 
                View what the agent did and access artifacts it produced 
- 
                Get an in-depth summary of the run 
- 
                Track events of all sub-tasks 
- 
                Chat to follow up on results 

###### Ongoing runs

For an ongoing run, you can perform the following actions.

- 
                View live events as the agent works 
- 
                Pause the run 
- 
                Cancel the run 

###### Runs requiring input

For runs that are waiting on your input, you can perform the following actions.

- 
                Approve or deny authorization requests for third-party applications 
- 
                Chat with the agent to provide clarifications 

## Accessing mission control

        You can access mission control from anywhere in the Quick desktop application.

- 
                Choose the **mission control**icon in the top-right navigation bar.
- 
                A quick-access popover appears showing agent runs, pending inputs, and schedule management. 
- 
                To view the full mission control landing page, click on the mission control header in the popover menu. 

You can work from the lightweight popover for quick actions such as unblocking an agent, or open the full page for a comprehensive view of all agent activity.

## KPIs and metrics

        Mission control displays key performance indicators to help you understand agent health and productivity at a glance. The following metrics are available.

| Metric | Description | 
|---|---|
| Errored runs | Number of agent runs that ended with an error. | 
| Active agents | Count of agents that are currently running. | 
| Tasks completed | Number of agent tasks completed in the past week. | 
| Total runs | Total number of runs across all agents. |