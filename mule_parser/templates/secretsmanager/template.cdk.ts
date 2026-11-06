new secretsmanager.Secret(this, '{{resource_prefix}}Secret', {
  secretName: 'mule-migration/{{resource_prefix}}',
  description: 'Migrated Mule secret reference'
});
