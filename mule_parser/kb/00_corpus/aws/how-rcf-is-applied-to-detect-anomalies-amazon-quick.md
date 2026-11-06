# How RCF is applied to detect anomalies - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/how-does-rcf-detect-anomalies.html](https://docs.aws.amazon.com/quick/latest/userguide/how-does-rcf-detect-anomalies.html)

---

A human can easily distinguish a data point that stands out from the rest of the data. RCF does the same thing by building a "forest" of decision trees, and then monitoring how new data points change the forest.

An *anomaly* is a data point that draws your
				attention away from normal points—think of an image of a red flower in a
				field of yellow flowers. This "displacement of attention" is encoded in
				the (expected) position of a tree (that is, a model in RCF) that would be occupied
				by the input point. The idea is to create a forest where each decision tree grows
				out of a partition of the data sampled for training the algorithm. In more technical
				terms, each tree builds a specific type of binary space partitioning tree on the
				samples. As Amazon Quick Sight samples the data, RCF assigns each data point an anomaly score.
				It gives higher scores to data points that look anomalous. The score is, in
				approximation, inversely proportional to the resulting depth of the point in the
				tree. The random cut forest assigns an anomaly score by computing the average score
				from each constituent tree and scaling the result with respect to the sample size. 

The votes or scores of the different models are aggregated because each of the models by itself is a weak predictor. Amazon Quick Sight identifies a data point as anomalous when its score is significantly different from the recent points. What qualifies as an anomaly depends on the application.

The paper [Random Cut
					Forest Based Anomaly Detection On Streams](http://proceedings.mlr.press/v48/guha16.pdf) provides multiple examples of
				this state-of-the-art online anomaly detection (time-series anomaly detection). RCFs
				are used on contiguous segments or “shingles" of data, where the data in the
				immediate segment acts as a context for the most recent one. Previous versions of
				RCF-based anomaly-detection algorithms score an entire shingle. The algorithm in
				Amazon Quick Sight also provides an approximate location of the anomaly in the current extended
				context. This approximate location can be useful in the scenario where there is
				delay in detecting the anomaly. Delays occur because any algorithm needs to
				characterize "previously seen deviations" to "anomalous
				deviations," which can unfold over some time.