# Customizations - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/customizations.html](https://docs.aws.amazon.com/quick/latest/userguide/customizations.html)

---

Using Amazon Quick, you can create a customized experience for people using either the AWS Management Console or Quick consoles embedded in your application.

Currently, different options for customizing Quick are available separately in the console and the Quick API. Following, you can find information about the available options.

The following customization options are currently available:

- 
                You can customize the welcome content Quick provides for new users: - 
                        You can accept or decline the sample assets. These assets include sample datasets and analyses that are added when a person signs in for the first time. 
- 
                        You can show or hide default introductory videos. These videos include the animation that displays for new users and also the tutorial videos shown on the Amazon Quick home page. 
 
- 
                        
- 
                You can create and specify a default theme. 
- 
                You can customize dashboard report emails, pixel perfect report emails, and alert emails by editing the email template. 

###### Important

All customizations apply only to the AWS Region that you are using in the API or that is selected in the Amazon Quick console.

To check your Region setting, you can use one of the following procedures.

###### To check your AWS Region on the Amazon Quick console

- 
                Choose your profile icon to open the menu. 
- 
                View your current AWS Region, listed next to a location icon. 
- 
                (Optional) Choose another AWS Region from the menu to change to that Region. Remember to change back after you are finished with customizations. 

###### To check your AWS Region using the AWS CLI

- 
                On the command line, enter the following command and press Enter to view the current settings. `aws configure list`To reconfigure your default Region, use the `aws configure`command.

To keep your default Region, you can add the `--region` parameter to most
            CLI commands.