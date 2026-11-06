# filter | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/dataweave/latest/dw-core-functions-filter](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-filter)

---

`[9,2,3,4,5] filter (value, index) -> (value > 2)`DataWeave# filter

## filter<T>(@StreamCapable items: Array<T>, criteria: (item: T, index: Number) -> Boolean): Array<T>

Iterates over an array and applies an expression that returns matching values.

The expression must return `true` or `false`. If the expression returns `true`
for a value or index in the array, the value gets captured in the output array.
If it returns `false` for a value or index in the array, that item gets
filtered out of the output. If there are no matches, the output array will
be empty.

### Parameters

| Name | Description | 
|---|---|
| 
 | The array to filter. | 
| 
 | Boolean expression that selects an  | 

### Example

This example returns an array of values in the array that are greater than `2`.

#### Source

#### Output

`[9,3,4,5]`JSON### Example

This example returns an array of all the users with age bigger or equal to 30. The script accesses data of each element from within the lambda expression.

#### Source

```
%dw 2.0
---
[{name: "Mariano", age: 37}, {name: "Shoki", age: 30}, {name: "Tomo", age: 25}, {name: "Ana", age: 29}]
          filter ((value, index) -> value.age >= 30)
```
DataWeave#### Output

```
[
   {
     "name": "Mariano",
     "age": 37
   },
   {
     "name": "Shoki",
     "age": 30
   }
]
```
JSON### Example

This example returns an array of all items found at an index (`$$`)
greater than `1` where the value of the element is less than `5`. Notice that
it is using anonymous parameters as selectors instead of using named
parameters in an anonymous function.

#### Source

```
%dw 2.0
output application/json
---
[9, 2, 3, 4, 5] filter (($$ > 1) and ($ < 5))
```
DataWeave#### Output

`[3,4]`JSON### Example

This example reads a JSON array that contains objects with `user` and `error` keys, and uses the `filter` function to return only the objects in which the value of the `error` key is `null`.

#### Source

```
%dw 2.0
output application/json
var users = [
   {
      "user": {
         "name": "123",
         "lastName": "Smith"
      },
      "error": "That name doesn't exists"
   },
   {
      "user": {
         "name": "John",
         "lastName": "Johnson"
      },
      "error": null
   }
]
---
users filter ((item, index) -> item.error == null)
```
DataWeave#### Output

```
[
  {
    "user": {
      "name": "John",
      "lastName": "Johnson"
    },
    "error": null
  }
]
```
JSON### Example

This example reads a JSON array and uses the `filter` function to extract the phone numbers that are active.

#### Source

```
%dw 2.0
output application/json
---
{
    id: payload.Id,
    markCode: payload.marketCode,
    languageCode: payload.languageCode,
    username: payload.profile.base.username,
    phoneNumber: (payload.profile.base.phone filter ($.activeInd == "Y" and $.primaryInd== "Y")).number default []
}
```
DataWeave#### Input

```
{
  "Id": "1184001100000000517",
  "marketCode": "US",
  "languageCode": "en-US",
  "profile": {
  "base": {
     "username": "TheMule",
     "activeInd": "R",
     "phone": [
       {
          "activeInd": "Y",
          "type": "mobile",
          "primaryInd": "Y",
          "number": "230678123"
       },
       {
         "activeInd": "N",
         "type": "mobile",
         "primaryInd": "N",
         "number": ""
       },
       {
          "activeInd": "Y",
          "type": "mobile",
          "primaryInd": "Y",
          "number": "154896523"
       }
      ]
    }
  }
 }
```
JSON#### Output

```
{
  "id": "1184001100000000517",
  "markCode": "US",
  "languageCode": "en-US",
  "username": "TheMule",
  "phoneNumber": [
    "230678123"
    "154896523"
  ]
}
```
JSON## filter(@StreamCapable text: String, criteria: (character: String, index: Number) -> Boolean): String

Iterates over a string and applies an expression that returns matching values.

The expression must return `true` or `false`. If the expression returns `true`
for a character or index in the array, the character gets captured in the output string.
If it returns `false` for a character or index in the array, that character gets
filtered out of the output. If there are no matches, the output string will
be empty.

### Parameters

| Name | Description | 
|---|---|
| 
 | The text to filter. | 
| 
 | The criteria to use. | 

### Example

This example shows how `filter` can be used to remove all characters in odd positions.

#### Source

```
%dw 2.0
output application/json
---
"hello world" filter ($$ mod 2) == 0
```
DataWeave#### Output

`"hlowrd"`Json## filter(@StreamCapable value: Null, criteria: (item: Nothing, index: Nothing) -> Any): Null

Helper function that enables `filter` to work with a `null` value.