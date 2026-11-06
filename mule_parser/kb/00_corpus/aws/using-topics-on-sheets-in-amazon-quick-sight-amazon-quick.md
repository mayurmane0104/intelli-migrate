# Using Topics on sheets in Amazon Quick Sight - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/using-q-topics-on-sheets.html](https://docs.aws.amazon.com/quick/latest/userguide/using-q-topics-on-sheets.html)

---

Amazon Quick Sight provides a guided workflow for creating topics. You can step out of the guided workflow and come back to it later, without disrupting your work.

By enabling one or more Quick Sight topics in your analysis workspace, you activate the ML-powered automated data prep , which speeds Natural Language (NL) topic creation. Automated data prep automatically selects high value fields, based on how they are used and on common Q&A needs. It automatically chooses user-friendly field names and synonyms, based on terms from existing analyses and on common dictionaries. It also automatically formats data, so it's immediately useful when presented.

Automated data prep binds the topic to your analysis and prepares an index for searching in natural language. A blue dot denotes this binding. Dashboard users find that the new Amazon Quick Sight topic is automatically selected, making it easier for them to query the dataset.

The following rules apply to working with topics:

- 
            You must be an owner of the underlying dataset before you can create a topic using that dataset or an analysis that uses that dataset. 
- 
            You must be an owner of a topic before you can link the existing topic to an analysis. 

###### To enable a topic

- 
            Open the analysis that you want to use with automated data prep . 
- 
            On the top navigation bar, choose the topic icon. 
- 
            Choose one of the following: - 
                    To activate a new topic, select **Create new topic**and enter a topic title and optional description.
- 
                    To activate an existing topic, select **Update existing topic**and choose the topic from the list.
 
- 
                    
- 
            Choose **ENABLE TOPIC**to confirm your choice.
- 
            When the topic is finished processing, you can use what it learned from the analysis to ask questions in natural language. Now, when users navigate to the dashboard, the linked topic is automatically selected in the search bar. 

After a topic is linked to an analysis, further updates to the analysis are not
        automatically synced to the topic. Authors need to manage updating topics manually from the
            **Topics** page. 

When you enable a topic for an analysis or dashboard, you are starting a process where automated data prep learns from how you analyze your data. Ask it questions, and provide feedback and further information by following the screen prompts. The more you interact with the topic, the better prepared it becomes to answer your questions.

To learn more, see [https://docs.aws.amazon.com/quicksight/latest/user/quicksight-q-starting-from-sheets.html](https://docs.aws.amazon.com/quicksight/latest/user/quicksight-q-starting-from-sheets.html).