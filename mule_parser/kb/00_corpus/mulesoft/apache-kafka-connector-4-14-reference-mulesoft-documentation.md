# Apache Kafka Connector 4.14 Reference | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/kafka-connector/latest/kafka-connector-reference](https://docs.mulesoft.com/kafka-connector/latest/kafka-connector-reference)

---

String

# Apache Kafka Connector 4.14 Reference

Anypoint Connector for Apache Kafka (Apache Kafka Connector) enables you to interact with the Apache Kafka messaging system. It provides seamless integration between your Mule app and an Apache Kafka cluster, using Mule runtime engine (Mule).

| When a Message Listeneror aBatch Message Listeneruses the`MANUAL`acknowledgement mode, you must use aCommitoperation at the end of the flow when the flow finishes successfully (either because there were no errors or because there is anOn Error Continuecomponent in the flow). | 

| Mule server notifications are not supported because the Kafka library used in the connector manages network disruptions internally. | 

## Consumer Configuration

Configuration for consumers for Apache Kafka Connector.

| Name | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | Name for this configuration. Connectors reference the configuration with this name. | x | ||
| 
 | Connection types for this configuration. | x | ||
| 
 | Enumeration, one of 
 | Defines the way that the Kafka Broker instance is notified of the consumption of messages. 
 | 
 | |
| 
 | Number | Time to wait to perform a poll if data is not available in the buffer (fetched). If no value is set, the poll is returned immediately with any records that are currently available in the buffer or else returns empty if there is no data. Must not be negative. | 
 | |
| 
 | Enumeration, one of: 
 | Time unit for the  | 
 | |
| 
 | Number | Time to wait for an operation to finish. If no value is set or a negative value is set, the operation waits forever. | 
 | |
| 
 | Enumeration, one of: 
 | Time unit for the  | 
 | |
| 
 | String | Converts the provided timestamps into  | ||
| 
 | Configures the minimum amount of time that a dynamic configuration instance can remain idle before Mule considers it eligible for expiration. | 

### Consumer Plaintext Connection Type

Use an unauthenticated and non-encrypted connection type.

| Name | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | Array of String | List of servers to bootstrap the connection with the Kafka cluster. This can be a partial list of the available servers. For example,  | x | |
| 
 | String | Default group ID for all the Kafka consumers that use this configuration. | ||
| 
 | Number | Determines the number of consumers the connection initially creates. | 
 | |
| 
 | Number | The maximum delay between invocations of poll() when using consumer group management. This places an upper bound on the amount of time that the consumer can be idle before fetching more records. If poll() is not called before the expiration of this timeout, then the consumer is considered failed and the group rebalances to reassign the partitions to another member. For consumers using a non-null  | 
 | |
| 
 | Enumeration, one of: 
 | Time unit for the  | 
 | |
| 
 | Enumeration, one of: 
 | Controls how to read messages that are written transactionally. 
 Non-transactional messages are returned unconditionally in either mode. Messages are always returned in offset order. Hence, in the  In particular, any messages appearing after messages belonging to ongoing transactions are withheld until the relevant transaction is completed. As a result,  | 
 | |
| 
 | Boolean | Determines whether internal topics matching a subscribed pattern are excluded from the subscription. It is always possible to explicitly subscribe to an internal topic. | 
 | |
| 
 | Enumeration, one of: 
 | Determines what to do when there is no initial offset in Kafka or if the current offset no longer exists on the server, for example, because the data was deleted. 
 | 
 | |
| 
 | Number | Amount of time to wait before attempting to retry a failed request to a given topic partition. This avoids repeatedly sending requests in a tight loop under some failure scenarios. | 
 | |
| 
 | Enumeration, one of: 
 | Time unit for the  | 
 | |
| 
 | Boolean | Automatically check the CRC32 of the records consumed. This ensures that no on-the-wire or on-disk corruption to the messages occurred. This check adds some overhead, so in situations that require extremely high performance, this can be disabled. | 
 | |
| 
 | Number | Size of the TCP receive buffer (SO_RCVBUF) to use when reading data. If the value is  | 
 | |
| 
 | Enumeration, one of: 
 | Unit of measure for the  | 
 | |
| 
 | Number | Size of the TCP send buffer (SO_SNDBUF) to use when sending data. If the value is  | 
 | |
| 
 | Enumeration, one of: 
 | Unit of measure for the  | 
 | |
| 
 | Number | Maximum amount of time the client waits for the response of a request. If the response is not received before the timeout elapses, the client resends the request if necessary, or fails the request if the retries are exhausted. You can override this parameter at the source level. | 
 | |
| 
 | Enumeration, one of: 
 | Time unit for the  | 
 | |
| 
 | Number | Maximum number of records returned on a poll call to the Kafka cluster. You can override this parameter at the source level. | 
 | |
| 
 | Enumeration, one of: 
 | Controls how the client uses DNS lookups. If set to USE_ALL_DNS_IPS then, when the lookup returns multiple IP addresses for a hostname, they attempt to connect before failing the connection. Applies to both bootstrap and advertised servers. If the value is RESOLVE_CANONICAL_BOOTSTRAP_SERVERS_ONLY each entry is resolved and expanded into a list of canonical names. 
 | 
 | |
| 
 | Number | Expected time between heartbeats to the consumer coordinator when using Kafka’s group management facilities. Heartbeats are used to ensure that the consumer’s session stays active and to facilitate rebalancing when new consumers join or leave the group. The value must be set lower than  | 
 | |
| 
 | Enumeration, one of: 
 | Time unit for the  | 
 | |
| 
 | Number | Timeout used to detect consumer failures when using Kafka’s group management facility. The consumer sends periodic heartbeats to indicate its aliveness to the broker. If no heartbeats are received by the broker before the expiration of this session timeout, then the broker removes this consumer from the group and initiates a rebalance. The value must be in the allowable range as configured in the broker configuration by  | 
 | |
| 
 | Enumeration, one of: 
 | Time unit for the  | 
 | |
| 
 | Number | Close idle connections after the number of milliseconds specified by this configuration. | 
 | |
| 
 | Enumeration, one of: 
 | Time unit for the  | 
 | |
| 
 | Object | Additional properties used to customize the Kafka connection. For example: 
 | ||
| 
 | Defines a TLS configuration used by both clients and server sides to secure the communication for the Mule app. The connector automatically sets the  | |||
| 
 | String | Endpoint identification algorithm used by clients to validate the server hostname. The default value is an empty string, which means the endpoint identification algorithm is disabled. Clients, including client connections created by the broker for inter-broker communication, verify that the broker host name matches the host name in the brokers certificate. | ||
| 
 | Array of String | List of subscription regular expressions to which to subscribe. Topics are automatically rebalanced between the topic consumers. | ||
| 
 | Array of  | List of topic-partition pairs to assign. Consumers are not automatically rebalanced. | ||
| 
 | Number | Minimum amount of data the server returns for a fetch request. If insufficient data is available, the request waits for the specified minimum amount of data to accumulate before answering the request. The default setting of  | 
 | |
| 
 | Enumeration, one of: 
 | Unit of measure for the  | 
 | |
| 
 | Number | Maximum amount of data the server returns for a fetch request. Records are fetched in batches by the consumer. If the first record batch in the first non-empty partition of the fetch is larger than this value, the record batch is still returned to ensure that the consumer can make progress. As such, this is not an absolute maximum. The maximum record batch size accepted by the broker is defined using  | 
 | |
| 
 | Enumeration, one of: 
 | Unit of measure for the  | 
 | |
| 
 | Number | Maximum amount of data per partition that the server returns. The consumer fetches records in batches. If the first record batch in the first non-empty partition of the fetch is larger than this limit, the batch is still returned to ensure that the consumer can make progress. The maximum record batch size accepted by the broker is defined using  | 
 | |
| 
 | Enumeration, one of: 
 | Unit of measure for the  | 
 | |
| 
 | Number | Maximum amount of time the server blocks before answering the fetch request if there isn’t sufficient data to immediately satisfy the requirement specified by  | 
 | |
| 
 | Enumeration, one of: 
 | Time unit for the  | 
 | |
| 
 | Configures a reconnection strategy to use when a connector operation fails to connect to an external server. | 

### Consumer Kerberos Connection Type

Use Kerberos configuration files.

| Name | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | Array of String | List of servers to bootstrap the connection with the Kafka cluster. This can be a partial list of the available servers. For example,  | x | |
| 
 | String | Default group ID for all the Kafka consumers that use this configuration. | ||
| 
 | Number | Determines the number of consumers the connection initially creates. | 
 | |
| 
 | Number | The maximum delay between invocations of poll() when using consumer group management. This places an upper bound on the amount of time that the consumer can be idle before fetching more records. If poll() is not called before the expiration of this timeout, then the consumer is considered failed and the group rebalances to reassign the partitions to another member. For consumers using a non-null  | 
 | |
| 
 | Enumeration, one of: 
 | Time unit for the  | 
 | |
| 
 | Enumeration, one of: 
 | Controls how to read messages that are written transactionally. 
 Non-transactional messages are returned unconditionally in either mode. Messages are always returned in offset order. Hence, in the  In particular, any messages appearing after messages belonging to ongoing transactions are withheld until the relevant transaction is completed. As a result,  | 
 | |
| 
 | Boolean | Determines whether internal topics matching a subscribed pattern are excluded from the subscription. It is always possible to explicitly subscribe to an internal topic. | 
 | |
| 
 | Enumeration, one of: 
 | Determines what to do when there is no initial offset in Kafka or if the current offset no longer exists on the server, for example, because the data was deleted. 
 | 
 | |
| 
 | Number | Amount of time to wait before attempting to retry a failed request to a given topic partition. This avoids repeatedly sending requests in a tight loop under some failure scenarios. | 
 | |
| 
 | Enumeration, one of: 
 | Time unit for the  | 
 | |
| 
 | Boolean | Automatically check the CRC32 of the records consumed. This ensures that no on-the-wire or on-disk corruption to the messages occurred. This check adds some overhead, so in situations that require extremely high performance, this can be disabled. | 
 | |
| 
 | Number | Size of the TCP receive buffer (SO_RCVBUF) to use when reading data. If the value is  | 
 | |
| 
 | Enumeration, one of: 
 | Unit of measure for the  | 
 | |
| 
 | Number | Size of the TCP send buffer (SO_SNDBUF) to use when sending data. If the value is  | 
 | |
| 
 | Enumeration, one of: 
 | Unit of measure for the  | 
 | |
| 
 | Number | Maximum amount of time the client waits for the response of a request. If the response is not received before the timeout elapses, the client resends the request if necessary, or fails the request if the retries are exhausted. You can override this parameter at the source level. | 
 | |
| 
 | Enumeration, one of: 
 | Time unit for the  | 
 | |
| 
 | Number | Maximum number of records returned on a poll call to the Kafka cluster. You can override this parameter at the source level. | 
 | |
| 
 | Enumeration, one of: 
 | Controls how the client uses DNS lookups. If set to USE_ALL_DNS_IPS then, when the lookup returns multiple IP addresses for a hostname, they attempt to connect before failing the connection. Applies to both bootstrap and advertised servers. If the value is RESOLVE_CANONICAL_BOOTSTRAP_SERVERS_ONLY each entry is resolved and expanded into a list of canonical names. 
 | 
 | |
| 
 | Number | Expected time between heartbeats to the consumer coordinator when using Kafka’s group management facilities. Heartbeats are used to ensure that the consumer’s session stays active and to facilitate rebalancing when new consumers join or leave the group. The value must be set lower than  | 
 | |
| 
 | Enumeration, one of: 
 | Time unit for the  | 
 | |
| 
 | Number | Timeout used to detect consumer failures when using Kafka’s group management facility. The consumer sends periodic heartbeats to indicate its aliveness to the broker. If no heartbeats are received by the broker before the expiration of this session timeout, then the broker removes this consumer from the group and initiates a rebalance. The value must be in the allowable range as configured in the broker configuration by  | 
 | |
| 
 | Enumeration, one of: 
 | Time unit for the  | 
 | |
| 
 | Number | Close idle connections after the number of milliseconds specified by this configuration. | 
 | |
| 
 | Enumeration, one of: 
 | Time unit for the  | 
 | |
| 
 | Object | Additional properties used to customize the Kafka connection. For example: 
 | ||
| 
 | Defines a TLS configuration used by both clients and server sides to secure the communication for the Mule app. The connector automatically sets the  | |||
| 
 | String | Endpoint identification algorithm used by clients to validate the server hostname. The default value is an empty string, which means the endpoint identification algorithm is disabled. Clients, including client connections created by the broker for inter-broker communication, verify that the broker host name matches the host name in the brokers certificate. | ||
| 
 | Array of String | List of subscription regular expressions to which to subscribe. Topics are automatically rebalanced between the topic consumers. | ||
| 
 | Array of  | List of topic-partition pairs to assign. Consumers are not automatically rebalanced. | ||
| 
 | Number | Minimum amount of data the server returns for a fetch request. If insufficient data is available, the request waits for the specified minimum amount of data to accumulate before answering the request. The default setting of  | 
 | |
| 
 | Enumeration, one of: 
 | Unit of measure for the  | 
 | |
| 
 | Number | Maximum amount of data the server returns for a fetch request. Records are fetched in batches by the consumer. If the first record batch in the first non-empty partition of the fetch is larger than this value, the record batch is still returned to ensure that the consumer can make progress. As such, this is not an absolute maximum. The maximum record batch size accepted by the broker is defined using  | 
 | |
| 
 | Enumeration, one of: 
 | Unit of measure for the  | 
 | |
| 
 | Number | Maximum amount of data per partition that the server returns. The consumer fetches records in batches. If the first record batch in the first non-empty partition of the fetch is larger than this limit, the batch is still returned to ensure that the consumer can make progress. The maximum record batch size accepted by the broker is defined using  | 
 | |
| 
 | Enumeration, one of: 
 | Unit of measure for the  | 
 | |
| 
 | Number | Maximum amount of time the server blocks before answering the fetch request if there isn’t sufficient data to immediately satisfy the requirement specified by  | 
 | |
| 
 | Enumeration, one of: 
 | Time unit for the  | 
 | |
| 
 | String | Entity that is authenticated by a computer system or a network. Principals can be individual people, computers, services, or computational entities such as processes and threads. | x | |
| 
 | String | Kerberos principal name that Kafka runs as. | x | |
| 
 | String | Path to the  | ||
| 
 | Boolean | Set this option to  
 | 
 | |
| 
 | String | Name of the ticket cache that contains the user’s ticket-granting ticket (TGT). If this value is set,  | ||
| 
 | Boolean | Set this option to  | 
 | |
| 
 | String | Set this option to the file name of the keytab to obtain the principal’s secret key. | ||
| 
 | Boolean | Set this option to  | 
 | |
| 
 | Configures a reconnection strategy to use when a connector operation fails to connect to an external server. | 

### Consumer SASL/OAUTHBEARER - Client Credentials Connection Type

OAuth Bearer authentication is a mechanism for authenticating requests using bearer tokens, which are typically used to authenticate users and applications to access resources. Apache Kafka® supports OAuth Bearer authentication for establishing connections securely. Additionally, the connector supports only [RFC6749 standard](https://datatracker.ietf.org/doc/html/rfc6749#section-4.4.3).

For more information, refer to the [Confluent](https://docs.confluent.io/platform/current/security/authentication/sasl/oauthbearer/overview.html) documentation.

| Name | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | Array of String | List of servers to bootstrap the connection with the Kafka cluster. This can be a partial list of the available servers. For example,  | x | |
| 
 | String | The endpoint identification algorithm used by clients to validate server host name. The default value is an empty string, which means it is disabled. Clients including client connections created by the broker for inter-broker communication verify that the broker host name matches the host name in the brokers certificate. | ||
| 
 | String | Default Group ID for all the Kafka Consumers that use this configuration. | ||
| 
 | Number | Determines the number of consumers the connection initially creates. | 1 | |
| 
 | Number | The maximum delay between invocations of poll() when using consumer group management. This places an upper bound on the amount of time that the consumer can be idle before fetching more records. If poll() is not called before the expiration of this timeout, then the consumer is considered failed and the group rebalances to reassign the partitions to another member. For consumers using a non-null  | 60 | |
| 
 | Enumeration, one of: 
 | Determines the time unit for request timeout scalar. This parameter can be overridden at source level. | SECONDS | |
| 
 | Enumeration, one of: 
 | Controls how to read messages that are written transactionally. 
 Non-transactional messages are returned unconditionally in either mode. Messages are always returned in offset order. Hence, in the  In particular, any messages appearing after messages belonging to ongoing transactions are withheld until the relevant transaction is completed. As a result,  | READ_UNCOMMITTED | |
| 
 | Boolean | Whether internal topics matching a subscribed pattern is excluded from the subscription. It is always possible to explicitly subscribe to an internal topic. | true | |
| 
 | Enumeration, one of: 
 | Determines what to do when there is no initial offset in Kafka or if the current offset no longer exists on the server, for example, because the data was deleted. 
 | 
 | |
| 
 | Number | The amount of time to wait before attempting to retry a failed request to a given topic partition. This avoids repeatedly sending requests in a tight loop under some failure scenarios. | 100 | |
| 
 | Enumeration, one of: 
 | Determines the time unit for the reconnect backoff timeout scalar. | MILLISECONDS | |
| 
 | Boolean | Automatically check the CRC32 of the records consumed. This ensures no on-the-wire or on-disk corruption to the messages occurred. This check adds some overhead, so it may be disabled in cases seeking extreme performance. | true | |
| 
 | Number | The size of the TCP receive buffer (SO_RCVBUF) to use when reading data. If the value is -1, the OS default is used. You can override this field at the source level. | 64 | |
| 
 | Enumeration, one of: 
 | The unit of measure for the receive buffer size scalar. You can override this field at the source level. | KB | |
| 
 | Number | The size of the TCP send buffer (SO_SNDBUF) to use when sending data. If the value is -1, the OS default is used. You can override this field at the source level. | 128 | |
| 
 | Enumeration, one of: 
 | The unit of measure for the send buffer size scalar. This parameter can be overridden at source level. | KB | |
| 
 | Number | The configuration controls the maximum amount of time the client waits for the response of a request. If the response is not received before the timeout elapses the client will resend the request if necessary or fail the request if retries are exhausted. This parameter can be overridden at source level. | 30 | |
| 
 | Enumeration, one of: 
 | Determines the time unit for request timeout scalar. This parameter can be overridden at source level. | SECONDS | |
| 
 | Number | The maximum number of records returned on a poll call to the Kafka cluster. This parameter can be overridden at source level. | 500 | |
| 
 | Enumeration, one of: 
 | Controls how the client uses DNS lookups. If set to use_all_dns_ips then, when the lookup returns multiple IP addresses for a hostname, they will all be attempted to connect to before failing the connection. Applies to both bootstrap and advertised servers. If the value is resolve_canonical_bootstrap_servers_only each entry will be resolved and expanded into a list of canonical names. | USE_ALL_DNS_IPS | |
| 
 | Number | The expected time between heartbeats to the consumer coordinator when using Kafka’s group management facilities. Heartbeats are used to ensure that the consumer’s session stays active and to facilitate rebalancing when new consumers join or leave the group. The value must be set lower than session.timeout.ms, but typically should be set no higher than 1/3 of that value. It can be adjusted even lower to control the expected time for normal rebalances. | 3 | |
| 
 | Enumeration, one of: 
 | Determines the time unit for fetch heartbeat interval time scalar. | SECONDS | |
| 
 | Number | The timeout used to detect consumer failures when using Kafka’s group management facility. The consumer sends periodic heartbeats to indicate its liveness to the broker. If no heartbeats are received by the broker before the expiration of this session timeout, then the broker will remove this consumer from the group and initiate a rebalance. Note that the value must be in the allowable range as configured in the broker configuration by group.min.session.timeout.ms and group.max.session.timeout.ms. | 10 | |
| 
 | Enumeration, one of: 
 | Determines the time unit for session timeout scalar. | SECONDS | |
| 
 | Number | Close idle connections after the number of milliseconds specified by this config. | 540 | |
| 
 | Enumeration, one of: 
 | Determines the time unit for connections maximum idle time scalar. | SECONDS | |
| 
 | Object | Additional properties used to customize the Kafka connection. For example: 
 | ||
| 
 | Defines a TLS configuration, which can be used from both the client and server sides to secure communication for the Mule app. The connector will automatically set the 'security.protocol' to use for communication. Valid values are PLAINTEXT / SSL / SASL_PLAINTEXT / SASL_SSL. Default value when no configuration has been provided is PLAINTEXT(or SASL_PLAINTEXT for SASL authentication - kerberos/scram/plain/token). If SSL was configured as protocol on the broker side then the user needs to configure at least the keystore in the 'tls:context' child element of this config and the connector will automatically use SSL(or SASL_SSL for SASL authentication) as 'security.protocol'. | |||
| 
 | Array of String | The list of subscription regular expressions to subscribe to. This topics will be automatically rebalanced between the amount of consumers of the topic. | ||
| 
 | Array of  | The list of topic-partition pairs to assign. Note that there will be no automatic rebalance of the consumers | ||
| 
 | Number | The minimum amount of data the server should return for a fetch request. If insufficient data is available the request waits for that much data to accumulate before answering the request. The default setting of 1 byte means that fetch requests are answered as soon as a single byte of data is available or the fetch request times out waiting for data to arrive. Setting this to something greater than 1 will cause the server to wait for larger amounts of data to accumulate which can improve server throughput a bit at the cost of some additional latency. This parameter can be overridden at source level. | 1 | |
| 
 | Enumeration, one of: 
 | BYTE | ||
| 
 | Number | The maximum amount of data the server should return for a fetch request. Records are fetched in batches by the consumer, and if the first record batch in the first non-empty partition of the fetch is larger than this value, the record batch will still be returned to ensure that the consumer can make progress. As such, this is not an absolute maximum. The maximum record batch size accepted by the broker is defined via message.max.bytes (broker config) or max.message.bytes (topic config). Note that the consumer performs multiple fetches in parallel. This parameter can be overridden at source level. | 1 | |
| 
 | Enumeration, one of: 
 | The unit of measure for the maximum partition fetch size scalar. This parameter can be overridden at source level. | MB | |
| 
 | Number | The maximum amount of data per-partition the server will return. Records are fetched in batches by the consumer. If the first record batch in the first non-empty partition of the fetch is larger than this limit, the batch will still be returned to ensure that the consumer can make progress. The maximum record batch size accepted by the broker is defined via message.max.bytes (broker config) or max.message.bytes (topic config). See fetch.max.bytes for limiting the consumer request size.This parameter can be overridden at source level. | 1 | |
| 
 | Enumeration, one of: 
 | The unit of measure for the maximum partition fetch size scalar. This parameter can be overridden at source level. | MB | |
| 
 | Number | The maximum amount of time the server will block before answering the fetch request if there isn’t sufficient data to immediately satisfy the requirement given by fetch.min.bytes. | 500 | |
| 
 | Enumeration, one of: 
 | Determines the time unit for fetch maximum wait timeout scalar. | MILLISECONDS | |
| 
 | String | Specifies the configuration key used to define the OAuth client ID within the JAAS configuration. | clientId | |
| 
 | String | The value for the Client ID which refers to the unique identifier assigned to the OAuth client, facilitating secure authentication and authorization processes. | x | |
| 
 | String | Specifies the configuration key used to define the OAuth client secret within the JAAS configuration. | clientSecret | |
| 
 | String | The value for the client secret which refers to the confidential authentication credential assigned to the OAuth client. | x | |
| 
 | String | Specifies the configuration key used to define the OAuth token endpoint within the JAAS configuration. | sasl.oauthbearer.token.endpoint.url | |
| 
 | String | Describes the URL where clients can request access tokens from the authentication server. | x | |
| 
 | String | Specifies the configuration key used to define the OAuth scope within the JAAS configuration. | scope | |
| 
 | String | Defines the specific permissions and access rights granted to the client application by the authorization server. | ||
| 
 | String | Specifies the configuration key used to define the OAuth audience within the JAAS configuration. | audience | |
| 
 | String | Comma separated list of one or more target audiences for the access token. | ||
| 
 | Number | Sets the maximum duration, in seconds, for which an access token remains valid. This helps prevent unauthorized access by limiting the access token’s lifespan, ensuring that even if the access token is intercepted, it becomes invalid after a set period, thus enhancing security and enforcing re-authentication. The default value is null (not set). When this field is not configured, the connector uses the actual token expiration time provided by the OAuth server in the token response ( If this value is set longer than the actual token TTL, the token expires at its natural expiration time as provided by the OAuth server, not at the configured maximum. If this value is set to the same value as the actual token TTL, the token expires at the configured time, which happens to match the server’s intended expiration time. | ||
| 
 | String | Unique identifier associated with an authenticated user, often used for authorization decisions and resource access. | ||
| 
 | Enumeration, one of: 
 | Defines whether to include client credentials in the basic authentication header or in the body of the authentication request. | BASIC_AUTHENTICATION_HEADER | |
| 
 | Boolean | Indicates whether this login module must be successfully authenticated for Kafka clients to establish a connection using OAuth 2.0 bearer tokens. | true | |
| 
 | Boolean | Whether to include 'Accept-application/json' header in the authentication request. | true | |
| 
 | Object | Represents a mapping of key-value pairs containing extensions for custom broker OAuth implementations. If you specify a key for the OAuth Extensions field, ensure that the input contains only alphabetic characters and is at least one character long. If you specify a value for OAuth Extensions field, ensure the input contains only printable ASCII characters or whitespace (including space, tab, carriage return, and newline), and the value is at least one character long. You don’t need to include the  | ||
| 
 | Number | Time for which the login refresh thread waits until a certain portion of the credential’s lifespan passes and attempts to refresh it. Acceptable values range from (0.5) 50% to (1.0) 100%, with a default of (0.8) 80% if unspecified. | 0.8 | |
| 
 | Number | The maximum random jitter added to the login refresh thread’s sleep time relative to the credential’s lifespan is between (0) 0% and (0.25) 25%, with a default of (0.05) 5% if unspecified. | 0.05 | |
| 
 | Number | The desired minimum time in seconds for the login refresh thread to wait before refreshing a credential. Legal values are between 0 and 900 (15 minutes). | 60 | |
| 
 | Number | The amount of buffer time in seconds before credential expiration to maintain when refreshing a credential. Legal values are between 0 and 3600 (1 hour). A default value of 300 (5 minutes) is used if no value is specified. | 300 | |
| 
 | Boolean | Indicates whether to use persistent connections: 
 Mule uses persistent connections. 
 Mule closes the connection after the first request completes. | true | |
| 
 | Number | Maximum number of connections to open to the backend. HTTP requests are sent in parallel over multiple connections. Setting this value too high can impact latency and consume additional resources without increasing throughput. By default, the number of connections is unlimited. | -1 | |
| 
 | Number | The number of milliseconds that a connection can remain idle before it is closed. The value of this attribute is only used when persistent connections are enabled. | 30000 | |
| 
 | Boolean | Whether received responses should be streamed, meaning processing continues as soon as all headers are parsed and the body streamed as it arrives. When enabled, the response MUST be eventually read since depending on the configured buffer size it may not fit into memory and processing will stop until space is available. | false | |
| 
 | Number | Size of the buffer that stores the HTTP response, in bytes. By default, the space is not limited. | -1 | |
| 
 | Encapsulates the configurable properties for TCP client socket connections. | |||
| 
 | Configures a proxy for outbound connections. | |||
| 
 | Boolean | Specifies whether to follow redirects or not. | false | |
| 
 | Number | Maximum time that the request element will block the execution of the flow waiting for the HTTP response. | 60000 | |
| 
 | When the application is deployed, a connectivity test is performed on all connectors. If set to true, deployment fails if the test doesn’t pass after exhausting the associated reconnection strategy | 

### Consumer SASL/SCRAM Connection Type

Use Salted Challenge Response Authentication Mechanism (SCRAM) or SASL/SCRAM, a family of SASL mechanisms that addresses the security concerns with traditional mechanisms that perform username and password authentication like PLAIN. Apache Kafka supports SCRAM-SHA-256 and SCRAM-SHA-512.

For more information, refer to the [Confluent](https://docs.confluent.io/platform/current/security/authentication/sasl/scram/overview.html) documentation.

| Name | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | Array of String | List of servers to bootstrap the connection with the Kafka cluster. This can be a partial list of the available servers. For example,  | x | |
| 
 | String | Default group ID for all the Kafka consumers that use this configuration. | ||
| 
 | Number | Determines the number of consumers the connection initially creates. | 
 | |
| 
 | Number | The maximum delay between invocations of poll() when using consumer group management. This places an upper bound on the amount of time that the consumer can be idle before fetching more records. If poll() is not called before the expiration of this timeout, then the consumer is considered failed and the group rebalances to reassign the partitions to another member. For consumers using a non-null  | 
 | |
| 
 | Enumeration, one of: 
 | Time unit for the  | 
 | |
| 
 | Enumeration, one of: 
 | Controls how to read messages that are written transactionally. 
 Non-transactional messages are returned unconditionally in either mode. Messages are always returned in offset order. Hence, in the  In particular, any messages appearing after messages belonging to ongoing transactions are withheld until the relevant transaction is completed. As a result,  | 
 | |
| 
 | Boolean | Determines whether internal topics matching a subscribed pattern are excluded from the subscription. It is always possible to explicitly subscribe to an internal topic. | 
 | |
| 
 | Enumeration, one of: 
 | Determines what to do when there is no initial offset in Kafka or if the current offset no longer exists on the server, for example, because the data was deleted. 
 | 
 | |
| 
 | Number | Amount of time to wait before attempting to retry a failed request to a given topic partition. This avoids repeatedly sending requests in a tight loop under some failure scenarios. | 
 | |
| 
 | Enumeration, one of: 
 | Time unit for the  | 
 | |
| 
 | Boolean | Automatically check the CRC32 of the records consumed. This ensures that no on-the-wire or on-disk corruption to the messages occurred. This check adds some overhead, so in situations that require extremely high performance, this can be disabled. | 
 | |
| 
 | Number | Size of the TCP receive buffer (SO_RCVBUF) to use when reading data. If the value is  | 
 | |
| 
 | Enumeration, one of: 
 | Unit of measure for the  | 
 | |
| 
 | Number | Size of the TCP send buffer (SO_SNDBUF) to use when sending data. If the value is  | 
 | |
| 
 | Enumeration, one of: 
 | Unit of measure for the  | 
 | |
| 
 | Number | Maximum amount of time the client waits for the response of a request. If the response is not received before the timeout elapses, the client resends the request if necessary, or fails the request if the retries are exhausted. You can override this parameter at the source level. | 
 | |
| 
 | Enumeration, one of: 
 | Time unit for the  | 
 | |
| 
 | Number | Maximum number of records returned on a poll call to the Kafka cluster. You can override this parameter at the source level. | 
 | |
| 
 | Enumeration, one of: 
 | Controls how the client uses DNS lookups. If set to USE_ALL_DNS_IPS then, when the lookup returns multiple IP addresses for a hostname, they attempt to connect before failing the connection. Applies to both bootstrap and advertised servers. If the value is RESOLVE_CANONICAL_BOOTSTRAP_SERVERS_ONLY each entry is resolved and expanded into a list of canonical names. 
 | 
 | |
| 
 | Number | Expected time between heartbeats to the consumer coordinator when using Kafka’s group management facilities. Heartbeats are used to ensure that the consumer’s session stays active and to facilitate rebalancing when new consumers join or leave the group. The value must be set lower than  | 
 | |
| 
 | Enumeration, one of: 
 | Time unit for the  | 
 | |
| 
 | Number | Timeout used to detect consumer failures when using Kafka’s group management facility. The consumer sends periodic heartbeats to indicate its aliveness to the broker. If no heartbeats are received by the broker before the expiration of this session timeout, then the broker removes this consumer from the group and initiates a rebalance. The value must be in the allowable range as configured in the broker configuration by  | 
 | |
| 
 | Enumeration, one of: 
 | Time unit for the  | 
 | |
| 
 | Number | Close idle connections after the number of milliseconds specified by this configuration. | 
 | |
| 
 | Enumeration, one of: 
 | Time unit for the  | 
 | |
| 
 | Object | Additional properties used to customize the Kafka connection. For example: 
 | ||
| 
 | Defines a TLS configuration used by both clients and server sides to secure the communication for the Mule app. The connector automatically sets the  | |||
| 
 | String | Endpoint identification algorithm used by clients to validate the server hostname. The default value is an empty string, which means the endpoint identification algorithm is disabled. Clients, including client connections created by the broker for inter-broker communication, verify that the broker host name matches the host name in the brokers certificate. | ||
| 
 | Array of String | List of subscription regular expressions to which to subscribe. Topics are automatically rebalanced between the topic consumers. | ||
| 
 | Array of  | List of topic-partition pairs to assign. Consumers are not automatically rebalanced. | ||
| 
 | Number | Minimum amount of data the server returns for a fetch request. If insufficient data is available, the request waits for the specified minimum amount of data to accumulate before answering the request. The default setting of  | 
 | |
| 
 | Enumeration, one of: 
 | Unit of measure for the  | 
 | |
| 
 | Number | Maximum amount of data the server returns for a fetch request. Records are fetched in batches by the consumer. If the first record batch in the first non-empty partition of the fetch is larger than this value, the record batch is still returned to ensure that the consumer can make progress. As such, this is not an absolute maximum. The maximum record batch size accepted by the broker is defined using  | 
 | |
| 
 | Enumeration, one of: 
 | Unit of measure for the  | 
 | |
| 
 | Number | Maximum amount of data per partition that the server returns. The consumer fetches records in batches. If the first record batch in the first non-empty partition of the fetch is larger than this limit, the batch is still returned to ensure that the consumer can make progress. The maximum record batch size accepted by the broker is defined using  | 
 | |
| 
 | Enumeration, one of: 
 | Unit of measure for the  | 
 | |
| 
 | Number | Maximum amount of time the server blocks before answering the fetch request if there isn’t sufficient data to immediately satisfy the requirement specified by  | 
 | |
| 
 | Enumeration, one of: 
 | Time unit for the  | 
 | |
| 
 | String | Username with which to login. | x | |
| 
 | String | Password with which to login. | x | |
| 
 | Enumeration, one of: 
 | Encryption algorithm used by SCRAM. | x | |
| 
 | Configures a reconnection strategy to use when a connector operation fails to connect to an external server. | 

### Consumer SASL/PLAIN Connection Type

Use SASL authenticated with a username and password.

For more information, refer to the [Confluent](https://docs.confluent.io/platform/current/security/authentication/sasl/plain/overview.html) documentation.

Enable FIPS mode by setting the `com.mulesoft.connectors.allow-registration-of-sasl-security-provider-in-fips=true` flag to true. This adds the `com.sun.security.sasl.Provider` security provider in the FIPS environment.

| Name | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | Array of String | List of servers to bootstrap the connection with the Kafka cluster. This can be a partial list of the available servers. For example,  | x | |
| 
 | String | Default group ID for all the Kafka consumers that use this configuration. | ||
| 
 | Number | Determines the number of consumers the connection initially creates. | 
 | |
| 
 | Number | The maximum delay between invocations of poll() when using consumer group management. This places an upper bound on the amount of time that the consumer can be idle before fetching more records. If poll() is not called before the expiration of this timeout, then the consumer is considered failed and the group rebalances to reassign the partitions to another member. For consumers using a non-null  | 
 | |
| 
 | Enumeration, one of: 
 | Time unit for the  | 
 | |
| 
 | Enumeration, one of: 
 | Controls how to read messages that are written transactionally. 
 Non-transactional messages are returned unconditionally in either mode. Messages are always returned in offset order. Hence, in the  In particular, any messages appearing after messages belonging to ongoing transactions are withheld until the relevant transaction is completed. As a result,  | 
 | |
| 
 | Boolean | Determines whether internal topics matching a subscribed pattern are excluded from the subscription. It is always possible to explicitly subscribe to an internal topic. | 
 | |
| 
 | Enumeration, one of: 
 | Determines what to do when there is no initial offset in Kafka or if the current offset no longer exists on the server, for example, because the data was deleted. 
 | 
 | |
| 
 | Number | Amount of time to wait before attempting to retry a failed request to a given topic partition. This avoids repeatedly sending requests in a tight loop under some failure scenarios. | 
 | |
| 
 | Enumeration, one of: 
 | Time unit for the  | 
 | |
| 
 | Boolean | Automatically check the CRC32 of the records consumed. This ensures that no on-the-wire or on-disk corruption to the messages occurred. This check adds some overhead, so in situations that require extremely high performance, this can be disabled. | 
 | |
| 
 | Number | Size of the TCP receive buffer (SO_RCVBUF) to use when reading data. If the value is  | 
 | |
| 
 | Enumeration, one of: 
 | Unit of measure for the  | 
 | |
| 
 | Number | Size of the TCP send buffer (SO_SNDBUF) to use when sending data. If the value is  | 
 | |
| 
 | Enumeration, one of: 
 | Unit of measure for the  | 
 | |
| 
 | Number | Maximum amount of time the client waits for the response of a request. If the response is not received before the timeout elapses, the client resends the request if necessary, or fails the request if the retries are exhausted. You can override this parameter at the source level. | 
 | |
| 
 | Enumeration, one of: 
 | Time unit for the  | 
 | |
| 
 | Number | Maximum number of records returned on a poll call to the Kafka cluster. You can override this parameter at the source level. | 
 | |
| 
 | Enumeration, one of: 
 | Controls how the client uses DNS lookups. If set to USE_ALL_DNS_IPS then, when the lookup returns multiple IP addresses for a hostname, they attempt to connect before failing the connection. Applies to both bootstrap and advertised servers. If the value is RESOLVE_CANONICAL_BOOTSTRAP_SERVERS_ONLY each entry is resolved and expanded into a list of canonical names. 
 | 
 | |
| 
 | Number | Expected time between heartbeats to the consumer coordinator when using Kafka’s group management facilities. Heartbeats are used to ensure that the consumer’s session stays active and to facilitate rebalancing when new consumers join or leave the group. The value must be set lower than  | 
 | |
| 
 | Enumeration, one of: 
 | Time unit for the  | 
 | |
| 
 | Number | Timeout used to detect consumer failures when using Kafka’s group management facility. The consumer sends periodic heartbeats to indicate its aliveness to the broker. If no heartbeats are received by the broker before the expiration of this session timeout, then the broker removes this consumer from the group and initiates a rebalance. The value must be in the allowable range as configured in the broker configuration by  | 
 | |
| 
 | Enumeration, one of: 
 | Time unit for the  | 
 | |
| 
 | Number | Close idle connections after the number of milliseconds specified by this configuration. | 
 | |
| 
 | Enumeration, one of: 
 | Time unit for the  | 
 | |
| 
 | Object | Additional properties used to customize the Kafka connection. For example: 
 | ||
| 
 | Defines a TLS configuration used by both clients and server sides to secure the communication for the Mule app. The connector automatically sets the  | |||
| 
 | String | Endpoint identification algorithm used by clients to validate the server hostname. The default value is an empty string, which means the endpoint identification algorithm is disabled. Clients, including client connections created by the broker for inter-broker communication, verify that the broker host name matches the host name in the brokers certificate. | ||
| 
 | Array of String | List of subscription regular expressions to which to subscribe. Topics are automatically rebalanced between the topic consumers. | ||
| 
 | Array of  | List of topic-partition pairs to assign. Consumers are not automatically rebalanced. | ||
| 
 | Number | Minimum amount of data the server returns for a fetch request. If insufficient data is available, the request waits for the specified minimum amount of data to accumulate before answering the request. The default setting of  | 
 | |
| 
 | Enumeration, one of: 
 | Unit of measure for the  | 
 | |
| 
 | Number | Maximum amount of data the server returns for a fetch request. Records are fetched in batches by the consumer. If the first record batch in the first non-empty partition of the fetch is larger than this value, the record batch is still returned to ensure that the consumer can make progress. As such, this is not an absolute maximum. The maximum record batch size accepted by the broker is defined using  | 
 | |
| 
 | Enumeration, one of: 
 | Unit of measure for the  | 
 | |
| 
 | Number | Maximum amount of data per partition that the server returns. The consumer fetches records in batches. If the first record batch in the first non-empty partition of the fetch is larger than this limit, the batch is still returned to ensure that the consumer can make progress. The maximum record batch size accepted by the broker is defined using  | 
 | |
| 
 | Enumeration, one of: 
 | Unit of measure for the  | 
 | |
| 
 | Number | Maximum amount of time the server blocks before answering the fetch request if there isn’t sufficient data to immediately satisfy the requirement specified by  | 
 | |
| 
 | Enumeration, one of: 
 | Time unit for the  | 
 | |
| 
 | String | User used by the client to connect to the Kafka broker. | x | |
| 
 | String | Password used by the client to connect to the Kafka broker. | x | |
| 
 | Configures a reconnection strategy to use when a connector operation fails to connect to an external server. | 

### Consumer SASL/TOKEN Connection Type

Use delegation tokens to authenticate to the Kafka cluster.

| Due to security reasons, a delegation token cannot be renewed if the initial authentication uses a delegation token. For more information, refer to [Delegation Token Support for Kafka](https://cwiki.apache.org/confluence/display/KAFKA/KIP-48+Delegation+token+support+for+Kafka). | 

| Name | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | Array of String | List of servers to bootstrap the connection with the Kafka cluster. This can be a partial list of the available servers. For example,  | x | |
| 
 | String | Default group ID for all the Kafka consumers that use this configuration. | ||
| 
 | Number | Determines the number of consumers the connection initially creates. | 
 | |
| 
 | Number | The maximum delay between invocations of poll() when using consumer group management. This places an upper bound on the amount of time that the consumer can be idle before fetching more records. If poll() is not called before the expiration of this timeout, then the consumer is considered failed and the group rebalances to reassign the partitions to another member. For consumers using a non-null  | 
 | |
| 
 | Enumeration, one of: 
 | Time unit for the  | 
 | |
| 
 | Enumeration, one of: 
 | Controls how to read messages that are written transactionally. 
 Non-transactional messages are returned unconditionally in either mode. Messages are always returned in offset order. Hence, in the  In particular, any messages appearing after messages belonging to ongoing transactions are withheld until the relevant transaction is completed. As a result,  | 
 | |
| 
 | Boolean | Determines whether internal topics matching a subscribed pattern are excluded from the subscription. It is always possible to explicitly subscribe to an internal topic. | 
 | |
| 
 | Enumeration, one of: 
 | Determines what to do when there is no initial offset in Kafka or if the current offset no longer exists on the server, for example, because the data was deleted. 
 | 
 | |
| 
 | Number | Amount of time to wait before attempting to retry a failed request to a given topic partition. This avoids repeatedly sending requests in a tight loop under some failure scenarios. | 
 | |
| 
 | Enumeration, one of: 
 | Time unit for the  | 
 | |
| 
 | Boolean | Automatically check the CRC32 of the records consumed. This ensures that no on-the-wire or on-disk corruption to the messages occurred. This check adds some overhead, so in situations that require extremely high performance, this can be disabled. | 
 | |
| 
 | Number | Size of the TCP receive buffer (SO_RCVBUF) to use when reading data. If the value is  | 
 | |
| 
 | Enumeration, one of: 
 | Unit of measure for the  | 
 | |
| 
 | Number | Size of the TCP send buffer (SO_SNDBUF) to use when sending data. If the value is  | 
 | |
| 
 | Enumeration, one of: 
 | Unit of measure for the  | 
 | |
| 
 | Number | Maximum amount of time the client waits for the response of a request. If the response is not received before the timeout elapses, the client resends the request if necessary, or fails the request if the retries are exhausted. You can override this parameter at the source level. | 
 | |
| 
 | Enumeration, one of: 
 | Time unit for the  | 
 | |
| 
 | Number | Maximum number of records returned on a poll call to the Kafka cluster. You can override this parameter at the source level. | 
 | |
| 
 | Enumeration, one of: 
 | Controls how the client uses DNS lookups. If set to USE_ALL_DNS_IPS then, when the lookup returns multiple IP addresses for a hostname, they attempt to connect before failing the connection. Applies to both bootstrap and advertised servers. If the value is RESOLVE_CANONICAL_BOOTSTRAP_SERVERS_ONLY each entry is resolved and expanded into a list of canonical names. 
 | 
 | |
| 
 | Number | Expected time between heartbeats to the consumer coordinator when using Kafka’s group management facilities. Heartbeats are used to ensure that the consumer’s session stays active and to facilitate rebalancing when new consumers join or leave the group. The value must be set lower than  | 
 | |
| 
 | Enumeration, one of: 
 | Time unit for the  | 
 | |
| 
 | Number | Timeout used to detect consumer failures when using Kafka’s group management facility. The consumer sends periodic heartbeats to indicate its aliveness to the broker. If no heartbeats are received by the broker before the expiration of this session timeout, then the broker removes this consumer from the group and initiates a rebalance. The value must be in the allowable range as configured in the broker configuration by  | 
 | |
| 
 | Enumeration, one of: 
 | Time unit for the  | 
 | |
| 
 | Number | Close idle connections after the number of milliseconds specified by this configuration. | 
 | |
| 
 | Enumeration, one of: 
 | Time unit for the  | 
 | |
| 
 | Object | Additional properties used to customize the Kafka connection. For example: 
 | ||
| 
 | Defines a TLS configuration used by both clients and server sides to secure the communication for the Mule app. The connector automatically sets the  | |||
| 
 | String | Endpoint identification algorithm used by clients to validate the server hostname. The default value is an empty string, which means the endpoint identification algorithm is disabled. Clients, including client connections created by the broker for inter-broker communication, verify that the broker host name matches the host name in the brokers certificate. | ||
| 
 | Array of String | List of subscription regular expressions to which to subscribe. Topics are automatically rebalanced between the topic consumers. | ||
| 
 | Array of  | List of topic-partition pairs to assign. Consumers are not automatically rebalanced. | ||
| 
 | Number | Minimum amount of data the server returns for a fetch request. If insufficient data is available, the request waits for the specified minimum amount of data to accumulate before answering the request. The default setting of  | 
 | |
| 
 | Enumeration, one of: 
 | Unit of measure for the  | 
 | |
| 
 | Number | Maximum amount of data the server returns for a fetch request. Records are fetched in batches by the consumer. If the first record batch in the first non-empty partition of the fetch is larger than this value, the record batch is still returned to ensure that the consumer can make progress. As such, this is not an absolute maximum. The maximum record batch size accepted by the broker is defined using  | 
 | |
| 
 | Enumeration, one of: 
 | Unit of measure for the  | 
 | |
| 
 | Number | Maximum amount of data per partition that the server returns. The consumer fetches records in batches. If the first record batch in the first non-empty partition of the fetch is larger than this limit, the batch is still returned to ensure that the consumer can make progress. The maximum record batch size accepted by the broker is defined using  | 
 | |
| 
 | Enumeration, one of: 
 | Unit of measure for the  | 
 | |
| 
 | Number | Maximum amount of time the server blocks before answering the fetch request if there isn’t sufficient data to immediately satisfy the requirement specified by  | 
 | |
| 
 | Enumeration, one of: 
 | Time unit for the  | 
 | |
| 
 | String | ID of the token. | x | |
| 
 | String | Token HMAC. | x | |
| 
 | Enumeration, one of: 
 | Encryption algorithm used by SCRAM. | x | |
| 
 | Configures a reconnection strategy to use when a connector operation fails to connect to an external server. | 

## Producer Configuration

Configuration for producers for Apache Kafka Connector.

| Name | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | String | Name for this configuration. Connectors reference the configuration with this name. | x | |
| 
 | Connection types for this configuration. | x | ||
| 
 | String | Default topic name to use by the producer operations, overridable at the operation’s configuration level. | 
 | |
| 
 | String | Converts the provided timestamps into  | ||
| 
 | Configures the minimum amount of time that a dynamic configuration instance can remain idle before Mule considers it eligible for expiration. | 

### Producer Plaintext Connection Type

Use an unauthenticated and non-encrypted connection type.

| Name | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | Array of String | List of servers to bootstrap the connection with the Kafka cluster. This can be a partial list of the available servers. For example,  | x | |
| 
 | Number | Producer attempts to batch records together into fewer requests whenever multiple records are sent to the same partition. This helps performance on both the client and the server. This configuration controls the default batch size in bytes. No attempt is made to batch records larger than this size. Requests sent to brokers contain multiple batches, one for each partition with the data that is available to send. A small batch size makes batching less common and can reduce throughput (a batch size of  | 
 | |
| 
 | Enumeration, one of: 
 | Unit of measure for the  | 
 | |
| 
 | Number | Total bytes of memory the producer uses to buffer records waiting to send to the server. If records are sent faster than they are delivered to the server, the producer blocks for  | 
 | |
| 
 | Enumeration, one of: 
 | Unit of measure for the  | 
 | |
| 
 | Enumeration, one of: 
 | Controls how the client uses DNS lookups. If set to USE_ALL_DNS_IPS then, when the lookup returns multiple IP addresses for a hostname, they attempt to connect before failing the connection. Applies to both bootstrap and advertised servers. If the value is RESOLVE_CANONICAL_BOOTSTRAP_SERVERS_ONLY each entry is resolved and expanded into a list of canonical names.. 
 | 
 | |
| 
 | Enumeration, one of: 
 | Compression type for all data generated by the producer. The default is  | 
 | |
| 
 | Number | Close idle connections after the specified time is reached. | 
 | |
| 
 | Enumeration, one of: 
 | Time unit for the  | 
 | |
| 
 | Number | Upper limit on the time to report success or failure after a call to  | 
 | |
| 
 | Enumeration, one of: 
 | Time unit for the  | 
 | |
| 
 | Boolean | When set to  | 
 | |
| 
 | Number | Producer groups together any records that arrive in between request transmissions into a single batched request. Normally this occurs only under load when records arrive faster than they are sent out. However, in some circumstances the client might want to reduce the number of requests, even under moderate load.
  | 
 | |
| 
 | Enumeration, one of: 
 | Time unit for the  | 
 | |
| 
 | Number | Controls for how long  | 
 | |
| 
 | Enumeration, one of: 
 | Time unit for the  | 
 | |
| 
 | Number | Maximum number of unacknowledged requests the client sends on a single connection before blocking. If the value is greater than  | 
 | |
| 
 | Number | Maximum size of a request in bytes. This setting limits the number of record batches the producer sends in a single request to avoid sending huge requests. This is also effectively a cap on the maximum record batch size. Note that the server has its own cap on record batch size, which might be different from this. | 
 | |
| 
 | Enumeration, one of: 
 | Unit of measure for the  | 
 | |
| 
 | Enumeration, one of: 
 | Number of acknowledgments the producer requires the leader to receive before considering a request complete. This controls the durability of records that are sent. | 
 | |
| 
 | Number | Size of the TCP receive buffer (SO_RCVBUF) to use when reading data. If the value is  | 
 | |
| 
 | Enumeration, one of: 
 | Unit of measure for the  | 
 | |
| 
 | Number | Setting a value greater than  | 
 | |
| 
 | Number | Amount of time to wait before attempting to retry a failed request to a given topic partition. This avoids repeatedly sending requests in a tight loop under some failure scenarios. | 
 | |
| 
 | Enumeration, one of: 
 | Time unit for the  | 
 | |
| 
 | Number | Size of the TCP send buffer (SO_SNDBUF) to use when sending data. If the value is  | 
 | |
| 
 | Enumeration, one of: 
 | Unit of measure for the  | 
 | |
| 
 | Number | Maximum amount of time the client waits for the response to a request. If the response is not received before the timeout elapses, the client resends the request if necessary or fails the request if retries are exhausted. This value must be larger than  | 
 | |
| 
 | Enumeration, one of: 
 | Time unit for the  | 
 | |
| 
 | Enumeration, one of: 
 | Controls the partitioning strategy. | 
 | |
| 
 | Object | Additional properties used to customize the Kafka connection. For example: 
 | ||
| 
 | Defines a TLS configuration, used by both clients and server sides to secure the communication for the Mule app. The connector automatically sets the  | |||
| 
 | String | Endpoint identification algorithm used by clients to validate the server hostname. The default value is an empty string, which means the endpoint identification algorithm is disabled. Clients, including client connections created by the broker for inter-broker communication, verify that the broker host name matches the host name in the brokers certificate. | ||
| 
 | Configures a reconnection strategy to use when a connector operation fails to connect to an external server. | 

### Producer Kerberos Connection Type

Use Kerberos configuration files.

| Name | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | Array of String | List of servers to bootstrap the connection with the Kafka cluster. This can be a partial list of the available servers. For example,  | x | |
| 
 | Number | Producer attempts to batch records together into fewer requests whenever multiple records are sent to the same partition. This helps performance on both the client and the server. This configuration controls the default batch size in bytes. No attempt is made to batch records larger than this size. Requests sent to brokers contain multiple batches, one for each partition with the data that is available to send. A small batch size makes batching less common and can reduce throughput (a batch size of  | 
 | |
| 
 | Enumeration, one of: 
 | Unit of measure for the  | 
 | |
| 
 | Number | Total bytes of memory the producer uses to buffer records waiting to send to the server. If records are sent faster than they are delivered to the server, the producer blocks for  | 
 | |
| 
 | Enumeration, one of: 
 | Unit of measure for the  | 
 | |
| 
 | Enumeration, one of: 
 | Controls how the client uses DNS lookups. If set to USE_ALL_DNS_IPS then, when the lookup returns multiple IP addresses for a hostname, they attempt to connect before failing the connection. Applies to both bootstrap and advertised servers. If the value is RESOLVE_CANONICAL_BOOTSTRAP_SERVERS_ONLY each entry is resolved and expanded into a list of canonical names. 
 | 
 | |
| 
 | Enumeration, one of: 
 | Compression type for all data generated by the producer. The default is  | 
 | |
| 
 | Number | Close idle connections after the specified time is reached. | 
 | |
| 
 | Enumeration, one of: 
 | Time unit for the  | 
 | |
| 
 | Number | Upper limit on the time to report success or failure after a call to  | 
 | |
| 
 | Enumeration, one of: 
 | Time unit for the  | 
 | |
| 
 | Boolean | When set to  | 
 | |
| 
 | Number | Producer groups together any records that arrive in between request transmissions into a single batched request. Normally this occurs only under load when records arrive faster than they are sent out. However, in some circumstances the client might want to reduce the number of requests, even under moderate load.
  | 
 | |
| 
 | Enumeration, one of: 
 | Time unit for the  | 
 | |
| 
 | Number | Controls for how long  | 
 | |
| 
 | Enumeration, one of: 
 | Time unit for the  | 
 | |
| 
 | Number | Maximum number of unacknowledged requests the client sends on a single connection before blocking. If the value is greater than  | 
 | |
| 
 | Number | Maximum size of a request in bytes. This setting limits the number of record batches the producer sends in a single request to avoid sending huge requests. This is also effectively a cap on the maximum record batch size. Note that the server has its own cap on record batch size, which might be different from this. | 
 | |
| 
 | Enumeration, one of: 
 | Unit of measure for the  | 
 | |
| 
 | Enumeration, one of: 
 | Number of acknowledgments the producer requires the leader to receive before considering a request complete. This controls the durability of records that are sent. | 
 | |
| 
 | Number | Size of the TCP receive buffer (SO_RCVBUF) to use when reading data. If the value is  | 
 | |
| 
 | Enumeration, one of: 
 | Unit of measure for the  | 
 | |
| 
 | Number | Setting a value greater than  | 
 | |
| 
 | Number | Amount of time to wait before attempting to retry a failed request to a given topic partition. This avoids repeatedly sending requests in a tight loop under some failure scenarios. | 
 | |
| 
 | Enumeration, one of: 
 | Time unit for the  | 
 | |
| 
 | Number | Size of the TCP send buffer (SO_SNDBUF) to use when sending data. If the value is  | 
 | |
| 
 | Enumeration, one of: 
 | Unit of measure for the  | 
 | |
| 
 | Number | Maximum amount of time the client waits for the response to a request. If the response is not received before the timeout elapses, the client resends the request if necessary or fails the request if retries are exhausted. This value must be larger than  | 
 | |
| 
 | Enumeration, one of: 
 | Time unit for the  | 
 | |
| 
 | Enumeration, one of: 
 | Controls the partitioning strategy. | 
 | |
| 
 | Object | Additional properties used to customize the Kafka connection. For example: 
 | ||
| 
 | Defines a TLS configuration, used by both clients and server sides to secure the communication for the Mule app. The connector automatically sets the  | |||
| 
 | String | Endpoint identification algorithm used by clients to validate the server hostname. The default value is an empty string, which means the endpoint identification algorithm is disabled. Clients, including client connections created by the broker for inter-broker communication, verify that the broker host name matches the host name in the brokers certificate. | ||
| 
 | String | Entity that is authenticated by a computer system or a network. Principals can be individual people, computers, services, or computational entities such as processes and threads. | x | |
| 
 | String | Kerberos principal name that Kafka runs as. | x | |
| 
 | String | Path to the  | ||
| 
 | Boolean | Set this option to  
 | 
 | |
| 
 | String | Name of the ticket cache that contains the user’s ticket-granting ticket (TGT). If this value is set,  | ||
| 
 | Boolean | Set this option to  | 
 | |
| 
 | String | Set this option to the file name of the keytab to obtain the principal’s secret key. | ||
| 
 | Boolean | Set this option to  | 
 | |
| 
 | Configures a reconnection strategy to use when a connector operation fails to connect to an external server. | 

### Producer SASL/OAUTHBEARER - Client Credentials Connection Type

OAuth Bearer authentication is a mechanism for authenticating requests using bearer tokens, which are typically used to authenticate users and applications to access resources. Apache Kafka® supports OAuth Bearer authentication for establishing connections securely.

For more information, refer to the [Confluent](https://docs.confluent.io/platform/current/security/authentication/sasl/oauthbearer/overview.html) documentation.

| Name | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | Array of String | List of servers to bootstrap the connection with the Kafka cluster. This can be a partial list of the available servers. For example,  | x | |
| 
 | String | The endpoint identification algorithm used by clients to validate server host name. The default value is an empty string, which means it is disabled. Clients including client connections created by the broker for inter-broker communication verify that the broker host name matches the host name in the brokers certificate. | ||
| 
 | Number | The producer attempts to batch records together into fewer requests whenever multiple records are being sent to the same partition. This helps performance on both the client and the server. This configuration controls the default batch size in bytes. No attempt will be made to batch records larger than this size. Requests sent to brokers will contain multiple batches, one for each partition with data available to be sent. A small batch size will make batching less common and may reduce throughput (a batch size of zero will disable batching entirely). A very large batch size may use memory a bit more wastefully as we will always allocate a buffer of the specified batch size in anticipation of additional records. | 16 | |
| 
 | Enumeration, one of: 
 | The unit of measure for the batch size scalar. | KB | |
| 
 | Number | The total bytes of memory the producer can use to buffer records waiting to be sent to the server. If records are sent faster than they can be delivered to the server the producer will block for max.block.ms after which it will throw an exception. This setting should correspond roughly to the total memory the producer will use, but is not a hard bound since not all memory the producer uses is used for buffering. Some additional memory will be used for compression (if compression is enabled) as well as for maintaining in-flight requests. The default value in the Kafka docs is of 33554432 (32MB), but this should be capped to align with expected values for mule instances in cloudhub (v0.1 core) | 1000 | |
| 
 | Enumeration, one of: 
 | The unit of measure for the max request size scalar. | KB | |
| 
 | Enumeration, one of: 
 | Controls how the client uses DNS lookups. If set to use_all_dns_ips then, when the lookup returns multiple IP addresses for a hostname, they will all be attempted to connect to before failing the connection. Applies to both bootstrap and advertised servers. If the value is resolve_canonical_bootstrap_servers_only each entry will be resolved and expanded into a list of canonical names. | USE_ALL_DNS_IPS | |
| 
 | Enumeration, one of: 
 | The compression type for all data generated by the producer. The default is none (i.e. no compression). Valid values are none, gzip, snappy, lz4, or zstd. Compression is of full batches of data, so the efficacy of batching will also impact the compression ratio (more batching means better compression). | NONE | |
| 
 | Number | Close idle connections after the value specified by this config. | 540 | |
| 
 | Enumeration, one of: 
 | Determines the time unit for the connections maximum idle scalar. | SECONDS | |
| 
 | Number | An upper bound on the time to report success or failure after a call to send() returns. This limits the total time that a record will be delayed prior to sending, the time to await acknowledgment from the broker (if expected), and the time allowed for retriable send failures. The producer may report failure to send a record earlier than this config if either an unrecoverable error is encountered, the retries have been exhausted, or the record is added to a batch which reached an earlier delivery expiration deadline. The value of this config should be greater than or equal to the sum of request.timeout.ms and linger.ms. | 120 | |
| 
 | Enumeration, one of: 
 | Determines the time unit for the delivery timeout scalar. | SECONDS | |
| 
 | Boolean | When set to 'true', the producer will ensure that exactly one copy of each message is written in the stream. If 'false', producer retries due to broker failures, etc, may write duplicates of the retried message in the stream. Note that enabling idempotence requires max.in.flight.requests.per.connection to be less than or equal to 5, retries to be greater than 0 and acks must be 'all'. If these values are not explicitly set by the user, suitable values will be chosen. If incompatible values are set, a ConnectionException will be thrown | false | |
| 
 | Number | The producer groups together any records that arrive in between request transmissions into a single batched request. Normally this occurs only under load when records arrive faster than they can be sent out. However in some circumstances the client may want to reduce the number of requests even under moderate load. This setting accomplishes this by adding a small amount of artificial delay?that is, rather than immediately sending out a record the producer waits for up to the given delay to allow other records to be sent so that the sends can be batched together. This can be thought of as analogous to Nagle’s algorithm in TCP. This setting gives the upper bound on the delay for batching: once we get batch.size worth of records for a partition it is sent immediately regardless of this setting, however if we have fewer than this many bytes accumulated for this partition we will 'linger' for the specified time waiting for more records to show up. This setting defaults to 0 (i.e. no delay). Setting linger.ms=5, for example, would have the effect of reducing the number of requests sent but would add up to 5ms of latency to records sent in the absence of load. | 0 | |
| 
 | Enumeration, one of: 
 | Determines the time unit for the linger time scalar. | SECONDS | |
| 
 | Number | The configuration controls how long KafkaProducer.send() and KafkaProducer.partitionsFor() will block.These methods can be blocked either because the buffer is full or metadata unavailable.Blocking in the user-supplied serializers or partitioner will not be counted against this timeout. | 60 | |
| 
 | Enumeration, one of: 
 | Determines the time unit for the maximum block time scalar. | SECONDS | |
| 
 | Number | The maximum number of unacknowledged requests the client will send on a single connection before blocking. Note that if this setting is set to be greater than 1 and there are failed sends, there is a risk of message re-ordering due to retries (i.e., if retries are enabled). | 5 | |
| 
 | Number | The maximum size of a request in bytes. This setting will limit the number of record batches the producer will send in a single request to avoid sending huge requests. This is also effectively a cap on the maximum record batch size. Note that the server has its own cap on record batch size which may be different from this. | 1 | |
| 
 | Enumeration, one of: 
 | The unit of measure for the max request size scalar. | MB | |
| 
 | Enumeration, one of: 
 | The number of acknowledgments the producer requires the leader to have received before considering a request complete. This controls the durability of records that are sent | NONE | |
| 
 | Number | The size of the TCP receive buffer (SO_RCVBUF) to use when reading data. If the value is -1, the OS default will be used. This parameter can be overridden at source level. | 64 | |
| 
 | Enumeration, one of: 
 | The unit of measure for the receive buffer size scalar. This parameter can be overridden at source level. | KB | |
| 
 | Number | Setting a value greater than zero will cause the client to resend any record whose send fails with a potentially transient error. Note that this retry is no different than if the client resent the record upon receiving the error. Allowing retries without setting max.in.flight.requests.per.connection to 1 will potentially change the ordering of records because if two batches are sent to a single partition, and the first fails and is retried but the second succeeds, then the records in the second batch may appear first. Note additionally that produce requests will be failed before the number of retries has been exhausted if the timeout configured by delivery.timeout.ms expires first before successful acknowledgment. Users should generally prefer to leave this config unset and instead use delivery.timeout.ms to control retry behavior. | 1 | |
| 
 | Enumeration, one of: 
 | Determines the time unit for the retry backoff timeout time scalar. | MILLISECONDS | |
| 
 | Number | The amount of time to wait before attempting to retry a failed request to a given topic partition. This avoids repeatedly sending requests in a tight loop under some failure scenarios. | 100 | |
| 
 | Number | The size of the TCP send buffer (SO_SNDBUF) to use when sending data. If the value is -1, the OS default will be used. This parameter can be overridden at source level. | 128 | |
| 
 | Enumeration, one of: 
 | The unit of measure for the send buffer size scalar. This parameter can be overridden at source level. | KB | |
| 
 | Enumeration, one of: 
 | Determines the time unit for the request timeout time scalar. | SECONDS | |
| 
 | Number | The configuration controls the maximum amount of time the client waits for the response of a request. If the response is not received before the timeout elapses the client will resend the request if necessary or fail the request if retries are exhausted. This should be larger than replica.lag.time.max.ms (a broker configuration) to reduce the possibility of message duplication due to unnecessary producer retries. | 30 | |
| 
 | Enumeration, one of: 
 | The configuration controls which partitioning strategy is used when sending messages without providing a key or a partition. | DEFAULT | |
| 
 | Object | Additional properties used to customize the Kafka connection. For example: 
 | ||
| 
 | Defines a TLS configuration, which can be used from both the client and server sides to secure communication for the Mule app. The connector will automatically set the 'security.protocol' to use for communication. Valid values are PLAINTEXT / SSL / SASL_PLAINTEXT / SASL_SSL. Default value when no configuration has been provided is PLAINTEXT(or SASL_PLAINTEXT for SASL authentication - kerberos/scram/plain/token). If SSL was configured as protocol on the broker side then the user needs to configure at least the keystore in the 'tls:context' child element of this config and the connector will automatically use SSL(or SASL_SSL for SASL authentication) as 'security.protocol'. | |||
| 
 | String | Specifies the configuration key used to define the OAuth client ID within the JAAS configuration. | clientId | |
| 
 | String | The value for the Client ID which refers to the unique identifier assigned to the OAuth client, facilitating secure authentication and authorization processes. | x | |
| 
 | String | Specifies the configuration key used to define the OAuth client secret within the JAAS configuration. | clientSecret | |
| 
 | String | The value for the client secret which refers to the confidential authentication credential assigned to the OAuth client. | x | |
| 
 | String | Specifies the configuration key used to define the OAuth token endpoint within the JAAS configuration. | sasl.oauthbearer.token.endpoint.url | |
| 
 | String | Describes the URL where clients can request access tokens from the authentication server. | x | |
| 
 | String | Specifies the configuration key used to define the OAuth scope within the JAAS configuration. | scope | |
| 
 | String | Defines the specific permissions and access rights granted to the client application by the authorization server. | ||
| 
 | String | Specifies the configuration key used to define the OAuth audience within the JAAS configuration. | audience | |
| 
 | String | Comma separated list of one or more target audiences for the access token. | ||
| 
 | Number | Sets the maximum duration, in seconds, for which an access token remains valid. This helps prevent unauthorized access by limiting the access token’s lifespan, ensuring that even if the access token is intercepted, it becomes invalid after a set period, thus enhancing security and enforcing re-authentication. The default value is null (not set). When this field is not configured, the connector uses the actual token expiration time provided by the OAuth server in the token response ( If this value is set longer than the actual token TTL, the token expires at its natural expiration time as provided by the OAuth server, not at the configured maximum. If this value is set to the same value as the actual token TTL, the token expires at the configured time, which happens to match the server’s intended expiration time. | ||
| 
 | String | Unique identifier associated with an authenticated user, often used for authorization decisions and resource access. | ||
| 
 | Enumeration, one of: 
 | Defines whether to include client credentials in the basic authentication header or in the body of the authentication request. | BASIC_AUTHENTICATION_HEADER | |
| 
 | Boolean | Indicates whether this login module must be successfully authenticated for Kafka clients to establish a connection using OAuth 2.0 bearer tokens. | true | |
| 
 | Boolean | Whether to include 'Accept-application/json' header in the authentication request. | true | |
| 
 | Object | Represents a mapping of key-value pairs containing extensions for custom broker OAuth implementations. If you specify a key for the OAuth Extensions field, ensure that the input contains only alphabetic characters and is at least one character long. If you specify a value for OAuth Extensions field, ensure the input contains only printable ASCII characters or whitespace (including space, tab, carriage return, and newline), and the value is at least one character long. You don’t need to include the  | ||
| 
 | Number | Time for which the login refresh thread waits until a certain portion of the credential’s lifespan passes and attempts to refresh it. Acceptable values range from (0.5) 50% to (1.0) 100%, with a default of (0.8) 80% if unspecified. | 0.8 | |
| 
 | Number | The maximum random jitter added to the login refresh thread’s sleep time relative to the credential’s lifespan is between (0) 0% and (0.25) 25%, with a default of (0.05) 5% if unspecified. | 0.05 | |
| 
 | Number | The desired minimum time in seconds for the login refresh thread to wait before refreshing a credential. Legal values are between 0 and 900 (15 minutes). | 60 | |
| 
 | Number | The amount of buffer time in seconds before credential expiration to maintain when refreshing a credential. Legal values are between 0 and 3600 (1 hour). A default value of 300 (5 minutes) is used if no value is specified. | 300 | |
| 
 | Boolean | Indicates whether to use persistent connections: 
 Mule uses persistent connections. 
 Mule closes the connection after the first request completes. | true | |
| 
 | Number | Maximum number of connections to open to the backend. HTTP requests are sent in parallel over multiple connections. Setting this value too high can impact latency and consume additional resources without increasing throughput. By default, the number of connections is unlimited. | -1 | |
| 
 | Number | The number of milliseconds that a connection can remain idle before it is closed. The value of this attribute is only used when persistent connections are enabled. | 30000 | |
| 
 | Boolean | Whether received responses should be streamed, meaning processing continues as soon as all headers are parsed and the body streamed as it arrives. When enabled, the response MUST be eventually read since depending on the configured buffer size it may not fit into memory and processing will stop until space is available. | false | |
| 
 | Number | Size of the buffer that stores the HTTP response, in bytes. By default, the space is not limited. | -1 | |
| 
 | Encapsulates the configurable properties for TCP client socket connections. | |||
| 
 | Configures a proxy for outbound connections. | |||
| 
 | Boolean | Specifies whether to follow redirects or not. | false | |
| 
 | Number | Maximum time that the request element will block the execution of the flow waiting for the HTTP response. | 60000 | |
| 
 | When the application is deployed, a connectivity test is performed on all connectors. If set to true, deployment fails if the test doesn’t pass after exhausting the associated reconnection strategy | 

### Producer SASL/SCRAM Connection Type

Use Salted Challenge Response Authentication Mechanism (SCRAM) or SASL/SCRAM, a family of SASL mechanisms that addresses the security concerns with traditional mechanisms that perform username and password authentication like PLAIN. Apache Kafka supports SCRAM-SHA-256 and SCRAM-SHA-512.

For more information, refer to the [Confluent](https://docs.confluent.io/platform/current/security/authentication/sasl/scram/overview.html) documentation.

| Name | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | Array of String | List of servers to bootstrap the connection with the Kafka cluster. This can be a partial list of the available servers. For example,  | x | |
| 
 | Number | Producer attempts to batch records together into fewer requests whenever multiple records are sent to the same partition. This helps performance on both the client and the server. This configuration controls the default batch size in bytes. No attempt is made to batch records larger than this size. Requests sent to brokers contain multiple batches, one for each partition with the data that is available to send. A small batch size makes batching less common and can reduce throughput (a batch size of  | 
 | |
| 
 | Enumeration, one of: 
 | Unit of measure for the  | 
 | |
| 
 | Number | Total bytes of memory the producer uses to buffer records waiting to send to the server. If records are sent faster than they are delivered to the server, the producer blocks for  | 
 | |
| 
 | Enumeration, one of: 
 | Unit of measure for the  | 
 | |
| 
 | Enumeration, one of: 
 | Controls how the client uses DNS lookups. If set to USE_ALL_DNS_IPS then, when the lookup returns multiple IP addresses for a hostname, they attempt to connect before failing the connection. Applies to both bootstrap and advertised servers. If the value is RESOLVE_CANONICAL_BOOTSTRAP_SERVERS_ONLY each entry is resolved and expanded into a list of canonical names. 
 | 
 | |
| 
 | Enumeration, one of: 
 | Compression type for all data generated by the producer. The default is  | 
 | |
| 
 | Number | Close idle connections after the specified time is reached. | 
 | |
| 
 | Enumeration, one of: 
 | Time unit for the  | 
 | |
| 
 | Number | Upper limit on the time to report success or failure after a call to  | 
 | |
| 
 | Enumeration, one of: 
 | Time unit for the  | 
 | |
| 
 | Boolean | When set to  | 
 | |
| 
 | Number | Producer groups together any records that arrive in between request transmissions into a single batched request. Normally this occurs only under load when records arrive faster than they are sent out. However, in some circumstances the client might want to reduce the number of requests, even under moderate load.
  | 
 | |
| 
 | Enumeration, one of: 
 | Time unit for the  | 
 | |
| 
 | Number | Controls for how long  | 
 | |
| 
 | Enumeration, one of: 
 | Time unit for the  | 
 | |
| 
 | Number | Maximum number of unacknowledged requests the client sends on a single connection before blocking. If the value is greater than  | 
 | |
| 
 | Number | Maximum size of a request in bytes. This setting limits the number of record batches the producer sends in a single request to avoid sending huge requests. This is also effectively a cap on the maximum record batch size. Note that the server has its own cap on record batch size, which might be different from this. | 
 | |
| 
 | Enumeration, one of: 
 | Unit of measure for the  | 
 | |
| 
 | Enumeration, one of: 
 | Number of acknowledgments the producer requires the leader to receive before considering a request complete. This controls the durability of records that are sent. | 
 | |
| 
 | Number | Size of the TCP receive buffer (SO_RCVBUF) to use when reading data. If the value is  | 
 | |
| 
 | Enumeration, one of: 
 | Unit of measure for the  | 
 | |
| 
 | Number | Setting a value greater than  | 
 | |
| 
 | Number | Amount of time to wait before attempting to retry a failed request to a given topic partition. This avoids repeatedly sending requests in a tight loop under some failure scenarios. | 
 | |
| 
 | Enumeration, one of: 
 | Time unit for the  | 
 | |
| 
 | Number | Size of the TCP send buffer (SO_SNDBUF) to use when sending data. If the value is  | 
 | |
| 
 | Enumeration, one of: 
 | Unit of measure for the  | 
 | |
| 
 | Number | Maximum amount of time the client waits for the response to a request. If the response is not received before the timeout elapses, the client resends the request if necessary or fails the request if retries are exhausted. This value must be larger than  | 
 | |
| 
 | Enumeration, one of: 
 | Time unit for the  | 
 | |
| 
 | Enumeration, one of: 
 | Controls the partitioning strategy. | 
 | |
| 
 | Object | Additional properties used to customize the Kafka connection. For example: 
 | ||
| 
 | Defines a TLS configuration, used by both clients and server sides to secure the communication for the Mule app. The connector automatically sets the  | |||
| 
 | String | Endpoint identification algorithm used by clients to validate the server hostname. The default value is an empty string, which means the endpoint identification algorithm is disabled. Clients, including client connections created by the broker for inter-broker communication, verify that the broker host name matches the host name in the brokers certificate. | ||
| 
 | String | Username with which to login. | x | |
| 
 | String | Password with which to login. | x | |
| 
 | Enumeration, one of: 
 | Encryption algorithm used by SCRAM. | x | |
| 
 | Configures a reconnection strategy to use when a connector operation fails to connect to an external server. | 

### Producer SASL/PLAIN Connection Type

Use SASL authenticated with a username and password.

For more information, refer to the [Confluent](https://docs.confluent.io/platform/current/security/authentication/sasl/plain/overview.html) documentation.

| Name | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | Array of String | List of servers to bootstrap the connection with the Kafka cluster. This can be a partial list of the available servers. For example,  | x | |
| 
 | Number | Producer attempts to batch records together into fewer requests whenever multiple records are sent to the same partition. This helps performance on both the client and the server. This configuration controls the default batch size in bytes. No attempt is made to batch records larger than this size. Requests sent to brokers contain multiple batches, one for each partition with the data that is available to send. A small batch size makes batching less common and can reduce throughput (a batch size of zero disables batching entirely). A very large batch size can result in more wasteful use of memory as a buffer of the specified batch size is always allocated in anticipation of additional records. | 
 | |
| 
 | Enumeration, one of: 
 | Unit of measure for the  | 
 | |
| 
 | Number | Total bytes of memory the producer uses to buffer records waiting to send to the server. If records are sent faster than they are delivered to the server, the producer blocks for  | 
 | |
| 
 | Enumeration, one of: 
 | Unit of measure for the  | 
 | |
| 
 | Enumeration, one of: 
 | Controls how the client uses DNS lookups. If set to USE_ALL_DNS_IPS then, when the lookup returns multiple IP addresses for a hostname, they attempt to connect before failing the connection. Applies to both bootstrap and advertised servers. If the value is RESOLVE_CANONICAL_BOOTSTRAP_SERVERS_ONLY each entry is resolved and expanded into a list of canonical names. 
 | 
 | |
| 
 | Enumeration, one of: 
 | Compression type for all data generated by the producer. The default is  | 
 | |
| 
 | Number | Close idle connections after the specified time is reached. | 
 | |
| 
 | Enumeration, one of: 
 | Time unit for the  | 
 | |
| 
 | Number | Upper limit on the time to report success or failure after a call to  | 
 | |
| 
 | Enumeration, one of: 
 | Time unit for the  | 
 | |
| 
 | Boolean | When set to  | 
 | |
| 
 | Number | Producer groups together any records that arrive in between request transmissions into a single batched request. Normally this occurs only under load when records arrive faster than they are sent out. However, in some circumstances the client might want to reduce the number of requests, even under moderate load.
  | 
 | |
| 
 | Enumeration, one of: 
 | Time unit for the  | 
 | |
| 
 | Number | Controls for how long  | 
 | |
| 
 | Enumeration, one of: 
 | Time unit for the  | 
 | |
| 
 | Number | Maximum number of unacknowledged requests the client sends on a single connection before blocking. If the value is greater than  | 
 | |
| 
 | Number | Maximum size of a request in bytes. This setting limits the number of record batches the producer sends in a single request to avoid sending huge requests. This is also effectively a cap on the maximum record batch size. Note that the server has its own cap on record batch size, which might be different from this. | 
 | |
| 
 | Enumeration, one of: 
 | Unit of measure for the  | 
 | |
| 
 | Enumeration, one of: 
 | Number of acknowledgments the producer requires the leader to receive before considering a request complete. This controls the durability of records that are sent. | 
 | |
| 
 | Number | Size of the TCP receive buffer (SO_RCVBUF) to use when reading data. If the value is  | 
 | |
| 
 | Enumeration, one of: 
 | Unit of measure for the  | 
 | |
| 
 | Number | Setting a value greater than  | 
 | |
| 
 | Number | Amount of time to wait before attempting to retry a failed request to a given topic partition. This avoids repeatedly sending requests in a tight loop under some failure scenarios. | 
 | |
| 
 | Enumeration, one of: 
 | Time unit for the  | 
 | |
| 
 | Number | Size of the TCP send buffer (SO_SNDBUF) to use when sending data. If the value is  | 
 | |
| 
 | Enumeration, one of: 
 | Unit of measure for the  | 
 | |
| 
 | Number | Maximum amount of time the client waits for the response to a request. If the response is not received before the timeout elapses, the client resends the request if necessary or fails the request if retries are exhausted. This value must be larger than  | 
 | |
| 
 | Enumeration, one of: 
 | Time unit for the  | 
 | |
| 
 | Enumeration, one of: 
 | Controls the partitioning strategy. | 
 | |
| 
 | Object | Additional properties used to customize the Kafka connection. For example: 
 | ||
| 
 | Defines a TLS configuration, used by both clients and server sides to secure the communication for the Mule app. The connector automatically sets the  | |||
| 
 | String | Endpoint identification algorithm used by clients to validate the server hostname. The default value is an empty string, which means the endpoint identification algorithm is disabled. Clients, including client connections created by the broker for inter-broker communication, verify that the broker host name matches the host name in the brokers certificate. | ||
| 
 | String | Username with which to login. | x | |
| 
 | String | Password with which to login. | x | |
| 
 | Configures a reconnection strategy to use when a connector operation fails to connect to an external server. | 

### Producer SASL/TOKEN Connection Type

Use delegation tokens to authenticate to the Kafka cluster.

| Due to security reasons, a delegation token cannot be renewed if the initial authentication uses a delegation token. For more information, refer to [Delegation Token Support for Kafka](https://cwiki.apache.org/confluence/display/KAFKA/KIP-48+Delegation+token+support+for+Kafka). | 

| Name | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | Array of String | List of servers to bootstrap the connection with the Kafka cluster. This can be a partial list of the available servers. For example,  | x | |
| 
 | Number | Producer attempts to batch records together into fewer requests whenever multiple records are sent to the same partition. This helps performance on both the client and the server. This configuration controls the default batch size in bytes. No attempt is made to batch records larger than this size. Requests sent to brokers contain multiple batches, one for each partition with the data that is available to send. A small batch size makes batching less common and can reduce throughput (a batch size of zero disables batching entirely). A very large batch size can result in more wasteful use of memory as a buffer of the specified batch size is always allocated in anticipation of additional records. | 
 | |
| 
 | Enumeration, one of: 
 | Unit of measure for the  | 
 | |
| 
 | Number | Total bytes of memory the producer uses to buffer records waiting to send to the server. If records are sent faster than they are delivered to the server, the producer blocks for  | 
 | |
| 
 | Enumeration, one of: 
 | Unit of measure for the  | 
 | |
| 
 | Enumeration, one of: 
 | Controls how the client uses DNS lookups. If set to USE_ALL_DNS_IPS then, when the lookup returns multiple IP addresses for a hostname, they attempt to connect before failing the connection. Applies to both bootstrap and advertised servers. If the value is RESOLVE_CANONICAL_BOOTSTRAP_SERVERS_ONLY each entry is resolved and expanded into a list of canonical names. 
 | 
 | |
| 
 | Enumeration, one of: 
 | Compression type for all data generated by the producer. The default is  | 
 | |
| 
 | Number | Close idle connections after the specified time is reached. | 
 | |
| 
 | Enumeration, one of: 
 | Time unit for the  | 
 | |
| 
 | Number | Upper limit on the time to report success or failure after a call to  | 
 | |
| 
 | Enumeration, one of: 
 | Time unit for the  | 
 | |
| 
 | Boolean | When set to  | 
 | |
| 
 | Number | Producer groups together any records that arrive in between request transmissions into a single batched request. Normally this occurs only under load when records arrive faster than they are sent out. However, in some circumstances the client might want to reduce the number of requests, even under moderate load.
  | 
 | |
| 
 | Enumeration, one of: 
 | Time unit for the  | 
 | |
| 
 | Number | Controls for how long  | 
 | |
| 
 | Enumeration, one of: 
 | Time unit for the  | 
 | |
| 
 | Number | Maximum number of unacknowledged requests the client sends on a single connection before blocking. If the value is greater than  | 
 | |
| 
 | Number | Maximum size of a request in bytes. This setting limits the number of record batches the producer sends in a single request to avoid sending huge requests. This is also effectively a cap on the maximum record batch size. Note that the server has its own cap on record batch size, which might be different from this. | 
 | |
| 
 | Enumeration, one of: 
 | Unit of measure for the  | 
 | |
| 
 | Enumeration, one of: 
 | Number of acknowledgments the producer requires the leader to receive before considering a request complete. This controls the durability of records that are sent. | 
 | |
| 
 | Number | Size of the TCP receive buffer (SO_RCVBUF) to use when reading data. If the value is  | 
 | |
| 
 | Enumeration, one of: 
 | Unit of measure for the  | 
 | |
| 
 | Number | Setting a value greater than  | 
 | |
| 
 | Number | Amount of time to wait before attempting to retry a failed request to a given topic partition. This avoids repeatedly sending requests in a tight loop under some failure scenarios. | 
 | |
| 
 | Enumeration, one of: 
 | Time unit for the  | 
 | |
| 
 | Number | Size of the TCP send buffer (SO_SNDBUF) to use when sending data. If the value is  | 
 | |
| 
 | Enumeration, one of: 
 | Unit of measure for the  | 
 | |
| 
 | Number | Maximum amount of time the client waits for the response to a request. If the response is not received before the timeout elapses, the client resends the request if necessary or fails the request if retries are exhausted. This value must be larger than  | 
 | |
| 
 | Enumeration, one of: 
 | Time unit for the  | 
 | |
| 
 | Enumeration, one of: 
 | Controls the partitioning strategy. | 
 | |
| 
 | Object | Additional properties used to customize the Kafka connection. For example: 
 | ||
| 
 | Defines a TLS configuration, used by both clients and server sides to secure the communication for the Mule app. The connector automatically sets the  | |||
| 
 | String | Endpoint identification algorithm used by clients to validate the server hostname. The default value is an empty string, which means the endpoint identification algorithm is disabled. Clients, including client connections created by the broker for inter-broker communication, verify that the broker host name matches the host name in the brokers certificate. | ||
| 
 | String | ID of the token. | x | |
| 
 | String | Token HMAC. | x | |
| 
 | Enumeration, one of: 
 | Encryption algorithm used by SCRAM. | x | |
| 
 | Configures a reconnection strategy to use when a connector operation fails to connect to an external server. | 

## Consumer Sources

### Batch Message Listener

`<kafka:batch-message-listener>`

This source supports the consumption of messages from a Kafka cluster, producing a list of messages to the flow.

| Name | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | String | Name of the configuration to use. | x | |
| 
 | Number | Amount of time to block. Defines the total timeout for polling. | ||
| 
 | Enumeration, one of: 
 | Time unit for the  | ||
| 
 | Enumeration, one of: 
 | Defines the way that the Kafka Broker instance is notified of the consumption of messages. 
 | ||
| 
 | Number | Number of parallel consumers. | 
 | |
| 
 | Boolean | Determines whether to execute this source on only the primary node when running Mule instances in a cluster. | ||
| 
 | Defines a policy for processing the redelivery of the same message. | |||
| 
 | Retry strategy in case of connectivity errors. | 

#### Output

| Type | Array of  | 
| Attributes Type | 

#### Associated Configurations

| The Batch Message Listenersource does not support configurable streaming strategies because the source takes a batch of records as an input stream. The streaming strategy configuration is non-repeatable-stream by default for the source. | 

### Message Listener

`<kafka:message-listener>`

This source supports the consumption of messages from a Kafka cluster, producing a single message to the flow.

| Name | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | String | Name of the configuration to use. | x | |
| 
 | Number | Amount of time to block. Defines the total timeout for polling. | ||
| 
 | Enumeration, one of: 
 | Time unit for the  | ||
| 
 | Enumeration, one of: 
 | Defines the way that the Kafka Broker instance is notified of the consumption of messages. 
 | ||
| 
 | Number | Number of parallel consumers. | 
 | |
| 
 | Boolean | Determines whether to execute this source on only the primary node when running Mule instances in a cluster. | ||
| 
 | 
 | Configures how Mule processes streams. Repeatable streams are the default behavior. | ||
| 
 | Defines a policy for processing the redelivery of the same message. | |||
| 
 | Retry strategy in case of connectivity errors. | 

#### Output

| Type | Binary | 
| Attributes Type | 

#### Associated Configurations

## Consumer Operations

### Commit

`<kafka:commit>`

Commits the offsets associated to a message or batch of messages consumed in a **Message Listener**. This is a list or a single message consumed in the **Batch Message Listener** source.

| Name | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | String | Name of the configuration to use. | x | |
| 
 | String | Commit key of the last poll. This operation is valid only when used inside a flow that uses one of the sources ( | x | |
| 
 | Retry strategy in case of connectivity errors. | 

#### Associated Configurations

#### Throws

- 
KAFKA:SECURITY 
- 
KAFKA:INVALID_ACK_MODE 
- 
KAFKA:RETRY_EXHAUSTED 
- 
KAFKA:ALREADY_COMMITTED 
- 
KAFKA:TIMEOUT 
- 
KAFKA:SESSION_NOT_FOUND 
- 
KAFKA:NOT_FOUND 
- 
KAFKA:CONNECTIVITY 

### Consume

`<kafka:consume>`

Receives messages from one or more Kafka topics. This operation works similarly to the **Message Listener** source, so all the operations that apply to that, apply to this operation as well.

| The Consumeoperation does not return the`consumerCommitKey`. | 

| Name | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | String | Name of the configuration to use. | x | |
| 
 | Number | Number of time units that this operation waits for receiving messages. | ||
| 
 | Enumeration, one of: 
 | Time unit for the  | ||
| 
 | Number | Timeout for the operation to start executing. | ||
| 
 | Enumeration, one of: 
 | Time unit for the  | ||
| 
 | Enumeration, one of: 
 | Defines the way that the Kafka Broker instance is notified of the consumption of messages. 
 | 
 | |
| 
 | 
 | Configures how Mule processes streams. Repeatable streams are the default behavior. | ||
| 
 | String | Name of the variable that stores the operation’s output. | ||
| 
 | String | Expression that evaluates the operation’s output. The outcome of the expression is stored in the  | 
 | |
| 
 | Retry strategy in case of connectivity errors. | 

#### Output

| Type | Binary | 
| Attributes Type | 

#### Associated Configurations

#### Throws

- 
KAFKA:SECURITY 
- 
KAFKA:RETRY_EXHAUSTED 
- 
KAFKA:ILLEGAL_STATE 
- 
KAFKA:TIMEOUT 
- 
KAFKA:SERIALIZATION_ERROR 
- 
KAFKA:INVALID_OFFSET 
- 
KAFKA:INVALID_INPUT 
- 
KAFKA:NOT_FOUND 
- 
KAFKA:CONNECTIVITY 

### Seek

`<kafka:seek>`

Sets the current offset of the consumer for the given topic and partition to the provided offset value.

| Name | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | String | Name of the configuration to use. | x | |
| 
 | String | Name of the topic on which the  | x | |
| 
 | Number | Partition number that has its offset modified. | x | |
| 
 | Number | Offset value to commit for the configured partition. | x | |
| 
 | Number | Timeout for the operation to start executing. | ||
| 
 | Enumeration, one of: 
 | Time unit for the  | ||
| 
 | Retry strategy in case of connectivity errors. | 

#### Associated Configurations

#### Throws

- 
KAFKA:INVALID_TOPIC 
- 
KAFKA:SECURITY 
- 
KAFKA:RETRY_EXHAUSTED 
- 
KAFKA:TIMEOUT 
- 
KAFKA:INVALID_OFFSET 
- 
KAFKA:INVALID_INPUT 
- 
KAFKA:NOT_FOUND 
- 
KAFKA:CONNECTIVITY 

## Producer Operations

### Bulk Publish

`<kafka:bulk-publish>`

Publishes a bulk of messages to the specified Kafka topic, optionally specifying the partition, key, and message content for it. This operation supports transactions.

| Name | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | String | Name of the configuration to use. | x | |
| 
 | Array of  | List of messages to publish. | 
 | |
| 
 | Enumeration, one of: 
 | Type of joining action that operations can take for transactions. | 
 | |
| 
 | String | Name of the variable that stores the operation’s output. | ||
| 
 | String | Expression that evaluates the operation’s output. The outcome of the expression is stored in the  | 
 | |
| 
 | Retry strategy in case of connectivity errors. | 

#### Output

| Type | Array of  | 

#### Associated Configurations

#### Throws

- 
KAFKA:SECURITY 
- 
KAFKA:INVALID_TOPIC_PARTITION 
- 
KAFKA:RETRY_EXHAUSTED 
- 
KAFKA:TIMEOUT 
- 
KAFKA:AUTHENTICATION_ERROR 
- 
KAFKA:INPUT_TOO_LARGE 
- 
KAFKA:CONNECTIVITY 

### Publish

`<kafka:publish>`

Publishes a message to the specified Kafka topic, optionally specifying the partition, key, and message content for it. This operation supports transactions.

| Name | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | String | Name of the configuration to use. | x | |
| 
 | String | Topic to publish to. | ||
| 
 | Number | (Optional) Topic partition. | ||
| 
 | Binary | (Optional) Key for the published message. | ||
| 
 | Binary | (Optional) Message content of the message. | 
 | |
| 
 | Object | (Optional) Headers for the message. | ||
| 
 | Enumeration, one of: 
 | Type of joining action that operations can take for transactions. | 
 | |
| 
 | String | Name of the variable that stores the operation’s output. | ||
| 
 | String | Expression that evaluates the operation’s output. The outcome of the expression is stored in the  | 
 | |
| 
 | Retry strategy in case of connectivity errors. | 

#### Output

| Type | 

#### Associated Configurations

#### Throws

- 
KAFKA:SECURITY 
- 
KAFKA:INVALID_TOPIC_PARTITION 
- 
KAFKA:RETRY_EXHAUSTED 
- 
KAFKA:TIMEOUT 
- 
KAFKA:INPUT_TOO_LARGE 
- 
KAFKA:CONNECTIVITY 

## Object Types

### Consumer Context

Type for the consumer context.

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | String | Consumer commit key. | 

### CRL File

Specifies the location of the certification revocation list (CRL) file.

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | String | Path to the CRL file. | 

### Custom OCSP Responder

Configures a custom OCSP responder for certification revocation checks.

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | String | URL of the OCSP responder. | ||
| 
 | String | Alias of the signing certificate for the OCSP response. If specified, the alias must be in the truststore. | 

### Expiration Policy

Configures an expiration policy strategy.

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | Number | Configures the maximum amount of time that a dynamic configuration instance can remain idle before Mule considers it eligible for expiration. | ||
| 
 | Enumeration, one of: 
 | Time unit for the  | 

### Kafka Message

Represents a Kafka message.

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | Attributes associated with the Kafka message. | |||
| 
 | Binary | Payload of the Kafka message, represented as an InputStream. | 

### Kafka Message Attributes

Represents the attributes of a Kafka message.

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | Object | Headers of the Kafka message, represented as a map in which the key is a string and the value is an InputStream. | ||
| 
 | Binary | Key of the Kafka message, represented as an InputStream. | ||
| 
 | Number | Partition of the topic where the Kafka message is sent. | ||
| 
 | String | Topic to which the Kafka message belongs to. | 

### Kafka Message Metadata

Metadata of the Kafka message.

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | Number | Offset of the message. | ||
| 
 | Number | Partition of the message. | ||
| 
 | Number | Serialized key size of the message. | ||
| 
 | Number | Serialized value size of the message. | ||
| 
 | DateTime | Timestamp of the message. | ||
| 
 | String | Topic of the message. | 

### Kafka Record Attributes

Attributes of the Kafka record.

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | String | Consumer commit key. | ||
| 
 | DateTime | Timestamp of record creation. | ||
| 
 | Object | Map of HTTP headers in the message. | ||
| 
 | Binary | Keys of the record. | ||
| 
 | Number | Leader epoch of the record. | ||
| 
 | DateTime | Log append timestamp of the record. | ||
| 
 | Number | Offset of the record. | ||
| 
 | Number | Partition of the record. | ||
| 
 | Number | Serialized key size of the record. | ||
| 
 | Number | Serialized value size of the record. | ||
| 
 | String | Topic of the record. | 

### Keystore

Configures the keystore for the TLS protocol. The keystore you generate contains a private key and a public certificate.

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | String | Path to the keystore. Mule resolves the path relative to the current classpath and file system. | ||
| 
 | String | Type of keystore. | ||
| 
 | String | Alias of the key to use when the keystore contains multiple private keys. By default, Mule uses the first key in the file. | ||
| 
 | String | Password used to protect the private key. | ||
| 
 | String | Password used to protect the keystore. | ||
| 
 | String | Encryption algorithm that the keystore uses. | 

### Proxy Config Params

Configures the proxy configuration parameters.

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | String | Hostname or IP address of the proxy server. | ||
| 
 | Number | Port of the proxy server. | ||
| 
 | String | Username to authenticate against the proxy server. | ||
| 
 | String | Password to authenticate against the proxy server. | 

### Reconnect

Configures a standard reconnection strategy, which specifies how often to reconnect and how many reconnection attempts the connector source or operation can make.

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | Number | How often to attempt to reconnect, in milliseconds. | ||
| 
 | Boolean | If  | ||
| 
 | Number | How many reconnection attempts the Mule app can make. | 

### Reconnect Forever

Configures a forever reconnection strategy by which the connector source or operation attempts to reconnect at a specified frequency for as long as the Mule app runs.

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | Number | How often to attempt to reconnect, in milliseconds. | ||
| 
 | Boolean | If  | 

### Reconnection

Configures a reconnection strategy for an operation.

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | Boolean | What to do if, when an app is deployed, a connectivity test does not pass after exhausting the associated reconnection strategy: 
 | ||
| 
 | Reconnection strategy to use. | 

### Record

Type for records.

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | Kafka record attributes. | |||
| 
 | Binary | Payload for the record. | ||
| 
 | 

### Ser Byte Array

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | Binary | 

### Redelivery Policy

Configures the redelivery policy for executing requests that generate errors. You can add a redelivery policy to any source in a flow.

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | Number | Maximum number of times that a redelivered request can be processed unsuccessfully before returning a REDELIVERY_EXHAUSTED error. | ||
| 
 | Boolean | If  | ||
| 
 | String | Secure hashing algorithm to use if the  | ||
| 
 | String | Defines one or more expressions to use to determine when a message has been redelivered. This property may only be set if  | ||
| 
 | ObjectStore | Configures the object store that stores the redelivery counter for each message. | 

### Repeatable File Store Stream

Configures the repeatable file-store streaming strategy by which Mule keeps a portion of the stream content in memory. If the stream content is larger than the configured buffer size, Mule backs up the buffer’s content to disk and then clears the memory.

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | Number | Maximum amount of memory that the stream can use for data. If the amount of memory exceeds this value, Mule buffers the content to disk. To optimize performance: 
 | ||
| 
 | Enumeration, one of: 
 | Unit for the  | 

### Repeatable In Memory Stream

Configures the in-memory streaming strategy by which the request fails if the data exceeds the MAX buffer size. Always run performance tests to find the optimal buffer size for your specific use case.

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | Number | Initial amount of memory to allocate to the data stream. If the streamed data exceeds this value, the buffer expands by  | ||
| 
 | Number | Amount by which the buffer size expands if it exceeds its initial size. Setting a value of  | ||
| 
 | Number | Maximum amount of memory to use. If more than that is used then a STREAM_MAXIMUM_SIZE_EXCEEDED error is raised. A value lower than or equal to zero means no limit. | ||
| 
 | Enumeration, one of: 
 | Unit for the  | 

### Standard Revocation Check

Configures standard revocation checks for TLS certificates.

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | Boolean | Which elements to verify in the certificate chain: 
 | ||
| 
 | Boolean | How to check certificate validity: 
 | ||
| 
 | Boolean | Whether to use the secondary method to check certificate validity: 
 | ||
| 
 | Boolean | What to do if the revocation server can’t be reached or is busy: 
 | 

### Tcp Client Socket Params

Configures the TCP client socket parameters.

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | Number | Size of the buffer (in bytes) used when sending data, set on the socket itself. | ||
| 
 | Number | Buffer size. | ||
| 
 | Number | Sets the  | 
 | |
| 
 | Boolean | If set, data is sent immediately rather than being collected for efficiency, prioritizing latency over network traffic reduction. Despite the socket default being false, this option defaults to true because reducing network traffic is generally not a major concern. | 
 | |
| 
 | Number | Sets the  | ||
| 
 | Boolean | Enables the  | 
 | |
| 
 | Number | How long the connector waits before timing out when establishing a connection to the remote service. | 
 | 

### TLS

Configures TLS to provide secure communications for the Mule app.

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | String | Comma-separated list of protocols enabled for this context. | ||
| 
 | String | Comma-separated list of cipher suites enabled for this context. | ||
| 
 | Configures the TLS truststore. | |||
| 
 | Configures the TLS keystore. | |||
| 
 | Configures a revocation checking mechanism. | 

### Topic Partition

Type for topic partition.

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | String | Topic name. | x | |
| 
 | Number | Number of partitions. | x | 

### Truststore

Configures the truststore for TLS.

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | String | Path to the truststore. Mule resolves the path relative to the current classpath and file system. | ||
| 
 | String | Password used to protect the truststore. | ||
| 
 | String | Type of truststore. | ||
| 
 | String | Encryption algorithm that the truststore uses. | ||
| 
 | Boolean | If  | 

## See Also

- 
[Salesforce Help](https://help.salesforce.com)