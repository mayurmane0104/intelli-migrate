new ssm.StringParameter(this, '{{resource_prefix}}RdsEndpointParameter', {
  parameterName: '/{{resource_prefix}}/rds/endpoint',
  stringValue: 'REPLACE_WITH_RDS_PROXY_ENDPOINT'
});
