# AWS KMS examples using AWS CLI with Bash script - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/bash_kms_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/bash_kms_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Bash script with AWS KMS.

*Scenarios* are code examples that show you how to accomplish specific tasks by calling multiple functions within a service or combined with other AWS services.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Scenarios

    The following code example shows how to manage encryption options for DynamoDB tables.

- Create a table with default encryption. 
- Create a table with a customer managed CMK. 
- Update table encryption settings. 
- Describe table encryption. 

- **AWS CLI with Bash script**
- 
            
                    Create a table with default encryption. `# Create a table with default encryption (AWS owned key) aws dynamodb create-table \ --table-name CustomerData \ --attribute-definitions \ AttributeName=CustomerID,AttributeType=S \ --key-schema \ AttributeName=CustomerID,KeyType=HASH \ --billing-mode PAY_PER_REQUEST \ --sse-specification Enabled=true,SSEType=KMS`Create a table with a customer managed CMK. `# Step 1: Create a customer managed key in KMS aws kms create-key \ --description "Key for DynamoDB table encryption" \ --key-usage ENCRYPT_DECRYPT \ --customer-master-key-spec SYMMETRIC_DEFAULT # Store the key ID for later use KEY_ID=$(aws kms list-keys --query "Keys[?contains(KeyArn, 'Key for DynamoDB')].KeyId" --output text) # Step 2: Create a table with the customer managed key aws dynamodb create-table \ --table-name SensitiveData \ --attribute-definitions \ AttributeName=RecordID,AttributeType=S \ --key-schema \ AttributeName=RecordID,KeyType=HASH \ --billing-mode PAY_PER_REQUEST \ --sse-specification Enabled=true,SSEType=KMS,KMSMasterKeyId=$KEY_ID`Update table encryption. `# Update a table to use a different KMS key aws dynamodb update-table \ --table-name CustomerData \ --sse-specification Enabled=true,SSEType=KMS,KMSMasterKeyId=$KEY_ID`Describe table encryption. `# Describe the table to see encryption settings aws dynamodb describe-table \ --table-name CustomerData \ --query "Table.SSEDescription"`- 
                    For API details, see the following topics in *AWS CLI Command Reference*.
 
-