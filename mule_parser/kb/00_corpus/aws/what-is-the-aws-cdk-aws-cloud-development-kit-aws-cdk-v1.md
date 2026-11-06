# What is the AWS CDK? - AWS Cloud Development Kit (AWS CDK) v1

**Source:** [https://docs.aws.amazon.com/cdk/v1/guide/index.html](https://docs.aws.amazon.com/cdk/v1/guide/index.html)

---

This is the AWS CDK v1 Developer Guide. The older CDK v1 entered
      maintenance on June 1, 2022 and will now only receive critical bug fixes and security patches.
      New features will be developed for CDK v2 exclusively. Support for CDK v1 will
      end entirely on June 1, 2023. [Migrate to CDK v2](./work-with-cdk-v2.html)
      to have access to the latest features and fixes.

Welcome to the *AWS Cloud Development Kit (AWS CDK) Developer Guide*. This document provides
    information about the AWS CDK, a framework for defining cloud infrastructure in code and
    provisioning it through CloudFormation.

###### Important

The CDK has been released in two major versions, v1 and v2. This is the Developer Guide for the older AWS CDK v1.

CDK v1 entered maintenance on June 1, 2022. During the maintenance phase,
      CDK v1 will receive critical bug fixes and security patches only. New features will be
      developed exclusively for CDK v2 during the v1 maintenance phase. On June 1, 2023,
      support will end for AWS CDK v1. For more details, see [AWS CDK Maintenance Policy](https://github.com/aws/aws-cdk-rfcs/blob/master/text/0079-cdk-2.0.md#aws-cdk-maintenance-policy).

The AWS CDK lets you build reliable, scalable, cost-effective applications in the cloud with the considerable expressive power of a programming language. This approach yields many benefits, including:

- 
      Build with high-level constructs that automatically provide sensible, secure defaults for your AWS resources, defining more infrastructure with less code. 
- 
      Use programming idioms like parameters, conditionals, loops, composition, and inheritance to model your system design from building blocks provided by AWS and others. 
- 
      Put your infrastructure, application code, and configuration all in one place, ensuring that at every milestone you have a complete, cloud-deployable system. 
- 
      Employ software engineering practices such as code reviews, unit tests, and source control to make your infrastructure more robust. 
- 
      Connect your AWS resources together (even across stacks) and grant permissions using simple, intent-oriented APIs. 
- 
      Import existing CloudFormation templates to give your resources a CDK API. 
- 
      Use the power of CloudFormation to perform infrastructure deployments predictably and repeatedly, with rollback on error. 
- 
      Easily share infrastructure design patterns among teams within your organization or even with the public. 

The AWS CDK supports TypeScript, JavaScript, Python, Java, C#/.Net, and Go. Developers can use
    one of these supported programming languages to define reusable cloud components known as [Constructs](./constructs.html). You compose these together into [Stacks](./stacks.html) and [Apps](./apps.html).

![App containing stacks with constructs like SQS Queue, Lambda, S3 Bucket, and DynamoDB Table.](/images/cdk/v1/guide/images/AppStacks.png) 

     
     
  ## Why use the AWS CDK?

    It's easier to show than to explain! Here's some CDK code that creates an Amazon ECS
      service with AWS Fargate launch type (this is the code we use in the [Creating an AWS Fargate service using the AWS CDK](./ecs-example.html)).

```
export class MyEcsConstructStack extends core.Stack {
  constructor(scope: core.App, id: string, props?: core.StackProps) {
    super(scope, id, props);
    const vpc = new ec2.Vpc(this, "MyVpc", {
      maxAzs: 3, // Default is all AZs in region
    });
    const cluster = new ecs.Cluster(this, "MyCluster", {
      vpc: vpc,
    });
    // Create a load-balanced Fargate service and make it public
    new ecs_patterns.ApplicationLoadBalancedFargateService(
      this,
      "MyFargateService",
      {
        cluster: cluster, // Required
        cpu: 512, // Default is 256
        desiredCount: 6, // Default is 1
        taskImageOptions: {
          image: ecs.ContainerImage.fromRegistry(
            "public.ecr.aws/ecs-sample-image/amazon-ecs-sample:latest"
          ),
        },
        memoryLimitMiB: 2048, // Default is 512
        publicLoadBalancer: true, // Default is false
      }
    );
  }
}
```
This class produces an CloudFormation [template of more than 500 lines](https://github.com/awsdocs/aws-cdk-guide/blob/main/doc_source/my_ecs_construct-stack.yaml); deploying the AWS CDK app produces more than 50
      resources of the following types.

And let's not forget... code completion within your IDE or editor!

![Code editor showing autocomplete suggestions for Node.js and Python runtime options.](/images/cdk/v1/guide/images/CodeCompletion.png) 

       
       
    ## Developing with the AWS CDK

    It's easy to [get set up](./getting-started.html) and [write your first CDK app](./hello-world.html). Short code examples are
      available throughout this Guide in the AWS CDK's supported programming languages: TypeScript,
      JavaScript, Python, Java, and C#. Longer examples are available [in our GitHub
        repository](https://github.com/aws-samples/aws-cdk-examples/tree/CDKv1).

The [AWS CDK Toolkit](./cli.html) is a command line tool for interacting with
      CDK apps. It enables developers to synthesize artifacts such as CloudFormation templates, deploy stacks
      to development AWS accounts, and **diff** against a deployed stack to
      understand the impact of a code change.

The [AWS Construct Library](./constructs.html) offers constructs for each
      AWS service, many with "rich" APIs that provide high-level abstractions. The aim of the
      AWS Construct Library is to reduce the complexity and glue logic required when integrating
      various AWS services to achieve your goals on AWS.

###### Note

There is no charge for using the AWS CDK, but you might incur AWS charges for creating
        or using AWS [chargeable resources](https://docs.aws.amazon.com/general/latest/gr/glos-chap.html#chargeable-resources), such
        as running Amazon EC2 instances or using Amazon S3 storage. Use the [AWS Pricing Calculator](https://calculator.aws/#/) to estimate charges for
        the use of various AWS resources.

## The Construct Programming Model

    The Construct Programming Model (CPM) extends the concepts behind the AWS CDK into additional domains. Other tools using the CPM include:

- 
        [CDK for Terraform](https://www.terraform.io/docs/cdktf/index.html)(CDKtf)
- 
        [CDK for Kubernetes](https://cdk8s.io/)(CDK8s)
- 
        [Projen](https://github.com/projen/projen), for building project configurations

[Construct Hub](https://constructs.dev/) is an online registry where you
      can find and publish construct libraries for CDKs like the AWS CDK.

## Additional documentation and resources

    In addition to this guide, the following other resources are available to AWS CDK users:

- 
        [cdk.dev](https://cdk.dev/)community hub, including a Slack channel
- 
        [AWS Developer Blog](https://aws.amazon.com/blogs/developer/category/developer-tools/aws-cloud-development-kit)CDK category

### Resources for serverless apps with CDK

These tools can work with the AWS CDK to simplify serverless application development and deployment.

- 
          [AWS Chalice](https://github.com/aws/chalice), a Python serverless microframework

## Contributing to the AWS CDK

    Because the AWS CDK is open source, the team encourages you to contribute to make it an even
      better tool. For details, see [Contributing](https://github.com/awslabs/aws-cdk/blob/main/CONTRIBUTING.md).

## About Amazon Web Services

    Amazon Web Services (AWS) is a collection of digital infrastructure services that developers can use when developing their applications. The services include computing, storage, database, and application synchronization (messaging and queueing).

AWS uses a pay-as-you-go service model. You are charged only for the services that you
      — or your applications — use. Also, to make AWS useful as a platform for
      prototyping and experimentation, AWS offers a free usage tier, in which services are free
      below a certain level of usage. For more information about AWS costs and the free usage
      tier, see [Test-Driving
        AWS in the Free Usage Tier](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-free-tier.html).

To obtain an AWS account, go to [aws.amazon.com](https://aws.amazon.com), and
      then choose 

**Create an AWS Account**.