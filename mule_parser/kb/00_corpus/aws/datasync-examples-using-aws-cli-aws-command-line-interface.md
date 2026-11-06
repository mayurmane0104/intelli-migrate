# DataSync examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_datasync_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_datasync_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with DataSync.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `update-location-azure-blob`.

- **AWS CLI**
- 
            
                    **To update your transfer location with a new agent**The following `update-location-object-storage`example updates your DataSync location for Microsoft Azure Blob Storage with a new agent.`aws datasync update-location-azure-blob \ --location-arn``arn:aws:datasync:us-west-2:123456789012:location/loc-abcdef01234567890`\ --agent-arns`arn:aws:datasync:us-west-2:123456789012:agent/agent-1234567890abcdef0`\ --sas-configuration '`{ \ "Token": "sas-token-for-azure-blob-storage-access" \ }`'This command produces no output. For more information, see [Replacing your agent](https://docs.aws.amazon.com/datasync/latest/userguide/replacing-agent.html)in the*AWS DataSync User Guide*.- 
                    For API details, see [UpdateLocationAzureBlob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/update-location-azure-blob.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-location-hdfs`.

- **AWS CLI**
- 
            
                    **To update your transfer location with a new agent**The following `update-location-hdfs`example updates your DataSync HDFS location with a new agent. You only need the`--kerberos-keytab`and`--kerberos-krb5-conf`options if your HDFS cluster uses Kerberos authentication.`aws datasync update-location-hdfs \ --location-arn``arn:aws:datasync:us-west-2:123456789012:location/loc-abcdef01234567890`\ --agent-arns`arn:aws:datasync:us-west-2:123456789012:agent/agent-1234567890abcdef0`\ --kerberos-keytab`file://hdfs.keytab`--kerberos-krb5-conf`file://krb5.conf`Contents of `hdfs.keytab`:`N/A. The content of this file is encrypted and not human readable.`Contents of `krb5.conf`:`[libdefaults] default_realm = EXAMPLE.COM dns_lookup_realm = false dns_lookup_kdc = false rdns = true ticket_lifetime = 24h forwardable = true udp_preference_limit = 1000000 default_tkt_enctypes = aes256-cts-hmac-sha1-96 aes128-cts-hmac-sha1-96 des3-cbc-sha1 default_tgs_enctypes = aes256-cts-hmac-sha1-96 aes128-cts-hmac-sha1-96 des3-cbc-sha1 permitted_enctypes = aes256-cts-hmac-sha1-96 aes128-cts-hmac-sha1-96 des3-cbc-sha1 [realms] EXAMPLE.COM = { kdc = kdc1.example.com admin_server = krbadmin.example.com default_domain = example.com } [domain_realm] .example.com = EXAMPLE.COM example.com = EXAMPLE.COM [logging] kdc = FILE:/var/log/krb5kdc.log admin_server = FILE:/var/log/kerberos/kadmin.log default = FILE:/var/log/krb5libs.log`This command produces no output. For more information, see [Replacing your agent](https://docs.aws.amazon.com/datasync/latest/userguide/replacing-agent.html)in the*AWS DataSync User Guide*.- 
                    For API details, see [UpdateLocationHdfs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/update-location-hdfs.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-location-nfs`.

- **AWS CLI**
- 
            
                    **To update your transfer location with a new agent**The following `update-location-nfs`example updates your DataSync NFS location with a new agent.`aws datasync update-location-nfs \ --location-arn``arn:aws:datasync:us-west-2:123456789012:location/loc-abcdef01234567890`\ --on-prem-config`AgentArns=arn:aws:datasync:us-west-2:123456789012:agent/agent-1234567890abcdef0`This command produces no output. For more information, see [Replacing your agent](https://docs.aws.amazon.com/datasync/latest/userguide/replacing-agent.html)in the*AWS DataSync User Guide*.- 
                    For API details, see [UpdateLocationNfs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/update-location-nfs.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-location-object-storage`.

- **AWS CLI**
- 
            
                    **To update your transfer location with a new agent**The following `update-location-object-storage`example updates your DataSync object storage location with a new agent.`aws datasync update-location-object-storage \ --location-arn``arn:aws:datasync:us-west-2:123456789012:location/loc-abcdef01234567890`\ --agent-arns`arn:aws:datasync:us-west-2:123456789012:agent/agent-1234567890abcdef0`\ --secret-key`secret-key-for-object-storage`This command produces no output. For more information, see [Replacing your agent](https://docs.aws.amazon.com/datasync/latest/userguide/replacing-agent.html)in the*AWS DataSync User Guide*.- 
                    For API details, see [UpdateLocationObjectStorage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/update-location-object-storage.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-location-smb`.

- **AWS CLI**
- 
            
                    **To update your transfer location with a new agent**The following `update-location-smb`example updates your DataSync SMB location with a new agent.`aws datasync update-location-smb \ --location-arn``arn:aws:datasync:us-west-2:123456789012:location/loc-abcdef01234567890`\ --agent-arns`arn:aws:datasync:us-west-2:123456789012:agent/agent-1234567890abcdef0`\ --password`smb-file-server-password`This command produces no output. For more information, see [Replacing your agent](https://docs.aws.amazon.com/datasync/latest/userguide/replacing-agent.html)in the*AWS DataSync User Guide*.- 
                    For API details, see [UpdateLocationSmb](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/update-location-smb.html)in*AWS CLI Command Reference*.
 
-