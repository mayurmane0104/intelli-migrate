# Customize the look and feel of Amazon Quick Sight embedded dashboards and visuals - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/embedding-runtime-theming.html](https://docs.aws.amazon.com/quick/latest/userguide/embedding-runtime-theming.html)

---

You can use the Amazon Quick Sight Embedding SDK (version 2.5.0 and higher) to make changes to the theming of your embedded Amazon Quick Sight dashboards and visuals at runtime. Runtime theming makes it easier to integrate your Software as a service (SaaS) application with your Amazon Quick Sight embedded assets. Runtime theming allows you to synchronize the theme of your embedded content with the themes of the parent application that your Amazon Quick Sight assets are embedded into. You can also use runtime theming to add customization options for readers. Theming changes can be applied to embedded assets at initialization or throughout the lifetime of your embedded dashboard or visual.

For more information about themes, see [Using themes in Amazon Quick Sight](./themes-in-quicksight.html). For more information about using the
                Amazon Quick Sight Embedding SDK, see the [amazon-quicksight-embedding-sdk](https://github.com/awslabs/amazon-quicksight-embedding-sdk) on GitHub.

**Prerequisites**

Before you can get started, make sure that you have the following prerequisites.

- 
                    You are using the Amazon Quick Sight Embedding SDK version 2.5.0 or higher. 
- 
                    Permissions to access the theme that you want to work with. To grant permissions to a theme in Amazon Quick Sight, make a `UpdateThemePermissions`API call or use the**Share**icon next to the theme in the Amazon Quick Sight console's analysis editor.

## Terminology and concepts

                The following terminology can be useful when working with embedded runtime theming.

- 
                        *Theme*– A collection of settings that you can apply to multiple analyses and dashboards that change how the content is displayed.
- 
                        *ThemeConfiguration*– A configuration object that contains all of the display properties for a theme.
- 
                        *Theme Override*– A`ThemeConfiguration`object that is applied to the active theme to override some or all aspects of how content is displayed.
- 
                        *Theme ARN*– An Amazon Resource Name (ARN) that identifies a Amazon Quick Sight theme. Following is an example of custom theme ARN.`arn:aws:quicksight:region:account-id:theme/theme-id`Amazon Quick Sight provided starter themes don't have a region in their theme ARN. Following is an example of a starter theme ARN. `arn:aws:quicksight::aws:theme/CLASSIC`

## Setting up

                Make sure that you have the following information ready to get started working with runtime theming.

- 
                        The theme ARNs of the themes that you want to use. You can choose an existing theme, or you can create a new one. To obtain a list all themes and theme ARNs in your Amazon Quick Sight account, make a call to the [ListThemes](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListThemes.html)API operation. For information on preset Amazon Quick Sight themes, see[Setting a default theme for Amazon Quick analyses with the Amazon Quick APIs](./customizing-quicksight-default-theme.html).
- 
                        If you are using registered user embedding, make sure that the user has access to the themes that you want to use. If you are using anonymous user embedding, pass a list of theme ARNs to the `AuthorizedResourceArns`parameter of the`GenerateEmbedUrlForAnonymousUser`API. Anonymous users are granted access to any theme that is listed in the`AuthorizedResourceArns`parameter.

## SDK method interface

                **Setter methods**

The following table describes different setter methods that developers can use for runtime theming.

| Method | Description | 
|---|---|
| 
 | Replaces the active theme of a dashboard or visual with another theme. If applied, the theme override is removed. An error is returned if you don't have access to the theme or if the theme doesn't exist. | 
| 
 | Sets a dynamic  An error is returned if the
                                             | 

## Initializing embedded content with a theme

                To initialize an embedded dashboard or visual with a non-default theme, define
                    a `themeOptions` object on the `DashboardContentOptions`
                    or `VisualContentOptions` parameters, and set the
                        `themeArn` property within `themeOptions` to the
                    desired theme ARN.

The following example initializes an embedded dashboard with the
                        `MIDNIGHT` theme.

`import { createEmbeddingContext } from 'amazon-quicksight-embedding-sdk'; const embeddingContext = await createEmbeddingContext(); const { embedDashboard, } = embeddingContext; const frameOptions = { url: '<YOUR_EMBED_URL>', container: '#experience-container', }; const contentOptions = { themeOptions: { themeArn: "arn:aws:quicksight::aws:theme/MIDNIGHT" } }; // Embedding a dashboard experience const embeddedDashboardExperience = await embedDashboard(frameOptions, contentOptions);`

## Initializing embedded content with a theme override

                Developers can use theme overrides to define the theme of an embedded
                    dashboard or visual at runtime. This allows the dashboard or visual to inherit a
                    theme from a third-party application without the need to pre-configure a theme
                    within Amazon Quick Sight. To initialize an embedded dashboard or visual with a
                    theme override, set the `themeOverride` property within
                        `themeOptions` in either the `DashboardContentOptions`
                    or `VisualContentOptions` parameters. The following example overrides
                    the font of a dashboard's theme from the default font to ```
Amazon
                        Ember
```
.

`import { createEmbeddingContext } from 'amazon-quicksight-embedding-sdk'; const embeddingContext = await createEmbeddingContext(); const { embedDashboard, } = embeddingContext; const frameOptions = { url: '<YOUR_EMBED_URL>', container: '#experience-container', }; const contentOptions = { themeOptions: { "themeOverride":{"Typography":{"FontFamilies":[{"FontFamily":"Comic Neue"}]}} } }; // Embedding a dashboard experience const embeddedDashboardExperience = await embedDashboard(frameOptions, contentOptions);`

## Initializing embedded content with preloaded themes

                Developers can configure a set of dashboard themes to be preloaded on
                    initialization. This is most beneficial for quick toggling between different
                    views, for example dark and light modes. An embedded dashboard or visual can be
                    initialized with up to 5 preloaded themes. To use preloaded themes, set the
                        `preloadThemes` property in either
                        `DashboardContentOptions` or `VisualContentOptions`
                    with an array of up to 5 `themeArns`. The following example preloads
                    the `Midnight` and `Rainier` starter themes to a
                    dashboard.

`import { createEmbeddingContext } from 'amazon-quicksight-embedding-sdk'; const embeddingContext = await createEmbeddingContext(); const { embedDashboard, } = embeddingContext; const frameOptions = { url: '<YOUR_EMBED_URL>', container: '#experience-container', }; const contentOptions = { themeOptions: { "preloadThemes": ["arn:aws:quicksight::aws:theme/RAINIER", "arn:aws:quicksight::aws:theme/MIDNIGHT"] } }; // Embedding a dashboard experience const embeddedDashboardExperience = await embedDashboard(frameOptions, contentOptions);`