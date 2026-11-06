const {{function_name}} = new lambda.Function(this, '{{resource_prefix}}Function', {
  functionName: '{{resource_prefix}}-handler',
  runtime: {{runtime}},
  handler: '{{handler}}',
  code: lambda.Code.fromAsset('generated/app'),
  environment: {
    PARAMETER_PATH: '/{{resource_prefix}}/'
  }
});
