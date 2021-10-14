#!/usr/bin/python3

import boto3
import sys

# The calls to AWS STS AssumeRole must be signed with the access key ID
# and secret access key of an existing IAM user or by using existing temporary 
# credentials such as those from another role. (You cannot call AssumeRole 
# with the access key for the root account.) The credentials can be in 
# environment variables or in a configuration file and will be discovered 
# automatically by the boto3.client() function. For more information, see the 
# Python SDK documentation: 
# http://boto3.readthedocs.io/en/latest/reference/services/sts.html#client

# create an STS client object that represents a live connection to the 
# STS service

access_key=sys.argv[1]
secret_key=sys.argv[2]
acc_name=sys.argv[3]
link_name_account= {}

role_arn= "arn:aws:iam::"+link_name_account[acc_name]+":role/aws-auth"
sts_client = boto3.client('sts', aws_access_key_id=access_key,
                    aws_secret_access_key=secret_key, )
# # Call the assume_role method of the STSConnection object and pass the role
# ARN and a role session name.

assumed_role_object=sts_client.assume_role(
    RoleArn=role_arn,
    RoleSessionName="AssumeRoleName1",
    DurationSeconds=43200,
)

# From the response that contains the assumed role, get the temporary 
# credentials that can be used to make subsequent API calls
credentials=assumed_role_object['Credentials']

# Use the temporary credentials that AssumeRole returns to make a 
# connection to Amazon S3  
print("Adicionar esse profile no seu arquivo credentials \n")
print("["+acc_name+"-sts]")
print("aws_access_key_id="+ credentials['AccessKeyId'])
print("aws_secret_access_key="+ credentials['SecretAccessKey'])
print("aws_session_token=\""+credentials['SessionToken']+"\"")
