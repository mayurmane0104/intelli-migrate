# Visualize, analyze, and share data with analyses, dashboards, and reports in Amazon Quick Sight - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/quick-bi.html](https://docs.aws.amazon.com/quick/latest/userguide/quick-bi.html)

---

Amazon Quick Sight is a comprehensive business intelligence service that enables you to transform raw data into meaningful insights through interactive visualizations, dashboards, and reports. Whether you're connecting to databases, preparing datasets, creating analyses, or sharing dashboards with stakeholders, Amazon Quick Sight provides the tools you need to make data-driven decisions.

###### Note

Amazon Quick Sight is available only for Amazon Quick accounts provisioned through the AWS Management Console.
            It is not available for Free or Plus accounts created at
            [quick.aws.com](https://quick.aws.com).

This section covers the complete Amazon Quick Sight workflow, from initial data connection through final report sharing. You'll learn how to connect to various data sources, prepare and transform your data, create compelling visualizations, build interactive dashboards, and leverage generative BI capabilities to accelerate your analytics workflow. Each topic builds upon the previous one, providing a comprehensive guide to maximizing your use of Amazon Quick Sight's powerful features.

###### Topics

## Key concepts

        The following terms are used throughout this section.

- **Data source**
- 
                    A connection to an external data repository such as a database, data warehouse, cloud service, or file. Data sources provide the raw data for your analyses. 
- **Data preparation**
- 
                    The process of transforming data for use in an analysis. This includes filtering data, renaming fields, changing data types, adding calculated fields, and creating SQL queries to refine data. 
- **Dataset**
- 
                    A prepared collection of data ready for use in analyses and dashboards. Datasets can be stored in SPICE for fast performance or queried directly from the source. 
- **SPICE**
- 
                    *SPICE (Super-fast, Parallel, In-memory Calculation Engine)*is the in-memory engine that Quick Sight uses for high-performance analytics. SPICE speeds up analytical queries on imported data so you don't need to retrieve data from the source every time you change an analysis or update a visual.
- **Analysis**
- 
                    The workspace for creating data visualizations. Each analysis contains a collection of visualizations that you arrange and customize on one or more sheets. 
- **Visual**
- 
                    A graphical representation of data such as a chart, graph, or table. All visuals begin in AutoGraph mode, which automatically selects the best visualization type for the fields you select. 
- **Sheet**
- 
                    A page within an analysis that displays a set of visualizations and insights. You can add multiple sheets to an analysis and configure them to work independently or together. 
- **Dashboard**
- 
                    The published version of an analysis. You share dashboards with other Quick users and control what they can do with the data.