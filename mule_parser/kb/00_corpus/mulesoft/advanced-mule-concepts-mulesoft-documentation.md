# Advanced Mule Concepts | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/mule-runtime/latest/advanced-mule-concepts](https://docs.mulesoft.com/mule-runtime/latest/advanced-mule-concepts)

---

# Advanced Mule Concepts

After you become familiar with the basics of Mule application development and Mule runtime engine (Mule) concepts, you can focus on more advanced features, such as the execution engine, the classloading isolation mechanism, and distributed file polling.

Learn about the [execution engine](execution-engine) to understand how Mule runtime engine processes the operations in a Mule application flow, and to understand how to change the thread pools if needed. Mule runtime engine uses execution metadata provided by operations in a flow to perform autotuning.

The [classloading isolation](about-classloading-isolation) mechanism implemented in Mule 4 is designed to make upgrades easier by preventing components from exposing their internal resources. All components interact with each other through their defined APIs so that only exposed resources can be accessed by other components. Classloading isolation ensures that a component’s internal content is protected and can be changed any time, without affecting other components.

Mule 4 supports [distributed file polling](distributed-file-polling), which allows connectors to read files from certain directories as they are created. Distributed file polling also makes it possible to poll files in all cluster nodes.

Mule 4 also supports [distributed locking](distributed-locking), which provides the ability to create locks for synchronizing access to resources within Mule components.

Learn more about [Mule data types](mule-data-types) to understand how Mule centralizes data access across different components, and also how DataWeave uses this information to determine which reader and writer to use.

You can refer to the [Javadocs](mule-4-api-javadoc) for Mule Kernel (the community edition of Mule runtime engine) to learn definitions for classes, fields, and data types.

You can see a list of [third-party software](third-party-software-in-mule) that is included as part of Mule runtime engine as internal dependencies.