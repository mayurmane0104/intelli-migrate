# Move Transformation to Separate Files (Anypoint Studio) | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/mule-runtime/latest/transform-move-transformations-separate-file-studio-task](https://docs.mulesoft.com/mule-runtime/latest/transform-move-transformations-separate-file-studio-task)

---

![An edit icon in the Transform Message component](_images/dw-multiple-outputs-edit.png) 

# Move Transformation to Separate Files (Anypoint Studio)

By default, the DataWeave code from a Transform Message component is expressed inline within your Mule XML file. You can instead keep each in a separate file ( `.dwl` ) and have your XML reference them. These files are packaged with your Mule application when built.

To export the DataWeave code to a `.dwl` file:

- 
Click the **Edit Current Target**button.![An edit icon in the Transform Message component](_images/dw-multiple-outputs-edit.png)  
- 
Select the **File**radio button.![A target output payload with an option to choose a source code](_images/dataweave-externalfile2.png)  - 
Type a name for your `.dwl`file.
- 
Click **OK**.
 
- 

A file is created under the `src/main/resources` folder in your project containing your DataWeave code.