import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    instance_id = "YOUR_DEV_EC2_ID"
    ec2.start_instances(InstanceIds=[instance_id])
    return "Dev WordPress started"
