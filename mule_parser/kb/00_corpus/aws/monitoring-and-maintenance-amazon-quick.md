# Monitoring and maintenance - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/int-actions-monitoring.html](https://docs.aws.amazon.com/quick/latest/userguide/int-actions-monitoring.html)

---

Monitoring your action connectors helps ensure reliable performance and identify issues before they impact users. Regular monitoring allows you to track usage patterns, optimize performance, and maintain healthy connections to external services.

## Performance monitoring

        You can assess action connector performance using the following metrics and analytics.

### CloudWatch metrics

- 
                    Action execution success rates - Track the percentage of successful action executions to identify reliability issues. 
- 
                    Response times - Monitor how long actions take to complete and identify performance bottlenecks. 
- 
                    Error frequencies - Track error patterns to identify common failure points and areas for improvement. 
- 
                    API quota usage - Monitor usage against service limits to prevent throttling and plan for capacity. 

### Usage analytics

The following usage analytics are collected for action connectors:

- 
                    Active users - Track how many users are actively using action connectors to understand adoption and usage patterns. 
- 
                    Popular actions - Identify which actions are used most frequently to prioritize optimization efforts. 
- 
                    Execution patterns - Analyze when and how often actions are executed to optimize resource allocation. 
- 
                    Error trends - Monitor error patterns over time to identify systemic issues and improvement opportunities. 

## Connection health

        You can assess action connector health using the following connection health tools:

### Status monitoring

- 
                    Connection state - Monitor whether connectors are actively connected and functioning properly. 
- 
                    Authentication validity - Track the status of authentication tokens and credentials to prevent access failures. 
- 
                    Token expiration tracking - Monitor when authentication tokens will expire and need renewal. 
- 
                    Service availability - Track the availability and response status of connected external services. 

### Automated maintenance

- 
                    Token refresh handling. 
- 
                    Connection recovery. 
- 
                    Error retry logic. 
- 
                    Performance optimization. 

## CloudWatch metrics reference

        | Metric | Description | Unit | 
|---|---|---|
| ActionSuccess | Successful executions | Count | 
| ActionLatency | Execution time | Milliseconds | 
| AuthFailures | Failed authentications | Count | 
| APIThrottling | API throttling events | Count |