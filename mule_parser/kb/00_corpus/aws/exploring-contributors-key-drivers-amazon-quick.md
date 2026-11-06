# Exploring contributors (key drivers) - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/exploring-anomalies-key-drivers.html](https://docs.aws.amazon.com/quick/latest/userguide/exploring-anomalies-key-drivers.html)

---

If your anomaly insight is set up to detect key drivers, Quick Sight runs the
					contribution analysis to determine which categories (dimensions) are influencing
					the outliers. The **Contributors** section appears on the left. 

**Contributors** contains the following sections:

- 
						**Narrative**– At top left, a summary describes any changes in the metrics.
- 
						**Top contributors configuration**– Choose**Configure**to change the contributors and the date range to use in this section.
- 
						**Sort by**– Sets the sort applied to the results that appear below. You can choose from the following:- 
								**Absolute difference**
- 
								**Contribution percentage**(default)
- 
								**Deviation from expected**
- 
								**Percentage difference**
 
- 
								
- 
						**Top contributor results**– Displays the results of the top contributor analysis for the point in time selected on the timeline at right.Contribution analysis identifies up to four of the top contributing factors or key drivers of an anomaly. For example, Amazon Quick Sight can show you the top customers that contributed to a spike in sales in the US for health products. This panel appears only if you choose to include fields in contribution analysis when you configure the anomaly. If you don't see this panel and you want to display it, you can turn it on. To do so, go to the analysis, choose anomaly configuration from the insight's menu, and choose up to four fields to analyze for contributions. If you make changes in the sheet controls that exclude the contributing drivers, the **Contributions**panel closes.