# percentileOver - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/percentileOver-function.html](https://docs.aws.amazon.com/quick/latest/userguide/percentileOver-function.html)

---

The `percentileOver` function calculates the *n*th
			percentile of a measure partitioned by a list of dimensions. There are two varieties of
			the `percentileOver` calculation available in Quick:

- 
				[percentileContOver](https://docs.aws.amazon.com/quicksight/latest/user/percentileContOver-function.html)uses linear interpolation to determine result.
- 
				[percentileDiscOver](https://docs.aws.amazon.com/quicksight/latest/user/percentileDiscOver-function.html)uses actual values to determine result.

The `percentileOver` function is an alias of
				`percentileDiscOver`.