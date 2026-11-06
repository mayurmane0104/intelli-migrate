# Troubleshooting - Powertools for AWS Lambda (Python)

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/build_recipes/troubleshooting](https://docs.aws.amazon.com/powertools/python/latest/build_recipes/troubleshooting)

---

We use essential cookies and similar tools that are necessary to provide our site and services. We use performance cookies to collect anonymous statistics, so we can understand how customers use our site and make improvements. Essential cookies cannot be deactivated, but you can choose “Customize” or “Decline” to decline performance cookies.

If you agree, AWS and approved third parties will also use cookies to provide useful site features, remember your preferences, and display relevant content, including relevant advertising. To accept or decline all non-essential cookies, choose “Accept” or “Decline.” To make more detailed choices, choose “Customize.”

Customize cookie preferences

We use cookies and similar tools (collectively, "cookies") for the following purposes.

Essential

Essential cookies are necessary to provide our site and services and cannot be deactivated. They are usually set in response to your actions on the site, such as setting your privacy preferences, signing in, or filling in forms.

Allowed

Performance

Performance cookies provide anonymous statistics about how customers navigate our site so we can improve site experience and performance. Approved third parties may perform analytics on our behalf, but they cannot use the data for their own purposes.

Allowed

Functional

Functional cookies help us provide useful site features, remember your preferences, and display relevant content. Approved third parties may set these cookies to provide certain site features. If you do not allow these cookies, then some or all of these services may not function properly.

Allowed

Advertising

Advertising cookies may be set through our site by us or our advertising partners and help us deliver relevant marketing content. If you do not allow these cookies, you will experience less relevant advertising.

Allowed

Blocking some types of cookies may impact your experience of our sites. You may review and change your choices at any time by selecting Cookie preferences in the footer of this site. We and selected third-parties use cookies or similar technologies as specified in the AWS Cookie Notice.

Your privacy choices

We and our advertising partners (“we”) may use information we collect from or about you to show you ads on other websites and online services. Under certain laws, this activity is referred to as “cross-context behavioral advertising” or “targeted advertising.”

To opt out of our use of cookies or similar technologies to engage in these activities, select “Opt out of cross-context behavioral ads” and “Save preferences” below. If you clear your browser cookies or visit this site from a different device or browser, you will need to make your selection again. For more information about cookies and how we use them, read our Cookie Notice.

To opt out of the use of other identifiers, such as contact information, for these activities, fill out the form here.

For more information about how AWS handles your information, read the AWS Privacy Notice.

Unable to save cookie preferences

We will only store essential cookies at this time, because we were unable to save your cookie preferences.

If you want to change your cookie preferences, try again later using the link in the AWS console footer, or contact support if the problem persists.

This section covers the most frequent issues encountered when building and deploying Lambda functions with Powertools for AWS Lambda (Python). Each issue includes symptoms to help identify the problem and practical solutions with working code examples.

Lambda deployment package too large (>50MB unzipped)

Symptoms:
- RequestEntityTooLargeException during deployment
- Slow cold starts
- High memory usage

Solutions:

1 2 3 4 5 6 7 8 91011121314

#!/bin/bash# 1. Use Lambda Layers for heavy dependencies
pipinstallaws-lambda-powertools[all]-tlayers/powertools/python/
# 2. Remove unnecessary files
findbuild/-name"*.pyc"-delete
findbuild/-name"__pycache__"-typed-execrm-rf{}+
findbuild/-name"tests"-typed-execrm-rf{}+
# 3. Strip debug symbols from compiled libraries
findbuild/-name"*.so"-execstrip--strip-debug{}\;# 4. Use container images for very large packages# Deploy as container image instead of ZIP

Symptoms:
- ModuleNotFoundError: No module named 'aws_lambda_powertools'
- Function fails at runtime with import errors

Solutions:

1 2 3 4 5 6 7 8 9101112

#!/bin/bash# 1. Verify dependencies are in the package
unzip-llambda-package.zip|greppowertools
# 2. Check Python path in Lambda
python-c"import sys; print(sys.path)"# 3. Ensure platform compatibility
pipinstall--platformmanylinux2014_x86_64--only-binary=:all:aws-lambda-powertools[all]# 4. Test imports locallycdbuild&&python-c"from aws_lambda_powertools import Logger; print('OK')"

Architecture mismatch errors

Symptoms:
- ImportError: /lib64/libc.so.6: version GLIBC_2.XX not found
- Compiled extensions fail to load

Solutions:

12345678

#!/bin/bash# Use Docker with Lambda base image
dockerrun--rm-v"$PWD":/var/taskpublic.ecr.aws/lambda/python:3.13\pipinstallaws-lambda-powertools[all]-t/var/task/
# Or force Linux-compatible wheels
pipinstall--platformmanylinux2014_x86_64--implementationcp\--python-version3.13--only-binary=:all:aws-lambda-powertools[all]

Symptoms:
- High initialization duration in CloudWatch logs
- Timeouts on first invocation

Solutions:

1 2 3 4 5 6 7 8 91011121314

#!/bin/bash# 1. Optimize package size (see above)# 2. Use public Powertools for AWS layer# Layer ARN: arn:aws:lambda:{REGION}:017000801446:layer:AWSLambdaPowertoolsPythonV3-python313-x86_64:1# 3. Enable provisioned concurrency for critical functions
awslambdaput-provisioned-concurrency-config\--function-namemy-function\--provisioned-concurrency-configProvisionedConcurrencyCount=10\--region-name{REGION}# 4. Minimize imports in handler# Import only what you need, avoid heavy imports at module level

Symptoms:
- Works locally but fails in CI/CD
- Different behavior between team members

Solutions:

1 2 3 4 5 6 7 8 9101112131415161718

#!/bin/bash# 1. Use lock files for reproducible builds# Poetry: poetry.lock# uv: uv.lock# pip: requirements.txt with pinned versions# 2. Use Docker for consistent build environment
dockerrun--rm-v"$PWD":/app-w/apppython:3.13-slim\bash-c"pip install -r requirements.txt -t build/"# 3. Pin all tool versionspip==24.0
poetry==1.8.0
uv==0.1.0
# 4. Use same Python version everywhere
python-version:'3.13'# In CI/CDpython="^3.13"# In pyproject.toml

Layer compatibility issues

Symptoms:
- Layer not found or incompatible runtime
- Version conflicts between layer and function dependencies

Solutions:

1 2 3 4 5 6 7 8 910111213

#!/bin/bash# 1. Use correct layer ARN for your region and Python version# Check: https://docs.aws.amazon.com/powertools/python/latest/#lambda-layer# 2. Verify layer compatibility
awslambdaget-layer-version\--layer-nameAWSLambdaPowertoolsPythonV3-python313-x86_64\--version-number22\--region-name{REGION}# 3. Avoid version conflicts# Don't include Powertools for AWS in deployment package if using layer
pipinstallpydanticrequests-tbuild/# Exclude powertools