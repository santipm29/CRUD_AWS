import json, mongo

def get(event, context):
    parameter = False
    try:
        id = event["pathParameters"]["id"]
        parameter = True
    except Exception as e:
        print("Error: ", e)

    if parameter:
        res = mongo.getUser("user", id)
    else:
        res = mongo.getUsers("user")
 
    response = {"statusCode": 200, "body": json.dumps( res )}       
    return response

