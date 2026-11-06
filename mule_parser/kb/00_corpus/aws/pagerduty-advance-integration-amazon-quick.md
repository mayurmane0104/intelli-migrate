# PagerDuty Advance integration - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/pagerduty-advance-integration.html](https://docs.aws.amazon.com/quick/latest/userguide/pagerduty-advance-integration.html)

---

Connect Amazon Quick to the PagerDuty Advance MCP and use AI to securely contact PagerDuty Advance. Teams can access incident context, history, and runbooks from the SRE agent, query the Insights agent for proactive ways to improve, or alter on-call coverage with Shift agent from their AI-enabled platform of choice.

## What you can do

        
        The PagerDuty Advance integration enables you to:

- 
                Access incident context, history, and runbooks for active incident response 
- 
                Perform root cause analysis and technical troubleshooting 
- 
                Query on-call schedules and manage shift coverage 
- 
                Analyze historical trends and performance metrics (MTTR, MTTA) 
- 
                Generate insights for service reliability and team performance 
- 
                Collaborate with PagerDuty Advance agents from your AI-enabled platform of choice 

## Available tools

        
        The MCP server for PagerDuty Advance typically provides these tools:

- 
                `analytics_agent_tool`- Runs an analytics agent for historical reporting and trend analysis, including performance metrics (MTTR, MTTA), team benchmarking, service reliability statistics, and executive KPI tracking.
- 
                `schedules_agent_tool`- Runs a schedules agent for on-call and scheduling information, including shift assignments, schedule configurations, escalation policies, user availability conflicts, and coverage management.
- 
                `sre_agent_tool`- Runs an SRE agent for incident response and technical troubleshooting, including active incident triage, root cause analysis, diagnostics, alert explanations, change event analysis, and runbook generation.

###### Note

The specific tools and capabilities available through this MCP server may change over time. For the most current information about supported tools, features, and implementation details, check the official PagerDuty documentation and MCP server repository.

## Setting up PagerDuty Advance integration

        
        PagerDuty Advance integration uses MCP server connectivity to provide agent capabilities. For detailed setup instructions, see [Model Context Protocol (MCP) integration](./mcp-integration.html).

You'll need:

- 
                PagerDuty account with appropriate permissions 
- 
                PagerDuty API credentials (Client ID and Client Secret) 
- 
                Amazon Quick with MCP integration enabled 

## Compatibility

        
        PagerDuty Advance integration supports:

- 
                **Chat Agents:**Yes
- 
                **Flows:**Yes
- 
                **Knowledge Base:**No