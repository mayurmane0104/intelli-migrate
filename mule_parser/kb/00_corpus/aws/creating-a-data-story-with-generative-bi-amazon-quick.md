# Creating a data story with Generative BI - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/working-with-stories-create.html](https://docs.aws.amazon.com/quick/latest/userguide/working-with-stories-create.html)

---

Use the following procedure to create a data story with Generative BI.

###### To create a data story

- 
	Open the [Quick console](https://quicksight.aws.amazon.com/).
- 
                At left, choose **Stories**.
- 
                On the **Data stories**page, choose**New Data Story**.
- 
                In the **Story**screen that appears, navigate to the**Build story**modal and input a data story prompt that you would like to generate. For the best results, don't phrase the prompt like a question. Instead, type the data story that you want Quick Sight to build. For example, say you want to create a data story about the most commonly performed medical procedures by region. A good prompt for this use case is "Build a data story about most commonly performed procedures by physicians in various regions. Also, show the specialties where patients are admitted the most. Recommend where we need to staff more physicians by specialty, and include at least four points of supporting data."You can optionally skip this step and manually create your data story. If you choose to forego entering a prompt, you still need to add a visual to the data story. 
- 
                Under **Select visuals**, choose**Add**.
- 
                Choose the dashboard that contains the visuals that you want to use, and then choose the visuals that you want. You can add up to 20 visuals to a data story. If you don't see the dashboard that you want to use, use the **Find your dashboards**search bar at the top of the modal.You can choose visuals from any number of dashboards that you have sharing permissions to. Visuals that show a **Restricted**badge have permissions that restrict them from being added to a data story. A visual might be restricted for one of the following reasons:- 
                        The dataset is connected to a data source that uses trusted identity propagation with Amazon Redshift. 
- 
                        The dataset is located inside of a restricted folder. 
 
- 
                        
- 
                (Optional) Use the **Select documents**section to upload up to 5 documents to be used in the data story. Each document can't exceed 10MB. These documents are only used to generate the data story and are not stored in Quick Sight. The following image shows the**Select documents**section of the**Build story**screen.
- 
                (Optional) If your Quick account is connected to an Amazon Q Business application, check the **Use insights from Amazon Q Business**checkbox to augment your data story with unstructured data sources from Amazon Q Business. For more information about connecting a Quick account to a Amazon Q Business application, see[Augmenting Amazon Quick Sight insights with Amazon Q Business](./generative-bi-q-business.html).
- 
                Choose **Build**.

After the data story generates, review the data story and choose from the following options:

- 
                **Keep**– Saves the generated content to the canvas. When you choose this option, the**Build story**modal closes and you can start editing your data story.
- 
                **Try again**– Allows users to edit the prompt and generate a new data story.
- 
                **Discard**– Deletes the generated data story.