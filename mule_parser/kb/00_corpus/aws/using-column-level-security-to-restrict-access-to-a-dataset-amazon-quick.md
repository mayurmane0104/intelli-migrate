# Using column-level security to restrict access to a dataset - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/restrict-access-to-a-data-set-using-column-level-security.html](https://docs.aws.amazon.com/quick/latest/userguide/restrict-access-to-a-data-set-using-column-level-security.html)

---

In the Enterprise edition of Quick, you can restrict access to a dataset
			by configuring column-level security (CLS) on it. A dataset or analysis with CLS enabled
			has the restricted 
				 
					![The lock icon for CLS.](/images/quick/latest/userguide/images/cls-restricted-icon.png) symbol next to it. By default, all users and groups have access to
			the data. By using CLS, you can manage access to specific columns in your
			dataset.

				 
				 
			 symbol next to it. By default, all users and groups have access to
			the data. By using CLS, you can manage access to specific columns in your
			dataset.

If you use an analysis or dashboard that contains datasets with CLS restrictions that you don't have access to, you can't create, view, or edit visuals that use the restricted fields. For most visual types, if a visual has restricted columns that you don't have access to, you can't see the visual in your analysis or dashboard.

Tables and pivot tables behave differently. If a table or pivot table uses restricted
			columns in the **Rows** or **Columns** field wells,
			and you don't have access to these restricted columns, you can't see the visual in an
			analysis or dashboard. If a table or pivot table has restricted columns in the
				**Values** field well, you can see the table in an analysis or
			dashboard with only the values that you have access to. The values for restricted
			columns show as ** Not Authorized**.

To enable column-level security on an analysis or dashboard, you need administrator access.

###### To create a new analysis with CLS

- 
				On the Quick start page, choose the **Analyses**tab.
- 
				At upper right, choose **New analysis**.
- 
				Choose a dataset, and choose **Column-level security**.
- 
				Select the columns that you want to restrict, and then choose **Next**. By default, all groups and users have access to all columns.
- 
				Choose who can access each column, and then choose **Apply**to save your changes.

###### To use an existing analysis for CLS

- 
				On the Quick start page, choose the **Data**tab.
- 
				On the Data page, open your dataset 
- 
				On the dataset details page that opens, for **Column-level security**, choose**Set up**.
- 
				Select the columns that you want to restrict, and then choose **Next**. By default, all groups and users have access to all columns.
- 
				Choose who can access each column, and then choose **Apply**to save your changes.

###### To create a dashboard with CLS

- 
				On the Quick navigation pane, choose the **Analyses**tab.
- 
				Choose the analysis that you want to create a dashboard of. 
- 
				At upper right, choose **Publish**.
- 
				Choose one of the following: - 
						To create a new dashboard, choose **Publish new dashboard as**and enter a name for the new dashboard.
- 
						To replace an existing dashboard, choose **Replace an existing dashboard**and choose the dashboard from the list.
 Additionally, you can choose **Advanced publish options**. For more information, see[Publishing dashboards](./creating-a-dashboard.html).
- 
						
- 
				Choose **Publish dashboard**.
- 
				(Optional) Do one of the following: - 
						To publish a dashboard without sharing, choose **x**at the upper right of the**Share dashboard with users**screen when it appears. You can share the dashboard later by choosing**Share**from the application bar.
- 
						To share the dashboard, follow the procedure in [Sharing Amazon Quick Sight dashboards](./sharing-a-dashboard.html).
 
-