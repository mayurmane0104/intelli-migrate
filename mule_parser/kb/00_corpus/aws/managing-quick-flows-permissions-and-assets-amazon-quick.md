# Managing Quick Flows permissions and assets - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/managing-quick-flows-permissions-and-assets.html](https://docs.aws.amazon.com/quick/latest/userguide/managing-quick-flows-permissions-and-assets.html)

---

Administrators manage Quick Flows permissions and assets through two interfaces in the Quick console: the Custom Permissions page and the Asset Management page.

## Custom Permissions page

        The Custom Permissions page controls which Quick Flows capabilities and features are available to users.

### Restrict capabilities

- **Enable or disable flows**— Control whether Quick Flows is available to users in your account. When disabled, all Quick Flows functionality is unavailable, but existing flows are preserved. Quick Flows is enabled by default for new Quick instances.

### Restrict features

- **Allow creators to share without approval**— When enabled, creators can share flows without review. When disabled, all eligible users can review and approve flow sharing requests.
- **Enable bedrock model usage in General knowledge step for output refinement**— Controls whether Bedrock models are available for General knowledge steps. Enabled by default.
- **Enable UI agent to perform browser tasks**(Preview) — Controls whether UI agent steps can be used in flows.

## Asset Management page

        The Asset Management page provides oversight of all flows in your organization.

- **Share flows**— Share flows on behalf of creators, redistribute flows to different groups, or manage sharing permissions across the organization.
- **Transfer ownership**— Transfer flow ownership between users, such as when a creator leaves the organization.
- **Unlist flows**— Remove flows from the shared library, making them unavailable to viewers while preserving them for the creator to edit. Unlisted flows can be re-shared once issues are resolved.