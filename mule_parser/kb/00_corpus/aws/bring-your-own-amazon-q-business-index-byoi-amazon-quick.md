# Bring Your Own Amazon Q Business Index (BYOI) - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/quick-byoa.html](https://docs.aws.amazon.com/quick/latest/userguide/quick-byoa.html)

---

Amazon Quick enables you to use your existing Amazon Q Business indexes as data sources. You can leverage your enterprise data without having to recreate indexes. This capability, known as Bring Your Own Index (BYOI), lets you connect your Amazon Q Business indexes to Amazon Quick and use them alongside other data sources for comprehensive analytics and intelligent responses.

BYOI supports two implementation methods:

- **IDC Implementation**
- 
                Uses IAM Identity Center for authentication. Requires both Amazon Q Business and Amazon Quick to authenticate through IAM Identity Center in the same AWS account and region. 
- **Non-IDC Implementation**
- 
                Supports multiple authentication methods including native identities, AWS Managed Microsoft AD, and IAM federation. All Amazon Quick users automatically receive access to connected Amazon Q Business indexes.