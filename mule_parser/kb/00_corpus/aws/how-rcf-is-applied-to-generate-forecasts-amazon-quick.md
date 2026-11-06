# How RCF is applied to generate forecasts - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/how-does-rcf-generate-forecasts.html](https://docs.aws.amazon.com/quick/latest/userguide/how-does-rcf-generate-forecasts.html)

---

To forecast the next value in a stationary time sequence, the RCF algorithm
				answers the question "What would be the most likely completion, after we have a
				candidate value?" It uses a single tree in RCF to perform a search for the best
				candidate. The candidates across different trees are aggregated, because each tree
				by itself a weak predictor. The aggregation also allows the generation of quantile
				errors. This process is repeated **t** times to predict
				the **t**−th value in the future. 

The algorithm in Amazon Quick Sight is called *BIFOCAL*. It uses two RCFs
				to create a CALibrated BI-FOrest architecture. The first RCF is used to filter out
				anomalies and provide a weak forecast, which is corrected by the second. Overall,
				this approach provides significantly more robust forecasts in comparison to other
				widely available algorithms such as ETS. 

The number of parameters in the Amazon Quick Sight forecasting algorithm is significantly fewer than for other widely available algorithms. This allows it to be useful out of the box, without human adjustment for a larger number of time series data points. As more data accumulates in a particular time series, the forecasts in Amazon Quick Sight can adjust to data drifts and changes of pattern. For time series that show trends, trend detection is performed first to make the series stationary. The forecast of that stationary sequence is projected back with the trend.

Because the algorithm relies on an efficient online algorithm (RCF), it can support interactive "what-if" queries. In these, some of the forecasts can be altered and treated as hypotheticals to provide conditional forecasts. This is the origin of the ability to explore "what-if" scenarios during analysis.