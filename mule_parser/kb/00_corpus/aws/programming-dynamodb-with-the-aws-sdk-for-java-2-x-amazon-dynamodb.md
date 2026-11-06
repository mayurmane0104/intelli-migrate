# Programming DynamoDB with the AWS SDK for Java 2.x - Amazon DynamoDB

**Source:** [https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ProgrammingWithJava.html](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ProgrammingWithJava.html)

---

This programming guide provides an orientation for programmers who want to use Amazon DynamoDB with Java. The guide covers different concepts including abstraction layers, configuration management, error handling, controlling retry policies, and managing keep-alive.

###### Topics

## About the AWS SDK for Java 2.x

        You can access DynamoDB from Java using the official AWS SDK for Java. The SDK for Java has two
            versions: 1.x and 2.x. The end-of-support for 1.x was [announced](https://aws.amazon.com/blogs/developer/announcing-end-of-support-for-aws-sdk-for-java-v1-x-on-december-31-2025/) on January 12, 2024. It will
            enter
            maintenance mode on July 31, 2024 and its
            end-of-support is due on December 31, 2025. For new development, we highly recommend
            that you use 2.x, which was first released in 2018. This guide exclusively targets 2.x
            and focuses only on the parts of the SDK relevant to DynamoDB.

For information about maintenance and support for the AWS SDKs, see [AWS SDK and Tools
                maintenance policy](https://docs.aws.amazon.com/sdkref/latest/guide/maint-policy.html) and [AWS SDKs and Tools version
                support matrix](https://docs.aws.amazon.com/sdkref/latest/guide/version-support-matrix.html) in the *AWS SDKs and Tools Reference Guide*.

The AWS SDK for Java 2.x is a major rewrite of the 1.x code base. The SDK for Java 2.x supports modern Java features, such as the non-blocking I/O introduced in Java 8. The SDK for Java 2.x also adds support for pluggable HTTP client implementations to provide more network connection flexibility and configuration options.

A noticeable change between the SDK for Java 1.x and the SDK for Java 2.x is the use of a new
            package name. The Java 1.x SDK uses the `com.amazonaws` package name,
            while the Java 2.x SDK uses `software.amazon.awssdk`. Similarly, Maven
            artifacts for the Java 1.x SDK use the `com.amazonaws`
            `groupId`, while Java 2.x SDK artifacts use the
                `software.amazon.awssdk`
            `groupId`.

###### Important

The AWS SDK for Java 1.x has a DynamoDB package named
                `com.amazonaws.dynamodbv2`. The "v2" in the package name doesn't indicate
                that it's for Java 2 (J2SE). Rather, "v2" indicates that the package supports the
                    [second version](./CurrentAPI.html) of the DynamoDB low-level API
                instead of the [original version](./Appendix.APIv20111205.html) of the
                low-level API.

### Support for Java versions

The AWS SDK for Java 2.x provides full support for long-term support (LTS) [Java releases](https://github.com/aws/aws-sdk-java-v2?tab=readme-ov-file#maintenance-and-support-for-java-versions).

## Getting started with the AWS SDK for Java 2.x

        The following tutorial shows you how to use [Apache Maven](https://maven.apache.org/) for defining dependencies for the SDK for Java 2.x. This tutorial also
            shows you how to write the code that connects to DynamoDB for listing the available DynamoDB
            tables. The tutorial in this guide is based on the tutorial 

[Get started with the AWS SDK for Java 2.x](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html)in the

*AWS SDK for Java 2.x Developer Guide*. We've edited this tutorial to make calls to DynamoDB instead of Amazon S3.

###### To complete this tutorial, do the following:

### Step 1: Set up for this tutorial

Before you begin this tutorial, you need the following:

- 
                    Permission to access DynamoDB. 
- 
                    A Java development environment that's configured with single sign-on access to AWS services using the AWS access portal. 

To
                set
                up for this tutorial, follow the instructions in [Setup
                    overview](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/setup.html#setup-overview) in the *AWS SDK for Java 2.x Developer Guide*. After you
                    [configure
                    your development environment with single sign-on access](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/setup.html#setup-credentials) for the Java SDK
                and you have an [active
                    AWS access portal session](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/setup.html#setup-login-sso), then continue to [Step 2](#GetStartedJavaProjectSetup) of this tutorial.

### Step 2: Create the project

To create the project for this tutorial, you run a Maven command that prompts you
                for input on how to configure the project. After all input is entered and confirmed,
                Maven finishes building out the project by creating a `pom.xml`
                file and creating stub Java files.

- 
                    Open a terminal or command prompt window and navigate to a directory of your choice, for example, your `Desktop`or`Home`folder.
- 
                    Enter the following command at the terminal, and then press **Enter**.`mvn archetype:generate \ -DarchetypeGroupId=software.amazon.awssdk \ -DarchetypeArtifactId=archetype-app-quickstart \ -DarchetypeVersion=2.22.0`
- 
                    For each prompt, enter the value listed in the second column. Prompt Value to enter `Define value for property 'service':``dynamodb``Define value for property 'httpClient'`:`apache-client``Define value for property 'nativeImage'`:`false``Define value for property 'credentialProvider'``identity-center``Define value for property 'groupId':``org.example``Define value for property 'artifactId':``getstarted``Define value for property 'version' 1.0-SNAPSHOT:`*<Enter>*`Define value for property 'package' org.example:`*<Enter>*
- 
                    After you enter the last value, Maven lists the choices that you made. To confirm, enter **Y**. Or, enter**N**, and then re-enter your choices.

Maven creates a project folder named `getstarted` based on the
                    `artifactId` value that you entered. Inside the
                    `getstarted` folder, find a file named `README.md`
                that you can review, a `pom.xml` file, and a `src`
                directory.

Maven builds the following directory tree.

`getstarted ├── README.md ├── pom.xml └── src ├── main │ ├── java │ │ └── org │ │ └── example │ │ ├── App.java │ │ ├── DependencyFactory.java │ │ └── Handler.java │ └── resources │ └── simplelogger.properties └── test └── java └── org └── example └── HandlerTest.java 10 directories, 7 files`

The following shows the contents of the `pom.xml` project
                file.

The `dependencyManagement` section contains a dependency to the
                        AWS SDK for Java 2.x, and the `dependencies` section has a dependency for
                        DynamoDB. Specifying these dependencies forces Maven to include the relevant
                            `.jar`
                        files in your Java class path. By default, the AWS SDK doesn't include all
                        the classes for all AWS services. For
                        DynamoDB,
                        if you use the low-level interface, then you should have
                        a dependency on the `dynamodb` artifact. Or, if you use the
                        high-level interface, on the `dynamodb-enhanced` artifact. If you
                        don't include the relevant dependencies, then your code
                        can't
                        compile. The project uses Java 1.8 because of the `1.8` value in
                        the `maven.compiler.source` and
                            `maven.compiler.target` properties.

```
<?xml version="1.0" encoding="UTF-8"?>
 <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
     <modelVersion>4.0.0</modelVersion>
 
     <groupId>org.example</groupId>
     <artifactId>getstarted</artifactId>
     <version>1.0-SNAPSHOT</version>
     <packaging>jar</packaging>
     <properties>
         <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
         <maven.compiler.source>1.8</maven.compiler.source>
         <maven.compiler.target>1.8</maven.compiler.target>
         <maven.shade.plugin.version>3.2.1</maven.shade.plugin.version>
         <maven.compiler.plugin.version>3.6.1</maven.compiler.plugin.version>
         <exec-maven-plugin.version>1.6.0</exec-maven-plugin.version>
         <aws.java.sdk.version>2.22.0</aws.java.sdk.version>
```
` <-------- SDK version picked up from archetype version`.
         <slf4j.version>1.7.28</slf4j.version>
         <junit5.version>5.8.1</junit5.version>
     </properties>
 
     <dependencyManagement>
         <dependencies>
             <dependency>
                 <groupId>software.amazon.awssdk</groupId>
                 <artifactId>bom</artifactId>
                 <version>${aws.java.sdk.version}</version>
                 <type>pom</type>
                 <scope>import</scope>
             </dependency>
         </dependencies>
     </dependencyManagement>
 
     <dependencies>
         <dependency>
             <groupId>software.amazon.awssdk</groupId>
             <artifactId>dynamodb</artifactId> ` <-------- DynamoDB dependency`
             <exclusions>
                 <exclusion>
                     <groupId>software.amazon.awssdk</groupId>
                     <artifactId>netty-nio-client</artifactId>
                 </exclusion>
                 <exclusion>
                     <groupId>software.amazon.awssdk</groupId>
                     <artifactId>apache-client</artifactId>
                 </exclusion>
             </exclusions>
         </dependency>
 
         <dependency>
             <groupId>software.amazon.awssdk</groupId>
             <artifactId>sso</artifactId>` <-------- Required for identity center authentication.`
         </dependency>
 
         <dependency>
             <groupId>software.amazon.awssdk</groupId>
             <artifactId>ssooidc</artifactId>` <-------- Required for identity center authentication.`
         </dependency>
 
         <dependency>
             <groupId>software.amazon.awssdk</groupId>
             <artifactId>apache-client</artifactId>` <-------- HTTP client specified.`
             <exclusions>
                 <exclusion>
                     <groupId>commons-logging</groupId>
                     <artifactId>commons-logging</artifactId>
                 </exclusion>
             </exclusions>
         </dependency>
 
         <dependency>
             <groupId>org.slf4j</groupId>
             <artifactId>slf4j-api</artifactId>
             <version>${slf4j.version}</version>
         </dependency>
 
         <dependency>
             <groupId>org.slf4j</groupId>
             <artifactId>slf4j-simple</artifactId>
             <version>${slf4j.version}</version>
         </dependency>
 
         <!-- Needed to adapt Apache Commons Logging used by Apache HTTP Client to Slf4j to avoid
         ClassNotFoundException: org.apache.commons.logging.impl.LogFactoryImpl during runtime -->
         <dependency>
             <groupId>org.slf4j</groupId>
             <artifactId>jcl-over-slf4j</artifactId>
             <version>${slf4j.version}</version>
         </dependency>
 
         <!-- Test Dependencies -->
         <dependency>
             <groupId>org.junit.jupiter</groupId>
             <artifactId>junit-jupiter</artifactId>
             <version>${junit5.version}</version>
             <scope>test</scope>
         </dependency>
     </dependencies>
 
     <build>
         <plugins>
             <plugin>
                 <groupId>org.apache.maven.plugins</groupId>
                 <artifactId>maven-compiler-plugin</artifactId>
                 <version>${maven.compiler.plugin.version}</version>
             </plugin>
         </plugins>
     </build>
 
 </project>### Step 3: Write the code

The following code shows the `App` class that Maven creates. The
                    `main` method is the entry point into the application, which creates
                an instance of the `Handler` class and then calls its
                    `sendRequest` method.

```
package org.example;
 import org.slf4j.Logger;
 import org.slf4j.LoggerFactory;
 
 public class App {
     private static final Logger logger = LoggerFactory.getLogger(App.class);
 
     public static void main(String... args) {
         logger.info("Application starts");
 
         Handler handler = new Handler();
         handler.sendRequest();
 
         logger.info("Application ends");
     }
 }
```
The `DependencyFactory` class
                that
                Maven creates contains the `dynamoDbClient` factory
                method that builds and returns an [ DynamoDbClient](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/dynamodb/DynamoDbClient.html) instance. The
                    

`DynamoDbClient` instance uses an instance of the Apache-based HTTP
                client. This is because you specified `apache-client` when Maven prompted
                you for which HTTP client to use.The following code shows the `DependencyFactory` class.

```
package org.example;
 
 import software.amazon.awssdk.http.apache.ApacheHttpClient;
 import software.amazon.awssdk.services.dynamodb.DynamoDbClient;
 
 /**
  * The module containing all dependencies required by the {@link Handler}.
  */
 public class DependencyFactory {
 
     private DependencyFactory() {}
 
     /**
      * @return an instance of DynamoDbClient
      */
     public static DynamoDbClient dynamoDbClient() {
         return DynamoDbClient.builder()
                        .httpClientBuilder(ApacheHttpClient.builder())
                        .build();
     }
 }
```
The `Handler` class contains the main logic of your program. When an
                instance of `Handler` is created in the `App` class, the
                    `DependencyFactory` furnishes the `DynamoDbClient` service
                client. Your code uses the `DynamoDbClient` instance to call
                DynamoDB.

Maven generates the following `Handler` class with a
                        *TODO** TODO* comment with
                code.

```
package org.example;
 
 import software.amazon.awssdk.services.dynamodb.DynamoDbClient;
 
 
 public class Handler {
     private final DynamoDbClient dynamoDbClient;
 
     public Handler() {
         dynamoDbClient = DependencyFactory.dynamoDbClient();
     }
 
     public void sendRequest() {
         // TODO: invoking the API calls using dynamoDbClient.
     }
 }
```
To fill in the logic, replace the entire contents of the `Handler`
                class with the following code. The `sendRequest` method is filled in and
                the necessary imports are added.

The following code uses the [ DynamoDbClient](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/dynamodb/DynamoDbClient.html) instance to retrieve a list of
                        existing tables. If tables exist for a given account and
                        AWS Region,
                        then the code uses the 

`Logger` instance to log the names of
                        these tables.```
package org.example;
 
 import org.slf4j.Logger;
 import org.slf4j.LoggerFactory;
 import software.amazon.awssdk.services.dynamodb.DynamoDbClient;
 import software.amazon.awssdk.services.dynamodb.model.ListTablesResponse;
 
 
 public class Handler {
     private final DynamoDbClient dynamoDbClient;
 
     public Handler() {
         dynamoDbClient = DependencyFactory.dynamoDbClient();
     }
 
     public void sendRequest() {
         Logger logger = LoggerFactory.getLogger(Handler.class);
 
         logger.info("calling the DynamoDB API to get a list of existing tables");
         ListTablesResponse response = dynamoDbClient.listTables();
 
         if (!response.hasTableNames()) {
             logger.info("No existing tables found for the configured account & region");
         } else {
             response.tableNames().forEach(tableName -> logger.info("Table: " + tableName));
         }
     }
 }
```
### Step 4: Build and run the application

After you create the project and it contains the complete `Handler`
                class, build and run the application.

- 
                    Make sure that you have an active AWS IAM Identity Center session. To confirm, run the AWS Command Line Interface (AWS CLI) command `aws sts get-caller-identity`and check the response. If you don't have an active session, then see[Sign in using the AWS CLI](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/setup.html#setup-login-sso)for instructions.
- 
                    Open a terminal or command prompt window and navigate to your project directory `getstarted`.
- 
                    To build your project, run the following command: `mvn clean package`
- 
                    To run the application, run the following command: `mvn exec:java -Dexec.mainClass="org.example.App"`

After you view the file, delete the object, and then delete the bucket.

#### Success

If your Maven project built and ran without error, then congratulations! You've successfully built your first Java application using the SDK for Java 2.x.

#### Cleanup

To clean up the resources that you created during this tutorial, delete the
                    project folder `getstarted`.

## Reviewing the AWS SDK for Java 2.x documentation

        The [AWS SDK for Java 2.x Developer Guide](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/home.html) covers all aspects of the SDK across all AWS services.
            We
            recommend that you review the following topics:

- 
                [Migrate from version 1.x to 2.x](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration.html)– Includes a detailed explanation of the differences between 1.x and 2.x. This topic also contains instructions about how to use both major versions side-by-side.
- 
                [DynamoDB guide for Java 2.x SDK](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/examples-dynamodb.html)– Shows you how to perform basic DynamoDB operations: creating a table, manipulating items, and retrieving items. These examples use the low-level interface. Java has several interfaces, as explained in the following section:[Supported interfaces](#JavaInterfaces).

###### Tip

After you review these topics, bookmark the [AWS SDK for Java 2.x API Reference](https://sdk.amazonaws.com/java/api/latest/). It
                covers all AWS services, and
                we
                recommend that you use it as your main API reference.

## Supported interfaces

        The AWS SDK for Java 2.x supports the following interfaces, depending on the level of abstraction that you want.

###### Topics in this section

### Low-level interface

The low-level interface provides a one-to-one mapping to the underlying service
                API. Every DynamoDB API is available through this interface. This means that the
                low-level interface can provide complete functionality, but it's often more verbose
                and complex to use. For example, you have to use the `.s()` functions to
                hold strings and the `.n()` functions to hold numbers. The following
                example of [PutItem](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_PutItem.html)
                inserts an item using the low-level interface.

```
import org.slf4j.*;
import software.amazon.awssdk.http.crt.AwsCrtHttpClient;
import software.amazon.awssdk.services.dynamodb.DynamoDbClient;
import software.amazon.awssdk.services.dynamodb.model.*;
import java.util.Map;
public class PutItem {
    // Create a DynamoDB client with the default settings connected to the DynamoDB
    // endpoint in the default region based on the default credentials provider chain.
    private static final DynamoDbClient DYNAMODB_CLIENT = DynamoDbClient.create();
    private static final Logger LOGGER = LoggerFactory.getLogger(PutItem.class);
    private void putItem() {
        PutItemResponse response = DYNAMODB_CLIENT.putItem(PutItemRequest.builder()
                .item(Map.of(
                        "pk", AttributeValue.builder().s("123").build(),
                        "sk", AttributeValue.builder().s("cart#123").build(),
                        "item_data", AttributeValue.builder().s("YourItemData").build(),
                        "inventory", AttributeValue.builder().n("500").build()
                        // ... more attributes ...
                ))
                .returnConsumedCapacity(ReturnConsumedCapacity.TOTAL)
                .tableName("YourTableName")
                .build());
        LOGGER.info("PutItem call consumed [" + response.consumedCapacity().capacityUnits() + "] Write Capacity Unites (WCU)");
    }
}
```
### High-level interface

The high-level interface in the AWS SDK for Java 2.x is called the DynamoDB enhanced client. This interface provides a more idiomatic code authoring experience.

The enhanced client offers a way to map between client-side data classes and DynamoDB
                tables designed to store that data. You define the relationships between tables and
                their corresponding model classes in your code. Then, you can rely on the SDK to
                manage the data type manipulation. For more information about the enhanced client,
                see [DynamoDB
                    enhanced client API](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/dynamodb-enhanced-client.html) in the
                *AWS SDK for Java 2.x Developer Guide*.

The following example of [PutItem](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_PutItem.html) uses
                the high-level interface. In this example,
                the
                    `DynamoDbBean` named `YourItem` creates
                a `TableSchema`
                that
                enables its direct use as input for the `putItem()`
                call.

```
import org.slf4j.*;
import software.amazon.awssdk.enhanced.dynamodb.*;
import software.amazon.awssdk.enhanced.dynamodb.mapper.annotations.*;
import software.amazon.awssdk.enhanced.dynamodb.model.*;
import software.amazon.awssdk.services.dynamodb.model.ReturnConsumedCapacity;
public class DynamoDbEnhancedClientPutItem {
    private static final DynamoDbEnhancedClient ENHANCED_DYNAMODB_CLIENT = DynamoDbEnhancedClient.builder().build();
    private static final DynamoDbTable<YourItem> DYNAMODB_TABLE = ENHANCED_DYNAMODB_CLIENT.table("YourTableName", TableSchema.fromBean(YourItem.class));
    private static final Logger LOGGER = LoggerFactory.getLogger(PutItem.class);
    private void putItem() {
        PutItemEnhancedResponse<YourItem> response = DYNAMODB_TABLE.putItemWithResponse(PutItemEnhancedRequest.builder(YourItem.class)
                .item(new YourItem("123", "cart#123", "YourItemData", 500))
                .returnConsumedCapacity(ReturnConsumedCapacity.TOTAL)
                .build());
        LOGGER.info("PutItem call consumed [" + response.consumedCapacity().capacityUnits() + "] Write Capacity Unites (WCU)");
    }
    @DynamoDbBean
    public static class YourItem {
        public YourItem() {}
        public YourItem(String pk, String sk, String itemData, int inventory) {
            this.pk = pk;
            this.sk = sk;
            this.itemData = itemData;
            this.inventory = inventory;
        }
        private String pk;
        private String sk;
        private String itemData;
        private int inventory;
        @DynamoDbPartitionKey
        public void setPk(String pk) {
            this.pk = pk;
        }
        public String getPk() {
            return pk;
        }
        @DynamoDbSortKey
        public void setSk(String sk) {
            this.sk = sk;
        }
        public String getSk() {
            return sk;
        }
        public void setItemData(String itemData) {
            this.itemData = itemData;
        }
        public String getItemData() {
            return itemData;
        }
        public void setInventory(int inventory) {
            this.inventory = inventory;
        }
        public int getInventory() {
            return inventory;
        }
    }
}
```
The AWS SDK for Java 1.x has its own high-level interface, which is often referred to by
                its main class `DynamoDBMapper`. The AWS SDK for Java 2.x is published in a
                separate package (and Maven artifact) named
                    `software.amazon.awssdk.enhanced.dynamodb`. The Java 2.x SDK is
                often referred to by its main class `DynamoDbEnhancedClient`.

#### High-level interface using immutable data classes

The mapping feature of the DynamoDB enhanced client API also works with immutable
                    data classes. An immutable class has only getters and requires a builder class
                    that the SDK uses to create instances of the class. Immutability in Java is a
                    commonly used style that
                    developers
                    can use to create classes that have
                    no
                    side-effects. These classes are more predictable in their
                    behavior in complex multi-threaded applications. Instead of using the
                        `@DynamoDbBean` annotation as shown in the [High-level interface example](#highleveleg), immutable classes use
                    the `@DynamoDbImmutable` annotation, which takes the builder class as
                    its input.

The following example takes the builder class
                        `DynamoDbEnhancedClientImmutablePutItem` as input to create a
                    table schema. The example then provides the schema as input for the [PutItem](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_PutItem.html)
                    API call.

```
import org.slf4j.*;
import software.amazon.awssdk.enhanced.dynamodb.*;
import software.amazon.awssdk.enhanced.dynamodb.model.*;
import software.amazon.awssdk.services.dynamodb.model.ReturnConsumedCapacity;
public class DynamoDbEnhancedClientImmutablePutItem {
    private static final DynamoDbEnhancedClient ENHANCED_DYNAMODB_CLIENT = DynamoDbEnhancedClient.builder().build();
    private static final DynamoDbTable<YourImmutableItem> DYNAMODB_TABLE = ENHANCED_DYNAMODB_CLIENT.table("YourTableName", TableSchema.fromImmutableClass(YourImmutableItem.class));
    private static final Logger LOGGER = LoggerFactory.getLogger(DynamoDbEnhancedClientImmutablePutItem.class);
    private void putItem() {
        PutItemEnhancedResponse<YourImmutableItem> response = DYNAMODB_TABLE.putItemWithResponse(PutItemEnhancedRequest.builder(YourImmutableItem.class)
                .item(YourImmutableItem.builder()
                                        .pk("123")
                                        .sk("cart#123")
                                        .itemData("YourItemData")
                                        .inventory(500)
                                        .build())
                .returnConsumedCapacity(ReturnConsumedCapacity.TOTAL)
                .build());
        LOGGER.info("PutItem call consumed [" + response.consumedCapacity().capacityUnits() + "] Write Capacity Unites (WCU)");
    }
}
```
The following example shows the immutable data class.

```
@DynamoDbImmutable(builder = YourImmutableItem.YourImmutableItemBuilder.class)
class YourImmutableItem {
    private final String pk;
    private final String sk;
    private final String itemData;
    private final int inventory;
    public YourImmutableItem(YourImmutableItemBuilder builder) {
        this.pk = builder.pk;
        this.sk = builder.sk;
        this.itemData = builder.itemData;
        this.inventory = builder.inventory;
    }
    public static YourImmutableItemBuilder builder() { return new YourImmutableItemBuilder(); }
    @DynamoDbPartitionKey
    public String getPk() {
        return pk;
    }
    @DynamoDbSortKey
    public String getSk() {
        return sk;
    }
    public String getItemData() {
        return itemData;
    }
    public int getInventory() {
        return inventory;
    }
    static final class YourImmutableItemBuilder {
        private String pk;
        private String sk;
        private String itemData;
        private int inventory;
        private YourImmutableItemBuilder() {}
        public YourImmutableItemBuilder pk(String pk) { this.pk = pk; return this; }
        public YourImmutableItemBuilder sk(String sk) { this.sk = sk; return this; }
        public YourImmutableItemBuilder itemData(String itemData) { this.itemData = itemData; return this; }
        public YourImmutableItemBuilder inventory(int inventory) { this.inventory = inventory; return this; }
        public YourImmutableItem build() { return new YourImmutableItem(this); }
    }
}
```
#### High-level interface using immutable data classes and third-party boilerplate generation libraries

Immutable data classes (shown in the previous example) require some
                    boilerplate code. For example, the getter and setter logic on the data classes,
                    in addition to the `Builder` classes. Third-party libraries, such as
                        [Project Lombok](https://projectlombok.org/), can help you
                    generate that type of boilerplate code. Reducing most of the boilerplate code
                    helps you limit the amount of code needed for working with immutable data
                    classes and the AWS SDK. This further results in improved productivity and
                    readability of your code. For more information, see 

[Use third-party libraries, such as Lombok](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/ddb-en-client-use-immut.html#ddb-en-client-use-immut-lombok)in the

*AWS SDK for Java 2.x Developer Guide*.

The following example demonstrates how Project Lombok simplifies the code needed to use the DynamoDB enhanced client API.

```
import org.slf4j.*;
import software.amazon.awssdk.enhanced.dynamodb.*;
import software.amazon.awssdk.enhanced.dynamodb.model.*;
import software.amazon.awssdk.services.dynamodb.model.ReturnConsumedCapacity;
public class DynamoDbEnhancedClientImmutableLombokPutItem {
    private static final DynamoDbEnhancedClient ENHANCED_DYNAMODB_CLIENT = DynamoDbEnhancedClient.builder().build();
    private static final DynamoDbTable<YourImmutableLombokItem> DYNAMODB_TABLE = ENHANCED_DYNAMODB_CLIENT.table("YourTableName", TableSchema.fromImmutableClass(YourImmutableLombokItem.class));
    private static final Logger LOGGER = LoggerFactory.getLogger(DynamoDbEnhancedClientImmutableLombokPutItem.class);
    private void putItem() {
        PutItemEnhancedResponse<YourImmutableLombokItem> response = DYNAMODB_TABLE.putItemWithResponse(PutItemEnhancedRequest.builder(YourImmutableLombokItem.class)
                .item(YourImmutableLombokItem.builder()
                        .pk("123")
                        .sk("cart#123")
                        .itemData("YourItemData")
                        .inventory(500)
                        .build())
                .returnConsumedCapacity(ReturnConsumedCapacity.TOTAL)
                .build());
        LOGGER.info("PutItem call consumed [" + response.consumedCapacity().capacityUnits() + "] Write Capacity Unites (WCU)");
    }
}
```
The following example shows the immutable data object of the immutable data class.

```
import lombok.*;
import software.amazon.awssdk.enhanced.dynamodb.mapper.annotations.*;
@Builder
@DynamoDbImmutable(builder = YourImmutableLombokItem.YourImmutableLombokItemBuilder.class)
@Value
public class YourImmutableLombokItem {
    @Getter(onMethod_=@DynamoDbPartitionKey)
    String pk;
    @Getter(onMethod_=@DynamoDbSortKey)
    String sk;
    String itemData;
    int inventory;
}
```
The `YourImmutableLombokItem` class uses the following annotations
                    that Project Lombok and the AWS SDK provide:

- 
                        [@Builder](https://projectlombok.org/features/Builder)– Produces complex builder APIs for data classes that Project Lombok provides.
- 
                        [@DynamoDbImmutable](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/enhanced/dynamodb/mapper/annotations/DynamoDbImmutable.html)– Identifies the`DynamoDbImmutable`class as a DynamoDB mappable entity annotation that the AWS SDK provides.
- 
                        [@Value](https://projectlombok.org/features/Value)– The immutable variant of`@Data`. By default, all fields are made private and final, and setters are not generated. Project Lombok provides this annotation.

### Document interface

The AWS SDK for Java 2.x Document interface avoids the need to specify data type descriptors. The data types are implied by the semantics of the data itself. This Document interface is similar to the AWS SDK for Java 1.x, Document interface, but with a redesigned interface.

The following [Document interface example](#DocInterfaceEg) shows
                the `PutItem` call expressed using the Document interface. The example
                also uses EnhancedDocument. To
                run
                commands against a DynamoDB table using the enhanced document API, you must first
                associate the table with your document table schema to create a
                    `DynamoDBTable` resource object. The Document table schema builder
                requires the primary index key and attribute converter providers.

You can use `AttributeConverterProvider.defaultProvider()` to convert
                document attributes of default types. You can change the overall default behavior
                with a custom `AttributeConverterProvider` implementation. You can also
                change the converter for a single attribute. The [AWS SDKs and Tools Reference Guide](https://docs.aws.amazon.com/sdkref/latest/guide/version-support-matrix.html) provides more details and examples about how to
                use custom converters. Their primary use is for attributes of your domain classes
                that don't have a default converter available. Using a custom converter, you can
                provide the SDK with the needed information to write or read to DynamoDB.

```
import org.slf4j.*;
import software.amazon.awssdk.enhanced.dynamodb.*;
import software.amazon.awssdk.enhanced.dynamodb.document.EnhancedDocument;
import software.amazon.awssdk.enhanced.dynamodb.model.*;
import software.amazon.awssdk.services.dynamodb.model.ReturnConsumedCapacity;
public class DynamoDbEnhancedDocumentClientPutItem {
    private static final DynamoDbEnhancedClient ENHANCED_DYNAMODB_CLIENT = DynamoDbEnhancedClient.builder().build();
    private static final DynamoDbTable<EnhancedDocument> DYNAMODB_TABLE =
            ENHANCED_DYNAMODB_CLIENT.table("YourTableName", TableSchema.documentSchemaBuilder()
                            .addIndexPartitionKey(TableMetadata.primaryIndexName(),"pk", AttributeValueType.S)
                            .addIndexSortKey(TableMetadata.primaryIndexName(), "sk", AttributeValueType.S)
                            .attributeConverterProviders(AttributeConverterProvider.defaultProvider())
                            .build());
    private static final Logger LOGGER = LoggerFactory.getLogger(DynamoDbEnhancedDocumentClientPutItem.class);
    private void putItem() {
        PutItemEnhancedResponse<EnhancedDocument> response = DYNAMODB_TABLE.putItemWithResponse(
                        PutItemEnhancedRequest.builder(EnhancedDocument.class)
                                .item(
                                    EnhancedDocument.builder()
                                            .attributeConverterProviders(AttributeConverterProvider.defaultProvider())
                                            .putString("pk", "123")
                                            .putString("sk", "cart#123")
                                            .putString("item_data", "YourItemData")
                                            .putNumber("inventory", 500)
                                            .build())
                                .returnConsumedCapacity(ReturnConsumedCapacity.TOTAL)
                                .build());
        LOGGER.info("PutItem call consumed [" + response.consumedCapacity().capacityUnits() + "] Write Capacity Unites (WCU)");
    }
}
```
To convert JSON documents to and from the native Amazon DynamoDB data types, you can use the following utility methods:

- 
                    `EnhancedDocument.fromJson(String json)`
- 
                    `EnhancedDocument.toJson()`

### Comparing interfaces with a `Query` example

            This section shows the same [ Query](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Query.html) call expressed using the various interfaces. To fine
                tune the results of these queries,
                note
                the following:

- 
                    DynamoDB targets one specific partition key value, so you must specify the partition key completely. 
- 
                    To have the query target only cart items, the sort key has a key condition expression that uses `begins_with`.
- 
                    We use `limit()`to limit the query to a maximum of 100 returned items.
- 
                    We set the `scanIndexForward`to false. The results are returned in order of UTF-8 bytes, which usually means the cart item with the lowest number is returned first. By setting the`scanIndexForward`to false, we reverse the order and the cart item with the highest number is returned first.
- 
                    We apply a filter to remove any result that does not match the criteria. The data being filtered consumes read capacity whether the item matches the filter. 

###### Example `Query` using the low-level interface

The following example queries a table named `YourTableName` using a
                        `keyConditionExpression`. This limits the query to a specific
                    partition key value and sort key value that begin with a specific prefix value.
                    These key conditions limit the amount of data read from DynamoDB. Finally, the
                    query applies a filter on the data retrieved from DynamoDB using a
                        `filterExpression`.

```
import org.slf4j.*;
import software.amazon.awssdk.services.dynamodb.DynamoDbClient;
import software.amazon.awssdk.services.dynamodb.model.*;
import java.util.Map;
public class Query {
    // Create a DynamoDB client with the default settings connected to the DynamoDB 
    // endpoint in the default region based on the default credentials provider chain.
    private static final DynamoDbClient DYNAMODB_CLIENT = DynamoDbClient.builder().build();
    private static final Logger LOGGER = LoggerFactory.getLogger(Query.class);
    private static void query() {
        QueryResponse response = DYNAMODB_CLIENT.query(QueryRequest.builder()
                .expressionAttributeNames(Map.of("#name", "name"))
                .expressionAttributeValues(Map.of(
                    ":pk_val", AttributeValue.fromS("id#1"),
                    ":sk_val", AttributeValue.fromS("cart#"),
                    ":name_val", AttributeValue.fromS("SomeName")))
                .filterExpression("#name = :name_val")
                .keyConditionExpression("pk = :pk_val AND begins_with(sk, :sk_val)")
                .limit(100)
                .scanIndexForward(false)
                .tableName("YourTableName")
                .build());
        LOGGER.info("nr of items: " + response.count());
        LOGGER.info("First item pk: " + response.items().get(0).get("pk"));
        LOGGER.info("First item sk: " + response.items().get(0).get("sk"));
    }
}
```
###### Example `Query` using the Document interface

The following example queries a table named `YourTableName` using
                    the Document interface.

```
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import software.amazon.awssdk.enhanced.dynamodb.*;
import software.amazon.awssdk.enhanced.dynamodb.document.EnhancedDocument;
import software.amazon.awssdk.enhanced.dynamodb.model.*;
import java.util.Map;
public class DynamoDbEnhancedDocumentClientQuery {
    // Create a DynamoDB client with the default settings connected to the DynamoDB 
    // endpoint in the default region based on the default credentials provider chain.
    private static final DynamoDbEnhancedClient ENHANCED_DYNAMODB_CLIENT = DynamoDbEnhancedClient.builder().build();
    private static final DynamoDbTable<EnhancedDocument> DYNAMODB_TABLE =
            ENHANCED_DYNAMODB_CLIENT.table("YourTableName", TableSchema.documentSchemaBuilder()
                    .addIndexPartitionKey(TableMetadata.primaryIndexName(),"pk", AttributeValueType.S)
                    .addIndexSortKey(TableMetadata.primaryIndexName(), "sk", AttributeValueType.S)
                    .attributeConverterProviders(AttributeConverterProvider.defaultProvider())
                    .build());
    private static final Logger LOGGER = LoggerFactory.getLogger(DynamoDbEnhancedDocumentClientQuery.class);
    private void query() {
        PageIterable<EnhancedDocument> response = DYNAMODB_TABLE.query(QueryEnhancedRequest.builder()
                .filterExpression(Expression.builder()
                        .expression("#name = :name_val")
                        .expressionNames(Map.of("#name", "name"))
                        .expressionValues(Map.of(":name_val", AttributeValue.fromS("SomeName")))
                        .build())
                .limit(100)
                .queryConditional(QueryConditional.sortBeginsWith(Key.builder()
                        .partitionValue("id#1")
                        .sortValue("cart#")
                        .build()))
                .scanIndexForward(false)
                .build());
        LOGGER.info("nr of items: " + response.items().stream().count());
        LOGGER.info("First item pk: " + response.items().iterator().next().getString("pk"));
        LOGGER.info("First item sk: " + response.items().iterator().next().getString("sk"));
    }
}
```
###### Example `Query` using the high-level interface

The following example queries a table named `YourTableName` using
                    the DynamoDB enhanced client API.

```
import org.slf4j.*;
import software.amazon.awssdk.enhanced.dynamodb.*;
import software.amazon.awssdk.enhanced.dynamodb.mapper.annotations.*;
import software.amazon.awssdk.enhanced.dynamodb.model.*;
import software.amazon.awssdk.services.dynamodb.model.AttributeValue;
import java.util.Map;
public class DynamoDbEnhancedClientQuery {
    private static final DynamoDbEnhancedClient ENHANCED_DYNAMODB_CLIENT = DynamoDbEnhancedClient.builder().build();
    private static final DynamoDbTable<YourItem> DYNAMODB_TABLE = ENHANCED_DYNAMODB_CLIENT.table("YourTableName", TableSchema.fromBean(DynamoDbEnhancedClientQuery.YourItem.class));
    private static final Logger LOGGER = LoggerFactory.getLogger(DynamoDbEnhancedClientQuery.class);
    private void query() {
        PageIterable<YourItem> response = DYNAMODB_TABLE.query(QueryEnhancedRequest.builder()
                .filterExpression(Expression.builder()
                        .expression("#name = :name_val")
                        .expressionNames(Map.of("#name", "name"))
                        .expressionValues(Map.of(":name_val", AttributeValue.fromS("SomeName")))
                        .build())
                .limit(100)
                .queryConditional(QueryConditional.sortBeginsWith(Key.builder()
                        .partitionValue("id#1")
                        .sortValue("cart#")
                        .build()))
                .scanIndexForward(false)
                .build());
        LOGGER.info("nr of items: " + response.items().stream().count());
        LOGGER.info("First item pk: " + response.items().iterator().next().getPk());
        LOGGER.info("First item sk: " + response.items().iterator().next().getSk());
    }
    @DynamoDbBean
    public static class YourItem {
        public YourItem() {}
        public YourItem(String pk, String sk, String name) {
            this.pk = pk;
            this.sk = sk;
            this.name = name;
        }
        private String pk;
        private String sk;
        private String name;
        @DynamoDbPartitionKey
        public void setPk(String pk) {
            this.pk = pk;
        }
        public String getPk() {
            return pk;
        }
        @DynamoDbSortKey
        public void setSk(String sk) {
            this.sk = sk;
        }
        public String getSk() {
            return sk;
        }
        public void setName(String name) {
            this.name = name;
        }
        public String getName() {
            return name;
        }
    }
}
```
###### High-level interface using immutable data classes

When you perform a
                            `Query`
                        with the high-level immutable data classes, the code is the same as the
                        high-level interface example except for the construction of the entity class
                            `YourItem` or `YourImmutableItem`. For more
                        information, see the [PutItem](#HighLevelImmutableDataClassEg) example.

###### High-level interface using immutable data classes and third-party boilerplate generation libraries

When you perform a `Query` with the high-level immutable data
                        classes, the code is the same as the high-level interface example except for
                        the construction of the entity class `YourItem` or
                            `YourImmutableLombokItem`. For more information, see the
                            [PutItem](#HighLevelImmutableDataClassEg)
                        example.

## Additional code examples

        For additional examples of how to use DynamoDB with the SDK for Java 2.x, refer to the following code example repositories:

## Synchronous and asynchronous programming

        The AWS SDK for Java 2.x provides both *synchronous* and
                *asynchronous* clients for AWS services, such as DynamoDB.

The `DynamoDbClient` and `DynamoDbEnhancedClient` classes
            provide synchronous methods that block your thread's
            execution
            until the client receives a response from the service. This client is the most
            straightforward way of interacting with DynamoDB if you have no need for asynchronous
            operations.

The `DynamoDbAsyncClient` and `DynamoDbEnhancedAsyncClient`
            classes provide asynchronous methods that return immediately, and give control back to
            the calling thread without waiting for a response. The non-blocking client has an
            advantage that it
            uses
            for high concurrency across a few threads, which provides efficient handling of I/O
            requests with minimal compute resources. This improves throughput and
            responsiveness.

The AWS SDK for Java 2.x uses the native support for non-blocking I/O. The AWS SDK for Java 1.x had to simulate non-blocking I/O.

The synchronous methods return before a response is available, so you need a way to
            get the response when it's ready. The asynchronous methods in the AWS SDK for Java return a
                [ CompletableFuture](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/concurrent/CompletableFuture.html) object that contains the results of the
            asynchronous operation in the future. When you call 

`get()` or
                `join()` on these `CompletableFuture` objects, your code
            blocks
            until
            the result is available. If you call these at the same time that you make the request,
            then the behavior is similar to a plain synchronous call.For
            more information about asynchronous programming, see [Use asynchronous
                programming](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/asynchronous.html) in the
            *AWS SDK for Java 2.x Developer Guide*.

## HTTP clients

        For supporting every client, there exists an HTTP client that handles communication with the AWS services. You can plug in alternative HTTP clients, choosing one that has the characteristics that best fit your application. Some are more lightweight; some have more configuration options.

Some HTTP clients support only synchronous use, while others support only asynchronous
            use. For a flowchart that can help you select the optimal HTTP client for your workload,
            see [HTTP client recommendations](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/http-configuration.html#http-clients-recommend) in the
            *AWS SDK for Java 2.x Developer Guide*.

The following list presents some of the possible HTTP clients:

###### Topics

### Apache-based HTTP client

The [ ApacheHttpClient](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/http/apache/ApacheHttpClient.html) class supports synchronous service
                clients. It's the default HTTP client for synchronous use. For information about
                configuring the 

`ApacheHttpClient` class, see [Configure the Apache-based HTTP client](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/http-configuration-apache.html)in the

*AWS SDK for Java 2.x Developer Guide*.

`URLConnection`-based HTTP client

            The [ UrlConnectionHttpClient](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/http/urlconnection/UrlConnectionHttpClient.html) class is another option for
                synchronous clients. It loads more quickly than the Apache-based HTTP client, but
                has fewer features. For information about configuring the
                    

`UrlConnectionHttpClient` class, see [Configure the URLConnection-based HTTP client](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/http-configuration-url.html)in the

*AWS SDK for Java 2.x Developer Guide*.

### Netty-based HTTP client

The `NettyNioAsyncHttpClient` class supports async clients. It's the
                default choice for async use. For information about configuring the
                    `NettyNioAsyncHttpClient` class, see [Configure the Netty-based HTTP client](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/http-configuration-netty.html) in the
                    *AWS SDK for Java 2.x Developer Guide*.

### AWS CRT-based HTTP client

The newer `AwsCrtHttpClient` and `AwsCrtAsyncHttpClient`
                classes from the AWS Common Runtime (CRT) libraries are more options that support
                synchronous and asynchronous clients. Compared to other HTTP clients, AWS CRT
                offers:

- 
                    Faster SDK startup time 
- 
                    Smaller memory footprint 
- 
                    Reduced latency time 
- 
                    Connection health management 
- 
                    DNS load balancing 

For information about configuring the `AwsCrtHttpClient` and
                    `AwsCrtAsyncHttpClient` classes, see [Configure
                    the AWS CRT-based HTTP clients](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/http-configuration-crt.html) in the
                    *AWS SDK for Java 2.x Developer Guide*.

The AWS CRT-based HTTP client isn't the default because that would break backward compatibility for existing applications. However, for DynamoDB we recommend that you use the AWS CRT-based HTTP client for both sync and async uses.

For an introduction to the AWS CRT-based HTTP client, see [Announcing availability of the AWS CRT HTTP Client in the
                    AWS SDK for Java 2.x](https://aws.amazon.com/blogs/developer/announcing-availability-of-the-aws-crt-http-client-in-the-aws-sdk-for-java-2-x/) on the 

*AWS Developer Tools Blog*.

## Configuring an HTTP client

        When configuring a client, you can provide various configuration options, including:

- 
                Setting timeouts for different aspects of API calls. 
- 
                Enabling TCP Keep-Alive. 
- 
                Controlling the retry policy when encountering errors. 
- 
                Specifying execution attributes that [Execution interceptor](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/interceptors.html)instances can modify. Execution interceptors can write code that intercept the execution of your API requests and responses. This enables you to perform tasks such as publishing metrics and modifying requests in-flight.
- 
                Adding or manipulating HTTP headers. 
- 
                Enabling the tracking of [client-side performance metrics](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/metrics.html). Using this feature helps you to collect metrics about the service clients in your application and analyze the output in Amazon CloudWatch.
- 
                Specifying an alternate executor service to be used for scheduling tasks, such as async retry attempts and timeout tasks. 

You control the configuration by providing a [ ClientOverrideConfiguration](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/core/client/config/ClientOverrideConfiguration.html) object to the service client
                

`Builder` class. You'll see this in some code examples in the following
            sections.The `ClientOverrideConfiguration` provides standard configuration choices.
            The different pluggable HTTP clients have implementation-specific configuration
            possibilities as
            well.

###### Topics in this section

### Timeout configuration

You can adjust the client configuration to control various timeouts related to the service calls. DynamoDB provides lower latencies compared to other AWS services. Therefore, you might want to adjust these properties to lower timeout values so that you can fail fast if there's a networking issue.

You can customize the latency related behavior using
                    `ClientOverrideConfiguration` on the DynamoDB client or by changing
                detailed configuration options on the underlying HTTP client implementation.

You can configure the following impactful properties using
                    `ClientOverrideConfiguration`:

- 
                    `apiCallAttemptTimeout`– The amount of time to wait for a single attempt for an HTTP request to complete before giving up and timing out.
- 
                    `apiCallTimeout`– The amount of time that the client has to completely execute an API call. This includes the request handler execution that consists of all the HTTP requests, including retries.

The AWS SDK for Java 2.x provides [default values](https://github.com/aws/aws-sdk-java-v2/blob/a0c8a0af1fa572b16b5bd78f310594d642324156/http-client-spi/src/main/java/software/amazon/awssdk/http/SdkHttpConfigurationOption.java#L134) for some timeout options, such as connection timeout and
                socket timeouts. The SDK doesn't provide default values for API call timeouts or
                individual API call attempt timeouts. If these timeouts aren't set in the
                    

`ClientOverrideConfiguration`, then the SDK uses the socket timeout
                value instead for the overall API call timeout. The socket timeout has a default
                value of 30 seconds.### RetryMode

Another configuration related to the timeout configuration that you should
                consider is the `RetryMode` configuration object. This configuration
                object contains a collection of retry behaviors.

The SDK for Java 2.x supports the following retry modes:

- 
                    `legacy`– The default retry mode if you don't explicitly change it. This retry mode is specific to the Java SDK. It's characterized by up to three retries, or more for services such as DynamoDB, which has up to eight retries.
- 
                    `standard`– Named "standard" because it's more consistent with other AWS SDKs. This mode waits for a random amount of time ranging from 0ms to 1,000ms for the first retry. If another retry is necessary, then this mode picks another random time from 0ms to 1,000ms and multiplies it by two. If an additional retry is necessary, then it does the same random pick multiplied by four, and so on. Each wait is capped at 20 seconds. This mode performs retries on more detected failure conditions than the`legacy`mode. For DynamoDB, it performs up to three total max attempts unless you override with[numRetries](#numRetries).
- 
                    `adaptive`– Builds on`standard`mode and dynamically limits the rate of AWS requests to maximize success rate. This can occur at the expense of request latency. We don't recommend adaptive retry mode when predictable latency is important.

You can find an expanded definition of these retry modes in the [Retry
                    behavior](https://docs.aws.amazon.com/sdkref/latest/guide/feature-retry-behavior.html) topic in the *AWS SDKs and Tools Reference Guide*.

#### Retry policies

All `RetryMode` configurations have a [ RetryPolicy](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/core/retry/RetryPolicy.html), which is built based on one or more
                        

[configurations. The](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/core/retry/conditions/RetryCondition.html)

`RetryCondition`[is especially important to the retry behavior of the DynamoDB SDK client implementation. This condition limits the number of retries that the SDK makes using a token bucket algorithm. Depending on the selected retry mode, throttling exceptions may or may not subtract tokens from the](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/core/retry/conditions/TokenBucketRetryCondition.html)

`TokenBucketRetryCondition``TokenBucket`.When a client encounters a retryable error, such as a throttling exception or a temporary server error, then the SDK automatically retries the request. You can control how many times and how quickly these retries happen.

When configuring a client, you can provide a `RetryPolicy` that
                supports the following parameters:

- 
                    `numRetries`– The maximum number of retries that should be applied before a request is considered to be failed. The default value is 8 regardless of the retry mode that you use.###### WarningMake sure that you change this default value after due consideration. 
- 
                    `backoffStrategy`– The`BackoffStrategy``FullJitterBackoffStrategy`
- 
                    `retryCondition`– The`RetryCondition`

The following code provides an alternative retry policy. It specifies a total of five retries (six total requests). The first retry should occur after a delay of approximately 100ms, with each additional retry doubling that time exponentially, up to a maximum delay of one second.

```
DynamoDbClient client = DynamoDbClient.builder()
    .overrideConfiguration(ClientOverrideConfiguration.builder()
        .retryPolicy(RetryPolicy.builder()
            .backoffStrategy(FullJitterBackoffStrategy.builder()
                .baseDelay(Duration.ofMillis(100))
                .maxBackoffTime(Duration.ofSeconds(1))
                .build())
            .numRetries(5)
            .build())
        .build())
    .build();
```
### DefaultsMode

The timeout properties that `ClientOverrideConfiguration` and the
                    `RetryMode` don't manage are typically configured implicitly by
                specifying a `DefaultsMode`.

The AWS SDK for Java 2.x (version 2.17.102 or later) introduced support for
                    `DefaultsMode`. This feature provides a set of default values for
                common configurable settings, such as HTTP communication settings, retry behavior,
                service Regional endpoint settings, and potentially any SDK-related configuration.
                When you use this feature, you can get new configuration defaults tailored to common
                usage scenarios.

The default modes are standardized across all of the AWS SDKs. The SDK for Java 2.x supports the following default modes:

- 
                    `legacy`– Provides default settings that vary by AWS SDK and that existed before`DefaultsMode`was established.
- 
                    `standard`– Provides default non-optimized settings for most scenarios.
- 
                    `in-region`– Builds on the standard mode and includes settings tailored for applications that call AWS services from within the same AWS Region.
- 
                    `cross-region`– Builds on the standard mode and includes settings with high timeouts for applications that call AWS services in a different Region.
- 
                    `mobile`– Builds on the standard mode and includes settings with high timeouts tailored for mobile applications with higher latencies.
- 
                    `auto`– Builds on the standard mode and includes experimental features. The SDK attempts to discover the runtime environment to determine the appropriate settings automatically. The auto-detection is heuristics-based and does not provide 100% accuracy. If the runtime environment can't be determined, then standard mode is used. The auto-detection might query[Instance metadata and user data](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html), which might introduce latency. If startup latency is critical to your application, we recommend choosing an explicit`DefaultsMode`instead.

You can configure the defaults mode in the following ways:

- 
                    Directly on a client, through `AwsClientBuilder.Builder#defaultsMode(DefaultsMode)`.
- 
                    On a configuration profile, through the `defaults_mode`profile file property.
- 
                    Globally, through the `aws.defaultsMode`system property.
- 
                    Globally, through the `AWS_DEFAULTS_MODE`environment variable.

###### Note

For any mode other than `legacy`, the vended default values might
                    change as best practices evolve. Therefore, if you're using a mode other than
                        `legacy`, then we encourage you to perform testing when upgrading
                    the SDK.

The [Smart configuration
                    defaults](https://docs.aws.amazon.com/sdkref/latest/guide/feature-smart-config-defaults.html) in the *AWS SDKs and Tools Reference Guide* provides a
                list of configuration properties and their default values in the different default
                modes.

You choose the defaults mode value based on your application's characteristics and the AWS service that the application interacts with.

These values are configured with a broad selection of AWS services in mind. For
                a typical DynamoDB deployment in which both your DynamoDB
                tables
                and application are deployed in one Region, the `in-region` defaults mode
                is most relevant among the `standard` default modes.

###### Example DynamoDB SDK client configuration tuned for low-latency calls

The following example adjusts the timeouts to lower values for an expected low-latency DynamoDB call.

```
DynamoDbAsyncClient asyncClient = DynamoDbAsyncClient.builder()
    .defaultsMode(DefaultsMode.IN_REGION)
    .httpClientBuilder(AwsCrtAsyncHttpClient.builder())
    .overrideConfiguration(ClientOverrideConfiguration.builder()
        .apiCallTimeout(Duration.ofSeconds(3))
        .apiCallAttemptTimeout(Duration.ofMillis(500))
        .build())
    .build();
```
The individual HTTP client implementation may provide you with even more
                    granular control over the timeout and connection usage behavior. For example,
                    for the AWS CRT-based client, you can enable
                        `ConnectionHealthConfiguration`, which enables the client to
                    actively monitor the health of the used connections. For more information, see
                        [Advanced configuration of AWS CRT-based HTTP clients](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/http-configuration-crt.html#configuring-the-crt-based-http-client) in the
                        *AWS SDK for Java 2.x Developer Guide*.

### Keep-Alive configuration

Enabling keep-alive can reduce latencies by reusing connections. There are two different kinds of keep-alive: HTTP Keep-Alive and TCP Keep-Alive.

- 
                    HTTP Keep-Alive attempts to maintain the HTTPS connection between the client and server so later requests can reuse that connection. This skips the heavyweight HTTPS authentication on later requests. HTTP Keep-Alive is enabled by default on all clients. 
- 
                    TCP Keep-Alive requests that the underlying operating system sends small packets over the socket connection to provide extra assurance that the socket is kept alive and to immediately detect any drops. This ensures that a later request won't spend time trying to use a dropped socket. By default, TCP Keep-Alive is disabled on all clients. The following code examples show how to enable it on each HTTP client. When enabled for all non-CRT based HTTP clients, the actual Keep-Alive mechanism is dependent on the operating system. Therefore, you must configure additional TCP Keep-Alive values, such as timeout and number of packets, through the operating system. You can do this using `sysctl`on Linux or macOS, or using registry values on Windows.

###### Example to enable TCP Keep-Alive on an Apache-based HTTP client

```
DynamoDbClient client = DynamoDbClient.builder()
    .httpClientBuilder(ApacheHttpClient.builder().tcpKeepAlive(true))
    .build();
```
`URLConnection`-based HTTP client

                Any synchronous client that uses the `URLConnection`-based HTTP
                    client [ HttpURLConnection](https://docs.oracle.com/javase/8/docs/api/java/net/HttpURLConnection.html) doesn't have a 

[mechanism](https://docs.oracle.com/javase/8/docs/api/java/net/doc-files/net-properties.html)to enable keep-alive.

###### Example to enable TCP Keep-Alive on a Netty-based HTTP client

```
DynamoDbAsyncClient client = DynamoDbAsyncClient.builder()
    .httpClientBuilder(NettyNioAsyncHttpClient.builder().tcpKeepAlive(true))
    .build();
```
###### Example to enable TCP Keep-Alive on an AWS CRT-based HTTP client

With the AWS CRT-based HTTP client, you can enable TCP keep-alive and control the duration.

```
DynamoDbClient client = DynamoDbClient.builder()
    .httpClientBuilder(AwsCrtHttpClient.builder()
    .tcpKeepAliveConfiguration(TcpKeepAliveConfiguration.builder()
        .keepAliveInterval(Duration.ofSeconds(50))
        .keepAliveTimeout(Duration.ofSeconds(5))
        .build()))
    .build();
```
When using the asynchronous DynamoDB client, you can enable TCP Keep-Alive as shown in the following code.

```
DynamoDbAsyncClient client = DynamoDbAsyncClient.builder()
    .httpClientBuilder(AwsCrtAsyncHttpClient.builder()
    .tcpKeepAliveConfiguration(TcpKeepAliveConfiguration.builder()
        .keepAliveInterval(Duration.ofSeconds(50))
        .keepAliveTimeout(Duration.ofSeconds(5))
        .build()))
    .build();
```
## Error handling

        When it comes to exception handling, the AWS SDK for Java 2.x uses runtime (unchecked) exceptions.

The base exception, covering all SDK exceptions, is [ SdkServiceException](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/core/exception/SdkServiceException.html), which extends from the Java unchecked
                

`RuntimeException`. If you catch this, you'll catch all exceptions that
            the SDK throws.`SdkServiceException` has a subclass called [ AwsServiceException](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/awscore/exception/AwsServiceException.html). This subclass indicates any issue in
            communication with the AWS service. It has a subclass called 

[, which indicates an issue in communication with DynamoDB. If you catch this, you'll catch all exceptions related to DynamoDB, but no other SDK exceptions.](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/dynamodb/model/DynamoDbException.html)

`DynamoDbException`There are more specific [exception types](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/dynamodb/model/DynamoDbException.html) under 

`DynamoDbException`. Some of these
            exception types apply to control-plane operations such as [. Others apply to data-plane operations. The following is an example of a common data-plane exception:](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/dynamodb/model/TableAlreadyExistsException.html)

`TableAlreadyExistsException`- 
                `ConditionalCheckFailedException`

Other situations don't have a specific exception defined. For example, when your
            requests get throttled the specific `ProvisionedThroughputExceededException`
            might get thrown, while in other cases the more generic `DynamoDbException`
            is thrown. In either case, you can determine if throttling caused the exception by
            checking if `isThrottlingException()` returns `true`.

Depending on your application needs, you can catch all
                `AwsServiceException` or `DynamoDbException` instances.
            However, you often need different behavior in different situations. The logic to deal
            with a condition check failure is different than that to handle throttling. Define which
            exceptional paths you want to deal with and make sure to test the alternative paths.
            This helps you make sure that you can deal with all relevant scenarios.

For lists of common errors that you might encounter, see [Error handling with DynamoDB](./Programming.Errors.html). Also see [Common Errors](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/CommonErrors.html) in the *Amazon DynamoDB API Reference*. The API
            Reference also provides the exact errors possible for each
            API
            operation, such as for the [ Query](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Query.html)
            operation. For information about handling exceptions, see 

[Exception handling for the AWS SDK for Java 2.x](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/handling-exceptions.html)in the

*AWS SDK for Java 2.x Developer Guide*.

## AWS request ID

        Each request includes a request ID, which can be useful to pull if you're working with
            AWS Support to diagnose an issue. Each exception derived from
                `SdkServiceException` has a [ requestId()](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/core/exception/SdkServiceException.html#requestId()) method available to retrieve the request
            ID.

## Logging

        Using the logging provided that the SDK provides can be useful both for catching any
            important messages from the client libraries and for more in-depth debugging purposes.
            Loggers are hierarchical and the SDK uses `software.amazon.awssdk` as its
            root logger. You can configure the level with one of `TRACE`,
                `DEBUG`, `INFO`, `WARN`, `ERROR`,
                `ALL`, or `OFF`. The configured level applies to that logger
            and down into the logger hierarchy.

For its logging, the AWS SDK for Java 2.x uses the Simple Logging Façade for Java (SLF4J).
            This acts as an abstraction layer around other loggers, and you can use it to plug in
            the logger that you prefer. For instructions about plugging in loggers, see the [SLF4J user manual](https://www.slf4j.org/manual.html).

Each logger has a particular behavior. By default, the Log4j 2.x logger creates a
                `ConsoleAppender`, which appends log events to `System.out`
            and defaults to the `ERROR` log level.

The SimpleLogger logger included in SLF4J outputs by default to
                `System.err` and defaults to the `INFO` log level.

We recommend that you set the level to `WARN` for
                `software.amazon.awssdk` for any production deployments to catch any
            important messages from the SDK's client libraries while limiting the output
            quantity.

If SLF4J can't find a supported logger on the class path (no SLF4J binding), then it
            defaults to a [no operation
                implementation](https://www.slf4j.org/codes.html#noProviders). This implementation results in logging messages to
                

`System.err` explaining that SLF4J could not find a logger implementation
            on the classpath. To prevent this situation, you must add a logger implementation. To do
            this, you can add a dependency in your Apache Maven `pom.xml` on artifacts,
            such as `org.slf4j.slf4j-simple` or
                `org.apache.logging.log4j.log4j-slf4j2-imp`.For information about how to configure the logging in the SDK, including adding
            logging dependencies to your application configuration, see [Logging with the
                SDK for Java 2.x](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/logging-slf4j.html) in the *AWS SDK for Java Developer Guide*.

The following configuration in the `Log4j2.xml` file shows how to adjust
            the logging behavior if you use the Apache Log4j 2 logger. This configuration sets the
            root logger level to `WARN`. All loggers in the hierarchy inherit this log
            level, including the `software.amazon.awssdk` logger.

By default, the output goes to `System.out`. In the following example, we
            still override the default output Log4j appender to apply a tailored Log4j
                `PatternLayout`.

###### Example of a `Log4j2.xml` configuration file

            The following configuration logs messages to the console at the `ERROR`
                and `WARN` levels for all logger hierarchies.

```
<Configuration status="WARN">
  <Appenders>
    <Console name="ConsoleAppender" target="SYSTEM_OUT">
      <PatternLayout pattern="%d{YYYY-MM-dd HH:mm:ss} [%t] %-5p %c:%L - %m%n" />
    </Console>
  </Appenders>
  <Loggers>
    <Root level="WARN">
      <AppenderRef ref="ConsoleAppender"/>
    </Root>
  </Loggers>
</Configuration>
```
### AWS request ID logging

When something goes wrong, you can find request IDs within exceptions. However, if you want the request IDs for requests that aren't generating exceptions, then you can use logging.

The `software.amazon.awssdk.request` logger outputs request IDs at the
                    `DEBUG` level. The following example extends the previous [configuration example](#Log4j2ConfigEg) to keep the root logger
                level at `ERROR`, the `software.amazon.awssdk` at level
                    `WARN`, and the `software.amazon.awssdk.request` at level
                    `DEBUG`. Setting these levels helps to catch the request IDs and
                other request-related details, such as the endpoint and status code.

```
<Configuration status="WARN">
  <Appenders>
    <Console name="ConsoleAppender" target="SYSTEM_OUT">
      <PatternLayout pattern="%d{YYYY-MM-dd HH:mm:ss} [%t] %-5p %c:%L - %m%n" />
    </Console>
  </Appenders>
  <Loggers>
    <Root level="ERROR">
      <AppenderRef ref="ConsoleAppender"/>
    </Root>
    <Logger name="software.amazon.awssdk" level="WARN" />
    <Logger name="software.amazon.awssdk.request" level="DEBUG" />
  </Loggers>
</Configuration>
```
Here is an example of the log output:

`2022-09-23 16:02:08 [main] DEBUG software.amazon.awssdk.request:85 - Sending Request: DefaultSdkHttpFullRequest(httpMethod=POST, protocol=https, host=dynamodb.us-east-1.amazonaws.com, encodedPath=/, headers=[amz-sdk-invocation-id, Content-Length, Content-Type, User-Agent, X-Amz-Target], queryParameters=[]) 2022-09-23 16:02:08 [main] DEBUG software.amazon.awssdk.request:85 - Received successful response: 200, Request ID: QS9DUMME2NHEDH8TGT9N5V53OJVV4KQNSO5AEMVJF66Q9ASUAAJG, Extended Request ID: not available`

## Pagination

        Some requests, such as [ Query](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Query.html)
            and 

[, limit the size of data returned on a single request and require you make repeated requests to pull subsequent pages.](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Scan.html)

`Scan`You can control the maximum number of items to read for each page with the
                `Limit` parameter. For example, you can use the `Limit`
            parameter to retrieve only the last 10 items. This limit specifies how many items to
            read from the table before any filtering is applied. If you want exactly 10 items after
            filtering, there's no way to specify that. You can control only the pre-filtered count
            and check client-side when you've actually retrieved 10 items. Regardless of the limit,
            responses always have a maximum size of 1 MB.

A `LastEvaluatedKey` might be included in the API response. This indicates
            that the response ended because it reached a count limit or a size limit. This key is
            the last key evaluated for that response. By interacting directly with the API, you can
            retrieve this `LastEvaluatedKey` and pass it to a follow-up call as
                `ExclusiveStartKey` to read the next chunk from that starting point. If
            no `LastEvaluatedKey` is returned, it means that there are no more items that
            match the `Query` or `Scan` API call.

The following example uses the low-level interface to limit the items to 100 based on
            the `keyConditionExpression` parameter.

```
QueryRequest.Builder queryRequestBuilder = QueryRequest.builder()
        .expressionAttributeValues(Map.of(
                ":pk_val", AttributeValue.fromS("123"),
                ":sk_val", AttributeValue.fromN("1000")))
        .keyConditionExpression("pk = :pk_val AND sk > :sk_val")
        .limit(100)
        .tableName(TABLE_NAME);
while (true) {
    QueryResponse queryResponse = DYNAMODB_CLIENT.query(queryRequestBuilder.build());
    queryResponse.items().forEach(item -> {
        LOGGER.info("item PK: [" + item.get("pk") + "] and SK: [" + item.get("sk") + "]");
    });
    if (!queryResponse.hasLastEvaluatedKey()) {
        break;
    }
    queryRequestBuilder.exclusiveStartKey(queryResponse.lastEvaluatedKey());
}
```
The AWS SDK for Java 2.x can simplify this interaction with DynamoDB by providing auto-pagination methods that make multiple service calls to automatically get the next pages of results for you. This simplifies your code, but it takes away some control of resource usage that you would keep by manually reading pages.

By using the `Iterable` methods available in the DynamoDB client, such as
                [ QueryPaginator](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/dynamodb/DynamoDbClient.html#queryPaginator(software.amazon.awssdk.services.dynamodb.model.QueryRequest)) and 

[, the SDK takes care of the pagination. The return type of these methods is a custom iterable that you can use to iterate through all the pages. The SDK internally handles service calls for you. Using the Java Stream API, you can handle the result of](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/dynamodb/DynamoDbClient.html#scanPaginator(software.amazon.awssdk.services.dynamodb.model.ScanRequest))

`ScanPaginator``QueryPaginator` as shown in the following
            example.```
QueryPublisher queryPublisher =
    DYNAMODB_CLIENT.queryPaginator(QueryRequest.builder()
        .expressionAttributeValues(Map.of(
            ":pk_val", AttributeValue.fromS("123"),
            ":sk_val", AttributeValue.fromN("1000")))
        .keyConditionExpression("pk = :pk_val AND sk > :sk_val")
        .limit(100)
        .tableName("YourTableName")
        .build());
queryPublisher.items().subscribe(item ->
    System.out.println(item.get("itemData"))).join();
```
## Data class annotations

        The Java SDK provides several annotations that you can put on the attributes of your
            data class. These annotations influence how the SDK interacts with the attributes. By
            adding an annotation, you can have an attribute behave as an implicit atomic counter,
            maintain an auto-generated timestamp value, or track an item version number. For more
            information, see [Data class
                annotations](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/ddb-en-client-anno-index.html).