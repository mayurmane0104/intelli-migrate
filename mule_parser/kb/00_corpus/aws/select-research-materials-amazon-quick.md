# Select research materials - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/select-research-materials.html](https://docs.aws.amazon.com/quick/latest/userguide/select-research-materials.html)

---

After defining your research objective, you can select the data sources that Quick Research will use to gather information. Set your preferences and control what sources Quick Research uses. Include files, web search preferences, company assets, and premium and public datasets.

###### To select research materials

- 
                 In the material selection interface, review the available data source options. 
- 
                 Select the types of materials you want to include: - Toggle - **Web search**to include online sources
- 
                         Choose **File upload**to add specific documentsFor best results, include key documents that are most relevant to your research goals. Adding more materials may increase research time and lead to less focused insights. If you're working with larger collections, consider using Spaces to organize and optimize extensive research materials for better results. 
- Choose - **Quick assets**to include data spaces, dashboards, knowledge bases, and integrations in your research. For more information about creating and managing data spaces, see- [Organize, collaborate, and share resources with spaces in Amazon Quick](./working-with-spaces.html).
- Choose - **Third party data**to incorporate data from premium datasets and trusted public data sources to enhance your research. For more information, see- [Using third party data in Amazon Quick Research](./third-party-data.html).
 
- 
                 Choose **Review plan**to review a draft research plan before starting, or choose**Start researching**to begin research immediately.

## Web search

        Enable web search to allow Quick Research to gather information from publicly available online sources. This includes academic papers, industry reports, news articles, and other relevant web content related to your research objective.

Amazon Quick uses the internet to enhance your results. Web search queries may be processed in a different AWS Region than your primary Region. For more information, see 
            [Cross-Region calls for web search](./regions.html#web-search-cross-region).

To prioritize or avoid certain websites, you can expand the web search section to enter a list of preferred websites and a list of websites to avoid. Both fields are optional and can take a maximum of 3,500 characters.

We recommend providing a list of web domains (such as `example.com`), but you can also include types of websites such as `government websites` or `blogs`. If you enter a website address like `example.com/path/to/specific/page`, it will be shortened to `example.com`, so you don't need to enter multiple websites for a single domain.

###### Note

Adding a domain to the list of preferred websites doesn't guarantee that the website will be used in research. A website might not be used include: the site is behind a paywall, the site doesn't allow agents to access it, or the site's content is found to be less relevant than other sites.

## Uploaded files

        Upload specific documents, PDFs, spreadsheets, or other files that you want Quick Research to analyze as part of your research. This is useful when you have particular sources or documents that are directly relevant to your research objective.

###### To upload files

- 
                Choose **Upload**to open the**File Uploads**window.
- 
                Add files using one of the following methods: - Choose - **Add Files**to navigate to your files in File Explorer
- Drag and drop up to 20 files into the upload area 
 If you need to include more than 20 files in your research, consider organizing them in Spaces instead. 
- 
                When you're finished selecting files, choose **Done**.

Accepted file formats include .pdf, .txt, .doc, .xls, and .csv files. The file size limit is 25MB per file.

## Quick assets

        Connect Quick Research to your existing data spaces to include internal documents, reports, knowledge bases, and integrations in your research. You can combine external web sources with your organization's proprietary information. Quick Research can also fetch data through Quick action connectors, enabling it to pull live data from connected systems during the research process.

For optimal results, consider selecting the most relevant assets for your specific research question. Choose **Browse** to add assets from Quick.

###### To add Quick assets

- 
                Choose **Browse**to open the**Add assets**window in the right pane.
- 
                Select from the available resource type tabs: - **Recent**- Recently accessed assets
- **Space**- Available data spaces (maximum of 2 selections)
- **Dashboard**- Dashboard resources (maximum of 2 selections)
- **Topic**- Topic resources (maximum of 2 selections)
- **Knowledgebase**- Knowledge base resources
- **Integration**- Action connectors that can fetch live data from connected systems
 
- 
                Review the available assets, which display the Name, Owner, and Last Modified date and time for each asset. 
- 
                Select the assets you want to include in your research. 
- 
                When you're finished specifying all assets, choose **Add**.