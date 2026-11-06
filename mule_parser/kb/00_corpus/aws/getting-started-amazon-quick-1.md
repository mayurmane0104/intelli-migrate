# Getting started - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/getting-started-quick-automate.html](https://docs.aws.amazon.com/quick/latest/userguide/getting-started-quick-automate.html)

---

Amazon Quick Automate is a browser-based solution that requires no installation, has minimal IT dependencies, and is always up to date. Amazon Quick Automate is designed for **technical teams and power users** who build, test, and maintain intelligent automations across enterprise systems. These users typically have a strong understanding of business processes, system integrations, but may not necessarily be software developers. Amazon Quick Automate equips advanced users and technical teams with the flexibility, control, and depth needed to design and scale enterprise-grade automations. To get started with Amazon Quick Automate, simply access it through your Amazon Quick and begin exploring the automation capabilities that best fit your needs.

## Key capabilities

        - Multi-agent architecture - Planning Agent designs automations from natural language inputs 
- UI Agent handles interface interactions 
- Specialized agents for process-specific tasks 
- Integration with 
 
- Enterprise controls and governance - Granular access control management 
- Comprehensive activity logging 
- Built-in version control 
- Governance features for compliance 
 
- Human-in-the-loop capabilities 
- Case management 
- Exception handling support 
- Real-time monitoring 
- Built in scalability 

## Setup tasks

        Complete these setup tasks to prepare your Amazon Quick Automate environment for creating automations.

### Sign up

Before you can use Amazon Quick Automate, you need to sign up for and create your account. The sign-up process establishes your initial workspace and provides access to Amazon Quick Automate.

### Set up automation groups

Automation groups create logical groupings for automations, allowing organizations to manage permissions and resources efficiently across different departments or projects. These groups provide a way to organize your automations and setup permissions based on business units, functional areas, or project teams. By organizing automations into groups, you can apply consistent access controls, resource restrictions, and governance policies. This organizational structure supports scalable automation management as your organization's automation needs grow and evolve. After signing up, configure automation groups and permissions to organize your automations and control access across your organization. This step ensures that different departments and teams can work with automations appropriate to their roles and responsibilities.

Setting up proper automation groups and permissions from the beginning helps maintain security and compliance as your automation environment grows. You'll establish the organizational structure that supports efficient workflow management across multiple departments or projects.

### Setup user roles

Amazon Quick Automate provides granular role based access: Viewer, Contributor, and Owner. Viewers can submit new project ideas, interact with human in the loop tasks, and access monitoring dashboards. Contributors can build, test, and deploy automations. Owners can control automation access to systems through integrations and secure credentials as well as user access.

### Configure integrations

- After setting up AWS service integrations, you can begin using them in Quick Automate. See - [Action connectors](./action-integrations.html)for setup details.
- First, add the integration to an Automation Group. This allows you to control access for which automations can use this integration. To add an integration to your Automation Group: - Go to the - **Projects**page
- Click - **Manage groups**and select the group you want to add an integration to
- In the - **Assets**sections, click- **Add**, and then- **Actions**
- Select the Integration you created earlier and click - **Add**to link it to your Automation Group
 
- Now when users create projects in that Automation Group, they will find the actions associated with this Integration and be able to select this Integration for authentication 

### Set up Virtual Private Cloud (VPC) connections

Amazon Quick Automate can access publicly hosted internet endpoints by default. For more complex setups, including accessing privately hosted websites, Amazon Quick Automate automation jobs can optionally be associated with your VPC. For more information, see [Setting up a VPC to use with Amazon Quick](./vpc-setup-for-quicksight.html).

With this configuration in place, all outbound network traffic from the managed browser is routed through an ENI in your configured VPC. From there, you can send that traffic to privately hosted resources or use it to obtain a persistent IP for IP allow listing.

The VPC-connected Amazon Quick Automate setup provides:

- **Direct access**to privately hosted resources in the connected VPC
- **Extended access**to other privately hosted resources in peered, PrivateLinked, etc. VPCs
- **Internet access**through your managed Internet Gateway

#### Setup instructions

**Step 1:** Choose your VPC

Select an existing VPC or create a new one that includes private and public subnets in one or more Availability Zones, NAT and Internet Gateways.

###### Note

If creating a new VPC, the default selections in AWS VPC creation wizards are sufficient.

**Step 2:** Setup connectivity to target resources

Bot traffic will egress through an ENI in your connected VPC. Choose the appropriate connectivity method:

For resources in the same VPC:

- No additional setup required 

For resources in different VPCs, use one of these AWS constructs:

- AWS VPC Endpoint Services (PrivateLink) - Exposing individual service endpoints from one VPC to another 
- AWS Transit Gateway - Centralized management of a cluster of peered networks 
- AWS VPC Peering - Direct connection between a pair of VPCs 

**Step 3:** Create Quick VPC Connection

Use Quick Admin tools to create a VPC Connection. This step creates two ENIs in the private subnet within your chosen VPC.

**Step 4:** Associate VPC Connection with Automation Group

Once the VPC Connection is created, associate it with your automation group from the VPC connection section in the automation group page. After this association is configured, all subsequent automations run within the specified group will use the VPC Connection for network access.

### Create project

This section walks you through the process of creating a new automation project in Amazon Quick Automate.

###### To create a new project

- Click the - **Create Project**button to begin.
- Fill in the project details in the Provide project details section: - **Name:**Enter a descriptive name for your automation project.
- **Group:**Select the appropriate group for your automation.
- **Description**(optional): Provide additional context about the project's purpose.
- **Upload Documents**(optional): Attach existing documentation to jumpstart your automation.
 
- Click - **Next: Business case**to proceed to the business case section.

#### Defining the business case (Section is optional)

This section is optional but recommended for tracking ROI and prioritization. Complete the following fields:

- **Hours saved per case:**Estimate time savings per instance.
- **Cases per year:**Enter the expected annual volume.
- **Hours saved per year:**This may calculate automatically based on previous entries.
- **Project priority:**Set the relative importance of this automation.
- **Target launch date:**Define the target implementation date.

Click **Create** to finalize and generate your new automation project.

###### Note

Required fields are marked accordingly in the interface. Optional fields provide additional context but can be completed later if needed.

After creating your project, you can access a summary page with Overview, launch goals and document section will open for review. This comprehensive layout allows you to quickly grasp the essential information about your project or resource. You will have Summary (default selected), Versions and Deployments tabs.

In Summary, the Overview section provides a high-level description and launch Goals. The Documents section contains relevant document uploaded. On the right-hand side of the page, you'll notice a Status panel. This panel offers real-time updates on the current state of your project. It may include information such as deployment status, health checks, or any ongoing processes.