# Tutorial: Create a prepared Amazon Quick Sight dataset - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/example-prepared-data-set.html](https://docs.aws.amazon.com/quick/latest/userguide/example-prepared-data-set.html)

---

Use the following procedure to prepare the Marketing dataset and create an
					analysis. If you don't see the Web and Social Media Analytics sample data
					already in Amazon Quick Sight, you can download it: [web-and-social-analytics.csv.zip](samples/web-and-social-analytics.csv.zip).

###### To prepare the Marketing dataset and create an analysis

- 
						From the Amazon Quick homepage, choose **Data**in the navigation pane.
- 
						In the **Datasets**tab, choose**New**then**Dataset**.
- 
						From the existing data sources, choose the **Web and Social Media Analytics**Amazon S3 data source. Choose your table and then choose**Edit/Preview data**.Amazon Quick opens the data preparation page. 
- 
						For **Dataset Name**, enter`Marketing Sample`to replace*Web and Social Media Analytics*for the dataset name.
- 
						Exclude some fields from the dataset. In the **Fields**pane, choose the three-dot menu for the**Twitter followers cumulative**and**Mailing list cumulative**fields, and then choose**Exclude field**. To select more than one field at a time, press the Ctrl key while you select (Command key on Mac).
- 
						Rename a field. In the **Dataset**preview pane, scroll to the**Website Pageviews**field and choose the pencil icon to edit.In the **Edit field**page that opens, for**Name**, enter`Website page views`, and then choose**Apply**.
- 
						Add a calculated field that substitutes a text string for any 0-length string value in the **Events**field:- 
								On the data preparation page, scroll to the top of the **Fields**pane, and then choose**Add calculated field**.
- 
								In the **Add calculated field**page that opens, for**Add name**, enter`populated_event`.
- 
								In the **Functions**pane at right, double-click the**ifelse**function from the list of functions. This adds the function to the calculated field formula.
- 
								Expand the **Field list**pane by choosing the drop-down arrow, and then double-click the**Events**field. This adds the field to the calculated field formula.
- 
								In formula editor, enter the following additional functions and parameters required, in bold in the following: ifelse( **strlen(**{Events}**)=0, 'Unknown', {Events}**).The final formula should be as follows: `ifelse(strlen({Events})=0, 'Unknown', {Events})`.
- 
								Choose **Save**.The new calculated field is created, and appears at the top of the **Fields**pane.
 
- 
								
- 
						Choose **Save**.

## Next steps

					Create an analysis by using the procedure in [Tutorial: Create an Amazon Quick Sight analysis](./example-create-an-analysis.html).