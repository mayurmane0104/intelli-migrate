# Managing API Instance Versions | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/api-manager/latest/manage-versions-instances-concept](https://docs.mulesoft.com/api-manager/latest/manage-versions-instances-concept)

---

# Managing API Instance Versions

After you publish new version details for an API definition to Exchange, you must update the **Asset version** of your deployed API instances in API Manager to reflect the changes.

The API Asset version can only be upgraded or downgraded within the same major version (minor and patch versions). If you need to upgrade to a different major version, you must create a new API Instance.

For more information about versions in Exchange, see [Asset Versions](../../exchange/asset-versions).

To change the asset version of an API instance:

- 
Navigate to **Anypoint Platform**>**API Manager**.
- 
In **API Administration**, click the name of the API instance for which you want to change the version.
- 
Select **Actions**>**Change API specification**.
- 
In **Asset version**, select your desired version.
- 
Click **Change**.

## See Also

- 
[Delete an Asset in Exchange](../../exchange/to-delete-asset)(also describes deprecating an asset)