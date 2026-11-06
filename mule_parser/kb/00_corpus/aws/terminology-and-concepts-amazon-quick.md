# Terminology and concepts - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/quicksight_dev-terminology.html](https://docs.aws.amazon.com/quick/latest/userguide/quicksight_dev-terminology.html)

---

This section provides a list of terms for development in Amazon Quick Sight.

**Anonymous Amazon Quick Sight User:** – A temporary Amazon Quick Sight
			user identity that virtually belongs to a namespace, and is usable only with embedding.
			You can use tag-based rules to implement row-level security for such users.

**Caller identity:** – The identity of the
			AWS Identity and Access Management user making an API request. The identity of the caller is determined by
			Amazon Quick Sight using the signature attached to the request. Through the use of our provided SDK
			clients, no manual steps are necessary to generate the signature or attach it to the
			requests. However, you can do it manually if you want to. 

**Invoker identity:** – In addition to the caller
			identity, but not as a replacement for it, you can assume a caller’s identity through
			the IAM `AssumeRole` API when making calls to Amazon Quick Sight. AWS approves
			callers through their invoker’s identity. This is done to avoid having to explicitly add
			multiple accounts belonging to the same Amazon Quick Sight subscription. 

**Namespace:** – a logical container that allows
			you to isolate user pools so that you can organize clients, subsidiaries, teams, and so
			on. For more information, see [Supporting multitenancy with isolated namespaces](https://docs.aws.amazon.com/quicksight/latest/user/namespaces.html)
		

**QuickSight ARN:** – Amazon Resource Name (ARN).
			Amazon Quick Sight resources are identified using their name or ARN. For example, these are the
			ARNs for a group named `MyGroup1`, a user named `User1`, and a
			dashboard with the ID `1a1ac2b2-3fc3-4b44-5e5d-c6db6778df89`:

`arn:aws:quicksight:us-east-1:111122223333:group/default/MyGroup1 arn:aws:quicksight:us-east-1:111122223333:user/default/User1 arn:aws:quicksight:us-west-2:111122223333:dashboard/1a1ac2b2-3fc3-4b44-5e5d-c6db6778df89`

The following examples show ARNs for a template named `MyTemplate` and a
			dashboard named `MyDashboard`.

- 
				Sample ARN for a template `arn:aws:quicksight:us-east-1:111122223333:template/MyTemplate`
- 
				Sample ARN for a template, referencing a specific version of the template `arn:aws:quicksight:us-east-1:111122223333:template/MyTemplate/version/10`
- 
				Sample ARN for a template alias `arn:aws:quicksight:us-east-1:111122223333:template/MyTemplate/alias/STAGING`
- 
				Sample ARN for a dashboard `arn:aws:quicksight:us-east-1:111122223333:dashboard/MyDashboard`
- 
				Sample ARN for a dashboard, referencing a specific version of the dashboard `arn:aws:quicksight:us-east-1:111122223333:dashboard/MyDashboard/version/10`

Depending on the scenario, you might need to provide an entity’s name, ID, or ARN. You can retrieve the ARN if you have the name, using some of the Amazon Quick Sight API operations.

**Amazon Quick Sight dashboard:** – An entity which
			identifies Amazon Quick Sight reports, created from analyses or templates. Amazon Quick Sight dashboards are
			sharable. With the right permissions, scheduled email reports can be created from them.
			The `CreateDashboard` and `DescribeDashboard` API Operations act
			on the dashboard entity.

**Amazon Quick Sight template:** – An entity which
			encapsulates the metadata required to create an analysis or a dashboard. It abstracts
			the dataset associated with the analysis by replacing it with placeholders. Templates
			can be used to create dashboards by replacing dataset placeholders with datasets that
			follow the same schema that was used to create the source analysis and template.

**Amazon Quick Sight user:** – This is an Amazon Quick Sight user
			identity acted upon by your API call. This user isn't identical to the caller identity
			but might be the one that maps to the user within Amazon Quick Sight.