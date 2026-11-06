# Data tables - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/actions-data-tables.html](https://docs.aws.amazon.com/quick/latest/userguide/actions-data-tables.html)

---

Data table actions enable you to work with structured data in table format. These actions allow you to create, transform, and output tabular data in your automations.

## Sort Table

        Orders a table by a column. Used to organize your data in ascending or descending order.

**Properties:**

- **Data Table**(required): The table variable to sort (e.g.,- `my_table`)
- **Column Name to Sort**(required): Name of the column to sort by (e.g., "Total amount")
- **Sort Order**(dropdown): Choose "Ascending" (smallest first) or "Descending" (largest first) - default: Descending
- **Sorted Table**(output): Variable name for the new sorted table

## Filter Table

        Keeps rows matching a criteria. Used to extract relevant rows from a larger data set.

**Properties:**

- **Data Table**(required): The table variable to filter (e.g.,- `my_table`)
- **Filter Expression**(required): Boolean expression using column names and operators (==, >, <, !=). Combine conditions with & (AND) or | (OR). Use single quotes for column names with spaces and text values (e.g., "'Team' == 'Sales' & 'Total amount' > 100")
- **Filtered Table**(output): Variable name for the filtered table

Example filters:

```
# Column 'amount' is greater than 25
"amount > 25"
# Column 'team' equals text 'Sales'
"team == 'Sales'"
# Multiple conditions
"amount > 25 & status == 'active'"
# Grouped conditions
"(amount > 25 & team == 'Sales') | (amount > 50 & team == 'Marketing')"
# Column 'title' contains text 'Director'
"title.str.contains('Director')"
# Column 'Customer No' equals a variable customer_id
"`Customer No` == " + str(customer_id)
# Column 'ProfitCenter' equals variable profitCenter
"`ProfitCenter` == '" + str(profitCenter) + "'"
```
## Lookup Value

        Searches a value in a table. Used to lookup a value in one column and get the corresponding value from another column in the same row.

**Properties:**

- **Data Table**(required): The table to search in (e.g.,- `my_table`)
- **Column Name to Search**(required): Column containing the lookup value (e.g., "Employee ID")
- **Value to Search For**(required): The value to find (e.g., "12345")
- **Column Name to Output**(required): Column to retrieve the result from (e.g., "Date of hire")
- **Cell Value**(output): Variable storing the found value. Returns first match or empty if not found.

## Add Columns

        Creates new columns in a table. Newly added columns are appended to the end of the existing table.

**Properties:**

- **Data Table**(required): The table to modify (e.g.,- `my_table`)
- **Column Names to Add**(required): Array of new column names (e.g., ["Name", "Address"])
- **Default Value**(optional): Initial value for all cells in new columns (e.g., "N/A")
- **Updated Table**(output): Variable name for the modified table

## Remove Columns

        Deletes columns from a table. Outputs a table with all of the remaining columns.

**Properties:**

- **Data Table**(required): The table to modify (e.g.,- `my_table`)
- **Columns to Remove**(required): Array of column names or index numbers. Index numbers start at 0 and can be specific numbers (e.g., [0,1,2]) or ranges (e.g., range(0,2))
- **Updated Table**(output): Variable name for the modified table

## Keep Columns

        Drops extra columns from a table. Used to select a specific subset of columns you want to keep.

**Properties:**

- **Data Table**(required): The table to modify (e.g.,- `my_table`)
- **Columns to Keep**(required): Array of column names to retain (e.g., ["Name", "Address"])
- **Updated Table**(output): Variable name for the modified table

## Add New Row

        Appends a new row to a table. The new row can be created with specific values or as a blank row and is added to the bottom of the table.

**Properties:**

- **Data Table**(required): The table to modify (e.g.,- `my_table`)
- **Row Values**(optional): Array of values for the new row, starting from the first column (e.g., ["Q1", "Sales", 100]). If empty, adds a blank row. Missing values result in blank cells.
- **Updated Table**(output): Variable name for the modified table

## Remove Rows

        Deletes rows from a table. Outputs a table with all of the remaining rows.

**Properties:**

- **Data Table**(required): The table to modify (e.g.,- `my_table`)
- **Rows to Remove**(required): Array of row positions (0-based indexing). Index numbers start at 0 and can be specific numbers (e.g., [0,1,2]) or ranges (e.g., range(0,2))
- **Updated Table**(output): Variable name for the modified table

## Remove Duplicates

        Deletes duplicate rows. Used to create a dataset of unique rows based on specific columns.

**Properties:**

- **Data Table**(required): The table to clean (e.g.,- `my_table`)
- **Columns to Check**(optional): Array of column names for duplicate detection (e.g., ["Name", "Address"]). If empty, checks entire rows for uniqueness. Duplicates are identified by combined values across specified columns.
- **Duplicate Row to Keep**(dropdown): Choose "First" or "Last" occurrence to retain (default: First)
- **Updated Table**(output): Variable name for the modified table

## Append Tables

        Combines the rows of two tables. Used to add data from one table to another.

**Properties:**

- **Table to Append To**(required): Main table receiving additional rows (e.g.,- `main_table`)
- **Table to Add**(required): Source table providing rows to append (e.g.,- `new_data`)
- **Handle Column Differences**(dropdown):- "Add": Keep all columns from both tables 
- "Ignore": Only keep columns matching the primary table 
- "Error": Require exact column matches 
 
- **Combined Table**(output): Variable name for the merged table

## Create New Table

        Creates an empty table. Used to set up a table with required columns to add rows to in subsequent steps. The new table has no rows.

**Properties:**

- **Column Names**(optional): Array of column names for the new table (e.g., ["Name", "Address"]). If empty, creates a table with no columns.
- **New Table**(output): Variable name for the newly created table

## Convert Text to Table

        Transforms delimited text into a structured table.

**Properties:**

- **Text to Convert**(required): Delimited text containing table data (e.g., "Year,Qty 2001,100")
- **Value Separator**(optional): Character separating values in rows (default: ",")
- **Newline Separator**(optional): Character separating rows (default: " ")
- **Has Headers**(checkbox): Whether first row contains column names. If True, uses first row as headers; if False, generates default names (Column0, Column1, etc.)
- **New Table**(output): Variable name for the newly created table

## Convert Table to HTML

        Creates an HTML formatted table. Used to output your table as formatted text for a document, email, and more.

**Properties:**

- **Data Table**(required): The table to format (e.g.,- `my_table`)
- **Formatted Table Text**(output): Variable storing the HTML formatted text

## Examples

        
        **Loop through rows in a table**

To loop through rows in a data table, use the "Loop through items" action under "Process flow". Provide the data table variable as an input for "Collection of items". Update the "Item reference" to `row` as each item represents a single row of the table.

**Use or update cell values in a row**

When looping through rows in a table, refer to individual cell values using the syntax of `row["column name"]` where column name is replaced with the name of the column for the specific cell.

To update the value of a cell in a row, use the "Save value" action under "General". The "Value to save" is the value you want to update the cell with. The "Variable name" is the reference to the cell using the same syntax as above, `row["column name"]`.