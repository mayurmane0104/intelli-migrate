# HealthImaging examples using AWS CLI with Bash script - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/bash_medical-imaging_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/bash_medical-imaging_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Bash script with HealthImaging.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `CreateDatastore`.

- **AWS CLI with Bash script**
- 
            
                
                `############################################################################### # function errecho # # This function outputs everything sent to it to STDERR (standard error output). ############################################################################### function errecho() { printf "%s\n" "$*" 1>&2 } ############################################################################### # function imaging_create_datastore # # This function creates an AWS HealthImaging data store for importing DICOM P10 files. # # Parameters: # -n data_store_name - The name of the data store. # # Returns: # The datastore ID. # And: # 0 - If successful. # 1 - If it fails. ############################################################################### function imaging_create_datastore() { local datastore_name response local option OPTARG # Required to use getopts command in a function. # bashsupport disable=BP5008 function usage() { echo "function imaging_create_datastore" echo "Creates an AWS HealthImaging data store for importing DICOM P10 files." echo " -n data_store_name - The name of the data store." echo "" } # Retrieve the calling parameters. while getopts "n:h" option; do case "${option}" in n) datastore_name="${OPTARG}" ;; h) usage return 0 ;; \?) echo "Invalid parameter" usage return 1 ;; esac done export OPTIND=1 if [[ -z "$datastore_name" ]]; then errecho "ERROR: You must provide a data store name with the -n parameter." usage return 1 fi response=$(aws medical-imaging create-datastore \ --datastore-name "$datastore_name" \ --output text \ --query 'datastoreId') local error_code=${?} if [[ $error_code -ne 0 ]]; then aws_cli_error_log $error_code errecho "ERROR: AWS reports medical-imaging create-datastore operation failed.$response" return 1 fi echo "$response" return 0 }`- 
                    For API details, see [CreateDatastore](https://docs.aws.amazon.com/goto/aws-cli/medical-imaging-2023-07-19/CreateDatastore)in*AWS CLI Command Reference*.
 ###### NoteThere's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/aws-cli/bash-linux/medical-imaging#code-examples).
- 
                    

The following code example shows how to use `DeleteDatastore`.

- **AWS CLI with Bash script**
- 
            
                
                `############################################################################### # function errecho # # This function outputs everything sent to it to STDERR (standard error output). ############################################################################### function errecho() { printf "%s\n" "$*" 1>&2 } ############################################################################### # function imaging_delete_datastore # # This function deletes an AWS HealthImaging data store. # # Parameters: # -i datastore_id - The ID of the data store. # # Returns: # 0 - If successful. # 1 - If it fails. ############################################################################### function imaging_delete_datastore() { local datastore_id response local option OPTARG # Required to use getopts command in a function. # bashsupport disable=BP5008 function usage() { echo "function imaging_delete_datastore" echo "Deletes an AWS HealthImaging data store." echo " -i datastore_id - The ID of the data store." echo "" } # Retrieve the calling parameters. while getopts "i:h" option; do case "${option}" in i) datastore_id="${OPTARG}" ;; h) usage return 0 ;; \?) echo "Invalid parameter" usage return 1 ;; esac done export OPTIND=1 if [[ -z "$datastore_id" ]]; then errecho "ERROR: You must provide a data store ID with the -i parameter." usage return 1 fi response=$(aws medical-imaging delete-datastore \ --datastore-id "$datastore_id") local error_code=${?} if [[ $error_code -ne 0 ]]; then aws_cli_error_log $error_code errecho "ERROR: AWS reports medical-imaging delete-datastore operation failed.$response" return 1 fi return 0 }`- 
                    For API details, see [DeleteDatastore](https://docs.aws.amazon.com/goto/aws-cli/medical-imaging-2023-07-19/DeleteDatastore)in*AWS CLI Command Reference*.
 ###### NoteThere's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/aws-cli/bash-linux/medical-imaging#code-examples).
- 
                    

The following code example shows how to use `GetDatastore`.

- **AWS CLI with Bash script**
- 
            
                
                `############################################################################### # function errecho # # This function outputs everything sent to it to STDERR (standard error output). ############################################################################### function errecho() { printf "%s\n" "$*" 1>&2 } ############################################################################### # function imaging_get_datastore # # Get a data store's properties. # # Parameters: # -i data_store_id - The ID of the data store. # # Returns: # [datastore_name, datastore_id, datastore_status, datastore_arn, created_at, updated_at] # And: # 0 - If successful. # 1 - If it fails. ############################################################################### function imaging_get_datastore() { local datastore_id option OPTARG # Required to use getopts command in a function. local error_code # bashsupport disable=BP5008 function usage() { echo "function imaging_get_datastore" echo "Gets a data store's properties." echo " -i datastore_id - The ID of the data store." echo "" } # Retrieve the calling parameters. while getopts "i:h" option; do case "${option}" in i) datastore_id="${OPTARG}" ;; h) usage return 0 ;; \?) echo "Invalid parameter" usage return 1 ;; esac done export OPTIND=1 if [[ -z "$datastore_id" ]]; then errecho "ERROR: You must provide a data store ID with the -i parameter." usage return 1 fi local response response=$( aws medical-imaging get-datastore \ --datastore-id "$datastore_id" \ --output text \ --query "[ datastoreProperties.datastoreName, datastoreProperties.datastoreId, datastoreProperties.datastoreStatus, datastoreProperties.datastoreArn, datastoreProperties.createdAt, datastoreProperties.updatedAt]" ) error_code=${?} if [[ $error_code -ne 0 ]]; then aws_cli_error_log $error_code errecho "ERROR: AWS reports list-datastores operation failed.$response" return 1 fi echo "$response" return 0 }`- 
                    For API details, see [GetDatastore](https://docs.aws.amazon.com/goto/aws-cli/medical-imaging-2023-07-19/GetDatastore)in*AWS CLI Command Reference*.
 ###### NoteThere's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/aws-cli/bash-linux/medical-imaging#code-examples).
- 
                    

The following code example shows how to use `ListDatastores`.

- **AWS CLI with Bash script**
- 
            
                
                `############################################################################### # function errecho # # This function outputs everything sent to it to STDERR (standard error output). ############################################################################### function errecho() { printf "%s\n" "$*" 1>&2 } ############################################################################### # function imaging_list_datastores # # List the HealthImaging data stores in the account. # # Returns: # [[datastore_name, datastore_id, datastore_status]] # And: # 0 - If successful. # 1 - If it fails. ############################################################################### function imaging_list_datastores() { local option OPTARG # Required to use getopts command in a function. local error_code # bashsupport disable=BP5008 function usage() { echo "function imaging_list_datastores" echo "Lists the AWS HealthImaging data stores in the account." echo "" } # Retrieve the calling parameters. while getopts "h" option; do case "${option}" in h) usage return 0 ;; \?) echo "Invalid parameter" usage return 1 ;; esac done export OPTIND=1 local response response=$(aws medical-imaging list-datastores \ --output text \ --query "datastoreSummaries[*][datastoreName, datastoreId, datastoreStatus]") error_code=${?} if [[ $error_code -ne 0 ]]; then aws_cli_error_log $error_code errecho "ERROR: AWS reports list-datastores operation failed.$response" return 1 fi echo "$response" return 0 }`- 
                    For API details, see [ListDatastores](https://docs.aws.amazon.com/goto/aws-cli/medical-imaging-2023-07-19/ListDatastores)in*AWS CLI Command Reference*.
 ###### NoteThere's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/aws-cli/bash-linux/medical-imaging#code-examples).
-