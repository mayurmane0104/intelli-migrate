new cloudwatch.Alarm(this, '{{resource_prefix}}ErrorsAlarm', {
  alarmName: '{{resource_prefix}}-lambda-errors',
  metric: {{function_name}}.metricErrors(),
  threshold: 1,
  evaluationPeriods: 1
});
