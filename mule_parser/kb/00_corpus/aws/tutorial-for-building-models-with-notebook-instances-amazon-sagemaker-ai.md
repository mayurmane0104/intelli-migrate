# Tutorial for building models with Notebook Instances - Amazon SageMaker AI

**Source:** [https://docs.aws.amazon.com/sagemaker/latest/dg/gs-console.html](https://docs.aws.amazon.com/sagemaker/latest/dg/gs-console.html)

---

[Disaggregated Prefill and Decode for HyperPod inference](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-model-deployment-dpd.html)

*13 June 2026*

We use essential cookies and similar tools that are necessary to provide our site and services. We use performance cookies to collect anonymous statistics, so we can understand how customers use our site and make improvements. Essential cookies cannot be deactivated, but you can choose “Customize” or “Decline” to decline performance cookies. 

 If you agree, AWS and approved third parties will also use cookies to provide useful site features, remember your preferences, and display relevant content, including relevant advertising. To accept or decline all non-essential cookies, choose “Accept” or “Decline.” To make more detailed choices, choose “Customize.”

Essential cookies are necessary to provide our site and services and cannot be deactivated. They are usually set in response to your actions on the site, such as setting your privacy preferences, signing in, or filling in forms.

Performance cookies provide anonymous statistics about how customers navigate our site so we can improve site experience and performance. Approved third parties may perform analytics on our behalf, but they cannot use the data for their own purposes.

Functional cookies help us provide useful site features, remember your preferences, and display relevant content. Approved third parties may set these cookies to provide certain site features. If you do not allow these cookies, then some or all of these services may not function properly.

Advertising cookies may be set through our site by us or our advertising partners and help us deliver relevant marketing content. If you do not allow these cookies, you will experience less relevant advertising.

Blocking some types of cookies may impact your experience of our sites. You may review and change your choices at any time by selecting Cookie preferences in the footer of this site. We and selected third-parties use cookies or similar technologies as specified in the [AWS Cookie Notice](https://aws.amazon.com/legal/cookies/).

We will only store essential cookies at this time, because we were unable to save your cookie preferences.

If you want to change your cookie preferences, try again later using the link in the AWS console footer, or contact support if the problem persists.

This Get Started tutorial walks you through how to create a SageMaker notebook instance, open a Jupyter notebook with a preconfigured kernel with the Conda environment for machine learning, and start a SageMaker AI session to run an end-to-end ML cycle. You'll learn how to save a dataset to a default Amazon S3 bucket automatically paired with the SageMaker AI session, submit a training job of an ML model to Amazon EC2, and deploy the trained model for prediction by hosting or batch inferencing through Amazon EC2.

This tutorial explicitly shows a complete ML flow of training the XGBoost model from
            the SageMaker AI built-in model pool. You use the [US Adult Census dataset](https://archive.ics.uci.edu/ml/datasets/adult),
            and you evaluate the performance of the trained SageMaker AI XGBoost model on predicting
            individuals' income.

[SageMaker AI
                        XGBoost](https://docs.aws.amazon.com/sagemaker/latest/dg/xgboost.html) – The [XGBoost](https://xgboost.readthedocs.io/en/latest/) model is
                    adapted to the SageMaker AI environment and preconfigured as Docker containers. SageMaker AI
                    provides a suite of 

[Adult Census
                        dataset](https://archive.ics.uci.edu/ml/datasets/adult) – The dataset from the 

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

Tutorials cover training ML models SQL, predicting churn, K-means clustering, XGBoost, multi-class classification, regression.

Train ML models SQL statements; SageMaker AI Autopilot integration enables predictions within Redshift clusters.

Fully managed ML service enables building, training, deploying models; renamed SageMaker AI December 2024.

Administrators configure unified AWS data, AI, ML analytics platform managing users, access, governance, generative AI development.

SageMaker built-in algorithms support tabular, text, image, time-series supervised unsupervised ML tasks.