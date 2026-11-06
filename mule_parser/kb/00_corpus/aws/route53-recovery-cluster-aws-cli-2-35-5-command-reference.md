# route53-recovery-cluster — AWS CLI 2.35.5 Command Reference

**Source:** [https://docs.aws.amazon.com/cli/latest/reference/route53-recovery-cluster/index.html](https://docs.aws.amazon.com/cli/latest/reference/route53-recovery-cluster/index.html)

---

[ [aws](../index.html#cli-aws) ]

Welcome to the Routing Control (Recovery Cluster) API Reference Guide for Amazon Route 53 Application Recovery Controller.

With Route 53 ARC, you can use routing control with extreme reliability to recover applications by rerouting traffic across Availability Zones or Amazon Web Services Regions. Routing controls are simple on/off switches hosted on a highly available cluster in Route 53 ARC. A cluster provides a set of five redundant Regional endpoints against which you can run API calls to get or update the state of routing controls. To implement failover, you set one routing control to ON and another one to OFF, to reroute traffic from one Availability Zone or Amazon Web Services Region to another.

Be aware that you must specify a Regional endpoint for a cluster when you work with API cluster operations to get or update routing control states in Route 53 ARC.In addition, you must specify the US West (Oregon) Region for Route 53 ARC API calls. For example, use the parameter`--region us-west-2`with AWS CLI commands. For more information, see[Get and update routing control states using the API](https://docs.aws.amazon.com/r53recovery/latest/dg/routing-control.update.api.html)in the Amazon Route 53 Application Recovery Controller Developer Guide.

This API guide includes information about the API operations for how to get and update routing control states in Route 53 ARC. To work with routing control in Route 53 ARC, you must first create the required components (clusters, control panels, and routing controls) using the recovery cluster configuration API.

For more information about working with routing control in Route 53 ARC, see the following: