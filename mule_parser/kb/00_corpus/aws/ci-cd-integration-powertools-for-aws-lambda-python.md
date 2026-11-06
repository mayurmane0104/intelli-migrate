# CI/CD Integration - Powertools for AWS Lambda (Python)

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/build_recipes/cicd-integration](https://docs.aws.amazon.com/powertools/python/latest/build_recipes/cicd-integration)

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

Automate your Lambda function builds and deployments using popular CI/CD platforms. These examples show how to build and deploy Lambda functions with Powertools for AWS with proper cross-platform compatibility and deploy them reliably.

GitHub Actions provides a powerful, integrated CI/CD platform that runs directly in your GitHub repository. It offers excellent integration with AWS services, supports matrix builds for testing multiple configurations, and provides a rich ecosystem of pre-built actions.

name:Simple Lambda Deployment from Sourceon:push:branches:[main]env:AWS_REGION:us-east-1jobs:deploy:runs-on:ubuntu-lateststeps:-uses:actions/checkout@08c6903cd8c0fde910a37f88322edcfb5dd907a8# v5.0.0-name:Set up Pythonuses:actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065# v5.6.0with:python-version:'3.13'-name:Install dependenciesrun:|# Simple pip install - the action handles the restpip install --platform manylinux2014_x86_64 --only-binary=:all: \--python-version 3.13 -r requirements.txt -t src-deploy/-name:Configure AWS credentialsuses:aws-actions/configure-aws-credentials@209f2a4450bb4b277e1dedaff40ad2fd8d4d0a4c# v4.3.0with:role-to-assume:${{ secrets.AWS_ROLE_TO_ASSUME }}aws-region:${{ env.AWS_REGION }}-name:Deploy to Lambdauses:aws-actions/aws-lambda-deploy@246115fccc1ad110c97f729696574d09eb5c690dwith:function-name:powertools-simple-functioncode-artifacts-dir:src-deploy/# Deploy from current directoryhandler:app.lambda_handlerruntime:python3.13environment:'{"POWERTOOLS_SERVICE_NAME":"powertools-simple","POWERTOOLS_METRICS_NAMESPACE":"MyApp","POWERTOOLS_LOG_LEVEL":"INFO"}'timeout:30memory-size:512role:${{ secrets.LAMBDA_EXECUTION_ROLE_ARN }}dry-run:false# Set to true for validation without deployment

AWS CodeBuild is a fully managed build service that compiles source code, runs tests, and produces deployment packages. It integrates seamlessly with other AWS services and provides consistent build environments with automatic scaling.