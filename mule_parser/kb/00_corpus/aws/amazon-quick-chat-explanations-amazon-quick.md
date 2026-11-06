# Amazon Quick chat explanations - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/chat-explanations.html](https://docs.aws.amazon.com/quick/latest/userguide/chat-explanations.html)

---

In Amazon Quick, when you chat with dashboards and datasets, each answer includes an Explanation that shows how the model arrived at each numerical claim, including the data sources, assumptions, filters, calculations, and SQL queries that the model used. Instead of manually verifying each answer by finding the original source and re-creating the logic, you can directly see the model's assumptions at the click of a button.

![An Explanation button appears at the bottom of chat answers that contain numerical claims from structured sources.](/images/quick/latest/userguide/images/chat-explanation-button.png) 

             
             
        ## Chat with your dashboards

            When you chat with your dashboard data, open the Explanation to see which dashboards and sheets were selected. You can also see which filters were applied. This helps you validate whether the answer matches your intent.

For example, suppose you open your "Test Drive Conversion" dashboard and ask "what electric car models have an almost perfect satisfaction score but a low conversion rate?" You want to see if some cars test drive well but don't result in a sale. You open the Explanation and check the Assumptions section. Chat defined "electric car model" by using the vehicle model naming terminology. It searched for names that ended with "E" (electric) or "SE" (sport electric). Although that might be correct in most cases, the best field to ensure accuracy is "vehicle_fueltype". You type that directly in the chat: "use the vehicle fuel type for identifying electric cars." You then open the refreshed and correct Explanation.

![Explanation with sample data showing "electric" defined as models ending with 'E', 'SE', or containing 'SE ALL4'.](/images/quick/latest/userguide/images/chat-explanation-dashboard-assumptions.png) 

                 
                 
            ![Updated Explanation with corrected definition, using fuel type equals electric.](/images/quick/latest/userguide/images/chat-explanation-dashboard-corrected.png) 

                 
                 
            ### Explanation components

- 
                        **Found data in**– Displays the dashboards and corresponding sheets where the insight came from.
- 
                        **Filters**– Lists dashboard filter values that were used to arrive at the answer.
- 
                        **Assumptions**– Unpacks any large language model (LLM)-derived definitions from either the data directly (like referencing agent instructions) or from world knowledge.
- 
                        **Calculation explained**– Shows any calculations that the model performed to arrive at the answer, presented in both natural language and as a math formula.

## Chat with your datasets

            When you chat directly with your datasets, you can see the SQL queries that are generated. Use these queries to verify that the model understood your intent. In the car dealer example, suppose you ask "what's the no-show rate, and which car model struggles with it the most?"

- 
                    **Found data in**– Displays the datasets where the insight came from.
- 
                    **Assumptions**– Unpacks any LLM-derived definitions from either the data directly (like referencing dataset-level descriptive metadata) or from world knowledge.
- 
                    **Calculation explained**– Shows any calculations that the model performed to arrive at the answer, presented in both natural language and as a math formula.
- 
                    **Generated SQL**– Displays the specific SQL query that produced each numerical claim.

![Explanation panel for a dataset-sourced answer, displaying the SQL queries that produced each claim.](/images/quick/latest/userguide/images/chat-explanation-dataset-sql.png)