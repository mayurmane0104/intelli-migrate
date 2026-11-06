# Build Recipes - Powertools for AWS Lambda (Python)

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/build_recipes](https://docs.aws.amazon.com/powertools/python/latest/build_recipes)

---

# Build Recipes

As the Python ecosystem continues to evolve with new package managers, build tools, and dependency resolution strategies, choosing the right approach for Lambda deployments has become increasingly complex. Modern Python applications often involve compiled extensions, platform-specific dependencies, and sophisticated toolchains that require careful consideration for serverless environments.

This guide provides practical recipes for packaging Lambda functions with Powertools for AWS Lambda (Python) using different build tools and dependency managers.

## Key benefits[¶](https://docs.aws.amazon.com/powertools/python/latest/build_recipes/#key-benefits)

- **Optimized packaging**- Reduce deployment package size and cold start times
- **Dependency management**- Handle complex dependency trees efficiently
- **Build reproducibility**- Consistent builds across environments
- **Layer optimization**- Leverage Lambda Layers for better performance
- **Multi-tool support**- Choose the right tool for your workflow

## Terminology[¶](https://docs.aws.amazon.com/powertools/python/latest/build_recipes/#terminology)

Understanding these key terms will help you navigate the build recipes more effectively:

| Term | Definition | 
|---|---|
| Deployment Package | A ZIP archive or container image containing your Lambda function code and all its dependencies, ready for deployment to AWS Lambda | 
| Lambda Layer | A ZIP archive containing libraries, custom runtimes, or other function dependencies that can be shared across multiple Lambda functions | 
| Build Tool | Software that automates the process of compiling, packaging, and preparing your code for deployment (e.g., pip, poetry, uv, pants) | 
| Dependency Manager | Tool responsible for resolving, downloading, and managing external libraries your project depends on | 
| Lock File | A file that records the exact versions of all dependencies used in your project, ensuring reproducible builds (e.g., poetry.lock, uv.lock) | 
| Cold Start | The initialization time when AWS Lambda creates a new execution environment for your function, including loading your deployment package | 
| SAM (Serverless Application Model) | AWS framework for building serverless applications, providing templates and CLI tools for deploying Lambda functions and related resources | 
| CDK (Cloud Development Kit) | AWS framework for defining cloud infrastructure using familiar programming languages, enabling infrastructure as code for Lambda deployments | 

## Guide sections[¶](https://docs.aws.amazon.com/powertools/python/latest/build_recipes/#guide-sections)

This guide is organized into focused sections to help you find exactly what you need:

### 📚 Fundamentals[¶](https://docs.aws.amazon.com/powertools/python/latest/build_recipes/#fundamentals)

- [Getting started](https://docs.aws.amazon.com/powertools/python/latest/build_recipes/getting-started/)
- [Cross-platform builds](https://docs.aws.amazon.com/powertools/python/latest/build_recipes/cross-platform/)

### 🔧 Build tools[¶](https://docs.aws.amazon.com/powertools/python/latest/build_recipes/#build-tools)

- [Build with pip](https://docs.aws.amazon.com/powertools/python/latest/build_recipes/build-tools/#pip)
- [Build with uv](https://docs.aws.amazon.com/powertools/python/latest/build_recipes/build-tools/#uv)
- [Build with Poetry](https://docs.aws.amazon.com/powertools/python/latest/build_recipes/build-tools/#poetry)
- [Build with SAM](https://docs.aws.amazon.com/powertools/python/latest/build_recipes/build-tools/#sam)
- [Build with CDK](https://docs.aws.amazon.com/powertools/python/latest/build_recipes/build-tools/#cdk)
- [Build with Pants](https://docs.aws.amazon.com/powertools/python/latest/build_recipes/build-tools/#pants)

### ⚡ Advanced topics[¶](https://docs.aws.amazon.com/powertools/python/latest/build_recipes/#advanced-topics)

- [Performance optimization](https://docs.aws.amazon.com/powertools/python/latest/build_recipes/performance-optimization/)
- [CI/CD integration](https://docs.aws.amazon.com/powertools/python/latest/build_recipes/cicd-integration/)
- [Troubleshooting](https://docs.aws.amazon.com/powertools/python/latest/build_recipes/troubleshooting/)