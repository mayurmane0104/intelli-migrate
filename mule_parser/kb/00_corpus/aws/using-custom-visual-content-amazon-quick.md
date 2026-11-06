# Using custom visual content - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/custom-visual-content.html](https://docs.aws.amazon.com/quick/latest/userguide/custom-visual-content.html)

---

You can embed webpages and online videos, forms, and images in your Quick dashboards using the custom visual content chart type.

For example, you can embed the image of your company logo in your dashboards. You can also embed an online video from your organization's latest conference, or embed an online form asking readers of the dashboard if the dashboard is helpful.

After you create custom visual content, you can use navigation actions to navigate within them. You can also use parameters to control what appears in them.

The following limitations apply to custom visual content:

- 
				Only `https`URL schemes are supported.
- 
				Custom visual content isn't supported in email reports. 
- 
				Images and websites that use hotlink protection won't load in custom visuals. 

To embed a webpage, video, online form, or image in your dashboard, choose the custom
			visual content icon in the **Visual types** pane.

For more information about adding visuals to a dashboard, see [Adding a visual](./creating-a-visual.html#create-a-visual).

Use the following procedures to learn how to embed custom visuals in your dashboards.

## Best practices for using custom visual content

			When embedding web content using the custom visual content chart type, we recommend the following:

- 
					Choose web content from sources that support viewing or opening the content in an IFrame. If the source of the web content doesn't support being viewed or opened in an IFrame, the content doesn't appear in Quick, even if the URL is accurate. 
- 
					When possible, use embeddable URLs, especially for videos, online forms, spreadsheets, and documents. Embeddable URLs create a better experience for readers of your dashboard and make interacting with the content easier. You can usually find the embeddable URL for content when you choose to share the content from the source website. 
- 
					To embed internal URLs or URLs that you own, you might need to set them to be opened in an IFrame. 
- 
					When viewing custom visual content in an analysis or dashboard, make sure you enable all cookies. If third-party cookies are blocked in your browser, images that are part of the website that is embedded within the custom content visual do not render. ###### NoteChrome has announced plans to deprecate all third-party cookies by the end of 2024. This means that websites that are embedded within Quick custom content visuals will no longer show any contents that rely on third-party cookies in Chrome. For more information about Chrome's plans to deprecate third party cookies, see [Chrome is deprecating third-party cookies](https://cloud.google.com/looker/docs/best-practices/chrome-third-party-cookie-deprecation).

## Embedding images in a dashboard

			You can embed an online image in a dashboard using the image URL. Use the following procedure to embed an image using the custom visual content chart type.

Embedded images don't appear in a browser that has third-party cookies blocked. To see embedded images in a dashboard, enable third-party cookies in your browser settings.

###### To embed an image in a dashboard

- 
					In the **Visual types**pane, choose the custom visual content icon.
- 
					In the visual, choose **Customize visual**.
- 
					In the **Properties**pane that opens, under**Custom content**, enter the image URL for the image that you want to embed.
- 
					Choose **Apply**.The image appears as a webpage in the visual. 
- 
					Choose **Show as image**.If the URL is an image, the image appears in the visual. If the URL is not an image, such as a URL to a slide show, gallery, or webpage, the following message appears: `This URL doesn't appear to be an image. Update the URL to an image`. To do so, open the image that you want to embed in a separate browser tab, or choose an embeddable URL for the image (usually found when you choose to share the image).
- 
					(Optional) For **Image sizing options**, choose one of the following options:- 
							**Fit to width**– This option fits the image to the width of the visual.
- 
							**Fit to height**– This option fits the image to the height of the visual.
- 
							**Scale to visual**– This option scales the image to the width and height of the visual. This option might contort the image.
- 
							**Do not scale**– This option keeps the image at its original scale and doesn't fit the image to the dimensions of the visual. With this option, the image is centered in the visual and the parts of the image that are within the width and height of the visual appear. Some parts of the image might not appear if the visual is smaller than the image. If the visual is larger than the image, however, the image is centered in the visual and is surrounded by white space.
 
- 
							

## Embedding online forms in a dashboard

			You can embed an online form in a dashboard using the embeddable URL. Use the following procedure to embed an online form using the custom visual content chart type.

###### To embed an online form in a dashboard

- 
					In the **Visual types**pane, choose the custom visual content icon.
- 
					In the visual, choose **Customize visual**.
- 
					In the **Properties**pane that opens, under**Custom content**, enter the form URL for the online form that you want to embed.If possible, use an embeddable URL for the form. Using an embeddable URL creates a better experience for readers of your dashboard who might want to interact with the form. You can often find the embeddable URL when you choose to share the form on the site where you create it. 
- 
					Choose **Apply**.The form appears in the visual. 

## Embedding webpages in a dashboard

			You can embed webpage in a dashboard using the URL. Use the following procedure to embed webpage using the custom visual content chart type.

###### To embed a webpage in a dashboard

- 
					In the **Visual types**pane, choose the custom visual content icon.
- 
					In the visual, choose **Customize visual**.
- 
					In the **Properties**pane that opens, under**Custom content**, enter the URL for the webpage that you want to embed.
- 
					Choose **Apply**.The webpage appears in the visual. 

## Embedding online videos in a dashboard

			You can embed an online video in a dashboard using the embeddable video URL. Use the following procedure to embed an online video using the custom visual content chart type.

###### To embed an online video in a dashboard

- 
					In the **Visual types**pane, choose the custom visual content icon.
- 
					In the visual, choose **Customize visual**.
- 
					In the **Properties**pane that opens, under**Custom content**, enter the embeddable URL for the video that you want to embed.To find the embeddable URL for a video, share the video and copy the embed URL from IFrame code. The following is an example of an embed URL for a YouTube video: `https://www.youtube.com/embed/`. For a Vimeo video, the following is an example of an embed URL:`uniqueid``https://player.vimeo.com/video/`.`uniqueid`
- 
					Choose **Apply**.The video appears in the visual.