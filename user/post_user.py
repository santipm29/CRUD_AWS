import json
from user import mongo
from jsonschema import Draft4Validator

def load_file(name):
    with open(name) as f:
        return json.load(f)

def type(name):
        types = {'string' : 'caracter', 'number' : 'numérico', 'object': 'objeto'}
        if name in types:
            return types[name]

def beautify(path, instance, message, validator_value):
    if 'is not of type' in message:
        return 'El campo \''+str(path[-1]) +'\' con el valor \''  + str(instance) +'\' debe ser de tipo ' + type(validator_value)
    elif 'is a required property' in message:
        return 'El campo '+message.replace('is a required property','es obligatorio')
    elif 'is too short' in message and len(instance)==0:
        return 'El campo \''+str(path[-1]) +'\' es obligatorio'
    else:
        return message

def validate(message):
    SCHEMA = load_file('validation/jsonschema.json')
    v = Draft4Validator(SCHEMA)
    errors = []
    for error in sorted(v.iter_errors(message), key=str):
        errors.append({"mensaje" : beautify(error.path,error.instance,error.message, error.validator_value)})
        
    return errors


def post(event, context):
    body = json.loads(event["body"])
    errors = validate(body)
    resp = []
    if not errors:
        resp.append(mongo.insert("user", body))
    else:
        resp.append(errors)
            
            
    response = {"statusCode": 200, "body": json.dumps( resp )}
    return response



