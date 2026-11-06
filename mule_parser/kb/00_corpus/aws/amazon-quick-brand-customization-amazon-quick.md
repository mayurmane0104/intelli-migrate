# Amazon Quick brand customization - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/brand-customization.html](https://docs.aws.amazon.com/quick/latest/userguide/brand-customization.html)

---

Amazon Quick allows account admins to customize their application's branding and visual theme to align with their organization's guidelines. This customization includes the following visual elements to create a cohesive look and feel across all non-administrative Amazon Quick console pages, schedules, alerts, and email reports.

- 
            Logo 
- 
            Favicon 
- 
            Associated alt text for visual assets 

The following list shows the different areas customizable theme colors are grouped into.

###### Brand colors

- 
            **Global navigation bar**colors are applied to the topmost bar in the Amazon Quick UI and include the company logo that is diaplayed in the standard and embedded Amazon Quick consoles.
- 
            **Application bar**colors are applied to the secondary navigation bar that contains contextual actions.

###### Interaction colors

- 
            **Accent**colors are applied to interactive elements like buttons, borders, and icons.

###### Surface colors

- 
            **Primary**colors are applied to high-emphasis surfaces like the homepage background and text.
- 
            **Secondary**colors are applied to practical surfaces like borders, backgrounds, and form fields. Secondary colors are used alongside primary colors.

###### Status colors

- 
            **Success**colors are applied to success messages.
- 
            **Danger**colors are applied to error messages.
- 
            **Warning**colors are applied to warning messages.
- 
            **Info**colors are applied to informational messages.

###### Data visualization colors

- 
            **Dimension**colors are used to identify associations between data columns that share the same role.
- 
            **Measure**colors are used to idenfity metrics or measured values.

###### Features

- 
            **Visualization**colors are applied to the**Visualization**icon.
- 
            **Insight**colors are applied to the**Insight**icon.
- 
            **Connection**colors are applied to the**Connection**icon.
- 
            **Automation**colors are applied to the**Automation**icon.

Use the following sections to get started with brand customization in Amazon Quick.

###### Topics

## Permisisons for Amazon Quick brand customization

        To set up a brand, you must be granted an Admin role through IAM Identity Center or IAM. Admins
            whose roles are granted to them within Amazon Quick can't create brands. To learn
            more about integrating your account with IAM Identity Center, see [Configure your Amazon Quick account with IAM Identity Center](https://docs.aws.amazon.com/quicksight/latest/user/sec-identity-management-identity-center.html). For
            information about admin roles and capabilities, see [Understanding Amazon Quick subscriptions and
            roles](https://docs.aws.amazon.com/quicksight/latest/user/user-types.html#subscription-role-mapping).

Admin users can only manage brands that are in the same capacity Region as their Amazon Quick account.

The IAM role that you use to create a brand in Amazon Quick must contain
                `quicksight:*` or granular action permissions to manage brands in the
            admin console. The following granular permissions are required for admins to work with
            Amazon Quick brands:

- 
                `quicksight:CreateBrand`
- 
                `quicksight:UpdateBrand`
- 
                `quicksight:DescribeBrand`
- 
                `quicksight:DescribeBrandPublishedVersion`
- 
                `quicksight:UpdateBrandPublishedVersion`
- 
                `quicksight:DeleteBrand`
- 
                `quicksight:ListBrands`
- 
                `quicksight:UpdateBrandAssignment`
- 
                `quicksight:DescribeBrandAssignment`
- 
                `quicksight:DeleteBrandAssignment`

After you confirm that your Admin role contains the required permissions, you can
                [Create a custom brand](https://docs.aws.amazon.com/quicksight/latest/user/brand-customization-create.html) in the Amazon Quick admin
            console.

## Create a custom brand in Amazon Quick

        Use the following procedure to create a custom brand in Amazon Quick.

- 
	Open the [Quick console](https://quicksight.aws.amazon.com/).
- 
                Choose the user icon at the top right, and then choose **Manage Quick**.
- 
                Choose **Customize application**.
- 
                On the **Customize application**page that opens, choose**ADD BRAND**. The**Brand settings**page opens.
- 
                Navigate to the **Brand Info**section.
- 
                For **Brand name**, enter a name for the brand. The brand name can contain up to 512 characters.
- 
                (Optional) For **Brand description**, enter a description for the custom brand. The brand description can contain up to 512 characters.
- 
                Navigate to the **Logo**section.![The Logo section of the Brand Info page.](/images/quick/latest/userguide/images/logo.png)  
- 
                For **Primary**, choose the ellipsis (three dots) next to the primary icon, and then choose**Replace image**.
- 
                In the **Choose image**pop up that opens, perform one of the following actions:- 
                        Drag and drop image into the **Drag an image here**box.
- 
                        Choose **Select a file**to select a file from your computer.
- 
                        Enter a public URL or Amazon S3 URI in the text bar. 
 The image that you choose must be a `.jpeg`,`.png`, or`.svg`format and can't exceed 1MB.When you are finished choosing an image, choose **Apply**.
- 
                        
- 
                For **Favicon**, choose the ellipsis (three dots) next to the favicon, and then choose**Replace image**.
- 
                In the **Choose image**pop up that opens, perform one of the following actions:- 
                        Drag and drop image into the **Drag an image here**box.
- 
                        Choose **Select a file**to select a file from your computer.
- 
                        Enter a public URL or Amazon S3 URI in the text bar. 
 The image that you choose must be a `.jpeg`,`.png`, or`.svg`format and can't exceed 1MB.When you are finished choosing an image, choose **Apply**.
- 
                        
- 
                (Optional) For **Alt text**, enter alt text to display with the logo. The alt text can contain up to 512 characters.
- 
                To make changes to the theme colors of the brand, navigate to the **Appearance**pane on the left and choose**Theme**.
- 
                The **Theme settings**page appears and displays all parts of a Amazon Quick theme that can be customized. The following image shows the configuration settings of the global navigation bar.![The configuration settings for the global navigation bar. Use the Background and Foreground swatches to customize the colors of every theme item listed on the Theme settings page.](/images/quick/latest/userguide/images/navigation-bar.png)  
- 
                To change the background color of an area, navigate to the item that you want to change and choose the **Background**color swatch.
- 
                In the **Custom color**pop up that appears, choose a color from the color gradient or enter a hex code value in the**HEX**bar, and then choose**APPLY**.
- 
                To change the foreground color of an area, navigate to the item that you want to change and choose the **Foreground**color swatch.
- 
                In the **Custom color**pop up that appears, choose a color from the color gradient or enter a hex code value in the**HEX**bar, and then choose**APPLY**.
- 
                When you are finished configuring a custom brand, choose **PUBLISH**to publish and apply the brand customization to all Amazon Quick user accounts. If you don't want to publish the brand, choose**SAVE**to save the brand for later.

When you finish creating a brand in Amazon Quick, the new brand appears in the brands
            table on the **Customize application** page of the Quick admin
            console. The **Status** column of the brands table indicates which
            brand is currently published to the Quick account. To make changes to a custom
            brand, locate the brand that you want to change in the brands table, choose the ellipsis
            (three dots) icon in the **Actions** column, and then choose
                **Publish**, **Edit**, or
                **Delete**.
            

Once you publish a brand, it can take up to 10 minutes for the new brand to propagate across all users.