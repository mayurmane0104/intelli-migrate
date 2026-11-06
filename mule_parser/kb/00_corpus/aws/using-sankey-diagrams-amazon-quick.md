# Using Sankey diagrams - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/sankey-diagram.html](https://docs.aws.amazon.com/quick/latest/userguide/sankey-diagram.html)

---

Use Sankey diagrams to show flows from one category to another, or paths from one stage to the next.

For example, a Sankey diagram can show the number of people migrating from one country to another. A Sankey diagram can also show the path a web visitor takes from one page to the next on a company website, with possible stops along the way.

## Data for Sankey diagrams

			To create Sankey diagrams in Quick, your dataset should contain a measure and two dimensions (one dimension containing source categories and another containing destination categories).

The following table is a simple example of data for a Sankey diagram.

| Dimension (Source) | Dimension (Destination) | Measure (Weight) | 
|---|---|---|
| A | W | 500 | 
| A | X | 23 | 
| A | Y | 147 | 

The following Sankey diagram is created when the dimensions and measure are added to the field well, with the A node on the left linking to the W, Y, and X nodes on the right. The width of each link between nodes is determined by the value in the Measure (Weight) column. The nodes are automatically ordered.

To create multilevel Sankey diagrams in Amazon Quick, your dataset should still contain a measure and two dimensions (one for source and one for destination), but in this case your data values differ.

The following table is a simple example of data for a multilevel Sankey diagram with two stages.

| Dimension (Source) | Dimension (Destination) | Measure (Weight) | 
|---|---|---|
| A | W | 500 | 
| A | X | 23 | 
| A | Y | 147 | 
| W | Z | 300 | 
| X | Z | 5 | 
| Y | Z | 50 | 

The following Sankey diagram is created when the dimensions and measure are added to the field well. Here, the A node on the left links to the W, Y, and X nodes in the middle, and the W, Y, and X nodes then link to the Z node on the right. The width of each link between nodes is determined by the value in the Measure (Weight) column.

### Working with cyclical data

Sometimes, the data that you use for a Sankey diagram contains cycles. For example, suppose that you're visualizing user traffic flows between pages on a website. You might discover that users who come to page A move to page E, and then come back to page A. An entire flow might look something like A-E-A-B-A-E-A.

When your data contains cycles, the nodes in each cycle are repeated in Quick. For example, if your data contains the flow A-E-A-B-A-E-A, the following Sankey diagram is created.

## Preparing data for Sankey diagrams

			If your dataset doesn't contain Source or Destination columns, prepare your
				data to include them. You can prepare data when creating a new dataset, or when
				editing an existing dataset. For more information about creating a new dataset and
				preparing it, see [Creating datasets](./creating-data-sets.html). For more information about opening an
				existing dataset for data preparation, see [Editing datasets](./edit-a-data-set.html).

The following procedure uses an example table (illustrated in following) to demonstrate how to prepare your data for Sankey diagrams in Quick. The table includes three columns: Customer ID, Time, and Action.

| Customer ID | Time | Action | 
|---|---|---|
| 1 | 9:05 am | Step 1 | 
| 1 | 9:06 am | Step 2 | 
| 1 | 9:08 am | Step 3 | 
| 2 | 11:44 am | Step 1 | 
| 2 | 11:47 am | Step 2 | 
| 2 | 11:48 am | Step 3 | 

To create a Sankey diagram in Quick using this data, first add Source and Destination columns to the table. Use the following procedure to learn how.

###### To add Source and Destination columns to your table

- 
					Add a Step Number column to the table to number or rank each row. There are multiple ways to compute the Step Number column. If your data source is compatible with SQL and your database supports `ROW_NUMBER`or`RANK`functions, you can use custom SQL in Quick to order the rows in the Step Number column. For more information about using custom SQL in Quick, see[Using SQL to customize data](./adding-a-SQL-query.html).Customer ID Time Action Step Number 1 9:05 am Step 1 1 1 9:06 am Step 2 2 1 9:08 am Step 3 3 2 11:44 am Step 1 1 2 11:47 am Step 2 2 2 11:48 am Step 3 3 
- 
					Add a Next Row Number column to the table with values equal to Step Number plus one. For example, in the first data row of the table, the value for Step Number is 1. To compute the value for Next Step Number for that row, add 1 to that value. 1 + 1 = 2 The value for Step Number in the second data row of the table is 2; therefore, the value for Next Step Number is 3. 2 + 1 = 3 Customer ID Time Action Step Number Next Step Number 1 9:05 am Step 1 1 2 1 9:06 am Step 2 2 3 1 9:08 am Step 3 3 4 2 11:44 am Step 1 1 2 2 11:47 am Step 2 2 3 2 11:48 am Step 3 3 4 
- 
					Join the table with itself: - 
							For **Join type**, choose**Inner**.
- 
							For **Join clauses**, do the following:- 
									Choose **Customer ID**=**Customer ID**
- 
									Choose **Next Step Number**=**Step Number**
 
- 
									
 Joining the two tables creates two columns for Customer ID, Time, Action, Step Number and Next Step Number. The columns from the table at the left of the join are Source columns. The columns from the table at the right of the join are Destination columns. For more information about joining data in Quick, see [Joining data](./joining-data.html).
- 
							
- 
					(Optional) Rename columns to indicate sources and destinations. The following is an example: - 
							Rename the **Action**column on the left to**Source**.
- 
							Rename the **Action [copy]**column on the right to**Destination**.
- 
							Rename the **Time**column on the left to**Start Time**.
- 
							Rename the **Time [copy]**column on the right to**End Time**.
 Your data is now ready to visualize. 
- 
							

## Creating Sankey diagrams

			Use the following procedure to create a Sankey diagram.

###### To create a Sankey diagram

- 
					On the analysis screen, choose **Visualize**on the left toolbar.
- 
					On the application bar, choose **Add**, and then choose**Add visual**.
- 
					On the **Visual types**pane, choose the Sankey diagram icon.
- 
					On the menu in the upper-right corner of the visual, choose the **Properties**icon.
- 
					In the **Properties pane**, choose either the**Source**or**Destination**section.

### Customizing the number of nodes

Use the following procedure to customize the number of nodes that appear in a Sankey diagram. Quick supports up to 100 Source/Destination nodes.

###### To customize the number of nodes that appear in a Sankey diagram

- 
						On the analysis page, choose the Sankey diagram visual that you want to format. 
- 
						On the menu in the upper-right corner of the visual, select the **Format Visual**icon.
- 
						In the **Properties**pane that opens, choose either the**Source**or**Destination**tab.
- 
						For **Number of nodes displayed**, enter a number.The nodes in the diagram update to the number that you specified. The top nodes are automatically shown. All other nodes are placed in an **Other**category.###### NoteSpecifying the number of Source nodes controls how many Source nodes can appear overall in the diagram. Specifying the number of Destination nodes controls how many Destination nodes can appear per Source node. This means that if there is more than one Source node in your diagram, the overall number of Destination nodes will be higher than the number specified. Quick supports up to 100 Source/Destination nodes. For example, the following Sankey diagram has a limit of three source nodes (out of five), so the top three are shown in the diagram. The other two source nodes are placed in the Other category. To remove the **Other**category from the diagram, select it in the view and choose**Hide “other” categories**.

## Sankey diagram features

			To understand the features supported by Sankey diagrams, use the following table.

| Feature | Supported? | For more information | 
|---|---|---|
| Changing the legend display | No | |
| Changing the title display | Yes | [Titles and subtitles on visual types in Quick](./customizing-a-visual-title.html) | 
| Changing the axis range | No | |
| Changing the visual colors | No | |
| Focusing on or excluding elements | Yes | |
| Sorting | No | |
| Performing field aggregation | Yes | [Changing field aggregation](./changing-field-aggregation.html) | 
| Adding drill-downs | No | |
| Conditional formatting | No |