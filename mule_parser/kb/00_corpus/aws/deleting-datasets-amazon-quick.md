# Deleting datasets - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/delete-a-data-set.html](https://docs.aws.amazon.com/quick/latest/userguide/delete-a-data-set.html)

---

###### Important

Currently, deleting a dataset is irreversible and can cause irreversible loss of work. Deletes don't cascade to delete dependent objects. Instead, dependent objects stop working, even if you replace the deleted dataset with an identical dataset.

Before you delete a dataset, we strongly recommend that you first point each dependent analysis or dashboard to a new dataset.

Currently, when you delete a dataset while dependent visuals still exist, the analyses and dashboards that contain those visuals have no way to assimilate new metadata. They remain visible, but they can't function. They can't be repaired by adding an identical dataset.

This is because datasets include metadata that is integral to the analyses and dashboards that depend on that dataset. This metadata is uniquely generated for each dataset. Although the Quick Sight engine can read the metadata, it isn't readable by humans (for example, it doesn't contain field names). So, an exact replica of the dataset has different metadata. Each dataset's metadata is unique, even for multiple datasets that share the same name and the same fields.

###### To delete a dataset

- 
				Make sure that the dataset isn't being used by any analysis or dashboard that someone wants to keep using. On the **Data**page, choose the dataset that you no longer need. Then choose**Delete Dataset**at upper-right.
- 
				If you receive a warning if this dataset is in use, track down all dependent analyses and dashboards and point them at a different dataset. If this isn't feasible, try one or more of these best practices instead of deleting it: - 
						Rename the dataset, so that the dataset is clearly deprecated. 
- 
						Filter the data, so that the dataset has no rows. 
- 
						Remove everyone else's access to the dataset. 
 We recommend that you use whatever means you can to inform owners of dependent objects that this dataset is being deprecated. Also, make sure that you provide sufficient time for them to take action. 
- 
						
- 
				After you make sure that there are no dependent objects that will stop functioning after the dataset is deleted, choose the dataset and choose **Delete Data Set**. Confirm your choice, or choose**Cancel**.

###### Important

Currently, deleting a dataset is irreversible and can cause irreversible loss of work. Deletes don't cascade to delete dependent objects. Instead, dependent objects stop working, even if you replace the deleted dataset with an identical dataset.