# Restricting others from creating new datasets from your dataset - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/restrict-create-dataset.html](https://docs.aws.amazon.com/quick/latest/userguide/restrict-create-dataset.html)

---

When you create a dataset in Amazon Quick, you can prevent others from using it as a source for other datasets. You can specify if others can use it to create any datasets at all. Or you can specify the type of datasets others can or can't create from your dataset, such as direct query datasets or SPICE datasets.

Use the following procedure to learn how to restrict others from creating new datasets from your dataset.

###### To restrict others from creating new datasets from your dataset

- 
					From the Quick start page, choose **Data**in the pane at left.
- 
					Choose **Create**then choose the dataset that you want to restrict creating new datasets from.
- 
					On the page that opens for that dataset, choose **Edit dataset**.
- 
					On the data preparation page that opens, choose **Manage**at upper right, and then choose**Properties**.
- 
					In the **Dataset properties**pane that opens, choose from the following options:- 
							To restrict anyone from creating any type of new datasets from this dataset, turn off **Allow new datasets to be created from this one**.The toggle is blue when creating new datasets is allowed. It's gray when creating new datasets isn't allowed. 
- 
							To restrict others from creating direct query datasets, clear **Allow direct query**.
- 
							To restrict others from creating SPICE copies of your dataset, clear **Allow SPICE copies**.For more information about SPICE datasets, see [Importing data into SPICE](./spice.html).
 
- 
							
- 
					Close the pane.