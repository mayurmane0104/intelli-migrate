new ssm.StringParameter(this, '{{resource_prefix}}Parameter', {
  parameterName: '/{{resource_prefix}}/config',
  stringValue: 'REPLACE_AT_DEPLOYMENT'
});
