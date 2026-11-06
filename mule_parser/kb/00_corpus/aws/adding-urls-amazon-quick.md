# Adding URLs - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/using-narratives-expression-editor-urls.html](https://docs.aws.amazon.com/quick/latest/userguide/using-narratives-expression-editor-urls.html)

---

Using the **URL** button on the editing menu of the narrative
				expression editor, you can add static and dynamic URLs (hyperlinks) into a
				narrative. You can also use the following keyboard shortcuts: ⌘+⇧+L or Ctrl+⇧+L. 

A static URL is a link that doesn’t change; it always opens the same URL. A dynamic URL is a link that changes based on the expressions or parameters that you provide when you set it up. It's built with dynamically evaluated expressions or parameters.

Following are of examples of when you might add a static link in your narrative:

- 
					**In an IF statement, you might use the URL in the conditional content.**If you do and a metric fails to meet an expected value, your link might send the user to a wiki with a list of best practices to improve the metric.
- 
					**You might use a static URL to create a link to another sheet in the same dashboard, by using the following steps:**- 
							Go to the sheet that you want to make the link to. 
- 
							Copy that sheet's URL. 
- 
							Return to the narrative editor and create a link using the URL that you just copied. 
 
- 
							

Following are examples of when you might add a dynamic link in your narrative:

- 
					**To search a website with a query, by using the following steps.**- 
							Create a URL with the following link. `https://google.com?q=<<``formatDate(now(),'yyyy-MM-dd')`>>This link sends a query to Google with search text that is the evaluated value of the following. `formatDate(now(), 'yyyy-MM-dd')`If the value of `now()`is`02/02/2020`, then the link on your narrative contains`https://google.com?q=2020-02-02`.
 
- 
							
- 
					**To create a link that updates a parameter.**To do this, create or edit a link and set the URL to the current dashboard or analysis URL. Then add the expression that sets the parameter value to at the end, for example`#p.myParameter=12345`.Suppose that the following is the dashboard link that you start with. `https://us-east-1.quicksight.aws.amazon.com/sn/analyses/00000000-1111-2222-3333-44444444`If you add a parameter value assignment to it, it looks like the following. `https://us-east-1.quicksight.aws.amazon.com/sn/analyses/00000000-1111-2222-3333-44444444``#p.myParameter=12345`For more information on parameters in URLs, see [Using parameters in a URL](./parameters-in-a-url.html).