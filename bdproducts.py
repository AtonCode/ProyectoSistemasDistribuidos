import random
import json
import pymongo as db
import certifi

bdclient = db.MongoClient("mongodb://admin:<password>@ac-k7prfpv-shard-00-00.x7lltov.mongodb.net:27017,ac-k7prfpv-shard-00-01.x7lltov.mongodb.net:27017,ac-k7prfpv-shard-00-02.x7lltov.mongodb.net:27017/?ssl=true&replicaSet=atlas-zzo4os-shard-0&authSource=admin&retryWrites=true&w=majority", tlsCAFile=certifi.where())

mydb = bdclient['distribuidos']

mycol = mydb["catalogo"]

with open('data.json') as file: 
    file_data = json.load(file)
    print('Ha cargado el archivo')
      
if isinstance(file_data, list): 
    mycol.insert_many(file_data)
    print('Ha almacenado en la base de datos')   
else: 
    mycol.insert_one(file_data)