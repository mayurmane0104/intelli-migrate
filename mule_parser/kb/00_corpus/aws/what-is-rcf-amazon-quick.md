# What is RCF? - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/what-is-random-cut-forest.html](https://docs.aws.amazon.com/quick/latest/userguide/what-is-random-cut-forest.html)

---

A *random cut forest* (RCF) is a special type of
					*random forest* (RF) algorithm, a widely used
				and successful technique in machine learning. It takes a set of random data points,
				cuts them down to the same number of points, and then builds a collection of models.
				In contrast, a model corresponds to a decision tree—thus the name forest.
				Because RFs can't be easily updated in an incremental manner, RCFs were invented
				with variables in tree construction that were designed to allow incremental updates. 

As an unsupervised algorithm, RCF uses cluster analysis to detect spikes in time series data, breaks in periodicity or seasonality, and data point exceptions. Random cut forests can work as a synopsis or sketch of a dynamic data stream (or a time-indexed sequence of numbers). The answers to our questions about the stream come out of that synopsis. The following characteristics address the stream and how we make connections to anomaly detection and forecasting:

- 
					A *streaming algorithm*is an online algorithm with a small memory footprint. An online algorithm makes its decision about the input point indexed by time**t**before it sees the**(t+1)-**st point. The small memory allows nimble algorithms that can produce answers with low latency and allow a user to interact with the data.
- 
					Respecting the ordering imposed by time, as in an *online*algorithm, is necessary in anomaly detection and forecasting. If we already know what will happen the day after tomorrow, then predicting what happens tomorrow isn't a forecast—it's just interpolating an unknown missing value. Similarly, a new product introduced today can be an anomaly, but it doesn't necessarily remain an anomaly at the end of the next quarter.