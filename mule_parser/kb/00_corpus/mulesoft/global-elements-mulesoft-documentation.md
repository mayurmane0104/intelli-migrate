# Global Elements | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/mule-runtime/latest/global-elements](https://docs.mulesoft.com/mule-runtime/latest/global-elements)

---

![A menu for creating and managing global configuration elements in Mule](_images/mruntime-new-global-element.png) 

# Global Elements

A global element is a reusable object containing parameters that any number of elements in a flow can share. You reference a global element from Anypoint Connectors or components in your Mule application.

Use the global element to apply configuration details to multiple local elements in flows. Create one global element that defines parameters and configuration details, and then reference the global element from any flow element that uses this configuration. This practice enables you to ensure consistency across flow elements.

Note that some components require their properties stored in a global element.

## Benefits

Global elements provide many benefits to you as a Mule application developer: reusability, efficiency, and flexibility.

- 
Reusability You can configure a global element once and then share that configuration among processors of the same type. Configuring global elements is particularly useful when you have to define the connection details and login credentials for an external source, such as a SaaS application or database. 
- 
Efficiency You don’t have to change the same configuration multiple times for different processors in the flow if they all share a global element. For example, if you have multiple connectors that connect to the same service using one set of credentials, you can change the configuration in the global element and the changes apply to all flow elements that reference the global element. 
- 
Flexibility An element in a flow can apply a global element’s configuration exactly as defined, or it can apply modifications to the global configuration properties. 

## Before You Start

Review the features of the [Anypoint Studio visual editor](../../studio/) to learn more about developing Mule applications using the Anypoint Studio graphical user interface and to understand the context in which you use global elements.

## Create a Global Element

You can create global elements in two ways:

- 
From the **Global Elements**tab in the Anypoint Studio canvas
- 
From the properties panel of any connector or module that supports global elements 

### From the Anypoint Studio Canvas

- 
In the Anypoint Studio visual editor, click the **Global Elements**tab to access a list of all global elements in an application:![A menu for creating and managing global configuration elements in Mule](_images/mruntime-new-global-element.png)  
- 
Click **Create**to add a new global element.
- 
In the **Choose Global Type**wizard, navigate the directories or use the filter to select the type of global element you want to create, and then click**OK**.
- 
Define the configurable parameters of your global element in the **Global Element Properties**window.
- 
Click **OK**to save.

### From the Properties Panel of a Connector or Module

To create a new global element from within a local component you placed in your flow:

- 
Click the component you want to create a global element for: ![A basic flow component setup with error handling](_images/mruntime-global-element-component.png)  
- 
In the properties panel, click the Add icon next to the **Connector Configuration**:![An interface for creating a new global element in Mule](_images/mruntime-global-element-create.png)  
- 
Complete the required fields for the type of global element you want to create.