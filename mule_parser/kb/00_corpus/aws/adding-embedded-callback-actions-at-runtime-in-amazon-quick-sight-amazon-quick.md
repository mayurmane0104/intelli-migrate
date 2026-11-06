# Adding embedded callback actions at runtime in Amazon Quick Sight - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/embedding-custom-actions-callback.html](https://docs.aws.amazon.com/quick/latest/userguide/embedding-custom-actions-callback.html)

---

Use embedded datapoint callback actions to build tighter integrations between your software as a service (SaaS) application and your Amazon Quick Sight embedded dashboards and visuals. Developers can register datapoints to be called back with the Amazon Quick Sight embedding SDK. When you register a callback action for a visual, readers can select a datapoint on the visual to receive a callback that provides data specific to the selected data point. This information can be used to flag key records, compile raw data specific to the datapoint, capture records, and compile data for backend processes.

Embedded callbacks aren't supported for custom visual content, text boxes, or insights.

Before you begin registering datapoints for callback, update the Embedding SDK to
                version 2.3.0. For more information about using the Amazon Quick Sight Embedding SDK,
                see the [amazon-quicksight-embedding-sdk](https://github.com/awslabs/amazon-quicksight-embedding-sdk) on GitHub.

A datapoint callback can be registered to one or more visuals at runtime through
                the Amazon Quick Sight SDK. You can also register a datapoint callback to any
                interaction supported by the [VisualCustomAction](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_VisualCustomAction.html) API structure. This allows the datapoint callback to
                initiate when the user selects the datapoint on the visual or when the datapoint is
                selected from the datapoint context menu. The following example registers a
                datapoint callback that the reader initiates when they select a datapoint on the
                visual.

`/const MY_GET_EMBED_URL_ENDPOINT = "https://my.api.endpoint.domain/MyGetEmbedUrlApi"; // Sample URL // The dashboard id to embed const MY_DASHBOARD_ID = "my-dashboard"; // Sample ID // The container element in your page that will have the embedded dashboard const MY_DASHBOARD_CONTAINER = "#experience-container"; // Sample ID // SOME HELPERS const ActionTrigger = { DATA_POINT_CLICK: "DATA_POINT_CLICK", DATA_POINT_MENU: "DATA_POINT_MENU", }; const ActionStatus = { ENABLED: "ENABLED", DISABLED: "DISABLED", }; // This function makes a request to your endpoint to obtain an embed url for a given dashboard id // The example implementation below assumes the endpoint takes dashboardId as request data // and returns an object with EmbedUrl property const myGetEmbedUrl = async (dashboardId) => { const apiOptions = { dashboardId, }; const apiUrl = new URL(MY_GET_EMBED_URL_ENDPOINT); apiUrl.search = new URLSearchParams(apiOptions).toString(); const apiResponse = await fetch(apiUrl.toString()); const apiResponseData = await apiResponse.json(); return apiResponseData.EmbedUrl; }; // This function constructs a custom action object const myConstructCustomActionModel = ( customActionId, actionName, actionTrigger, actionStatus ) => { return { Name: actionName, CustomActionId: customActionId, Status: actionStatus, Trigger: actionTrigger, ActionOperations: [ { CallbackOperation: { EmbeddingMessage: {}, }, }, ], }; }; // This function adds a custom action on the first visual of first sheet of the embedded dashboard const myAddVisualActionOnFirstVisualOfFirstSheet = async ( embeddedDashboard ) => { // 1. List the sheets on the dashboard const { SheetId } = (await embeddedDashboard.getSheets())[0]; // If you'd like to add action on the current sheet instead, you can use getSelectedSheetId method // const SheetId = await embeddedDashboard.getSelectedSheetId(); // 2. List the visuals on the specified sheet const { VisualId } = (await embeddedDashboard.getSheetVisuals(SheetId))[0]; // 3. Add the custom action to the visual try { const customActionId = "custom_action_id"; // Sample ID const actionName = "Flag record"; // Sample name const actionTrigger = ActionTrigger.DATA_POINT_CLICK; // or ActionTrigger.DATA_POINT_MENU const actionStatus = ActionStatus.ENABLED; const myCustomAction = myConstructCustomActionModel( customActionId, actionName, actionTrigger, actionStatus ); const response = await embeddedDashboard.addVisualActions( SheetId, VisualId, [myCustomAction] ); if (!response.success) { console.log("Adding visual action failed", response.errorCode); } } catch (error) { console.log("Adding visual action failed", error); } }; const parseDatapoint = (visualId, datapoint) => { datapoint.Columns.forEach((Column, index) => { // FIELD | METRIC const columnType = Object.keys(Column)[0]; // STRING | DATE | INTEGER | DECIMAL const valueType = Object.keys(Column[columnType])[0]; const { Column: columnMetadata } = Column[columnType][valueType]; const value = datapoint.RawValues[index][valueType]; const formattedValue = datapoint.FormattedValues[index]; console.log( `Column: ${columnMetadata.ColumnName} has a raw value of ${value} and formatted value of ${formattedValue.Value} for visual: ${visualId}` ); }); }; // This function is used to start a custom workflow after the end user selects a datapoint const myCustomDatapointCallbackWorkflow = (callbackData) => { const { VisualId, Datapoints } = callbackData; parseDatapoint(VisualId, Datapoints); }; // EMBEDDING THE DASHBOARD const main = async () => { // 1. Get embed url let url; try { url = await myGetEmbedUrl(MY_DASHBOARD_ID); } catch (error) { console.log("Obtaining an embed url failed"); } if (!url) { return; } // 2. Create embedding context const embeddingContext = await createEmbeddingContext(); // 3. Embed the dashboard const embeddedDashboard = await embeddingContext.embedDashboard( { url, container: MY_DASHBOARD_CONTAINER, width: "1200px", height: "300px", resizeHeightOnSizeChangedEvent: true, }, { onMessage: async (messageEvent) => { const { eventName, message } = messageEvent; switch (eventName) { case "CONTENT_LOADED": { await myAddVisualActionOnFirstVisualOfFirstSheet(embeddedDashboard); break; } case "CALLBACK_OPERATION_INVOKED": { myCustomDatapointCallbackWorkflow(message); break; } } }, } ); }; main().catch(console.error);`

You can also configure the preceding example to initiate datapoint callback when
                the user opens the context menu. To do this with the preceding example, set the
                value of `actionTrigger` to
                `ActionTrigger.DATA_POINT_MENU`.

After a datapoint callback is registered, it's applied to most datapoints on the
                specified visual or visuals. Callbacks don't apply to totals or subtotals on
                visuals. When a reader interacts with a datapoint, a
                    `CALLBACK_OPERATION_INVOKED` message is emitted to the
                Amazon Quick Sight embedding SDK. This message is captured by the
                    `onMessage` handler. The message contains the raw and display values
                for the full row of data associated with the datapoint that is selected. It also
                contains the column metadata for all columns in the visual that the datapoint is
                contained in. The following is an example of a
                    `CALLBACK_OPERATION_INVOKED` message.

```
{
   CustomActionId: "custom_action_id",
   DashboardId: "dashboard_id",
   SheetId: "sheet_id",
   VisualId: "visual_id",
   DataPoints: [
        {
            RawValues: [
                    {
                        String: "Texas" // 1st raw value in row
                    },
                    {
                        Integer: 1000 // 2nd raw value in row
                    }
            ],
            FormattedValues: [
                    {Value: "Texas"}, // 1st formatted value in row
                    {Value: "1,000"} // 2nd formatted value in row
            ],
            Columns: [
                    { // 1st column metadata
                        Dimension: {
                            String: {
                                Column: {
                                    ColumnName: "State",
                                    DatsetIdentifier: "..."
                                }
                            }
                        }
                    },
                    { // 2nd column metadata
                        Measure: {
                            Integer: {
                                Column: {
                                    ColumnName: "Cancelled",
                                    DatsetIdentifier: "..."
                                },
                                AggregationFunction: {
                                    SimpleNumericalAggregation: "SUM"
                                }
                            }
                        }
                    }
            ]
        }
   ]
}
```