UPDATE CLOUDWATCH ALARM USING BOTO3

import boto3

def lambda_handler(event, context):
    # Define parameters for updating the CloudWatch alarm
    alarm_name = 'ApplicationInsights/AWS_AppRegistry_Application-BODSDBDev/AWS/EBS/VolumeQueueLength/vol-0545101b9457d081d/'
    actions_enabled = True
    ok_actions = ['arn:aws:sns:ap-southeast-2:931636534260:S4HanaCloudwatchAlerts']
    alarm_actions = ['arn:aws:sns:ap-southeast-2:931636534260:S4HanaCloudwatchAlerts']
    insufficient_data_actions = ['arn:aws:sns:ap-southeast-2:931636534260:S4HanaCloudwatchAlerts']
    
    # Update the CloudWatch alarm
    update_cloudwatch_alarm(alarm_name, actions_enabled, ok_actions, alarm_actions, insufficient_data_actions)

def update_cloudwatch_alarm(alarm_name, actions_enabled, ok_actions, alarm_actions, insufficient_data_actions):
    # Create a CloudWatch client
    client = boto3.client('cloudwatch')

    # Update the CloudWatch alarm
    response = client.put_metric_alarm(
        AlarmName=alarm_name,
        ActionsEnabled=actions_enabled,
        OKActions=ok_actions,
        AlarmActions=alarm_actions,
        EvaluationPeriods=2,
        MetricName='VolumeQueueLength',
        Period=30,
        Namespace='AWS/EBS',
        ComparisonOperator='GreaterThanOrEqualToThreshold',
        Statistic='Average',
        Threshold=90,
        InsufficientDataActions=insufficient_data_actions
        # Add other parameters as needed
    )

    print("CloudWatch alarm updated successfully.")


# THIS ONE IS FOR MULTIPLE ALARMS USING FOR LOOP

--contributor: Aditya Pandita--

import boto3

def lambda_handler(event, context):
    # Define parameters for updating the CloudWatch alarms
    alarm_names = [
        'ApplicationInsights/AWS_AppRegistry_Application-BODSDBDev/AWS/EBS/VolumeQueueLength/vol-0545101b9457d081d/',
        'AnotherAlarmName',
        'YetAnotherAlarmName'
    ]
    actions_enabled = True
    ok_actions = ['arn:aws:sns:ap-southeast-2:931636534260:S4HanaCloudwatchAlerts']
    alarm_actions = ['arn:aws:sns:ap-southeast-2:931636534260:S4HanaCloudwatchAlerts']
    insufficient_data_actions = ['arn:aws:sns:ap-southeast-2:931636534260:S4HanaCloudwatchAlerts']
    
    # Update each CloudWatch alarm
    for alarm_name in alarm_names:
        update_cloudwatch_alarm(alarm_name, actions_enabled, ok_actions, alarm_actions, insufficient_data_actions)

def update_cloudwatch_alarm(alarm_name, actions_enabled, ok_actions, alarm_actions, insufficient_data_actions):
    # Create a CloudWatch client
    client = boto3.client('cloudwatch')

    # Update the CloudWatch alarm
    response = client.put_metric_alarm(
        AlarmName=alarm_name,
        ActionsEnabled=actions_enabled,
        OKActions=ok_actions,
        AlarmActions=alarm_actions,
        EvaluationPeriods=2,
        MetricName='VolumeQueueLength',
        Period=30,
        Namespace='AWS/EBS',
        ComparisonOperator='GreaterThanOrEqualToThreshold',
        Statistic='Average',
        Threshold=90,
        InsufficientDataActions=insufficient_data_actions
        # Add other parameters as needed
    )

    print(f"CloudWatch alarm '{alarm_name}' updated successfully.")
