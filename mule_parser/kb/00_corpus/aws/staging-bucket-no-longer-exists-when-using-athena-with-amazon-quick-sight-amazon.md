# Staging bucket no longer exists when using Athena with Amazon Quick Sight - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/troubleshoot-athena-missing-bucket.html](https://docs.aws.amazon.com/quick/latest/userguide/troubleshoot-athena-missing-bucket.html)

---

Use this section to help solve this error: "**The staging bucket for this
					query result no longer exists in the underlying data source.**"

 When you create a dataset using Athena, Amazon Quick Sight creates an Amazon S3 bucket. By
				default, this bucket has a name similar to
						"`aws-athena-query-results-`".
				If you remove this bucket, then your next Athena query might fail with an error
				saying the staging bucket no longer exists. `<REGION>`-`<ACCOUNTID>`

To fix this error, create a new bucket with the same name in the correct AWS Region.