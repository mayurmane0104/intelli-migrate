# Dataset requirements for using ML insights with Amazon Quick Sight - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/ml-data-set-requirements.html](https://docs.aws.amazon.com/quick/latest/userguide/ml-data-set-requirements.html)

---

To begin using the machine learning capabilities of Amazon Quick Sight, you need to connect to or import your data. You can use an existing Amazon Quick Sight dataset or create a new one. You can directly query your SQL-compatible source, or ingest the data into SPICE.

The data must have the following properties:

- 
				At least one metric (for example, sales, orders, shipped units, sign ups, and so on). 
- 
				At least one category dimension (for example, product category, channel, segment, industry, and so on). Categories with NULL values are ignored. 
- 
				Anomaly detection requires a minimum of 15 data points for training. For example, if the grain of your data is daily, you need at least 15 days of data. If the grain is monthly, you need at least 15 months of data. 
- 
				Forecasting work best with more data. Make sure that your dataset has enough historical data for optimal results. For example, if the grain of your data is daily, you need at least 38 days of data. If the grain is monthly, you need at least 43 months of data. Following are the requirements for each time grain: - 
						Years: 32 data points 
- 
						Quarters: 35 data points 
- 
						Months: 43 data points 
- 
						Weeks: 35 data points 
- 
						Days: 38 data points 
- 
						Hours: 39 data points 
- 
						Minutes: 46 data points 
- 
						Seconds: 46 data points 
 
- 
						
- 
				If you want to analyze anomalies or forecasts, you also need at least one date dimension. 

If you don't have a dataset to get started, you can download this sample dataset:
				[ML Insights Sample Dataset VI](samples/ml-insights.csv.zip).
			After you have a dataset ready, create a new analysis from the dataset.