# Creating Amazon S3 datasets - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/create-a-data-set-s3-procedure.html](https://docs.aws.amazon.com/quick/latest/userguide/create-a-data-set-s3-procedure.html)

---

###### To create an Amazon S3 dataset

- 
                    Check [Data source quotas](./data-source-limits.html)to make sure that your target file set doesn't exceed data source quotas.
- 
                    Create a manifest file to identify the text files that you want to import, using one of the formats specified in [Supported formats for Amazon S3 manifest files](./supported-manifest-file-format.html).
- 
                    Save the manifest file to a local directory, or upload it into Amazon S3. 
- 
                    On the Quick start page, choose **Data**.
- 
                    On the **Data**page, choose**Create**then**New dataset**.
- 
                    Choose the Amazon S3 icon and then choose **Next**.
- 
                    For **Data source name**, enter a description of the data source. This name should be something that helps you distinguish this data source from others.
- 
                    For **Upload a manifest file**, do one of the following:- 
                            To use a local manifest file, choose **Upload**, and then choose**Upload a JSON manifest file**. For**Open**, choose a file, and then choose**Open**.
- 
                            To use a manifest file from Amazon S3, choose **URL**, and enter the URL for the manifest file. To find the URL of a pre-existing manifest file in the Amazon S3 console, navigate to the appropriate file and choose it. A properties panel displays, including the link URL. You can copy the URL and paste it into Quick Sight.
 
- 
                            
- 
                    Choose **Connect**.
- 
                    To make sure that the connection is complete, choose **Edit/Preview data**. Otherwise, choose**Visualize**to create an analysis using the data as-is.If you choose **Edit/Preview data**, you can specify a dataset name as part of preparing the data. Otherwise, the dataset name matches the name of the manifest file.To learn more about data preparation, see [Preparing data in Amazon Quick Sight](./preparing-data.html).

## Creating datasets based on multiple Amazon S3 files

                You can use one of several methods to merge or combine files from Amazon S3 buckets inside Quick Sight:

- 
                        **Combine files by using a manifest**– In this case, the files must have the same number of fields (columns). The data types must match between fields in the same position in the file. For example, the first field must have the same data type in each file. The same goes for the second field, and the third field, and so on. Quick Sight takes field names from the first file.The files must be listed explicitly in the manifest. However, they don't have to be inside the same Amazon S3 bucket. In addition, the files must follow the rules described in [Supported formats for Amazon S3 manifest files](./supported-manifest-file-format.html).For more details about combining files using a manifest, see [Creating a dataset using Amazon S3 files](./create-a-data-set-s3.html).
- 
                        **Merge files without using a manifest**– To merge multiple files into one without having to list them individually in the manifest, you can use Athena. With this method, you can simply query your text files, like they are in a table in a database. For more information, see the post[Analyzing data in Amazon S3 using Athena](https://aws.amazon.com/blogs/big-data/analyzing-data-in-s3-using-amazon-athena/)in the Big Data blog.
- 
                        **Use a script to append files before importing**– You can use a script designed to combine your files before uploading.