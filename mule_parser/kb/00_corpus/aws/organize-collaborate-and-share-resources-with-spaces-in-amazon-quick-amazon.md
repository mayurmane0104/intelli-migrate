# Organize, collaborate, and share resources with spaces in Amazon Quick - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/working-with-spaces.html](https://docs.aws.amazon.com/quick/latest/userguide/working-with-spaces.html)

---

A space in Amazon Quick is a collection of data and Quick resources scoped for a particular team or domain. You can use spaces to aggregate and organize files, dashboards, topics, knowledge bases, and application actions into a unified and customizable knowledge center for your team. Spaces integrate seamlessly with Quick agents for contextual conversations and are designed to scale across personal, team, and cross-team use cases.

Spaces allow your team to get the most relevant results from conversational agents and
        other AI tools inside Quick by grounding the results with only data relevant for
        your task or domain. Multiple people on the team can contribute to the knowledge inside a
        space; this reduces data silos and streamline information discovery. Spaces also serve as a
        data layer for apps in Amazon Quick applications. For more information, see
        [Build web applications with apps in Amazon Quick](./using-amazon-quick-apps.html).

###### Note

Quick resources added to a space respect user access permissions. If a user can't access a resource outside a space, they won't be able to access it inside a space. Files uploaded to a space are always available to everyone with access to the space.

You can use spaces to accomplish tasks like:

- 
            Aggregating and sharing customer feedback, allowing any team member to ask questions and get summaries 
- 
            Onboarding new team members with team documents, manuals, and processes 
- 
            Analyzing hundreds of annual reports 
- 
            Summarizing and search for action items from audio meeting recordings 

###### Topics

## Amazon Quick user interactions with spaces

        The following table shows how each user type in Amazon Quick interacts with spaces.

| User type | Capabilities | 
|---|---|
| Administrators | 
 | 
| Author Pro and Reader Pro users | 
 | 

## Amazon Quick user permission for spaces

        What you can do with a space also depends on the permissions you're assigned for it. There are two permission types that users can be assigned:

- 
                **Owner**– Owners can create, edit, share, and delete a space.
- 
                **Viewer**– Viewers can view ask questions, and download files from spaces.

The following table outlines how user permissions determine what you can do with a Amazon Quick space:

| Permissions type | Permissions | 
|---|---|
| Owners | 
 As an owner, you can designate another user co-owner of a space. If you do so, the user can undertake all post-creation management actions an owner can. | 
| Viewers | 
 | 

## Understanding file upload status

        When you upload files, you should see the following status messages:

- **Uploading**
- 
                    Files are being uploaded into your computer. 
- **Processing**
- 
                    Files are being processed. 
- **Text ready**
- 
                    The text content of the document is ready to be queried. However, the document's images and tables are still processing. 
- **Ready**
- 
                    The text and media of the document has been processed. 
- **Deleting**
- 
                    The document is being deleted. 

## Limitations of spaces

        The following list outlines the limitations of spaces:

- 
                A space can't contain other spaces. 
- 
                Users can't access Amazon Quick resouces (topics, dashboards) in a space if they don't have access to the resource outside it. Sharing a space doesn't automatically give access to users to assets within it. 
- 
                If an Amazon Quick resource is linked to a space is deleted outside the space, users of the space won't get notified of the deletion. Deleted assets will only display a message indicating unavailability. 
- 
                Files uploaded to spaces will be rejected if your index data storage capacity is full. Reach out to your system administrator if this happens. 
- 
                Files uploaded to a space must be one of the following formats: `.html`,`.xhtml`,`.txt`,`.pdf`,`.csv`,`.tsv`,`.xml`,`.json`,`.md`,`.rtf`,`.xslt`,`.eml`,`.vtt`,`.docx`,`.dotx`,`.docm`,`.dotm`,`.ppt`,`.pptx`,`.pptm`,`.ppsm`,`.ppsx`,`.xlsx`,`.xls`,`.xlam`,`.xlsm`,`.xltx`,`.xltm`,`.c`,`.h`,`.cpp`,`.hpp`,`.cs`,`.java`,`.py`,`.go`,`.rb`,`.scala`,`.m`,`.sql`,`.clj`,`.mp3`,`.wav`,`.m4a`,`.flac`,`.ogg`,`.mp4`,`.mov`,`.m4v`.
- 
                File uploads are limited to 500 MB for PDF, Word, and PowerPoint files, and 50 MB for all other supported file types. 
- 
                Spaces support up to 10,000 files (compared to 20 files in regular chat conversations), as long as the total space storage is less than 10 GB. 
- 
                You can add at most 20 resources of a specific resource type (dashboard, topic, knowledge base, or action) to a space.