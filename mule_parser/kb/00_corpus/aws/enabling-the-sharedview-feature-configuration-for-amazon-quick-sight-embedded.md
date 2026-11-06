# Enabling the SharedView feature configuration for Amazon Quick Sight embedded analytics - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/embedded-view-sharing-set-up.html](https://docs.aws.amazon.com/quick/latest/userguide/embedded-view-sharing-set-up.html)

---

When you create an the embedded instance with the Amazon Quick Sight API, set
                    the value of `SharedView` in the `FeatureConfigurations`
                    payload to `true`, as shown in the example below.
                        `SharedView` overrides the `StatePersistence`
                    configurations for registered users who access embedded dashboards. If a
                    dashboard user has `StatePersistence` disabled and
                        `SharedView` enabled, their state will persist.

```
const generateNewEmbedUrl = async () => {
    const generateUrlPayload = {
        experienceConfiguration: {
            QuickSightConsole: {
            FeatureConfigurations: {
                "SharedView": { 
                    "Enabled": true
                 },
            },
        },
    }
    const result: GenerateEmbedUrlResult = await generateEmbedUrlForRegisteredUser(generateUrlPayload);
    return result.url;
};
```