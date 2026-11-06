# Managing Public Portal Resources | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/exchange/to-manage-public-portal-resources](https://docs.mulesoft.com/exchange/to-manage-public-portal-resources)

---

```
ACCESS_TOKEN=$(curl https://anypoint.mulesoft.com/accounts/login \
-XPOST -d "username=YOUR_USERNAME&password=YOUR_PASSWORD" | \
jq -r ".access_token")
```
# Managing Public Portal Resources

You can upload up to 100 resources to a public portal. Each image is one resource. Attempting to add more will result in an error. You can delete resources to reduce the number and then add more up to the limit.

These examples show how to list, retrieve, and delete resources from a public portal with the Exchange Experience API.

## Authentication

Log in to Anypoint Platform and get an authentication token. Begin every request with the header `Authorization: bearer ACCESS_TOKEN`.

## Using the API

To list all resources:

```
 curl https://anypoint.mulesoft.com/exchange/api/v2/portals/:organizationDomain/draft/resources \
  -H 'Authorization: bearer YOUR_ACCESS_TOKEN'
```
To get a specific resource:

```
 curl https://anypoint.mulesoft.com/exchange/api/v2/portals/:organizationDomain/draft/resources/:resourceId \
  -H 'Authorization: bearer YOUR_ACCESS_TOKEN'
```
To delete a specific resource:

```
 curl -X DELETE \
  https://anypoint.mulesoft.com/exchange/api/v2/portals/:organizationDomain/draft/resources/:resourceId \
  -H 'Authorization: bearer YOUR_ACCESS_TOKEN'
```
With:

organizationDomain: Your organization's domain resourceId: The image file name.