# Installation - Powertools for AWS Lambda (Python)

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/getting-started/install](https://docs.aws.amazon.com/powertools/python/latest/getting-started/install)

---

# Installation

## Package manager[¶](https://docs.aws.amazon.com/powertools/python/latest/getting-started/install/#package-manager)

Most features use Python standard library and the AWS SDK *(boto3)* that are available in the AWS Lambda runtime.

| `1` | 
 | 

| `1` | 
 | 

| `1` | 
 | 

| `1` | 
 | 

### Extra dependencies[¶](https://docs.aws.amazon.com/powertools/python/latest/getting-started/install/#extra-dependencies)

Some features require additional dependencies. Install them as needed:

| Feature | Install | Default dependency | 
|---|---|---|
| [Tracer](https://docs.aws.amazon.com/powertools/python/latest/core/tracer/) | `pip install "aws-lambda-powertools[tracer]"` | `aws-xray-sdk` | 
| [Validation](https://docs.aws.amazon.com/powertools/python/latest/utilities/validation/) | `pip install "aws-lambda-powertools[validation]"` | `fastjsonschema` | 
| [Parser](https://docs.aws.amazon.com/powertools/python/latest/utilities/parser/) | `pip install "aws-lambda-powertools[parser]"` | `pydantic` | 
| [Data Masking](https://docs.aws.amazon.com/powertools/python/latest/utilities/data_masking/) | `pip install "aws-lambda-powertools[datamasking]"` | `aws-encryption-sdk`,`jsonpath-ng` | 
| [Datadog Metrics](https://docs.aws.amazon.com/powertools/python/latest/core/metrics/datadog/) | `pip install "aws-lambda-powertools[datadog]"` | `datadog-lambda` | 
| [Kafka (Avro)](https://docs.aws.amazon.com/powertools/python/latest/utilities/kafka/) | `pip install "aws-lambda-powertools[kafka-consumer-avro]"` | `avro` | 
| [Kafka (Protobuf)](https://docs.aws.amazon.com/powertools/python/latest/utilities/kafka/) | `pip install "aws-lambda-powertools[kafka-consumer-protobuf]"` | `protobuf` | 
| Redis | `pip install "aws-lambda-powertools[redis]"` | `redis` | 
| Valkey | `pip install "aws-lambda-powertools[valkey]"` | `valkey-glide` | 
| All at once | `pip install "aws-lambda-powertools[all]"` | All core extras | 

### Local development[¶](https://docs.aws.amazon.com/powertools/python/latest/getting-started/install/#local-development)

Powertools for AWS Lambda (Python) relies on the AWS SDK bundled in the Lambda runtime. When developing locally, install the SDK as a dev dependency:

| `1` | 
 | 

### Alpha releases[¶](https://docs.aws.amazon.com/powertools/python/latest/getting-started/install/#alpha-releases)

We publish `prerelease` versions to PyPi for early feedback on unstable releases.

| `1` | 
 | 

| `1` | 
 | 

| `1` | 
 | 

## Lambda Layer[¶](https://docs.aws.amazon.com/powertools/python/latest/getting-started/install/#lambda-layer)

[Lambda Layer](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html) is a .zip file archive that contains pre-packaged dependencies. We compile and optimize all dependencies for both x86_64 and ARM architectures.

Replace `{region}` with your AWS region (e.g., `eu-west-1`) and `{python_version}` without the period (e.g., `python313` for Python 3.13).

| Architecture | Layer ARN | 
|---|---|
| x86_64 | `arn:aws:lambda:{region}:017000801446:layer:AWSLambdaPowertoolsPythonV3-{python_version}-x86_64:27` | 
| ARM64 | `arn:aws:lambda:{region}:017000801446:layer:AWSLambdaPowertoolsPythonV3-{python_version}-arm64:27` | 

### All regional Layer ARNs[¶](https://docs.aws.amazon.com/powertools/python/latest/getting-started/install/#all-regional-layer-arns)

## Click to expand and copy any regional Lambda Layer ARN

| Region | Layer ARN | 
|---|---|
| `af-south-1` | arn:aws:lambda:af-south-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python310-x86_64:36 | 
| `ap-east-1` | arn:aws:lambda:ap-east-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python310-x86_64:36 | 
| `ap-northeast-1` | arn:aws:lambda:ap-northeast-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python310-x86_64:36 | 
| `ap-northeast-2` | arn:aws:lambda:ap-northeast-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python310-x86_64:36 | 
| `ap-northeast-3` | arn:aws:lambda:ap-northeast-3:017000801446:layer:AWSLambdaPowertoolsPythonV3-python310-x86_64:36 | 
| `ap-south-1` | arn:aws:lambda:ap-south-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python310-x86_64:36 | 
| `ap-south-2` | arn:aws:lambda:ap-south-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python310-x86_64:36 | 
| `ap-southeast-1` | arn:aws:lambda:ap-southeast-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python310-x86_64:36 | 
| `ap-southeast-2` | arn:aws:lambda:ap-southeast-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python310-x86_64:36 | 
| `ap-southeast-3` | arn:aws:lambda:ap-southeast-3:017000801446:layer:AWSLambdaPowertoolsPythonV3-python310-x86_64:36 | 
| `ap-southeast-4` | arn:aws:lambda:ap-southeast-4:017000801446:layer:AWSLambdaPowertoolsPythonV3-python310-x86_64:36 | 
| `ap-southeast-5` | arn:aws:lambda:ap-southeast-5:017000801446:layer:AWSLambdaPowertoolsPythonV3-python310-x86_64:36 | 
| `ap-southeast-7` | arn:aws:lambda:ap-southeast-7:017000801446:layer:AWSLambdaPowertoolsPythonV3-python310-x86_64:36 | 
| `ca-central-1` | arn:aws:lambda:ca-central-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python310-x86_64:36 | 
| `ca-west-1` | arn:aws:lambda:ca-west-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python310-x86_64:36 | 
| `eu-central-1` | arn:aws:lambda:eu-central-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python310-x86_64:36 | 
| `eu-central-2` | arn:aws:lambda:eu-central-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python310-x86_64:36 | 
| `eu-north-1` | arn:aws:lambda:eu-north-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python310-x86_64:36 | 
| `eu-south-1` | arn:aws:lambda:eu-south-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python310-x86_64:36 | 
| `eu-south-2` | arn:aws:lambda:eu-south-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python310-x86_64:36 | 
| `eu-west-1` | arn:aws:lambda:eu-west-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python310-x86_64:36 | 
| `eu-west-2` | arn:aws:lambda:eu-west-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python310-x86_64:36 | 
| `eu-west-3` | arn:aws:lambda:eu-west-3:017000801446:layer:AWSLambdaPowertoolsPythonV3-python310-x86_64:36 | 
| `il-central-1` | arn:aws:lambda:il-central-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python310-x86_64:36 | 
| `mx-central-1` | arn:aws:lambda:mx-central-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python310-x86_64:36 | 
| `sa-east-1` | arn:aws:lambda:sa-east-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python310-x86_64:36 | 
| `us-east-1` | arn:aws:lambda:us-east-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python310-x86_64:36 | 
| `us-east-2` | arn:aws:lambda:us-east-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python310-x86_64:36 | 
| `us-west-1` | arn:aws:lambda:us-west-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python310-x86_64:36 | 
| `us-west-2` | arn:aws:lambda:us-west-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python310-x86_64:36 | 

| Region | Layer ARN | 
|---|---|
| `af-south-1` | arn:aws:lambda:af-south-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python311-x86_64:36 | 
| `ap-east-1` | arn:aws:lambda:ap-east-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python311-x86_64:36 | 
| `ap-northeast-1` | arn:aws:lambda:ap-northeast-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python311-x86_64:36 | 
| `ap-northeast-2` | arn:aws:lambda:ap-northeast-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python311-x86_64:36 | 
| `ap-northeast-3` | arn:aws:lambda:ap-northeast-3:017000801446:layer:AWSLambdaPowertoolsPythonV3-python311-x86_64:36 | 
| `ap-south-1` | arn:aws:lambda:ap-south-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python311-x86_64:36 | 
| `ap-south-2` | arn:aws:lambda:ap-south-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python311-x86_64:36 | 
| `ap-southeast-1` | arn:aws:lambda:ap-southeast-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python311-x86_64:36 | 
| `ap-southeast-2` | arn:aws:lambda:ap-southeast-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python311-x86_64:36 | 
| `ap-southeast-3` | arn:aws:lambda:ap-southeast-3:017000801446:layer:AWSLambdaPowertoolsPythonV3-python311-x86_64:36 | 
| `ap-southeast-4` | arn:aws:lambda:ap-southeast-4:017000801446:layer:AWSLambdaPowertoolsPythonV3-python311-x86_64:36 | 
| `ap-southeast-5` | arn:aws:lambda:ap-southeast-5:017000801446:layer:AWSLambdaPowertoolsPythonV3-python311-x86_64:36 | 
| `ap-southeast-7` | arn:aws:lambda:ap-southeast-7:017000801446:layer:AWSLambdaPowertoolsPythonV3-python311-x86_64:36 | 
| `ca-central-1` | arn:aws:lambda:ca-central-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python311-x86_64:36 | 
| `ca-west-1` | arn:aws:lambda:ca-west-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python311-x86_64:36 | 
| `eu-central-1` | arn:aws:lambda:eu-central-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python311-x86_64:36 | 
| `eu-central-2` | arn:aws:lambda:eu-central-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python311-x86_64:36 | 
| `eu-north-1` | arn:aws:lambda:eu-north-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python311-x86_64:36 | 
| `eu-south-1` | arn:aws:lambda:eu-south-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python311-x86_64:36 | 
| `eu-south-2` | arn:aws:lambda:eu-south-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python311-x86_64:36 | 
| `eu-west-1` | arn:aws:lambda:eu-west-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python311-x86_64:36 | 
| `eu-west-2` | arn:aws:lambda:eu-west-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python311-x86_64:36 | 
| `eu-west-3` | arn:aws:lambda:eu-west-3:017000801446:layer:AWSLambdaPowertoolsPythonV3-python311-x86_64:36 | 
| `il-central-1` | arn:aws:lambda:il-central-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python311-x86_64:36 | 
| `mx-central-1` | arn:aws:lambda:mx-central-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python311-x86_64:36 | 
| `sa-east-1` | arn:aws:lambda:sa-east-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python311-x86_64:36 | 
| `us-east-1` | arn:aws:lambda:us-east-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python311-x86_64:36 | 
| `us-east-2` | arn:aws:lambda:us-east-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python311-x86_64:36 | 
| `us-west-1` | arn:aws:lambda:us-west-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python311-x86_64:36 | 
| `us-west-2` | arn:aws:lambda:us-west-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python311-x86_64:36 | 

| Region | Layer ARN | 
|---|---|
| `af-south-1` | arn:aws:lambda:af-south-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python312-x86_64:36 | 
| `ap-east-1` | arn:aws:lambda:ap-east-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python312-x86_64:36 | 
| `ap-northeast-1` | arn:aws:lambda:ap-northeast-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python312-x86_64:36 | 
| `ap-northeast-2` | arn:aws:lambda:ap-northeast-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python312-x86_64:36 | 
| `ap-northeast-3` | arn:aws:lambda:ap-northeast-3:017000801446:layer:AWSLambdaPowertoolsPythonV3-python312-x86_64:36 | 
| `ap-south-1` | arn:aws:lambda:ap-south-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python312-x86_64:36 | 
| `ap-south-2` | arn:aws:lambda:ap-south-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python312-x86_64:36 | 
| `ap-southeast-1` | arn:aws:lambda:ap-southeast-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python312-x86_64:36 | 
| `ap-southeast-2` | arn:aws:lambda:ap-southeast-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python312-x86_64:36 | 
| `ap-southeast-3` | arn:aws:lambda:ap-southeast-3:017000801446:layer:AWSLambdaPowertoolsPythonV3-python312-x86_64:36 | 
| `ap-southeast-4` | arn:aws:lambda:ap-southeast-4:017000801446:layer:AWSLambdaPowertoolsPythonV3-python312-x86_64:36 | 
| `ap-southeast-5` | arn:aws:lambda:ap-southeast-5:017000801446:layer:AWSLambdaPowertoolsPythonV3-python312-x86_64:36 | 
| `ap-southeast-7` | arn:aws:lambda:ap-southeast-7:017000801446:layer:AWSLambdaPowertoolsPythonV3-python312-x86_64:36 | 
| `ca-central-1` | arn:aws:lambda:ca-central-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python312-x86_64:36 | 
| `ca-west-1` | arn:aws:lambda:ca-west-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python312-x86_64:36 | 
| `eu-central-1` | arn:aws:lambda:eu-central-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python312-x86_64:36 | 
| `eu-central-2` | arn:aws:lambda:eu-central-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python312-x86_64:36 | 
| `eu-north-1` | arn:aws:lambda:eu-north-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python312-x86_64:36 | 
| `eu-south-1` | arn:aws:lambda:eu-south-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python312-x86_64:36 | 
| `eu-south-2` | arn:aws:lambda:eu-south-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python312-x86_64:36 | 
| `eu-west-1` | arn:aws:lambda:eu-west-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python312-x86_64:36 | 
| `eu-west-2` | arn:aws:lambda:eu-west-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python312-x86_64:36 | 
| `eu-west-3` | arn:aws:lambda:eu-west-3:017000801446:layer:AWSLambdaPowertoolsPythonV3-python312-x86_64:36 | 
| `il-central-1` | arn:aws:lambda:il-central-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python312-x86_64:36 | 
| `mx-central-1` | arn:aws:lambda:mx-central-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python312-x86_64:36 | 
| `sa-east-1` | arn:aws:lambda:sa-east-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python312-x86_64:36 | 
| `us-east-1` | arn:aws:lambda:us-east-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python312-x86_64:36 | 
| `us-east-2` | arn:aws:lambda:us-east-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python312-x86_64:36 | 
| `us-west-1` | arn:aws:lambda:us-west-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python312-x86_64:36 | 
| `us-west-2` | arn:aws:lambda:us-west-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python312-x86_64:36 | 

| Region | Layer ARN | 
|---|---|
| `af-south-1` | arn:aws:lambda:af-south-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python313-x86_64:36 | 
| `ap-east-1` | arn:aws:lambda:ap-east-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python313-x86_64:36 | 
| `ap-northeast-1` | arn:aws:lambda:ap-northeast-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python313-x86_64:36 | 
| `ap-northeast-2` | arn:aws:lambda:ap-northeast-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python313-x86_64:36 | 
| `ap-northeast-3` | arn:aws:lambda:ap-northeast-3:017000801446:layer:AWSLambdaPowertoolsPythonV3-python313-x86_64:36 | 
| `ap-south-1` | arn:aws:lambda:ap-south-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python313-x86_64:36 | 
| `ap-south-2` | arn:aws:lambda:ap-south-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python313-x86_64:36 | 
| `ap-southeast-1` | arn:aws:lambda:ap-southeast-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python313-x86_64:36 | 
| `ap-southeast-2` | arn:aws:lambda:ap-southeast-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python313-x86_64:36 | 
| `ap-southeast-3` | arn:aws:lambda:ap-southeast-3:017000801446:layer:AWSLambdaPowertoolsPythonV3-python313-x86_64:36 | 
| `ap-southeast-4` | arn:aws:lambda:ap-southeast-4:017000801446:layer:AWSLambdaPowertoolsPythonV3-python313-x86_64:36 | 
| `ap-southeast-5` | arn:aws:lambda:ap-southeast-5:017000801446:layer:AWSLambdaPowertoolsPythonV3-python313-x86_64:36 | 
| `ap-southeast-7` | arn:aws:lambda:ap-southeast-7:017000801446:layer:AWSLambdaPowertoolsPythonV3-python313-x86_64:36 | 
| `ca-central-1` | arn:aws:lambda:ca-central-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python313-x86_64:36 | 
| `ca-west-1` | arn:aws:lambda:ca-west-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python313-x86_64:36 | 
| `eu-central-1` | arn:aws:lambda:eu-central-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python313-x86_64:36 | 
| `eu-central-2` | arn:aws:lambda:eu-central-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python313-x86_64:36 | 
| `eu-north-1` | arn:aws:lambda:eu-north-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python313-x86_64:36 | 
| `eu-south-1` | arn:aws:lambda:eu-south-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python313-x86_64:36 | 
| `eu-south-2` | arn:aws:lambda:eu-south-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python313-x86_64:36 | 
| `eu-west-1` | arn:aws:lambda:eu-west-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python313-x86_64:36 | 
| `eu-west-2` | arn:aws:lambda:eu-west-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python313-x86_64:36 | 
| `eu-west-3` | arn:aws:lambda:eu-west-3:017000801446:layer:AWSLambdaPowertoolsPythonV3-python313-x86_64:36 | 
| `il-central-1` | arn:aws:lambda:il-central-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python313-x86_64:36 | 
| `mx-central-1` | arn:aws:lambda:mx-central-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python313-x86_64:36 | 
| `sa-east-1` | arn:aws:lambda:sa-east-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python313-x86_64:36 | 
| `us-east-1` | arn:aws:lambda:us-east-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python313-x86_64:36 | 
| `us-east-2` | arn:aws:lambda:us-east-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python313-x86_64:36 | 
| `us-west-1` | arn:aws:lambda:us-west-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python313-x86_64:36 | 
| `us-west-2` | arn:aws:lambda:us-west-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python313-x86_64:36 | 

| Region | Layer ARN | 
|---|---|
| `af-south-1` | arn:aws:lambda:af-south-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python314-x86_64:36 | 
| `ap-east-1` | arn:aws:lambda:ap-east-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python314-x86_64:36 | 
| `ap-northeast-1` | arn:aws:lambda:ap-northeast-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python314-x86_64:36 | 
| `ap-northeast-2` | arn:aws:lambda:ap-northeast-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python314-x86_64:36 | 
| `ap-northeast-3` | arn:aws:lambda:ap-northeast-3:017000801446:layer:AWSLambdaPowertoolsPythonV3-python314-x86_64:36 | 
| `ap-south-1` | arn:aws:lambda:ap-south-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python314-x86_64:36 | 
| `ap-south-2` | arn:aws:lambda:ap-south-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python314-x86_64:36 | 
| `ap-southeast-1` | arn:aws:lambda:ap-southeast-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python314-x86_64:36 | 
| `ap-southeast-2` | arn:aws:lambda:ap-southeast-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python314-x86_64:36 | 
| `ap-southeast-3` | arn:aws:lambda:ap-southeast-3:017000801446:layer:AWSLambdaPowertoolsPythonV3-python314-x86_64:36 | 
| `ap-southeast-4` | arn:aws:lambda:ap-southeast-4:017000801446:layer:AWSLambdaPowertoolsPythonV3-python314-x86_64:36 | 
| `ap-southeast-5` | arn:aws:lambda:ap-southeast-5:017000801446:layer:AWSLambdaPowertoolsPythonV3-python314-x86_64:36 | 
| `ap-southeast-7` | arn:aws:lambda:ap-southeast-7:017000801446:layer:AWSLambdaPowertoolsPythonV3-python314-x86_64:36 | 
| `ca-central-1` | arn:aws:lambda:ca-central-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python314-x86_64:36 | 
| `ca-west-1` | arn:aws:lambda:ca-west-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python314-x86_64:36 | 
| `eu-central-1` | arn:aws:lambda:eu-central-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python314-x86_64:36 | 
| `eu-central-2` | arn:aws:lambda:eu-central-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python314-x86_64:36 | 
| `eu-north-1` | arn:aws:lambda:eu-north-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python314-x86_64:36 | 
| `eu-south-1` | arn:aws:lambda:eu-south-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python314-x86_64:36 | 
| `eu-south-2` | arn:aws:lambda:eu-south-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python314-x86_64:36 | 
| `eu-west-1` | arn:aws:lambda:eu-west-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python314-x86_64:36 | 
| `eu-west-2` | arn:aws:lambda:eu-west-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python314-x86_64:36 | 
| `eu-west-3` | arn:aws:lambda:eu-west-3:017000801446:layer:AWSLambdaPowertoolsPythonV3-python314-x86_64:36 | 
| `il-central-1` | arn:aws:lambda:il-central-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python314-x86_64:36 | 
| `mx-central-1` | arn:aws:lambda:mx-central-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python314-x86_64:36 | 
| `sa-east-1` | arn:aws:lambda:sa-east-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python314-x86_64:36 | 
| `us-east-1` | arn:aws:lambda:us-east-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python314-x86_64:36 | 
| `us-east-2` | arn:aws:lambda:us-east-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python314-x86_64:36 | 
| `us-west-1` | arn:aws:lambda:us-west-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python314-x86_64:36 | 
| `us-west-2` | arn:aws:lambda:us-west-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python314-x86_64:36 | 

## Click to expand and copy any regional Lambda Layer ARN

| Region | Layer ARN | 
|---|---|
| `af-south-1` | arn:aws:lambda:af-south-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python310-arm64:36 | 
| `ap-east-1` | arn:aws:lambda:ap-east-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python310-arm64:36 | 
| `ap-northeast-1` | arn:aws:lambda:ap-northeast-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python310-arm64:36 | 
| `ap-northeast-2` | arn:aws:lambda:ap-northeast-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python310-arm64:36 | 
| `ap-northeast-3` | arn:aws:lambda:ap-northeast-3:017000801446:layer:AWSLambdaPowertoolsPythonV3-python310-arm64:36 | 
| `ap-south-1` | arn:aws:lambda:ap-south-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python310-arm64:36 | 
| `ap-south-2` | arn:aws:lambda:ap-south-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python310-arm64:36 | 
| `ap-southeast-1` | arn:aws:lambda:ap-southeast-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python310-arm64:36 | 
| `ap-southeast-2` | arn:aws:lambda:ap-southeast-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python310-arm64:36 | 
| `ap-southeast-3` | arn:aws:lambda:ap-southeast-3:017000801446:layer:AWSLambdaPowertoolsPythonV3-python310-arm64:36 | 
| `ap-southeast-4` | arn:aws:lambda:ap-southeast-4:017000801446:layer:AWSLambdaPowertoolsPythonV3-python310-arm64:36 | 
| `ap-southeast-5` | arn:aws:lambda:ap-southeast-5:017000801446:layer:AWSLambdaPowertoolsPythonV3-python310-arm64:36 | 
| `ap-southeast-7` | arn:aws:lambda:ap-southeast-7:017000801446:layer:AWSLambdaPowertoolsPythonV3-python310-arm64:36 | 
| `ca-central-1` | arn:aws:lambda:ca-central-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python310-arm64:36 | 
| `eu-central-1` | arn:aws:lambda:eu-central-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python310-arm64:36 | 
| `eu-central-2` | arn:aws:lambda:eu-central-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python310-arm64:36 | 
| `eu-north-1` | arn:aws:lambda:eu-north-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python310-arm64:36 | 
| `eu-south-1` | arn:aws:lambda:eu-south-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python310-arm64:36 | 
| `eu-south-2` | arn:aws:lambda:eu-south-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python310-arm64:36 | 
| `eu-west-1` | arn:aws:lambda:eu-west-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python310-arm64:36 | 
| `eu-west-2` | arn:aws:lambda:eu-west-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python310-arm64:36 | 
| `eu-west-3` | arn:aws:lambda:eu-west-3:017000801446:layer:AWSLambdaPowertoolsPythonV3-python310-arm64:36 | 
| `il-central-1` | arn:aws:lambda:il-central-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python310-arm64:36 | 
| `mx-central-1` | arn:aws:lambda:mx-central-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python310-arm64:36 | 
| `sa-east-1` | arn:aws:lambda:sa-east-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python310-arm64:36 | 
| `us-east-1` | arn:aws:lambda:us-east-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python310-arm64:36 | 
| `us-east-2` | arn:aws:lambda:us-east-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python310-arm64:36 | 
| `us-west-1` | arn:aws:lambda:us-west-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python310-arm64:36 | 
| `us-west-2` | arn:aws:lambda:us-west-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python310-arm64:36 | 

| Region | Layer ARN | 
|---|---|
| `af-south-1` | arn:aws:lambda:af-south-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python311-arm64:36 | 
| `ap-east-1` | arn:aws:lambda:ap-east-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python311-arm64:36 | 
| `ap-northeast-1` | arn:aws:lambda:ap-northeast-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python311-arm64:36 | 
| `ap-northeast-2` | arn:aws:lambda:ap-northeast-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python311-arm64:36 | 
| `ap-northeast-3` | arn:aws:lambda:ap-northeast-3:017000801446:layer:AWSLambdaPowertoolsPythonV3-python311-arm64:36 | 
| `ap-south-1` | arn:aws:lambda:ap-south-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python311-arm64:36 | 
| `ap-south-2` | arn:aws:lambda:ap-south-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python311-arm64:36 | 
| `ap-southeast-1` | arn:aws:lambda:ap-southeast-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python311-arm64:36 | 
| `ap-southeast-2` | arn:aws:lambda:ap-southeast-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python311-arm64:36 | 
| `ap-southeast-3` | arn:aws:lambda:ap-southeast-3:017000801446:layer:AWSLambdaPowertoolsPythonV3-python311-arm64:36 | 
| `ap-southeast-4` | arn:aws:lambda:ap-southeast-4:017000801446:layer:AWSLambdaPowertoolsPythonV3-python311-arm64:36 | 
| `ap-southeast-5` | arn:aws:lambda:ap-southeast-5:017000801446:layer:AWSLambdaPowertoolsPythonV3-python311-arm64:36 | 
| `ap-southeast-7` | arn:aws:lambda:ap-southeast-7:017000801446:layer:AWSLambdaPowertoolsPythonV3-python311-arm64:36 | 
| `ca-central-1` | arn:aws:lambda:ca-central-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python311-arm64:36 | 
| `eu-central-1` | arn:aws:lambda:eu-central-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python311-arm64:36 | 
| `eu-central-2` | arn:aws:lambda:eu-central-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python311-arm64:36 | 
| `eu-north-1` | arn:aws:lambda:eu-north-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python311-arm64:36 | 
| `eu-south-1` | arn:aws:lambda:eu-south-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python311-arm64:36 | 
| `eu-south-2` | arn:aws:lambda:eu-south-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python311-arm64:36 | 
| `eu-west-1` | arn:aws:lambda:eu-west-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python311-arm64:36 | 
| `eu-west-2` | arn:aws:lambda:eu-west-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python311-arm64:36 | 
| `eu-west-3` | arn:aws:lambda:eu-west-3:017000801446:layer:AWSLambdaPowertoolsPythonV3-python311-arm64:36 | 
| `il-central-1` | arn:aws:lambda:il-central-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python311-arm64:36 | 
| `mx-central-1` | arn:aws:lambda:mx-central-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python311-arm64:36 | 
| `sa-east-1` | arn:aws:lambda:sa-east-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python311-arm64:36 | 
| `us-east-1` | arn:aws:lambda:us-east-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python311-arm64:36 | 
| `us-east-2` | arn:aws:lambda:us-east-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python311-arm64:36 | 
| `us-west-1` | arn:aws:lambda:us-west-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python311-arm64:36 | 
| `us-west-2` | arn:aws:lambda:us-west-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python311-arm64:36 | 

| Region | Layer ARN | 
|---|---|
| `af-south-1` | arn:aws:lambda:af-south-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python312-arm64:36 | 
| `ap-east-1` | arn:aws:lambda:ap-east-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python312-arm64:36 | 
| `ap-northeast-1` | arn:aws:lambda:ap-northeast-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python312-arm64:36 | 
| `ap-northeast-2` | arn:aws:lambda:ap-northeast-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python312-arm64:36 | 
| `ap-northeast-3` | arn:aws:lambda:ap-northeast-3:017000801446:layer:AWSLambdaPowertoolsPythonV3-python312-arm64:36 | 
| `ap-south-1` | arn:aws:lambda:ap-south-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python312-arm64:36 | 
| `ap-south-2` | arn:aws:lambda:ap-south-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python312-arm64:36 | 
| `ap-southeast-1` | arn:aws:lambda:ap-southeast-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python312-arm64:36 | 
| `ap-southeast-2` | arn:aws:lambda:ap-southeast-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python312-arm64:36 | 
| `ap-southeast-3` | arn:aws:lambda:ap-southeast-3:017000801446:layer:AWSLambdaPowertoolsPythonV3-python312-arm64:36 | 
| `ap-southeast-4` | arn:aws:lambda:ap-southeast-4:017000801446:layer:AWSLambdaPowertoolsPythonV3-python312-arm64:36 | 
| `ap-southeast-5` | arn:aws:lambda:ap-southeast-5:017000801446:layer:AWSLambdaPowertoolsPythonV3-python312-arm64:36 | 
| `ap-southeast-7` | arn:aws:lambda:ap-southeast-7:017000801446:layer:AWSLambdaPowertoolsPythonV3-python312-arm64:36 | 
| `ca-central-1` | arn:aws:lambda:ca-central-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python312-arm64:36 | 
| `eu-central-1` | arn:aws:lambda:eu-central-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python312-arm64:36 | 
| `eu-central-2` | arn:aws:lambda:eu-central-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python312-arm64:36 | 
| `eu-north-1` | arn:aws:lambda:eu-north-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python312-arm64:36 | 
| `eu-south-1` | arn:aws:lambda:eu-south-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python312-arm64:36 | 
| `eu-south-2` | arn:aws:lambda:eu-south-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python312-arm64:36 | 
| `eu-west-1` | arn:aws:lambda:eu-west-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python312-arm64:36 | 
| `eu-west-2` | arn:aws:lambda:eu-west-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python312-arm64:36 | 
| `eu-west-3` | arn:aws:lambda:eu-west-3:017000801446:layer:AWSLambdaPowertoolsPythonV3-python312-arm64:36 | 
| `il-central-1` | arn:aws:lambda:il-central-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python312-arm64:36 | 
| `mx-central-1` | arn:aws:lambda:mx-central-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python312-arm64:36 | 
| `sa-east-1` | arn:aws:lambda:sa-east-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python312-arm64:36 | 
| `us-east-1` | arn:aws:lambda:us-east-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python312-arm64:36 | 
| `us-east-2` | arn:aws:lambda:us-east-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python312-arm64:36 | 
| `us-west-1` | arn:aws:lambda:us-west-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python312-arm64:36 | 
| `us-west-2` | arn:aws:lambda:us-west-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python312-arm64:36 | 

| Region | Layer ARN | 
|---|---|
| `af-south-1` | arn:aws:lambda:af-south-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python313-arm64:36 | 
| `ap-east-1` | arn:aws:lambda:ap-east-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python313-arm64:36 | 
| `ap-northeast-1` | arn:aws:lambda:ap-northeast-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python313-arm64:36 | 
| `ap-northeast-2` | arn:aws:lambda:ap-northeast-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python313-arm64:36 | 
| `ap-northeast-3` | arn:aws:lambda:ap-northeast-3:017000801446:layer:AWSLambdaPowertoolsPythonV3-python313-arm64:36 | 
| `ap-south-1` | arn:aws:lambda:ap-south-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python313-arm64:36 | 
| `ap-south-2` | arn:aws:lambda:ap-south-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python313-arm64:36 | 
| `ap-southeast-1` | arn:aws:lambda:ap-southeast-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python313-arm64:36 | 
| `ap-southeast-2` | arn:aws:lambda:ap-southeast-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python313-arm64:36 | 
| `ap-southeast-3` | arn:aws:lambda:ap-southeast-3:017000801446:layer:AWSLambdaPowertoolsPythonV3-python313-arm64:36 | 
| `ap-southeast-4` | arn:aws:lambda:ap-southeast-4:017000801446:layer:AWSLambdaPowertoolsPythonV3-python313-arm64:36 | 
| `ap-southeast-5` | arn:aws:lambda:ap-southeast-5:017000801446:layer:AWSLambdaPowertoolsPythonV3-python313-arm64:36 | 
| `ap-southeast-7` | arn:aws:lambda:ap-southeast-7:017000801446:layer:AWSLambdaPowertoolsPythonV3-python313-arm64:36 | 
| `ca-central-1` | arn:aws:lambda:ca-central-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python313-arm64:36 | 
| `eu-central-1` | arn:aws:lambda:eu-central-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python313-arm64:36 | 
| `eu-central-2` | arn:aws:lambda:eu-central-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python313-arm64:36 | 
| `eu-north-1` | arn:aws:lambda:eu-north-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python313-arm64:36 | 
| `eu-south-1` | arn:aws:lambda:eu-south-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python313-arm64:36 | 
| `eu-south-2` | arn:aws:lambda:eu-south-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python313-arm64:36 | 
| `eu-west-1` | arn:aws:lambda:eu-west-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python313-arm64:36 | 
| `eu-west-2` | arn:aws:lambda:eu-west-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python313-arm64:36 | 
| `eu-west-3` | arn:aws:lambda:eu-west-3:017000801446:layer:AWSLambdaPowertoolsPythonV3-python313-arm64:36 | 
| `il-central-1` | arn:aws:lambda:il-central-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python313-arm64:36 | 
| `mx-central-1` | arn:aws:lambda:mx-central-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python313-arm64:36 | 
| `sa-east-1` | arn:aws:lambda:sa-east-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python313-arm64:36 | 
| `us-east-1` | arn:aws:lambda:us-east-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python313-arm64:36 | 
| `us-east-2` | arn:aws:lambda:us-east-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python313-arm64:36 | 
| `us-west-1` | arn:aws:lambda:us-west-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python313-arm64:36 | 
| `us-west-2` | arn:aws:lambda:us-west-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python313-arm64:36 | 

| Region | Layer ARN | 
|---|---|
| `af-south-1` | arn:aws:lambda:af-south-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python314-arm64:36 | 
| `ap-east-1` | arn:aws:lambda:ap-east-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python314-arm64:36 | 
| `ap-northeast-1` | arn:aws:lambda:ap-northeast-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python314-arm64:36 | 
| `ap-northeast-2` | arn:aws:lambda:ap-northeast-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python314-arm64:36 | 
| `ap-northeast-3` | arn:aws:lambda:ap-northeast-3:017000801446:layer:AWSLambdaPowertoolsPythonV3-python314-arm64:36 | 
| `ap-south-1` | arn:aws:lambda:ap-south-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python314-arm64:36 | 
| `ap-south-2` | arn:aws:lambda:ap-south-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python314-arm64:36 | 
| `ap-southeast-1` | arn:aws:lambda:ap-southeast-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python314-arm64:36 | 
| `ap-southeast-2` | arn:aws:lambda:ap-southeast-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python314-arm64:36 | 
| `ap-southeast-3` | arn:aws:lambda:ap-southeast-3:017000801446:layer:AWSLambdaPowertoolsPythonV3-python314-arm64:36 | 
| `ap-southeast-4` | arn:aws:lambda:ap-southeast-4:017000801446:layer:AWSLambdaPowertoolsPythonV3-python314-arm64:36 | 
| `ap-southeast-5` | arn:aws:lambda:ap-southeast-5:017000801446:layer:AWSLambdaPowertoolsPythonV3-python314-arm64:36 | 
| `ap-southeast-7` | arn:aws:lambda:ap-southeast-7:017000801446:layer:AWSLambdaPowertoolsPythonV3-python314-arm64:36 | 
| `ca-central-1` | arn:aws:lambda:ca-central-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python314-arm64:36 | 
| `eu-central-1` | arn:aws:lambda:eu-central-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python314-arm64:36 | 
| `eu-central-2` | arn:aws:lambda:eu-central-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python314-arm64:36 | 
| `eu-north-1` | arn:aws:lambda:eu-north-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python314-arm64:36 | 
| `eu-south-1` | arn:aws:lambda:eu-south-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python314-arm64:36 | 
| `eu-south-2` | arn:aws:lambda:eu-south-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python314-arm64:36 | 
| `eu-west-1` | arn:aws:lambda:eu-west-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python314-arm64:36 | 
| `eu-west-2` | arn:aws:lambda:eu-west-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python314-arm64:36 | 
| `eu-west-3` | arn:aws:lambda:eu-west-3:017000801446:layer:AWSLambdaPowertoolsPythonV3-python314-arm64:36 | 
| `il-central-1` | arn:aws:lambda:il-central-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python314-arm64:36 | 
| `mx-central-1` | arn:aws:lambda:mx-central-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python314-arm64:36 | 
| `sa-east-1` | arn:aws:lambda:sa-east-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python314-arm64:36 | 
| `us-east-1` | arn:aws:lambda:us-east-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python314-arm64:36 | 
| `us-east-2` | arn:aws:lambda:us-east-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python314-arm64:36 | 
| `us-west-1` | arn:aws:lambda:us-west-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python314-arm64:36 | 
| `us-west-2` | arn:aws:lambda:us-west-2:017000801446:layer:AWSLambdaPowertoolsPythonV3-python314-arm64:36 | 

## Want to inspect the Layer contents?

| `1` | 
 | 

`Location` key.
### Using SSM Parameter Store[¶](https://docs.aws.amazon.com/powertools/python/latest/getting-started/install/#using-ssm-parameter-store)

We publish Layer ARNs to SSM Parameter Store for easier automation:

| 1 2 3 4 5 | 
 | 

| 1 2 3 4 5 6 7 | 
 | 

### Infrastructure as Code examples[¶](https://docs.aws.amazon.com/powertools/python/latest/getting-started/install/#infrastructure-as-code-examples)

| 1 2 3 4 5 6 7 8 9 10 11 | 
 | 

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 | 
 | 

| 1 2 3 4 5 6 7 8 9 10 11 12 13 | 
 | 

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 | 
 | 

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 | 
 | 

### AWS China regions[¶](https://docs.aws.amazon.com/powertools/python/latest/getting-started/install/#aws-china-regions)

| Region | Architecture | Layer ARN | 
|---|---|---|
| cn-north-1 | x86_64 | `arn:aws-cn:lambda:cn-north-1:498634801083:layer:AWSLambdaPowertoolsPythonV3-{python_version}-x86_64:27` | 
| cn-north-1 | ARM64 | `arn:aws-cn:lambda:cn-north-1:498634801083:layer:AWSLambdaPowertoolsPythonV3-{python_version}-arm64:27` | 

### AWS GovCloud regions[¶](https://docs.aws.amazon.com/powertools/python/latest/getting-started/install/#aws-govcloud-regions)

| Region | Architecture | Layer ARN | 
|---|---|---|
| us-gov-east-1 | x86_64 | `arn:aws-us-gov:lambda:us-gov-east-1:165087284144:layer:AWSLambdaPowertoolsPythonV3-{python_version}-x86_64:27` | 
| us-gov-east-1 | ARM64 | `arn:aws-us-gov:lambda:us-gov-east-1:165087284144:layer:AWSLambdaPowertoolsPythonV3-{python_version}-arm64:27` | 
| us-gov-west-1 | x86_64 | `arn:aws-us-gov:lambda:us-gov-west-1:165093116878:layer:AWSLambdaPowertoolsPythonV3-{python_version}-x86_64:27` | 
| us-gov-west-1 | ARM64 | `arn:aws-us-gov:lambda:us-gov-west-1:165093116878:layer:AWSLambdaPowertoolsPythonV3-{python_version}-arm64:27` | 

## Serverless Application Repository (SAR)[¶](https://docs.aws.amazon.com/powertools/python/latest/getting-started/install/#serverless-application-repository-sar)

SAR deploys a CloudFormation stack with a copy of our Lambda Layer in your account. This allows you to use semantic versioning.

| Python | Architecture | SAR App | 
|---|---|---|
| 3.10 | x86_64 | [aws-lambda-powertools-python-layer-v3-python310-x86-64](https://serverlessrepo.aws.amazon.com/applications/eu-west-1/057560766410/aws-lambda-powertools-python-layer-v3-python310-x86-64) | 
| 3.11 | x86_64 | [aws-lambda-powertools-python-layer-v3-python311-x86-64](https://serverlessrepo.aws.amazon.com/applications/eu-west-1/057560766410/aws-lambda-powertools-python-layer-v3-python311-x86-64) | 
| 3.12 | x86_64 | [aws-lambda-powertools-python-layer-v3-python312-x86-64](https://serverlessrepo.aws.amazon.com/applications/eu-west-1/057560766410/aws-lambda-powertools-python-layer-v3-python312-x86-64) | 
| 3.13 | x86_64 | [aws-lambda-powertools-python-layer-v3-python313-x86-64](https://serverlessrepo.aws.amazon.com/applications/eu-west-1/057560766410/aws-lambda-powertools-python-layer-v3-python313-x86-64) | 
| 3.14 | x86_64 | [aws-lambda-powertools-python-layer-v3-python314-x86-64](https://serverlessrepo.aws.amazon.com/applications/eu-west-1/057560766410/aws-lambda-powertools-python-layer-v3-python314-x86-64) | 
| 3.10 | ARM64 | [aws-lambda-powertools-python-layer-v3-python310-arm64](https://serverlessrepo.aws.amazon.com/applications/eu-west-1/057560766410/aws-lambda-powertools-python-layer-v3-python310-arm64) | 
| 3.11 | ARM64 | [aws-lambda-powertools-python-layer-v3-python311-arm64](https://serverlessrepo.aws.amazon.com/applications/eu-west-1/057560766410/aws-lambda-powertools-python-layer-v3-python311-arm64) | 
| 3.12 | ARM64 | [aws-lambda-powertools-python-layer-v3-python312-arm64](https://serverlessrepo.aws.amazon.com/applications/eu-west-1/057560766410/aws-lambda-powertools-python-layer-v3-python312-arm64) | 
| 3.13 | ARM64 | [aws-lambda-powertools-python-layer-v3-python313-arm64](https://serverlessrepo.aws.amazon.com/applications/eu-west-1/057560766410/aws-lambda-powertools-python-layer-v3-python313-arm64) | 
| 3.14 | ARM64 | [aws-lambda-powertools-python-layer-v3-python314-arm64](https://serverlessrepo.aws.amazon.com/applications/eu-west-1/057560766410/aws-lambda-powertools-python-layer-v3-python314-arm64) | 

## SAR Infrastructure as Code examples

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 | 
 | 

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 | 
 | 

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 | 
 | 

## Need least-privilege IAM permissions?

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 | 
 |