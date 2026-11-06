# Troubleshooting - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/qbiz-indexes-troubleshooting.html](https://docs.aws.amazon.com/quick/latest/userguide/qbiz-indexes-troubleshooting.html)

---

## Amazon Q Business not seen in Integrations page

            
            **Symptoms**

- 
                    Amazon Q Business option missing from Integrations page 
- 
                    Cannot create new Amazon Q Business integration 

**Resolution**

- 
                    Only Admin users have access to create a Amazon Q Business/BYOI knowledge base 
- 
                    Verify user has Admin persona permissions 

## Failed to fetch Amazon Q Business applications

            
            **Resolution**

- 
                    Confirm Amazon Q Business is enabled in the Admin console 
- 
                    Try logging out and back in to refresh the session, then retry the operation 

## Amazon Q Business application not seen in the list of applications displayed during knowledge base creation

            
            **Symptoms**

- 
                    Amazon Q Business applications list is empty on Create Knowledge Base page 
- 
                    Amazon Q Business applications list is populated but missing expected applications 

**Resolution**

- 
                    Check if missing Amazon Q Business applications were granted permissions in the AWS resources page of the Admin console 

## Failed to create dataset. Chat instance is not ready. Please try again later

            
            **Symptoms**

- 
                    Knowledge base creation fails with error "Chat instance is not ready. Please try again later" 
- 
                    Unable to complete knowledge base creation process 

**Resolution**

- 
                    If this is the first time creating a knowledge base in Amazon Quick, wait 5 minutes and retry the operation