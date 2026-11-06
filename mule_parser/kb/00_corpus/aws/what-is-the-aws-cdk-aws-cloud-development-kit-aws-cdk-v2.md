# What is the AWS CDK? - AWS Cloud Development Kit (AWS CDK) v2

**Source:** [https://docs.aws.amazon.com/cdk/v2/guide/index.html](https://docs.aws.amazon.com/cdk/v2/guide/index.html)

---

This is the AWS CDK v2 Developer Guide. The older CDK v1 entered maintenance on June 1, 2022 and ended support on June 1, 2023.

The AWS Cloud Development Kit (AWS CDK) is an open-source software development framework for defining cloud infrastructure in code and provisioning it through AWS CloudFormation.

The AWS CDK consists of two primary parts:

- 
         [AWS CDK Construct Library](./constructs.html)
- 
         AWS CDK Toolkit - Tools that you can use to manage and interact with your CDK apps, such as performing synthesis or deployment. The CDK Toolkit consists of a command line tool ( [CDK CLI](./ref-cli-cmd.html)) and a programmatic library ([CDK Toolkit Library](./toolkit-library.html)).

The AWS CDK supports  TypeScript,  JavaScript,  Python,  Java,  C#/.Net, and  Go. You can use any of these supported programming languages to define reusable cloud components known as  [constructs](./constructs.html). You compose these together into [stacks](./stacks.html) and [apps](./apps.html). Then, you deploy your CDK applications through AWS CloudFormation to provision or update your resources.

![CDK app and process overview](/images/cdk/v2/guide/images/AppStacks.png) 

       
       
   ## Benefits of the AWS CDK

      Use the AWS CDK to develop reliable, scalable, cost-effective applications in the cloud with the considerable expressive power of a programming language. This approach yields many benefits, including:

- 
               **Develop and manage your infrastructure as code (IaC)**
- 
               Practice *infrastructure as code*to create, deploy, and maintain infrastructure in a programmatic, descriptive, and declarative way. With IaC, you treat infrastructure the same way developers treat code. This results in a scalable and structured approach to managing infrastructure. To learn more about IaC, see[Infrastructure as code](https://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/infrastructure-as-code.html)in the*Introduction to DevOps on AWS Whitepaper*.With the AWS CDK, you can put your infrastructure, application code, and configuration all in one place, ensuring that you have a complete, cloud-deployable system at every milestone. Employ software engineering best practices such as code reviews, unit tests, and source control to make your infrastructure more robust. 

- 
               **Define your cloud infrastructure using general-purpose programming languages**
- 
               With the AWS CDK, you can use any of the following programming languages to define your cloud infrastructure: TypeScript, JavaScript, Python, Java, C#/.Net, and Go. Choose your preferred language and use programming elements like parameters, conditionals, loops, composition, and inheritance to define the desired outcome of your infrastructure. Use the same programming language to define your infrastructure and your application logic. Receive the benefits of developing infrastructure in your preferred IDE (Integrated Development Environment), such as syntax highlighting and intelligent code completion. ![Code snippet showing CDK setup for ECS cluster with VPC and Fargate service configuration.](/images/cdk/v2/guide/images/CodeCompletion.png)  

- 
               **Deploy infrastructure through AWS CloudFormation**
- 
               AWS CDK integrates with AWS CloudFormation to deploy and provision your infrastructure on AWS. AWS CloudFormation is a managed AWS service that offers extensive support of resource and property configurations for provisioning services on AWS. With AWS CloudFormation, you can perform infrastructure deployments predictably and repeatedly, with rollback on error. If you are already familiar with AWS CloudFormation, you don’t have to learn a new IaC management service when getting started with the AWS CDK. 

- 
               **Get started developing your application quickly with constructs**
- 
               Develop faster by using and sharing reusable components called constructs. Use low-level constructs to define individual AWS CloudFormation resources and their properties. Use high-level constructs to quickly define larger components of your application, with sensible, secure defaults for your AWS resources, defining more infrastructure with less code. Create your own constructs that are customized for your unique use cases and share them across your organization or even with the public. 

## Example of the AWS CDK

      The following is an example of using the AWS CDK Constructs Library to create an Amazon Elastic Container Service (Amazon ECS) service with AWS Fargate launch type. For more details of this example, see  [Example: Create an AWS Fargate service using the AWS CDK](./ecs-example.html).

###### Example

```
export class MyEcsConstructStack extends Stack {
  constructor(scope: App, id: string, props?: StackProps) {
    super(scope, id, props);
    const vpc = new ec2.Vpc(this, "MyVpc", {
      maxAzs: 3 // Default is all AZs in region
    });
    const cluster = new ecs.Cluster(this, "MyCluster", {
      vpc: vpc
    });
    // Create a load-balanced Fargate service and make it public
    new ecs_patterns.ApplicationLoadBalancedFargateService(this, "MyFargateService", {
      cluster: cluster, // Required
      cpu: 512, // Default is 256
      desiredCount: 6, // Default is 1
      taskImageOptions: { image: ecs.ContainerImage.fromRegistry("amazon/amazon-ecs-sample") },
      memoryLimitMiB: 2048, // Default is 512
      publicLoadBalancer: true // Default is false
    });
  }
}
```
This class produces an AWS CloudFormation template of more than 500 lines. Deploying the AWS CDK app produces more than 50 resources of the following types:

## AWS CDK features

       
         ### The AWS CDK GitHub repository

For the official AWS CDK GitHub repository, see [aws-cdk](https://github.com/aws/aws-cdk). Here, you can submit 

[issues](https://github.com/aws/aws-cdk/issues), view our

[license](https://github.com/aws/aws-cdk/blob/main/LICENSE), track

[releases](https://github.com/aws/aws-cdk/releases), and more.

Because the AWS CDK is open-source, the team encourages you to contribute to make it an even better tool. For details, see [Contributing to the AWS Cloud Development Kit (AWS CDK)](https://github.com/aws/aws-cdk/blob/main/CONTRIBUTING.md).

### The AWS CDK API reference

The AWS CDK Construct Library provides APIs to define your CDK application and add CDK constructs to the application. For more information, see the [AWS CDK API Reference](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-construct-library.html).

### The Construct Programming Model

The Construct Programming Model (CPM) extends the concepts behind the AWS CDK into additional domains. Other tools using the CPM include:

- 
               [CDK for Terraform](https://www.terraform.io/docs/cdktf/index.html)(CDKtf)
- 
               [CDK for Kubernetes](https://cdk8s.io/)(CDK8s)
- 
               [Projen](https://github.com/projen/projen), for building project configurations

### The Construct Hub

The [Construct Hub](https://constructs.dev/) is an online registry where you can find, publish, and share open-source AWS CDK libraries.

## Next steps

      To get started with using the AWS CDK, see  [Getting started with the AWS CDK](./getting-started.html).

## Learn more

      To continue learning about the AWS CDK, see the following:

- 
            [Learn AWS CDK core concepts](./core-concepts.html)
- 
            [AWS CDK Workshop](https://cdkworkshop.com/)
- 
            [AWS CDK Patterns](https://cdkpatterns.com/)
- 
            [AWS CDK code examples](https://github.com/aws-samples/aws-cdk-examples)
- 
            [cdk.dev](https://cdk.dev/)
- 
            [Awesome CDK](https://github.com/kalaiser/awesome-cdk)
- 
            [AWS Solutions Constructs](https://aws.amazon.com/solutions/constructs/)
- 
            [AWS Developer Tools Blog](https://aws.amazon.com/blogs/developer/category/developer-tools/aws-cloud-development-kit/)
- 
            [AWS CDK on Stack Overflow](https://stackoverflow.com/questions/tagged/aws-cdk)**aws-cdk**on Stack Overflow.
- 
            [AWS CDK tutorial for AWS Cloud9](https://docs.aws.amazon.com/cloud9/latest/user-guide/sample-cdk.html)

To learn more about related topics to the AWS CDK, see the following:

- 
            [AWS CloudFormation concepts](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-whatis-concepts.html)
- 
            [AWS Glossary](https://docs.aws.amazon.com/general/latest/gr/glos-chap.html)

To learn more about tools related to the AWS CDK that can be used to simplify serverless application development and deployment, see the following:

- 
            [AWS Serverless Application Model](https://aws.amazon.com/serverless/sam/)
- 
            [AWS Chalice](https://github.com/aws/chalice)