# Metadata - Powertools for AWS Lambda (Python)

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/utilities/metadata](https://docs.aws.amazon.com/powertools/python/latest/utilities/metadata)

---

# Metadata

The Metadata utility allows you to fetch data from the [AWS Lambda Metadata Endpoint (LMDS)](https://docs.aws.amazon.com/lambda/latest/dg/configuration-metadata-endpoint.html). This can be useful for retrieving information about the Lambda execution environment, such as the Availability Zone ID.

## Key features[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/metadata/#key-features)

- Fetch execution environment metadata from the Lambda Metadata Endpoint
- Automatic caching for the duration of the Lambda sandbox
- Graceful fallback to empty metadata outside Lambda (local dev, tests)
- Forward-compatible dataclass that can be extended as new fields are added

## Getting started[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/metadata/#getting-started)

### Usage[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/metadata/#usage)

You can fetch data from the Lambda Metadata Endpoint using the `get_lambda_metadata` function.

## Tip

Metadata is cached for the duration of the Lambda sandbox, so subsequent calls to `get_lambda_metadata` will return the cached data.

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 | 
 | 

You can also fetch metadata eagerly during cold start, so it's ready for subsequent invocations:

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 | 
 | 

### Available metadata[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/metadata/#available-metadata)

| Property | Type | Description | 
|---|---|---|
| `availability_zone_id` | `str`or`None` | The AZ where the function is running (e.g., `use1-az1`) | 

## Testing your code[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/metadata/#testing-your-code)

The metadata endpoint is not available during local development or testing. To ease testing, the `get_lambda_metadata` function automatically detects when it's running in a non-Lambda environment and returns an empty `LambdaMetadata` instance. This allows you to write tests without needing to mock the endpoint.

If you want to mock specific metadata values for testing purposes, you can patch the internal `_fetch_metadata` function and set the required environment variables:

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 | 
 | 

We also expose a `clear_metadata_cache` function that can be used to clear the cached metadata, allowing you to test different metadata values within the same execution context.