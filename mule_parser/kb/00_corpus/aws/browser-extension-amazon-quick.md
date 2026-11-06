# Browser extension - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/browser-extension.html](https://docs.aws.amazon.com/quick/latest/userguide/browser-extension.html)

---

The Amazon Quick browser extension is available within Amazon Quick to all eligible
            users by default and requires no administrative setup for user access. Users can find
            the browser extension installation link under **Connections** >
                **Extensions**. The following procedures are for IT administrators
            who want to automatically deploy or disable the Amazon Quick browser extension across
            all browsers in their organization using managed device policies.

## Deploy the browser extension

            ###### Note

The following deployment guide applies only when you have a managed device fleet with managed browsers.

To deploy the browser extension to all users in your organization, you can define
                an **ExtensionSettings** policy and distribute this policy to your
                managed devices.

### Install using ExtensionSettings policy

The **ExtensionSettings** policy is an administrative setting
                    for Chrome, Edge, and Firefox that
                    allows you to manage the installation, permissions, and runtime behavior of
                    specific extensions on managed devices. This policy provides granular control by
                    letting administrators specify custom configurations, such as setting
                    installation modes like force install and restricting or allowing specific site
                    access and permissions for individual extensions or all extensions.

The format of the **ExtensionSettings** policy depends on the
                    operating system where you want to distribute this policy.
                        Windows, Mac, and Linux are
                    supported.

To set the install mode in the **ExtensionSettings** policy,
                    you need the extension identifier and the store URL:

- 
                        **Chrome/Edge**- 
                                ID: `innkphffipcmiflfibbeghfnkifiokgo`
- 
                                URL: `https://clients2.google.com/service/update2/crx`
 
- 
                                
- 
                        **Firefox**- 
                                ID: `quick-browser-extension@amazon.com`
- 
                                URL: `https://addons.mozilla.org/firefox/downloads/latest/amazon-quick/latest.xpi`
 
- 
                                

### Distribute ExtensionSettings policy

Distributing the **ExtensionSettings** policy depends on the
                    device and browser management solution used by your organization. You can use
                    managed solutions like **Chrome Enterprise Core** or
                        **Microsoft Edge** management service, or distribute the
                        **ExtensionSettings** policy using **Group
                        Policy**, which differs per operating system.

## Disable the browser extension

            ###### Note

The following deployment guide applies only when you have a managed device fleet with managed browsers.

To disable the browser extension for all users in your organization, you can
                define an **ExtensionSettings** policy and distribute this policy
                to your managed devices.

### Disable using ExtensionSettings policy

The **ExtensionSettings** policy is an administrative setting
                    for Chrome, Edge, and Firefox that allows you to manage the installation,
                    permissions, and runtime behavior of specific extensions on managed devices.
                    This policy provides granular control by letting administrators specify custom
                    configurations, such as disabling individual extensions.

The format of the **ExtensionSettings** policy depends on the
                    operating system where you want to distribute this policy. See the documentation
                    for the **ExtensionSettings** policy to determine the format.
                    Windows, Mac, and Linux are supported.

To block the use of the extension in the
                        **ExtensionSettings** policy, you need the extension
                    identifier:

- 
                        **Chrome/Edge**ID: `innkphffipcmiflfibbeghfnkifiokgo`
- 
                        **Firefox**ID: `quick-browser-extension@amazon.com`

### Distribute ExtensionSettings policy

Distributing the **ExtensionSettings** policy depends on the
                    device and browser management solution used by your organization. You can use
                    managed solutions like **Chrome Enterprise Core** or
                        **Microsoft Edge** management service, or distribute the
                        **ExtensionSettings** policy using **Group
                        Policy**, which differs per operating system.