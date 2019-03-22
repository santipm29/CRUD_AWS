import pymongo

CLIENT = pymongo.MongoClient('mongodb://52.90.145.195:27017/')
DATABASE = CLIENT["santiagopatino"]


def insert(col, message):
    collection = DATABASE[col]
    try:
        registry = collection.insert_one(message)
        response = (f'Guardado correctamente con ID {registry.inserted_id}')
    except Exception as e:
        response = (f'Error al guardar {e}') 
        
    return response

def update(col, id):
    collection = DATABASE[col]
    try:
        print("update")

    except Exception as e:
        response = {f' {e}'}