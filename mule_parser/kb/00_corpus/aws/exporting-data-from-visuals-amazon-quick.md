# Exporting data from visuals - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/exporting-data.html](https://docs.aws.amazon.com/quick/latest/userguide/exporting-data.html)

---

###### Note

Export files can directly return information from the dataset import. This makes the files vulnerable to CSV injection if the imported data contains formulas or commands. For this reason, export files can prompt security warnings. To avoid malicious activity, turn off links and macros when reading exported files.

Using the Amazon Quick console, you can export data from any type of chart or graph. The export contains only the data in the fields that are currently visible in the selected visualization. Any data that is filtered out is excluded from the export file. You can export data into the following formats:

- 
                    A text file containing comma-separated values (CSV), available for all visual types. 
- 
                    A Microsoft Excel workbook file (.xslx), available for pivot tables and table charts only. 

The following rules apply:

- 
                    Exported files are downloaded to the default download directory configured in the browser that you're currently using. 
- 
                    The downloaded file is named for the visualization that you exported it from. To make the file name unique, it has a sequential timestamp (a Unix epoch data type). 
- 
                    Default limit for export to CSV format: 500 MB or 1M rows whichever comes first 
- 
                    Default limit for export to Excel format: - 
                            from Pivot Table visual 400K cells or 50K rows 
- 
                            from Table visual 800K cells or 100K rows 
 ###### NoteWith a subscription to Paginated Reporting, you are able to [schedule the export of visuals in CSV and Excel formats](https://docs.aws.amazon.com/quicksight/latest/user/sending-reports.html)and export up to 3M rows (CSV) and 16M cells (Excel).
- 
                            
- 
                    You can't export data from an insight, because insights consume the data, but don't contain the data. 
- 
                    Quick Sight doesn't support exporting data from more than a single visualization at a time. To export data from additional visuals in the same analysis or dashboard, repeat this process for each visual. To export all the data from a dashboard or analysis, you need to connect to the original data source using valid credentials and a tool that you can use to extract data. 

Use the following procedure to export data from a visualization in Amazon Quick Sight. Before you begin, open the analysis or dashboard that contains the data that you want to export.

###### To export data from a visualization

- 
                    Choose the visualization that you want to export. Make sure that it is selected and highlighted. 
- 
                    At top right on the visual, open the menu and choose one of the following: - 
                            To export to CSV, choose **Export to CSV**.
- 
                            To export to XSLX, choose **Export to Excel**. This option is available only for pivot tables and table charts.
 
- 
                            
- 
                    Depending on your browser settings, one of the following happens: - 
                            The file automatically goes to your default **Download**location.
- 
                            A dialog box appears so you can choose a file name and location. 
- 
                            A dialog box appears so you can choose to open the file with the default software or to save to. 
 
-