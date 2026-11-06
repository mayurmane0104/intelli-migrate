# Compute - Amazon SageMaker Unified Studio

**Source:** [https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/compute.html](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/compute.html)

---

On a project's **Compute** page in Amazon SageMaker Unified Studio, you can view compute
    information and add compute resources such as Amazon Redshift and Amazon EMR Serverless
    clusters to your project. Amazon SageMaker Unified Studio supports different kinds of compute resources:

- 
      **Data warehouse**: This includes Amazon Redshift Serverless workgroups and Amazon Redshift provisioned clusters. Workgroups are a collection of compute resources that you can use to run data warehousing queries and engineering notebooks without managing underlying infrastructure. Clusters are scalable compute environments that enable the processing and analysis of large datasets. For more information, see[Amazon Redshift compute connections in Amazon SageMaker Unified Studio](./compute-redshift.html).
- 
      **Data processing**: This includes connections to Amazon EMR on EC2 clusters, Amazon EMR on EKS virtual clusters, Amazon EMR Serverless applications, and Glue ETL computes. For more information, see the following links:
- 
      **HyperPod clusters**: In Amazon SageMaker Unified Studio, you can launch machine learning workloads on Amazon SageMaker AI HyperPod clusters. For more information, see[HyperPod clusters](./sagemaker-hyperpods.html).
- 
      **Spaces**: Spaces are used to manage the storage and resource needs of applications running on JupyterLab and Code Editor. You can create and manage multiple code spaces within your project. The experience differs by domain type. For more information, see[Code spaces in Amazon SageMaker Unified Studio](./ide-spaces.html).
- 
      **MLflow tracking servers**: MLflow tracking servers make it possible to use MLflow in Amazon SageMaker Unified Studio to create, manage, analyze, and compare machine learning experiments. For more information, see[Track experiments using MLflow](./sagemaker-experiments.xml.html).
- 
      **MLﬂow Apps**: MLﬂow Apps are the latest managed MLﬂow oﬀering that provides faster startup times, cross-account sharing, and integration with SageMaker AI features. For more information, see[Track experiments using MLflow](./sagemaker-experiments.xml.html)in Identity Center-based domains and[Track experiments using MLflow](./use-mlflow-experiments.html)in IAM-based domains.
- 
      **Workflow environments**: Use a workflow environment to share scheduled workflows with other project members. For more information, see[Create a workflow environment](./workflow-environments.html#create-workflow-environment).

###### Note

Adding a serverless or cluster compute connection adds the compute resource to the project space, so all project members can access it.