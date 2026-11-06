# Creating a shared view with the Amazon Quick Sight createSharedView API - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/embedded-view-sharing-sdk-create.html](https://docs.aws.amazon.com/quick/latest/userguide/embedded-view-sharing-sdk-create.html)

---

After you update the Embedding SDK to version 2.8.0 or higher, use the
                        `createSharedView` API to create a new shared view. Record the
                        `sharedViewId` and the `dashboardId` that the
                    operation returns. The example below creates a new shared view.

```
const response = await embeddingFrame.createSharedView();
const sharedViewId = response.message.sharedViewId;
const dashboardId = response.message.dashboardId;
```
`createSharedView` can only be called when a user views a
                    dashboard. For console-specific shared view creation, make sure that users are
                    on the dashboard page before you enable the `createSharedView`
                    action. You can do this with the `PAGE_NAVIGATION` event, shown in
                    the example below.

```
const contentOptions = {
    onMessage: async (messageEvent, metadata) => {
    switch (messageEvent.eventName) {
            case 'CONTENT_LOADED': {
                console.log("Do something when the embedded experience is fully loaded.");
                break;
            }
            case 'ERROR_OCCURRED': {
                console.log("Do something when the embedded experience fails loading.");
                break;
            }
            case 'PAGE_NAVIGATION': {
                setPageType(messageEvent.message.pageType); 
                if (messageEvent.message.pageType === 'DASHBOARD') {
                    setShareEnabled(true);
                    } else {
                    setShareEnabled(false);
                }
                break;
            }
        }
    }
};
```