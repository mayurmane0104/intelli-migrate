# Configuring TLS Context for Omni Gateway in Connected Mode | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/gateway/latest/flex-conn-tls-config](https://docs.mulesoft.com/gateway/latest/flex-conn-tls-config)

---

**Keystore**

# Configuring TLS Context for Omni Gateway in Connected Mode

Using encryption, Transport Layer Security (TLS) policies protect communication between clients, API instances, and upstream services. After you [create a secret group](../../anypoint-security/asm-secret-group-creation-task), you can add a TLS context or a mutual authentication TLS (mTLS) context and apply the TLS context to API instances in API Manager to encrypt their inbound and outbound traffic.

When you add a TLS context, you can also select the ciphers to use with the TLS context and configure different inbound and outbound validation settings.

Omni Gateway supports the following:

- 
Regular TLS between a client and the API instance (HTTPS), referred to as inbound TLS 
- 
Regular TLS between an API instance and an upstream service, referred to as outbound TLS 
- 
Mutual authentication TLS (mTLS) in both the inbound and outbound direction 

By default, Omni Gateway supports outbound TLS to communicate with upstream services that require a secure communication channel. For default outbound communication, Omni Gateway uses only TLS 1.2. To find the default TLS 1.2 ciphers, see [Omni Gateway Supported Ciphers](#supported-ciphers). To find the ciphers, see [Omni Gateway Supported Ciphers](#supported-ciphers). Applying a TLS context to an upstream overrides the default TLS context for that upstream. Because the default ciphers may change for later Omni Gateway versions, you can apply a TLS context to an upstream to ensure it remains the same.

Omni Gateway implements inbound TLS at the port level, meaning that an inbound TLS context applied to an API instance is also applied to all other instances that share the same port. To learn more about how TLS context is shared across ports, see [Inbound TLS Context Applied to Shared Ports](#tls-context-applied-to-shared-ports).

Port sharing is not a concern for outbound TLS. You can select the outbound TLS context for each individual upstream service.

| The Authority Information Access (AIA) certificate extension is not supported when configuring outbound TLS contexts. | 

## Before You Begin

Before configuring the TLS context for an Omni Gateway Connected Mode, complete the following tasks:

- 
Ensure the following permissions are enabled: - 
*Grant access to secrets*in Secrets Manager
- 
*Deploy API Proxies*in API ManagerYour Anypoint Platform Admin can add these permissions in Access Management. See [Manage Team Permissions](../../access-management/configure-teams#manage-team-permissions)for more information.
 
- 
- 
When adding a secret group, refer to the [TLS Configuration Options](#tls-configuration-options).Depending on your desired configuration, either: 
- 
Privacy Enhanced Mail (PEM) type is required for your Keystore or Truststore. 
 

## TLS Configuration Options

You can configure your TLS context to support regular TLS and mTLS in both the inbound and outbound direction. Depending on the desired configuration, you must add different certificate files to your secret group and select different TLS context configuration options.

Refer to the following cross reference table for the required TLS context configuration settings you need in the [Add a TLS Context](#add-a-tls-context) step:

| Parameter | Inbound TLS | Inbound mTLS | Outbound TLS | Outbound mTLS | 
|---|---|---|---|---|
| Required | Required | Not Used | Required | |
| 
 | Not Used | Required | Required, unless skip server cert validation is selected | Required to validate upstream certificate | 
| 
 | Not Selected | Selected | Not Used | Not Used | 
| 
 | Not Used | Not Used | Either | Not Selected | 

A parameter that is "Not Used" for a configuration implies its status does not affect configuration.

To simplify your configurations, you can create different TLS contexts for the different traffic directions of your API instance. However, you can also use the same TLS context to support different traffic directions, but you cannot support TLS and mTLS for the same direction using the same context. If you use the same TLS context for different directions, ensure you include the required parameters for both directions.

## Add a TLS Context for Omni Gateway

Adding a TLS context to your secret group requires supplying a name, target, version, and a keystore or truststore. Optionally, you can add context expiration date and ALPN Protocols and configure the inbound and outbound settings.

| If you edit a secret group, including a TLS context, that is currently applied to an API instance, you must redeploy the API instance to apply the changes. You must individually redeploy all instances affected by the change. To redeploy API instances, see  | 

To add a TLS context:

- 
Go to **Anypoint Platform > Secrets Manager**.
- 
Ensure your secret group is downloadable. This enables you to apply your TLS context to API instances. To ensure your secret group is downloadable: - 
Click the pencil icon next to the name of your secret group. 
- 
If **Secret Group Downloadable**is selected, click**Cancel**
- 
If **Secret Group Downloadable**is not selected, select it, then click**Save**.
 
- 
- 
In the **Secret Groups**list view, click the**Edit**button of the secret group to add a TLS context.
- 
Select **TLS Context**in the menu on the left, and click**Add TLS Context**.
- 
In the Create TLS context screen, add the required information: - 
**Name**
 Enter a name for your TLS context.
- 
**Target**
 Select**Omni Gateway**to use the TLS context as the SSL validation for Omni Gateway APIs.
- 
**Min TLS Version**and**Max TLS Version**
 You can choose to support a range of TLS versions or a single version by selecting the same version for both the minimum and maximum.
- 
**Keystore**
 If necessary for your configuration, from the drop-down list, select the keystore to store in the TLS context. Only PEM type keystores are visible. The keystore contains the certificate Omni Gateway presents to the remote party for both inbound and outbound TLS.To comply with security standards, all certificates must be 2048 bits or longer. 
- 
**Truststore**
 If necessary for your configuration, from the drop-down list, select a truststore to store certificates trusted by the client. Only PEM type truststores are visible. The truststore contains the CA path that Omni uses to validate the remote party certificate for both inbound and outbound TLS.Upstream certificates must include the Subject Alternative Name (SAN) extension. The Common Name (CN) field is deprecated. Omni Gateway supports the SAN extension of type `dNSName`.
- 
**Expiration Date**
 Optionally, enter an expiration date for the TLS context.
- 
**ALPN Protocols**
 By default,**H2 - HTTP/1.1**are the selected ALPN protocols. Change this value to support different protocols.
- 
**Inbound Settings**
 If you want to support mTLS for inbound traffic, select**Validate Client certificate**.
- 
**Outbound Settings**
 If you do not want support mTLS for outbound traffic, select**Skip server certificate validation**.
 
- 
- 
If you want to customize cipher support for your TLS context, [Select Ciphers](#select-ciphers).Cipher selection is not available if only supporting TLS version 1.3. 
- 
Click **Save**.

## Apply a TLS Context to an API

You can apply a TLS context to an API instance either when creating a new instance or by editing an existing instance.

API instance settings configuration has two parts, the downstream configuration and the upstream configuration. Inbound TLS context is a downstream configuration option, and outbound TLS context is an upstream configuration option. When adding a new API instance, the downstream and upstream configuration is on separate pages. When editing an API instance, the downstream and upstream configuration options appear on the same page but are in different sections.

For information about either option, see the relevant tutorial:

To apply a TLS context:

- 
Go to **Anypoint Platform > API Manager**.
- 
Navigate to either the: - 
Upstream or downstream configuration page, if adding a new API instance. 
- 
**Settings**page, if editing an existing API instance.
 
- 
- 
Select **HTTPS**for the**Protocol**configuration field if configuring an inbound TLS context.
- 
Click **Add TLS Context**.- 
Select a **Secret Group**.
- 
Select a **TLS Context**.
- 
Click **Ok**.
 
- 
- 
Finish creating the API instance or save the configuration edits. 

## Inbound TLS Context Applied to Shared Ports

Though a port must have an API instance to have an inbound TLS context applied, the inbound TLS context is applied to the port rather than the API instance.

Applying an inbound TLS context to an API instance that shares its port with other instances applies the inbound TLS context to all instances sharing the port.

When you apply, edit, or remove the inbound TLS context of an API instance sharing a port, API Manager shows a warning with a list of the instances sharing the port. You can then choose to override the inbound TLS context of the listed API instances. Overriding the inbound TLS context of the API instances that share the port applies the inbound TLS context to the instances and then redeploys the instances.

Overriding the inbound TLS context of deployed API instances redeploys the instances. Redeploying causes a brief period of downtime in the API instances.

If you edit the port of an API instance that previously shared a port and an inbound TLS context with other instances, the inbound TLS context remains applied to the instances on the previous port.

## Edit Secret Groups and Redeploy API Instances

To edit a secret group, see [Edit a Secret Group](../../anypoint-security/asm-secret-group-creation-task#edit-a-secret-group).

If you edit a secret group currently applied to an API instance, to apply the changes to the API instance, you must individually redeploy all instances the changes affect.

To redeploy an API instance:

- 
Go to **Anypoint Platform > API Manager**.
- 
Click the name of the API instance to redeploy. 
- 
Click **Runtime & Endpoint Configuration > Save & Apply**.

## Select Ciphers

When you configure a TLS context, Secrets Manager applies default ciphers based on the TLS versions you select. In addition to the defaults, you can select other ciphers to use with the selected TLS version. Each TLS context can have multiple ciphers.

To select ciphers:

- 
Click **Ciphers**to see available ciphers.
- 
Select ciphers. Cipher selection is not available if only supporting TLS version 1.3. 
- 
Click **Save**

## TLS Cipher Support on Omni Gateway

Omni can support a range of TLS Versions from TLS 1.2 to TLS 1.3, and you can also customize some of the ciphers to support.

You cannot customize the list of TLS 1.3 Ciphers. If you support TLS 1.3, you must support the TLS 1.3 default ciphers.

If you support TLS 1.2, the TLS 1.2 default Ciphers are selected. However, unlike TLS 1.3, you can customize different TLS 1.2 ciphers.

| For outbound TLS Context, ensure that your API upstream supports the selected ciphers and versions. | 

### Omni Gateway Supported Ciphers

Omni Gateway supports the following TLS Ciphers in Connected Mode and Local Mode:

| Cipher | TLS Version | Default | Advice | 
|---|---|---|---|
| TLS AES 128 GCM SHA256 | 1.3 | Yes | Secure | 
| TLS AES 256 GCM SHA384 | 1.3 | Yes | Secure | 
| TLS CHACHA20 POLY1305 SHA256 | 1.3 | Yes | Secure | 
| TLS ECDHE ECDSA WITH AES 128 GCM SHA256 | 1.2 | Yes | Recommended | 
| TLS ECDHE ECDSA WITH AES 256 GCM SHA384 | 1.2 | Yes | Recommended | 
| TLS ECDHE ECDSA WITH CHACHA20 POLY1305 SHA256 | 1.2 | Yes | Recommended | 
| TLS ECDHE PSK WITH CHACHA20 POLY1305 SHA256 | 1.2 | No | Recommended | 
| TLS ECDHE RSA WITH AES 128 GCM SHA256 | 1.2 | Yes | Secure | 
| TLS ECDHE RSA WITH AES 256 GCM SHA384 | 1.2 | Yes | Secure | 
| TLS ECDHE RSA WITH CHACHA20 POLY1305 SHA256 | 1.2 | Yes | Secure | 
| TLS RSA WITH AES 128 GCM SHA256 | 1.2 | No | Weak | 
| TLS RSA WITH AES 256 GCM SHA384 | 1.2 | No | Weak | 
| TLS RSA WITH AES 128 CBC SHA | 1.2 | No | Weak | 
| TLS RSA WITH AES 256 CBC SHA | 1.2 | No | Weak | 
| TLS PSK WITH AES 128 CBC SHA | 1.2 | No | Weak | 
| TLS PSK WITH AES 256 CBC SHA | 1.2 | No | Weak | 
| TLS ECDHE ECDSA WITH AES 128 CBC SHA | 1.2 | No | Weak | 
| TLS ECDHE ECDSA WITH AES 256 CBC SHA | 1.2 | No | Weak | 
| TLS ECDHE RSA WITH AES 128 CBC SHA | 1.2 | No | Weak | 
| TLS ECDHE RSA WITH AES 256 CBC SHA | 1.2 | No | Weak | 
| TLS ECDHE PSK WITH AES 128 CBC SHA | 1.2 | No | Weak | 
| TLS ECDHE PSK WITH AES 256 CBC SHA | 1.2 | No | Weak |