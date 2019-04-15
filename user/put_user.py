import json
from user import mongo

def put(event, context):
    parameter = False
    res = {}
    try:
        id = event["pathParameters"]["id"]
        body = json.loads(event["body"])
        parameter = True
    except Exception as e:
        print("Error: ", e)

    if parameter:
        res["mensaje"] = mongo.update('user', id, body)   
    else:
        res["mensaje"] = "No se recibió el id del cliente"
 
    response = {"statusCode": 200, "body": json.dumps( res )}       
    return response
