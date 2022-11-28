import boto3
import http.client
import errno
import socket
import json

def lambda_handler(event, context):
    client = boto3.client('lambda')
    websiteurl='54.173.151.187' #enter your site url
    metriname='Websitecode' #enter metric name
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((websiteurl, 80))
        response=client.invoke(
            FunctionName='SendMetric', #paste real name of the lambda function you defined.
            InvocationType='Event',
            LogType='Tail',
            Payload=json.dumps({"VAL": 200,"MNAM": metriname}) 
        )
        print("Metrics 200 sent to Cloudwatch")
    except socket.error as e:
        if 'Connection refused' in str(e):
            response=client.invoke(
                FunctionName='SendMetric', #paste real name of the lambda function you defined.
                InvocationType='Event',
                LogType='Tail',
                Payload=json.dumps({"VAL": 100,"MNAM": metriname}) 
            )
            print("Metrics 100 sent to Cloudwatch")
        else:
            response=client.invoke(
                FunctionName='SendMetric',
                InvocationType='Event',
                LogType='Tail',
                Payload=json.dumps({"VAL": 50,"MNAM": metriname}) 
            )
            print("Metrics 50 sent to Cloudwatch")