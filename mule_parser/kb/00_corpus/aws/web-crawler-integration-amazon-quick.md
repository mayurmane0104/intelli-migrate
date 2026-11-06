# Web Crawler integration - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/web-crawler-integration.html](https://docs.aws.amazon.com/quick/latest/userguide/web-crawler-integration.html)

---

With Web Crawler integration in Amazon Quick, you can create knowledge bases from website content by crawling and indexing web pages. This integration supports data ingestion capabilities with different authentication options.

## Web Crawler capabilities

        
        Web Crawler users can ask questions about content stored on websites and web pages. For example, users can search documentation sites, knowledge bases, or specific information across multiple web pages.

The integration helps users access and understand web content regardless of location or type. It provides contextual details such as publication dates, modification history, and page ownership for more efficient information discovery.

###### Note

Web Crawler integration supports data ingestion only. It doesn't provide action capabilities for managing websites or web services.

## Prerequisites

        
        Before you set up Web Crawler integration, make sure you have the following:

- 
                Website URLs to crawl and index. 
- 
                An Amazon Quick Enterprise subscription. 
- 
                A website that is not behind a firewall and does not require special browser plugins to connect. 

## Prepare website access and authentication

        
        Before setting up the integration in Amazon Quick, prepare your website access credentials. Web Crawler integration supports different authentication methods:

- **No authentication**
- 
                    Use for crawling websites that don't require authentication. 
- **Basic authentication**
- 
                    Standard HTTP Basic Authentication for secured websites. When you visit a protected site, your browser displays a dialog box that asks for your credentials. **Required credentials:**- 
                            **Login page URL**- The URL of the login page
- **Username**- Basic auth username
- **Password**- Basic auth password
 
- 
                            
- **Form authentication**
- 
                    For websites that use HTML form-based login pages. You specify XPath expressions to identify the form fields on the login page. XPath (XML Path Language) is a query language for navigating elements in an HTML or XML document. To find an XPath for a web page element, right-click the element in your browser and choose **Inspect**. In the developer tools, right-click the highlighted HTML code, choose**Copy**, and then choose**Copy XPath**.**Required information:**- **Login page URL**- URL of the login form (for example,- `https://example.com/login`)
- **Username**- Login username
- **Password**- Login password
- **Username field XPath**- XPath to username input field (for example,- `//input[@id='username']`)
- 
                            **Username button XPath**(Optional) - XPath to username button field (for example,`//input[@id='username_button']`)
- **Password field XPath**- XPath to password input field (for example,- `//input[@id='password']`)
- **Password button XPath**- XPath to password button (for example,- `//button[@type='password']`)
 
- **SAML authentication**
- 
                    For websites that use SAML-based single sign-on (SSO) authentication. SAML (Security Assertion Markup Language) authentication is a federated identity standard that enables SSO. Users authenticate through a centralized identity provider (such as Microsoft Azure AD or Okta) instead of entering credentials directly into each application. The identity provider passes a secure token back to the application to grant access. **Required information:**- **Login page URL**- URL of the SAML login page
- **Username**- SAML username
- **Password**- SAML password
- 
                            **Username field XPath**- XPath to username input field (for example,`//input[@id='username']`)
- 
                            **Username button XPath**(Optional) - XPath to username button field (for example,`//input[@id='username_button']`)
- 
                            **Password field XPath**- XPath to password input field (for example,`//input[@id='password']`)
- 
                            **Password button XPath**- XPath to password button (for example,`//button[@type='password']`)
 

### XPath configuration examples

Use these XPath examples to configure form and SAML authentication:

```
Username field examples:
//input[@id='username']
//input[@name='user']
//input[@class='username-field']
Password field examples:
//input[@id='password']
//input[@name='pass']
//input[@type='password']
Submit button examples:
//button[@type='submit']
//input[@type='submit']
//button[contains(text(), 'Login')]
            
```
## Set up Web Crawler integration

        
        After preparing your website access requirements, create the Web Crawler integration in Amazon Quick.

- 
                In the Amazon Quick console, choose **Knowledge**.
- 
                Find **Web Crawler**and choose the**Add**(+) icon.
- 
                Choose **Access data from Web Crawler**. Web Crawler integration supports data access only - action execution is not available for web crawling.
- 
                Configure integration details and authentication method, then create knowledge bases as needed. - 
                        Choose the authentication type for your web crawler integration. 
- 
                        Enter the required details based on your chosen authentication method. 
- 
                        (Optional) Choose a VPC connection to crawl sites hosted in your private network. The VPC connection must be configured in admin settings before you can choose it here. For more information, see [Setting up a VPC to use with Amazon Quick](./vpc-setup-for-quicksight.html).###### NoteYou can't change the VPC connection after the integration is created. To use a different VPC connection, create a new integration. 
- 
                        Choose **Create and continue**.
- 
                        Enter the name and description for your knowledge base. 
- 
                        Add the content URLs that you want to crawl. 
- 
                        Choose **Create**.
 
- 
                        

After you choose **Create**, the data sync starts automatically.

## Configure crawling

        
        You can configure which websites and pages to crawl and how to filter the content.

### Configure URLs and content sources

Configure which websites and pages to crawl:

#### Direct URLs

Specify individual URLs to crawl:

```
https://example.com/docs
https://example.com/blog
https://example.com/support
                
```
**Limit:** Maximum 10 URLs per dataset

### Content filters and crawl settings

#### Crawl scope settings

To view these settings, you must first set up a knowledge base and then examine the advanced settings option.

- **Crawl depth**
- 
                            - Range: 0-10 (default: 1) 
- 0 = crawl only specified URLs 
- 1 = include linked pages one level deep 
- Higher values follow links deeper into the site 
 
- **Maximum links per page**
- 
                            - Default: 1000 
- Maximum: 1,000 
- Controls how many links to follow from each page 
 
- **Wait time**
- 
                            - Default: 1 
- 
                                    The time (in seconds) that the web crawler waits for each page after the page reaches a ready state. Increase this value for pages with dynamic JavaScript content that loads after the main template. 
 

## Manage knowledge bases

        
        After setting up your Web Crawler integration, you can create and manage knowledge bases from your crawled website content.

### Edit existing knowledge bases

You can modify your existing Web Crawler knowledge bases:

- 
                    In the Amazon Quick console, choose **Knowledge bases**.
- 
                    Choose your Web Crawler knowledge base from the list. 
- 
                    Choose the three-dot icon under **Actions**, then choose**Edit knowledge base**.
- 
                    Update your configuration settings as needed and choose **Save**.

### Attachments and file crawling

Control whether the system processes files and attachments linked from web pages:

- 
                    **Enable file attachment crawling**– Choose this option to crawl and index files and attachments found on web pages, such as PDFs, documents, and media files.

### Crawling behavior and sync configuration

Your Web Crawler integration follows these crawling practices:

- **Incremental sync model:**First sync performs full crawl. Subsequent syncs capture changes only.
- **Automatic retry:**Built-in retry logic for failed requests.
- **Duplicate handling:**Automatic detection and deduplication of URLs.
- **Crawler identification:**Identifies itself with user-agent string "aws-quick-on-behalf-of-<UUID>" in request headers.

#### Sitemap discovery

Web Crawler automatically checks for sitemaps by appending common sitemap paths to your seed URLs. You don't need to provide sitemap URLs separately. The following paths are checked:

`sitemap.xml sitemap_index.xml sitemap/sitemap.xml sitemap/sitemap_index.xml sitemaps/sitemap.xml sitemap/index.xml`

For example, if your seed URL is `https://example.com/docs`, the crawler checks for `https://example.com/docs/sitemap.xml`, `https://example.com/docs/sitemap_index.xml`, and so on.

###### Note

Web Crawler does not follow recursive sitemap index references. Only the URLs listed directly in a discovered sitemap are used. Sitemap directives in robots.txt are not used for sitemap discovery.

#### Robots.txt compliance

Web Crawler respects the robots.txt protocol and honors user-agent and allow/disallow directives. This enables you to control how the crawler accesses your site.

##### How robots.txt checking works

- **Host-level checking:**Web Crawler reads robots.txt files at the host level (for example, example.com/robots.txt)
- **Multiple host support:**For domains with multiple hosts, Web Crawler honors robots rules for each host separately
- **Fallback behavior:**If Web Crawler can't fetch robots.txt due to blocking, parsing errors, or timeouts, it behaves as if robots.txt doesn't exist. In this case, the crawler proceeds to crawl the site.

##### Supported robots.txt fields

Web Crawler recognizes these robots.txt fields (field names are case-insensitive, values are case-sensitive):

- `user-agent`
- Identifies which crawler the rules apply to. 
- `allow`
- A URL path that may be crawled. 
- `disallow`
- A URL path that may not be crawled. 
- `crawl-delay`
- The time (in seconds) to wait between requests to your website. 

#### Meta tag support

Web Crawler supports page-level robots meta tags that you can use to control how your data is used. You can specify page-level settings by including a meta tag on HTML pages or in an HTTP header.

##### Supported meta tags

- `noindex`
- Do not index the page. If you don't specify this rule, the page may be indexed and eligible to appear in experiences. 
- `nofollow`
- Do not follow the links on this page. If you don't specify this rule, Web Crawler may use the links on the page to discover those linked pages. 

You can combine multiple values using a comma (for example, "noindex, nofollow").

###### Note

To detect meta tags, Web Crawler must access your page. Don't block your page with robots.txt, because this prevents the page from being recrawled.

## Troubleshooting

        
        Use this section to resolve common issues with Web Crawler integration.

### Authentication failures

**Symptoms:**

- "Unable to authenticate" error messages 
- 401/403 HTTP responses 
- Login page redirect loops 
- Session timeout errors 

**Resolution steps:**

- Verify the site is reachable from the AWS Region where the Amazon Quick instance is set up. 
- Verify that your credentials are correct and haven't expired. 
- Check authentication endpoint availability and accessibility. 
- Validate XPath configurations by testing them in browser developer tools. 
- Review browser network logs to understand the authentication flow. 
- Ensure the login page URL is correct and accessible. 
- Test authentication manually using the same credentials. 

### Access and connectivity issues

**Symptoms:**

- Connection timeouts and network errors 
- Network unreachable errors 
- DNS resolution failures 

**Resolution steps:**

- 
                    Verify network connectivity to target websites. 
- 
                    Validate site accessibility: - Check DNS resolution for target domains. 
- Verify SSL/TLS configuration and certificates. 
- Test access from different networks if possible. 
 

### DNS resolution

The Web Crawler uses DNS to resolve website hostnames (for example, `www.example.com`) to IP addresses. By default, it uses public DNS resolution.

When crawling sites inside a VPC, you may need to configure a private DNS server so the crawler can resolve hostnames for internal sites. Choose one of the following options based on your VPC configuration:

- 
                    **Use the VPC-provided DNS server**— If your VPC has both**DNS hostnames**and**DNS resolution**enabled, you can use the default VPC DNS resolver (typically 10.0.0.2, or more generally the VPC CIDR base+2). For more information, see[VPC](./vpc-amazon-virtual-private-cloud.html).
- 
                    **Use a custom DNS server**— If your VPC uses a custom DNS resolver, provide the IP address of your organization's internal DNS server. Work with your network administrator to obtain this address.

If you don't configure a DNS server, the crawler resolves only publicly registered hostnames.

### JavaScript-dependent navigation

**Symptoms:**

- Only the seed URL is indexed, no additional pages discovered 
- Crawl completes successfully but returns only one document 

**Resolution steps:**

- 
                    Web Crawler executes JavaScript and renders page content, but does not simulate user interactions such as clicks, scrolls, or hover actions. If your site loads navigation links through user interaction (for example, click handlers, infinite scroll, or dynamic menus), the crawler cannot discover those links. 
- 
                    Inspect your page in browser developer tools to check if navigation links use standard `<a href="...">`elements. If links are wired through JavaScript event handlers instead, the crawler will not follow them.
- 
                    If your site provides a sitemap, Web Crawler automatically checks for common sitemap paths on your seed URLs. Ensure your sitemap is available at a standard location (for example, `/sitemap.xml`) so the crawler can discover additional URLs without relying on in-page link extraction.
- 
                    Alternatively, provide all target page URLs directly as seed URLs. 
- 
                    If content can be exported as HTML, PDF, or text files, consider using the Amazon S3 connector as your data source instead. 

### Crawl and content issues

**Symptoms:**

- Missing or incomplete content 
- Incomplete crawls or early termination 
- Rate limiting errors (429 responses) 
- Content not being indexed properly 

**Resolution steps:**

- 
                    Review robots.txt restrictions: - Check robots.txt file for crawl restrictions. 
- Verify that the crawler is allowed to access target paths. 
- Ensure robots.txt compliance isn't blocking content. 
 
- 
                    Check rate limiting and throttling: - Monitor response headers for rate limit information. 
- Implement appropriate crawl delays. 
 
- 
                    Verify URL patterns and filters: - Test regex patterns for accuracy. 
- Check URL formatting and structure. 
- Validate include/exclude pattern logic. 
 
- 
                    Review content restrictions: - Check for noindex meta tags on pages. 
- Verify content type support. 
- Ensure content size is within limits. 
 
- 
                    Update the wait time so that the content loads on the page before the crawler starts crawling. 

### Known limitations

Web Crawler integration has the following limitations:

- **URL limits:**Maximum of 10 seed URLs per dataset. You can't provide sitemap URLs in the seed URL field.
- **Crawl depth:**Maximum crawl depth of 10 levels
- **Security requirements:**HTTPS required for web proxy configurations

The following limitations apply when using the Web Crawler with a VPC connection:

- **No HTTP/3 (QUIC) support:**HTTP/3 is not supported. Most sites will fall back to HTTP/2 automatically, but sites configured for HTTP/3 only will not be accessible.
- **DNS over TCP required:**DNS resolution must use TCP. Verify that your DNS server supports DNS over TCP before configuring VPC crawling.
- **Publicly trusted SSL certificates required:**Internal sites must use a certificate from a well-known certificate authority (for example, Let's Encrypt or DigiCert). Sites using self-signed or private CA certificates will fail to connect.
- **IPv4 only:**Only IPv4 addresses are supported. Sites accessible exclusively over IPv6 cannot be crawled.