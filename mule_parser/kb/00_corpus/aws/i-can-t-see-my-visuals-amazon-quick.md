# I can't see my visuals - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/troubleshoot-adding-visuals.html](https://docs.aws.amazon.com/quick/latest/userguide/troubleshoot-adding-visuals.html)

---

Use the following section to help you troubleshoot missing visuals. Before you
				continue, check to make sure you can still access your data source. If you can't
				connect to your data source, see [Data source connectivity issues for Amazon Quick Sight](./troubleshoot-connect-to-datasources.html).

- 
					If you are having trouble adding a visual to an analysis, try the following: - 
							Check your connectivity and confirm that you have access to all domains that Quick Sight uses for access. To see a list of all URLs Quick Sight uses, see [Domains accessed by Quick Sight](https://docs.aws.amazon.com//quicksight/latest/developerguide/vpc-interface-endpoints.html#vpc-interface-endpoints-restrictvpc-interface-endpoints-supported-domains).
- 
							Check that you aren't trying to add more objects than the quota allows. Amazon Quick Sight supports up to 30 datasets in a single analysis, up to 30 visuals in a single sheet, and a limit of 20 sheets per analysis. 
- 
							Suppose that you are editing an analysis for a selected data source and the connection to the data source ends unexpectedly. The resulting error state can prevent further changes to the analysis. In this case, you can't add more visuals to the analysis. Check for this state. 
 
- 
							
- 
					If your visuals don't load, try the following: - 
							If you are using a corporate network, seek out help from your network administrator and verify that the network's firewall settings permit traffic from `*.aws.amazon.com`,`amazonaws.com`,`wss://*.aws.amazon.com`, and`cloudfront.net`.
- 
							Add exceptions to your ad blocker for `*.aws.amazon.com`,`amazonaws.com`,`wss://*.aws.amazon.com`, and`cloudfront.net`.
- 
							If you are using a proxy server, verify that `*.quicksight.aws.amazon.com`and`cloudfront.net`are added to the list of approved domains (the allow list).
 
-