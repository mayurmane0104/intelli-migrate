# Maintainers playbook - Powertools for AWS Lambda (Python)

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/maintainers](https://docs.aws.amazon.com/powertools/python/latest/maintainers)

---

# Maintainers

## Overview[¶](https://docs.aws.amazon.com/powertools/python/latest/maintainers/#overview)

Please treat this content as a living document.

This is document explains who the maintainers are, their responsibilities, and how they should be doing it. If you're interested in contributing, see [CONTRIBUTING](https://github.com/aws-powertools/powertools-lambda-python/blob/develop/CONTRIBUTING.md).

## Current Maintainers[¶](https://docs.aws.amazon.com/powertools/python/latest/maintainers/#current-maintainers)

| Maintainer | GitHub ID | Affiliation | 
|---|---|---|
| Leandro Damascena | [leandrodamascena](https://github.com/leandrodamascena) | Amazon | 

## AWS Contributors[¶](https://docs.aws.amazon.com/powertools/python/latest/maintainers/#aws-contributors)

Active contributors from AWS who help maintain and improve this project.

| Contributor | GitHub ID | 
|---|---|
| Ana Falcão | [anafalcao](https://github.com/anafalcao) | 

## Emeritus[¶](https://docs.aws.amazon.com/powertools/python/latest/maintainers/#emeritus)

Previous active maintainers who contributed to this project.

| Maintainer | GitHub ID | Affiliation | 
|---|---|---|
| Alexander Schueren | [am29d](https://github.com/am29d) | Amazon | 
| Heitor Lessa | [heitorlessa](https://github.com/heitorlessa) | Adyen | 
| Michal Ploski | [mploski](https://github.com/mploski) | Splunk | 
| Nicolas Moutschen | [nmoutschen](https://github.com/nmoutschen) | Apollo | 
| Ruben Fonseca | [rubenfonseca](https://github.com/rubenfonseca) | N/A | 
| Simon Thulbourn | [sthulb](https://github.com/sthulb) | N/A | 
| Tom McCarthy | [cakepietoast](https://github.com/cakepietoast) | MongoDB | 

## Labels[¶](https://docs.aws.amazon.com/powertools/python/latest/maintainers/#labels)

These are the most common labels used by maintainers to triage issues, pull requests (PR), and for project management:

| Label | Usage | Notes | 
|---|---|---|
| triage | New issues that require maintainers review | Issue template | 
| bug | Unexpected, reproducible and unintended software behavior | PR/Release automation; Doc snippets are excluded; | 
| not-a-bug | New and existing bug reports incorrectly submitted as bug | Analytics | 
| documentation | Documentation improvements | PR/Release automation; Doc additions, fixes, etc.; | 
| feature-request | New or enhancements to existing features | Issue template | 
| typing | New or enhancements to static typing | Issue template | 
| RFC | Technical design documents related to a feature request | Issue template | 
| bug-upstream | Bug caused by upstream dependency | |
| help wanted | Tasks you want help from anyone to move forward | Bandwidth, complex topics, etc. | 
| need-customer-feedback | Tasks that need more feedback before proceeding | 80/20% rule, uncertain, etc. | 
| need-more-information | Missing information before making any calls | |
| need-documentation | PR is missing or has incomplete documentation | |
| need-issue | PR is missing a related issue for tracking change | PR automation | 
| need-rfc | Feature request requires a RFC to improve discussion | |
| pending-release | Merged changes that will be available soon | Release automation auto-closes/notifies it | 
| revisit-in-3-months | Blocked issues/PRs that need to be revisited | Often related to `need-customer-feedback`, prioritization, etc. | 
| breaking-change | Changes that will cause customer impact and need careful triage | |
| do-not-merge | PRs that are blocked for varying reasons | Timeline is uncertain | 
| size/XS | PRs between 0-9 LOC | PR automation | 
| size/S | PRs between 10-29 LOC | PR automation | 
| size/M | PRs between 30-99 LOC | PR automation | 
| size/L | PRs between 100-499 LOC | PR automation | 
| size/XL | PRs between 500-999 LOC, often PRs that grown with feedback | PR automation | 
| size/XXL | PRs with 1K+ LOC, largely documentation related | PR automation | 
| tests | PRs that add or change tests | PR automation | 
| `<utility>` | PRs related to a Powertools for AWS Lambda (Python) utility, e.g. `parameters`,`tracer` | PR automation | 
| feature | New features or minor changes | PR/Release automation | 
| dependencies | Changes that touch dependencies, e.g. Dependabot, etc. | PR/ automation | 
| github-actions | Changes in GitHub workflows | PR automation | 
| github-templates | Changes in GitHub issue/PR templates | PR automation | 
| internal | Changes in governance and chores (linting setup, baseline, etc.) | PR automation | 
| tech-debt | Changes in tech debt | |
| customer-reference | Authorization to use company name in our documentation | Public Relations | 
| community-content | Suggested content to feature in our documentation | Public Relations | 

## Maintainer Responsibilities[¶](https://docs.aws.amazon.com/powertools/python/latest/maintainers/#maintainer-responsibilities)

Maintainers are active and visible members of the community, and have [maintain-level permissions on a repository](https://docs.github.com/en/organizations/managing-access-to-your-organizations-repositories/repository-permission-levels-for-an-organization). Use those privileges to serve the community and evolve code as follows.

Be aware of recurring ambiguous situations and [document them](https://docs.aws.amazon.com/powertools/python/latest/maintainers/#common-scenarios) to help your fellow maintainers.

### Uphold Code of Conduct[¶](https://docs.aws.amazon.com/powertools/python/latest/maintainers/#uphold-code-of-conduct)

Model the behavior set forward by the [Code of Conduct](https://github.com/aws-powertools/powertools-lambda-python/blob/develop/CODE_OF_CONDUCT.md) and raise any violations to other maintainers and admins. There could be unusual circumstances where inappropriate behavior does not immediately fall within the [Code of Conduct](https://github.com/aws-powertools/powertools-lambda-python/blob/develop/CODE_OF_CONDUCT.md).

These might be nuanced and should be handled with extra care - when in doubt, do not engage and reach out to other maintainers and admins.

### Prioritize Security[¶](https://docs.aws.amazon.com/powertools/python/latest/maintainers/#prioritize-security)

Security is your number one priority. Maintainer's Github keys must be password protected securely and any reported security vulnerabilities are addressed before features or bugs.

Note that this repository is monitored and supported 24/7 by Amazon Security, see [Reporting a Vulnerability](https://github.com/aws-powertools/powertools-lambda-python/blob/develop/SECURITY.md) for details.

### Review Pull Requests[¶](https://docs.aws.amazon.com/powertools/python/latest/maintainers/#review-pull-requests)

Review pull requests regularly, comment, suggest, reject, merge and close. Accept only high quality pull-requests. Provide code reviews and guidance on incoming pull requests.

PRs are [labeled](https://docs.aws.amazon.com/powertools/python/latest/maintainers/#labels) based on file changes and semantic title. Pay attention to whether labels reflect the current state of the PR and correct accordingly.

Use and enforce [semantic versioning](https://semver.org/) pull request titles, as these will be used for [CHANGELOG](https://github.com/aws-powertools/powertools-lambda-python/blob/develop/CHANGELOG.md) and [Release notes](https://github.com/aws-powertools/powertools-lambda-python/releases) - make sure they communicate their intent at the human level.

TODO: This is an area we want to automate using the new GitHub GraphQL API.


For issues linked to a PR, make sure `pending release` label is applied to them when merging. [Upon release](https://docs.aws.amazon.com/powertools/python/latest/maintainers/#releasing-a-new-version), these issues will be notified which release version contains their change.

See [Common scenarios](https://docs.aws.amazon.com/powertools/python/latest/maintainers/#common-scenarios) section for additional guidance.

### Triage New Issues[¶](https://docs.aws.amazon.com/powertools/python/latest/maintainers/#triage-new-issues)

Manage [labels](https://docs.aws.amazon.com/powertools/python/latest/maintainers/#labels), review issues regularly, and create new labels as needed by the project. Remove `triage` label when you're able to confirm the validity of a request, a bug can be reproduced, etc. Give priority to the original author for implementation, unless it is a sensitive task that is best handled by maintainers.

TODO: This is an area we want to automate using the new GitHub GraphQL API.


Make sure issues are assigned to our [board of activities](https://github.com/orgs/awslabs/projects/51/) and have the right [status](https://docs.aws.amazon.com/powertools/python/latest/roadmap/#roadmap-status-definition).

Use our [labels](https://docs.aws.amazon.com/powertools/python/latest/maintainers/#labels) to signal good first issues to new community members, and to set expectation that this might need additional feedback from the author, other customers, experienced community members and/or maintainers.

Be aware of [casual contributors](https://opensource.com/article/17/10/managing-casual-contributors) and recurring contributors. Provide the experience and attention you wish you had if you were starting in open source.

See [Common scenarios](https://docs.aws.amazon.com/powertools/python/latest/maintainers/#common-scenarios) section for additional guidance.

### Triage Bug Reports[¶](https://docs.aws.amazon.com/powertools/python/latest/maintainers/#triage-bug-reports)

Be familiar with [our definition of bug](https://docs.aws.amazon.com/powertools/python/latest/maintainers/#is-that-a-bug). If it's not a bug, you can close it or adjust its title and labels - always communicate the reason accordingly.

For bugs caused by upstream dependencies, replace `bug` with `bug-upstream` label. Ask the author whether they'd like to raise the issue upstream or if they prefer us to do so.

Assess the impact and make the call on whether we need an emergency release. Contact other [maintainers](https://docs.aws.amazon.com/powertools/python/latest/maintainers/#current-maintainers) when in doubt.

See [Common scenarios](https://docs.aws.amazon.com/powertools/python/latest/maintainers/#common-scenarios) section for additional guidance.

### Triage RFCs[¶](https://docs.aws.amazon.com/powertools/python/latest/maintainers/#triage-rfcs)

RFC is a collaborative process to help us get to the most optimal solution given the context. Their purpose is to ensure everyone understands what this context is, their trade-offs, and alternative solutions that were part of the research before implementation begins.

Make sure you ask these questions in mind when reviewing:

- Does it use our [RFC template](https://github.com/aws-powertools/powertools-lambda-python/issues/new?assignees=&labels=RFC%2Ctriage&template=rfc.yml&title=RFC%3A+TITLE)?
- Does the match our [Tenets](https://docs.aws.amazon.com/powertools/python/latest/#tenets)?
- Does the proposal address the use case? If so, is the recommended usage explicit?
- Does it focus on the mechanics to solve the use case over fine-grained implementation details?
- Can anyone familiar with the code base implement it?
- If approved, are they interested in contributing? Do they need any guidance?
- Does this significantly increase the overall project maintenance? Do we have the skills to maintain it?
- If we can't take this use case, are there alternative projects we could recommend? Or does it call for a new project altogether?

When necessary, be upfront that the time to review, approve, and implement a RFC can vary - see [Contribution is stuck](https://docs.aws.amazon.com/powertools/python/latest/maintainers/#contribution-is-stuck). Some RFCs may be further updated after implementation, as certain areas become clearer.

Some examples using our initial and new RFC templates: #92, #94, #95, #991, #1226

### Releasing a new version[¶](https://docs.aws.amazon.com/powertools/python/latest/maintainers/#releasing-a-new-version)

Only maintainers with write access to this repository can release a new version

Releasing a new version is a multi-step process that takes up to 2 hours to complete. Most steps are automated - you provide inputs to trigger the release and monitor progress.

**Prerequisites**: Ensure the commit history in the `develop` branch is up to date, commit messages are semantic, and include their respective area (e.g., `feat(logger): <change>`, `chore(ci): ...`).

**Release Steps**:

- **Run**and ensure they pass- [end-to-end tests](https://github.com/aws-powertools/powertools-lambda-python/actions/workflows/run-e2e-tests.yml)
- **Trigger Release v3 workflow**- Run the- `Release v3`- [latest version](https://pypi.org/project/aws-lambda-powertools/)) and the new Lambda Layer version number. To find the new Lambda Layer version number, go to this- [page](https://docs.aws.amazon.com/powertools/python/latest/#python-313)and increase the version by one (N + 1).
- **Monitor the release workflow**- it runs tests, publishes to PyPI, deploys Lambda layers to Beta and Prod environments across all commercial regions, runs canary tests, and updates documentation. If it fails, see the- [Re-run partial failed Release workflow](https://docs.aws.amazon.com/powertools/python/latest/maintainers/#re-run-partial-failed-release-workflow)section
- **Review and merge documentation/version PRs**- two PRs will be created to update documentation and bump version files. Review, approve and merge both (order doesn't matter)
- **Deploy GovCloud layers**- Run the- `Layer Deployment (GovCloud)`- `develop`branch,- `Prod`environment, and the Layer version number from step 2.
- **Deploy China layers**- Run the- `Layer Deployment (Partitions)`- `develop`branch,- `Prod`environment, and the Layer version number from step 2.
- **Update documentation**- Run the- `Rebuild latest docs`- `develop`branch and the PyPI package version

Once complete, you can start drafting the release notes to let customers know **what changed and what's in it for them (a.k.a why they should care)**. We have guidelines in the [release notes](https://docs.aws.amazon.com/powertools/python/latest/maintainers/#drafting-release-notes) section so you know what good looks like.

#### Re-run partial failed Release workflow[¶](https://docs.aws.amazon.com/powertools/python/latest/maintainers/#re-run-partial-failed-release-workflow)

While workflows are designed to be stable, failures can occur during the release process. If the release workflow fails, you have two recovery options:

**Option 1: Re-run failed jobs** The Release v3 pipeline contains several steps, and one of them is `publish_layer`. This step is responsible for building and deploying public Lambda layers. If this step fails due to CloudFormation errors (we deploy approximately 600 layers per release and cannot control CloudFormation quotas), you can re-run only the failed jobs. This will retry the deployment and typically resolves quota-related issues.

**Option 2: Re-trigger the entire workflow**
If the release fails due to workflow modifications or permission issues that prevent re-running failed jobs, trigger the Release v3 workflow again.

Avoid PyPI errors

Make sure to select `Skip publishing to PyPI` as it can't publish more than once. This is useful for semi-failed releases when rerunning the entire workflow to avoid duplicate publishes

#### Release process visualized[¶](https://docs.aws.amazon.com/powertools/python/latest/maintainers/#release-process-visualized)

Every release makes hundreds of checks, security scans, canaries and deployments - all of these are automated.

This is a close visual representation of the main steps (GitHub Actions UI should be the source of truth), along with the approximate time it takes for each key step to complete.

#### Drafting release notes[¶](https://docs.aws.amazon.com/powertools/python/latest/maintainers/#drafting-release-notes)

Make sure the release workflow completed before you edit release notes.

Visit the [Releases page](https://github.com/aws-powertools/powertools-lambda-python/releases) and choose the edit pencil button.

Make sure the `tag` field reflects the new version you're releasing, the target branch field is set to `develop`, and `release title` matches your tag e.g., `v1.26.0`.

You'll notice we group all changes based on their [labels](https://docs.aws.amazon.com/powertools/python/latest/maintainers/#labels) like `feature`, `bug`, `documentation`, etc.

Spotted a typo?

Edit the respective PR title/labels and run the [Release Drafter workflow](https://github.com/aws-powertools/powertools-lambda-python/actions/workflows/release-drafter.yml).

All good, what's next?

The best part comes now!

Replace the placeholder `[Human readable summary of changes]` with what you'd like to communicate to customers what this release is all about.

Always put yourself in the customers shoes. Most read the first sentence only to know whether this is for them.

These are some questions to keep in mind when drafting your first or future release notes:

- **Can customers briefly understand the main changes in less than 30s?**- *tip: first paragraph is punchy and optimizes for dependabot-like notifications.*
 
- **Are we calling out key contributor(s) to this release?**
- **Is it clear what each change enables/unlocks and before?**- *tip: use present and active voice; lead with the answer.*
 
- **Does it include a link to the documentation for each main change?**- *tip: release explains what a change unblocks/enables (before/after), docs go in details*
 
- **Is code snippet better in text or**- [graphic](https://carbon.now.sh)?
- **Does code snippet focus on the change only?**- *tip: release snippets highlight functionality, no need to be functional (that's docs)*
 

Once you're happy, hit `Publish release` 🎉🎉🎉.

### Releasing an alpha release[¶](https://docs.aws.amazon.com/powertools/python/latest/maintainers/#releasing-an-alpha-release)

You can manually trigger the `pre-release` workflow to publish alpha releases *( prerelease)* to PyPi when needed.

### Run end to end tests[¶](https://docs.aws.amazon.com/powertools/python/latest/maintainers/#run-end-to-end-tests)

E2E tests are run on every push to `develop` or manually via [run-e2e-tests workflow](https://github.com/aws-powertools/powertools-lambda-python/actions/workflows/run-e2e-tests.yml).

To run locally, you need [AWS CDK CLI](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html#getting_started_prerequisites) and an [account bootstrapped](https://docs.aws.amazon.com/cdk/v2/guide/bootstrapping.html) (`cdk bootstrap`). With a default AWS CLI profile configured, or `AWS_PROFILE` environment variable set, run `make e2e tests`.

### Releasing a documentation hotfix[¶](https://docs.aws.amazon.com/powertools/python/latest/maintainers/#releasing-a-documentation-hotfix)

You can rebuild the latest documentation without a full release via this [GitHub Actions Workflow](https://github.com/aws-powertools/powertools-lambda-python/actions/workflows/rebuild_latest_docs.yml). Choose `Run workflow`, keep `develop` as the branch, and input the latest Powertools for AWS Lambda (Python) version available.

This workflow will update both user guide and API documentation.

### Maintain Overall Health of the Repo[¶](https://docs.aws.amazon.com/powertools/python/latest/maintainers/#maintain-overall-health-of-the-repo)

TODO: Coordinate renaming

`develop`to`main`

Keep the `develop` branch at production quality at all times. Backport features as needed. Cut release branches and tags to enable future patches.

### Manage Roadmap[¶](https://docs.aws.amazon.com/powertools/python/latest/maintainers/#manage-roadmap)

See [Roadmap section](https://docs.aws.amazon.com/powertools/python/latest/roadmap/)

Ensure the repo highlights features that should be elevated to the project roadmap. Be clear about the feature’s status, priority, target version, and whether or not it should be elevated to the roadmap.

### Add Continuous Integration Checks[¶](https://docs.aws.amazon.com/powertools/python/latest/maintainers/#add-continuous-integration-checks)

Add integration checks that validate pull requests and pushes to ease the burden on Pull Request reviewers. Continuously revisit areas of improvement to reduce operational burden in all parties involved.

### Negative Impact on the Project[¶](https://docs.aws.amazon.com/powertools/python/latest/maintainers/#negative-impact-on-the-project)

Actions that negatively impact the project will be handled by the admins, in coordination with other maintainers, in balance with the urgency of the issue. Examples would be [Code of Conduct](https://github.com/aws-powertools/powertools-lambda-python/blob/develop/CODE_OF_CONDUCT.md) violations, deliberate harmful or malicious actions, spam, monopolization, and security risks.

### Becoming a maintainer[¶](https://docs.aws.amazon.com/powertools/python/latest/maintainers/#becoming-a-maintainer)

In 2023, we will revisit this. We need to improve our understanding of how other projects are doing, their mechanisms to promote key contributors, and how they interact daily.

We suspect this process might look similar to the [OpenSearch project](https://github.com/opensearch-project/.github/blob/main/MAINTAINERS.md#becoming-a-maintainer).

## Common scenarios[¶](https://docs.aws.amazon.com/powertools/python/latest/maintainers/#common-scenarios)

These are recurring ambiguous situations that new and existing maintainers may encounter. They serve as guidance. It is up to each maintainer to follow, adjust, or handle in a different manner as long as [our conduct is consistent](https://docs.aws.amazon.com/powertools/python/latest/maintainers/#uphold-code-of-conduct)

### Contribution is stuck[¶](https://docs.aws.amazon.com/powertools/python/latest/maintainers/#contribution-is-stuck)

A contribution can get stuck often due to lack of bandwidth and language barrier. For bandwidth issues, check whether the author needs help. Make sure you get their permission before pushing code into their existing PR - do not create a new PR unless strictly necessary.

For language barrier and others, offer a 1:1 chat to get them unblocked. Often times, English might not be their primary language, and writing in public might put them off, or come across not the way they intended to be.

In other cases, you may have constrained capacity. Use `help wanted` label when you want to signal other maintainers and external contributors that you could use a hand to move it forward.

### Insufficient feedback or information[¶](https://docs.aws.amazon.com/powertools/python/latest/maintainers/#insufficient-feedback-or-information)

When in doubt, use `need-more-information` or `need-customer-feedback` labels to signal more context and feedback are necessary before proceeding. You can also use `revisit-in-3-months` label when you expect it might take a while to gather enough information before you can decide.

### Crediting contributions[¶](https://docs.aws.amazon.com/powertools/python/latest/maintainers/#crediting-contributions)

We credit all contributions as part of each [release note](https://github.com/aws-powertools/powertools-lambda-python/releases) as an automated process. If you find  contributors are missing from the release note you're producing, please add them manually.

### Is that a bug?[¶](https://docs.aws.amazon.com/powertools/python/latest/maintainers/#is-that-a-bug)

A bug produces incorrect or unexpected results at runtime that differ from its intended behavior. Bugs must be reproducible. They directly affect customers experience at runtime despite following its recommended usage.

Documentation snippets, use of internal components, or unadvertised functionalities are not considered bugs.

### Mentoring contributions[¶](https://docs.aws.amazon.com/powertools/python/latest/maintainers/#mentoring-contributions)

Always favor mentoring issue authors to contribute, unless they're not interested or the implementation is sensitive (*e.g., complexity, time to release, etc.*).

Make use of `help wanted` and `good first issue` to signal additional contributions the community can help.

### Long running issues or PRs[¶](https://docs.aws.amazon.com/powertools/python/latest/maintainers/#long-running-issues-or-prs)

Try offering a 1:1 call in the attempt to get to a mutual understanding and clarify areas that maintainers could help.

In the rare cases where both parties don't have the bandwidth or expertise to continue, it's best to use the `revisit-in-3-months` label. By then, see if it's possible to break the PR or issue in smaller chunks, and eventually close if there is no progress.

## E2E framework[¶](https://docs.aws.amazon.com/powertools/python/latest/maintainers/#e2e-framework)

### Structure[¶](https://docs.aws.amazon.com/powertools/python/latest/maintainers/#structure)

Our E2E framework relies on [Pytest fixtures](https://docs.pytest.org/en/6.2.x/fixture.html) to coordinate infrastructure and test parallelization - see [Test Parallelization](https://docs.aws.amazon.com/powertools/python/latest/maintainers/#test-runner-parallelization) and [CDK CLI Parallelization](https://docs.aws.amazon.com/powertools/python/latest/maintainers/#cdk-cli-parallelization).

**tests/e2e structure**

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 | 
 | 

Where:

- `<feature>/infrastructure.py`
- `<feature>/handlers/`- `BasicHandler`).
- `utils/`
- `conftest.py`- **Top-level (**. Builds Lambda Layer only once and blocks I/O across all CPU workers.- `e2e/conftest`)
- **Feature-level (**. Deploys stacks in parallel and make them independent of each other.- `e2e/<feature>/conftest`)
 

### Mechanics[¶](https://docs.aws.amazon.com/powertools/python/latest/maintainers/#mechanics)

Under [ BaseInfrastructure](https://github.com/aws-powertools/powertools-lambda-python/blob/develop/tests/e2e/utils/infrastructure.py), we hide the complexity of deployment and delete coordination under 

`deploy`, `delete`, and `create_lambda_functions` methods.This allows us to benefit from test and deployment parallelization, use IDE step-through debugging for a single test, run one, subset, or all tests and only deploy their related infrastructure, without any custom configuration.

Class diagram to understand abstraction built when defining a new stack (

`LoggerStack`)

### Authoring a new feature E2E test[¶](https://docs.aws.amazon.com/powertools/python/latest/maintainers/#authoring-a-new-feature-e2e-test)

Imagine you're going to create E2E for Event Handler feature for the first time. Keep the following mental model when reading:

#### 1. Define infrastructure[¶](https://docs.aws.amazon.com/powertools/python/latest/maintainers/#1-define-infrastructure)

We use CDK as our Infrastructure as Code tool of choice. Before you start using CDK, you'd take the following steps:

- Create `tests/e2e/event_handler/infrastructure.py`file
- Create a new class `EventHandlerStack`and inherit from`BaseInfrastructure`
- Override `create_resources`method and define your infrastructure using CDK
- (Optional) Create a Lambda function under `handlers/alb_handler.py`

Excerpt

`tests/e2e/event_handler/infrastructure.py`

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 | 
 | 

Excerpt

`tests/e2e/event_handler/handlers/alb_handler.py`

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 | 
 | 

#### 2. Deploy/Delete infrastructure when tests run[¶](https://docs.aws.amazon.com/powertools/python/latest/maintainers/#2-deploydelete-infrastructure-when-tests-run)

We need to create a Pytest fixture for our new feature under `tests/e2e/event_handler/conftest.py`.

This will instruct Pytest to deploy our infrastructure when our tests start, and delete it when they complete whether tests are successful or not. Note that this file will not need any modification in the future.

Excerpt

`conftest.py`for Event Handler

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 | 
 | 

#### 3. Access stack outputs for E2E tests[¶](https://docs.aws.amazon.com/powertools/python/latest/maintainers/#3-access-stack-outputs-for-e2e-tests)

Within our tests, we should now have access to the `infrastructure` fixture we defined earlier in `tests/e2e/event_handler/conftest.py`.

We can access any Stack Output using pytest dependency injection.

Excerpt

`tests/e2e/event_handler/test_header_serializer.py`

| 1 2 3 4 5 6 7 8 9 10 11 | 
 | 

### Internals[¶](https://docs.aws.amazon.com/powertools/python/latest/maintainers/#internals)

#### Test runner parallelization[¶](https://docs.aws.amazon.com/powertools/python/latest/maintainers/#test-runner-parallelization)

Besides speed, we parallelize our end-to-end tests to ease asserting async side-effects may take a while per test too, *e.g., traces to become available*.

The following diagram demonstrates the process we take every time you use `make e2e` locally or at CI:

#### CDK CLI parallelization[¶](https://docs.aws.amazon.com/powertools/python/latest/maintainers/#cdk-cli-parallelization)

For CDK CLI to work with [independent CDK Apps](https://docs.aws.amazon.com/cdk/v2/guide/apps.html), we specify an output directory when synthesizing our stack and deploy from said output directory.

We create the typical CDK `app.py` at runtime when tests run, since we know which feature and Python version we're dealing with (locally or at CI).

Excerpt

`cdk_app_V39.py`for Event Handler created at deploy phase

| 1 2 3 4 | 
 | 

When we run E2E tests for a single feature or all of them, our `cdk.out` looks like this:

| 1 2 3 4 5 6 7 | 
 | 

Where:

- `<feature>`- `manifest.json`, our- `cdk_app_<PyVersion>.py`and- `stack_outputs.json`
- `layer_build`
- `layer_build.diff`

Together, all of this allows us to use Pytest like we would for any project, use CDK CLI and its [context methods](https://docs.aws.amazon.com/cdk/v2/guide/context.html#context_methods) (`from_lookup`), and use step-through debugging for a single E2E test without any extra configuration.

NOTE: VSCode doesn't support debugging processes spawning sub-processes (like CDK CLI does w/ shell and CDK App). Maybe

[this works](https://stackoverflow.com/a/65339352). PyCharm works just fine.