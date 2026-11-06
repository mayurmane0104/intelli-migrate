# Secure Configuration Properties | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/mule-runtime/latest/secure-configuration-properties](https://docs.mulesoft.com/mule-runtime/latest/secure-configuration-properties)

---

```
encrypted:
    value1: "![nHWo5JhNAYM+TzxqeHdRDXx15Q5R56YVGiQgXCoBCew=]"
    value2: "![nHWo6XyCADP+TzxqeHdRDXx15Q5R56YVGiQgXCoDFaj=]"
testPropertyA: "testValueA"
testPropertyB: "testValueB"
```
# Secure Configuration Properties

You can encrypt configuration properties as another security level for your applications. To create secure configuration properties, review the following process:

- 
Create a secure configuration properties file. 
- 
Define secure properties in the file by enclosing the encrypted values between the sequence `![value]`.
- 
Configure the file in the project with the Mule Secure Configuration Properties Extension module. The file must point to or include the decryption key. 

## Attributes

Before you create a secure properties file and define its properties, review the secure configuration properties attributes and encrypting attributes used in the process:

| Attribute Name | Description | 
|---|---|
| Name | A unique name for your global secure configuration properties. | 
| Key | A word or phrase that you specify to unlock the properties value. For example,  | 
| File | The location of the file that the key unlocks. | 
| Encoding | Encoding of the file that the key unlocks. The default value is UTF-8. | 
| File Level Encryption | Set to  | 

| Attribute Name | Description | 
|---|---|
| Algorithm | The algorithm you use to encrypt the content of the property. See  | 
| Mode | The procedure that lets the Mule runtime engine repeatedly use a block cipher with a single key. See  | 
| Use random IVs | Set this attribute to  | 

## Create a Secure Configuration Properties File

The first task in securing configuration properties is to create a YAML configuration file (`.yaml`) or a Spring-formatted Properties file (`.properties`), where you define the properties. The Mule Secure Configuration Properties Extension module enables you to configure YAML or Properties file types.

You can create secure configuration properties files either in `src/main/resources` in your Mule project, or by using absolute paths.

## Define Secure Configuration Properties in the File

Define secure properties in the file by enclosing the encrypted values between the sequence `![value]` with no spaces or characters before or after the closing bracket (`]`). Trailing spaces cause decryption to fail.

The file can contain both encrypted and nonencrypted values that you can use anywhere in the Mule application.

| Secure access to the operating system. Anyone who runs a `ps`command or views a Java console can see the decrypted values that the Mule app stores in memory. | 

The following `file1.yaml` example contains both encrypted and nonencrypted configuration properties values:

| Enclose the encrypted value in quotes so that the system reads it as a string. | 

The following `file1.properties` example contains the configuration properties used in the previous example but uses a Spring-formatted properties file:

encrypted.value1=![nHWo5JhNAYM+TzxqeHdRDXx15Q5R56YVGiQgXCoBCew=] encrypted.value2=![nHWo6XyCADP+TzxqeHdRDXx15Q5R56YVGiQgXCoDFaj=] testPropertyA=testValueA testPropertyB=testValueB

## Encrypt Properties Using the Secure Properties Tool

Use the Secure Properties Tool to encrypt or decrypt text strings, values inside a properties file, or all the contents of a properties file.

Verify that you have the latest available version of this tool to use all the functions detailed in this article.

[Secure Properties Tool Jar file - Supports Java 17](_attachments/secure-properties-tool-j17.jar).

Latest release: 11/22/2024.

Note that the syntax has changed from earlier versions. To avoid issues, use the syntax and the JAR file provided in this article. Also, the tool doesn’t support the hash character `#` in the input text.git st

See [Parameters Reference](#parameter-reference) for a complete list and definition of all accepted parameters.

### Encrypt Text Strings

Use the following syntax to encrypt or decrypt a text string provided as a parameter:

`java -cp secure-properties-tool-j17.jar com.mulesoft.tools.SecurePropertiesTool \ <method> \ <operation> \ <algorithm> \ <mode> \ <key> \ <value> \ --use-random-iv [optional]`console.linenums

- 
Set `<method>`to`string`to configure the tool to process a text string.
- 
Specify the other parameters to perform your desired operation. 

For example, if you run:

`java -cp secure-properties-tool-j17.jar com.mulesoft.tools.SecurePropertiesTool \ string \ encrypt \ Blowfish \ CBC \ mulesoft \ "some value to encrypt"`console.linenums

The tool returns:

`8q5e1+jy0cND2iV2WPThahmz6XsDwB6Z`console.linenums

### Encrypt Files

In addition to processing strings, the encryption tool processes `.yaml` or `.properties` files. You can encrypt or decrypt the values inside a properties file, or all the file’s content.

#### Encrypt Properties Inside a File

Use the following syntax to encrypt or decrypt all values inside a properties file:

`java -cp secure-properties-tool-j17.jar com.mulesoft.tools.SecurePropertiesTool \ <method> \ <operation> \ <algorithm> \ <mode> \ <key> \ <input file> \ <output file> \ --use-random-iv [optional]`console.linenums

- 
Set `<method>`to`file`.
- 
Set `<input file>`to the properties file to process.
- 
Set `<output file>`to the file that’s generated after the process.
- 
Specify the other parameters to perform your desired operation. 

For example, consider the file `example_in.yaml` with the following content:

```
properties:
  example1:
    value: "Muleman is here"
  example2: "Max the mule"
```
yamlIf you run:

`java -cp secure-properties-tool-j17.jar com.mulesoft.tools.SecurePropertiesTool \ file \ encrypt \ Blowfish \ CBC \ mulesoft \ example_in.yaml \ example_out.yaml`console.linenums

The tool generates the file `example_out.yaml` with the following content:

```
properties:
  example1:
    value: "![qCReIPK3jcqD7WR84ISSIQ==]"
  example2: "![En8lII21ZHrdIaINw0+mSA==]"
```
yaml#### Encrypt All the Content of a File

Use the following syntax to encrypt or decrypt all the content of a properties file:

`java -cp secure-properties-tool-j17.jar com.mulesoft.tools.SecurePropertiesTool \ <method> \ <operation> \ <algorithm> \ <mode> \ <key> \ <input file> \ <output file> --use-random-iv [optional]`console.linenums

- 
Set `<method>`to`file-level`.
- 
Set `<input file>`to the properties file to process.
- 
Set `<output file>`to the file that’s generated after the process.
- 
Specify the other parameters to perform your desired operation. 

For example, consider the file `example_in.yaml` with the following content:

```
properties:
  example1:
    value: "Muleman is here"
  example2: "Max the mule"
```
yamlIf you run:

`java -cp secure-properties-tool-j17.jar com.mulesoft.tools.SecurePropertiesTool \ file-level \ encrypt \ Blowfish \ CBC \ mulesoft \ example_in.yaml \ example_out.yaml`console.linenums

The tool generates the file `example_out.yaml` with the following content:

`k/J1EHyxJagOcyQELoaqIDCzzKc1bLGJiHY2dv6jzuhtVpP1LTlgK3y8EH7OkK5iuuu8kik3P5dCDMixZXwn/EV6xbUwLFKnEb4x1pUX6aopLP/KULm0pQ==`txt

### Parameters Reference

| Parameter | Description | ||||||
|---|---|---|---|---|---|---|---|
| 
 | Sets the encryption or decryption method. Accepted values are: 
 | ||||||
| 
 | Sets the operation to perform. Accepted values are: 
 | ||||||
| 
 | Specifies the algorithm to use during the operation. | ||||||
| 
 | Specifies the mode to use during the operation. | ||||||
| 
 | Specifies the word used to lock or unlock the file or value during the operation. 
 | ||||||
| 
 | Specifies the string value that’s encrypted or decrypted during the  | ||||||
| 
 | Specifies if the operation uses random initialization vectors (IVs). | ||||||
| 
 | Specifies the properties file that’s encrypted or decrypted during the  | ||||||
| 
 | Specifies the encrypted or decrypted properties file that’s created after the  | 

## Configure the File in the Project

You can configure a secure properties file both in standalone XML or in Anypoint Studio, with the Mule Secure Configuration Properties Extension module available from [Exchange](https://anypoint.mulesoft.com/exchange/com.mulesoft.modules/mule-secure-configuration-property-module/).

### Configure the File with the Extension Module in XML

In your XML flow, use the module `<secure-properties:config>` to configure the file. Review the following example:

**Secure Configuration Properties with Default Values**

```
<secure-properties:config key="${runtime.property}"
  file="file1.yaml" name="test">
    <secure-properties:encrypt/>
</secure-properties:config>
<global-property name="prop" value="my-${secure::property.key1}"/>
```
xml- 
The `<secure-properties:encrypt>`tag is required even when using the default values.
- 
The prefix `secure::`is required for loading the key.Use the `secure::`prefix to access all values inside a secure properties file, even if the values aren’t encrypted. Doing this enables you to switch between files (or environments) without changing the entire configuration.
- 
At deployment time, a decryption key is passed into the Mule runtime engine as a system environment variable `runtime.property`. This property must be the exact key used to encrypt the values stored in the`file1.yaml`file.
- 
The default encryption algorithm and mode is used. 
- 
If the actual (decrypted) value of the property `property.key1`is, for example,`"property"`, the value of the property`prop`is`"my-property"`.

You can also change the encryption algorithm and crypto mode by setting additional attributes of the `<secure-properties:encrypt>` tag:

**Secure Configuration Properties with Custom Values**

```
<secure-properties:config key="${runtime.property}"
  file="file1.properties" name="test">
    <secure-properties:encrypt algorithm="AES" mode="CBC" useRandomIVs="true"/>
</secure-properties:config>
```
xmlIn the previous example, the `<secure-properties:encrypt>` tag uses the `AES` algorithm with `CBC` mode and `random IV`.

| The  | 

### Configure the File with the Extension Module in Studio

If you are developing applications using Anypoint Studio, you can also create secure configuration properties using the module by adding it as a dependency in your Mule app.

#### Install the Extension Module

- 
Open your Mule project in Anypoint Studio. 
- 
Go to the Mule Palette section. 
- 
Click **Search in Exchange**.
- 
In the Add Module to Project window, search for **Mule Secure Configuration Property Extension**in the**Type a search term to look up in Exchange**box.
- 
Select the module name in the list. 
- 
Click **Add**and then**Finish**.

#### Add and Configure Secure Configuration Properties to your App

- 
Go to your Mule app configuration file. 
- 
Select **Global Elements**tab.
- 
Click **Create**.
- 
Select **Secure Properties Config**.
- 
Configure the global element with a **File**location,**Key**,**Algorithm**,**Mode**,**Use random IV**,**File level encryption**, and**Encoding**.
- 
Click **OK**.

![Configuration panel for secure properties](_images/mruntime-secure-config-properties-studio.png) 

| The  | 

#### Verify Secure Configuration Properties at Development Time

When you are developing applications in Studio, you can verify that secure configurations properties for a connector are set up correctly by testing the connector connection.
The following example shows a Salesforce connector configuration with its secure properties (username, password, and token) encrypted in a `.yaml` file:

![Configuration panel for a Salesforce connection](_images/mruntime-secure-config-properties-studio2.png) 

Add the `secure::` prefix before the property name definition, to enable access to all values inside a secure properties file, even if the values aren’t encrypted.

You can click **Test Connection** to verify that the connection is functioning as expected and assure that the secure properties are read successfully.

## File-Level Encryption

Since version 1.1.0 of the Secure Configuration Properties module, you can encrypt an entire file rather than only individual properties values. You can encrypt a file both in XML or Anypoint Studio:

In your XML flow, add the `fileLevelEncryption` attribute and set it to `true`:

```
<secure-properties:config key="${runtime.property}" file="file1.yaml" fileLevelEncryption="true" name="test">
    <secure-properties:encrypt algorithm="AES" mode="CBC"/>
</secure-properties:config>
```
xmlIn Studio, in Secure Configuration Properties window, select **True** for the **File level encryption**:

![Secure properties configuration with AES encryption and CBC mode settings](_images/mruntime-secure-config-properties-studio3.png) 

## Secure Configuration Properties Use Cases

Review the following uses cases about secure configuration properties, where you can learn how a flow uses encrypted and nonencrypted values, set secure configuration properties files dynamically, and how you can work using more than one configuration file.

### Encrypted and Nonencrypted Values

The following example shows how a flow uses the encrypted `encrypted.value1` value to set the payload. At runtime, the decryption algorithm stores the decrypted value of `encrypted.value1` into memory.

```
<flow name="main">
    <set-payload value="${secure::encrypted.value1}"/>
</flow>
```
xmlThe following example shows how a flow uses a nonencrypted value from the same secure properties file:

```
<flow name="mainNonEncrypted">
    <set-payload value="${secure::testPropertyA}"/>
</flow>
```
xml### Set Secure Configuration Properties File Dynamically

A common configuration use case is to set the file to depend on a property (for example, `env`) to determine which file to use.

For example, to use a `development-properties` file during the development stage (which could not be encrypted) or a production file (with encrypted values).

**Secure Configuration Properties with Environment File Defined**

`<secure-properties:config key="${runtime.property}" file="${env}-properties.yaml" name="test"/>`xmlUsing this method, the value of the property `env` determines which file to use to load the secure configuration properties. You can set that `env` property using a `global property`, system property, or environment property.

**Secure Global Configuration Properties with Environment File Defined**

```
<global-property name="env" value="dev"/>
<secure-properties:config key="${runtime.property}" file="${env}-properties.yaml" name="test"/>
```
xmlUsing this method, the default value for the `env` property is `"dev"`, which can still be overridden with a system or environment property. Note that this is **required** for metadata resolution in Anypoint Studio. If you don’t define default values for the properties that are passed through the command line, you receive an error when you create the application model for all message processors that depend on those properties.

### Work with More Than One Configuration File

You can define more than one secure configuration properties file to read properties from. To do so, simply define a `<secure-properties:config />` tag for each file you want to load. Each secure configuration properties file is independently configured with an encryption algorithm, cipher mode, and encryption/decryption key. These settings don’t have to be the same among the files.

The following example shows how to use more than one configuration file:

```
<secure-properties:config key="${runtime.property}" file="file1.yaml" name="test">
    <secure-properties:encrypt algorithm="AES" mode="CBC"/>
</secure-properties:config>
<secure-properties:config key="${runtime.property}" file="file2.yaml" name="otherConfig">
    <secure-properties:encrypt algorithm="AES" mode="CBC"/>
</secure-properties:config>
```
xml## Supported Configuration File Types

- 
Spring-formatted properties: `.properties`
- 
YAML: `.yaml`

## Supported Algorithms and Modes

### Supported Algorithms

- 
AES (default) 
- 
Blowfish 
- 
DES 
- 
DESede 
- 
RC2 
- 
RCA 

You can use the following algorithms only if you configure a [Java Cryptography Extension (JCE) Provider](https://docs.oracle.com/cd/E19830-01/819-4712/ablsc/index.html) that adds support for them:

- 
Camellia 
- 
CAST5 
- 
CAST6 
- 
Noekeon 
- 
Rijndael 
- 
SEED 
- 
Serpent 
- 
Skipjack 
- 
TEA 
- 
Twofish 
- 
XTEA 
- 
RC5 
- 
RC6 

### Supported Modes

- 
CBC (default) 
- 
CFB 
- 
ECB 
- 
OFB 

## Frequently Asked Questions

After you learn about, create, and use secure configuration properties files for a while, you might have additional questions about troubleshooting and maximizing their use. Following are some common questions and answers. Refer as well to the topics linked to in See Also.

**What if a property is defined in multiple files?**

In that case, the actual property’s value will be the one in which is first defined.

**Can I define a secure property that depends on a previously defined secure property?**

Yes. Just use the same syntax: `property=My dependent ${secure::dependent.property} value`.

Note that secure configuration properties can depend on other secure configuration properties, but not on other Mule configuration properties.