# DataWeave Operators | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/dataweave/latest/dw-operators](https://docs.mulesoft.com/dataweave/latest/dw-operators)

---

```
%dw 2.0
output application/json
---
{ "mathOperators" : [
    { "2 + 2" : (2 + 2) },
    { "2 - 2" : (2 - 2) },
    { "2 * 2" : (2 * 2) },
    { "2 / 2" : (2 / 2) },
    { "[1,2,3] - 1 + 4" : [1,2,3] - 1 + 4},
    { "{a:1, b:2, c:3} - 'a' " : {a:1, b:2, c:3} - "a"},
    { "|2021-03-02T10:39:59| - |P1D| + |PT3H|" : |2021-03-02T10:39:59| - |P1D| + |PT3H|}
  ]
}
```
dataweave# DataWeave Operators

DataWeave supports several operators, including mathematical operators, equality operators, and operators such as prepend, append, and update.

## Mathematical Operators

DataWeave supports the most common mathematical operators:

| Operator | Description | 
|---|---|
| 
 | For addition. | 
| 
 | For subtraction. | 
| 
 | For multiplication. | 
| 
 | For division. | 

In addition to operating with numbers, the `(-)` and `(+)` operators can also operate with complex data structures like arrays, objects, and dates.

The following example uses mathematical operators with different data types:

```
{
  "mathOperators": [
    { "2 + 2": 4 },
    { "2 - 2": 0 },
    { "2 * 2": 4 },
    { "2 / 2": 1 },
    { "[1,2,3] - 1 + 4": [2,3,4] },
    { "{a:1, b:2, c:3} - 'a' ": {"b": 2, "c": 3} },
    { "|2021-03-02T10:39:59| - |P1D| + |PT3H|": "2021-03-01T13:39:59" }]
}
```
json## Equality and Relational Operators

DataWeave supports the following equality and relational operators:

| Operator | Description | 
|---|---|
| 
 | For less than. | 
| 
 | For greater than. | 
| 
 | For less than or equal to. | 
| 
 | For greater than or equal to. | 
| 
 | For equal to. | 
| 
 | Equality operator that tries to coerce one value to the type of the other when the types are different. | 

Note that you can negate these operators by using the [logical operator](#logical_operators), `not`.

The following example uses relational operators:

```
%dw 2.0
output application/json
---
{ "relational" : [
    { "1 < 1" : (1 < 1) },
    { "1 > 2" : (1 > 2) },
    { "1 <= 1" : (1 <= 1) },
    { "1 >= 1" : (1 >= 1) }
  ]
}
```
dataweave```
{ "relational": [
    { "(1 < 1)": false },
    { "(1 > 2)": false },
    { "(1 <= 1)": true },
    { "(1 >= 1)": true }
  ]
}
```
jsonNote that if the operands of the relational operator belong to different types,
DataWeave coerces the right-side operand to the type of the left-side operand.
For example, in the expression `"123" > 12` DataWeave coerces `12` (a Number type)
to `"12"` (a String type) and compares each String value lexicographically.
In the expression `123 > "12"`, DataWeave coerces the String value `"12"` to the Number value `12`
and compares the numbers.

These examples use equality operators:

```
%dw 2.0
output application/dw
---
{ "equality" :
  [
    (1 == 1),
    (1 == 2),
    ("true" == true),
    ("true" ~= true),
    (['true'] ~= [true]),
    ('1' ~= 1)
  ]
}
```
dataweave`{ equality: [ true, false, false, true, true, true ] }`text

## Logical Operators

DataWeave supports the following logical operators:

| Operator | Description | 
|---|---|
| 
 | Negates the result of the input. See also,  | 
| 
 | Negates the result of the input. See also,  | 
| 
 | Returns  | 
| 
 | Returns  | 

| Though the semantics of `not`and`!`are the same, their precedence
differs.`not true or true`is executed as`not (true or true)`,
so it returns`false`, whereas`!true or true`returns`true`because
the`!`only applies to the first`true`.`!(true or true)`returns`false`. | 

The following examples use logical operators:

```
%dw 2.0
var myArray = [1,2,3,4,5]
var myMap = myArray map not (($ mod 2) == 0)
output application/json
---
{
  "not" : [
    "notTrue" : not true,
    "notFalse" : not false,
    "myMapWithNot" : myMap
  ],
  "and" : [
    "andTrueFalse" : true and false,
    "andIsTrue" : (1 + 1 == 2) and (2 + 2 == 4),
    "andIsFalse" : (1 + 1 == 2) and (2 + 2 == 2)
  ],
  "or" : [
    "orTrueFalse" : true or false,
    "orIsTrue" : (1 + 1 == 2) or (2 + 2 == 2),
    "orIsFalse" : (1 + 1 == 1) or (2 + 2 == 2)
  ],
  "!-vs-not" : [
	  "example-!" : (! true or true),
	  "example-not" : (not true or true)
  ]
}
```
dataweaveNote that `myMap` iterates through the items in a list (`myArray`) and
determines whether the modulo (`mod`) expression *does not* evaluate to `0` when
applied to each given item.

```
{
  "not": [
    { "notTrue": false },
    { "notFalse": true },
    { "myMapWithNot": [ true, false, true, false, true ] }
  ],
  "and": [
    { "andTrueFalse": false },
    { "andIsTrue": true },
    { "andIsFalse": false }
  ],
  "or": [
    { "orTrueFalse": true },
    { "orIsTrue": true },
    { "orIsFalse": false }
  ],
  "!-vs-not": [
    { "example-!": true },
    { "example-not": false }
  ]
}
```
jsonNote that `not` works in expressions such as `not (true)`, but `not(true)`
(without the space) does not work.

You can use logical operators together. The following example uses:

- 
`or not`as defined in the`orNot`expression.
- 
`and not`in`andNot`.
- 
`not`and`and not`in`notWithAndNot`.

```
%dw 2.0
var orNot = if (1 + 1 == 4 or not 1 == 2) {"answer": "orNot - Condition met"}
             else {"answer": "nope"}
var andNot = if (1 + 1 == 2 and not 1 == 2) {"answer": "andNot - Condition met"}
             else {"answer": "nope"}
var notWithAndNot = if (not (1 + 1 == 2 and not 1 == 1)) {"answer": "notWithAndNot - Condition met"}
              else {"answer": "nope"}
output application/json
---
{ "answers" :
  [
    orNot,
    andNot,
    notWithAndNot
  ]
}
```
dataweave```
{
  "answers": [
    { "answer": "orNot - Condition met" },
    { "answer": "andNot - Condition met" },
    { "answer": "notWithAndNot - Condition met" }
  ]
}
```
jsonDataWeave executes the code inside each `if` block because all conditional expressions in the example evaluate to `true`.

## Prepend, Append, and Remove Operators for Arrays

DataWeave supports operators for appending and prepending items within an array:

| Operator | Description | 
|---|---|
| 
 | Prepends data on the left-hand side of the operator to items in the
         array on the right-hand side. For example,  | 
| 
 | Appends data on the right-hand side of the operator to items in the
         array on the left-hand side. For example,  | 
| 
 | Appends data on the right-hand side of the operator to items in the
        array on the left-hand side. For example,  | 
| 
 | Removes a specified element of any supported type from an array. | 

The following examples show uses of prepend, append, and remove operators on arrays:

```
%dw 2.0
output application/json
---
{
  "prepend-append" : [
  	 // Array on right side when prepending.
     { "prepend" : 1 >> [2] },
     { "prepend-number" : 1 >> [1] },
     { "prepend-string" : "a" >> [1] },
     { "prepend-object" : { "a" : "b"} >> [1] },
     { "prepend-array" : [1] >> [2, 3] },
     { "prepend-binary" : (1 as Binary) >> [1] },
     { "prepend-date-time" : |23:57:59Z| >> [ |2017-10-01| ] },
  	 // Array is on left side when appending.
     { "append-number" : [1] << 2 },
     { "append-string" : [1] << "a" },
     { "append-object" : [1] << { "a" : "b"} },
     { "append-array" : [1,2] << [1, 2, 3] },
     { "append-binary" : [1] << (1 as Binary) },
     { "append-date-time" : [ |2017-10-01| ] << |23:57:59Z| },
     { "append-object-to-array" : [1,2] << {"a" : "b"} },
     { "append-array-to-array1" : ["a","b"] << ["c","d"] },
     { "append-array-to-array2" : [["a","b"],["c","d"]] << ["e","f"] },
     // + always appends within the array
     { "append-with-+" : [1] + 2 },
     { "append-with-+" : [2] + 1 },
     { "removeNumberFromArray" : ( [1,2,3] - 2 ) },
     { "removeObjectFromArray" : ( [ {a : "b"}, {c : "d"} , { e : "f"} ] - { c : "d"} ) }
  ]
}
```
dataweave```
{
  "prepend-append": [
    { "prepend": [ 1, 2 ] },
    { "prepend-number": [ 1, 1 ] },
    { "prepend-string": [ "a", 1 ] },
    { "prepend-array": [ [ 1 ], 2, 3 ] },
    { "prepend-object": [ { "a": "b" }, 1 ] },
    { "prepend-binary": [ "\u0001", 1 ] },
    { "prepend-date-time": [ "23:57:59Z", "2017-10-01" ] },
    { "append-number": [ 1, 2 ] },
    { "append-string": [ 1, "a" ] },
    { "append-object": [ 1, { "a": "b" } ] },
    { "append-array": [ 1, 2, [ 1, 2, 3 ] ] },
    { "append-binary": [ 1, "\u0001" ] },
    { "append-date-time": [ "2017-10-01", "23:57:59Z" ] },
    { "append-object-to-array": [ 1, 2, { "a": "b" } ] },
    { "append-array-to-array1": [ "a", "b", ["c","d"] ] },
    { "append-array-to-array2": [ ["a","b"], ["c","d"], ["e","f"] ] },
    { "append-with-+": [ 1, 2] },
    { "append-with-+": [ 2, 1] },
    { "removeNumberFromArray": [ 1, 3 ] },
    { "removeObjectFromArray": [ { "a": "b" }, { "e": "f" } ] }
  ]
}
```
json## Scope and Flow Control Operators

DataWeave supports operators that control the flow and scope of expressions:

| Operator | Description | 
|---|---|
| 
 | Creates a scope in which new variables, functions, annotations, or namespaces can be declared and used. The syntax is similar to a mapping in that it is composed of a header and body separated by  | 
| 
 | Replaced by  | 

| Operator | Description | 
|---|---|
| 
 | An  | 
| 
 | An  | 

## Update Operator

DataWeave supports the `update` operator, which enables you to update specified fields of a data structure with new values.

*Introduced in DataWeave 2.3.0. Supported by Mule 4.3 and later.*

Versions prior to Mule 4.3 require the following syntax to increase the `age` value in `myInput` by one without recreating the entire object:

`%dw 2.0 var myInput = { "name": "Ken", "lastName":"Shokida", "age": 30 } output application/json --- myInput mapObject ((value,key) -> if(key as String == "age") {(key): value as Number + 1} else {(key): value} )`weave

In Mule 4.3, the `update` operator simplifies the syntax:

`%dw 2.0 var myInput = { "name": "Ken", "lastName":"Shokida", "age": 30 } output application/json --- myInput update { case age at .age -> age + 1 }`weave

Both DataWeave scripts return the same result:

```
{
  "name": "Ken",
  "lastName": "Shokida",
  "age": 31
}
```
JSONWith `update`, casting or iterating through all the key-value pairs is not necessary.

The `update` syntax is as follows:

`<value_to_update> update { case <variable_name> at <update_expression>[!]? [if(<conditional_expression>)]? -> <new value> ... }`weave

- 
`value_to_update`represents the original value to update.
- 
`update_expression`is the selector expression that matches a value in`value_to_update`.
- 
`variable_name`is the name of the variable to bind to the matched`update_expression`value.
- 
`new_value`is the expression with the new value.
- 
`[if(<conditional_expression>)]?`If`conditional_expression`returns`true`, the script updates the value. Use of a conditional expression is optional.
- 
`[!]`marks the selector as an upsert. If the expression doesn’t find a match, the`!`makes the`update`operator create all the required elements and insert the new value.
- 
`update_expression`supports multiple`case`expressions.

| The `update`operator doesn’t mutate the existing value. Instead, the operator creates a new value with the updated expressions. | 

### Selector Expressions

Use selector expressions with the `update` operator to specify the fields to update.

#### Value Selector

This matching selector can check for matches to any value within an object.

The following example updates a field at the root level and a field in a nested level using the value selector:

`%dw 2.0 var myInput = { "name": "Ken", "lastName":"Shokida", "age": 30, "address": { "street": "Amenabar", "zipCode": "AB1234" } } output application/json --- myInput update { case age at .age -> age + 1 case s at .address.street -> "First Street" }`weave

```
{
  "name": "Ken",
  "lastName": "Shokida",
  "age": 31,
  "address": {
    "street": "First Street",
    "zipCode": "AB1234"
  }
}
```
json#### Index Selector

This matching selector enables you to match any array by its index.

The following example updates an element that is at the first location of the array:

```
{
    "name": "Ken",
    "lastName":"Shokida",
    "age": 30,
    "addresses": [{
        "street": "Amenabar",
        "zipCode": "AB1234"
    }]
}
```
json`%dw 2.0 output application/json --- payload update { case s at .addresses[0] -> { "street": "Second Street", "zipCode": "ZZ123" } }`weave

```
{
  "name": "Ken",
  "lastName": "Shokida",
  "age": 30,
  "addresses": [
    {
      "street": "Second Street",
      "zipCode": "ZZ123"
    }
  ]
}
```
json#### Attribute Selector

This matching selector enables you to match any attribute value.

The following example updates an attribute value and changes it to upper case:

`<user name="leandro"/>`xml`%dw 2.0 output application/xml --- payload update { case name at .user.@name -> upper(name) }`weave

```
<?xml version='1.0' encoding='UTF-8'?>
<user name="LEANDRO"/>
```
xml#### Dynamic Selector

Any selector can incorporate an expression to make the selection dynamic.

The following example dynamically selects and updates the value of a field that is not hardcoded. Such a field can change at runtime. The example uses the variable `theFieldName` to obtain the field with key `name`, and it changes the value of that field to `Shoki`.

```
{
    "name": "Ken",
    "lastName":"Shokida"
}
```
json`%dw 2.0 var theFieldName = "name" output application/json --- payload update { case s at ."$(theFieldName)" -> "Shoki" }`weave

```
{
  "name": "Shoki",
  "lastName": "Shokida"
}
```
json### Conditional Update

The `update` operator has syntax for writing a conditional update if you want to modify a field under a given condition.

The following example updates the category based on the name of the user:

`[{"name": "Ken", "age": 30}, {"name": "Tomo", "age": 70}, {"name": "Kajika", "age": 10}]`json`%dw 2.0 output application/json --- payload map ((user) -> user update { case name at .name if(name == "Ken") -> name ++ " (Leandro)" case name at .name if(name == "Tomo") -> name ++ " (Christian)" } )`weave

```
[
  {
    "name": "Ken (Leandro)",
    "age": 30
  },
  {
    "name": "Tomo (Christian)",
    "age": 70
  },
  {
    "name": "Kajika",
    "age": 10
  }
]
```
json### Upserting

The `update` operator enables you to insert a field that is not present already by using the `!` symbol at the end of the selector expression. When the field is not present, the operator binds a `null` value to the variable.

The following example updates each object in the array `myInput`. If the field `name` is present in the object, the example applies the `upper` function to the value of `name`. If the field `name` is not present in the object, the example appends the key-value pair `"name": "JOHN"` to the object.

`%dw 2.0 var myInput = [{"lastName": "Doe"}, {"lastName": "Parker", "name": "Peter" }] output application/json --- myInput map ((value) -> value update { case name at .name! -> if(name == null) "JOHN" else upper(name) } )`weave

```
[
  {
    "lastName": "Doe",
    "name": "JOHN"
  },
  {
    "lastName": "Parker",
    "name": "PETER"
  }
]
```
json### Sugar Syntax

The `update` operator accepts a default variable named `$` in place of the longer  `<variable_name> at` syntax.

The following example binds the value of the expression `.age` to the default variable name `$`, which is used to express the new value. The longer equivalent is shown in comments.

```
{
    "name": "Ken",
    "lastName":"Shokida",
    "age": 30,
    "address": {
        "street": "Amenabar",
        "zipCode": "AB1234"
    }
}
```
json`%dw 2.0 output application/json --- payload update { //equivalent expression: //case age at .age -> age + 1 case .age -> $ + 1 case .address.street -> "First Street" }`weave

```
{
  "name": "Ken",
  "lastName": "Shokida",
  "age": 31,
  "address": {
    "street": "First Street",
    "zipCode": "AB1234"
  }
}
```
json## Metadata Assignment Operator

DataWeave supports the metadata assignment operator `<~`, which enables you to set the metadata of any value without using the `as` operator.
This operator is useful when you want to set the metadata and retain the current value type. If you are coercing the value to a new type, use [as](dataweave-types-coercion).

*Introduced in DataWeave 2.5.0. Supported by Mule 4.5 and later.*

The operator syntax is as follows:

`<valueB> <~ <objectA>`The operator assigns `objectA` as metadata to `valueB`. The arrow points to the value to which the metadata is assigned.

Versions prior to Mule 4.5 require the following syntax, for example, to add the `class` metadata field to an object:

`%dw 2.0 --- {name: "Ken"} as Object {class: "Person"}`weave

In Mule 4.5, the metadata assignment operator `<~` simplifies the syntax:

`%dw 2.0 --- {name: "Ken"} <~ {class: "Person"}`weave

### Metadata Assignment Using Metadata Annotations

DataWeave adds support for metadata annotations. These special annotations, marked with `@Metadata`, attach a key-value pair metadata to any value where they are used.

*Introduced in DataWeave 2.8.0.*

The following example achieves the same result as the previous one, but by defining an annotation, which is a class that binds the metadata key `class` to the value provided where it is used.

`%dw 2.8 @Metadata(key="class") annotation Class(value: String) --- @Class(value="Person") {name: "Ken"}`weave

Defining metadata using annotations provides the following benefits:

- 
You can define annotations once and reuse them as metadata throughout your code. 
- 
Annotations are additive, and using more than one annotation attaches all the key-value pairs together. 
- 
You get type checking, enabling you to force the value of the annotation to be of a certain type, ensuring consistency. 

However, there are certain restrictions when defining metadata annotations:

- 
Annotations marked with `@Metadata`can only have one parameter.
- 
The parameter must be called `value`.
- 
The metadata key is the value set to the key argument of the metadata annotation, not the name of the annotation itself (In the previous example, the metadata value is associated to the `class`key).
- 
Metadata annotations are additive, so if they are used on a reference that already has metadata, the new metadata is appended. 

The following is an example of a metadata annotation that marks a value as CData for the XML writter.

`%dw 2.8 output application/xml @Metadata(key="cdata") annotation CData(value: true) --- root: { test: @CData(value = true) "testCData" }`weave

```
<?xml version='1.0' encoding='UTF-8'?>
<root>
  <test><![CDATA[testCData]]></test>
</root>
```
xml### Metadata

Metadata is any additional information attached to a value that doesn’t affect its identity. Given any two values
`A` and `B` that are equal, if you attach metadata to `A` and call it `A'`, then `A == A' == B`. So you can define a value that is formed by the value
and the metadata attached to it.