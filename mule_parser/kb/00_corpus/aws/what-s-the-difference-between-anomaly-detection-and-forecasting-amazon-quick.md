# What's the difference between anomaly detection and forecasting? - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/difference-between-anomaly-detection-and-forecasting.html](https://docs.aws.amazon.com/quick/latest/userguide/difference-between-anomaly-detection-and-forecasting.html)

---

Anomaly detection identifies outliers and their contributing drivers to answer the question "What happened that doesn't usually happen?" Forecasting answers the question "If everything continues to happen as expected, what happens in the future?" The math that allows forecasting also enables us to ask "If a few things change, what happens then?"

Both anomaly detection and forecasting begin by examining the current known data points. Amazon Quick Sight anomaly detection begins with what is known so it can establish what is outside the known set, and identify those data points as anomalous (outliers). Amazon Quick Sight forecasting excludes the anomalous data points, and sticks with the known pattern. Forecasting focuses on the established pattern of data distribution. In contrast, anomaly detection focuses on the data points that deviate from what is expected. Each method approaches decision-making from a different direction.