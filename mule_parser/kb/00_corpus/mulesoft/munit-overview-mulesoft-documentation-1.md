# MUnit Overview | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/munit/latest](https://docs.mulesoft.com/munit/latest)

---

```
<dependency>
	<groupId>com.mulesoft.munit</groupId>
	<artifactId>munit-runner</artifactId>
	<version>LATEST_VERSION</version> 
```
**(1)**
	<classifier>mule-plugin</classifier>
	<scope>test</scope>
</dependency>xml# MUnit Overview

Build automated tests for your integrations and APIs with MUnit. MUnit is a Mule application testing framework that provides a full suite of integration and unit test capabilities, and is fully integrated with Maven and Surefire for integration with your continuous deployment environment.

MUnit version 3.0 and later works with all Mule versions since 4.3.

With MUnit you can:

- 
Create your test by writing Mule code 
- 
Mock processors 
- 
Spy any processor 
- 
Verify processor calls 
- 
Enable or ignore particular tests 
- 
Tag tests 
- 
Generate coverage reports 

You can create, design, and run MUnit tests in Anypoint Studio and Anypoint Code Builder.

MUnit has two main sub modules:

- 
MUnit 
- 
MUnit Tools 

Each module has its dependency:

## MUnit Dependencies

| 1 | Check the [MUnit Release Notes](munit-release-notes)to get theLATEST_VERSION. | 

## MUnit Tools Dependencies

```
<dependency>
	<groupId>com.mulesoft.munit</groupId>
	<artifactId>munit-tools</artifactId>
	<version>LATEST_VERSION</version> 
```
**(1)**
	<classifier>mule-plugin</classifier>
	<scope>test</scope>
</dependency>xml| 1 | Check the [MUnit Release Notes](munit-release-notes)to get theLATEST_VERSION. |