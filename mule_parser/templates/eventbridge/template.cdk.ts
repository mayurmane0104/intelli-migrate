new events.Rule(this, '{{resource_prefix}}Schedule', {
  ruleName: '{{resource_prefix}}-schedule',
  schedule: events.Schedule.rate(cdk.Duration.minutes(5)),
  targets: [new targets.LambdaFunction({{function_name}})]
});
