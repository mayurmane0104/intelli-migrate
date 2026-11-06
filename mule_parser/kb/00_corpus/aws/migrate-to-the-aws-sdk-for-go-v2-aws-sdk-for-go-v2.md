# Migrate to the AWS SDK for Go v2 - AWS SDK for Go v2

**Source:** [https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/migrate-gosdk.html](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/migrate-gosdk.html)

---

## Minimum Go Version

    
    
      The AWS SDK for Go requires a minimum version of Go 1.23.
      The latest version of Go can be downloaded on the
      [Downloads](https://go.dev/dl/) page.
      See the
      

[Release History](https://go.dev/doc/devel/release)for more information about each Go version release, and relevant information required for upgrading.

## Modularization

    
    The AWS SDK for Go has been updated to take advantage of the Go modules which became the default development mode in Go 1.13. A number of packages provided by the SDK have been modularized and are independently versioned and released respectively. This change enables improved application dependency modeling, and enables the SDK to provide new features and functionality that follows the Go module versioning strategy.

The following list are some Go modules provided by the SDK:

| Module | Description | 
|---|---|
| `github.com/aws/aws-sdk-go-v2` | The SDK core | 
| `github.com/aws/aws-sdk-go-v2/config` | Shared Configuration Loading | 
| `github.com/aws/aws-sdk-go-v2/credentials` | AWS Credential Providers | 
| `github.com/aws/aws-sdk-go-v2/feature/ec2/imds` | Amazon EC2 Instance Metadata Service Client | 

The SDK's service clients and higher level utilities modules are nested under the following import paths:

| Import Root | Description | 
|---|---|
| `github.com/aws/aws-sdk-go-v2/service/` | Service Client Modules | 
| `github.com/aws/aws-sdk-go-v2/feature/` | High-Level utilities for services like the Amazon S3 Transfer Manager | 

## Configuration Loading

    
    
      The
      [session](https://docs.aws.amazon.com/sdk-for-go/api/aws/session/)
      package and associated functionality are replaced with a
      simplified configuration system provided by the
      [config](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/config)
      package. The 

`config` package is a separate Go
      module, and can be included in your application's dependencies by
      with `go get`.
    `go get github.com/aws/aws-sdk-go-v2/config`

      The
      [session.New](https://docs.aws.amazon.com/sdk-for-go/api/aws/session/#New),
      [session.NewSession](https://docs.aws.amazon.com/sdk-for-go/api/aws/session/#NewSession),
      [NewSessionWithOptions](https://docs.aws.amazon.com/sdk-for-go/api/aws/session/#NewSessionWithOptions),
      and [session.Must](https://docs.aws.amazon.com/sdk-for-go/api/aws/session/#Must)
      must be migrated to
      [config.LoadDefaultConfig](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/config#LoadDefaultConfig).
    

      The `config` package provides several helper
      functions that aid in overriding the shared configuration loading
      programmatically. These function names are prefixed with
      `With` followed by option that they override.
      Let's look at some examples of how to migrate usage of the
      `session` package.
    

      For more information on loading shared configuration, see
      [Configure the SDK](./configure-gosdk.html).
    

### Examples

#### Migrating from NewSession to LoadDefaultConfig

          The following example shows how usage of
          `session.NewSession` without additional
          argument parameters is migrated to
          `config.LoadDefaultConfig`.
        

```
// V1 using NewSession
import "github.com/aws/aws-sdk-go/aws/session"
// ...
sess, err := session.NewSession()
if err != nil {
    // handle error
}
```
```
// V2 using LoadDefaultConfig
import "context"
import "github.com/aws/aws-sdk-go-v2/config"
// ...
cfg, err := config.LoadDefaultConfig(context.TODO())
if err != nil {
    // handle error
}
```
#### Migrating from NewSession with aws.Config options

          The example shows how to migrate overriding of
          `aws.Config` values during configuration
          loading. One or more `config.With*` helper
          functions can be provided to
          `config.LoadDefaultConfig` to override the
          loaded configuration values. In this example the AWS Region is
          overridden to `us-west-2` using the
          [config.WithRegion](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/config#WithRegion)
          helper function.
        

```
// V1
import "github.com/aws/aws-sdk-go/aws"
import "github.com/aws/aws-sdk-go/aws/session"
// ...
sess, err := session.NewSession(aws.Config{
    Region: aws.String("us-west-2")
})
if err != nil {
    // handle error
}
```
```
// V2
import "context"
import "github.com/aws/aws-sdk-go-v2/config"
// ...
cfg, err := config.LoadDefaultConfig(context.TODO(),
    config.WithRegion("us-west-2"),
)
if err != nil {
    // handle error
}
```
#### Migrating from NewSessionWithOptions

          This example shows how to migrate overriding values during
          configuration loading. Zero or more
          `config.With*` helper functions can be
          provided to `config.LoadDefaultConfig` to
          override the loaded configuration values. In this example we
          show how to override the target profile that is used when
          loading the AWS SDK shared configuration.
        

```
// V1
import "github.com/aws/aws-sdk-go/aws"
import "github.com/aws/aws-sdk-go/aws/session"
// ...
sess, err := session.NewSessionWithOptions(aws.Config{
    Profile: "my-application-profile"
})
if err != nil {
    // handle error
}
```
```
// V2
import "context"
import "github.com/aws/aws-sdk-go-v2/config"
// ...
cfg, err := config.LoadDefaultConfig(context.TODO(),
    config.WithSharedConfigProfile("my-application-profile"),
)
if err != nil {
    // handle error
}
```
## Mocking and `*iface`

    
    
      The `*iface` packages and interfaces therein
      (e.g.
      [s3iface.S3API](https://docs.aws.amazon.com/sdk-for-go/api/service/s3/s3iface/#S3API))
      have been removed. These interface definitions are not stable
      since they are broken every time a service adds a new operation.
    

      Usage of `*iface` should be replaced by scoped
      caller-defined interfaces for the service operations being used:
    

```
// V1
import "io"
import "github.com/aws/aws-sdk-go/service/s3"
import "github.com/aws/aws-sdk-go/service/s3/s3iface"
func GetObjectBytes(client s3iface.S3API, bucket, key string) ([]byte, error) {
    object, err := client.GetObject(&s3.GetObjectInput{
        Bucket: &bucket,
        Key:    &key,
    })
    if err != nil {
        return nil, err
    }
    defer object.Body.Close()
    return io.ReadAll(object.Body)
}
```
```
// V2
import "context"
import "io"
import "github.com/aws/aws-sdk-go-v2/service/s3"
type GetObjectAPIClient interface {
    GetObject(context.Context, *s3.GetObjectInput, ...func(*s3.Options)) (*s3.GetObjectOutput, error)
}
func GetObjectBytes(ctx context.Context, client GetObjectAPIClient, bucket, key string) ([]byte, error) {
    object, err := client.GetObject(ctx, &s3.GetObjectInput{
        Bucket: &bucket,
        Key:    &key,
    })
    if err != nil {
        return nil, err
    }
    defer object.Body.Close()
    return io.ReadAll(object.Body)
}
```
      See the [Unit Testing with the AWS SDK for Go v2](./unit-testing.html) for more information.
    

## Credentials and Credential Providers

    
    
      The
      [aws/credentials](https://docs.aws.amazon.com/sdk-for-go/api/aws/credentials/)
      package and associated credential providers have been relocated to the
      [credentials](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/credentials)
      package location. The 

`credentials` package is a
      Go module that you retrieve by using `go get`.
    `go get github.com/aws/aws-sdk-go-v2/credentials`

      The AWS SDK for Go v2 release updates the AWS Credential
      Providers to provide a consistent interface for retrieving AWS
      Credentials. Each provider implements the
      [aws.CredentialsProvider](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/aws#CredentialsProvider)
      interface, which defines a 

`Retrieve` method that
      returns a `(aws.Credentials, error)`.
      [aws.Credentials](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/aws#Credentials)that is analogous to the AWS SDK for Go v1

[credentials.Value](https://docs.aws.amazon.com/sdk-for-go/api/aws/credentials/#Value)type.

      You must wrap `aws.CredentialsProvider` objects
      with
      [aws.CredentialsCache](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/aws#CredentialsCache)
      to allow credential caching to occur. You use
      

[NewCredentialsCache](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/aws#NewCredentialsCache)to construct a

`aws.CredentialsCache` object. By
      default, credentials configured by
      `config.LoadDefaultConfig` are wrapped with
      `aws.CredentialsCache`.
    The following table list the location changes of the AWS credential providers from AWS SDK for Go v1 to v2.

| Name | V1 Import | V2 Import | 
|---|---|---|
| Amazon EC2 IAM Role Credentials | `github.com/aws/aws-sdk-go/aws/credentials/ec2rolecreds` | `github.com/aws/aws-sdk-go-v2/credentials/ec2rolecreds` | 
| Endpoint Credentials | `github.com/aws/aws-sdk-go/aws/credentials/endpointcreds` | `github.com/aws/aws-sdk-go-v2/credentials/endpointcreds` | 
| Process Credentials | `github.com/aws/aws-sdk-go/aws/credentials/processcreds` | `github.com/aws/aws-sdk-go-v2/credentials/processcreds` | 
| AWS Security Token Service | `github.com/aws/aws-sdk-go/aws/credentials/stscreds` | `github.com/aws/aws-sdk-go-v2/credentials/stscreds` | 

### Static Credentials

        Applications that use
        [credentials.NewStaticCredentials](https://docs.aws.amazon.com/sdk-for-go/api/aws/credentials//#NewStaticCredentials)
        to construct static credential programmatically must use
        [credentials.NewStaticCredentialsProvider](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/credentials#NewStaticCredentialsProvider).
      

#### Example

```
// V1
import "github.com/aws/aws-sdk-go/aws/credentials"
// ...
appCreds := credentials.NewStaticCredentials(accessKey, secretKey, sessionToken)
value, err := appCreds.Get()
if err != nil {
    // handle error
}
```
```
// V2
import "context"
import "github.com/aws/aws-sdk-go-v2/aws"
import "github.com/aws/aws-sdk-go-v2/credentials"
// ...
appCreds := aws.NewCredentialsCache(credentials.NewStaticCredentialsProvider(accessKey, secretKey, sessionToken))
value, err := appCreds.Retrieve(context.TODO())
if err != nil {
    // handle error
}
```
### Amazon EC2 IAM Role Credentials

        You must migrate usage of
        [NewCredentials](https://docs.aws.amazon.com/sdk-for-go/api/aws/credentials/ec2rolecreds/#NewCredentials)
        and
        [NewCredentialsWithClient](https://docs.aws.amazon.com/sdk-for-go/api/aws/credentials/ec2rolecreds/#NewCredentialsWithClient)
        to use
        [New](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/credentials/ec2rolecreds#New).
      

        The `ec2rolecreds` package's
        `ec2rolecreds.New` takes functional options of
        [ec2rolecreds.Options](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/credentials/ec2rolecreds#Options)
        as input, allowing you override the specific Amazon EC2 Instance
        Metadata Service client to use, or to override the credential
        expiry window.
      

#### Example

```
// V1
import "github.com/aws/aws-sdk-go/aws/credentials/ec2rolecreds"
// ...
appCreds := ec2rolecreds.NewCredentials(sess)
value, err := appCreds.Get()
if err != nil {
    // handle error
}
```
```
// V2
import "context"
import "github.com/aws/aws-sdk-go-v2/aws"
import "github.com/aws/aws-sdk-go-v2/credentials/ec2rolecreds"
// ...
// New returns an object of a type that satisfies the aws.CredentialProvider interface
appCreds := aws.NewCredentialsCache(ec2rolecreds.New())
value, err := appCreds.Retrieve(context.TODO())
if err != nil {
    // handle error
}
```
### Endpoint Credentials

        You must migrate usage of
        [NewCredentialsClient](https://docs.aws.amazon.com/sdk-for-go/api/aws/credentials/endpointcreds/#NewCredentialsClient)
        and
        [NewProviderClient](https://docs.aws.amazon.com/sdk-for-go/api/aws/credentials/endpointcreds/#NewProviderClient)
        to use
        [New](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/credentials/endpointcreds#New).
      

        The `endpointcreds` package's
        `New` function takes a string argument
        containing the URL of an HTTP or HTTPS endpoint to retrieve
        credentials from, and functional options of
        [endpointcreds.Options](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/credentials/endpointcreds#Options) 
        to mutate the credentials provider and override specific configuration settings.
      

### Process Credentials

        You must migrate usage of
        [NewCredentials](https://docs.aws.amazon.com/sdk-for-go/api/aws/credentials/processcreds/#NewCredentials),
        [NewCredentialsCommand](https://docs.aws.amazon.com/sdk-for-go/api/aws/credentials/processcreds/#NewCredentialsCommand),
        and
        [NewCredentialsTimeout](https://docs.aws.amazon.com/sdk-for-go/api/aws/credentials/processcreds/#NewCredentialsTimeout)
        to use
        [NewProvider](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/credentials/processcreds#New)
        or
        

[NewProviderCommand](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/credentials/processcreds#NewProviderCommand).

        The `processcreds` package's
        `NewProvider` function takes a string argument
        that is the command to be executed in the host environment's
        shell, and functional options of
        [Options](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/credentials/processcreds#Options)
        to mutate the credentials provider and override specific
        configuration settings.
      

        `NewProviderCommand` takes an implementation of
        the
        [NewCommandBuilder](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/credentials/processcreds#NewCommandBuilder)
        interface that defines more complex process commands that might
        take one or more command-line arguments, or have certain
        execution environment requirements.
        

[DefaultNewCommandBuilder](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/credentials/processcreds#DefaultNewCommandBuilder)implements this interface, and defines a command builder for a process that requires multiple command-line arguments.

#### Example

```
// V1
import "github.com/aws/aws-sdk-go/aws/credentials/processcreds"
// ...
appCreds := processcreds.NewCredentials("/path/to/command")
value, err := appCreds.Get()
if err != nil {
    // handle error
}
```
```
// V2
import "context"
import "github.com/aws/aws-sdk-go-v2/aws"
import "github.com/aws/aws-sdk-go-v2/credentials/processcreds"
// ...
appCreds := aws.NewCredentialsCache(processcreds.NewProvider("/path/to/command"))
value, err := appCreds.Retrieve(context.TODO())
if err != nil {
    // handle error
}
```
### AWS Security Token Service Credentials

#### AssumeRole

          You must migrate usage of
          [NewCredentials](https://docs.aws.amazon.com/sdk-for-go/api/aws/credentials/stscreds/#NewCredentials),
          and
          [NewCredentialsWithClient](https://docs.aws.amazon.com/sdk-for-go/api/aws/credentials/stscreds/#NewCredentialsWithClient)
          to use
          [NewAssumeRoleProvider](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/credentials/stscreds#NewAssumeRoleProvider).
        

          The `stscreds` package's
          `NewAssumeRoleProvider` function must be
          called with a
          [sts.Client](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/sts#Client),
          and the AWS Identity and Access Management Role ARN to be assumed
          from the provided 

`sts.Client`'s configured
          credentials. You can also provide a set of functional options
          of
          [AssumeRoleOptions](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/credentials/stscreds#AssumeRoleOptions)to modify other optional settings of the provider.

##### Example

```
// V1
import "github.com/aws/aws-sdk-go/aws/credentials/stscreds"
// ...
appCreds := stscreds.NewCredentials(sess, "arn:aws:iam::123456789012:role/demo")
value, err := appCreds.Get()
if err != nil {
    // handle error
}
```
```
// V2
import "context"
import "github.com/aws/aws-sdk-go-v2/credentials/stscreds"
import "github.com/aws/aws-sdk-go-v2/service/sts"
// ...
client := sts.NewFromConfig(cfg)
appCreds := stscreds.NewAssumeRoleProvider(client, "arn:aws:iam::123456789012:role/demo")
value, err := appCreds.Retrieve(context.TODO())
if err != nil {
    // handle error
}
```
#### AssumeRoleWithWebIdentity

          You must migrate usage of
          [NewWebIdentityCredentials](https://docs.aws.amazon.com/sdk-for-go/api/aws/credentials/stscreds/#NewWebIdentityCredentials),
          [NewWebIdentityRoleProvider](https://docs.aws.amazon.com/sdk-for-go/api/aws/credentials/stscreds/#NewWebIdentityRoleProvider),
          and
          [NewWebIdentityRoleProviderWithToken](https://docs.aws.amazon.com/sdk-for-go/api/aws/credentials/stscreds/#NewWebIdentityRoleProviderWithToken)
          to use
          [NewWebIdentityRoleProvider](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/credentials/stscreds#NewWebIdentityRoleProvider).
        

          The `stscreds` package's
          `NewWebIdentityRoleProvider` function must be
          called with a
          [sts.Client](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/sts#Client),
          and the AWS Identity and Access Management Role ARN to be assumed using the
          provided 

`sts.Client`'s configured
          credentials, and an implementation of a
          [IdentityTokenRetriever](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/credentials/stscreds#IdentityTokenRetriever)for providing the OAuth 2.0 or OpenID Connect ID token.

[IdentityTokenFile](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/credentials/stscreds#IdentityTokenFile)is an

`IdentityTokenRetriever` that can be
          used to provide the web identity token from a file located on
          the application's host file-system. You can also provide a set
          of functional options of
          [WebIdentityRoleOptions](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/credentials/stscreds#WebIdentityRoleOptions)to modify other optional settings for the provider.

##### Example

```
// V1
import "github.com/aws/aws-sdk-go/aws/credentials/stscreds"
// ...
appCreds := stscreds.NewWebIdentityRoleProvider(sess, "arn:aws:iam::123456789012:role/demo", "sessionName", "/path/to/token")
value, err := appCreds.Get()
if err != nil {
    // handle error
}
```
```
// V2
import "context"
import "github.com/aws/aws-sdk-go-v2/aws"
import "github.com/aws/aws-sdk-go-v2/credentials/stscreds"
import "github.com/aws/aws-sdk-go-v2/service/sts"
// ...
client := sts.NewFromConfig(cfg)
appCreds := aws.NewCredentialsCache(stscreds.NewWebIdentityRoleProvider(
        client,
        "arn:aws:iam::123456789012:role/demo",
        stscreds.IdentityTokenFile("/path/to/file"),
        func(o *stscreds.WebIdentityRoleOptions) {
            o.RoleSessionName = "sessionName"
        }))
value, err := appCreds.Retrieve(context.TODO())
if err != nil {
    // handle error
}
```
## Service Clients

    
    
      AWS SDK for Go provides service client modules nested under
      the `github.com/aws/aws-sdk-go-v2/service` import
      path. Each service client is contained in a Go package using each
      service's unique identifier. The following table provides some
      examples of service import paths in the AWS SDK for Go.
    

| Service Name | V1 Import Path | V2 Import Path | 
|---|---|---|
| Amazon S3 | `github.com/aws/aws-sdk-go/service/s3` | `github.com/aws/aws-sdk-go-v2/service/s3` | 
| Amazon DynamoDB | `github.com/aws/aws-sdk-go/service/dynamodb` | `github.com/aws/aws-sdk-go-v2/service/dynamodb` | 
| Amazon CloudWatch Logs | `github.com/aws/aws-sdk-go/service/cloudwatchlogs` | `github.com/aws/aws-sdk-go-v2/service/cloudwatchlogs` | 

      Each service client package is an independently versioned Go
      module. To add the service client as a dependency of your
      application, use the `go get` command with the
      service's import path. For example, to add the Amazon S3 client to
      your dependencies use
    

`go get github.com/aws/aws-sdk-go-v2/service/s3`

### Client Construction

        You can construct clients in the AWS SDK for Go using
        either the `New` or
        `NewFromConfig` constructor functions in the
        client's package. When migrating from the AWS SDK for Go v1, we
        recommend that you use the `NewFromConfig`
        variant, which will return a new service client using values
        from an `aws.Config`. The
        `aws.Config` value will have been created while
        loading the SDK shared configuration using
        `config.LoadDefaultConfig`. For details on
        creating service clients, see 
        [Use the AWS SDK for Go v2 with AWS services](./use-services.html).
      

#### Example 1

```
// V1
import "github.com/aws/aws-sdk-go/aws/session"
import "github.com/aws/aws-sdk-go/service/s3"
// ...
sess, err := session.NewSession()
if err != nil {
    // handle error
}
client := s3.New(sess)
```
```
// V2
import "context"
import "github.com/aws/aws-sdk-go-v2/config"
import "github.com/aws/aws-sdk-go-v2/service/s3"
// ...
cfg, err := config.LoadDefaultConfig(context.TODO())
if err != nil {
    // handle error
}
client := s3.NewFromConfig(cfg)
```
#### Example 2: Overriding Client Settings

```
// V1
import "github.com/aws/aws-sdk-go/aws"
import "github.com/aws/aws-sdk-go/aws/session"
import "github.com/aws/aws-sdk-go/service/s3"
// ...
sess, err := session.NewSession()
if err != nil {
    // handle error
}
client := s3.New(sess, &aws.Config{
    Region: aws.String("us-west-2"),
})
```
```
// V2
import "context"
import "github.com/aws/aws-sdk-go-v2/config"
import "github.com/aws/aws-sdk-go-v2/service/s3"
// ...
cfg, err := config.LoadDefaultConfig(context.TODO())
if err != nil {
    // handle error
}
client := s3.NewFromConfig(cfg, func(o *s3.Options) {
    o.Region = "us-west-2"
})
```
### Endpoints

        The
        [endpoints](https://docs.aws.amazon.com/sdk-for-go/api/aws/endpoints/)
        package no longer exists in the AWS SDK for Go. Each
        service client now embeds its required AWS endpoint metadata
        within the client package. This reduces the overall binary size
        of compiled applications by no longer including endpoint
        metadata for services not used by your application.
      

        Additionally, each service now exposes its own interface for
        endpoint resolution in `EndpointResolverV2`.
        Each API takes a unique set of parameters for a service
        `EndpointParameters`, the values of which are
        sourced by the SDK from various locations when an operation is
        invoked.
      

        By default, service clients use their configured AWS Region to
        resolve the service endpoint for the target Region. If your
        application requires a custom endpoint, you can specify custom
        behavior on `EndpointResolverV2` field on the
        `aws.Config` structure. If your application
        implements a custom
        [endpoints.Resolver](https://docs.aws.amazon.com/sdk-for-go/api/aws/endpoints/#Resolver)
        you must migrate it to conform to this new per-service
        interface.
      

        For more information on endpoints and implementing a custom
        resolver, see [Configure Client Endpoints](./configure-endpoints.html).
      

### Authentication

The AWS SDK for Go supports more advanced authentication behavior, which enables the use of newer AWS service features such as codecatalyst and S3 Express One Zone. Additionally, this behavior can be customized on a per-client basis.

### Invoking API Operations

        The number of service client operation methods have been reduced
        significantly. The
        `<OperationName>Request`,
        `<OperationName>WithContext`, and
        `<OperationName>` methods have all been
        consolidated into single operation method,
        `<OperationName>`.
      

#### Example

The following example shows how calls to the Amazon S3 PutObject operation would be migrated from AWS SDK for Go v1 to v2.

```
// V1
import "context"
import "github.com/aws/aws-sdk-go/service/s3"
// ...
client := s3.New(sess)
// Pattern 1
output, err := client.PutObject(&s3.PutObjectInput{
    // input parameters
})
// Pattern 2
output, err := client.PutObjectWithContext(context.TODO(), &s3.PutObjectInput{
    // input parameters
})
// Pattern 3
req, output := client.PutObjectRequest(context.TODO(), &s3.PutObjectInput{
    // input parameters
})
err := req.Send()
```
```
// V2
import "context"
import "github.com/aws/aws-sdk-go-v2/service/s3"
// ...
client := s3.NewFromConfig(cfg)
output, err := client.PutObject(context.TODO(), &s3.PutObjectInput{
    // input parameters
})
```
### Service Data Types

        The top-level input and output types of an operation are found
        in the service client package. The input and output type for a
        given operation follow the pattern of
        `<OperationName>Input` and
        `<OperationName>Output`, where
        `OperationName` is the name of the operation
        you are invoking. For example, the input and output shape for the
        Amazon S3 PutObject operation are
        [PutObjectInput](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/s3#PutObjectInput)
        and
        

[PutObjectOutput](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/s3#PutObjectOutput)respectively.

        All other service data types, other than input and output types,
        have been migrated to the `types` package
        located under the service client package import path hierarchy.
        For example, the
        [s3.AccessControlPolicy](https://docs.aws.amazon.com/sdk-for-go/api/service/s3/#AccessControlPolicy)
        type is now located at
        [types.AccessControlPolicy](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/s3/types#AccessControlPolicy).
      

#### Enumeration Values

          The SDK now provides a typed experience for all API
          enumeration fields. Rather than using a string literal value
          copied from the service API reference documentation, you can
          now use one of the concrete types found in the service
          client's `types` package. For example, you
          can provide the Amazon S3 PutObjectInput operation with an ACL
          to be applied on an object. In the AWS SDK for Go v1, this
          parameter was a `*string` type. In the
          AWS SDK for Go, this parameter is now a
          [types.ObjectCannedACL](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/s3/types#ObjectCannedACL).
          The 

`types` package provides generated
          constants for the valid enumeration values that can be
          assigned to this field. For example
          [types.ObjectCannedACLPrivate](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/s3/types#ObjectCannedACLPrivate)is the constant for the "private" canned ACL value. This value can be used in place of managing string constants within your application.

### Pointer Parameters

        The AWS SDK for Go v1 required pointer references to be passed
        for all input parameters to service operations. The AWS SDK for Go v2
        has simplified the experience with most services by
        removing the need to pass input values as pointers where
        possible. This change means that many service clients operations
        no longer require your application to pass pointer references
        for the following types: `uint8`,
        `uint16`, `uint32`,
        `int8`, `int16`,
        `int32`, `float32`,
        `float64`, `bool`. Similarly,
        slice and map element types have been updated accordingly to
        reflect whether their elements must be passed as pointer
        references.
      

        The
        [aws](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/aws)
        package contains helper functions for creating pointers for the
        Go built-in types, these helpers should be used to more easily
        handle creating pointer types for these Go types. Similarly,
        helper methods are provided for safely de-referencing pointer
        values for these types. For example, the
        

[aws.String](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/aws#String)function converts from

`string` ⇒
        `*string`. Inversely, the
        [aws.ToString](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/aws#ToString)converts from

`*string` ⇒
        `string`. When upgrading your application from
        AWS SDK for Go v1 to v2, you must migrate
        usage of the helpers for converting from the pointer types to
        the non-pointer variants. For example,
        [aws.StringValue](https://docs.aws.amazon.com/sdk-for-go/api/aws/#StringValue)must be updated to

`aws.ToString`.
      ### Errors Types

        The AWS SDK for Go takes full advantage of the error
        wrapping functionality
        [introduced
        in Go 1.13](https://go.dev/blog/go1.13-errors). Services that model error responses have
        generated types available in their client's
        

`types` package that can be used to test
        whether a client operation error was caused by one of these
        types. For example, Amazon S3 `GetObject`
        operation can return a `NoSuchKey` error if
        attempting to retrieve an object key that doesn't exist. You can
        use
        [errors.As](https://pkg.go.dev/errors#As)to test whether the returned operation error is a

[types.NoSuchKey](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/s3/types#NoSuchKey)error. In the event a service does not model a specific type for an error, you can utilize the

[smithy.APIError](https://pkg.go.dev/github.com/aws/smithy-go#APIError)interface type for inspecting the returned error code and message from the service. This functionality replaces

[awserr.Error](https://docs.aws.amazon.com/sdk-for-go/api/aws/awserr//#Error)and the other

[awserr](https://docs.aws.amazon.com/sdk-for-go/api/aws/awserr/)functionality from the AWS SDK for Go v1. For more details information on handling errors, see

[Handling Errors in the AWS SDK for Go V2](./handle-errors.html).

#### Example

```
// V1
import "github.com/aws/aws-sdk-go/aws/awserr"
import "github.com/aws/aws-sdk-go/service/s3"
// ...
client := s3.New(sess)
output, err := s3.GetObject(&s3.GetObjectInput{
    // input parameters
})
if err != nil {
    if awsErr, ok := err.(awserr.Error); ok {
        if awsErr.Code() == "NoSuchKey" {
            // handle NoSuchKey
        } else {
            // handle other codes
        }
        return
    }
    // handle a error
}
```
```
// V2
import "context"
import "github.com/aws/aws-sdk-go-v2/service/s3"
import "github.com/aws/aws-sdk-go-v2/service/s3/types"
import "github.com/aws/smithy-go"
// ...
client := s3.NewFromConfig(cfg)
output, err := client.GetObject(context.TODO(), &s3.GetObjectInput{
    // input parameters
})
if err != nil {
    var nsk *types.NoSuchKey
    if errors.As(err, &nsk) {
        // handle NoSuchKey error
        return
    }
    var apiErr smithy.APIError
    if errors.As(err, &apiErr) {
        code := apiErr.ErrorCode()
        message := apiErr.ErrorMessage()
        // handle error code
        return
    }
    // handle error
    return
}
```
### Paginators

        Service operation paginators are no longer invoked as methods on
        the service client. To use a paginator for an operation you must
        construct a paginator for an operation using one of the
        paginator constructor methods. For example, to use paginate over
        the Amazon S3 `ListObjectsV2` operation you must
        construct its paginator using the
        [s3.NewListObjectsV2Paginator](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/s3#NewListObjectsV2Paginator).
        This constructor returns a
        

[ListObjectsV2Paginator](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/s3#ListObjectsV2Paginator)which provides the methods

`HasMorePages`, and
        `NextPage` for determining whether there are
        more pages to retrieve and invoking the operation to retrieve
        the next page respectively. More details on using the SDK
        paginators can be found at [Using Operation Paginators](./using.html#using-operation-paginators).

Let's look at an example of how to migrate from a AWS SDK for Go v1 paginator to the AWS SDK for Go v2 equivalent.

#### Example

```
// V1
import "fmt"
import "github.com/aws/aws-sdk-go/service/s3"
// ...
client := s3.New(sess)
params := &s3.ListObjectsV2Input{
    // input parameters
}
totalObjects := 0
err := client.ListObjectsV2Pages(params, func(output *s3.ListObjectsV2Output, lastPage bool) bool {
    totalObjects += len(output.Contents)
    return !lastPage
})
if err != nil {
    // handle error
}
fmt.Println("total objects:", totalObjects)
```
```
// V2
import "context"
import "fmt"
import "github.com/aws/aws-sdk-go-v2/service/s3"
// ...
client := s3.NewFromConfig(cfg)
params := &s3.ListObjectsV2Input{
    // input parameters
}
totalObjects := 0
paginator := s3.NewListObjectsV2Paginator(client, params)
for paginator.HasMorePages() {
    output, err := paginator.NextPage(context.TODO())
    if err != nil {
        // handle error
    }
    totalObjects += len(output.Contents)
}
fmt.Println("total objects:", totalObjects)
```
### Waiters

        Service operation waiters are no longer invoked as methods on
        the service client. To use a waiter you first construct the
        desired waiter type, and then invoke the wait method. For
        example, to wait for a Amazon S3 Bucket to exist, you must
        construct a `BucketExists` waiter. Use the
        [s3.NewBucketExistsWaiter](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/s3#NewBucketExistsWaiter)
        constructor to create a
        

[s3.BucketExistsWaiter](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/s3#BucketExistsWaiter). The

`s3.BucketExistsWaiter` provides a
        `Wait` method which can be used to wait for a
        bucket to become available.
      ### Presigned Requests

        The V1 SDK technically supported presigning
        *any* AWS SDK operation, however, this does
        not accurately represent what is actually supported at the
        service level (and in reality most AWS service operations do not
        support presigning).
      

        AWS SDK for Go resolves this by exposing specific
        `PresignClient` implementations in service
        packages with specific APIs for supported presignable
        operations.
      

        **Note: If a service is missing presigning
        support for an operation that you were successfully using in SDK
        v1, please let us know by
         filing
        an issue on GitHub**
      

        Uses of
        [Presign](https://docs.aws.amazon.com/sdk-for-go/api/aws/request/#Request.Presign)
        and
        [PresignRequest](https://docs.aws.amazon.com/sdk-for-go/api/aws/request/#Request.PresignRequest)
        must be converted to use service-specific presigning clients.
      

The following example shows how to migrate presigning of an S3 GetObject request:

```
// V1
import (
    "fmt"
    "time"
    "github.com/aws/aws-sdk-go/aws"
    "github.com/aws/aws-sdk-go/aws/session"
    "github.com/aws/aws-sdk-go/service/s3"
)
func main() {
    sess := session.Must(session.NewSessionWithOptions(session.Options{
        SharedConfigState: session.SharedConfigEnable,
    }))
    svc := s3.New(sess)
    req, _ := svc.GetObjectRequest(&s3.GetObjectInput{
        Bucket: aws.String("
```
`amzn-s3-demo-bucket`"),
        Key:    aws.String("`key`"),
    })
    // pattern 1
    url1, err := req.Presign(20 * time.Minute)
    if err != nil {
        panic(err)
    }
    fmt.Println(url1)
    // pattern 2
    url2, header, err := req.PresignRequest(20 * time.Minute)
    if err != nil {
        panic(err)
    }
    fmt.Println(url2, header)
}
```
// V2
import (
    "context"
    "fmt"
    "time"
    "github.com/aws/aws-sdk-go-v2/aws"
    "github.com/aws/aws-sdk-go-v2/config"
    "github.com/aws/aws-sdk-go-v2/service/s3"
)
func main() {
    cfg, err := config.LoadDefaultConfig(context.Background())
    if err != nil {
        panic(err)
    }
    svc := s3.NewPresignClient(s3.NewFromConfig(cfg))
    req, err := svc.PresignGetObject(context.Background(), &s3.GetObjectInput{
        Bucket: aws.String("
```
`amzn-s3-demo-bucket`"),
        Key:    aws.String("`key`"),
    }, func(o *s3.PresignOptions) {
        o.Expires = 20 * time.Minute
    })
    if err != nil {
        panic(err)
    }
    fmt.Println(req.Method, req.URL, req.SignedHeader)
}
## Request customization

    
    
      The monolithic
      [request.Request](https://docs.aws.amazon.com/sdk-for-go/api/aws/request/#Request)
      API has been re-compartmentalized.
    

### Operation input/output

        The opaque `Request` fields
        `Params` and `Data`, which
        hold the operation input and output structures respectively, are
        now accessible within specific middleware phases as
        input/output:
      

        Request handlers which reference
        `Request.Params` and
        `Request.Data` must be migrated to middleware.
      

#### migrating `Params`

        
        ```
// V1
import (
    "github.com/aws/aws-sdk-go/aws"
    "github.com/aws/aws-sdk-go/aws/request"
    "github.com/aws/aws-sdk-go/aws/session"
    "github.com/aws/aws-sdk-go/service/s3"
)
func withPutObjectDefaultACL(acl string) request.Option {
    return func(r *request.Request) {
        in, ok := r.Params.(*s3.PutObjectInput)
        if !ok {
            return
        }
        if in.ACL == nil {
            in.ACL = aws.String(acl)
        }
        r.Params = in
    }
}
func main() {
    sess := session.Must(session.NewSession())
    sess.Handlers.Validate.PushBack(withPutObjectDefaultACL(s3.ObjectCannedACLBucketOwnerFullControl))
    // ...
}
```
```
// V2
import (
    "context"
    "github.com/aws/aws-sdk-go-v2/service/s3"
    "github.com/aws/aws-sdk-go-v2/service/s3/types"
    "github.com/aws/smithy-go/middleware"
    smithyhttp "github.com/aws/smithy-go/transport/http"
)
type withPutObjectDefaultACL struct {
    acl types.ObjectCannedACL
}
// implements middleware.InitializeMiddleware, which runs BEFORE a request has
// been serialized and can act on the operation input
var _ middleware.InitializeMiddleware = (*withPutObjectDefaultACL)(nil)
func (*withPutObjectDefaultACL) ID() string {
    return "withPutObjectDefaultACL"
}
func (m *withPutObjectDefaultACL) HandleInitialize(ctx context.Context, in middleware.InitializeInput, next middleware.InitializeHandler) (
    out middleware.InitializeOutput, metadata middleware.Metadata, err error,
) {
    input, ok := in.Parameters.(*s3.PutObjectInput)
    if !ok {
        return next.HandleInitialize(ctx, in)
    }
    if len(input.ACL) == 0 {
        input.ACL = m.acl
    }
    in.Parameters = input
    return next.HandleInitialize(ctx, in)
}
// create a helper function to simplify instrumentation of our middleware
func WithPutObjectDefaultACL(acl types.ObjectCannedACL) func (*s3.Options) {
    return func(o *s3.Options) {
        o.APIOptions = append(o.APIOptions, func (s *middleware.Stack) error {
            return s.Initialize.Add(&withPutObjectDefaultACL{acl: acl}, middleware.After)
        })
    }
}
func main() {
    cfg, err := config.LoadDefaultConfig(context.Background())
    if err != nil {
        // ...
    }
    svc := s3.NewFromConfig(cfg, WithPutObjectDefaultACL(types.ObjectCannedACLBucketOwnerFullControl))
    // ...
}
```
#### migrating `Data`

        
        ```
// V1
import (
    "github.com/aws/aws-sdk-go/aws"
    "github.com/aws/aws-sdk-go/aws/request"
    "github.com/aws/aws-sdk-go/aws/session"
    "github.com/aws/aws-sdk-go/service/s3"
)
func readPutObjectOutput(r *request.Request) {
        output, ok := r.Data.(*s3.PutObjectOutput)
        if !ok {
            return
        }
        // ...
    }
}
func main() {
    sess := session.Must(session.NewSession())
    sess.Handlers.Unmarshal.PushBack(readPutObjectOutput)
    svc := s3.New(sess)
    // ...
}
```
```
// V2
import (
    "context"
    "github.com/aws/aws-sdk-go-v2/config"
    "github.com/aws/aws-sdk-go-v2/service/s3"
    "github.com/aws/smithy-go/middleware"
    smithyhttp "github.com/aws/smithy-go/transport/http"
)
type readPutObjectOutput struct{}
var _ middleware.DeserializeMiddleware = (*readPutObjectOutput)(nil)
func (*readPutObjectOutput) ID() string {
    return "readPutObjectOutput"
}
func (*readPutObjectOutput) HandleDeserialize(ctx context.Context, in middleware.DeserializeInput, next middleware.DeserializeHandler) (
    out middleware.DeserializeOutput, metadata middleware.Metadata, err error,
) {
    out, metadata, err = next.HandleDeserialize(ctx, in)
    if err != nil {
        // ...
    }
    output, ok := in.Parameters.(*s3.PutObjectOutput)
    if !ok {
        return out, metadata, err
    }
    // inspect output...
    return out, metadata, err
}
func WithReadPutObjectOutput(o *s3.Options) {
    o.APIOptions = append(o.APIOptions, func (s *middleware.Stack) error {
        return s.Initialize.Add(&withReadPutObjectOutput{}, middleware.Before)
    })
}
func main() {
    cfg, err := config.LoadDefaultConfig(context.Background())
    if err != nil {
        // ...
    }
    svc := s3.NewFromConfig(cfg, WithReadPutObjectOutput)
    // ...
}
```
### HTTP request/response

        The `HTTPRequest` and
        `HTTPResponse` fields from
        `Request` are now exposed in specific
        middleware phases. Since middleware is transport-agnostic, you
        must perform a type assertion on the middleware input or output
        to reveal the underlying HTTP request or response.
      

        Request handlers which reference
        `Request.HTTPRequest` and
        `Request.HTTPResponse` must be migrated to
        middleware.
      

#### migrating `HTTPRequest`

        
        ```
// V1
import (
    "github.com/aws/aws-sdk-go/aws/request"
    "github.com/aws/aws-sdk-go/aws/session"
)
func withHeader(header, val string) request.Option {
    return func(r *request.Request) {
        request.HTTPRequest.Header.Set(header, val)
    }
}
func main() {
    sess := session.Must(session.NewSession())
    sess.Handlers.Build.PushBack(withHeader("x-user-header", "..."))
    svc := s3.New(sess)
    // ...
}
```
```
// V2
import (
    "context"
    "fmt"
    "github.com/aws/aws-sdk-go-v2/config"
    "github.com/aws/aws-sdk-go-v2/service/s3"
    "github.com/aws/smithy-go/middleware"
    smithyhttp "github.com/aws/smithy-go/transport/http"
)
type withHeader struct {
    header, val string
}
// implements middleware.BuildMiddleware, which runs AFTER a request has been
// serialized and can operate on the transport request
var _ middleware.BuildMiddleware = (*withHeader)(nil)
func (*withHeader) ID() string {
    return "withHeader"
}
func (m *withHeader) HandleBuild(ctx context.Context, in middleware.BuildInput, next middleware.BuildHandler) (
    out middleware.BuildOutput, metadata middleware.Metadata, err error,
) {
    req, ok := in.Request.(*smithyhttp.Request)
    if !ok {
        return out, metadata, fmt.Errorf("unrecognized transport type %T", in.Request)
    }
    req.Header.Set(m.header, m.val)
    return next.HandleBuild(ctx, in)
}
func WithHeader(header, val string) func (*s3.Options) {
    return func(o *s3.Options) {
        o.APIOptions = append(o.APIOptions, func (s *middleware.Stack) error {
            return s.Build.Add(&withHeader{
                header: header,
                val: val,
            }, middleware.After)
        })
    }
}
func main() {
    cfg, err := config.LoadDefaultConfig(context.Background())
    if err != nil {
        // ...
    }
    svc := s3.NewFromConfig(cfg, WithHeader("x-user-header", "..."))
    // ...
}
```
### Handler phases

SDK v2 middleware phases are the successor to v1 handler phases.

The following table provides a rough mapping of v1 handler phases to their equivalent location within the V2 middleware stack:

| v1 handler name | v2 middleware phase | 
|---|---|
| Validate | Initialize | 
| Build | Serialize | 
| Sign | Finalize | 
| Send | n/a (1) | 
| ValidateResponse | Deserialize | 
| Unmarshal | Deserialize | 
| UnmarshalMetadata | Deserialize | 
| UnmarshalError | Deserialize | 
| Retry | Finalize, after `"Retry"`middleware (2) | 
| AfterRetry | Finalize, before `"Retry"`middleware,
                post-`next.HandleFinalize()`(2,3) | 
| CompleteAttempt | Finalize, end of step | 
| Complete | Initialize, start of step,
                post- `next.HandleInitialize()`(3) | 

        (1) The `Send` phase in v1 is effectively the
        wrapped HTTP client round-trip in v2. This behavior is
        controlled by the `HTTPClient` field on client
        options.
      

        (2) Any middleware after the
        `"Retry"` middleware in the Finalize
        step will be part of the retry loop.
      

(3) The middleware "stack" at operation time is built into a repeatedly-decorated handler function. Each handler is responsible for calling the next one in the chain. This implicitly means that a middleware step can also take action AFTER its next step has been called.

For example, for the Initialize step, which is at the top of the stack, this means Initialize middlewares that take action after calling the next handler effectively operate at the end of the request:

```
// V2
import (
    "context"
    "github.com/aws/smithy-go/middleware"
)
type onComplete struct{}
var _ middleware.InitializeMiddleware = (*onComplete)(nil)
func (*onComplete) ID() string {
    return "onComplete"
}
func (*onComplete) HandleInitialize(ctx context.Context, in middleware.InitializeInput, next middleware.InitializeHandler) (
    out middleware.InitializeOutput, metadata middleware.Metadata, err error,
) {
    out, metadata, err = next.HandleInitialize(ctx, in)
    // the entire operation was invoked above - the deserialized response is
    // available opaquely in out.Result, run post-op actions here...
    return out, metadata, err
}
```
## Features

    
    ### Amazon EC2 Instance Metadata Service

The AWS SDK for Go provides an Amazon EC2 Instance Metadata Service (IMDS) client that you can use to query the local IMDS when executing your application on an Amazon EC2 instance. The IMDS client is a separate Go module that can be added to your application by using

`go get github.com/aws/aws-sdk-go-v2/feature/ec2/imds`

The client constructor and method operations have been updated to match the design of the other SDK service clients.

#### Example

```
// V1
import "github.com/aws/aws-sdk-go/aws/ec2metadata"
// ...
client := ec2metadata.New(sess)
region, err := client.Region()
if err != nil {
    // handle error
}
```
```
// V2
import "context"
import "github.com/aws/aws-sdk-go-v2/feature/ec2/imds"
// ...
client := imds.NewFromConfig(cfg)
region, err := client.GetRegion(context.TODO())
if err != nil {
    // handle error
}
```
### Amazon S3 Transfer Manager

        The Amazon S3 transfer manager is available for managing uploads
        and downloads of objects concurrently. This package is located
        in a Go module outside the service client import path. This
        module can be retrieved by using
        `go get github.com/aws/aws-sdk-go-v2/feature/s3/manager`.
      

        [s3.NewUploader](https://docs.aws.amazon.com/sdk-for-go/api/service/s3/s3manager/#NewUploader)
        and
        [s3.NewUploaderWithClient](https://docs.aws.amazon.com/sdk-for-go/api/service/s3/s3manager/#NewUploaderWithClient)
        have been replaced with the constructor method
        [manager.NewUploader](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/feature/s3/manager#)
        for creating an Upload manager client.
      

        [s3.NewDownloader](https://docs.aws.amazon.com/sdk-for-go/api/service/s3/s3manager/#NewDownloader)
        and
        [s3.NewDownloaderWithClient](https://docs.aws.amazon.com/sdk-for-go/api/service/s3/s3manager/#NewDownloaderWithClient)
        have been replaced with a single constructor method
        [manager.NewDownloader](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/feature/s3/manager#NewDownloader)
        for creating a Download manager client.
      

### Amazon CloudFront Signing Utilities

        The AWS SDK for Go provides Amazon CloudFront signing utilities
        in a Go module outside the service client import path. This
        module can be retrieved by using `go get`.
      

`go get github.com/aws/aws-sdk-go-v2/feature/cloudfront/sign`

### Amazon S3 Encryption Client

        Starting in AWS SDK for Go, the Amazon S3 encryption
        client is a separate module under [AWS Crypto Tools](https://docs.aws.amazon.com/aws-crypto-tools). The latest
        version of the S3 encryption client for Go, 3.x, is now
        available at
        [GitHub](https://github.com/aws/amazon-s3-encryption-client-go).
        This module can be retrieved by using 

`go get`:
      `go get github.com/aws/amazon-s3-encryption-client-go/v3`

        The separate `EncryptionClient`
        ([v1](https://docs.aws.amazon.com/sdk-for-go/api/service/s3/s3crypto/#EncryptionClient),
        [v2](https://docs.aws.amazon.com/sdk-for-go/api/service/s3/s3crypto/#EncryptionClientV2))
        and `DecryptionClient`
        ([v1](https://docs.aws.amazon.com/sdk-for-go/api/service/s3/s3crypto/#DecryptionClient),
        [v2](https://docs.aws.amazon.com/sdk-for-go/api/service/s3/s3crypto/#DecryptionClientV2))
        APIs have been replaced with a single client,
        [S3EncryptionClientV3](https://pkg.go.dev/github.com/aws/amazon-s3-encryption-client-go/v3/client#S3EncryptionClientV3),
        that exposes both encrypt and decrypt functionality.
      

Like other service clients in AWS SDK for Go, the operation APIs have been condensed:

        To learn how to migrate to the 3.x major version of the
        encryption client, see
        [this
        guide](https://docs.aws.amazon.com/amazon-s3-encryption-client/latest/developerguide/go-v3-migration.html).
      

## Service Customizations Changes

    
    ### Amazon S3

        When migrating from AWS SDK for Go v1 to v2, an important change
        to be aware of involves the handling of the
        `SSECustomerKey` used for server-side
        encryption with customer-provided keys (SSE-C). In AWS SDK for Go v1,
        the encoding of the `SSECustomerKey` to Base64
        was handled internally by the SDK. In SDK v2, this automatic
        encoding has been removed, and it is now required to manually
        encode the `SSECustomerKey` to Base64 before
        passing it to the SDK.
      

Example Adjustment:

```
// V1
import (
  "context"
  "encoding/base64"
  "github.com/aws/aws-sdk-go-v2/config"
  "github.com/aws/aws-sdk-go-v2/service/s3"
)
// ... more code
plainTextKey := "12345678901234567890123456789012" // 32 bytes in length
// calculate md5..
_, err = client.PutObjectWithContext(context.Background(), &s3.PutObjectInput{
    Bucket: aws.String("
```
`amzn-s3-demo-bucket`"),
    Key:    aws.String("`your-object-key`"),
    Body:                 strings.NewReader("hello-world"),
    SSECustomerKey:       &plainTextKey,
    SSECustomerKeyMD5:    &base64Md5,
    SSECustomerAlgorithm: aws.String("AES256"),
})
// ... more code
```
// V2
import (
  "github.com/aws/aws-sdk-go/aws"
  "github.com/aws/aws-sdk-go/aws/session"
  "github.com/aws/aws-sdk-go/service/s3"
)
// ... more code
plainTextKey := "12345678901234567890123456789012" // 32 bytes in length
base64EncodedKey := base64.StdEncoding.EncodeToString([]byte(plainTextKey))
// calculate md5..
_, err = client.PutObject(context.Background(), &s3.PutObjectInput{
    Bucket: aws.String("
```
`amzn-s3-demo-bucket`"),
    Key:    aws.String("`your-object-key`"),
    Body:                 strings.NewReader("hello-world"),
    SSECustomerKey:       &base64EncodedKey,
    SSECustomerKeyMD5:    &base64Md5,
    SSECustomerAlgorithm: aws.String("AES256"),
})
// ... more code