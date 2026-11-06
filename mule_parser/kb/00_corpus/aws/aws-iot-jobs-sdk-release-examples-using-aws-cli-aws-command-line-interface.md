# AWS IoT Jobs SDK release examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_iot-jobs-data-plane_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_iot-jobs-data-plane_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with AWS IoT Jobs SDK release.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `describe-job-execution`.

- **AWS CLI**
- 
            
                    **To get the details of a job execution**The following `describe-job-execution`example retrieves the details of the latest execution of the specified job and thing.`aws iot-jobs-data describe-job-execution \ --job-id``SampleJob`\ --thing-name`MotionSensor1`\ --endpoint-url`https://1234567890abcd.jobs.iot.us-west-2.amazonaws.com`Output: `{ "execution": { "approximateSecondsBeforeTimedOut": 88, "executionNumber": 2939653338, "jobId": "SampleJob", "lastUpdatedAt": 1567701875.743, "queuedAt": 1567701902.444, "status": "QUEUED", "thingName": "MotionSensor1 ", "versionNumber": 3 } }`For more information, see [Devices and Jobs](https://docs.aws.amazon.com/iot/latest/developerguide/jobs-devices.html)in the*AWS IoT Developer Guide*.- 
                    For API details, see [DescribeJobExecution](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot-jobs-data/describe-job-execution.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-pending-job-executions`.

- **AWS CLI**
- 
            
                    **To get a list of all jobs that are not in a terminal status for a thing**The following `get-pending-job-executions`example displays a list of all jobs that aren't in a terminal state for the specified thing.`aws iot-jobs-data get-pending-job-executions \ --thing-name``MotionSensor1`--endpoint-url`https://1234567890abcd.jobs.iot.us-west-2.amazonaws.com`Output: `{ "inProgressJobs": [ ], "queuedJobs": [ { "executionNumber": 2939653338, "jobId": "SampleJob", "lastUpdatedAt": 1567701875.743, "queuedAt": 1567701902.444, "versionNumber": 3 } ] }`For more information, see [Devices and Jobs](https://docs.aws.amazon.com/iot/latest/developerguide/jobs-devices.html)in the*AWS IoT Developer Guide*.- 
                    For API details, see [GetPendingJobExecutions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot-jobs-data/get-pending-job-executions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-next-pending-job-execution`.

- **AWS CLI**
- 
            
                    **To get and start the next pending job execution for a thing**The following `start-next-pending-job-execution`example retrieves and starts the next job execution whose status is IN_PROGRESS or QUEUED for the specified thing.`aws iot-jobs-data start-next-pending-job-execution \ --thing-name``MotionSensor1`--endpoint-url`https://1234567890abcd.jobs.iot.us-west-2.amazonaws.com`Output: `{ "execution": { "approximateSecondsBeforeTimedOut": 88, "executionNumber": 2939653338, "jobId": "SampleJob", "lastUpdatedAt": 1567714853.743, "queuedAt": 1567701902.444, "startedAt": 1567714871.690, "status": "IN_PROGRESS", "thingName": "MotionSensor1 ", "versionNumber": 3 } }`For more information, see [Devices and Jobs](https://docs.aws.amazon.com/iot/latest/developerguide/jobs-devices.html)in the*AWS IoT Developer Guide*.- 
                    For API details, see [StartNextPendingJobExecution](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot-jobs-data/start-next-pending-job-execution.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-job-execution`.

- **AWS CLI**
- 
            
                    **To update the status of a job execution**The following `update-job-execution`example updates the status of the specified job and thing.`aws iot-jobs-data update-job-execution \ --job-id``SampleJob`\ --thing-name`MotionSensor1`\ --status`REMOVED`\ --endpoint-url`https://1234567890abcd.jobs.iot.us-west-2.amazonaws.com`Output: `{ "executionState": { "status": "REMOVED", "versionNumber": 3 }, }`For more information, see [Devices and Jobs](https://docs.aws.amazon.com/iot/latest/developerguide/jobs-devices.html)in the*AWS IoT Developer Guide*.- 
                    For API details, see [UpdateJobExecution](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot-jobs-data/update-job-execution.html)in*AWS CLI Command Reference*.
 
-