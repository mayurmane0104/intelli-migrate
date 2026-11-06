# ADR 0006: Sanitize Terraform Resource Identifiers

## Context

Canonical Terraform renderers used the project slug directly as Terraform
resource labels and references. Real Mule/API names often contain hyphens
(`salesforce-account-sapi`), which are safe in AWS names but unsafe in
Terraform dot references such as `aws_apigatewayv2_api.salesforce-account-sapi`.

## Decision

Introduce a deterministic `_tf_identifier(...)` helper in the infrastructure
generator. Terraform-local labels and references now use a lower-snake,
reference-safe identifier, while AWS-facing names continue to preserve the
original project slug.

## Consequences

- Hyphenated project slugs no longer generate broken Terraform references.
- Human-facing AWS resource names remain traceable to the source project slug.
- Regression coverage checks API Gateway and Secrets Manager references for a
  hyphenated API project.
