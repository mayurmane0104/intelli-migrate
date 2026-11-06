new apigw.LambdaRestApi(this, '{{resource_prefix}}Api', {
  restApiName: '{{resource_prefix}}-api',
  handler: {{function_name}},
  deployOptions: {
    stageName: 'prod',
    metricsEnabled: true,
    loggingLevel: apigw.MethodLoggingLevel.INFO
  }
});
