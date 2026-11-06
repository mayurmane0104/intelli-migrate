# Using themes in Amazon Quick Sight - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/themes-in-quicksight.html](https://docs.aws.amazon.com/quick/latest/userguide/themes-in-quicksight.html)

---

In Amazon Quick Sight, a *theme* is a collection of settings
			that you can apply to multiple analyses and dashboards. Amazon Quick Sight includes some themes,
			and you can add your own by using the theme editor. You can share themes with
			permissions levels set to user or owner. Anyone who has access to the theme can apply it
			to analyses and dashboards, or use **Save as** to make their own copy
			of it. Theme owners can also edit the theme and share it with others.

An analysis can have only one theme applied. If you apply a theme to an analysis (by
			using the **Apply** button), it instantly changes it for
			everyone—both analysis and dashboard viewers. To explore and save color options
			without applying them, avoid editing and saving the applied theme. 

All colors come in pairs of background and foreground colors. The foreground colors are meant to specifically appear above their matching background color, so choose something that contrasts well.

The following table defines the different settings.

| Group | Setting | What the setting changes | 
|---|---|---|
| Main | Primary background | The background color used for visuals and other high emphasis
								UI. 
 | 
| Main | Primary foreground | The color of text and other foreground elements that appear over the
							primary background regions such as grid lines, borders, table banding,
							icons, and so on. 
 | 
| Main | Secondary background | The background color used for the sheet background and sheet controls. | 
| Main | Secondary foreground | The foreground color used for any sheet title, sheet control text, or UI that appears over the secondary background. | 
| Main | Accent | This setting is used as an interactive hint for the following: 
 | 
| Main | Accent foreground | The foreground color applies to any text or other elements that appear over the accent color. | 
| Main | Font | The font to use for all of the text. You can choose from a variety of fonts supported by Amazon Quick Sight. | 
| Data | Data colors | These are the data colors that charts rotate through when assigning colors to groups. You can add or remove colors to this list, or choose a color to change it. | 
| Data | Min max gradient | The default minimum and maximum gradient colors to use when a gradient is used as a scale, for example in heat maps. | 
| Data | Empty fill color | This is the color used with your data colors to indicate a lack of data. For example, this color appears in the empty portion of the progress bars that are shown in key performance indication (KPI) and gauge charts, or for empty heat map cells. | 
| Layout | Border | This setting toggles the border around the visuals that aren't currently selected. The selected visual's border still displays the accent color. | 
| Layout | Margin | This setting toggles the space between the sheet boundaries and the visuals. | 
| Layout | Gutter | This setting shows or hides the space between visuals in the grid. | 
| Other | Success Success foreground | These colors are used for success messages, for example the check mark for a successful download. | 
| Other | Warning Warning foreground | These colors are used for warning and informational messages. | 
| Other | Danger Danger foreground | These colors are used for error messages. | 
| Other | Dimension Dimension foreground | These colors are used for the names of fields that are identified as dimensions. This option also sets the color for dimensions in the filter panel of embedded dashboards. | 
| Other | Measure Measure foreground | These colors are used for the names of fields that are identified as measures. These colors also apply to measures in the filter panel of embedded dashboards. | 

###### To take a short tour of the theme viewer and editor

- 
	Open the [Quick console](https://quicksight.aws.amazon.com/).
- 
				Open an analysis, or create a new one. You must have an analysis open to work with themes. However, the view you see with the theme applied is only a preview. Themes are separate from analyses. No changes are made to your analysis, even when you save a theme. 
- 
				Choose **Edit**from the application bar, and then choose**Themes**. The themes panel opens.
- 
				The list of themes shows the following: - 
						**Applied theme**shows the theme that is currently applied to this analysis and its dashboards.
- 
						**My themes**shows themes that you created and themes that are shared with you.
- 
						**Starter themes**shows themes created by Amazon Quick Sight.
 
- 
						
- 
				Each theme has context menu that you can access from the **…**icon.The actions that are available to you on each theme depend on your level of access. - 
						**Theme owners**– If you created the theme, or someone shared it with you and made you an owner, you can do the following:- 
								**Edit**– Change the settings for the theme, and save them.
- 
								**Save**– Save changes you made to the theme. If you edit the applied theme save your changes, the new theme settings apply to all the analyses and dashboards that use it. An informational message displays before you overwrite an applied theme.
- 
								**Share**– Share the theme and assign user or owner permissions to other people.
- 
								**Delete**– Delete a theme. You can't undo this action. An informational message displays before you confirm deletion.
 
- 
								
- 
						**Theme users**– If someone shared the theme with you, or if it's an Amazon Quick Sight theme, you can do the following:- 
								**Apply**– Apply the theme to the current analysis. This option also applies the theme to dashboards created from the analysis. An informational message displays before you overwrite an applied theme.
- 
								**Save as**– Save the current theme to another name, so you can edit it.
 
- 
								
- 
						**Analysis authors**– If you have access to the analysis, but not the theme, you can do the following:- 
								You can see the analysis with the theme applied. 
- 
								You can see the theme in the **Theme**panel.
- 
								You can use **Save as**to create your own copy of the theme.
 
- 
								
- 
						**Dashboard viewers**– If you have access to the dashboard, but not the theme, you can do the following:- 
								You can see the dashboard with the theme applied. 
- 
								You can't see the theme or its settings. Dashboard users can't see the **Theme**panel.
 
- 
								
 
- 
						
- 
				To explore a theme's settings, choose the icons on the left to see settings for colors. 

The following procedure walks you through creating a theme. You can start on the analysis, or a copy of the analysis, that you want to use to preview the colors. Or you can start a new analysis. After you save the theme, you can apply it to the current analysis or to other analyses. If you share it, other people can use it too.

###### To use the theme editor

- 
	Open the [Quick console](https://quicksight.aws.amazon.com/).
- 
				Open an analysis, or create a new one. Choose **Edit**from the application bar, and then choose**Themes**. The**Themes**panel opens.You must have an analysis open to work with themes. However, the view you see with the theme applied is only a preview. Themes are separate from analyses. No changes are made to your analysis, even when you save a theme. 
- 
				Choose **Main**. The color picker used in each of these settings is the standard one used throughout Amazon Quick Sight.Set colors for **Primary background**and**Primary foreground**to use in visuals and other high impact UI.Set colors for **Secondary background**and**Secondary foreground**to use in sheets and sheet controls.Set colors for **Accent**and**Accent foreground**to use in interactive hints including buttons, borders around selected visuals, loading indicators, narration customizations, links, and the filter pane in embedded dashboards.
- 
				Choose **Data**.Set the **Colors**to use as data colors. Charts rotate through these when assigning colors. You can add or delete colors, or change the order they're in by dragging and dropping. To change an existing color, select it to open the color editor.Set colors for **Min max gradient**to use when a gradient is used as a scale, for example in heat maps.Set the color for **Empty fill**to use when showing a lack of data, for example the unfilled part of a progress bar.
- 
				Choose **Layout**.Enable or disable the **Border**check box to show or hide the border around the visuals that aren't currently selected.Enable or disable the **Margin**check box to show or hide the space between the sheet boundaries and the visuals.Enable or disable the **Gutter**check box to show or hide the space between visuals in the grid.
- 
				Choose **Other**.Set the color for **Success**to use in success messages, for example when you successfully download a .csv file. The success foreground color isn't currently used.Set the color for **Warning**to use in warning and informational messages. The warning foreground color isn't currently used.Set the color for **Danger**to use in error messages. The danger foreground color isn't currently used.Set the color for **Dimension**to use for the names of fields that are identified as dimensions. This option also sets the color for dimensions in the filter panel of embedded dashboards.Set the color for **Measure**to use for the names of fields that are identified as measures. This option also sets the color for measures in the filter panel of embedded dashboards.
- 
				To save the theme, choose **Main**and give the new theme a name, and then choose**Save**at the upper-right of the browser.Saving a theme doesn't apply it to the analysis, even though you can see a preview of the colors that uses the current analysis. 
- 
				To share the theme, save or close the theme you are viewing. Find the theme in your theme collection. Choose **Share**from the context menu (…).
- 
				To apply the theme, save or close the theme you are viewing. Find the theme in your theme collection. Choose **Apply**from the context menu (…).