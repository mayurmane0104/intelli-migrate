# Aggregators Module 1.1 | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/aggregators-module/latest](https://docs.mulesoft.com/aggregators-module/latest)

---

# Aggregators Module 1.1

For compatibility information and fixed issues, see the Aggregator Module Release Notes.

Aggregators Module contains different types of aggregators that use a specified configuration to both store and release values. An *aggregator scope* is a component that collects those values until a specified condition is met, when it then executes a processor’s chain of components, with the list of aggregated elements as the payload.

The basic aggregator configuration consists of the definition of the value to aggregate (extracted from the message through an expression evaluation), a condition that defines when the aggregation is considered complete, and a processor chain that executes once that condition is met.

Aggregators are pass-through routers. The same data that an aggregator scope receives is processed by the components that follow the aggregator scope. The only modification is variable propagation if any variables are set during the execution of any of the aggregation routes.

## Before You Begin

To use this module, you must be familiar with:

- 
Anypoint Connectors 
- 
Mule runtime engine (Mule) 
- 
Elements and global elements in a Mule flow 
- 
Creating a Mule app using Anypoint Studio or Anypoint Code Builder 

## See Also

- 
[Use Exchange to Discover Connectors, Templates, and Examples](../../connectors/introduction/intro-use-exchange)
- 
[Salesforce Help](https://help.salesforce.com)