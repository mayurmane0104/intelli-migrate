# Preparing a dataset based on file data - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/prepare-file-data.html](https://docs.aws.amazon.com/quick/latest/userguide/prepare-file-data.html)

---

Use the following procedure to prepare a dataset based on text or Microsoft Excel files from either your local network or Amazon S3.

###### To prepare a dataset based on text or Microsoft Excel files from a local network or S3

- 
				Open a file dataset for data preparation by choosing one of the following options: - 
						Create a new local file dataset, and then choose **Edit/Preview data**. For more information about creating a new dataset from a local text file, see[Creating a dataset using a local text file](https://docs.aws.amazon.com/quicksight/latest/user/create-a-data-set-file.html). For more information about creating a new dataset from a Microsoft Excel file, see[Creating a dataset using a Microsoft Excel file](https://docs.aws.amazon.com/quicksight/latest/user/create-a-data-set-excel.html).
- 
						Create a new Amazon S3 dataset, and then choose **Edit/Preview data**. For more information about creating a new Amazon S3 dataset using a new Amazon S3 data source, see[Creating a dataset using Amazon S3 files](https://docs.aws.amazon.com/quicksight/latest/user/create-a-data-set-s3.html). For more information about creating a new Amazon S3 dataset using an existing Amazon S3 data source, see[Creating a dataset using an existing Amazon S3 data source](https://docs.aws.amazon.com/quicksight/latest/user/create-a-data-set-existing-s3.html).
- 
						Open an existing Amazon S3, text file, or Microsoft Excel dataset for editing, from either the analysis page or the **Your Datasets**page. For more information about opening an existing dataset for data preparation, see[Editing datasets](https://docs.aws.amazon.com/quicksight/latest/user/edit-a-data-set.html).
 
- 
						
- 
				(Optional) On the data preparation page, enter a new name into the dataset name box on the application bar. This name defaults to the file name for local files. For example, it defaults to `Group 1`for Amazon S3 files.
- 
				Review the file upload settings and correct them if necessary. For more information about file upload settings, see [Choosing file upload settings](https://docs.aws.amazon.com/quicksight/latest/user/choosing-file-upload-settings.html).###### ImportantIf you want to change upload settings, make this change before you make any other changes to the dataset. New upload settings cause Amazon Quick Sight to reimport the file. This process overwrites all of your other changes. 
- 
				Prepare the data by doing one or more of the following: 
- 
				Check the [SPICE](./spice.html)indicator to see if you have enough capacity to import the dataset. File datasets automatically load into SPICE. The import happens when you choose either**Save & visualize**or**Save**.If you don't have access to enough SPICE capacity, you can make the dataset smaller by using one of the following options: - 
						Apply a filter to limit the number of rows. 
- 
						Select fields to remove from the dataset. 
 ###### NoteThe SPICE indicator doesn't update to how much space you save by removing fields or filtering the data. It continues to reflect the SPICE usage from the last import. 
- 
						
- 
				Choose **Save**to save your work, or**Cancel**to cancel it.You might also see **Save & visualize**. This option appears based on the screen that you started from. If this option isn't there, you can create a new visualization by starting from the dataset screen.

## Preparing a dataset based on a Microsoft Excel file

			Use the following procedure to prepare a Microsoft Excel dataset.

###### To prepare a Microsoft Excel dataset

- 
					Open a text file dataset for preparation by choosing one of the following options: - 
							Create a new Microsoft Excel dataset, and then choose **Edit/Preview data**. For more information about creating a new Excel dataset, see[Creating a dataset using a Microsoft Excel file](https://docs.aws.amazon.com/quicksight/latest/user/create-a-data-set-excel.html).
- 
							Open an existing Excel dataset for editing. You can do this from the analysis page or the **Your Datasets**page. For more information about opening an existing dataset for data preparation, see[Editing datasets](https://docs.aws.amazon.com/quicksight/latest/user/edit-a-data-set.html).
 
- 
							
- 
					(Optional) On the data preparation page, enter a name into the dataset name box in the application bar. If you don't rename the dataset, its name defaults to the Excel file name. 
- 
					Review the file upload settings and correct them if necessary. For more information about file upload settings, see [Choosing file upload settings](https://docs.aws.amazon.com/quicksight/latest/user/choosing-file-upload-settings.html).###### ImportantIf it's necessary to change upload settings, make this change before you make any other changes to the dataset. Changing upload settings causes Amazon Quick Sight to reimport the file. This process overwrites any changes you have made so far. 
- 
					(Optional) Change the worksheet selection. 
- 
					(Optional) Change the range selection. To do this, open **Upload Settings**from the on-dataset menu beneath the login name at upper right.
- 
					Prepare the data by doing one or more of the following: 
- 
					Check the [SPICE](./spice.html)indicator to see if you have enough space to import the dataset. Amazon Quick Sight must import Excel datasets into SPICE. This import happens when you choose either**Save & visualize**or**Save**.If you don't have enough SPICE capacity, you can choose to make the dataset smaller using one of the following methods: - 
							Apply a filter to limit the number of rows. 
- 
							Select fields to remove from the dataset. 
- 
							Define a smaller range of data to import. 
 ###### NoteThe SPICE indicator doesn't update to reflect your changes until after your load them. It shows the SPICE usage from the last import. 
- 
							
- 
					Choose **Save**to save your work, or**Cancel**to cancel it.You might also see **Save & visualize**. This option appears based on the screen that you started from. If this option isn't there, you can create a new visualization by starting from the dataset screen.