# Anypoint Code Builder Overview | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/anypoint-code-builder](https://docs.mulesoft.com/anypoint-code-builder)

---

# Anypoint Code Builder Overview

Use the Anypoint Code Builder integrated development environment (IDE) for your API designs, implementations, and integration development. Work locally with Anypoint Code Builder for Desktop on Microsoft Visual Studio Code (VS Code) or from your browser with Anypoint Code Builder through Anypoint Platform. The IDEs support the development lifecycle:

- 
API specification design, a mocking service for testing, source control, and publication to Anypoint Exchange 
- 
API implementation features for importing supported API specifications (such as OAS, RAML, AsyncAPI, or GraphQL) and autogenerating interfaces (scaffolding) for flows and error handlers within a Mule application 
- 
Integration development to connect systems, transform data to required formats, and provide business logic to manage messages and events programmatically within a Mule application 

The desktop and cloud IDEs offer the same Anypoint Code Builder functionality. Use the IDE that works better for your needs. You can share project snapshots between IDEs or with members of your team by using import and export features or by using a [source control management (SCM) system](#scm) of your choice.

For an introduction to Anypoint Code Builder, see our Trailhead badge, [Anypoint Code Builder: Quick Look](https://trailhead.salesforce.com/content/learn/modules/mulesoft-anypoint-code-builder-quick-look) (login required). Sign up if you don’t have a Trailhead account.

## Anypoint Extension Pack

Get the Anypoint Code Builder experience through the Anypoint Extension Pack for Visual Studio Code. The cloud-based extensions are preinstalled into a code-server implementation that makes VS Code accessible from a browser. The desktop extensions require installation to your VS Code IDE. See [Getting Started with Anypoint Code Builder](start-acb).

## Cloud Hosts

Anypoint Code Builder is available through Anypoint Platform from US, EU, Canada (desktop IDE only), Japan (desktop IDE only), and India (desktop IDE only) cloud hosts. To help your organization meet emerging regulatory requirements that differ by region, Anypoint Platform does not share organization information, permissions, account data, or projects between hosts.

| Control Plane | Platform URL | Description | 
|---|---|---|
| US Cloud | 
 | Non-EU region host. MuleSoft hosts this control plane within data centers in the United States. | 
| EU Cloud | 
 | EU-compliant host. MuleSoft hosts this control plane within EU (Frankfurt) data centers. | 
| Canada Cloud (desktop IDE only) | 
 | MuleSoft hosts this control plane within Canada (North America) data centers. | 
| Japan Cloud (desktop IDE only) | 
 | MuleSoft hosts this control plane within Japan (APAC) data centers. | 
| India Cloud (desktop IDE only) | 
 | MuleSoft hosts this control plane within India (APAC) data centers. | 

Anypoint Platform hosts deployment targets for managed Mule runtime versions and related data, including data and metadata about your Mule implementations.

To change the host from the default (US), see [Set the Desktop IDE to a Different Control Plane](start-acb#change-clouds).

Use of Anypoint Code Builder in the desktop and cloud IDEs requires an Anypoint Platform user account. Access to the cloud IDE and use of some features in both IDEs require permissions set by an organization administrator (see [Configuring Permissions](start-configure-permissions)).

To open Anypoint Code Builder from Anypoint Platform, see [Launch the Cloud IDE](start-acb#set-up-web). If you do not have an Anypoint Platform account through your organization, you can sign up in the US or EU cloud host for Anypoint Platform.

See [Anypoint Platform Hosting Overview](../hosting-home/) for more information.

## Get Familiar with the Basics

Some knowledge about designing an API using API specification languages (such as OAS, RAML, AsyncAPI, or gRPC) can be helpful. API implementations and integration development require familiarity with Mule application development, connectors, and the DataWeave transformation language. Anypoint Code Builder [Tutorials](tutorials) help you get started with these tasks.

It’s also useful to be familiar with these products and features:

- 
Anypoint Connectors provide operations for retrieving, modifying, and sending data to and from systems. Anypoint Code Builder provides [built-in connectors](acb-reference#builtin-connectors)and access to many other connectors from Anypoint Exchange.
- 
Core processors (also called Core components or Mule components) are programmatic building blocks that provide the business logic for integration and implementation applications. Examples include For Each ( `<foreach/>`), Transform Message (`<ee:transform/>`), and Flow (`<flow/>`). See[Anypoint Code Builder Components and Commands Reference](acb-reference).
- 
DataWeave is the programming language for all expressions and data transformations in your integrations and implementations. The language offers function libraries and mechanisms for creating customizations, including your own functions, libraries, and data types. To learn the basics of DataWeave and experiment with DataWeave scripts, see [DataWeave Tutorial and Playground](https://dataweave.mulesoft.com/).
- 
Scaffolding is an automatic process that uses APIkit to take an API specification as input and autogenerate an XML-based router and endpoints that you implement within a Mule application. 
- 
A flow is a block of components, including any connector operations, that Mule runtime engine (Mule) executes sequentially on an event and the message it contains. A flow can also contain an operation that triggers the creation of the event and initiates the execution of the flow. A subflow is similar to a flow but does not support the configuration of triggers (sometimes called message sources), which are exclusive to flows. A flow reference enables you to trigger execution of a flow or subflow from another flow. 
- 
A Mule application contains one or more XML-based configuration files for your connectors, components, secure configuration properties, scaffolded API specifications, and other parts of your integrations and implementations. The application runs on Mule and is part of a project that contains the resources needed to configure, build, run, test, and deploy the application. 

- 
Business groups organize APIs, Mule applications, and other resources within an Anypoint Platform organization. Organization administrators create and control access to business groups. For details about business groups, organizations, and related management features, see [Anypoint Platform Business Groups](../access-management/business-groups).

## Anypoint Platform Product Integrations

Both the web and desktop Anypoint Code Builder IDEs integrate with key Anypoint Platform products and features:

- 
Anypoint Exchange for publishing the API specifications that you create and importing API specifications and development resources (such as connectors, integration project templates and examples) into your projects 
- 
CloudHub and CloudHub 2.0 for deploying the implementations and integrations that you build 
- 
MuleSoft VCS for importing API specification projects into Anypoint Code Builder and optionally, synchronizing imported projects by using the Anypoint source control management (SCM) system 

The use of features provided by Anypoint Platform products through the cloud and desktop IDEs requires a connection from the IDE to Anypoint Platform. You establish this connection by logging in to your Anypoint Platform account from the IDE. For more information, see [Log in to Anypoint Platform from the IDE](start-acb#log-in-to-anypoint-platform-from-the-ide).

## Source and Version Control

Use any supported source control management (SCM) system. VS Code supports Git out-of-the-box in addition to several extensions for popular version control and SCM systems.

For guidance with Git setup in Anypoint Code Builder, see [Controlling Source Files](start-scm).

See VS Code documentation on [Git support](https://code.visualstudio.com/docs/sourcecontrol/overview) and [extensions for other SCM providers](https://code.visualstudio.com/docs/sourcecontrol/overview#_scm-providers). For extension authors only, VS Code also provides a [VS Code source control API](https://code.visualstudio.com/api/extension-guides/scm-provider).

## Feedback

To provide feedback about Anypoint Code Builder, complete the [feedback survey](https://www.surveymonkey.com/r/acb_feedback).

For questions or general discussion about Anypoint Code Builder, see [Trailblazer Discussion Topic](https://trailhead.salesforce.com/trailblazer-community/topics/mulesoftanypointcodebuilder?sort=LAST_MODIFIED_DATE_DESC).