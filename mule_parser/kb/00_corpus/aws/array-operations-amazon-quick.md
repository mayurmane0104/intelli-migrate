# Array operations - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/jle-arrays.html](https://docs.aws.amazon.com/quick/latest/userguide/jle-arrays.html)

---

JSON expression language allows generic array manipulation for the following functions:

- 
						`map`– Applies a mapping function to each element of an array and returns a new array with the transformed values.For example, `["map", [1, 2, 3], ["*", ["item"], 2]]`maps each element of the array`[1, 2, 3]`by multiplying it by 2.
- 
						`filter`– Filters an array based on a given condition and returns a new array containing only the elements that satisfy the conditionFor example, `["filter", [1, 2, 3, 4, 5], ["==", ["%", ["item"], 2], 0]]`filters the array`[1, 2, 3, 4, 5]`to include only the even numbers.
- 
						`reduce`– Reduces an array to a single value by applying a reducer function to each element and accumulating the result.For example, `["reduce", [1, 2, 3, 4, 5], ["+", ["acc"], ["item"]], 0]`reduces the array`[1, 2, 3, 4, 5]`to the sum of its elements.
- 
						`get`– Retrieves a value from an object or an array by specifying a key or index.For example, `["get", ["item"], "name"]`retrieves the value of the`"name"`property from the current item.
- 
						`unique`– Given an array returns only unique items inside this array.For example, `["unique", [1, 2, 2]]`returns`[1, 2]`.