# Managing domains - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/manage-domains.html](https://docs.aws.amazon.com/quick/latest/userguide/manage-domains.html)

---

| Applies
                    to:Enterprise Edition | 

| Intended audience: Amazon Quick administrators | 

In Amazon Quick Enterprise edition, you can embed Amazon Quick Sight dashboards, visuals, consoles,
        and Q search bars in an app or web page. Domains that are going to host these embedded
        assets must be on an *allow list*, the list of approved domains for your
        Quick subscription. This requirement protects your data by preventing unapproved
        domains from hosting embedded dashboards. To embed a Amazon Quick Sight dashboard, visual, console, or
        Q search bar to a web page or app, add approved domains to a static allow list in the
        Quick console. Alternatively, add them at runtime with the Quick
        API.

Use the following sections to learn more about adding domains for embedded analytics.

## Allow listing static domains

        You can add static domains to your allow list through the Amazon Quick console. All domains on your allow list (such as development, staging, and production) must be explicitly allowed, and they must use HTTPS. You can add up to 100 domains to the allow list.

To embed a dashboard to a static domain:

- 
                Approve the hosting domains and subdomains for embedding. 
- 
                Publish the dashboard. 
- 
                Share the dashboard with users or groups so they can see the embedded version of it. 

Use the following procedure to view or edit the list of approved domains.

###### To view or edit the list of approved domains

- 
                Choose the profile icon at top right. 
- 
                Choose **Manage Amazon Quick**. You must be an Amazon Quick admin to access this screen.
- 
                Choose **Domains and Embedding**on the left. The domains that you can embed a dashboard in are listed at the bottom of the page.
- 
                (Optional) Add a new domain here by entering it in the **Domain**box. You can also choose**Include subdomains**to allow embedded dashboards on all subdomains. Choose**Add**to add the domain.You can edit or delete existing domain by choosing the icons next to each domain in the list at the bottom of the page. 

Make sure that you use a valid HTTPS URL. The following list shows examples of URLs that are valid for embedded dashboards that use a static domain:

- 
                https://example-1.com 
- 
                https://www.アマゾンドメイン.jp 
- 
                https://www.亚马逊域名.cn:1234 
- 
                https://111.222.33.44:1234 
- 
                https://111.222.33.44 
- 
                http://localhost 

The following list shows examples of URLs that are *not* valid for
            embedded dashboards:

- 
                http://example 
- 
                https://example.com.*.example-1.co.uk 
- 
                https://co.uk 
- 
                https://111.222.33.44.55:1234 
- 
                https://111.222.33.44.55 

## Allow listing domains at runtime with the Amazon Quick API

        You can add a domain at runtime to an allow list with the `AllowedDomains`
            parameter of a `GenerateEmbedUrlForAnonymousUser` or a
                `GenerateEmbedUrlForRegisteredUser` API call. The
                `AllowedDomains` parameter is an optional parameter. It grants you the
            option as a developer to override the static domains that are configured in the
                **Manage Amazon Quick** menu. 

You can list up to three domains or subdomains. Adding domains to the allow list at
            runtime also adds HTTP support for the domain `localhost`. The generated URL
            is then embedded in a developer's website. Only the domains that are listed in the
            parameter can access the embedded dashboard.

###### Security best practice for IAM condition operators

Improperly configured IAM condition operators can allow unauthorized access to your embedded Quick resources through URL variations. When using the `quicksight:AllowedEmbeddingDomains` condition key in your IAM policies, use condition operators that either allow specific domains or deny all domains that are not specifically allowed. For more information about IAM condition operators, see [IAM JSON policy elements: Condition operators](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html) in the IAM User Guide.

Many different URL variations can point to the same resource. For example, the following URLs all resolve to the same content:

- `https://example.com`
- `https://example.com/`
- `https://Example.com`

If your policy uses operators that do not account for these URL variations, an attacker can bypass your restrictions by providing equivalent URL variations.

You must validate that your IAM policy uses appropriate condition operators to prevent bypass vulnerabilities and ensure that only your intended domains can access your embedded resources.

To embed a dashboard to a domain at runtime, see [Embedding with the Amazon Quick APIs](https://docs.aws.amazon.com/quicksight/latest/user/embedded-analytics-api.html).

Make sure that you use a valid URL. The following list shows examples of URLs that are valid for embedded dashboards that use a runtime domain:

- 
                https://example-1.com 
- 
                http://localhost 
- 
                https://www.アマゾンドメイン.jp 
- 
                https://*.sapp.amazon.com 

The following list shows examples of URLs that are *not* valid for
            embedded dashboards:

- 
                https://example.com.*.example-1.co.uk 
- 
                https://co.uk 
- 
                https://111.222.33.44.55:1234 
- 
                https://111.222.33.44.55 

For more information about embedded dashboards, see [Embedding with the Amazon Quick APIs](https://docs.aws.amazon.com/quicksight/latest/user/embedded-analytics-api.html).