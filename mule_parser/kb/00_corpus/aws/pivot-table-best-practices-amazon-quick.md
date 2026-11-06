# Pivot table best practices - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/pivot-table-best-practices.html](https://docs.aws.amazon.com/quick/latest/userguide/pivot-table-best-practices.html)

---

It's best to deploy a minimal set of rows, columns, metrics, and table calculations, rather than offering all possible combinations in one pivot table. If you include too many, you risk overwhelming the viewer and you can also run into the computational limitations of the underlying database.

To reduce the level of complexity and reduce the potential for errors, you can take the following actions:

- 
					Apply filters to reduce the data included in for the visual. 
- 
					Use fewer fields in the **Row**and**Column**field wells.
- 
					Use as few fields as possible in the **Values**field well.
- 
					Create additional pivot tables so that each displays fewer metrics. 

In some cases, there's a business need to examine many metrics in relation to each other. In these cases, it can be better to use multiple visuals on the same dashboard, each showing a single metric. You can reduce the size of the visuals on the dashboard, and colocate them to form a grouping. If a decision the viewer makes based on one visual creates the need for a different view, you can deploy custom URL actions to launch another dashboard according to the choices made by the user.

It's best to think of visuals as building blocks. Rather than using one visual for multiple purposes, use each visual to facilitate one aspect of a larger business decision. The viewer should have enough data to make a well-informed decision, without being overwhelmed by the inclusion of all possibilities.