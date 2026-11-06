# map | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/dataweave/latest/dw-core-functions-map](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-map)

---

```
%dw 2.0
output application/json
---
["jose", "pedro", "mateo"] map (value, index) -> { (index) : value}
```
DataWeave# map

## map<T, R>(@StreamCapable items: Array<T>, mapper: (item: T, index: Number) -> R): Array<R>

Iterates over items in an array and outputs the results into a new array.

### Parameters

| Name | Description | 
|---|---|
| 
 | The array to map. | 
| 
 | Expression or selector used to act on each  | 

### Example

This example iterates over an input array (`["jose", "pedro", "mateo"]`) to
produce an array of DataWeave objects. The anonymous function
`(value, index) → {index: value}` maps each item in the input to an object.
As `{index: value}` shows, each index from the input array becomes a key
for an output object, and each value of the input array becomes the value of
that object.

#### Source

#### Output

`[ { "0": "jose" }, { "1": "pedro" }, { "2": "mateo" } ]`JSON### Example

This example iterates over the input array (`['a', 'b', 'c']`) using
an anonymous function that acts on the items and indices of the input. For
each item in the input array, it concatenates the `index + 1` (`index` plus 1)
with an underscore (`_`), and the corresponding `value` to return the array,
`[ "1_a", "2_b", "3_c" ]`.

#### Source

```
%dw 2.0
output application/json
---
['a', 'b', 'c'] map ((value, index) -> (index + 1) ++ '_' ++ value)
```
DataWeave#### Output

`[ "1_a", "2_b", "3_c" ]`JSON### Example

If the parameters of the `mapper` function are not named, the index can be
referenced with `$$`, and the value with `$`. This example
iterates over each item in the input array `['joe', 'pete', 'matt']`
and returns an array of objects where the index is selected as the key.
The value of each item in the array is selected as the value of
the returned object. Note that the quotes around `$$`
are necessary to convert the numeric keys to strings.

#### Source

```
%dw 2.0
output application/json
---
['joe', 'pete', 'matt'] map ( "$$" : $)
```
DataWeave#### Output

```
[
  { "0": "joe" },
  { "1": "pete" },
  { "2": "matt" }
]
```
JSON### Example

This example iterates over a list of objects and transform the values into CSV. Each of these objects represent a CSV row. The `map` operation generates an object with `age` and `address` for each entry in the list. `$` represents the implicit variable under iteration.

#### Source

```
%dw 2.0
output application/csv
---
[{
 "age": 14 ,
 "name": "Claire"
}, {
 "age": 56,
 "name": "Max"
}, {
 "age": 89,
 "name": "John"
}] map {
   age: $.age,
   name: $.name
}
```
DataWeave#### Output

`age,name 14,Claire 56,Max 89,John`CSV

## map(@StreamCapable value: Null, mapper: (item: Nothing, index: Nothing) -> Any): Null

Helper function that enables `map` to work with a `null` value.