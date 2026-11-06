# Unique values computation - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/unique-values-function.html](https://docs.aws.amazon.com/quick/latest/userguide/unique-values-function.html)

---

The unique values computation counts the unique values in a category field. For example, you can create a computation to count the number of unique values in a dimension, such as how many customers you have

To use this function, you need at least one dimension in the
						**Categories** field well. 

## Parameters

					- *name*
- 
								A unique descriptive name that you assign or change. A name is assigned if you don't create your own. You can edit this later. 
- *Category*
- 
								The category dimension that you want to rank. 

## Computation outputs

					Each function generates a set of output parameters. You can add these outputs to the autonarrative to customize what it displays. You can also add your own custom text.

To locate the output parameters, open the
							**Computations** tab on the right, and locate the
						computation that you want to use. The names of the computations come from
						the name you provide when you create the insight. Choose the output
						parameter by clicking on it only once. If you click twice, you add the same
						output twice. Items displayed in **bold** can
						be used in the narrative. 

- 
							`categoryField`– The category field.- 
									**name**
 
- 
									
- 
							**uniqueGroupValuesCount**