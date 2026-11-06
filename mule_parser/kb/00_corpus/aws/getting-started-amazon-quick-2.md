# Getting started - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/getting-started-desktop.html](https://docs.aws.amazon.com/quick/latest/userguide/getting-started-desktop.html)

---

This section walks you through downloading, installing, and signing in to the Amazon Quick desktop application for macOS and Windows.

## Prerequisites

        Before you install the Amazon Quick desktop application, verify that your system meets the following requirements.

### macOS

| Requirement | Minimum | 
|---|---|
| Operating system | macOS 12 (Monterey) or later | 
| Processor | Apple Silicon (M1 or later) | 
| Memory | 8 GB RAM | 
| Disk space | 500 MB available (installation only). 10 GB or more recommended for search indexing and knowledge graph features. | 
| Internet | Required for sign-in, AI model access, and connected services | 

### Windows

| Requirement | Minimum | 
|---|---|
| Operating system | Windows 10 (64-bit) or later | 
| Processor | x86_64 compatible | 
| Memory | 8 GB RAM | 
| Disk space | 500 MB available (installation only). 10 GB or more recommended for search indexing and knowledge graph features. | 
| Internet | Required for sign-in, AI model access, and connected services | 

## Downloading and installing

        ###### Important

If your organization uses a Professional or Enterprise account, complete
                the steps in [Setting up Amazon Quick on desktop for enterprise deployments](./desktop-enterprise-setup.html) before downloading or distributing the
                application. Enterprise sign-in is not available until an administrator configures
                the extension access.

You can download the Amazon Quick desktop application from the following locations:

- 
                **Amazon Quick web application**– Sign in to Amazon Quick on the web. In the left navigation, choose**Extensions**. On the**QuickDesktop-extension**card, choose the menu, and then choose**Download for Windows**or**Download for Mac**.
- 
                **Direct download**– Use the following links:Platform Download macOS (Apple Silicon) [Amazon-Quick.dmg](https://desktop.downloads.quick.aws.com/mac/arm64/Amazon-Quick.dmg)Windows (x64) [Amazon-Quick.exe](https://desktop.downloads.quick.aws.com/windows/x64/Amazon-Quick.exe)

###### To install on macOS

- 
                Download the `.dmg`installer file.
- 
                Open the `.dmg`file.
- 
                Drag **Amazon Quick**to the**Applications**folder.
- 
                Open **Amazon Quick**from the Applications folder or Launchpad.

###### Note

On first launch, macOS might display a security prompt stating that the
                application is from an unidentified developer or was downloaded from the internet.
                Choose **Open** to continue. If macOS blocks the
                application, open **System Settings → Privacy &
                Security**, scroll to the **Security**
                section, and choose **Open Anyway** next to the
                message about Amazon Quick.

###### To install on Windows

- 
                Download the `.exe`installer file.
- 
                Run the installer and follow the on-screen prompts. 
- 
                After installation completes, launch **Amazon Quick**from the Start menu or desktop shortcut.

###### Note

On first launch, Windows might display a SmartScreen prompt. Choose **More info** and then **Run
                    anyway** to continue.

## Signing in

        The sign-in process depends on your account type. Amazon Quick supports both Free
            and Plus accounts and Professional and Enterprise accounts. When you open the
            application, you see the **Sign in to your Quick
            account** screen with two sign-in options.

###### To sign in with a Free or Plus account

- 
                Open the Amazon Quick desktop application. 
- 
                On the sign-in screen, choose **Continue with**and select your preferred sign-in provider. Available providers include email, Amazon, Apple, Google, and GitHub.
- 
                You are redirected to the quick.aws.com sign-in page. Enter your account credentials for the provider you selected. 
- 
                Complete any multi-factor authentication prompts. 
- 
                After authentication succeeds, the application loads the Home screen. 

###### Note

Enterprise sign-in must be configured by your organization's administrator
                before you can use it. If your administrator has not yet completed the setup,
                see [Setting up Amazon Quick on desktop for enterprise deployments](./desktop-enterprise-setup.html).

###### To sign in with a Professional or Enterprise account

- 
                Open the Amazon Quick desktop application. 
- 
                On the sign-in screen, choose **Enterprise login**.
- 
                You are redirected to your organization's identity provider. Enter your corporate credentials. 
- 
                After authentication succeeds, the application loads the Home screen. 

After you sign in, you can verify your authentication status in **Settings → Capabilities → Connections**. The **Authentication** section displays your signed-in account and
            a green checkmark with the text "Signed in as `your-email`
            (Social)" or your organization's identity type.

## Onboarding and setup

        After you sign in for the first time, Amazon Quick guides you through an onboarding flow to connect your data sources. Connecting your data sources allows Quick to monitor what matters, prepare for meetings, and provide more relevant responses.

The onboarding flow presents the following categories of connections:

| Category | Description | Examples | 
|---|---|---|
| Email | Calendar and email for meeting prep and action items | Microsoft Outlook, Gmail, Google Calendar | 
| Messaging | Threads, DMs, and channels — triage what matters | Slack, Microsoft Teams | 
| Local files | Grant access to folders on your computer | Any folder on your machine | 

For each category, you can choose **Connect** to set
            up the connection immediately, or choose **Dismiss** to
            skip it. Each connection opens a sign-in page where you authenticate with the
            third-party service and grant Quick the required permissions.

###### Tip

You can skip the onboarding flow entirely and connect your data sources later.
                To connect data sources at any time, open **Settings**
                in the sidebar, choose **Capabilities**, and select
                the **Connections** tab. Amazon Quick supports
                connections including Slack, Microsoft Outlook, Microsoft Teams, Gmail,
                Google Calendar, Google Drive, and more. For a complete list of available
                connections, see [Connecting your data sources](./connecting-data-sources-desktop.html).

## After setup

        After you complete the onboarding flow (or skip it), the Amazon Quick Home screen displays:

- 
                A **personalized greeting**based on the time of day.
- 
                The **chat input area**where you can start asking questions or requesting tasks.
- 
                **Connection setup cards**for any data sources you haven't connected yet. You can connect them at any time or dismiss them.
- 
                A **priority feed widget**showing the most important items from your connected services, with suggested actions you can take directly.

You're now ready to start using Amazon Quick on desktop. For an overview of the
            interface, see [Understanding the desktop interface](./desktop-interface.html). To connect additional data
            sources, see [Connecting your data sources](./connecting-data-sources-desktop.html).