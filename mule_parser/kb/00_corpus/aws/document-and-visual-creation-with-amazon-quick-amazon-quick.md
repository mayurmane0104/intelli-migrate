# Document and visual creation with Amazon Quick - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/document-and-visual-creation.html](https://docs.aws.amazon.com/quick/latest/userguide/document-and-visual-creation.html)

---

Quick can create professional-quality documents and business visuals from natural language requests. You can create and edit Word documents, Excel spreadsheets, PowerPoint presentations, PDFs, infographics, and other business visuals directly within Quick. Describe what you need, and Quick produces a downloadable file that you can use immediately or refine further.

Document and visual creation is available in the following Quick features:

- 
            **Quick chat**— Create and edit documents and visuals through conversational requests. For more information, see[Creating documents and visuals in chat](#artifact-gen-chat).

###### Topics

## Supported document and visual types

        Quick supports creating the following document and visual types:

- **Word documents (.docx)**
- 
                    Create professional reports, proposals, contracts, and other text-based documents. Quick generates formatted documents with styles, tables, images, charts, headers, footers, and tables of contents. 
- **Excel spreadsheets (.xlsx)**
- 
                    Create spreadsheets with formulas, charts, conditional formatting, and multiple worksheets. Quick supports dashboards, financial models, data analysis workbooks, trackers, and data exports. 
- **PowerPoint presentations (.pptx)**
- 
                    Create slide decks with professional themes, layouts, charts, speaker notes, and visual elements. Quick can create presentations from scratch or from an existing template. 
- **PDF documents (.pdf)**
- 
                    Create formatted PDF documents with styled pages, tables, headers, footers, and page numbers. 
- **Business visuals (.png)**
- 
                    Create visual infographics, posters, diagrams, and charts from natural language descriptions. 

## How document and visual creation works

        When you request a document or visual, Quick uses an AI-powered process to interpret your request and produce the file. The process works as follows:

- 
                You describe the document you want to create using natural language. For example, *"Create a quarterly sales report in Excel with charts showing revenue by region."*
- 
                Quick determines the appropriate document type and generates the file using specialized document creation tools. 
- 
                As the document is being built, you see real-time progress updates describing each step of the generation process. 
- 
                When the document creation is complete, you can preview it in a dedicated panel to review the content and format. 
- 
                If everything looks good in the preview, you can download the document. If you need to make edits and refine the content further, you can add comments to specific sections of the document and regenerate the document with the feedback included. For broader changes that apply across the document, you can also use chat to give feedback and suggested changes. 

You can also upload files to use as input for document generation. For example, you can upload a CSV file and ask Quick to create an Excel dashboard from the data, or upload a Word document and ask for specific edits.

## Creating documents and visuals in chat

        You can create documents and business visuals directly in Quick chat by describing what you need.

###### Create a new document or visual

- 
                Open Quick chat. 
- 
                (Optional) Upload any input files that you want to use as source data. You can upload spreadsheets ( `.csv`,`.xls`,`.xlsx`), documents (`.docx`), presentations (`.pptx`), PDFs, and JSON files.
- 
                Describe the document you want to create. Be specific about the content, structure, formatting, and any analytical requirements. See the following section for examples. 
- 
                Quick generates the document and displays progress updates as it works. When the document is ready, it appears in a preview panel. 
- 
                Choose **Download**to save the file to your device.

### Example prompts

The following examples demonstrate the range of documents and visuals you can create, from simple documents to complex multi-sheet financial models.

- **Financial modeling (Excel)**
- 
                        *"Our company is evaluating whether to build a new distribution center or lease additional warehouse space. Create an Excel model comparing the total cost of ownership for building versus leasing over 10 years. Include an assumptions sheet with construction costs, lease rates, annual escalation percentages, maintenance costs, and discount rate that I can adjust. Create a 10-year cash flow projection for each scenario with NPV and IRR calculations. Add a break-even analysis sheet and a conclusion page comparing the two options with charts."*This produces a multi-sheet workbook with an editable assumptions page, year-by-year cash flow projections for each scenario, Excel formulas that update when you change inputs, and a conclusion sheet with comparison charts and financial metrics. 
- **Data-driven presentation (PowerPoint)**
- 
                        *"Using the attached quarterly sales CSV, create a board-ready PowerPoint presentation. Include an executive summary slide with key metrics, regional breakdowns with bar charts, a year-over-year trend analysis with line charts, and a final slide with strategic recommendations. Use a dark professional theme with our company colors (navy and gold)."*Upload your data file alongside the prompt. Quick extracts the data, builds the charts, and applies the requested theme across all slides. 
- **Contract document (Word)**
- 
                        *"Create a professional services agreement in Word. Include sections for scope of work, payment terms with a milestone schedule table, intellectual property rights, confidentiality, termination clauses, and limitation of liability. Add a signature block at the end. Use formal legal formatting with numbered sections and sub-sections."*This produces a structured legal document with proper heading hierarchy, numbered clauses, formatted tables, and signature blocks. 
- **Operational dashboard (Excel)**
- 
                        *"Create a project management dashboard in Excel. Include a summary sheet with KPI cards for budget utilization, schedule variance, and resource allocation. Add a task tracker sheet with status columns that use conditional formatting (green for on track, yellow for at risk, red for blocked). Add a Gantt-style timeline sheet and a risk register with severity scoring formulas."*This produces a multi-sheet workbook with conditional formatting, formulas that calculate status indicators, and charts that visualize project health. 
- **Research report (Word with data)**
- 
                        *"Using the attached PDF research paper and the CSV dataset, create a Word report that summarizes the key findings, includes a methodology section, presents the data in formatted tables with alternating row shading, and adds charts showing the main trends. Include a table of contents and an executive summary at the top."*Upload both files with your prompt. Quick reads the PDF content and CSV data, then produces a formatted report that synthesizes both sources with embedded charts and tables. 
- **Visual infographic**
- 
                        *"Create an infographic showing the global impact of renewable energy adoption. Include statistics on solar and wind capacity growth over the last decade, a world map highlighting top adopting countries, and a comparison of energy costs between renewable and fossil fuel sources. Use a clean, modern design with a green and white color palette."*This produces a visually designed infographic with data visualizations, geographic elements, and styled typography. Because no source data is uploaded with this prompt, the statistics shown are illustrative. You can refine the values by providing a data file or describing updates in chat. 

## Editing existing documents

        You can edit documents that Quick has previously created, or upload your own files for editing. Quick preserves the existing formatting and structure while applying your requested changes. For most document types, you can upload your own files for editing. See individual document types below for details.

###### Edit an existing document

- 
                In Quick chat, upload the document you want to edit, or continue a conversation where a document was previously generated. 
- 
                Describe the changes you want to make. For example: - 
                        *"Change all the heading colors to dark blue."*
- 
                        *"Add a new column called Status to the first table."*
- 
                        *"Update the title slide to say Q1 2026 Results."*
 
- 
                        
- 
                Quick applies the edits and produces an updated version of the document. 

The following editing capabilities are supported for each document type.

- **Word (.docx)**
- 
                    - 
                            *Text replacement*— Replace words or phrases throughout the document. Example:*"Change all instances of 2025 to 2026."*
- 
                            *Formatting changes*— Update fonts, colors, sizes, and styles. Example:*"Make all Heading 1 text dark blue and 16pt."*
- 
                            *Section management*— Add, remove, or reorder sections. Example:*"Move the Conclusions section to before the Appendix."*
- 
                            *Table modifications*— Add rows, columns, or update cell values. Example:*"Add a Status column to the project tracking table."*
- 
                            *Headers and footers*— Add or update page headers, footers, and page numbers. Example:*"Add a footer with the company name and page numbers."*
 
- 
                            
- **Excel (.xlsx)**
- 
                    - 
                            *Cell updates*— Modify values, formulas, and number formats. Example:*"Update the Q4 revenue figure in cell B5 to $3.5M."*
- 
                            *Chart additions*— Add or modify charts and visualizations. Example:*"Add a bar chart comparing revenue across all quarters."*
- 
                            *Worksheet management*— Add new sheets or restructure existing ones. Example:*"Add a Summary sheet with totals from each regional sheet."*
- 
                            *Formatting*— Update styles, conditional formatting, and layout. Example:*"Apply alternating row colors and bold the header row."*
 
- 
                            
- **PowerPoint (.pptx)**
- 
                    - 
                            *Content updates*— Change text, titles, and bullet points. Example:*"Update the title slide to say Q1 2026 Results."*
- 
                            *Layout changes*— Modify slide layouts and visual elements. Example:*"Change slide 3 to a two-column layout with the chart on the right."*
- 
                            *Data modifications*— Update chart data and table content. Example:*"Update the sales chart with the new figures from the uploaded spreadsheet."*
- 
                            *Slide management*— Add, remove, or reorder slides. Example:*"Add a new slide after the introduction with a team overview."*
 
- 
                            
- **Infographics (.png)**
- 
                    Infographic editing applies to visuals that were created in the current conversation. You can request changes to a previously generated infographic without uploading a separate file. - 
                            *Text changes*— Update titles, labels, and descriptions. Example:*"Change the title to Global Warming Trends."*
- 
                            *Visual updates*— Modify colors, layout, and styling. Example:*"Make the background blue and increase the font size of the statistics."*
 
- 
                            

###### Note

PDF documents cannot be edited in place. To modify a PDF, Quick extracts the content and creates a new PDF with your requested changes.

## Working with uploaded files

        You can upload files to use as input when creating documents and visuals. Quick reads the content of your uploaded files and uses it to produce the requested output.

Common use cases include:

- 
                Uploading a CSV or JSON file and creating an Excel dashboard or report from the data 
- 
                Uploading a PDF and converting its content into a Word document or presentation 
- 
                Uploading multiple source files and creating a consolidated summary document 
- 
                Uploading a PowerPoint template and creating a new presentation that matches its visual style 

Supported input file types:

- 
                Spreadsheets: `.csv`,`.xls`,`.xlsx`
- 
                Documents: `.docx`,`.pdf`
- 
                Presentations: `.pptx`
- 
                Data files: `.json`
- 
                Brand assets: `.svg`(for logos used with brand theming)

## Using templates

        You can upload an existing file as a template so that Quick creates new content that matches the original's visual design, branding, and formatting. Template support varies by document type, with PowerPoint offering the most comprehensive template cloning workflow. This is useful when your organization has standardized document styles that you want to maintain across new documents.

### PowerPoint templates

PowerPoint has the most comprehensive template support. When you upload a
                `.pptx` file and ask Quick to create a new presentation
                using it as a template, Quick does the following:

- 
                    Inspects the template to discover slide layouts, shape names, theme fonts, and theme colors. 
- 
                    Classifies the template slides by type, such as title or cover slides, section dividers, and content slides. 
- 
                    Clones the template slides that best match each section of your new content. Cloning preserves backgrounds, brand colors, decorative elements, icons, and images from the original template. 
- 
                    Fills in your new content by replacing text in the cloned slides while keeping the visual design intact. 

The result is a new presentation with your content that looks like it was built by hand using the original template.

To use a PowerPoint template:

- 
                    Upload your `.pptx`template file in Quick chat.
- 
                    Describe the new presentation you want to create. Mention that you want to use the uploaded file as a template. For example: - 
                            *"Using this template, create a 12-slide presentation about our 2026 product roadmap."*
- 
                            *"Create a quarterly business review deck using this template and the attached CSV data."*
 
- 
                            
- 
                    Quick generates the presentation using the template's visual design and your new content. 

PowerPoint templates work best when the template contains a variety of slide layouts, such as title slides, content slides with text placeholders, and section dividers. Quick selects the most appropriate layout for each slide in the new presentation based on the content.

### Excel templates

When you upload an existing `.xlsx` file as a template,
                Quick clones the workbook and preserves its formatting, formulas, and
                structure. It then populates the cloned workbook with your new data while keeping
                the original styling intact.

This is useful for:

- 
                    Recurring reports that use the same layout each period, such as monthly financial statements or quarterly dashboards 
- 
                    Standardized workbooks with pre-built formulas, conditional formatting, and data validation rules that you want to reuse with new data 
- 
                    Branded spreadsheets with specific header styles, color schemes, and chart formatting 

To use an Excel template, upload your `.xlsx` file and describe what
                data to populate. For example: *"Using this template, fill in the revenue
                sheet with the data from the attached CSV and update the dashboard
                charts."*

### Word templates

Word documents do not have a dedicated template cloning workflow. However, you
                can achieve a similar result by uploading an existing `.docx` file and
                asking Quick to edit it with new content. When editing, Quick
                preserves the original formatting, styles, headers, footers, and structure while
                applying your requested changes.

For example, if your organization has a branded report template with specific
                fonts, colors, and section layouts, you can upload it and ask: *"Replace
                the placeholder content in this report template with the following project
                details..."*

For new Word documents created from scratch, Quick applies professional formatting with configurable styles. You can specify fonts, colors, and layout preferences in your prompt to match your organization's standards.

## Previewing and downloading

        When Quick creates a document or visual, it appears in a preview panel.
            You can access the preview panel by choosing **View more**
            from below the item in chat.

From the preview panel, you can:

- 
                Preview the created document or visual 
- 
                Download it to your device 
- 
                Continue editing by sending follow-up messages in chat 

The following download formats are supported:

| Type | Download format | 
|---|---|
| Word documents | `.docx` | 
| Excel spreadsheets | `.xlsx` | 
| PowerPoint presentations | `.pptx` | 
| PDF documents | `.pdf` | 
| Infographics and business visuals | `.png` | 

## Business visual creation

        Quick can create business visuals like infographics, charts, and data visualizations. You can turn insights into shareable images for presentations and reports, or generate professional graphics for business communication.

Business visuals are available in two ways:

### Standalone infographics and visuals

You can create standalone business visuals by describing what you need in Quick chat. Quick produces a professionally designed image that you can download and share. These visuals are ideal for:

- 
                    Data-driven infographics that summarize key metrics and trends 
- 
                    Comparison charts and diagrams for stakeholder communication 
- 
                    Visual summaries for executive briefings and team updates 
- 
                    Process diagrams and workflow visualizations 

Example prompts:

- 
                    *"Create an infographic comparing our Q1 and Q2 performance metrics with charts showing revenue growth, customer acquisition, and retention rates."*
- 
                    *"Create a visual summary of our three-year strategic roadmap with milestones and key deliverables for each phase."*
- 
                    *"Using the attached CSV, create a data visualization showing regional sales distribution with a map and supporting bar charts."*

You can also edit previously created visuals by describing the changes you want.
                For example: *"Change the color scheme to blue and white and update the
                title to say H1 2026 Results."*

### Visuals embedded in documents

When creating Word documents, PowerPoint presentations, or PDFs, you can request that Quick include generated visuals within the document. These embedded visuals include:

- 
                    Background images and hero visuals for presentation title slides and section dividers 
- 
                    Illustrations and concept visuals for reports and proposals 
- 
                    Custom icons and decorative elements with transparent backgrounds 
- 
                    Data charts and visualizations created from your uploaded data 

To include visuals in a document, mention them in your prompt. For example:

- 
                    *"Create a PowerPoint presentation about our product launch with generated hero images on the title and section divider slides."*
- 
                    *"Create a Word proposal with an illustrated cover page and concept visuals for each solution section."*

###### Note

Each visual takes a few seconds to generate. For best results, limit visual generation requests to a few images per document.

## Brand theming

        You can apply your organization's brand identity to created documents and visuals by providing theme assets. When brand theme files are available, Quick automatically applies your brand colors and logos.

Brand theming supports the following asset types:

- 
                Theme configuration files that define brand colors 
- 
                Logo files in SVG format 

To apply brand theming, upload your theme configuration file (JSON format) and SVG logo assets in Quick chat alongside your document request. The theme configuration file defines your brand colors as hex values. Quick detects the theme files and applies your brand colors and logos to the generated output.

###### Note

Brand theming for business visuals and infographics supports brand colors and logos. Typography and additional brand image assets are not included in theme configuration but can be provided as file uploads in chat.

Brand theming is available for all document and visual types, including Word documents, Excel spreadsheets, PowerPoint presentations, PDFs, and infographics.

## Best practices

        Follow these best practices to get the best results:

- 
                **Be specific in your requests.**Include details about the content, structure, formatting, and any specific requirements. For example, instead of "Create a report," try "Create a Word report with an executive summary, three data sections with tables, and a conclusion."
- 
                **Provide source data when possible.**Upload CSV, Excel, or JSON files so that Quick can use real data instead of generating placeholder content.
- 
                **Iterate on your documents.**Start with a first draft and then request specific edits in follow-up messages. This is often more effective than trying to specify everything in a single request.
- 
                **Specify the document type.**Mention the file format you want (Word, Excel, PowerPoint, PDF) in your request to ensure Quick generates the correct document type.
- 
                **Use templates for consistent styling.**When creating presentations, upload an existing`.pptx`template to maintain consistent visual styling across your organization.

## Limitations

        The following limitations apply to document and visual creation in Quick:

- 
                When you provide source data, Quick uses it exactly as given and does not fabricate additional data points. When no source data is provided, Quick can generate illustrative values such as common assumptions or sample inputs for models and templates. For editable document types (Word, Excel, PowerPoint), these values are clearly presented as defaults that you can modify directly in the downloaded file. For infographics (PNG), you can request changes by describing the updates you want in chat. 
- 
                PDF documents cannot be edited in place. To modify a PDF, Quick extracts the content and recreates the document. 
- 
                Complex formatting or highly customized layouts may require multiple iterations to achieve the desired result. 
- 
                Saving generated documents to a Space is not currently supported.