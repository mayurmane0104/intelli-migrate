# Automation - Powertools for AWS Lambda (Python)

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/automation](https://docs.aws.amazon.com/powertools/python/latest/automation)

---

# Automation

## Continuous integration practices[¶](https://docs.aws.amazon.com/powertools/python/latest/automation/#continuous-integration-practices)

We adhere to industry recommendations from the [OSSF Scorecard project](https://bestpractices.coreinfrastructure.org/en/criteria), among [others](https://docs.github.com/en/actions/security-guides/security-hardening-for-github-actions).

Since all code changes require a pull request (PR) along with one or more reviewers, we automate quality and security checks **before**, **during**, and **after** a PR is merged to trunk (`develop`).

We use a combination of tools coupled with peer review to increase its compound effect in detecting issues early.

This is a snapshot of our automated checks at a glance.

![Continuous Integration practices](https://docs.aws.amazon.com/powertools/python/latest/media/continuous_integration_practices.png)


### Pre-commit checks[¶](https://docs.aws.amazon.com/powertools/python/latest/automation/#pre-commit-checks)

Pre-commit checks are crucial for a fast feedback loop while ensuring security practices at the individual change level.

To prevent scenarios where these checks are intentionally omitted at the client side, we run at [CI level too](https://docs.aws.amazon.com/powertools/python/latest/automation/#pull-request-checks).

These run locally only for changed files

- **Merge conflict check**
- **Code linting**
- **CloudFormation linting**- `cfn-lint`ensures- [best practices](https://github.com/aws-cloudformation/cfn-lint/blob/86f0370bd43b400ed4c485180dbc2697f73367b2/docs/rules.md)at our documentation examples.
- **Markdown linting**- [industry markdown practices](https://github.com/DavidAnson/markdownlint/blob/d01180ec5a014083ee9d574b693a8d7fbc1e566d/README.md#rules--aliases)at this stage.
- **GitHub Actions linting**- `actionlint`ensures workflows follow- [GitHub Actions security practices](https://docs.github.com/en/actions/security-guides/security-hardening-for-github-actions). It guards against numerous- [leading practices](https://github.com/rhysd/actionlint/blob/main/docs/checks.md)to prevent common configuration mistakes, insecure inline scripts, among many others.
- **Terraform linting**
- **Secrets linting**

### Pre-Pull Request checks[¶](https://docs.aws.amazon.com/powertools/python/latest/automation/#pre-pull-request-checks)

For an improved contributing experience, most of our checks can run locally. For maintainers, this also means increased focus on reviewing actual value instead of standards and security malpractices that can be caught earlier.

These are in addition to [pre-commit checks](https://docs.aws.amazon.com/powertools/python/latest/automation/#pre-commit-checks).

- **Static typing analysis**- `mypy`checks for static typing annotations to prevent common bugs in Python that may or may not lead to abuse.
- **Tests**- `unit`,- `functional`, and- `performance`tests (- *see our definition*
- **Security baseline**- `bandit`detects common security issues defined by Python Code Quality Authority (PyCQA).
- **Complexity baseline**

### Pull Request checks[¶](https://docs.aws.amazon.com/powertools/python/latest/automation/#pull-request-checks)

While we trust contributors and maintainers do go through pre-commit and pre-pull request due diligence, we verify them at CI level.

Checks described earlier are omitted to improve reading experience.

- **Semantic PR title**- `chore(category): change`. This benefits contributors with a lower entry bar, no need for semantic commits. It also benefits everyone looking for an- [useful changelog message](https://docs.aws.amazon.com/powertools/python/latest/changelog/)on- **what**changed and- **where**.
- **Related issue check**- [Every change require an issue](https://github.com/aws-powertools/powertools-lambda-python/blob/0523ff64606514ea3e59c07c8c69c83d751f61fa/CONTRIBUTING.md#contributing-via-pull-requests)describing its needs. This enforces a PR has a related issue by blocking merge operations if missing.
- **Acknowledgment check**- [Ensures PR template](https://github.com/aws-powertools/powertools-lambda-python/blob/0523ff64606514ea3e59c07c8c69c83d751f61fa/.github/PULL_REQUEST_TEMPLATE.md#L36)is used and every contributor is aware of code redistribution.
- **Code coverage diff**
- **Contribution size check**
- **Dependency vulnerability check**
- **GitHub Actions security check**- `actions/checkout@<git-SHA>_`) to prevent abuse. Upgrades are handled by a- [separate automated process](https://github.com/aws-powertools/powertools-lambda-python/blob/0523ff64606514ea3e59c07c8c69c83d751f61fa/.github/dependabot.yml#L4)that includes a maintainer review to also prevent unexpected behavior changes.

### After merge checks[¶](https://docs.aws.amazon.com/powertools/python/latest/automation/#after-merge-checks)

Checks described earlier are omitted to improve reading experience.

We strike a balance in security and contribution experience. These automated checks take several minutes to complete. Failures are reviewed by a maintainer on-call and before a release.

- **End-to-end tests**- [high degree of parallelization](https://github.com/aws-powertools/powertools-lambda-python/blob/0523ff64606514ea3e59c07c8c69c83d751f61fa/MAINTAINERS.md#test-runner-parallelization). While it is designed to also run locally, it may incur AWS charges to contributors. For additional security, all infrastructure is ephemeral per change and per Python version.
- **SAST check**
- **Security posture check**- [OSSF security practices](https://bestpractices.coreinfrastructure.org/en/criteria)are no longer followed.
- **Rebuild Changelog**- [protected branch](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)while keeping removing error-prone tasks from maintainers.
- **Stage documentation**- [staged version](https://docs.aws.amazon.com/powertools/python/stage/). This gives us safety that our docs can always be rebuilt, and ready to release to production when needed.
- **Update draft release**- [Release Drafter](https://github.com/release-drafter/release-drafter)to generate a portion of our release notes and to always keep a fresh draft upon changes. You can read our- [thoughts on a good quality release notes here](https://github.com/aws-powertools/powertools-lambda-python/blob/0523ff64606514ea3e59c07c8c69c83d751f61fa/MAINTAINERS.md#drafting-release-notes)(human readable changes + automation).

## Continuous deployment practices[¶](https://docs.aws.amazon.com/powertools/python/latest/automation/#continuous-deployment-practices)

We adhere to industry recommendations from the [OSSF Scorecard project](https://bestpractices.coreinfrastructure.org/en/criteria), among [others](https://docs.github.com/en/actions/security-guides/security-hardening-for-github-actions).

Releases are triggered by maintainers along with a reviewer - [detailed info here](https://github.com/aws-powertools/powertools-lambda-python/blob/develop/MAINTAINERS.md#releasing-a-new-version). In addition to [checks that run for every code change](https://docs.aws.amazon.com/powertools/python/latest/automation/#continuous-integration-practices), our pipeline requires a manual approval before releasing.

We use a combination of provenance and signed attestation for our builds, source code sealing, SAST scanners, Python specific static code analysis, ephemeral credentials that last a given job step, and more.

This is a snapshot of our automated checks at a glance.

![Continuous Deployment practices](https://docs.aws.amazon.com/powertools/python/latest/media/continuous_deployment_practices.png)


## Lambda layer pipeline[¶](https://docs.aws.amazon.com/powertools/python/latest/automation/#lambda-layer-pipeline)

[Lambda Layer](https://docs.aws.amazon.com/lambda/latest/dg/chapter-layers.html) is a .zip file archive that can contain additional code, pre-packaged dependencies, data, or configuration files. It provides a way to efficiently include libraries and other resources in your Lambda functions, promoting code reusability and reducing deployment package sizes.

To build and deploy the Lambda Layers, we run a pipeline with the following steps:

- We fetch the latest PyPi release and use it as the source for our layer.
- We build Python versions ranging from **10 to 3.14**for x86_64 and arm64 architectures. This is necessary because we use pre-compiled libraries like**Pydantic**and**Cryptography**, which require specific Python versions for each layer.
- We provide layer distributions for both the **x86_64**and**arm64**architectures.
- For each Python version, we create a single CDK package containing both x86_64 and arm64 assets to optimize deployment performance.

Next, we deploy these CDK Assets to the beta account across all AWS regions. Once the beta deployment is complete, we run:

- **Canary Tests**: Run thorough canary tests to assess stability and functionality
- **Successful?**: Deploy previous CDK Asset to production across all regions
- **Failure?**: Halt pipeline to investigate and remediate issues before redeploying