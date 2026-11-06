# Continuous Integration | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/mule-runtime/latest/continuous-integration](https://docs.mulesoft.com/mule-runtime/latest/continuous-integration)

---

# Continuous Integration

The need for continuous integration (CI) for a project is very important. By using Maven as your build tool, you can create a build that gets triggered on every project change, and run all of its unit and functional tests automatically.

The advantages of CI are:

- 
Provides early notification of issues in the software development lifecycle. 
- 
Ensures code gets fully tested before release. 
- 
Successfully tested branches ensure better success when merging to the main branch. 

## Continuous Integration Objectives

A CI system does all of the following:

- 
Listens for new commits to a project’s source code management system. The CI system watches many branches for new commits. You can either use polling to find new commits, or the management system can trigger events that inform your program of commits. 
- 
Pulls the newest branch into a centralized server. 
- 
Creates build jobs on a centralized server. 
- 
Runs configurable unit and integration tests on the code base that compile, test, package, and deploy the project in a sandbox to ensure the project works correctly. 
- 
Stores artifacts in a repository. 
- 
Displays the results of each build. 
- 
Deploys passing builds to production. 

For information about these tools, see their websites.

## MuleSoft CI Tools

You can deploy Mule applications using:

You can create functional tests with [MUnit Unit Testing](../../munit/latest/).

The mule-maven-plugin supports deployments to:

- 
CloudHub 
- 
Runtime Fabric 
- 
On-premises Mule instances - 
Standalone deployment 
- 
Using Anypoint Runtime Manager REST API 
- 
Using Runtime Manager agent 
 
- 

For a complete CI example that uses Jenkins and Maven, see the Anypoint Platform Development: Advanced class on the [MuleSoft training site](https://trailheadacademy.salesforce.com/products/mulesoft). The training site also includes related classes and certification exams.

## External CI Tools

Popular CI tools are:

- 
Jenkins 
- 
Hudson 
- 
TeamCity 
- 
Bamboo 

For information about these tools, see their websites.

## Integration Notes

If you’ve chosen to use connectors in your functional test cases, watch out for potential port conflicts that can occur in a continuous build server.

If your target deployable is a web application and not a Mule application, consider using Junit Integration Test Runner for running your functional tests and avoiding port conflicts.