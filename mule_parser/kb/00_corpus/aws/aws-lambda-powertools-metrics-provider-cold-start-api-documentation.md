# aws_lambda_powertools.metrics.provider.cold_start API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/metrics/provider/cold_start.html](https://docs.aws.amazon.com/powertools/python/latest/api/metrics/provider/cold_start.html)

---

# Module `aws_lambda_powertools.metrics.provider.cold_start`

## Functions

- `def reset_cold_start_flag()`
- 
## Expand source code`def reset_cold_start_flag(): global is_cold_start if not is_cold_start: is_cold_start = True`