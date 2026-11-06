const {{resource_prefix}}Certificate = new acm.Certificate(this, '{{resource_prefix}}Certificate', {
  domainName: '{{domain_name}}',
  validation: acm.CertificateValidation.fromDns()
});
