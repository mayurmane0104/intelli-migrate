# Deployment Properties for Mule Applications | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/anypoint-code-builder/ref-deployment](https://docs.mulesoft.com/anypoint-code-builder/ref-deployment)

---

```
{
  "runtime": "4.7-e-java17",
  "workerSize": 0.1,
  "applicationName": "my-integration-app",
  "workers": 1,
  "autoStart": true
}
```
# Deployment Properties for Mule Applications

When deploying a Mule application to CloudHub, Anypoint Code Builder relies on a configuration in `deploy.json`. Mule applications are integration or implementation projects.

The `deploy.json` and `deploy_ch2.json` files contain the following properties for deployments of Mule applications to CloudHub and CloudHub 2.0, respectively, from Anypoint Code Builder.

| Property | Description | Host | 
|---|---|---|
| 
 | Provides the Mule runtime version used by the project. | CloudHub or CloudHub 2.0 | 
| 
 | Sets the worker memory relative to a single worker or a number of available workers. The default is  | CloudHub | 
| 
 | Sets the replica specific amount of memory capacity and processing power. The default value is  | CloudHub 2.0 | 
| 
 | Provides the hyphenated, lowercase name of the Mule application. | CloudHub or CloudHub 2.0 | 
| 
 | Sets the number of Mule runtime instances for running this Mule application. The default is  | CloudHub | 
| 
 | Sets dedicated instances of Mule runtime engine for running this Mule application. The default is  | CloudHub | 
| 
 | Indicates whether to start the application automatically after the deployment process completes. The default value is  | CloudHub or CloudHub 2.0 | 
| 
 | Indicates the model by which you want the replicas of your application to be updated or redeployed. The default value is  | CloudHub 2.0 | 
| 
 | Indicates whether Object Store v2 is enabled  for this application. The default value is  | CloudHub or CloudHub 2.0 |