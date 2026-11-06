# Add SLA Tiers for Anypoint DataGraph | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/api-manager/latest/datagraph-adding-sla-tiers](https://docs.mulesoft.com/api-manager/latest/datagraph-adding-sla-tiers)

---

![The illustration shows the Add SLA tier window](_images/datagraph-add-sla-tier.png) 

# Add SLA Tiers for Anypoint DataGraph

Add multiple SLA tiers to an Anypoint DataGraph instance to control user access and limit requests.

To add an SLA tier:

- 
Navigate to **Anypoint Platform**>**API Manager**.
- 
Click **DataGraph Administration**>**SLA Tiers**:
- 
From the DataGraph SLA Tiers page, click **Add SLA tier**:![The illustration shows the Add SLA tier window](_images/datagraph-add-sla-tier.png)  
- 
In the **# of Reqs**field, add the number of requests a client can make, for example,`100`.
- 
In the **Time Period**field, specify a timeout before a client request fails, for example,`60`.
- 
In the **Time Unit**field, select the unit of time from the drop-down list, for example,`Seconds`.
- 
If you want to display the SLA tier with the contract, select **Visible**.
- 
If you want to create additional SLA tiers, click **Add Limit**.
- 
Click **Add**.