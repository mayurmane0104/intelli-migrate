const {{resource_prefix}}Role = new iam.Role(this, '{{resource_prefix}}Role', {
  roleName: '{{resource_prefix}}-lambda-role',
  assumedBy: new iam.ServicePrincipal('lambda.amazonaws.com')
});
