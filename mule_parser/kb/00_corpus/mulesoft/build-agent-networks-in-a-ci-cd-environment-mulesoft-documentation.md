# Build Agent Networks in a CI/CD Environment | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/anypoint-code-builder/af-build-agent-networks-in-a-ci-cd-environment](https://docs.mulesoft.com/anypoint-code-builder/af-build-agent-networks-in-a-ci-cd-environment)

---

$ anypoint-cli-agent-fabric-plugin conf client_id myClientID $ anypoint-cli-agent-fabric-plugin conf client_secret myClientSecret $ anypoint-cli-agent-fabric-plugin conf organization myOrgId

# Build Agent Networks in a CI/CD Environment

Use the Anypoint CLI Agent Fabric plugin in CI/CD pipelines to configure agent network gateways, create and build projects, and publish and deploy networks from the command line, matching the lifecycle you can drive from Anypoint Code Builder. Automating these steps keeps environments aligned, lets you embed approvals, secrets, and quality gates in the pipeline, and avoids one-off scripts when you promote from development to staging and production.

For installation, package updates, and release details, see [Anypoint CLI Agent Fabric Plugin on npm](https://www.npmjs.com/package/mulesoft-anypoint-cli-agent-fabric-plugin).

## Before You Begin

Make sure you meet the [prerequisites](af-get-started#before-you-begin) for this task.

Install the Anypoint CLI Agent Fabric plugin by running this command in a terminal window:

`npm i mulesoft-anypoint-cli-agent-fabric-plugin`

| The installation package has been renamed from  If you have the previous version installed, you may encounter an  | 

### Authentication

You can authenticate to Anypoint Platform through the command line by running the `anypoint-cli-agent-fabric-plugin` command with a combination of parameters.

Or, you can set a combination of environment variables before running the `anypoint-cli-agent-fabric-plugin` command. For more information, see [Command-Line Parameters and Environment Variables](https://docs.mulesoft.com/anypoint-cli/latest/auth#command-line-parameters).

Set configuration file authentication using a client ID and client secret from your connected app.

Add authentication values to the configuration file using these commands.

For more information, see [Authentication to the Anypoint Platform CLI](../anypoint-cli/latest/auth).

### Create a Target Space for Your Environment

To deploy an agent network, you need a private space on CloudHub 2.0 or a deployment target on Anypoint Runtime Fabric. See [Set Up the Private Space or Deployment Target for Your Environment](af-get-started#setup-space).

After you create a target space, set up the ingress and egress gateways for deployment if you haven’t already done so. See [Set Up Agent Network Gateways for the Private Space or Deployment Target](af-get-started#setup-gateways).

## CLI for Agent Fabric Plugin Reference

Use these commands to set up gateways and author, publish, and deploy agent network projects.

| Command | Description | 
|---|---|
| Builds the agent network project and validates configuration | |
| Creates a new agent network project and generates the initial configuration files | |
| Deploys the agent network project to the target environment | |
| Publishes the agent network project to Anypoint Exchange | |
| Sets up the gateways for the agent network | 

## agent-network:project:build

> anypoint-cli-agent-fabric-plugin agent-network project build [flags]

Builds the current agent network project using the Maven wrapper (`mvnw` or `mvnw.cmd`).
This command validates the configuration and generates the artifacts required for publishing and deployment.

In addition to the [default flags](../anypoint-cli/latest/#default-options), this command accepts these flags:

| Flag | Description | Example | 
|---|---|---|
| 
 | Bearer token | 
 | 
| 
 | Client ID | 
 | 
| 
 | Client Secret | 
 | 
| 
 | Collect metrics | 
 | 
| 
 | Enable debug mode | 
 | 
| 
 | Environment name | 
 | 
| 
 | Force update the dependencies | 
 | 
| 
 | Host URL | 
 | 
| 
 | Organization name | 
 | 
| 
 | Password | 
 | 
| 
 | Path to the project | 
 | 
| 
 | Username | 
 | 

### Example

$ anypoint-cli-agent-fabric-plugin agent-network project build

## agent-network:project:create

> anypoint-cli-agent-fabric-plugin agent-network project create --name <projectName> [flags]

Creates a new agent network project in the current directory.
The command generates a project folder with initial configuration files, including `agent-network.yaml`.

In addition to the [default flags](../anypoint-cli/latest/#default-options), this command accepts these flags:

| Flag | Description | Example | 
|---|---|---|
| 
 | (Required) Name of the project | 
 | 
| 
 | Output directory for the project | 
 | 
| 
 | Asset ID (GAV) | 
 | 
| 
 | Asset version (GAV) | 
 | 
| 
 | Bearer token | 
 | 
| 
 | Client ID | 
 | 
| 
 | Client Secret | 
 | 
| 
 | Collect metrics | 
 | 
| 
 | Create a new directory under  | 
 | 
| 
 | Environment name | 
 | 
| 
 | Group ID (GAV) | 
 | 
| 
 | Host URL | 
 | 
| 
 | Organization name | 
 | 
| 
 | Password | 
 | 
| 
 | Tab size for indenting the API specification | 
 | 
| 
 | Username | 
 | 

### Example

$ anypoint-cli-agent-fabric-plugin agent-network project create --name my-agent-network

## agent-network:project:deploy

> anypoint-cli-agent-fabric-plugin agent-network project deploy [flags]

Deploys the agent network application to the target private space.
By default, the command uses the `agent-network-ingress-gw` and `agent-network-egress-gw` gateways, and the `agent-network-space` private space.
You can override these values using flags.

In addition to the [default flags](../anypoint-cli/latest/#default-options), this command accepts these flags:

| Flag | Description | Example | 
|---|---|---|
| 
 | Name of the target egress gateway | 
 | 
| 
 | Name of the target ingress gateway | 
 | 
| 
 | Name of the target private space to deploy | 
 | 
| 
 | Bearer token | 
 | 
| 
 | Client ID | 
 | 
| 
 | Client Secret | 
 | 
| 
 | Collect metrics | 
 | 
| 
 | Disable tracing functionalities | 
 | 
| 
 | Do not wait for the agent network to be ready | 
 | 
| 
 | Environment name | 
 | 
| 
 | Host URL | 
 | 
| 
 | Organization name | 
 | 
| 
 | Password | 
 | 
| 
 | Path to the project | 
 | 
| 
 | One or more deployment properties in  | 
 | 
| 
 | Username | 
 | 
| 
 | Format output as JSON | 
 | 

### Example

$ anypoint-cli-agent-fabric-plugin agent-network project deploy --environment Staging --target-space staging-private-space --property openai.apiKey:STAGING_API_KEY

## agent-network:project:publish

> anypoint-cli-agent-fabric-plugin agent-network project publish [flags]

Publishes the current agent network project to Anypoint Exchange. The command outputs links and details for all created assets.

In addition to the [default flags](../anypoint-cli/latest/#default-options), this command accepts these flags:

| Flag | Description | Example | 
|---|---|---|
| 
 | Bearer token | 
 | 
| 
 | Client ID | 
 | 
| 
 | Client Secret | 
 | 
| 
 | Collect metrics | 
 | 
| 
 | Enable debug mode | 
 | 
| 
 | Environment name | 
 | 
| 
 | Host URL | 
 | 
| 
 | Organization name | 
 | 
| 
 | Password | 
 | 
| 
 | Path to the project | 
 | 
| 
 | Username | 
 | 
| 
 | Format output as JSON | 
 | 

### Example

$ anypoint-cli-agent-fabric-plugin agent-network project publish

## agent-network:setup:gateways

> anypoint-cli-agent-fabric-plugin agent-network setup gateways [flags]

Sets up the agent network environment with the required ingress and egress gateways in the specified target private space. This step is required only if the target space does not already have gateways. In the typical (happy path) workflow, you run it once per target space before the first deployment.

In addition to the [default flags](../anypoint-cli/latest/#default-options), this command accepts these flags:

| Flag | Description | Example | 
|---|---|---|
| 
 | Name of the egress gateway | 
 | 
| 
 | Name of the ingress gateway | 
 | 
| 
 | Name of the target private space where the gateways will be set up | 
 | 
| 
 | Bearer token | 
 | 
| 
 | Client ID | 
 | 
| 
 | Client Secret | 
 | 
| 
 | Collect metrics | 
 | 
| 
 | Environment name | 
 | 
| 
 | Host URL | 
 | 
| 
 | Organization name | 
 | 
| 
 | Password | 
 | 
| 
 | Username | 
 | 

### Example

$ anypoint-cli-agent-fabric-plugin agent-network setup gateways --target-space my-space