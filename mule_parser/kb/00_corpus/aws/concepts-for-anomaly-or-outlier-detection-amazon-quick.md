# Concepts for anomaly or outlier detection - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/anomaly-detection-outliers-and-key-drivers.html](https://docs.aws.amazon.com/quick/latest/userguide/anomaly-detection-outliers-and-key-drivers.html)

---

Amazon Quick Sight uses the word *anomaly* to describe data
				points that fall outside an overall pattern of distribution. There are many other
				words for anomalies, which is a scientific term, including outliers, deviations,
				oddities, exceptions, irregularities, quirks, and many more. The term that you use
				might be based on the type of analysis you do, or the type of data you use, or even
				just the preference of your group. These outlying data points represent an
				entity—a person, place, thing, or time—which is exceptional in some
				way. 

Humans easily recognize patterns and spot things that aren't like the others. Our senses provide this information for us. If the pattern is simple, and there is only a little data, you can easily make a graph to highlight the outliers in your data. Some simple examples include the following:

- 
					A red balloon in a group of blue ones 
- 
					A racehorse that is far ahead of the others 
- 
					A kid who isn't paying attention during class 
- 
					A day when online orders are up, but shipping is down 
- 
					A person who got well, where others didn't 

Some data points represent a significant event, and others represent a random occurrence. Analysis uncovers which data is worth investigating, based on what driving factors (key drivers) contributed to the event. Questions are essential to data analysis. Why did it happen? What's it related to? Did it happen only once or many times? What can you do to encourage or discourage more like it?

Understanding how and why a variation exists, and whether there is a pattern in the variations, requires more thought. Without the assistance of machine learning, each person might come to a different conclusion, because they have different experience and information. Therefore, each person might make a slightly different business decision. If there is a lot of data or variables to consider, it can require an overwhelming amount of analysis.

ML-powered anomaly detection identifies the causations and correlations to enable you to make data-driven decisions. You still have control over defining how you want the job to work on your data. You can specify your own parameters, and choose additional options, such as identifying key drivers in a contribution analysis. Or you can use the default settings. The following section walks you through the setup process, and provides explanations for the options available.