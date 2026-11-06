# Performance Optimization - Powertools for AWS Lambda (Python)

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/build_recipes/performance-optimization](https://docs.aws.amazon.com/powertools/python/latest/build_recipes/performance-optimization)

---

# Performance optimization

Optimize your Lambda functions for better performance, reduced cold start times, and lower costs. These techniques help minimize package size, improve startup speed, and reduce memory usage.

Always validate your function's behavior after applying optimizations to ensure an optimization hasn't introduced any issues with your packages. For example, removal of directories that appear to be unnecessary, such as `docs`, can break some libraries.

## Reduce cold start times

- **Minimize package size**by excluding unnecessary files
- **Use compiled dependencies**when possible
- **Leverage Lambda SnapStart**or- **Provisioned concurrency**when possible

## Build optimization