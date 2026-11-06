# ADR 0009: Fix Infrastructure Generation (Phase 5)

**Date:** 2026-07-09
**Status:** Accepted

## Context

Three systemic defects found in InfrastructureGenerator and surrounding gates:
1. Free-form HCL generation could output Python syntax (triple-quotes, class/def).
2. No HCL syntax gate — Layer 2 skipped .tf files silently.
3. Missing source traceability on every resource block.

## Decision

### 5.2 Replace TODO stubs with STUB comments (valid HCL comments).

### 5.3 Static HCL syntax gate
- post_generation_gates._check_hcl_syntax() — raises PostGenerationGateError on Python syntax in .tf
- validation_pipeline Layer 2 — emits V-INFRA-HCL-SYNTAX findings
- validation_pipeline Layer 4 — detects HCL IAM wildcards (actions = ["*"])

### 5.4 Source traceability annotations
- Every resource block preceded by '# Traced from: <source>' or '# NEW - not present in source'
- post_generation_gates._check_new_infra_labels() — enforces presence of traceability comment

## Regression Tests
- test_infra_s5_terraform_has_no_python_syntax
- test_infra_s5_terraform_resources_are_traced
- test_infra_s5_scheduler_only_emitted_with_evidence
- test_infra_s5_hcl_gate_blocks_python_in_terraform
