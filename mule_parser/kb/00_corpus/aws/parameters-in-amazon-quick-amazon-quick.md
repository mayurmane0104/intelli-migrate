# Parameters in Amazon Quick - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/parameters-in-quicksight.html](https://docs.aws.amazon.com/quick/latest/userguide/parameters-in-quicksight.html)

---

*Parameters* are named variables that can transfer a
        value for use by an action or an object. By using parameters, you can create an easier way
        for a dashboard user to interact with dashboard features in a less technical way. Parameters
        can also connect one dashboard to another, allowing a dashboard user to drill down into data
        that's in a different analysis.

For example, a dashboard user can use a list to choose a value. That value sets a parameter that in turn sets a filter, calculation, or URL action to the chosen value. Then the visuals in the dashboard react to the user's choices.

To make the parameters accessible to the dashboard viewer, you add a parameter control. You can set up cascading controls, so that a selection in one control filters the options that display in another control. A control can appear as a list of options, a slider, or a text entry area. If you don't create a control, you can still pass a value to your parameter in the dashboard URL.

For a parameter to work, it needs to be connected to something in your analysis, regardless of whether it has a related control. You can reference parameters in the following:

- 
            Calculated fields (except for multivalue parameters) 
- 
            Filters 
- 
            Dashboard and analysis URLs 
- 
            Actions 
- 
            Titles and descriptions throughout an analysis 

Some ways that you can use parameters are the following:

- 
            Using a calculation, you can transform data that is shown in an analysis. 
- 
            If you add a control with a filter to an analysis you are publishing, the dashboard users can filter the data without creating their own filters. 
- 
            Using controls and custom actions, you can let dashboard users set values for the URL actions.