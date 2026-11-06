# Graphically Construct a Mapping (Design Center) | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/mule-runtime/latest/transform-graphically-construct-mapping-design-center-task](https://docs.mulesoft.com/mule-runtime/latest/transform-graphically-construct-mapping-design-center-task)

---

![A transformation flow from item type and price in a payload](_images/to-transform-data-c2fc6.png) 

# Graphically Construct a Mapping (Design Center)

Through the graphical UI of the Transform component you can do the tasks below. Each task will produce the DataWeave source code that describes the action.

## Map a Field

Drag an element on the input structure over to another on the output structure, this action creates a line that joins these two elements.

![A transformation flow from item type and price in a payload](_images/to-transform-data-c2fc6.png) 

![A table with properties for title, author, item, and year](_images/to-transform-data-afe5b.png) 

## Remove a Mapping

- 
Select the corresponding input element. A trash can icon ![Delete icon](_images/graphically-construct-mapping-design-center-task-2457b.png) appears on the connection. appears on the connection.
- 
Click the trash can icon. 

## Set a Fixed Value or Function

- 
Double click on a field (that doesn’t have any children) in the output tree. This adds a function icon ![Function icon](_images/graphically-construct-mapping-design-center-task-8a822.png) next to it. next to it.
- 
A box with the default value `null`appears. You can change`null`to anything you want, such as:- 
A fixed text value by using " ". 
- 
A reference to an input field. 
- 
A statement that includes DataWeave functions. 
 
- 

This experience relates to that of using a spreadsheet, where each field can be a direct reference to another field, or can be the product of a function that involves such references.

| Functions can be removed by clicking on the trash-can icons that appear next to them. |