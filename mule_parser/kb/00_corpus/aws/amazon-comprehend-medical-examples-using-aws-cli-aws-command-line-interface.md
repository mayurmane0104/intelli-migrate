# Amazon Comprehend Medical examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_comprehendmedical_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_comprehendmedical_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Amazon Comprehend Medical.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `describe-entities-detection-v2-job`.

- **AWS CLI**
- 
            
                    **To describe an entities detection job**The following `describe-entities-detection-v2-job`example displays the properties associated with an asynchronous entity detection job.`aws comprehendmedical describe-entities-detection-v2-job \ --job-id``"ab9887877365fe70299089371c043b96"`Output: `{ "ComprehendMedicalAsyncJobProperties": { "JobId": "ab9887877365fe70299089371c043b96", "JobStatus": "COMPLETED", "SubmitTime": "2020-03-18T21:20:15.614000+00:00", "EndTime": "2020-03-18T21:27:07.350000+00:00", "ExpirationTime": "2020-07-16T21:20:15+00:00", "InputDataConfig": { "S3Bucket": "comp-med-input", "S3Key": "" }, "OutputDataConfig": { "S3Bucket": "comp-med-output", "S3Key": "867139942017-EntitiesDetection-ab9887877365fe70299089371c043b96/" }, "LanguageCode": "en", "DataAccessRoleArn": "arn:aws:iam::867139942017:role/ComprehendMedicalBatchProcessingRole", "ModelVersion": "DetectEntitiesModelV20190930" } }`For more information, see [Batch APIs](https://docs.aws.amazon.com/comprehend-medical/latest/dev/textanalysis-batchapi.html)in the*Amazon Comprehend Medical Developer Guide*.- 
                    For API details, see [DescribeEntitiesDetectionV2Job](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehendmedical/describe-entities-detection-v2-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-icd10-cm-inference-job`.

- **AWS CLI**
- 
            
                    **To describe an ICD-10-CM inference job**The following `describe-icd10-cm-inference-job`example describes the properties of the requested inference job with the specified job-id.`aws comprehendmedical describe-icd10-cm-inference-job \ --job-id``"5780034166536cdb52ffa3295a1b00a7"`Output: `{ "ComprehendMedicalAsyncJobProperties": { "JobId": "5780034166536cdb52ffa3295a1b00a7", "JobStatus": "COMPLETED", "SubmitTime": "2020-05-18T21:20:15.614000+00:00", "EndTime": "2020-05-18T21:27:07.350000+00:00", "ExpirationTime": "2020-09-16T21:20:15+00:00", "InputDataConfig": { "S3Bucket": "comp-med-input", "S3Key": "AKIAIOSFODNN7EXAMPLE" }, "OutputDataConfig": { "S3Bucket": "comp-med-output", "S3Key": "AKIAIOSFODNN7EXAMPLE" }, "LanguageCode": "en", "DataAccessRoleArn": "arn:aws:iam::867139942017:role/ComprehendMedicalBatchProcessingRole", "ModelVersion": "0.1.0" } }`For more information, see [Ontology linking batch analysis](https://docs.aws.amazon.com/comprehend-medical/latest/dev/ontologies-batchapi.html)in the*Amazon Comprehend Medical Developer Guide*.- 
                    For API details, see [DescribeIcd10CmInferenceJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehendmedical/describe-icd10-cm-inference-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-phi-detection-job`.

- **AWS CLI**
- 
            
                    **To describe a PHI detection job**The following `describe-phi-detection-job`example displays the properties associated with an asynchronous protected health information (PHI) detection job.`aws comprehendmedical describe-phi-detection-job \ --job-id``"4750034166536cdb52ffa3295a1b00a3"`Output: `{ "ComprehendMedicalAsyncJobProperties": { "JobId": "4750034166536cdb52ffa3295a1b00a3", "JobStatus": "COMPLETED", "SubmitTime": "2020-03-19T20:38:37.594000+00:00", "EndTime": "2020-03-19T20:45:07.894000+00:00", "ExpirationTime": "2020-07-17T20:38:37+00:00", "InputDataConfig": { "S3Bucket": "comp-med-input", "S3Key": "" }, "OutputDataConfig": { "S3Bucket": "comp-med-output", "S3Key": "867139942017-PHIDetection-4750034166536cdb52ffa3295a1b00a3/" }, "LanguageCode": "en", "DataAccessRoleArn": "arn:aws:iam::867139942017:role/ComprehendMedicalBatchProcessingRole", "ModelVersion": "PHIModelV20190903" } }`For more information, see [Batch APIs](https://docs.aws.amazon.com/comprehend-medical/latest/dev/textanalysis-batchapi.html)in the*Amazon Comprehend Medical Developer Guide*.- 
                    For API details, see [DescribePhiDetectionJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehendmedical/describe-phi-detection-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-rx-norm-inference-job`.

- **AWS CLI**
- 
            
                    **To describe an RxNorm inference job**The following `describe-rx-norm-inference-job`example describes the properties of the requested inference job with the specified job-id.`aws comprehendmedical describe-rx-norm-inference-job \ --job-id``"eg8199877365fc70299089371c043b96"`Output: `{ "ComprehendMedicalAsyncJobProperties": { "JobId": "g8199877365fc70299089371c043b96", "JobStatus": "COMPLETED", "SubmitTime": "2020-05-18T21:20:15.614000+00:00", "EndTime": "2020-05-18T21:27:07.350000+00:00", "ExpirationTime": "2020-09-16T21:20:15+00:00", "InputDataConfig": { "S3Bucket": "comp-med-input", "S3Key": "AKIAIOSFODNN7EXAMPLE" }, "OutputDataConfig": { "S3Bucket": "comp-med-output", "S3Key": "AKIAIOSFODNN7EXAMPLE" }, "LanguageCode": "en", "DataAccessRoleArn": "arn:aws:iam::867139942017:role/ComprehendMedicalBatchProcessingRole", "ModelVersion": "0.0.0" } }`For more information, see [Ontology linking batch analysis](https://docs.aws.amazon.com/comprehend-medical/latest/dev/ontologies-batchapi.html)in the*Amazon Comprehend Medical Developer Guide*.- 
                    For API details, see [DescribeRxNormInferenceJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehendmedical/describe-rx-norm-inference-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-snomedct-inference-job`.

- **AWS CLI**
- 
            
                    **To describe an SNOMED CT inference job**The following `describe-snomedct-inference-job`example describes the properties of the requested inference job with the specified job-id.`aws comprehendmedical describe-snomedct-inference-job \ --job-id``"2630034166536cdb52ffa3295a1b00a7"`Output: `{ "ComprehendMedicalAsyncJobProperties": { "JobId": "2630034166536cdb52ffa3295a1b00a7", "JobStatus": "COMPLETED", "SubmitTime": "2021-12-18T21:20:15.614000+00:00", "EndTime": "2021-12-18T21:27:07.350000+00:00", "ExpirationTime": "2022-05-16T21:20:15+00:00", "InputDataConfig": { "S3Bucket": "comp-med-input", "S3Key": "AKIAIOSFODNN7EXAMPLE" }, "OutputDataConfig": { "S3Bucket": "comp-med-output", "S3Key": "AKIAIOSFODNN7EXAMPLE" }, "LanguageCode": "en", "DataAccessRoleArn": "arn:aws:iam::867139942017:role/ComprehendMedicalBatchProcessingRole", "ModelVersion": "0.1.0" } }`For more information, see [Ontology linking batch analysis](https://docs.aws.amazon.com/comprehend-medical/latest/dev/ontologies-batchapi.html)in the*Amazon Comprehend Medical Developer Guide*.- 
                    For API details, see [DescribeSnomedctInferenceJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehendmedical/describe-snomedct-inference-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `detect-entities-v2`.

- **AWS CLI**
- 
            
                    **Example 1: To detect entities directly from text**The following `detect-entities-v2`example shows the detected entities and labels them according to type, directly from input text.`aws comprehendmedical detect-entities-v2 \ --text``"Sleeping trouble on present dosage of Clonidine. Severe rash on face and leg, slightly itchy."`Output: `{ "Id": 0, "BeginOffset": 38, "EndOffset": 47, "Score": 0.9942955374717712, "Text": "Clonidine", "Category": "MEDICATION", "Type": "GENERIC_NAME", "Traits": [] }`For more information, see [Detect Entities Version 2](https://docs.aws.amazon.com/comprehend/latest/dg/extracted-med-info-V2.html)in the*Amazon Comprehend Medical Developer Guide*.**Example 2: To detect entities from a file path**The following `detect-entities-v2`example shows the detected entities and labels them according to type from a file path.`aws comprehendmedical detect-entities-v2 \ --text``file://medical_entities.txt`Contents of `medical_entities.txt`:`{ "Sleeping trouble on present dosage of Clonidine. Severe rash on face and leg, slightly itchy." }`Output: `{ "Id": 0, "BeginOffset": 38, "EndOffset": 47, "Score": 0.9942955374717712, "Text": "Clonidine", "Category": "MEDICATION", "Type": "GENERIC_NAME", "Traits": [] }`For more information, see [Detect Entities Version 2](https://docs.aws.amazon.com/comprehend-medical/latest/dev/textanalysis-entitiesv2.html)in the*Amazon Comprehend Medical Developer Guide*.- 
                    For API details, see [DetectEntitiesV2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehendmedical/detect-entities-v2.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `detect-phi`.

- **AWS CLI**
- 
            
                    **Example 1: To detect protected health information (PHI) directly from text**The following `detect-phi`example displays the detected protected health information (PHI) entities directly from input text.`aws comprehendmedical detect-phi \ --text``"Patient Carlos Salazar presented with rash on his upper extremities and dry cough. He lives at 100 Main Street, Anytown, USA where he works from his home as a carpenter."`Output: `{ "Entities": [ { "Id": 0, "BeginOffset": 8, "EndOffset": 21, "Score": 0.9914507269859314, "Text": "Carlos Salazar", "Category": "PROTECTED_HEALTH_INFORMATION", "Type": "NAME", "Traits": [] }, { "Id": 1, "BeginOffset": 94, "EndOffset": 109, "Score": 0.871849775314331, "Text": "100 Main Street, Anytown, USA", "Category": "PROTECTED_HEALTH_INFORMATION", "Type": "ADDRESS", "Traits": [] }, { "Id": 2, "BeginOffset": 145, "EndOffset": 154, "Score": 0.8302185535430908, "Text": "carpenter", "Category": "PROTECTED_HEALTH_INFORMATION", "Type": "PROFESSION", "Traits": [] } ], "ModelVersion": "0.0.0" }`For more information, see [Detect PHI](https://docs.aws.amazon.com/comprehend-medical/latest/dev/textanalysis-phi.html)in the*Amazon Comprehend Medical Developer Guide*.**Example 2: To detect protect health information (PHI) directly from a file path**The following `detect-phi`example shows the detected protected health information (PHI) entities from a file path.`aws comprehendmedical detect-phi \ --text``file://phi.txt`Contents of `phi.txt`:`"Patient Carlos Salazar presented with a rash on his upper extremities and a dry cough. He lives at 100 Main Street, Anytown, USA, where he works from his home as a carpenter."`Output: `{ "Entities": [ { "Id": 0, "BeginOffset": 8, "EndOffset": 21, "Score": 0.9914507269859314, "Text": "Carlos Salazar", "Category": "PROTECTED_HEALTH_INFORMATION", "Type": "NAME", "Traits": [] }, { "Id": 1, "BeginOffset": 94, "EndOffset": 109, "Score": 0.871849775314331, "Text": "100 Main Street, Anytown, USA", "Category": "PROTECTED_HEALTH_INFORMATION", "Type": "ADDRESS", "Traits": [] }, { "Id": 2, "BeginOffset": 145, "EndOffset": 154, "Score": 0.8302185535430908, "Text": "carpenter", "Category": "PROTECTED_HEALTH_INFORMATION", "Type": "PROFESSION", "Traits": [] } ], "ModelVersion": "0.0.0" }`For more information, see [Detect PHI](https://docs.aws.amazon.com/comprehend/latest/dg/how-medical-phi.html)in the*Amazon Comprehend Medical Developer Guide*.- 
                    For API details, see [DetectPhi](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehendmedical/detect-phi.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `infer-icd10-cm`.

- **AWS CLI**
- 
            
                    **Example 1: To detect medical condition entities and link to the ICD-10-CM Ontology directly from text**The following `infer-icd10-cm`example labels the detected medical condition entities and links those entities with codes in the 2019 edition of the International Classification of Diseases Clinical Modification (ICD-10-CM).`aws comprehendmedical infer-icd10-cm \ --text``"The patient complains of abdominal pain, has a long-standing history of diabetes treated with Micronase daily."`Output: `{ "Entities": [ { "Id": 0, "Text": "abdominal pain", "Category": "MEDICAL_CONDITION", "Type": "DX_NAME", "Score": 0.9475538730621338, "BeginOffset": 28, "EndOffset": 42, "Attributes": [], "Traits": [ { "Name": "SYMPTOM", "Score": 0.6724207401275635 } ], "ICD10CMConcepts": [ { "Description": "Unspecified abdominal pain", "Code": "R10.9", "Score": 0.6904221177101135 }, { "Description": "Epigastric pain", "Code": "R10.13", "Score": 0.1364113688468933 }, { "Description": "Generalized abdominal pain", "Code": "R10.84", "Score": 0.12508003413677216 }, { "Description": "Left lower quadrant pain", "Code": "R10.32", "Score": 0.10063883662223816 }, { "Description": "Lower abdominal pain, unspecified", "Code": "R10.30", "Score": 0.09933677315711975 } ] }, { "Id": 1, "Text": "diabetes", "Category": "MEDICAL_CONDITION", "Type": "DX_NAME", "Score": 0.9899052977561951, "BeginOffset": 75, "EndOffset": 83, "Attributes": [], "Traits": [ { "Name": "DIAGNOSIS", "Score": 0.9258432388305664 } ], "ICD10CMConcepts": [ { "Description": "Type 2 diabetes mellitus without complications", "Code": "E11.9", "Score": 0.7158446311950684 }, { "Description": "Family history of diabetes mellitus", "Code": "Z83.3", "Score": 0.5704703330993652 }, { "Description": "Family history of other endocrine, nutritional and metabolic diseases", "Code": "Z83.49", "Score": 0.19856023788452148 }, { "Description": "Type 1 diabetes mellitus with ketoacidosis without coma", "Code": "E10.10", "Score": 0.13285516202449799 }, { "Description": "Type 2 diabetes mellitus with hyperglycemia", "Code": "E11.65", "Score": 0.0993388369679451 } ] } ], "ModelVersion": "0.1.0" }`For more information, see [Infer ICD10-CM](https://docs.aws.amazon.com/comprehend/latest/dg/ontology-linking-icd10.html)in the*Amazon Comprehend Medical Developer Guide*.**Example 2: To detect medical condition entities and link to the ICD-10-CM Ontology from a file pathway**The following `infer-icd-10-cm`example labels the detected medical condition entities and links those entities with codes in the 2019 edition of the International Classification of Diseases Clinical Modification (ICD-10-CM).`aws comprehendmedical infer-icd10-cm \ --text``file://icd10cm.txt`Contents of `icd10cm.txt`:`{ "The patient complains of abdominal pain, has a long-standing history of diabetes treated with Micronase daily." }`Output: `{ "Entities": [ { "Id": 0, "Text": "abdominal pain", "Category": "MEDICAL_CONDITION", "Type": "DX_NAME", "Score": 0.9475538730621338, "BeginOffset": 28, "EndOffset": 42, "Attributes": [], "Traits": [ { "Name": "SYMPTOM", "Score": 0.6724207401275635 } ], "ICD10CMConcepts": [ { "Description": "Unspecified abdominal pain", "Code": "R10.9", "Score": 0.6904221177101135 }, { "Description": "Epigastric pain", "Code": "R10.13", "Score": 0.1364113688468933 }, { "Description": "Generalized abdominal pain", "Code": "R10.84", "Score": 0.12508003413677216 }, { "Description": "Left lower quadrant pain", "Code": "R10.32", "Score": 0.10063883662223816 }, { "Description": "Lower abdominal pain, unspecified", "Code": "R10.30", "Score": 0.09933677315711975 } ] }, { "Id": 1, "Text": "diabetes", "Category": "MEDICAL_CONDITION", "Type": "DX_NAME", "Score": 0.9899052977561951, "BeginOffset": 75, "EndOffset": 83, "Attributes": [], "Traits": [ { "Name": "DIAGNOSIS", "Score": 0.9258432388305664 } ], "ICD10CMConcepts": [ { "Description": "Type 2 diabetes mellitus without complications", "Code": "E11.9", "Score": 0.7158446311950684 }, { "Description": "Family history of diabetes mellitus", "Code": "Z83.3", "Score": 0.5704703330993652 }, { "Description": "Family history of other endocrine, nutritional and metabolic diseases", "Code": "Z83.49", "Score": 0.19856023788452148 }, { "Description": "Type 1 diabetes mellitus with ketoacidosis without coma", "Code": "E10.10", "Score": 0.13285516202449799 }, { "Description": "Type 2 diabetes mellitus with hyperglycemia", "Code": "E11.65", "Score": 0.0993388369679451 } ] } ], "ModelVersion": "0.1.0" }`For more information, see [Infer-ICD10-CM](https://docs.aws.amazon.com/comprehend-medical/latest/dev/ontology-icd10.html)in the*Amazon Comprehend Medical Developer Guide*.- 
                    For API details, see [InferIcd10Cm](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehendmedical/infer-icd10-cm.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `infer-rx-norm`.

- **AWS CLI**
- 
            
                    **Example 1: To detect medication entities and link to RxNorm directly from text**The following `infer-rx-norm`example shows and labels the detected medication entities and links those entities to concept identifiers (RxCUI) from the National Library of Medicine RxNorm database.`aws comprehendmedical infer-rx-norm \ --text``"Patient reports taking Levothyroxine 125 micrograms p.o. once daily, but denies taking Synthroid."`Output: `{ "Entities": [ { "Id": 0, "Text": "Levothyroxine", "Category": "MEDICATION", "Type": "GENERIC_NAME", "Score": 0.9996285438537598, "BeginOffset": 23, "EndOffset": 36, "Attributes": [ { "Type": "DOSAGE", "Score": 0.9892290830612183, "RelationshipScore": 0.9997978806495667, "Id": 1, "BeginOffset": 37, "EndOffset": 51, "Text": "125 micrograms", "Traits": [] }, { "Type": "ROUTE_OR_MODE", "Score": 0.9988924860954285, "RelationshipScore": 0.998291552066803, "Id": 2, "BeginOffset": 52, "EndOffset": 56, "Text": "p.o.", "Traits": [] }, { "Type": "FREQUENCY", "Score": 0.9953463673591614, "RelationshipScore": 0.9999889135360718, "Id": 3, "BeginOffset": 57, "EndOffset": 67, "Text": "once daily", "Traits": [] } ], "Traits": [], "RxNormConcepts": [ { "Description": "Levothyroxine Sodium 0.125 MG Oral Tablet", "Code": "966224", "Score": 0.9912070631980896 }, { "Description": "Levothyroxine Sodium 0.125 MG Oral Capsule", "Code": "966405", "Score": 0.8698278665542603 }, { "Description": "Levothyroxine Sodium 0.125 MG Oral Tablet [Synthroid]", "Code": "966191", "Score": 0.7448257803916931 }, { "Description": "levothyroxine", "Code": "10582", "Score": 0.7050482630729675 }, { "Description": "Levothyroxine Sodium 0.125 MG Oral Tablet [Levoxyl]", "Code": "966190", "Score": 0.6921631693840027 } ] }, { "Id": 4, "Text": "Synthroid", "Category": "MEDICATION", "Type": "BRAND_NAME", "Score": 0.9946461319923401, "BeginOffset": 86, "EndOffset": 95, "Attributes": [], "Traits": [ { "Name": "NEGATION", "Score": 0.5167351961135864 } ], "RxNormConcepts": [ { "Description": "Synthroid", "Code": "224920", "Score": 0.9462039470672607 }, { "Description": "Levothyroxine Sodium 0.088 MG Oral Tablet [Synthroid]", "Code": "966282", "Score": 0.8309829235076904 }, { "Description": "Levothyroxine Sodium 0.125 MG Oral Tablet [Synthroid]", "Code": "966191", "Score": 0.4945160448551178 }, { "Description": "Levothyroxine Sodium 0.05 MG Oral Tablet [Synthroid]", "Code": "966247", "Score": 0.3674522042274475 }, { "Description": "Levothyroxine Sodium 0.025 MG Oral Tablet [Synthroid]", "Code": "966158", "Score": 0.2588822841644287 } ] } ], "ModelVersion": "0.0.0" }`For more information, see [Infer RxNorm](https://docs.aws.amazon.com/comprehend/latest/dg/ontology-linking-rxnorm.html)in the*Amazon Comprehend Medical Developer Guide*.**Example 2: To detect medication entities and link to RxNorm from a file path.**The following `infer-rx-norm`example shows and labels the detected medication entities and links those entities to concept identifiers (RxCUI) from the National Library of Medicine RxNorm database.`aws comprehendmedical infer-rx-norm \ --text``file://rxnorm.txt`Contents of `rxnorm.txt`:`{ "Patient reports taking Levothyroxine 125 micrograms p.o. once daily, but denies taking Synthroid." }`Output: `{ "Entities": [ { "Id": 0, "Text": "Levothyroxine", "Category": "MEDICATION", "Type": "GENERIC_NAME", "Score": 0.9996285438537598, "BeginOffset": 23, "EndOffset": 36, "Attributes": [ { "Type": "DOSAGE", "Score": 0.9892290830612183, "RelationshipScore": 0.9997978806495667, "Id": 1, "BeginOffset": 37, "EndOffset": 51, "Text": "125 micrograms", "Traits": [] }, { "Type": "ROUTE_OR_MODE", "Score": 0.9988924860954285, "RelationshipScore": 0.998291552066803, "Id": 2, "BeginOffset": 52, "EndOffset": 56, "Text": "p.o.", "Traits": [] }, { "Type": "FREQUENCY", "Score": 0.9953463673591614, "RelationshipScore": 0.9999889135360718, "Id": 3, "BeginOffset": 57, "EndOffset": 67, "Text": "once daily", "Traits": [] } ], "Traits": [], "RxNormConcepts": [ { "Description": "Levothyroxine Sodium 0.125 MG Oral Tablet", "Code": "966224", "Score": 0.9912070631980896 }, { "Description": "Levothyroxine Sodium 0.125 MG Oral Capsule", "Code": "966405", "Score": 0.8698278665542603 }, { "Description": "Levothyroxine Sodium 0.125 MG Oral Tablet [Synthroid]", "Code": "966191", "Score": 0.7448257803916931 }, { "Description": "levothyroxine", "Code": "10582", "Score": 0.7050482630729675 }, { "Description": "Levothyroxine Sodium 0.125 MG Oral Tablet [Levoxyl]", "Code": "966190", "Score": 0.6921631693840027 } ] }, { "Id": 4, "Text": "Synthroid", "Category": "MEDICATION", "Type": "BRAND_NAME", "Score": 0.9946461319923401, "BeginOffset": 86, "EndOffset": 95, "Attributes": [], "Traits": [ { "Name": "NEGATION", "Score": 0.5167351961135864 } ], "RxNormConcepts": [ { "Description": "Synthroid", "Code": "224920", "Score": 0.9462039470672607 }, { "Description": "Levothyroxine Sodium 0.088 MG Oral Tablet [Synthroid]", "Code": "966282", "Score": 0.8309829235076904 }, { "Description": "Levothyroxine Sodium 0.125 MG Oral Tablet [Synthroid]", "Code": "966191", "Score": 0.4945160448551178 }, { "Description": "Levothyroxine Sodium 0.05 MG Oral Tablet [Synthroid]", "Code": "966247", "Score": 0.3674522042274475 }, { "Description": "Levothyroxine Sodium 0.025 MG Oral Tablet [Synthroid]", "Code": "966158", "Score": 0.2588822841644287 } ] } ], "ModelVersion": "0.0.0" }`For more information, see [Infer RxNorm](https://docs.aws.amazon.com/comprehend-medical/latest/dev/ontology-RxNorm.html)in the*Amazon Comprehend Medical Developer Guide*.- 
                    For API details, see [InferRxNorm](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehendmedical/infer-rx-norm.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `infer-snomedct`.

- **AWS CLI**
- 
            
                    **Example: To detect entities and link to the SNOMED CT Ontology directly from text**The following `infer-snomedct`example shows how to detect medical entities and link them to concepts from the 2021-03 version of the Systematized Nomenclature of Medicine, Clinical Terms (SNOMED CT).`aws comprehendmedical infer-snomedct \ --text``"The patient complains of abdominal pain, has a long-standing history of diabetes treated with Micronase daily."`Output: `{ "Entities": [ { "Id": 3, "BeginOffset": 26, "EndOffset": 40, "Score": 0.9598260521888733, "Text": "abdominal pain", "Category": "MEDICAL_CONDITION", "Type": "DX_NAME", "Traits": [ { "Name": "SYMPTOM", "Score": 0.6819021701812744 } ] }, { "Id": 4, "BeginOffset": 73, "EndOffset": 81, "Score": 0.9905840158462524, "Text": "diabetes", "Category": "MEDICAL_CONDITION", "Type": "DX_NAME", "Traits": [ { "Name": "DIAGNOSIS", "Score": 0.9255214333534241 } ] }, { "Id": 1, "BeginOffset": 95, "EndOffset": 104, "Score": 0.6371926665306091, "Text": "Micronase", "Category": "MEDICATION", "Type": "BRAND_NAME", "Traits": [], "Attributes": [ { "Type": "FREQUENCY", "Score": 0.9761165380477905, "RelationshipScore": 0.9984188079833984, "RelationshipType": "FREQUENCY", "Id": 2, "BeginOffset": 105, "EndOffset": 110, "Text": "daily", "Category": "MEDICATION", "Traits": [] } ] } ], "UnmappedAttributes": [], "ModelVersion": "1.0.0" }`For more information, see [InferSNOMEDCT](https://docs.aws.amazon.com/comprehend-medical/latest/dev/ontology-linking-snomed.html)in the*Amazon Comprehend Medical Developer Guide*.- 
                    For API details, see [InferSnomedct](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehendmedical/infer-snomedct.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-entities-detection-v2-jobs`.

- **AWS CLI**
- 
            
                    **To list entities detection jobs**The following `list-entities-detection-v2-jobs`example lists current asynchronous detection jobs.`aws comprehendmedical list-entities-detection-v2-jobs`Output: `{ "ComprehendMedicalAsyncJobPropertiesList": [ { "JobId": "ab9887877365fe70299089371c043b96", "JobStatus": "COMPLETED", "SubmitTime": "2020-03-19T20:38:37.594000+00:00", "EndTime": "2020-03-19T20:45:07.894000+00:00", "ExpirationTime": "2020-07-17T20:38:37+00:00", "InputDataConfig": { "S3Bucket": "comp-med-input", "S3Key": "" }, "OutputDataConfig": { "S3Bucket": "comp-med-output", "S3Key": "867139942017-EntitiesDetection-ab9887877365fe70299089371c043b96/" }, "LanguageCode": "en", "DataAccessRoleArn": "arn:aws:iam::867139942017:role/ComprehendMedicalBatchProcessingRole", "ModelVersion": "DetectEntitiesModelV20190930" } ] }`For more information, see [Batch APIs](https://docs.aws.amazon.com/comprehend-medical/latest/dev/textanalysis-batchapi.html)in the*Amazon Comprehend Medical Developer Guide*.- 
                    For API details, see [ListEntitiesDetectionV2Jobs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehendmedical/list-entities-detection-v2-jobs.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-icd10-cm-inference-jobs`.

- **AWS CLI**
- 
            
                    **To list all current ICD-10-CM inference jobs**The following example shows how the `list-icd10-cm-inference-jobs`operation returns a list of current asynchronous ICD-10-CM batch inference jobs.`aws comprehendmedical list-icd10-cm-inference-jobs`Output: `{ "ComprehendMedicalAsyncJobPropertiesList": [ { "JobId": "5780034166536cdb52ffa3295a1b00a7", "JobStatus": "COMPLETED", "SubmitTime": "2020-05-19T20:38:37.594000+00:00", "EndTime": "2020-05-19T20:45:07.894000+00:00", "ExpirationTime": "2020-09-17T20:38:37+00:00", "InputDataConfig": { "S3Bucket": "comp-med-input", "S3Key": "AKIAIOSFODNN7EXAMPLE" }, "OutputDataConfig": { "S3Bucket": "comp-med-output", "S3Key": "AKIAIOSFODNN7EXAMPLE" }, "LanguageCode": "en", "DataAccessRoleArn": "arn:aws:iam::867139942017:role/ComprehendMedicalBatchProcessingRole", "ModelVersion": "0.1.0" } ] }`For more information, see [Ontology linking batch analysis](https://docs.aws.amazon.com/comprehend-medical/latest/dev/ontologies-batchapi.html)in the*Amazon Comprehend Medical Developer Guide*.- 
                    For API details, see [ListIcd10CmInferenceJobs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehendmedical/list-icd10-cm-inference-jobs.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-phi-detection-jobs`.

- **AWS CLI**
- 
            
                    **To list protected health information (PHI) detection jobs**The following `list-phi-detection-jobs`example lists current protected health information (PHI) detection jobs`aws comprehendmedical list-phi-detection-jobs`Output: `{ "ComprehendMedicalAsyncJobPropertiesList": [ { "JobId": "4750034166536cdb52ffa3295a1b00a3", "JobStatus": "COMPLETED", "SubmitTime": "2020-03-19T20:38:37.594000+00:00", "EndTime": "2020-03-19T20:45:07.894000+00:00", "ExpirationTime": "2020-07-17T20:38:37+00:00", "InputDataConfig": { "S3Bucket": "comp-med-input", "S3Key": "" }, "OutputDataConfig": { "S3Bucket": "comp-med-output", "S3Key": "867139942017-PHIDetection-4750034166536cdb52ffa3295a1b00a3/" }, "LanguageCode": "en", "DataAccessRoleArn": "arn:aws:iam::867139942017:role/ComprehendMedicalBatchProcessingRole", "ModelVersion": "PHIModelV20190903" } ] }`For more information, see [Batch APIs](https://docs.aws.amazon.com/comprehend-medical/latest/dev/textanalysis-batchapi.html)in the*Amazon Comprehend Medical Developer Guide*.- 
                    For API details, see [ListPhiDetectionJobs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehendmedical/list-phi-detection-jobs.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-rx-norm-inference-jobs`.

- **AWS CLI**
- 
            
                    **To list all current Rx-Norm inference jobs**The following example shows how `list-rx-norm-inference-jobs`returns a list of current asynchronous Rx-Norm batch inference jobs.`aws comprehendmedical list-rx-norm-inference-jobs`Output: `{ "ComprehendMedicalAsyncJobPropertiesList": [ { "JobId": "4980034166536cfb52gga3295a1b00a3", "JobStatus": "COMPLETED", "SubmitTime": "2020-05-19T20:38:37.594000+00:00", "EndTime": "2020-05-19T20:45:07.894000+00:00", "ExpirationTime": "2020-09-17T20:38:37+00:00", "InputDataConfig": { "S3Bucket": "comp-med-input", "S3Key": "AKIAIOSFODNN7EXAMPLE" }, "OutputDataConfig": { "S3Bucket": "comp-med-output", "S3Key": "AKIAIOSFODNN7EXAMPLE" }, "LanguageCode": "en", "DataAccessRoleArn": "arn:aws:iam::867139942017:role/ComprehendMedicalBatchProcessingRole", "ModelVersion": "0.0.0" } ] }`For more information, see [Ontology linking batch analysis](https://docs.aws.amazon.com/comprehend-medical/latest/dev/ontologies-batchapi.html)in the*Amazon Comprehend Medical Developer Guide*.- 
                    For API details, see [ListRxNormInferenceJobs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehendmedical/list-rx-norm-inference-jobs.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-snomedct-inference-jobs`.

- **AWS CLI**
- 
            
                    **To list all SNOMED CT inference jobs**The following example shows how the `list-snomedct-inference-jobs`operation returns a list of current asynchronous SNOMED CT batch inference jobs.`aws comprehendmedical list-snomedct-inference-jobs`Output: `{ "ComprehendMedicalAsyncJobPropertiesList": [ { "JobId": "5780034166536cdb52ffa3295a1b00a7", "JobStatus": "COMPLETED", "SubmitTime": "2020-05-19T20:38:37.594000+00:00", "EndTime": "2020-05-19T20:45:07.894000+00:00", "ExpirationTime": "2020-09-17T20:38:37+00:00", "InputDataConfig": { "S3Bucket": "comp-med-input", "S3Key": "AKIAIOSFODNN7EXAMPLE" }, "OutputDataConfig": { "S3Bucket": "comp-med-output", "S3Key": "AKIAIOSFODNN7EXAMPLE" }, "LanguageCode": "en", "DataAccessRoleArn": "arn:aws:iam::867139942017:role/ComprehendMedicalBatchProcessingRole", "ModelVersion": "0.1.0" } ] }`For more information, see [Ontology linking batch analysis](https://docs.aws.amazon.com/comprehend-medical/latest/dev/ontologies-batchapi.html)in the*Amazon Comprehend Medical Developer Guide*.- 
                    For API details, see [ListSnomedctInferenceJobs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehendmedical/list-snomedct-inference-jobs.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-entities-detection-v2-job`.

- **AWS CLI**
- 
            
                    **To start an entities detection job**The following `start-entities-detection-v2-job`example starts an asynchronous entity detection job.`aws comprehendmedical start-entities-detection-v2-job \ --input-data-config``"S3Bucket=comp-med-input"`\ --output-data-config`"S3Bucket=comp-med-output"`\ --data-access-role-arn`arn:aws:iam::867139942017:role/ComprehendMedicalBatchProcessingRole`\ --language-code`en`Output: `{ "JobId": "ab9887877365fe70299089371c043b96" }`For more information, see [Batch APIs](https://docs.aws.amazon.com/comprehend-medical/latest/dev/textanalysis-batchapi.html)in the*Amazon Comprehend Medical Developer Guide*.- 
                    For API details, see [StartEntitiesDetectionV2Job](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehendmedical/start-entities-detection-v2-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-icd10-cm-inference-job`.

- **AWS CLI**
- 
            
                    **To start an ICD-10-CM inference job**The following `start-icd10-cm-inference-job`example starts an ICD-10-CM inference batch analysis job.`aws comprehendmedical start-icd10-cm-inference-job \ --input-data-config``"S3Bucket=comp-med-input"`\ --output-data-config`"S3Bucket=comp-med-output"`\ --data-access-role-arn`arn:aws:iam::867139942017:role/ComprehendMedicalBatchProcessingRole`\ --language-code`en`Output: `{ "JobId": "ef7289877365fc70299089371c043b96" }`For more information, see [Ontology linking batch analysis](https://docs.aws.amazon.com/comprehend-medical/latest/dev/ontologies-batchapi.html)in the*Amazon Comprehend Medical Developer Guide*.- 
                    For API details, see [StartIcd10CmInferenceJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehendmedical/start-icd10-cm-inference-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-phi-detection-job`.

- **AWS CLI**
- 
            
                    **To start a PHI detection job**The following `start-phi-detection-job`example starts an asynchronous PHI entity detection job.`aws comprehendmedical start-phi-detection-job \ --input-data-config``"S3Bucket=comp-med-input"`\ --output-data-config`"S3Bucket=comp-med-output"`\ --data-access-role-arn`arn:aws:iam::867139942017:role/ComprehendMedicalBatchProcessingRole`\ --language-code`en`Output: `{ "JobId": "ab9887877365fe70299089371c043b96" }`For more information, see [Batch APIs](https://docs.aws.amazon.com/comprehend-medical/latest/dev/textanalysis-batchapi.html)in the*Amazon Comprehend Medical Developer Guide*.- 
                    For API details, see [StartPhiDetectionJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehendmedical/start-phi-detection-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-rx-norm-inference-job`.

- **AWS CLI**
- 
            
                    **To start an RxNorm inference job**The following `start-rx-norm-inference-job`example starts an RxNorm inference batch analysis job.`aws comprehendmedical start-rx-norm-inference-job \ --input-data-config``"S3Bucket=comp-med-input"`\ --output-data-config`"S3Bucket=comp-med-output"`\ --data-access-role-arn`arn:aws:iam::867139942017:role/ComprehendMedicalBatchProcessingRole`\ --language-code`en`Output: `{ "JobId": "eg8199877365fc70299089371c043b96" }`For more information, see [Ontology linking batch analysis](https://docs.aws.amazon.com/comprehend-medical/latest/dev/ontologies-batchapi.html)in the*Amazon Comprehend Medical Developer Guide*.- 
                    For API details, see [StartRxNormInferenceJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehendmedical/start-rx-norm-inference-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-snomedct-inference-job`.

- **AWS CLI**
- 
            
                    **To start an SNOMED CT inference job**The following `start-snomedct-inference-job`example starts a SNOMED CT inference batch analysis job.`aws comprehendmedical start-snomedct-inference-job \ --input-data-config``"S3Bucket=comp-med-input"`\ --output-data-config`"S3Bucket=comp-med-output"`\ --data-access-role-arn`arn:aws:iam::867139942017:role/ComprehendMedicalBatchProcessingRole`\ --language-code`en`Output: `{ "JobId": "dg7289877365fc70299089371c043b96" }`For more information, see [Ontology linking batch analysis](https://docs.aws.amazon.com/comprehend-medical/latest/dev/ontologies-batchapi.html)in the*Amazon Comprehend Medical Developer Guide*.- 
                    For API details, see [StartSnomedctInferenceJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehendmedical/start-snomedct-inference-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `stop-entities-detection-v2-job`.

- **AWS CLI**
- 
            
                    **To stop an entity detection job**The following `stop-entities-detection-v2-job`example stops an asynchronous entity detection job.`aws comprehendmedical stop-entities-detection-v2-job \ --job-id``"ab9887877365fe70299089371c043b96"`Output: `{ "JobId": "ab9887877365fe70299089371c043b96" }`For more information, see [Batch APIs](https://docs.aws.amazon.com/comprehend-medical/latest/dev/textanalysis-batchapi.html)in the*Amazon Comprehend Medical Developer Guide*.- 
                    For API details, see [StopEntitiesDetectionV2Job](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehendmedical/stop-entities-detection-v2-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `stop-icd10-cm-inference-job`.

- **AWS CLI**
- 
            
                    **To stop an ICD-10-CM inference job**The following `stop-icd10-cm-inference-job`example stops an ICD-10-CM inference batch analysis job.`aws comprehendmedical stop-icd10-cm-inference-job \ --job-id``"4750034166536cdb52ffa3295a1b00a3"`Output: `{ "JobId": "ef7289877365fc70299089371c043b96", }`For more information, see [Ontology linking batch analysis](https://docs.aws.amazon.com/comprehend-medical/latest/dev/ontologies-batchapi.html)in the*Amazon Comprehend Medical Developer Guide*.- 
                    For API details, see [StopIcd10CmInferenceJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehendmedical/stop-icd10-cm-inference-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `stop-phi-detection-job`.

- **AWS CLI**
- 
            
                    **To stop a protected health information (PHI) detection job**The following `stop-phi-detection-job`example stops an asynchronous protected health information (PHI) detection job.`aws comprehendmedical stop-phi-detection-job \ --job-id``"4750034166536cdb52ffa3295a1b00a3"`Output: `{ "JobId": "ab9887877365fe70299089371c043b96" }`For more information, see [Batch APIs](https://docs.aws.amazon.com/comprehend-medical/latest/dev/textanalysis-batchapi.html)in the*Amazon Comprehend Medical Developer Guide*.- 
                    For API details, see [StopPhiDetectionJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehendmedical/stop-phi-detection-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `stop-rx-norm-inference-job`.

- **AWS CLI**
- 
            
                    **To stop an RxNorm inference job**The following `stop-rx-norm-inference-job`example stops an ICD-10-CM inference batch analysis job.`aws comprehendmedical stop-rx-norm-inference-job \ --job-id``"eg8199877365fc70299089371c043b96"`Output: `{ "JobId": "eg8199877365fc70299089371c043b96", }`For more information, see [Ontology linking batch analysis](https://docs.aws.amazon.com/comprehend-medical/latest/dev/ontologies-batchapi.html)in the*Amazon Comprehend Medical Developer Guide*.- 
                    For API details, see [StopRxNormInferenceJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehendmedical/stop-rx-norm-inference-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `stop-snomedct-inference-job`.

- **AWS CLI**
- 
            
                    **To stop a SNOMED CT inference job**The following `stop-snomedct-inference-job`example stops a SNOMED CT inference batch analysis job.`aws comprehendmedical stop-snomedct-inference-job \ --job-id``"8750034166436cdb52ffa3295a1b00a1"`Output: `{ "JobId": "8750034166436cdb52ffa3295a1b00a1", }`For more information, see [Ontology linking batch analysis](https://docs.aws.amazon.com/comprehend-medical/latest/dev/ontologies-batchapi.html)in the*Amazon Comprehend Medical Developer Guide*.- 
                    For API details, see [StopSnomedctInferenceJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehendmedical/stop-snomedct-inference-job.html)in*AWS CLI Command Reference*.
 
-