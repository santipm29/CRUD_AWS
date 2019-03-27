import json
from user import mongo

def delete(event, context):
    parameter = False
    try:
        id = event["pathParameters"]["id"]
        parameter = True
    except Exception as e:
        print("Error: ", e)

    if parameter:
        res = mongo.delete("user", id)
    else:
        res = {"mensaje" : "No se recibio el id del usuario"}
 
    response = {"statusCode": 200, "body": json.dumps( res )}       
    return response