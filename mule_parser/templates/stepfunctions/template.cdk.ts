const {{resource_prefix}}Workflow = new sfn.StateMachine(this, '{{resource_prefix}}Workflow', {
  stateMachineName: '{{resource_prefix}}-workflow',
  definitionBody: sfn.DefinitionBody.fromChainable(
    new tasks.LambdaInvoke(this, '{{resource_prefix}}Invoke', {
      lambdaFunction: {{function_name}}
    })
  )
});
