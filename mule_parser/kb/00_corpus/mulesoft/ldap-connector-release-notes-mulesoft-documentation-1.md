# LDAP Connector Release Notes | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/release-notes/connector/ldap-connector-release-notes-mule-4](https://docs.mulesoft.com/release-notes/connector/ldap-connector-release-notes-mule-4)

---

This release includes general security fixes.

# LDAP Connector Release Notes

Support Category: [Select](https://www.salesforce.com/en-us/wp-content/uploads/sites/4/documents/legal/Agreements/versioning-back-support-policy.pdf)

Anypoint Connector for Lightweight Directory Access Protocol (LDAP) is an open, vendor-neutral, industry standard application protocol for accessing and maintaining distributed directory information services over an Internet Protocol (IP) network. The LDAP connector allows Mule applications to interact with LDAP servers.

Guide: [LDAP Connector User Guide](../../ldap-connector/latest/)

## 3.7.0

**June 5, 2026**

### What’s New

- 
You can now use the new **Secure SSL Configuration**type instead of**SSL Configuration**type to establish secure connections. The**SSL Configuration**type was deprecated because it relied on global JVM environment configurations and could not support FIPS-compliant truststore types required under FIPS 140-3 environments.
- 
The **Secure SSL Configuration**type includes the new**TLS Context**field. Use this field to configure BCFKS truststores and the Bouncy Castle FIPS provider within your Mule applications.For more information, refer to [Secure SSL Configuration Type](../../ldap-connector/latest/ldap-connector-reference#secure-ssl-configuration-type).

### Compatibility

| Application/Service | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| OpenJDK | 8, 11, and 17 | 
| LDAP | v3 | 
| OpenLDAP | 2.4.x | 

### Fixed Issues

| Issue Resolution | ID | 
|---|---|
| W-21526999 | 

## 3.6.1

**November 7, 2025**

### Compatibility

| Application/Service | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| OpenJDK | 8, 11, and 17 | 
| LDAP | v3 | 
| OpenLDAP | 2.4.x | 

### Fixed Issues

| Issue Resolution | ID | 
|---|---|
| Connection management logging messages now reflect connection pooling behavior instead of indicating connections are closed. | W-19678434 | 

## 3.6.0

**September 25, 2024**

### What’s New

- 
LDAP Connector now returns `LDAP:SECURITY`error when attempting to establish an insecure connection (Basic Authentication configuration) in environments that require FIPS 140-2 compliance (mule.security.model=fips140-2). For sources or connection tests prior to deployment, an associated`LDAPException`message is thrown, ensuring LDAP connections meet advanced security requirements in regulated environments.

### Compatibility

| Application/Service | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| OpenJDK | 8, 11, and 17 | 
| LDAP | v3 | 
| OpenLDAP | 2.4.x | 

## 3.5.6

**January 26, 2024**

### What’s New

- 
This connector is now compatible with Java 17. 

### Compatibility

| Application/Service | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| OpenJDK | 8, 11, and 17 | 
| LDAP | v3 | 
| OpenLDAP | 2.4.x | 

## 3.5.5

**October 17, 2023**

### Compatibility

| Application/Service | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Java | 1.8 | 
| OpenJDK | 8 and 11 | 
| LDAP | v3 | 
| OpenLDAP | 2.4.x | 

### Fixed Issues

| Issue Resolution | ID | 
|---|---|
| The com.google.guava library is upgraded to version 32.0.1-jre to address reported security vulnerabilities. | W-13844853 | 

## 3.5.4

**April 18, 2023**

### Compatibility

| Application/Service | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Java | 1.8 | 
| OpenJDK | 8 and 11 | 
| LDAP | v3 | 
| OpenLDAP | 2.4.x | 

### Fixed Issues

| Issue Resolution | ID | 
|---|---|
| The connector now handles pagination from the LDAP server. | W-12980985 | 

## 3.5.3

**April 6, 2023**

### Compatibility

| Application/Service | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Java | 1.8 | 
| OpenJDK | 8 and 11 | 
| LDAP | v3 | 
| OpenLDAP | 2.4.x | 

### Fixed Issues

| Issue Resolution | ID | 
|---|---|
| The trust store custom configuration no longer overrides the default JVM trust store. | W-12282743 | 

## 3.5.2

**February 13, 2023**

### Compatibility

| Application/Service | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Java | 1.8 | 
| OpenJDK | 8 and 11 | 
| LDAP | v3 | 
| OpenLDAP | 2.4.x | 

### Fixed Issues

| Issue Resolution | ID | 
|---|---|
| The  | W-12233513 | 

## 3.5.1

**November 22, 2022**

### Compatibility

| Application/Service | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Java | 1.8 | 
| OpenJDK | 8 and 11 | 
| LDAP | v3 | 
| OpenLDAP | 2.4.x | 

### Fixed Issues

| Issue | ID | 
|---|---|
| The  | W-11987427 | 

## 3.5.0

**March 14, 2022**

### Compatibility

| Application/Service | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Java | 1.8 | 
| OpenJDK | 8 and 11 | 
| LDAP | v3 | 
| OpenLDAP | 2.4.x | 

### What’s New

- 
You can now configure a custom truststore for SSL and TLS configurations by using the new **Custom Truststore Path**and**Custom Truststore Password**fields.For information about using these new fields, see the [LDAP Connector Reference](../../ldap-connector/latest/ldap-connector-reference).

### Fixed Issues

| Issue | ID | 
|---|---|
| You can now configure a custom truststore with the connector. | SE-24432 | 

## 3.4.2

**January 25, 2022**

### Compatibility

| Application/Service | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Java | 1.8 | 
| OpenJDK | 8 and 11 | 
| LDAP | v3 | 
| OpenLDAP | 2.4.x | 

### Fixed Issues

| Issue | ID | 
|---|---|
| The connector did not pick up the Truststore when a resource related path is provided. | SE-24211 | 

## 3.4.1

**December 2, 2021**

### Compatibility

| Application/Service | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Java | 1.8 | 
| OpenJDK | 8 and 11 | 
| LDAP | v3 | 
| OpenLDAP | 2.4.x | 

### Fixed Issues

| Issue | ID | 
|---|---|
| The  | SE-23679 | 

## 3.4.0

**June 30, 2021**

### Compatibility

LDAP Connector is compatible with:

| Application/Service | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Java | 1.8 | 
| OpenJDK | 8 and 11 | 
| LDAP | v3 | 
| OpenLDAP | 2.4.x | 

### New Features

- 
Added support for LDAPS (LDAP over SSL), which consists of a new connection provider called **SSL Connection Provider**.

## 3.3.2

**June 8, 2021**

### Compatibility

LDAP Connector is compatible with:

| Application/Service | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Java | 1.8 | 
| OpenJDK | 8 and 11 | 
| LDAP | v3 | 
| OpenLDAP | 2.4.x | 

### Fixed Issues

- 
LDAP triggers were not receiving results after the first poll when using Open LDAP or MS AD. (SE-20905, SE-20906) 

## 3.3.1

**March 31, 2021**

### Compatibility

The LDAP Connector is compatible with:

| Application/Service | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Java | 1.8 | 
| OpenJDK | 8 and 11 | 
| LDAP | v3 | 
| OpenLDAP | 2.4.x | 

### Fixed Issues

An NPE was thrown while getting total results in a paged search. (SE-20290)

## 3.3.0

**December 11, 2020**

### Compatibility

The LDAP Connector is compatible with:

| Application/Service | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Java | 1.8 | 
| OpenJDK | 8 and 11 | 
| LDAP | v3 | 
| OpenLDAP | 2.4.x | 

### Fixed Issues

Improved LDAP exception handling by adding an `LDAP:OPERATION_NOT_COMPLETED` error type. (SE-18048)

## 3.2.6

**September 18, 2020**

### Compatibility

The LDAP Connector is compatible with:

| Application/Service | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Java | 1.8 | 
| OpenJDK | 8 and 11 | 
| LDAP | v3 | 
| OpenLDAP | 2.4.x | 

### Fixed Issues

Fixed the issue that caused the connector to hang while trying to close the TLS context. (SE-17272)

## 3.2.5

**September 7, 2020**

### Compatibility

The LDAP Connector is compatible with:

| Application/Service | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Java | 1.8 | 
| LDAP | v3 | 
| OpenLDAP | 2.4.x | 

### Fixed Issues

- 
Fixed a security vulnerability. (CONN-6899) 

## 3.2.4

**August 25, 2020**

### Compatibility

The LDAP Connector is compatible with:

| Application/Service | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Java | 1.8 | 
| LDAP | v3 | 
| OpenLDAP | 2.4.x | 

### Fixed Issues

- 
Several LDAP Connector operations did not escape metacharacters. (SE-17144) 

## 3.2.3

**July 3, 2020**

### Compatibility

The LDAP Connector is compatible with:

| Application/Service | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Java | 1.8 | 
| LDAP | v3 | 
| OpenLDAP | 2.4.x | 

### Fixed Issues

- 
Fixed issue where BIND operation of LDAP Connector was not properly parsing MS Active Directory GUID and SID values. (SE-16010) 

## 3.2.2

**June 16, 2020**

### Compatibility

The LDAP Connector is compatible with:

| Application/Service | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Java | 1.8 | 
| LDAP | v3 | 
| OpenLDAP | 2.4.x | 

### Fixed Issues

- 
Fixed issue where LDAP Connector was not properly processing MS Active Directory GUID and SID values. (SE-16010) 

## 3.2.1

**May 4, 2020**

### Compatibility

The LDAP Connector is compatible with:

| Application/Service | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Java | 1.8 | 
| LDAP | v3 | 
| OpenLDAP | 2.4.x | 

### Fixed Issues

- 
The connector now filters the DN attributes correctly. (SE-15744) 
- 
Fixed all reported vulnerabilities. 

## 3.2.0

**April 2, 2020**

### Compatibility

The LDAP Connector is compatible with:

| Application/Service | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Java | 1.8 | 
| LDAP | v3 | 
| OpenLDAP | 2.4.x | 

### Features

- 
The connector now supports the display of entity attributes as objects, containing the attribute metadata, depending on a property(Show attributes as objects) in the connector configuration(SE-15218). 

## 3.1.6

**February 3, 2020**

### Compatibility

The LDAP Connector is compatible with:

| Application/Service | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Java | 1.8 | 
| LDAP | v3 | 
| OpenLDAP | 2.4.x | 

### Fixed Issues

Fixed the issue where type definitions were missing, which made search results different for Mule 3 and Mule 4. (SE-14621)

## 3.1.5

**October 22, 2019**

### Compatibility

The LDAP Connector is compatible with:

| Application/Service | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Java | 1.8 | 
| LDAP | v3 | 
| OpenLDAP | 2.4.x | 

### Fixed Issues

- 
Anypoint Studio displayed an error message when an optional field was left unspecified. (SE-12729) 

## 3.1.4

**June 24, 2019**

### Compatibility

The LDAP Connector is compatible with:

| Application/Service | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Java | 1.8 | 
| LDAP | v3 | 
| OpenLDAP | 2.4.x | 

### Fixed Issues

- 
Mule LDAP Connector Search and Lookup Search didn’t return multi-value fields as arrays when they were built with a single value. (SE-11864) 

## 3.1.3

**April 23, 2019**

### Compatibility

The LDAP Connector is compatible with:

| Application/Service | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Java | 1.8 | 
| LDAP | v3 | 
| OpenLDAP | 2.4.x | 

### Fixed Issues

- 
Fixed an issue regarding transformation of an LDAPEntry to a string which was causing java.lang.ArrayIndexOutOfBoundsException. 

## 3.1.2

**February 20, 2019**

Release notes for version 3.1.2 of the LDAP connector.

### Compatibility

The LDAP Connector is compatible with:

| Application/Service | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Java | 1.8 | 
| LDAP | v3 | 
| OpenLDAP | 2.4.x | 

### Features

This release improves the quality of the code by refactoring and adding comments.

## 3.1.1

**October 26, 2018**

### Compatibility

The LDAP Connector is compatible with:

| Application/Service | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Java | 1.8 | 
| LDAP | v3 | 
| OpenLDAP | 2.4.x | 

### Fixed Issues

- 
The connector failed when the `authentication`parameter was not set. This was fixed and now it works as expected.

## 3.1.0

**September 13, 2017**

### Compatibility

The LDAP Connector is compatible with:

| Application/Service | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Java | 1.8 | 
| LDAP | v3 | 
| OpenLDAP | 2.4.x | 

### Features

- 
The connector now has 2 triggers one for new objects and one for modified objects. Using these 2 triggers one can receive notifications if ldap entries are created or updated since the app was started or since a configured timestamp that can be specified when configuring the trigger. 

## See Also

- 
[Salesforce Help](https://help.salesforce.com)
- 
[MuleSoft Services](https://www.mulesoft.com/support-and-services)
- 
[Known Issues](https://help.salesforce.com/s/issues)