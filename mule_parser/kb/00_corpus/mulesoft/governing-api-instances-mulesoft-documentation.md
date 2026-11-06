# Governing API Instances | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/api-manager/latest/govern-api-instances](https://docs.mulesoft.com/api-manager/latest/govern-api-instances)

---

# Governing API Instances

API Manager is closely integrated with [Anypoint API Governance](../../api-governance/). API Governance helps you ensure that every instance of a governed API conforms to standards, such as which policies are applied or whether a TLS context is required.

To govern an API instance:

## Apply a Governance Ruleset

To govern API instances, you must apply a governance ruleset to your desired API. To apply a governance ruleset, see [Applying Rulesets to Identified APIs](../../api-governance/create-profiles).

To create custom rulesets that enforce your own API management standards, see [Creating Custom Governance Rulesets](../../api-governance/create-custom-rulesets).

## View and Fix Instance Conformance Issues in API Manager

To view the conformance status of an API instance:

- 
Navigate to **Anypoint Platform**>**API Manager**.
- 
Click the name of the API instance for which you want to view the conformance status. **Instance Conformance**appears in the**API Summary**pane.
- 
If the instance is not conformant, select the **Governance Report**page to view nonconformance details for each ruleset.
- 
Click **View details**for each ruleset for more information about the conformance issues.