# Common Development Strategies | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/mule-runtime/latest/common-dev-strategies](https://docs.mulesoft.com/mule-runtime/latest/common-dev-strategies)

---

# Common Development Strategies

To help you develop your Mule applications, consider common development strategies and practices such as creating reproducible builds, modularizing your configuration files, and implementing reliability patterns, transaction management, continuous integration, orchestration in Mule, and enterprise integration patterns.

## Create Reproducible Builds

Create reproducible builds to facilitate application maintenance, by running a particular version of your Mule projects at any time. You can achieve this goal by:

- 
Using source control for your Mule projects 
- 
Managing dependencies by using Apache Maven and an in-house manager. 

For details, see the [Reproducible Builds](reproducible-builds) documentation.

## Implement Reliability Patterns

Implement a reliability pattern in your application design so your application is capable of reliable messaging, even if receives messages from a nontransactional connector. A reliability pattern design couples a reliable acquisition flow with an application logic flow.

For details, see the [Reliability Patterns](reliability-patterns) documentation.

## Implement Transaction Management

Implement transaction operations in a Mule app for which the result cannot remain indeterminate. When a series of steps in a flow must succeed or fail as one unit, Mule uses a transaction to demarcate that unit.

For details on the different transaction types, transaction actions operations and how you can configure a transaction in a Mule event source or Try Scope in the [Transaction Management](transaction-management) documentation.

Additionally, you can implement [Single Source Transactions](single-resource-transaction), [XA Transactions](xa-transactions) and [Using Bitronix to manage transactions](using-bitronix-to-manage-transactions).

## Modularize Configurations Files

Modularize configuration files by splitting monolithic configurations into several files, and leverage Mule’s capacity to load multiple configuration files at application start-up time. Although it might seem convenient to keep your Mule configurations in one file, a very large XML file quickly becomes unmanageable. Modularizing Mule configurations is an opportunity for splitting work across teams, whether these teams work on the same project or on different projects with an accent put on reuse. There are two options to load multiple configuration files:

- 
Side-by-side: Provide a list of independent configuration files to load. 
- 
Imported: Have one configuration file import several others, which in turn, can import other files. 

For details see the [Modularize Configurations Files](modularizing-your-configuration-files-for-team-development) documentation.

## Implement Continuous Integration

Implement continuous integration (CI) for your projects by using Maven as your build tool. Create a build that gets triggered on every project change, and run all of its unit and functional tests automatically. By doing so you can:

- 
Get early notification of issues in the software development lifecycle. 
- 
Ensure code gets fully tested before release. 
- 
Confirm that successfully tested branches ensure better success when merging to the main branch. 

For details, see the [Continuous Integration](continuous-integration) documentation.

## Implement Orchestration in Mule

Implement orchestration in Mule to facilitate the process of moving data through a Mule implementation based on flows. The orchestration implements business-level processes combining business-specific services across applications and information systems. Flows uses cases that orchestrate are:

- 
Simple integration. 
- 
Scheduling data processing. 
- 
Connecting cloud and on-premise applications. 
- 
Event processing, where multiple services must be composed and must operate simultaneously. 

For details, see the [Orchestration Using Mule](understanding-orchestration-using-mule) documentation.

## Implement Enterprise Integration Patterns

Implement enterprise integration patterns as solutions for designing, building messaging and integration systems, as well as to provide a common language for teams to use when architecting solutions.

For details, see the [Enterprise Integration Patterns Using Mule](understanding-enterprise-integration-patterns-using-mule) documentation.

## Configure Business Events Tracking

Mule applications can collect business event information about flows and message processors that handle your business transactions. You can configure default event tracking for supported components or entire flows, and you can also configure custom event tracking using the Custom Business Events component.

For details, see the [Business Events](business-events) documentation.

## Share Applications

Share Mule applications for splitting work across teams, whether these teams work on the same project or on different projects that they intent for reuse.

For details, see the [Share Applications](sharing-applications) documentation.

## Best Practices to Build Mule Applications

As you build your applications, consider the following best practices for creating a clean, organized, and sustainable project. These practices include guidelines on using Anypoint Studio, avoiding certain app-building issues, and specific settings for using Mule runtime engine (Mule) components and connectors.

For details, see the [Best Practices to Build Mule Apps](build-app-practices) documentation.