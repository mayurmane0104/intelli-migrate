# Consuming a shared Amazon Quick Sight view - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/embedded-view-sharing-sdk-consume.html](https://docs.aws.amazon.com/quick/latest/userguide/embedded-view-sharing-sdk-consume.html)

---

After you create a new shared view, use the Embedding SDK to make the shared view consumable for other users. The examples below set up a consumable shared view for an embedded dashboard in Amazon Quick Sight.

Append the `sharedViewId` to the embed URL, under
                                    ` /views/{viewId}`, and expose this URL to your
                                users. Users can use this URL to will navigate to that shared
                                view.

```
const response = await dashboardFrame.createSharedView();
const newEmbedUrl = await generateNewEmbedUrl();
const formattedUrl = new URL(newEmbedUrl);
formattedUrl.pathname = formattedUrl.pathname.concat('/views/' + response.message.sharedViewId);
const baseUrl = formattedUrl.href;
alert("Click to view this QuickSight shared view", baseUrl);
```