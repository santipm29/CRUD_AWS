import pymongo
from bson.objectid import ObjectId

CLIENT = pymongo.MongoClient('mongodb://52.90.145.195:27017/')
DATABASE = CLIENT["santiagopatino"]


def insert(col, message):
    collection = DATABASE[col]
    try:
        registry = collection.insert_one(message)
        response = {"mensaje": "Usuario creado correctamente", "id": str(registry.inserted_id)}
    except Exception as e:
        print(f'Error: {e}')
        response = {"mensaje": "Error al guardar"}
        
    return response

def update(col, id):
    collection = DATABASE[col]
    try:
        print("update")

    except Exception as e:
        response = {f' {e}'}

def delete(col, id):
    collection = DATABASE[col]
    response = {}
    try:
        resQuery = collection.delete_one({"_id": ObjectId(str(id))})
    except Exception as e:
        print("Error: ", e)
        response["mensaje"] = "Error al eliminar el usuario"  
    if resQuery.deleted_count > 0:
        response["mensaje"] = "Usuario eliminado correctamente"
    return response    

def getUser(col, id):
    collection = DATABASE[col]
    data = {}
    try:
        for x in collection.find( {"_id" : ObjectId(id)}):
            x['_id'] = str(x['_id'])
            data = x
    except Exception as e:
        print({f'Error: {e}'})
        data["mensaje"] =  "Error al encontrar usuario"
    
    if not data:
        data["mensaje"] = "Usuario no encontrado"
    return data

def getUsers(col):
    collection = DATABASE[col]
    data = []
    try:
        for x in collection.find():
            x['_id'] = str(x['_id'])
            data.append(x)
    except Exception as e:
        print({f'Error: {e}'})
        data.append({"mensaje": "Error al obtener los usuarios"})

    '' if data else data.append({"mensaje":"No hay usuarios registrados"})
    return data

