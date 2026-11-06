# startsWith - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/startsWith-function.html](https://docs.aws.amazon.com/quick/latest/userguide/startsWith-function.html)

---

`startsWith` evaluates if the expression starts with a substring that
				you specify. If the expression starts with the substring, `startsWith`
				returns true, and otherwise it returns false.

## Syntax

				`startsWith(``expression`,`substring`,`string-comparison-mode`)

## Arguments

				- 
							*expression*
- 
							The expression must be a string. It can be the name of a field that uses the string data type, a literal value like `'12 Main Street'`, or a call to another function that outputs a string.
- 
							*substring*
- 
							The set of characters to check against the *expression*. The substring can occur one or more times in the*expression*.
- 
							*string-comparison-mode*
- 
							(Optional) Specifies the string comparison mode to use: - 
									`CASE_SENSITIVE`– String comparisons are case-sensitive.
- 
									`CASE_INSENSITIVE`– String comparisons are case-insensitive.
 This value defaults to `CASE_SENSITIVE`when blank.
- 
									

## Return type

				Boolean

## Examples

				 
					### Default case sensitive example

The following case sensitive example evaluates if `state_nm`
						startsWith `New`.

`startsWith(``state_nm`,`"New"`)

The following are the given field values.

```
New York
new york
```
For these field values, the following values are returned.

```
true
false
```
### Case insensitive example

The following case insensitive example evaluates if `state_nm`
						startsWith `new`.

`startsWith(``state_nm`,`"new"`, CASE_INSENSITIVE)

The following are the given field values.

```
New York
new york
```
For these field values, the following values are returned.

```
true
true
```
### Example with conditional statements

The `startsWith` function can be used as the conditional
						statement within the following If functions: [avgIf](https://docs.aws.amazon.com/quicksight/latest/user/avgIf-function.html), [minIf](https://docs.aws.amazon.com/quicksight/latest/user/minIf-function.html), [distinct_countIf](https://docs.aws.amazon.com/quicksight/latest/user/distinct_countIf-function.html), [countIf](https://docs.aws.amazon.com/quicksight/latest/user/countIf-function.html),
							[maxIf](https://docs.aws.amazon.com/quicksight/latest/user/maxIf-function.html), [medianIf](https://docs.aws.amazon.com/quicksight/latest/user/medianIf-function.html), [stdevIf](https://docs.aws.amazon.com/quicksight/latest/user/stdevIf-function.html),
							[stdevpIf](https://docs.aws.amazon.com/quicksight/latest/user/stdevpIf-function.html),
							[sumIf](https://docs.aws.amazon.com/quicksight/latest/user/sumIf-function.html), [varIf](https://docs.aws.amazon.com/quicksight/latest/user/varIf-function.html), and [varpIf](https://docs.aws.amazon.com/quicksight/latest/user/varpIf-function.html). 

The following example sums `Sales` only if state_nm starts with
							`New`.

`sumIf(``Sales`,startsWith(`state_nm`,`"New"`))

### Does NOT contain example

The conditional `NOT` operator can be used to evaluate if the
						expression does not start with the specified substring. 

`NOT(startsWith(``state_nm`,`"New"`))

### Example using numeric values

Numeric values can be used in the expression or substring arguments by
						applying the `toString` function.

`startsWith(``state_nm`, toString(`5`) )