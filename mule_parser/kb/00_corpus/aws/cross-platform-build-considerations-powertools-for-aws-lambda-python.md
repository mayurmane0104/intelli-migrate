# Cross-Platform Build Considerations - Powertools for AWS Lambda (Python)

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/build_recipes/cross-platform](https://docs.aws.amazon.com/powertools/python/latest/build_recipes/cross-platform)

---

# Cross-platform builds

Many modern Python packages include compiled extensions written in Rust or C/C++ for performance reasons. These compiled components are platform-specific and can cause deployment issues when building on different architectures.

## Architecture Mismatch Issues

Building AWS Lambda packages on macOS (ARM64/Intel) for deployment on AWS Lambda (Linux x86_64 or ARM64) will result in incompatible binary dependencies that cause import errors at runtime.

## Common compiled libraries[¶](https://docs.aws.amazon.com/powertools/python/latest/build_recipes/cross-platform/#common-compiled-libraries)

Taking into consideration Powertools for AWS dependencies and common Python packages, these libraries include compiled Rust/C components that require architecture-specific builds:

| Library | Language | Components | Impact | Used in Powertools for AWS | 
|---|---|---|---|---|
| pydantic | Rust | Core validation engine | High - Core functionality affected | ✅ Core dependency | 
| aws-encryption-sdk | C | Encryption/decryption | High - Data masking fails | ✅ Optional (datamasking extra) | 
| protobuf | C++ | Protocol buffer serialization | High - Message parsing fails | ✅ Optional (kafka-consumer-protobuf) | 
| redis | C | Redis client with hiredis | Medium - Falls back to pure Python | ✅ Optional (redis extra) | 
| valkey-glide | Rust | High-performance Redis client | High - Client completely broken | ✅ Optional (valkey extra) | 
| orjson | Rust | JSON serialization | Medium - Performance degradation | ❌ Not used (but common) | 
| uvloop | C | Event loop implementation | Medium - Falls back to asyncio | ❌ Not used (but common) | 
| lxml | C | XML/HTML processing | High - XML parsing fails | ❌ Not used (but common) | 

## Powertools extras dependencies and architecture[¶](https://docs.aws.amazon.com/powertools/python/latest/build_recipes/cross-platform/#powertools-extras-dependencies-and-architecture)

Different Powertools for AWS extras dependencies have varying levels of architecture dependency:

| requirements.txt - Safe for any platform | |
|---|---|
| 1 2 3 4 5 6 | 
 | 

| requirements.txt - Requires Linux builds | |
|---|---|
| 1 2 3 4 5 6 7 8 | 
 | 

| requirements.txt - Requires careful platform handling | |
|---|---|
| 1 2 3 | 
 | 

## Powertools for AWS build strategy

- **Use**for maximum compatibility- `[all]`extra with Docker builds
- **Use specific extras**if you want to avoid certain compiled dependencies
- **Test imports**after building to catch architecture mismatches early

## Understanding Python wheels[¶](https://docs.aws.amazon.com/powertools/python/latest/build_recipes/cross-platform/#understanding-python-wheels)

Python wheels are binary distribution packages that include compiled extensions. Lambda requires specific wheel types based on the target runtime architecture and GLIBC version.

### Wheel naming convention[¶](https://docs.aws.amazon.com/powertools/python/latest/build_recipes/cross-platform/#wheel-naming-convention)

Wheels follow a specific naming pattern that indicates compatibility:

| `1` | 
 | 

**Example breakdown:**

| 1 2 3 4 5 6 | 
 | 

### Platform tags and Lambda compatibility[¶](https://docs.aws.amazon.com/powertools/python/latest/build_recipes/cross-platform/#platform-tags-and-lambda-compatibility)

| Platform Tag | Description | Lambda Compatibility | 
|---|---|---|
| `linux_x86_64` | Linux 64-bit Intel/AMD | ✅ Lambda x86_64 | 
| `linux_aarch64` | Linux 64-bit ARM | ✅ Lambda arm64 | 
| `macosx_*` | macOS (any version) | ❌ Not compatible | 
| `win_*` | Windows (any version) | ❌ Not compatible | 
| `any` | Pure Python, no compiled code | ✅ All platforms | 

### Source distributions vs wheels[¶](https://docs.aws.amazon.com/powertools/python/latest/build_recipes/cross-platform/#source-distributions-vs-wheels)

| Package Type | Extension | Compilation | Lambda Recommendation | 
|---|---|---|---|
| Wheel | `.whl` | Pre-compiled | ✅ Preferred - faster, consistent | 
| Source Distribution | `.tar.gz` | Compile during install | ❌ Avoid - platform-dependent compilation | 

**Why wheels matter for Lambda:**

- **Consistent builds**- Same binary across environments
- **Faster installs**- No compilation step required
- **Predictable dependencies**- Known system library requirements
- **Architecture safety**- Platform-specific binaries

## Lambda runtime environments[¶](https://docs.aws.amazon.com/powertools/python/latest/build_recipes/cross-platform/#lambda-runtime-environments)

Lambda managed runtimes use [specific Amazon Linux versions](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtimes-supported) versions with fixed GLIBC versions. Packages built on development machines with newer GLIBC versions will fail at runtime with import errors. Each Python runtime version corresponds to a specific Amazon Linux base system that determines compatible system library versions.

### Amazon Linux versions and GLIBC compatibility[¶](https://docs.aws.amazon.com/powertools/python/latest/build_recipes/cross-platform/#amazon-linux-versions-and-glibc-compatibility)

| Python Runtime | Base System | GLIBC Version | Architecture Support | 
|---|---|---|---|
| python3.10 | Amazon Linux 2 | 2.26 | x86_64, arm64 | 
| python3.11 | Amazon Linux 2 | 2.26 | x86_64, arm64 | 
| python3.12 | Amazon Linux 2023 | 2.34 | x86_64, arm64 | 
| python3.13 | Amazon Linux 2023 | 2.34 | x86_64, arm64 | 
| python3.14 | Amazon Linux 2023 | 2.34 | x86_64, arm64 | 

## GLIBC Version Mismatch

Compiled libraries built on systems with newer GLIBC versions will fail on Lambda runtimes with older GLIBC versions. Ubuntu 24.04 (GLIBC 2.39) and Ubuntu 22.04 (GLIBC 2.35) are incompatible with Lambda python3.11 and earlier (GLIBC 2.26). Always use `--platform` flags or Docker with Lambda base images.

### Manylinux compatibility tags[¶](https://docs.aws.amazon.com/powertools/python/latest/build_recipes/cross-platform/#manylinux-compatibility-tags)

Python wheels use manylinux tags to indicate GLIBC compatibility. Understanding these tags helps you choose the right wheels for Lambda:

| manylinux Tag | GLIBC Version | Lambda Compatibility | Recommendation | 
|---|---|---|---|
| manylinux1 | 2.5 | ✅ All runtimes | Legacy, limited package support | 
| manylinux2010 | 2.12 | ✅ All runtimes | Good compatibility | 
| manylinux2014 | 2.17 | ✅ All runtimes | Recommended for most packages | 
| manylinux_2_17 | 2.17 | ✅ All runtimes | Modern standard | 
| manylinux_2_24 | 2.24 | ✅ All runtimes | Good for newer packages | 
| manylinux_2_28 | 2.28 | ✅ python3.12+, ❌ python3.11- | Use with caution | 
| manylinux_2_34 | 2.34 | ✅ python3.12+, ❌ python3.11- | AL2023 only | 

## Runtime-specific considerations[¶](https://docs.aws.amazon.com/powertools/python/latest/build_recipes/cross-platform/#runtime-specific-considerations)

### Amazon Linux 2 (python3.8 - python3.11)[¶](https://docs.aws.amazon.com/powertools/python/latest/build_recipes/cross-platform/#amazon-linux-2-python38-python311)

Amazon Linux 2 is based on RHEL 7 and uses an older GLIBC version (2.26). This provides broad compatibility but may limit access to newer compiled features.

**Characteristics:**

- **GLIBC 2.26**- Compatible with most manylinux wheels
- **OpenSSL 1.0.2**- Legacy TLS support

**Best practices:**

| 1 2 3 4 5 | 
 | 

### Amazon Linux 2023 (python3.12+)[¶](https://docs.aws.amazon.com/powertools/python/latest/build_recipes/cross-platform/#amazon-linux-2023-python312)

Amazon Linux 2023 is a modern, minimal Linux distribution with updated system libraries and better security.

**Characteristics:**

- **GLIBC 2.34**- Supports newer compiled libraries
- **OpenSSL 3.0**- Latest TLS and cryptographic features
- **Smaller footprint**- Optimized for containers and serverless

**Migration considerations:**

| 1 2 3 4 5 6 7 8 9 | 
 | 

## Multi-platform build strategies[¶](https://docs.aws.amazon.com/powertools/python/latest/build_recipes/cross-platform/#multi-platform-build-strategies)

Use AWS Lambda base images to ensure Linux x86_64 or ARM64 compatibility:

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 | 
 | 

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 | 
 | 

Force installation of Linux-compatible wheels:

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 | 
 | 

Use GitHub Actions with Linux runners for consistent builds:

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 | 
 | 

## Debugging compatibility issues[¶](https://docs.aws.amazon.com/powertools/python/latest/build_recipes/cross-platform/#debugging-compatibility-issues)

When you encounter runtime errors related to compiled dependencies, use these techniques to diagnose and fix the issues:

### Common error patterns[¶](https://docs.aws.amazon.com/powertools/python/latest/build_recipes/cross-platform/#common-error-patterns)

| 1 2 3 4 5 6 7 8 9 10 11 12 13 | 
 | 

| 1 2 3 4 5 6 7 8 9 10 11 12 | 
 | 

| 1 2 3 4 5 6 7 8 9 | 
 | 

## Best practices for cross-platform builds[¶](https://docs.aws.amazon.com/powertools/python/latest/build_recipes/cross-platform/#best-practices-for-cross-platform-builds)

## Development Workflow

Develop locally on your preferred platform, but always build deployment packages in a Linux environment or Docker container to ensure compatibility.

- **Always build on Linux**for Lambda deployments, or use Docker with Lambda base images
- **Use**when installing with pip to force Linux-compatible wheels- `--platform`flags
- **Test imports**in your build environment before deployment
- **Pin dependency versions**to ensure reproducible builds across platforms
- **Use CI/CD with Linux runners**to avoid local architecture issues
- **Consider Lambda container images**for complex dependency scenarios