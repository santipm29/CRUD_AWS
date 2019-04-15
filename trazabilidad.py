import json, boto3, os, datetime, requests
from requests_aws4auth import AWS4Auth
from pytz import timezone

tz = timezone('America/Bogota')
fmt_elastic = "%Y-%m-%dT%H:%M:%S-05:00"
region = 'us-east-1' 
service = 'es'
credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)
host = 'https://search-setitalleraws-dv6uogranpir4guprd3lpjliau.us-east-1.es.amazonaws.com'
headers = { "Content-Type": "application/json" }


def elastic(message):
    #url = (f'{host}/talleraws/request')
    url = host + "/talleraws/request"
    
    r = requests.post(url, auth=awsauth, json=message, headers=headers) 
    print(r.text)
    
def recibir(event, context):
    message = event['Records'][0]['Sns']['Message']
    payload = {"timestamp": datetime.datetime.now(tz).strftime(fmt_elastic),"mensaje": json.loads(message)}
    print(payload)
    elastic(payload)
