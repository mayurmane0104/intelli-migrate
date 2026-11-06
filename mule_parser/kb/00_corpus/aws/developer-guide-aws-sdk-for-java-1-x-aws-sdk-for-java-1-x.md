# Developer Guide - AWS SDK for Java 1.x - AWS SDK for Java 1.x

**Source:** [https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/index.html](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/index.html)

---

The AWS SDK for Java 1.x reached end-of-support on December 31, 2025. We recommend that you migrate to
      the [AWS SDK for Java 2.x](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/home.html) to continue receiving new features, availability improvements, and
      security updates.

The
[AWS SDK for Java](https://aws.amazon.com/sdk-for-java/) provides a Java API for AWS services. Using
the SDK, you can easily build Java applications that work with Amazon S3, Amazon EC2, DynamoDB, and
more. We regularly add support for new services to the AWS SDK for Java. For a list of the supported
services and their API versions that are included with each release of the SDK, view the

[release notes](https://github.com/aws/aws-sdk-java#release-notes)for the version that you’re working with.

## Version 2 of the SDK released

      Take a look at the new AWS SDK for Java 2.x at
[https://github.com/aws/aws-sdk-java-v2/](https://github.com/aws/aws-sdk-java-v2/). It includes much awaited features, such as a way to plug in an
HTTP implementation. To get started, see the

[AWS SDK for Java 2.x Developer Guide](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide).

## Additional Documentation and Resources

      In addition to this guide, the following are valuable online resources for AWS SDK for Java developers:

## Eclipse IDE Support

      If you develop code using the Eclipse IDE, you can use the
[AWS Toolkit for Eclipse](https://aws.amazon.com/eclipse/)
to add the AWS SDK for Java to an existing Eclipse project or to create a new AWS SDK for Java project. The
toolkit also supports creating and uploading Lambda functions, launching and monitoring Amazon EC2
instances, managing IAM users and security groups, a AWS CloudFormation template editor, and more.

See the
[AWS Toolkit for Eclipse User Guide](https://docs.aws.amazon.com/toolkit-for-eclipse/v1/user-guide/)
for full documentation.

## Developing Applications for Android

      If you’re an Android developer, Amazon Web Services publishes an SDK made
         specifically for Android development: the [Amplify Android (AWS Mobile SDK for Android)](https://docs.aws.amazon.com/sdk-for-android/index.html).

## Viewing the SDK’s Revision History

      To view the release history of the AWS SDK for Java, including changes and supported services per SDK
version, see the SDK’s  [release notes](https://github.com/aws/aws-sdk-java#release-notes).

## Building Java Reference Documentation for Earlier SDK versions

      The [AWS SDK for Java API Reference](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/)
represents the most recent build of version 1.x of the SDK. If you’re using an earlier build of
the 1.x version, you might want to access the SDK reference documentation that matches the
version you’re using.

The easiest way to build the documentation is using Apache’s
[Maven](https://maven.apache.org/) build tool. 

*Download and install Maven first if you don’t already have it on your system*, then use the following instructions to build the reference documentation.

- 
            Locate and select the SDK version that you’re using on the [releases](https://github.com/aws/aws-sdk-java/releases)page of the SDK repository on GitHub.
- 
            Choose either the `zip`(most platforms, including Windows) or`tar.gz`(Linux, macOS, or Unix) link to download the SDK to your computer.
- 
            Unpack the archive to a local directory. 
- 
            On the command line, navigate to the directory where you unpacked the archive, and type the following. `mvn javadoc:javadoc`
- 
            After building is complete, you’ll find the generated HTML documentation in the `aws-java-sdk/target/site/apidocs/`directory.