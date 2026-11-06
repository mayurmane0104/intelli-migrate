# Code - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/actions-code.html](https://docs.aws.amazon.com/quick/latest/userguide/actions-code.html)

---

Code actions in Quick Automate let you implement custom logic using Python code blocks, going beyond what standard automation actions support. They are well-suited for complex data transformations and calculations, and run within a restricted Python environment to maintain security.

**Two Types of Code Actions:**

- **Single Line Expressions:**Quick, one-line operations that modify variables without returning values
- **Custom Code Blocks:**Multi-line Python functions for complex logic with parameters and return values

**When to use code actions:**

Use code blocks when you need to:

- Perform complex data transformations not available in standard actions 
- Implement custom business logic or calculations 
- Process or manipulate data structures (lists, dictionaries, JSON) 
- Work with dates, times, and time zones in custom ways 
- Parse or format strings with complex patterns 
- Optimize automation performance by consolidating multiple actions into one code block 

**When not to use code actions:**

Avoid code blocks when:

- A standard automation action already exists for your use case 
- The operation is simple enough for built-in actions 
- You need to interact with external APIs (use REST API integration instead) 
- You need to access file systems or databases (use appropriate integrations) 

**How to Access code actions:**

Code blocks are available through multiple interfaces:

- **Actions Panel (Recommended):**- Open your automation in the automation builder 
- Click on the Actions Panel on the right side 
- Locate "Custom Code Block" under the Code Actions section 
- Drag and drop the code block into your automation workflow 
 
- **Build with Assistant:**- Available during plan generation when the assistant determines custom code is needed 
- The assistant automatically suggests code blocks for complex operations 
- You can request code blocks by describing your custom logic needs 
 

**Actions available:**

## Single Line Expressions

        Single Line Expressions execute one-line Python statements that perform operations without returning a value. They are ideal for quick modifications to existing variables like appending to lists, updating dictionaries, or performing simple calculations that modify state.

**Properties:**

- Expression (required): The Python expression to execute (e.g., "my_list.append('new item')") 

**Examples:**

- **Appending to list**- `my_list.append("1") my_list.append(new_item)`
- **Removing List Items**- `task_list.remove(completed_task)`

## Custom Code Block

        Custom Code Blocks are multi-line Python functions that execute complex logic, accept parameters, and return values. They are the fallback option when standard automation actions and Single Line Expressions are not sufficient for your needs.

**Properties:**

- **Function Title (required)**: Name identifier for the code block (e.g., "Calculate_Total")
- **Function (required):**Python code block that contains your custom logic.- Step 1: Define Parameters - Click the "Edit" button to open the code editor 
- In the Parameter panel, click "Add" to create new parameters 
- Enter parameter names that match your automation variables 
- Parameters are available as function arguments 
 
- Step 2: Write Your Python Code 
 
- **Return Value (optional):**Variable name to store the function's output- Follow the required code block structure (see below) 
- Implement your custom logic within the function 
- Use only approved libraries and built-in functions 
- Include a return statement if you need to output data 
 

**Code Block Structure**

All code blocks must follow this specific format:

```
@code_block()
def your_function_name(parameter1, parameter2, parameter3):
-------------------------------------------------------------------------------------
    """
    Optional: Add a docstring describing what your function does
    """
    # Your custom logic here
    result = parameter1 + parameter2 + parameter3
    return result
```
**Built-in Python Functions and Imports**

All standard Python built-in functions are available without imports (len, str, int, etc.)

**Approved Standard Libraries (Security Restricted)**

Code blocks can ONLY import these standard libraries:

- `base64`- Base64 encoding/decoding
- `datetime`- Date and time operations
- `json`- JSON parsing and generation
- `math`- Mathematical functions
- `re`- Regular expressions
- `zoneinfo`- Time zone handling

###### Note

- Cannot import standard libraries other than the ones listed above. 
- Cannot install or import third-party libraries. - `pip install`is not supported in code blocks.

**Limitations**

- Restricted Python environment with limited library access. The execution environment is based on RestrictedPython, a subset of Python 3.10. 
- Code blocks cannot invoke other code blocks or actions 

**Best Practices**

- Keep code blocks simple and focused 
- Use descriptive function names 
- Always prefer pre-built actions when available 
- Test your code blocks thoroughly as focused debugging options are limited) 

**Example Use Cases**

- Mathematical operations (Calculate circle properties - radius as parameter - `def function (radius): return { "radius": radius, "diameter": 2 * radius, "circumference": round(2 * math.pi * radius, 2), "area": round(math.pi * radius ** 2, 2) }`
- Getting current date/time - `def function (): now = datetime.datetime.now() return { "current_date": now.strftime("%Y-%m-%d"), "current_time": now.strftime("%H:%M:%S"), "formatted": now.strftime("%B %d, %Y at %I:%M %p"), "iso_format": now.isoformat(), "timestamp": now.timestamp() }`
- Calculating date differences - Start date and end date as parameters - `def function _(start_date_str, end_date_str): # Parse date strings (format: YYYY-MM-DD)_ start = datetime.datetime.strptime(start_date_str, "%Y-%m-%d") end = datetime.datetime.strptime(end_date_str, "%Y-%m-%d") _# Calculate difference_ difference = end - start return { "days": difference.days, "weeks": difference.days // 7, "start": start_date_str, "end": end_date_str }`
- Pattern matching and text manipulation using regular expressions (Validating email addresses, phone numbers, etc.) - `def function (email, phone, zip_code): email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$' phone_pattern = r'^\d{3}-\d{3}-\d{4}$' zip_pattern = r'^\d{5}(-\d{4})?$' return { "email_valid": bool(re.match(email_pattern, email)), "phone_valid": bool(re.match(phone_pattern, phone)), "zip_valid": bool(re.match(zip_pattern, zip_code)) }`
- List Operations (Filter and Transform List) - `def function (numbers, threshold): # Filter numbers above threshold and calculate statistics filtered = [n for n in numbers if n > threshold] if filtered: return { "filtered_numbers": filtered, "count": len(filtered), "sum": sum(filtered), "average": sum(filtered) / len(filtered), "min": min(filtered), "max": max(filtered) } else: return { "filtered_numbers": [], "count": 0, "message": "No numbers above threshold" }`