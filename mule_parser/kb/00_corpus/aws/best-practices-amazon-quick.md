# Best practices - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/int-actions-best-practices.html](https://docs.aws.amazon.com/quick/latest/userguide/int-actions-best-practices.html)

---

Following best practices for action connectors helps ensure secure, reliable, and efficient operations. These practices help you maintain optimal performance, protect sensitive data, and minimize operational issues.

## Security

         
            ### Authentication management

- 
                    Regular credential rotation - Update API keys and OAuth tokens on a scheduled basis to maintain security. 
- 
                    Periodic permission reviews - Audit user and service permissions quarterly to ensure least-privilege access. 
- 
                    Token lifecycle monitoring - Track token expiration dates and set up alerts before credentials expire. 
- 
                    Access audit logging - Enable comprehensive logging to track who accessed which services and when. 

### Access control

- 
                    Implement least-privilege access - Grant only the minimum permissions necessary for each action to function properly. 
- 
                    Regular permission audits - Review and validate that current permissions align with actual usage patterns and business needs. 
- 
                    Document access patterns - Maintain clear documentation of who has access to which connectors and why. 
- 
                    Monitor usage anomalies - Set up alerts for unusual access patterns that might indicate security issues. 

## Performance

         
            ### Action configuration

- 
                    Optimize form defaults - Pre-populate commonly used values to reduce user input time and errors. 
- 
                    Configure appropriate timeouts - Set realistic timeout values based on typical response times for each service. 
- 
                    Set up error handling - Implement robust error handling with clear user messages and retry logic where appropriate. 
- 
                    Document dependencies - Clearly document any prerequisites or dependencies between different actions. 

### Resource management

- 
                    Monitor API quotas. 
- 
                    Track usage patterns. 
- 
                    Optimize refresh schedules. 
- 
                    Regular cleanup of unused connectors. 

## Maintenance

         
            ### Regular actions

- 
                    Review connector status. 
- 
                    Update configurations. 
- 
                    Validate connections. 
- 
                    Document changes. 

### Troubleshooting

- 
                    Monitor error patterns. 
- 
                    Review CloudWatch logs. 
- 
                    Track resolution times. 
- 
                    Document solutions.