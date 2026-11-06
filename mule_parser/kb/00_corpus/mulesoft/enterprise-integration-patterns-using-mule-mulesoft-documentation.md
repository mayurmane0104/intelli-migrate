# Enterprise Integration Patterns Using Mule | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/mule-runtime/latest/understanding-enterprise-integration-patterns-using-mule](https://docs.mulesoft.com/mule-runtime/latest/understanding-enterprise-integration-patterns-using-mule)

---

# Enterprise Integration Patterns Using Mule

Enterprise Integration Patterns are accepted solutions to recurring problems within a given context. The patterns provide a framework for designing, building messaging and integration systems, as well as a common language for teams to use when architecting solutions.

Mule supports most of the patterns shown in the Enterprise Integration Patterns book written by Gregor Hohpe and Bobby Woolf.

Mule reduces the effort required when building integrations by implementing the patterns that you use to design solutions. You can then simply configure and use these same patterns in Mule.

## Mapping Enterprise Integration Patterns into Mule Objects

Review the following list of Enterprise Integration Patterns that can be mapped directly to Mule objects:

### Integration Styles

| Pattern | Mapping to a Mule Object | 
|---|---|
| File Transfer | |
| Shared Database | |
| Remote Procedure Invocation | Mule APIs are meant to work like this procedure or even doing requests to external APIs. | 
| Messaging | Mule is all about Messaging. | 

### Messaging Systems

| Pattern | Mapping to a Mule Object | 
|---|---|
| Message Channel | Mule provides a message channel that connects the message processors in a flow. | 
| Pipes and Filters | A flow implements a pipe and filter architecture. | 
| Message Router | |
| Message Translator | |
| Message Endpoint | 

### Messaging Channels

| Pattern | Mapping to a Mule Object | 
|---|---|
| Point-to-Point Channel | The default channel within a flow. | 
| Message Bus | Mule is a message bus. | 
| Guaranteed Delivery | Using  | 

### Message Construction

| Pattern | Mapping to a Mule Object | 
|---|---|
| Event Message | Mule transmits events from different Application or Processors. | 
| Request Reply | Mule uses connectors that facilitate request-reply wise operations, or using  | 

### Message Routing

| Pattern | Mapping to a Mule Object | 
|---|---|
| Content-Based Router | |
| Message Filter | |
| Dynamic Routing | |
| Scatter Gather | |
| Splitter | 
 | 
| Aggregator | 

### Message Transformation

| Pattern | Mapping to a Mule Object | 
|---|---|
| Content Enricher | 

### Messaging Endpoints

| Pattern | Mapping to a Mule Object | 
|---|---|
| Polling Consumer | |
| Transactional Client | |
| Idempotent Receiver |