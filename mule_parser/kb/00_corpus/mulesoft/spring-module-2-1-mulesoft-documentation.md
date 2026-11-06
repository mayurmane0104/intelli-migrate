# Spring Module 2.1 | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/spring-module/latest](https://docs.mulesoft.com/spring-module/latest)

---

```
<?xml version="1.0" encoding="UTF-8"?>
<mule xmlns:spring="http://www.mulesoft.org/schema/mule/spring"
      xmlns="http://www.mulesoft.org/schema/mule/core"
      xmlns:doc="http://www.mulesoft.org/schema/mule/documentation"
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xsi:schemaLocation="http://www.mulesoft.org/schema/mule/core
        http://www.mulesoft.org/schema/mule/core/current/mule.xsd
        http://www.mulesoft.org/schema/mule/spring
        http://www.mulesoft.org/schema/mule/spring/current/mule-spring.xsd">
    <spring:config name="springConfig" files="beans.xml" />
</mule>
```
xml# Spring Module 2.1

Spring Module enables Mule apps to use the Spring framework.

Release Notes: [Spring Module Release Notes](../../release-notes/connector/spring-module-release-notes)

Exchange: [Spring Module](https://www.mulesoft.com/exchange/org.mule.modules/mule-spring-module/)

## Add Spring Module to Your Project

In Anypoint Studio 7, Spring module is provided in the default configuration.

In **Mule Palette**, search for "Spring" and drag the Authorization Filter operation to the Studio canvas.

## Configure Spring Module

- 
Add the following configuration: 
- 
Put the `beans.xml`file in`src/main/resources`.The Spring configuration must be valid. Here is an example beans.xml file: `<beans xmlns="http://www.springframework.org/schema/beans" xmlns:context="http://www.springframework.org/schema/context" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:jdbc="http://www.springframework.org/schema/jdbc" xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans-4.2.xsd http://www.springframework.org/schema/jdbc http://www.springframework.org/schema/jdbc/spring-jdbc-4.2.xsd http://www.springframework.org/schema/context http://www.springframework.org/schema/context/spring-context-4.2.xsd http://www.springframework.org/schema/security http://www.springframework.org/schema/security/spring-security-4.2.xsd"> <jdbc:embedded-database id="dataSource" type="DERBY"> <jdbc:script location="classpath:db/sql/create-db.sql" /> <jdbc:script location="classpath:db/sql/insert-data.sql" /> </jdbc:embedded-database> </beans>`xml

You must export the beans files used with the Spring module for your application to start. See [How to Export Resources](../../mule-runtime/latest/how-to-export-resources).

If you are using Anypoint Studio 7.x, you don’t need to manually update the `mule-artifact.json` file.

Because Mule also needs a descriptor where the Spring beans are declared, so the embedded packager within Studio automatically generates one with all the resources it picks up from the project. However, if you choose to declare the resources you need to export, then Studio packages only those resources.

The following example enables you to declare your `beans.xml` file in `mule-artifact.json`:

`{ "name": "MyApp", "minMuleVersion": "4.2.1", "classLoaderModelLoaderDescriptor": { "id": "mule", "attributes": { "exportedResources": [ "/org/mule/myapp/beans.xml" ] } } } }`example

## Spring Objects in Mule Components

You can use Spring objects in Mule configuration components (for instance, to point to the Derby data source created with Spring beans) as follows:

```
<?xml version="1.0" encoding="UTF-8"?>
<mule xmlns:db="http://www.mulesoft.org/schema/mule/db"
      xmlns:spring="http://www.mulesoft.org/schema/mule/spring"
      xmlns="http://www.mulesoft.org/schema/mule/core"
      xmlns:doc="http://www.mulesoft.org/schema/mule/documentation"
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xsi:schemaLocation="http://www.mulesoft.org/schema/mule/core
        http://www.mulesoft.org/schema/mule/core/current/mule.xsd
        http://www.mulesoft.org/schema/mule/spring
        http://www.mulesoft.org/schema/mule/spring/current/mule-spring.xsd
        http://www.mulesoft.org/schema/mule/db
        http://www.mulesoft.org/schema/mule/db/current/mule-db.xsd">
    <spring:config name="springConfig" files="beans.xml" />
    <db:config name="derbyConfig" doc:name="Database Config"  >
        <db:derby-connection database="datasource" create="true" />
    </db:config>
</mule>
```
xml## Spring Properties Placeholders

You cannot use the properties defined by Spring properties placeholders within your Mule app configuration; you can use them only in Spring configuration files. However, you can use properties defined in Mule through `<configuration-properties/>` within Spring configuration files.

## Limitations of Spring Objects

To use Spring module, consider implementation and injection limits:

- 
Spring objects cannot implement Mule API lifecycle methods. 
- 
Spring objects cannot be injected with Mule API services. The only service that can be used is the `org.mule.runtime.api.artifact.Registry`, which can be used to access any other service within the Mule API. This can be accomplished by using`@PostConstruct`over a method to initialize the object and retrieve the Mule API service.

## Use Spring Security as a Security Manager

| If you use Spring Framework 5.x with plain text passwords, you must prefix the password value with `{noop}`. For example, the password`admin`would be`{noop}admin`instead. | 

The Spring module supports the use of Spring security as a security manager in Mule apps. You must define an authentication manager in the Spring configuration file:

```
<beans xmlns="http://www.springframework.org/schema/beans"
  xmlns:context="http://www.springframework.org/schema/context"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns:jdbc="http://www.springframework.org/schema/jdbc"
  xmlns:ss="http://www.springframework.org/schema/security"
  xsi:schemaLocation="http://www.springframework.org/schema/beans
      http://www.springframework.org/schema/beans/spring-beans-4.2.xsd
      http://www.springframework.org/schema/jdbc
      http://www.springframework.org/schema/jdbc/spring-jdbc-4.2.xsd
      http://www.springframework.org/schema/context
      http://www.springframework.org/schema/context/spring-context-4.2.xsd
      http://www.springframework.org/schema/security
      http://www.springframework.org/schema/security/spring-security-4.2.xsd">
  <ss:authentication-manager alias="authenticationManager">
    <ss:authentication-provider>
      <ss:user-service id="userService">
        <ss:user name="admin" password="admin" authorities="ROLE_ADMIN" />
        <ss:user name="joe" password="secret" authorities="ROLE_ADMIN" />
        <ss:user name="anon" password="anon" authorities="ROLE_ANON" />
        <ss:user name="user" password="password" authorities="ROLE_ANON" />
        <ss:user name="ross" password="ross" authorities="ROLE_ANON" />
        <ss:user name="marie" password="marie" authorities="ROLE_ANON" />
      </ss:user-service>
    </ss:authentication-provider>
  </ss:authentication-manager>
</beans>
```
xmlYou can define a security manager within a Mule app that makes use of the Spring authentication manager like this:

```
<?xml version="1.0" encoding="UTF-8"?>
<mule
  xmlns:spring="http://www.mulesoft.org/schema/mule/spring"
  xmlns="http://www.mulesoft.org/schema/mule/core"
  xmlns:doc="http://www.mulesoft.org/schema/mule/documentation"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://www.springframework.org/schema/beans
    http://www.springframework.org/schema/beans/spring-beans-current.xsd
    http://www.mulesoft.org/schema/mule/core
    http://www.mulesoft.org/schema/mule/core/current/mule.xsd
    http://www.mulesoft.org/schema/mule/spring
    http://www.mulesoft.org/schema/mule/spring/current/mule-spring.xsd">
  <spring:config name="springConfig" files="beans.xml" />
  <spring:security-manager>
    <spring:delegate-security-provider
      name="memory-provider"
      delegate-ref="authenticationManager" />
  </spring:security-manager>
</mule>
```
xml## Validate Authentication with the Spring Authorization Filter

The Spring module adds support for a filter that fails if authentication cannot be validated using the Mule Security Manager:

```
<?xml version="1.0" encoding="UTF-8"?>
<mule
  xmlns:http="http://www.mulesoft.org/schema/mule/http"
  xmlns:db="http://www.mulesoft.org/schema/mule/db"
  xmlns:spring="http://www.mulesoft.org/schema/mule/spring"
  xmlns="http://www.mulesoft.org/schema/mule/core"
  xmlns:doc="http://www.mulesoft.org/schema/mule/documentation"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://www.springframework.org/schema/beans
    http://www.springframework.org/schema/beans/spring-beans-current.xsd
    http://www.mulesoft.org/schema/mule/core
    http://www.mulesoft.org/schema/mule/core/current/mule.xsd
    http://www.mulesoft.org/schema/mule/spring
    http://www.mulesoft.org/schema/mule/spring/current/mule-spring.xsd
    http://www.mulesoft.org/schema/mule/db
    http://www.mulesoft.org/schema/mule/db/current/mule-db.xsd
    http://www.mulesoft.org/schema/mule/http
    http://www.mulesoft.org/schema/mule/http/current/mule-http.xsd">
  <spring:config name="springConfig" files="beans.xml" />
  <spring:security-manager>
    <spring:delegate-security-provider
      name="memory-provider"
      delegate-ref="authenticationManager" />
  </spring:security-manager>
  <http:listener-config
    name="HTTP_Listener_config"
     doc:name="HTTP Listener config"  >
      <http:listener-connection
        host="0.0.0.0"
        port="9090" />
  </http:listener-config>
  <flow name="spring-exampleFlow"  >
    <http:listener
      config-ref="HTTP_Listener_config"
      path="/"
      doc:name="Listener"  />
    <http:basic-security-filter
      realm="mule" />
      <spring:authorization-filter
        requiredAuthorities="ROLE_ADMIN" />
  </flow>
</mule>
```
xmlThe `http:basic-security-filter` tries to authenticate the user using basic authentication. If the request is authenticated successfully, Mule retrieves the username and uses it in the Spring `authorization-filter` to search for that user and to try to authorize the request against the authority ROLE_ADMIN.

## See Also

- 
[Salesforce Help](https://help.salesforce.com)