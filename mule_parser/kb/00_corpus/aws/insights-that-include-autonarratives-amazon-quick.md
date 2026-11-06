# Insights that include autonarratives - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/auto-narratives.html](https://docs.aws.amazon.com/quick/latest/userguide/auto-narratives.html)

---

When you are adding an insight, also known as an autonarrative, to your analysis,
				you can choose from the following templates. In the following list, they are defined
				by example. Each definition includes a list of the minimum required fields for the
				autonarrative to work. If you are using only the suggested insights on the
					**Insights** tab, choose the appropriate fields to get an
				insight to show up in the suggested insights list.

For more information on customizing autonarratives, see [Working with autonarrative computations](./auto-narrative-computations.html).

- 
					**Bottom ranked**– For example, the bottom three states by sales revenue. Requires that you have at least one dimension in the**Categories**field well.
- 
					**Bottom movers**– For example, the bottom three products sold, by sales revenue. Requires that you have at least one dimension in the**Time**field well and at least one dimension in the**Categories**field well.
- 
					**Forecast***(ML-powered insight)*– For example, "Total sales are forecasted to be $58,613 for Jan 2016." Requires that you have at least one dimension in the**Time**field well.
- 
					**Growth rate**– For example, "The 3-month compounded growth rate for sales is 22.23%." Requires that you have at least one dimension in the**Time**field well.
- 
					**Maximum**– For example, "Highest month is Nov 2014 with sales of $112,326." Requires that you have at least one dimension in the**Time**field well.
- 
					**Metric comparison**– For example, "Total sales for Dec 2014 is $90,474, 10% higher than target of $81,426." Requires that you have at least one dimension in the**Time**field well and at least two measures in the**Values**field well.
- 
					**Minimum**– For example, "Lowest month is Feb 2011 with sales of $4,810." Requires that you have at least one dimension in the**Time**field well.
- 
					**Anomaly detection***(ML-powered insight)*– For example, top three outliers and their contributing drivers for total sales on January 3, 2019. Requires that you have at least one dimension in the**Time**field well, at least one measure in the**Values**field well, and at least one dimension in the**Categories**field well.
- 
					**Period over period**– For example, "Total sales for Nov 2014 increased by 44.39% ($34,532) from $77,793 to $112,326." Requires that you have at least one dimension in the**Time**field well.
- 
					**Period to date**– For example, "Year-to-date sales for Nov 30, 2014 increased by 25.87% ($132,236) from $511,236 to $643,472." Requires that you have at least one dimension in the**Time**field well.
- 
					**Top ranked**– For example, top three states by sales revenue. Requires that you have at least one dimension in the**Categories**field well.
- 
					**Top movers**– For example, top products by sales revenue for November 2014. Requires that you have at least one dimension in the**Time**field well and at least one dimension in the**Categories**field well.
- 
					**Total aggregation**– For example, "Total revenue is $2,297,200." Requires that you have at least one dimension in the**Time**field well and at least one measure in the**Values**field well.
- 
					**Unique values**– For example, "There are 793 unique values in`Customer_IDs`." Requires that you have at least one dimension in the**Categories**field well.