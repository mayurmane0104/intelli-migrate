# Workgroup and output errors when using Athena with Quick Sight - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/troubleshoot-athena-workgroup.html](https://docs.aws.amazon.com/quick/latest/userguide/troubleshoot-athena-workgroup.html)

---

To verify that workgroups are set up properly, check the following settings:

- 
					**The Athena workgroup that's associated with the data source must exist.**To fix this, you can return to the Athena data source settings and choose a different workgroup. For more information, see [Setting Up Workgroups](https://docs.aws.amazon.com/athena/latest/ug/workgroups-procedure.html)in the*Athena User Guide*.Another solution is to have the AWS account administrator recreate the workgroup in the Athena console. 
- 
					**The Athena workgroup that's associated with the data source must be enabled.**An AWS account administrator needs to enable the workgroup in the Athena console. Open the Athena console by using this direct link: [https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/home). Then choose the appropriate workgroup in the**Workgroup**panel and view its settings. Choose**Enable workgroup**.
- 
					**Make sure that you have access to the Amazon S3 output location that's associated with the Athena workgroup.**To grant Amazon Quick Sight permissions to access the S3 output location, the Amazon Quick Sight administrator can edit **Security & Permissions**in the**Manage QuickSight**screen.
- 
					**The Athena workgroup must have an associated S3 output location.**An AWS account administrator needs to associate an S3 bucket with the workgroup in the Athena console. Open the Athena console by using this direct link: [https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/home). Then choose the appropriate workgroup in the**Workgroup**panel and view its settings. Set**Query result location**.