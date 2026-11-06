# Adding and removing page breaks to a report - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/qs-reports-page-breaks.html](https://docs.aws.amazon.com/quick/latest/userguide/qs-reports-page-breaks.html)

---

You can add page breaks between sections of a pixel perfect report to organize the way
                data is rendered when the report is published by page. For example, let's say you
                have a report that contains two sections that are each 2.5 pages long. By default,
                    `Section 2` begins on the third page of the report directly following
                the end of `Section 1`. If you add a page break to the end of the
                    `Section 1`, `Section 2` begins on a new page, even if the
                last page of `Section 1` only uses half of a page. This is useful when
                you don't want different sections to share pages, but you don't know how many pages
                each section will need.

###### To add or delete a page break

- 
                    Select your section and choose the **Edit section**icon in the top left corner.
- 
                    In the **Edit section**pane that opens on the left, select the**Page break after**check box.
- 
                    Choose **Apply**.

When you check the **Page break after** box, a page break will
                appear at the end of the section. If you remove the check from the **Page
                    break after** box, the page break is removed from the end of the
                section. Also, the proceeding section renders directly under the last page of the
                section, even if it causes the two sections to share a page.

You can also add or remove a page break from a report by choosing the plus (+)
                icon at the bottom of an existing section and choosing **Add page
                    break** or **Remove page break**.