#!/usr/bin/python

import boto3

#Create Free teir Instance
ec2 = boto3.resource('ec2')
instance = ec2.create_instances(
    ImageId='ami-03291866',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    KeyName='keyPair',
    SecurityGroupIds=['sg-xxxxxxxxxx',])
print instance[0].id
