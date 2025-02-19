'''
Demo following this walkthrough:
https://www.youtube.com/watch?v=N3dIDz73J30&list=PL8tc66sMn9Kg05l6kvL_ujHKfaLi3fHLH&index=3&ab_channel=AnjaliSharma

1. log into the AWS management console
2. go to the services ec2, s3, iam, etc... just like you would through the GUI
3. Select IAM (Identity Access Mgmt) users, groups, roles, policies, etc.

See the aws_rootkey.csv file for the AWS credentials. Using a AWS user we called demo_user
'''

# session: AWS mgmt console
import boto3
import boto3.session

aws_mgmt_console = boto3.session.Session(profile_name='demo_user')
# for IAM you dont need to specify region_name since it is global but it is good practice
iam_resource_console = aws_mgmt_console.resource(service_name='iam', region_name='us-east-2')

# list all IAM users available (should just be demo_user as at the time thats all we created)
for user in iam_resource_console.users.all():
    print(user.name)

# see available methods for aws mgmt console
print(dir(aws_mgmt_console))

# see which resources are accessible through resource method
print(aws_mgmt_console.get_available_resources())
# ['cloudformation', 'cloudwatch', 'dynamodb', 'ec2', 'glacier', 'iam', 'opsworks', 's3', 'sns', 'sqs']

''' 
if an AWS service is not available as a resource you will need to access as a client, 
and some you can access as either such as IAM. 

Notice looking at users as the client with list_users() returns a dictionary so you will need to 
access through the dictionary. 
'''

iam_client_console = aws_mgmt_console.client(service_name='iam', region_name='us-east-2')
print(iam_client_console.list_users())
# print the users 
for user in iam_client_console.list_users()['Users']:
    print(user['UserName'])

