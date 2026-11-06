# Java Module 2.0 | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/java-module/latest](https://docs.mulesoft.com/java-module/latest)

---

# Java Module 2.0

Release Notes: [Java Module Release Notes](../../release-notes/connector/java-module)

Exchange: [Java Module](https://www.mulesoft.com/exchange/org.mule.module/mule-java-module/)

Mule 4 is built to:

- 
Minimize the need for custom code. 
- 
Avoid the need for you to know or understand Java. 

However, some advanced uses cases require integration with custom Java code, such as:

- 
Reuse of a library, such as a tax calculation library. 
- 
Reuse of a canonical object model that is standard in the organization. 
- 
Execution of custom logic using Java. 

MEL previously served as a bridge for creating instances of Java classes and executing Java methods. In Mule 4, interoperation with Java changed, due to the replacement of MEL by DataWeave, which is a functional language. Functional languages do not have side effects on their input arguments, so it does not make sense for DataWeave to execute random instance methods on random object instances. Therefore, pure DataWeave supports calling only static Java methods, without use of the Java module.

## Java Module Versus the Scripting Module

You can use the Java module, or execute Groovy code through the
[Scripting module](../../scripting-module/latest/). However, the Scripting
module does not offer DataSense support, user interface support, visual aids
for methods available for each class, autocompletion, and so on. See
[Java Integration](../../mule-runtime/latest/).

## See Also

- 
[Salesforce Help](https://help.salesforce.com)