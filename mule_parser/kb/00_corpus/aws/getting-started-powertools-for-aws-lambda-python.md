# Getting Started - Powertools for AWS Lambda (Python)

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/build_recipes/getting-started](https://docs.aws.amazon.com/powertools/python/latest/build_recipes/getting-started)

---

# Getting started

## Prerequisites[¶](https://docs.aws.amazon.com/powertools/python/latest/build_recipes/getting-started/#prerequisites)

Before using any of these recipes, ensure you have:

- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)configured
- Python 3.10+ installed
- Your preferred build tool installed (see individual recipes)

## Choosing the right tool[¶](https://docs.aws.amazon.com/powertools/python/latest/build_recipes/getting-started/#choosing-the-right-tool)

Each build tool has its strengths and is optimized for different use cases. Consider your project complexity, team preferences, and deployment requirements when selecting the best approach.

| Tool | Best for | Considerations | 
|---|---|---|
| [pip](https://docs.aws.amazon.com/powertools/python/latest/build_recipes/build-tools/#pip) | Simple projects, CI/CD | Lightweight, universal | 
| [uv](https://docs.aws.amazon.com/powertools/python/latest/build_recipes/build-tools/#uv) | Fast builds, performance-critical | Extremely fast, Rust-based | 
| [poetry](https://docs.aws.amazon.com/powertools/python/latest/build_recipes/build-tools/#poetry) | Modern Python projects | Excellent dependency management, lock files | 
| [SAM](https://docs.aws.amazon.com/powertools/python/latest/build_recipes/build-tools/#sam) | AWS-native deployments | Integrated with AWS, local testing | 
| [CDK](https://docs.aws.amazon.com/powertools/python/latest/build_recipes/build-tools/#cdk) | Infrastructure as code | Programmatic infrastructure, type safety | 
| [pants](https://docs.aws.amazon.com/powertools/python/latest/build_recipes/build-tools/#pants) | Monorepos, complex projects | Advanced build system, incremental builds | 

## Tip

All examples in this guide are available in the [project repository](https://github.com/aws-powertools/powertools-lambda-python/tree/develop/examples/build_recipes).