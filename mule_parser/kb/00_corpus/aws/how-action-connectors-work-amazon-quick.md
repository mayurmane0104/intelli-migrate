# How action connectors work - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/int-actions-how-it-works.html](https://docs.aws.amazon.com/quick/latest/userguide/int-actions-how-it-works.html)

---

Action connectors in Amazon Quick create secure connections between Amazon Quick and external services. When you configure these integrations, you can perform actions based on your authentication level and permissions.

## Core components

        - **Action connectors**
- 
                    The foundational resources that integrate with external services. For a list of supported connectors, see [Supported integrations](./supported-integrations.html). For information about setting up AWS built-in service action connectors, see[AWS service action connectors](./builtin-services-integration.html).
- **Authentication methods**
- 
                    Action connectors support multiple authentication methods including Default OAuth app, Custom OAuth app, Service-to-Service OAuth, and API key. For detailed information about each authentication method, see [Authentication methods](./quick-action-auth.html).
- **Implementation types**
- 
                    - 
                            **On-demand actions for immediate, user-triggered operations**- Real-time operations that execute immediately when you trigger them. You can initiate actions through chat interfaces, dashboards, or Amazon Q Apps. Examples include creating tickets, sending messages, or querying data.
- 
                            **Automated workflows for scheduled or system-triggered tasks**- System-managed operations that execute based on schedules or triggers. They run in the background without user intervention. Examples include data synchronization, report generation, or system maintenance.
 
- 
                            
- **Permission models**
- 
                    - 
                            **Personal access permissions through 3LO**- You can grant specific permissions to Amazon Quick through Three-Legged OAuth, maintaining control over your service access. Permissions are tied to your identity and credentials in the target service.
- 
                            **Service-level permissions for automated workflows**- Applied to automated workflows, these permissions support system-to-system interactions without user involvement. They're configured at the service level and typically use API keys or service account credentials.
- 
                            **Entity-level access controls**- Govern access to actions within Amazon Quick, determining which users or groups can execute specific actions. These controls integrate with Amazon Quick's broader permission system for consistent access management across the platform.
 
-