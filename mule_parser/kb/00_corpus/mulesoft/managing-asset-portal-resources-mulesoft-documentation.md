# Managing Asset Portal Resources | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/exchange/to-manage-asset-portal-resources](https://docs.mulesoft.com/exchange/to-manage-asset-portal-resources)

---

```
ACCESS_TOKEN=$(curl https://anypoint.mulesoft.com/accounts/login \
-XPOST -d "username=YOUR_USERNAME&password=YOUR_PASSWORD" | \
jq -r ".access_token")
```
# Managing Asset Portal Resources

You can upload up to 100 resources to an asset portal. Attempting to add more will result in an error. You can delete resources to reduce the number and then add more up to the limit.

Only image resources can be uploaded to asset portals. Allowed image formats are: `bmp`, `gif`, `ico`, `jpe`, `jpeg`, `jpg`, `png`, `svg`, `tif`, `tiff`, or `webp`. The size limit for an image resource is 2 MB.

These examples show how to list, retrieve, and delete resources from an asset portal with the Exchange Experience API.

## Authentication

Log in to Anypoint Platform and get an authentication token. Begin every request with the header `Authorization: bearer ACCESS_TOKEN`.

## Using the API

To list all resources:

```
curl https://anypoint.mulesoft.com/exchange/api/v2/assets/:groupId/:assetId/:version/portal/draft/resources \
  -H 'Authorization: bearer YOUR_ACCESS_TOKEN'
```
To get a specific resource:

```
curl https://anypoint.mulesoft.com/exchange/api/v2/assets/:groupId/:assetId/:version/portal/draft/resources/:resourceId \
  -H 'Authorization: bearer YOUR_ACCESS_TOKEN'
```
To delete a specific resource:

```
 curl -X DELETE \
  https://anypoint.mulesoft.com/exchange/api/v2/assets/:groupId/:assetId/:version/portal/draft/resources/:resourceId \
  -H 'Authorization: bearer YOUR_ACCESS_TOKEN'
```
With:

groupId: The asset's groupId assetId: The asset's assetId version: The asset's version resourceId: The resource file name.