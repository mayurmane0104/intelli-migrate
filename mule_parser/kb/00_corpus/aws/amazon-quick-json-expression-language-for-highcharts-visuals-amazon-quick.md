# Amazon Quick JSON expression language for Highcharts visuals - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/highchart-expressions.html](https://docs.aws.amazon.com/quick/latest/userguide/highchart-expressions.html)

---

Highcharts visuals accept most [valid JSON
					values](https://www.w3schools.com/js/js_json_datatypes.asp), standard arithmetic operators, string operators, and conditional
				operators. The following JSON values are not supported for Highcharts
				visuals:

- 
					Functions 
- 
					Dates 
- 
					Undefined values 

Quick authors can use JSON expression language create JSON schemas for a highcharts visual. JSON expression language is used to bind JSON to APIs or datasets to allow dynamic population and modification of JSON structures. Developers can also use JSON expression language to inflate and transform JSON data with concise and intuitive expressions.

With JSON expression language, expressions are represented as arrays, where the
				first element specifies the operation and subsequent elements are the arguments. For
				example, `["unique", [1, 2, 2]]` applies the `unique`
				operation to the array `[1, 2, 2]`, resulting in `[1, 2]`.
				This array-based syntax allows for flexible expressions, that allow complex
				transformations on JSON data.

JSON expression language supports *nested expressions*. Nested
				expressions are expressions that contain other expressions as arguments. For example
					`["split", ["toUpper", "hello world"], " "]` first converts the
				string `hello world` into an uppercase, then splits it into array of
				words, resulting in `["HELLO", "WORLD"]`.

Use the following sections to learn more about JSON expression language for Highcharts visuals in Amazon Quick.