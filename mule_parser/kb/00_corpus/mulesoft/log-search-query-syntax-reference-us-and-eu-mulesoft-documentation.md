# Log Search Query Syntax Reference (US and EU) | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/monitoring/log-search-query-syntax](https://docs.mulesoft.com/monitoring/log-search-query-syntax)

---

`AND`

# Log Search Query Syntax Reference (US and EU)

| 
 | 

On [US](https://anypoint.mulesoft.com/monitoring) and [EU](https://eu1.anypoint.mulesoft.com/monitoring) Clouds, fine tune your search by using log query syntax.

## Search Terms

Search terms consist of terms and operators. Search terms can be either single terms, such as "hello" or phrases, such as "hello dolly".

You can combine multiple terms with boolean operators to form complex queries.

## Term Modifiers

You can modify query terms using the log search query language to provide a wide range of searching options.

## Wildcard Searches

You can use single and multiple character wildcard searches within single terms.

| You can’t use wildcard searches within phrase queries. | 

To perform a single character wildcard search use the `?` symbol. The single character wildcard search looks for terms that match the single character replaced by `?`. For example, to search for "text" or "test" you can use the search:

`te?t`

To perform a multiple-character wildcard search, use the * symbol. Multiple-character wildcard searches look for zero or more characters. For example, to search for test, tests, or tester, use the search:

`test*`

You can also use the wildcard searches in the middle of a term, for example: `te*t`.

| You can’t use a * or `?`symbol as the first character of a search. | 

## Fuzzy Searches

You can perform fuzzy searches by using the tilde~ symbol at the end of a single word term. For example, to search for a term similar in spelling to "roam" you can use the fuzzy search:

`roam˷`

This search returns terms like foam and roams.

## Boolean Operators

Boolean operators allow terms to be combined through logic operators. Log search query language supports `AND`, `+`, `OR`, `NOT` and `-` as Boolean operators.

| Boolean operators must be ALL CAPS. | 

| Boolean Operator | Description | Example | ||
|---|---|---|---|---|
| The  | To search for documents that contain "anypoint monitoring" use the query:
 | |||
| 
 | The  | To search for documents that contain either "monitoring anypoint" or just "monitoring" use the query: 
 or 
 | ||
| 
 | The  | To search for documents that contain "anypoint monitoring" but not "functional", use the query:
 
 | ||
| 
 | Requires that the term after the  | To search for documents that must contain "anypoint" and may contain "monitoring" use the query: 
 | ||
| 
 | Excludes documents that contain the term after the  | To search for documents that contain "anypoint monitoring" but not "results" use the query: 
 | 

## Special Characters

You can escape special characters that are part of the query syntax. The current list of supported special characters includes:

`+ - && || ! ( ) { } [ ] ^ " ~ * ? : \ < >`

To escape these characters, use the `\` before the character. For example, to search for (1+1):2 use the query:

`\(1\+1\)\:2`

## Search Fields

Specify a field name or use the default when performing a search. The field name and default field are specific to the search implementation.

Search any field by typing the field name, followed by a colon, and then the term you are looking for. For example, to find logs with a message that contains "called the function Value Selector" in the app "my-app", enter either of the following:

- 
`appId: "my-app" AND message: "called the function Value Selector"`
- 
`appId: "my-app" AND "called the function Value Selector"`

The default field, `message`, does not require a field indicator in the query.