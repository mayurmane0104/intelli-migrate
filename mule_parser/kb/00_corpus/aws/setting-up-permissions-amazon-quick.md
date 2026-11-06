# Setting up permissions - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/qbiz-indexes-permissions.html](https://docs.aws.amazon.com/quick/latest/userguide/qbiz-indexes-permissions.html)

---

To use Amazon Q Business indexes in Amazon Quick, you need to set up the appropriate permissions based on your implementation method:

## Initial Setup

            
            - 
                    Sign in to the Amazon Quick console as an administrator. 
- 
                    Navigate to the **Admin**section.
- 
                    Select **AWS Resources**.
- 
                    Choose **Amazon Q Business**from the list of available data sources.
- 
                    Choose **Select Applications**.

## Application Setup

            
            You can either connect to an existing Amazon Q Business application or create a new one:

- 
                    Choose one of the following options: - 
                            **Connect to existing Amazon Q Business application**- Select an existing application from your account.
- 
                            **Create new Amazon Q Business application**- Create a new application. The new application will use the same authentication used by your Amazon Quick instance setup.
 
- 
                            
- 
                    For new applications, the system automatically configures authentication based on your Amazon Quick instance setup. 
- 
                    Wait for application creation to complete. 
- 
                    You will be redirected to the Amazon Q Business application to configure indexes and data sources. 

## Access Management by Implementation

            
            - **IDC Implementation**
- 
                        - 
                                Access is managed through AWS Identity Center. 
- 
                                Access to the Amazon Q Business application is managed through the Amazon Q Business console. 
 
- 
                                
- **Non-IDC Implementation**
- 
                        - 
                                All Amazon Quick users automatically gain access to connected Amazon Q Business indexes. 
- 
                                No additional access management required in Amazon Q Business. 
 
- 
                                

Once permissions are set up, you can use your Amazon Q Business index as a knowledge base in Amazon Quick, and Admin users can create knowledge bases from Amazon Q Business indexes.