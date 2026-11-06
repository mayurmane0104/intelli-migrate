# Bounded and unbounded agents - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/int-actions-bounded-unbounded.html](https://docs.aws.amazon.com/quick/latest/userguide/int-actions-bounded-unbounded.html)

---

Amazon Quick offers two types of agents that provide different levels of access and functionality: bounded and unbounded agents. Understanding the differences between these agent types helps you implement the right solution for your use case.

## Bounded agents

        Bounded agents operate within defined parameters, specifically linked to one or more spaces within Amazon Quick. These agents can only access and perform actions on resources that are explicitly connected to their assigned spaces. For example, a bounded agent configured for the HR space can only access HR-related documents, datasets, and execute HR-related actions.

Use bounded agents for:

- 
                Department-specific workflows (HR, Finance, IT). 
- 
                Project team collaborations. 
- 
                Sensitive data handling. 
- 
                Compliance-focused operations. 

The bounded nature provides enhanced security by ensuring the agent can't access resources outside its designated spaces. This makes it ideal for scenarios where data isolation is important.

## Unbounded agents

        Unbounded agents have broader access capabilities and can work across all configured actions and resources within the Amazon Quick environment. These agents aren't restricted to specific spaces and can access any properly configured action connector available in the system.

Use unbounded agents for:

- 
                Organization-wide assistance. 
- 
                Cross-departmental workflows. 
- 
                General-purpose actions. 
- 
                Scenarios requiring access to multiple systems.