# Development environment - Powertools for AWS Lambda (Python)

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/contributing/setup](https://docs.aws.amazon.com/powertools/python/latest/contributing/setup)

---

# Development environment

This page describes how to setup your development environment to contribute to Powertools for AWS Lambda.

*End-to-end process*

## Requirements[¶](https://docs.aws.amazon.com/powertools/python/latest/contributing/setup/#requirements)

First time contributing to an open-source project ever?

Read this [introduction on how to fork and clone a project on GitHub](https://docs.github.com/en/get-started/quickstart/contributing-to-projects).

You'll need the following installed:

- [GitHub account](https://github.com/join). You'll need to be able to fork, clone, and contribute via pull request.
- [Python 3.10+](https://www.python.org/downloads/). Pick any version supported in- [AWS Lambda runtime](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html).
- [Docker](https://docs.docker.com/engine/install/). We use it to run documentation linters and non-Python tooling.
- [Fork the repository](https://github.com/aws-powertools/powertools-lambda-python/fork). You'll work against your fork of this repository.

## Additional requirements if running end-to-end tests

## Local environment[¶](https://docs.aws.amazon.com/powertools/python/latest/contributing/setup/#local-environment)

You can use `make dev` to create a local virtual environment and install all dependencies locally.

Curious about what `make dev` does under the hood?

We use `Make` to [automate common tasks](https://github.com/aws-powertools/powertools-lambda-python/blob/1ebe3275a5c53aed5a8eb76318e7d0af2367edfa/Makefile#L7) locally and in Continuous Integration environments.

## Local documentation[¶](https://docs.aws.amazon.com/powertools/python/latest/contributing/setup/#local-documentation)

You might find useful to run both the documentation website and the API reference locally while contributing:

- **Docs website**:- `make docs-local`- If you prefer using Docker: `make docs-local-docker`
 
- If you prefer using Docker: 
- **API reference**:- `make docs-api-local`