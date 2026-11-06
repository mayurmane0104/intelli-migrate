# Choosing file upload settings - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/choosing-file-upload-settings.html](https://docs.aws.amazon.com/quick/latest/userguide/choosing-file-upload-settings.html)

---

If you are using a file data source, confirm the upload settings, and correct them if necessary.

###### Important

If it's necessary to change upload settings, make these changes before you make any other changes to the dataset. Changing upload settings causes Amazon Quick Sight to reimport the file. This process overwrites any changes you have made so far.

## Changing text file upload settings

			Text file upload settings include the file header indicator, file format, text delimiter, text qualifier, and start row. If you are working with an Amazon S3 data source, the upload settings you select are applied to all files you choose to use in this dataset.

Use the following procedure to change text file upload settings.

- 
					On the data preparation page, open the **Upload Settings**pane by choosing the expand icon.
- 
					In **File format**, choose the file format type.
- 
					If you chose the **custom separated (CUSTOM)**format, specify the separating character in**Delimiter**.
- 
					If the file doesn't contain a header row, deselect the **Files include headers**check box.
- 
					If you want to start from a row other than the first row, specify the row number in **Start from row**. If the**Files include headers**check box is selected, the new starting row is treated as the header row. If the**Files include headers**check box is not selected, the new starting row is treated as the first data row.
- 
					In **Text qualifier**, choose the text qualifier, either single quotes (') or double quotes (").

## Changing Microsoft Excel file upload settings

			Microsoft Excel file upload settings include the range header indicator and whole worksheet selector.

Use the following procedure to change Microsoft Excel file upload settings.

- 
					On the data preparation page, open the **Upload Settings**pane by choosing the expand icon.
- 
					Leave **Upload whole sheet**selected.
- 
					If the file doesn't contain a header row, deselect the **Range contains headers**check box.