# User input steps - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/user-input-steps.html](https://docs.aws.amazon.com/quick/latest/userguide/user-input-steps.html)

---

User input steps collect information from users when they run a flow.

## Text

        The text input step collects free-form text from users. You can set a placeholder, a default value, and allow users to override the default at runtime.

Use placeholder text to guide users on what to enter. For example, you can present a set of options like "Enter 1 for Sales, 2 for Marketing, 3 for Support" to help users provide structured input that your flow can act on.

For configuration instructions, see [Editing flows](./editing-flows.html).

## Files

        The file upload step accepts a document, image, or video from users. You can upload a default file and allow users to override it at runtime. You can upload one file per step.

File uploads are subject to the same size and format restrictions as uploading files in chat. If your content exceeds these limits, consider using a space or knowledge base to process the request instead.

For configuration instructions, see [Editing flows](./editing-flows.html).