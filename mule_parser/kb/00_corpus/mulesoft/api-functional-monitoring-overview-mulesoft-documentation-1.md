# API Functional Monitoring Overview | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/api-functional-monitoring](https://docs.mulesoft.com/api-functional-monitoring)

---

![AFM page showing a selected monitor’s details](_images/afm-ui-test-versions-and-schedules-new.png) 

# API Functional Monitoring Overview

API Functional Monitoring is a component of Anypoint Platform that enables you to ensure the quality and reliability of public and private APIs that are being used in application networks.

Developers and operators can use API Functional Monitoring to perform consistent testing of the functional behavior and performance of APIs throughout the API lifecycle, in testing and production environments. You can:

- 
Monitor Public or Private APIs from the Anypoint Monitoring UI or by using the BAT command line interface (BAT CLI) 
- 
View and report on the results of monitor executions 

The Functional Monitoring page with a monitor selected is shown in the following image:

![AFM page showing a selected monitor’s details](_images/afm-ui-test-versions-and-schedules-new.png) 

| 1 | Duration of the test for the selected monitor. | 
| 2 | Daily average response time in milliseconds of all tests to all endpoints. The colors in each bar indicate the breakdown of the average time for each of the steps in a test. Hover over the bar to see the breakdown details. | 
| 3 | Schedule information, including when the next run is scheduled, the schedule interval, and information about the location where the tests are scheduled to run. | 
| 4 | Details about the previous execution, including the method executed and the assertions. | 
| 5 | A summary list of the last few executions. | 
| 6 | Option to add schedules to the selected monitor. | 

## Functional Monitoring Concepts

Following are the concepts you need to know to use API Functional Monitoring.

### Monitors

A monitor is a repeating schedule of one or more tests. Monitors are also called test suites.

### Tests

Tests run in monitors on a defined schedule. Test cases are defined using Behavior Driven Development (BDD) language, a common, declarative, and easy-to-use behavior-description language.

### Behavior Driven Development (BDD) Language

The BDD language is used to write tests. It is based on DataWeave and follows the “given-when-then” approach to describe behavior in terms of conditions and expected outcomes.

### Test Suites

See [Monitors](#afm-monitors).

### Schedules

Schedules are designated intervals and durations configured in monitors for test suites to run.

### Black Box Testing

Black box testing validates the overall behavior of an API and its live dependencies as a whole, based entirely on inputs and outputs. These tests are done without knowing or altering the API internals &mdash and without simulation or mocking.

### White Box Testing

White box testing validates the behavior of individual APIs against the understanding of how their internals work. As part of this type of testing, you mock and simulate dependencies, such as back-end systems and other APIs.

### Runtime Monitoring

Runtime monitoring ensures that deployed APIs operate within the expected performance level in production environments. Runtime monitoring uses behavioral test cases with real inputs, expected outputs, and live dependencies.

### Private APIs

Private APIs are APIs with endpoints that are accessible only within your network inside an Anypoint VPC.

### Public APIs

Public APIs are APIs with endpoints that are exposed to the public internet. Tests of such endpoints are run by workers that themselves run in public locations or private locations.

### Private Locations

A private location is a Mule application that runs in an environment in CloudHub 1.0 or Cloudhub 2.0. You can run tests against APIs that are accessible only within the private location. The private location environment might have an Anypoint VPC associated with it. You can create multiple private locations in a single instance of Anypoint VPC.

### Public Locations

A public location is a region, or resource pool, that is shared with other MuleSoft customers. Examples of such regions are `us-east-1`, `us-east-2`, and `eu-central-1`.

## Next Steps

Continue to [Getting Started with API Functional Monitoring](afm-getting-started).