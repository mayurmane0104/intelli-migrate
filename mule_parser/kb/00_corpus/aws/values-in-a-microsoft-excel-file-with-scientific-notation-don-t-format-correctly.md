# Values in a Microsoft Excel file with scientific notation don't format correctly in Quick Sight - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/troubleshooting-number-formatting.html](https://docs.aws.amazon.com/quick/latest/userguide/troubleshooting-number-formatting.html)

---

When you connect to a Microsoft Excel file that has a number column that contains values with scientific notation, they might not format correctly in Quick Sight. For example, the value 1.59964E+11, which is actually 159964032802, formats as 159964000000 in Quick Sight. This can lead to an incorrect analysis.

To resolve this issue, format the column as `Text` in Microsoft Excel,
				and then upload the file to Quick Sight.