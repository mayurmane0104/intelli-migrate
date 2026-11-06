# Monitor Applications and Servers | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/runtime-manager/monitoring](https://docs.mulesoft.com/runtime-manager/monitoring)

---

# Monitor Applications and Servers

After you deploy your application, use the monitoring dashboards in Runtime Manager to monitor the application’s performance. If you deployed the application to an on-premises server, you can also monitor the server.

Depending on the [deployment option](deployment-strategies) you use, different monitoring resources are available, including alerts, dashboards, notifications, and flow metrics.

| For CloudHub 2.0 deployments, the Runtime Manager monitoring feature is available for applications only. For more information, see [Monitoring Apps Deployed to CloudHub 2.0](../cloudhub-2/ch2-monitor-apps). | 

## Monitoring Servers

On applications that are deployed on-premises, use the following tools to get information about the servers.

- 
[Alerts](alerts-on-runtime-manager#conditions-on-mule-servers)![CloudHub logo cloud active](_images/logo-cloud-active.png)  ![Hybrid logo hybrid active](_images/logo-hybrid-active.png) Send e-mail alerts whenever key events occur. A history of when these alerts were triggered can also be accessed. 
- 
[Monitoring Dashboards](monitoring-dashboards#the-dashboard-for-a-server)![CloudHub logo cloud active](_images/logo-cloud-active.png)  ![Hybrid logo hybrid active](_images/logo-hybrid-active.png)  ![Anypoint Platform PCE logo server active](_images/logo-server-active.png)  ![Runtime Fabric logo rtf active](_images/logo-rtf-active.png) See the evolution of key performance metrics related to service usage and available processing power To use Runtime Manager monitoring dashboards when running Mule on Windows, the Mule service must be started by a user that belongs to the **Performance Log Users**group.