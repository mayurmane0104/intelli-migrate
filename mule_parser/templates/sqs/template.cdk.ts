const {{resource_prefix}}Queue = new sqs.Queue(this, '{{resource_prefix}}Queue', {
  queueName: '{{resource_prefix}}-queue',
  encryption: sqs.QueueEncryption.SQS_MANAGED
});
