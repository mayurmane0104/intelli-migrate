# Quick Flows limits - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/quick-flows-limits.html](https://docs.aws.amazon.com/quick/latest/userguide/quick-flows-limits.html)

---

## Flow limits

        The following limits apply to flow creation and management in your Quick instance:

- **Maximum flows per instance:**10,000 flows
- **Maximum flows per user:**100 flows
- **Maximum steps per flow:**35 steps

## Input limits

        Input limits vary depending on whether you are using General knowledge or Quick data as your data source.

### Text input limits

- **General knowledge:**40,000 characters
- **Quick data:**15,000 characters

### File upload limits

File upload limits depend on your knowledge source and file type:

**File size limits:**

- 
                    **General knowledge:**- Document files: Up to 50 MB (supported file types depend on output preference) 
- Video files: Up to 1 GB 
- Image files: Up to 4.5 MB 
 
- 
                    **Quick data:**- Document files: Up to 50 MB (.pdf, .txt, .rtf, .doc, .docx, .ppt, .pptx, .csv, .xls, .xlsx) 
- Image files: Up to 10 MB (.png, .jpg, .jpeg) 
 

**Maximum number of files:**

- **General knowledge:**Up to 5 files
- **Quick data:**Up to 20 files

**Character limits for file content:**

- 
                    **General knowledge:**- Faster responses: Up to 1M characters total context limit 
- Versatility and Performance: Up to 1M characters total context limit 
 The total context limit includes characters from output prompts defined at build time and characters from input steps and file upload steps at runtime. 
- **Quick data:**665,000 characters

## Output limits

        Output limits control the size of prompts and generated responses:

- 
                **Maximum input prompt size:**- General knowledge: 5,000 characters 
- Quick data: 5,000 characters 
 
- 
                **Maximum output characters rendered:**- General knowledge: Up to 40,000 characters 
- Quick data: 8,000 characters 
 

## Reasoning group limits

        - **Maximum iterations per reasoning group:**50 iterations

When referencing the output of a reasoning group, especially looped content, the output is bound by the input character limits of the receiving step. For larger outputs, consider staging the results and querying them in a later step.

## Schedule limits

        - 
                **Region availability**: Schedules in flows are currently supported in US East (N. Virginia), US West (Oregon), and Europe (Ireland)
- 
                **Maximum schedules per user**: 20 schedules per user
- 
                **Maximum schedules per instance**: 10,000 schedules

## Regional availability

        Certain features have regional limitations:

- 
                **Image generation:**Currently supported in US East (N. Virginia), US West (Oregon), and Europe (Ireland)