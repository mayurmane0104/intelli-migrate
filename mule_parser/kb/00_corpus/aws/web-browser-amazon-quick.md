# Web browser - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/actions-web-browser.html](https://docs.aws.amazon.com/quick/latest/userguide/actions-web-browser.html)

---

## Overview

        Browser actions provide a comprehensive automation toolkit for performing web interactions. Browser sessions are automatically managed — opened, maintained, and closed as needed. Quick Automate supports flexible element identification through AI-powered natural language descriptions and precise XPath selectors. Key capabilities include intelligent element targeting with fallback mechanisms, self-healing features that automatically handle popups and retry failed actions, data extraction including structured table content, and a full suite of interaction methods from basic clicks and typing to advanced AI-driven multi-step tasks.

**Element identification methods**

- **Description method:**Uses AI to identify elements using natural language descriptions (e.g., "Log In button"), making automations more resilient to UI changes.
- **XPath selector method:**Uses precise XPath expressions for exact element targeting (e.g.,- `//button[text()='Log in']`).
- **Combined approach:**When both methods are enabled, XPath is tried first before falling back to the description method, combining precision with adaptability.

**Self-Healing features available for type-ins and clicks**

- **HandlePopups:**Automatically detects and handles unexpected dialogs, cookie notices, and overlays, preventing blocking elements from interrupting workflows.
- **ValidateAndRetry:**Verifies action success through screenshot comparison and retries if needed, reducing false failures.

## Browser Session Management

        Browser instances are automatically created, maintained throughout workflows, and properly cleaned up when complete. The `restart_browser` action allows fresh sessions when needed for scenarios such as login timeouts or session expiration.

## Start Browser Session

        Opens a new browser session. Actions inside is scope interact with this browser. The browser closes automatically when finished.

**Properties:**

- **Action Title**(text-only): The title of the action displayed in the process visualization (default: Browser)

###### Note

- All browser actions must be placed within a browser session scope 
- Each browser scope is a browser session. Browser automatically closes when actions inside a scope completes. 

## Go to Webpage

        Navigates to a specific URL. Used to go to a new webpage in the current browser tab.

**Properties:**

- **URL**(required): The web address to navigate to (e.g., "example.com") Note: Please provide the complete URL when working with this.

## Click

        Clicks on a webpage element. Used to interact with buttons, links, or other clickable elements.

**Properties:**

- **Find Element with Description**(radio button): Use natural language description to identify the element with AI (default: ON)- **Description Field**(conditionally required): Natural language description of the browser element to click (e.g., "Submit button"). Don't use the action in the element, just the description of the element
 
- **Find Element with Selector**(radio button): Use XPath expression to identify the element (default: OFF)- **XPath Field**(conditionally required): XPath expression (e.g., "//input[@id='xyz']")
 
- **Self-healing**(checkbox): Use AI to handle unexpected popups automatically (default: OFF, optional)
- **Mouse Button**(dropdown): Which mouse button to click - Left, Middle, or Right (default: Left, optional)
- **Click Type**(dropdown): Single or Double click (default: Single, optional)
- **Get File Download**(radio button): Enable if click downloads a file (default: OFF, optional)
- **Downloaded File**(output, conditionally required): Variable name storing the downloaded file (default: downloaded_file)

**Element Identification:**

- At least one element identification method must be enabled 
- When both methods are enabled, XPath selector is tried first before falling back to description 

## Enter Text

        Types text into an input field. Used to fill in forms, search boxes, or other text inputs on webpages.

**Properties:**

- **Text to Enter**(required): The text you want to type into the field (e.g., "Order #12345")
- **Find Element with Description**(radio button): Use natural language description to identify the element with AI (default: ON)- **Description Field**(conditionally required): Natural language description (e.g., "Order number field")
 
- **Find Element with Selector**(radio button): Use XPath expression to identify the element (default: OFF)- **XPath Field**(conditionally required): XPath expression (e.g., "//input[@id='xyz']")
 
- **Self-healing**(checkbox): Use AI to handle unexpected popups automatically (default: OFF, optional)
- **Replace Existing Text**(checkbox): Clear any pre-existing text in the field before typing (default: ON)

**Element Identification:**

- At least one element identification method must be enabled. Recommended to use element description and move to element selector only if required. 

## Enter Credential

        Types a username or password. Used to securely sign in to a website using saved credentials.

**Properties:**

- **Credential**(dropdown, required): Choose which saved credential to use from automation group
- **Value to Enter**(dropdown, required): Choose whether to enter Username or Password (default: Username)
- **Find Element with Description**(radio button): Use natural language description to identify the element with AI (default: ON)- **Description Field**(conditionally required): Natural language description (e.g., "Username field")
 
- **Find Element with Selector**(radio button): Use XPath expression to identify the element (default: OFF)- **XPath Field**(conditionally required): XPath expression (e.g., "//input[@id='username']")
 
- **Self-healing**(checkbox): Use AI to handle unexpected popups automatically (default: OFF, optional)

**Element Identification:**

- At least one element identification method must be enabled 

## Select from Dropdown

        Chooses a value from a dropdown. Used to make selections in forms, filters, or other dropdown menus on webpages.

**Properties:**

- **Value to Select**(required): The option you want to select from the dropdown field (e.g., "Complete")
- **Find Element with Description**(radio button): Use natural language description to identify the element with AI (default: ON)- **Description Field**(conditionally required): Natural language description (e.g., "Order status dropdown")
 
- **Find Element with Selector**(radio button): Use XPath expression to identify the element (default: OFF)- **XPath Field**(conditionally required): XPath expression (e.g., "//select[@id='xyz']")
 
- **Self-healing**(checkbox): Use AI to handle unexpected popups automatically (default: OFF, optional)

**Element Identification:**

- At least one element identification method must be enabled 

## Extract Text

        Reads a value from a webpage. Used to capture the text from an individual field.

**Properties:**

- **Find Element with Description**(radio button): Use natural language description to identify the element with AI (default: ON)- **Description Field**(conditionally required): Natural language description (e.g., "Total amount field")
 
- **Find Element with Selector**(radio button): Use XPath expression to identify the element (default: OFF)- **XPath Field**(conditionally required): XPath expression (e.g., "//input[@id='xyz']")
 
- **Self-healing**(checkbox): Use AI to handle unexpected popups automatically (default: OFF, optional)
- **Extracted Text**(output): Variable name storing the extracted text (default: extracted_text)

**Element Identification:**

- At least one element identification method must be enabled 

## Extract Table

        Reads data from a webpage table. Used to capture structured information found in tables.

Intelligently extracts structured data from web pages using natural language targeting or XPath selectors. Features include AI-enhanced extraction, multiple attribute extraction (text, links, etc.), automatic column generation for attributes, and data table output for programmatic manipulation.

**Properties:**

- **Find Element with Description**(radio button): Use natural language description to identify the element with AI (default: ON)- **Description Field**(conditionally required): Natural language description (e.g., "Order details table")
 
- **Find Element with Selector**(radio button): Use XPath expression to identify the element (default: OFF)- **XPath Field**(conditionally required): XPath expression (e.g., "//table[@id='xyz']")
 
- **Self-healing**(checkbox): Use AI to handle unexpected popups automatically (default: OFF, optional)
- **Extract Multiple Pages**(radio button): Continue extracting data from additional pages if they exist (default: OFF, optional)
- **Next Page Button Selector**(conditionally displayed): XPath expression for next page button (e.g., "//*[@id='nextButton']", optional)
- **Intelligent Data Extraction**(checkbox): Use AI to extract and structure data from complex tables (default: ON). Do not use for large table sizes of 100 rows or more. This option should be used for complex tables or table-like structures, where normal table extraction from a web browser fails
- **Data to Extract**(multi-select dropdown): Choose what to extract - Text, Links (Href), or Element selectors (Xpath) (default: Text, optional)
- **Extracted Table**(output): Variable name storing the extracted data table (default: extracted_table)

**Element Identification:**

- At least one element identification method must be enabled 

**Usage Notes:**

- Additional data types are saved in separate columns (e.g., columnName_Href for Links) 
- Disable intelligent extraction for tables with 100+ rows for better performance 

## Take Screenshot

        Captures an image of the webpage. The screenshot is saved to a file to be used later in your process.

**Properties:**

- **File Name**(optional): Name for the saved image file. Auto-generated if empty (e.g., "Screenshot image")
- **File Type**(dropdown): Choose the image format - PNG or JPEG (default: PNG, optional)
- **Screenshot File**(output): Variable name storing the screenshot file (default: screenshot_file)

## Visual Q&A

        Answer questions about a webpage. Uses AI to visually analyze the page and answer true/false questions about the content.

**Properties:**

- **Question**(required): Enter your true/false question about the webpage content (e.g., "Is the product in-stock?")
- **Self-healing**(checkbox): Use AI to handle unexpected popups automatically (default: OFF, optional)
- **Answer**(output): Variable name storing the true/false response (default: is_true)

## Click and Upload Files

        Uploads files to a webpage. Used to automate file pickers by clicking on a file upload button and choosing the files to upload.

**Properties:**

- **Files to Upload**(required): The list of files to be uploaded, typically stored in a variable (e.g., [my_file1, my_file2])
- **Find Element with Description**(radio button): Use natural language description to identify the element with AI (default: ON)- **Description Field**(conditionally required): Natural language description (e.g., "Upload button")
 
- **Find Element with Selector**(radio button): Use XPath expression to identify the element (default: OFF)- **XPath Field**(conditionally required): XPath expression (e.g., "//input[@id='xyz']")
 
- **Self-healing**(checkbox): Use AI to handle unexpected popups automatically (default: OFF, optional)
- **Mouse Button**(dropdown): Which mouse button to click - Left, Middle, or Right (default: Left, optional)
- **Click Type**(dropdown): Single or Double click (default: Single, optional)

**File Requirements:**

- Must be an array of media/file objects 

**Element Identification:**

- At least one element identification method must be enabled 

## Enter Keystroke

        Sends a key command or shortcut. Used to automate typing individual keys or key combinations on a webpage.

**Properties:**

- **Special Keys**(dropdown, required): Select modifiers like Ctrl, Alt, Shift or singular keystrokes like Enter, Tab, Pagedown
- **Command Key**(optional): Enter the key to be used in combination with the Special key (e.g., "c" for Ctrl+c)
- **Find Element with Description**(radio button): Use natural language description to identify the element with AI (default: ON)- **Description Field**(conditionally required): Natural language description (e.g., "Search bar")
 
- **Find Element with Selector**(radio button): Use XPath expression to identify the element (default: OFF)- **XPath Field**(conditionally required): XPath expression (e.g., "//input[@id='xyz']")
 
- **Self-healing**(checkbox): Use AI to handle unexpected popups automatically (default: OFF, optional)

**Element Identification:**

- Both element toggles can be OFF - keystroke is sent to the current active field if no element is defined 

## Wait for Element

        Checks for an element to appear. Used to wait for changes or validate conditions on a webpage. Returns true if the element is found within the maximum wait time, false if not.

**Properties:**

- **Action Title**(text-only): Display name for the action
- **Element Selector**(required): XPath expression to define the element you want to check (e.g., "//input[@id='xyz']")
- **Max Wait Time**(optional): Maximum time to wait in seconds for the element to appear (default: 30)
- **Element Found**(output): Variable name storing whether the element was found (True/False) (default: is_found)

**Validation:**

- Max wait time must be an integer or decimal 

## Find Matching Elements

        Gets elements matching a pattern. Used to get a list of similar elements on a webpage that you can process one by one.

**Properties:**

- **Element Selector**(required): XPath expression to define the pattern for elements you want to get (e.g., "//div[@class='abc']")
- **List of Elements**(output): Variable name storing the list of found elements (default: element_list)

**Usage Notes:**

- The list is empty if no matching elements are found 
- Use for processing multiple similar elements like search results or hyperlinks 

## Wait for New Window

        Checks for a new window to open. Used after clicking a link or button that opens a new child window in the current browser session.

**Properties:**

- **Max Wait Time**(optional): Maximum time to wait in seconds for the new window to appear (default: 30)
- **Window Identifier**(output): Variable name storing the identifier for the new window (default: window_id)

**Usage Notes:**

- If time exceeds and window not found, an exception occurs 
- Window identifier can be used to switch focus or close the window 

**Validation:**

- Max wait time must be an integer or decimal 

## Switch Window

        Changes browser windows. After switching focus to the specified window, subsequent browser actions interact with that window.

**Properties:**

- **Window Identifier**(optional): The window you want to switch to, typically stored in a variable (e.g., window_id). Leave empty to switch to the main window

## Close Window

        Closes a browser window. Once closed, the automation returns to the main window of the current browser session.

**Properties:**

- **Window Identifier**(required): The window you want to close, typically stored in a variable (e.g., window_id)

## Save to Clipboard

        Copies text to the clipboard. Used to save text that you can paste later on. Existing clipboard text is replaced.

**Properties:**

- **Text to Save**(required): The text you want to copy to the clipboard (e.g., "Order #12345")

## Paste from Clipboard

        Inserts text from the clipboard. Used to paste copied text into webpage fields.

**Properties:**

- **Find Element with Description**(radio button): Use natural language description to identify the element with AI (default: ON)- **Description Field**(conditionally required): Natural language description (e.g., "Order number field")
 
- **Find Element with Selector**(radio button): Use XPath expression to identify the element (default: OFF)- **XPath Field**(conditionally required): XPath expression (e.g., "//input[@id='xyz']")
 
- **Self-healing**(checkbox): Use AI to handle unexpected popups automatically (default: OFF, optional)
- **Replace Existing Text**(checkbox): Clear any pre-existing text in the field before pasting (default: ON)

**Element Identification:**

- At least one element identification method must be enabled 

## Refresh Webpage

        Reloads the current webpage. Some pages may redirect on refresh.

**Properties:**

- **Action Title**(text-only): Display name for the action

## Restart Browser

        Closes and reopens the browser. A new session starts from a blank page.

**Properties:**

- **Restart All**(checkbox): Close and restart all browser windows, not just the current one (default: OFF, optional)

## Limitations

        **Element Identification Uncertainty**: If the AI cannot reliably identify UI elements, actions fail with 'LowConfidence' errors. In these cases, use more specific XPath selectors or element descriptions. **Browser Compatibility**: The system operates exclusively with Chrome browser instances and utilizes Playwright as the underlying automation framework, which means compatibility is limited to Chrome-supported web technologies and may not work with browser-specific features from other vendors. **Dynamic Content Challenges**: Highly dynamic pages with frequent layout changes, heavy JavaScript frameworks, or complex single-page applications may require additional wait times, retry logic, or specialized handling approaches. **Performance Overhead**: AI-powered features like natural language element targeting and self-healing capabilities require more processing time than direct XPath targeting.