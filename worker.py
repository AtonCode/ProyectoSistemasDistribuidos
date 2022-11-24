import sys
import threading
import zmq
import pymongo as db
import certifi

#El programa recibe la direccion y el puerto
#ex: 127.0.0.1:8010
port =  sys.argv[1]

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://100.96.1.2:"+port)


response = ''

bdclient = db.MongoClient("mongodb://admin:admin@ac-k7prfpv-shard-00-00.x7lltov.mongodb.net:27017,ac-k7prfpv-shard-00-01.x7lltov.mongodb.net:27017,ac-k7prfpv-shard-00-02.x7lltov.mongodb.net:27017/?ssl=true&replicaSet=atlas-zzo4os-shard-0&authSource=admin&retryWrites=true&w=majority", tlsCAFile=certifi.where())

mydb = bdclient['distribuidos']

mycol = mydb["catalogo"]




def create_products():
    response = ''
    x = mycol.find()
    for data in x:
        value = data['value']
        name = value['nombre']
        response = response + str(name) + '\n'
    return response

def search_id(nombre):
    response = ''
    x = mycol.find()
    for data in x:
        value = data['value']
        name = value['nombre']
        if (name == nombre):
            response = str(data['id'])
    if response == '':
        response = 'No existe ningun producto con ese nombre'
    return response


def health():
    alive = context.socket(zmq.REQ)
    alive.connect("tcp://127.0.0.1:8000")

    alive.send_string(dir)


def working():
    while True:
        msg_in = socket.recv_string()
        result = msg_in.split(maxsplit=1) 
        option = result[0]
        print(result[0])

        if option=="1":
            res = create_products()
            socket.send_string(res)
        
        elif option=="2":
            id = search_id(result[1])
            myquery = { 'id': id} 
            mycol.delete_one(myquery)
            socket.send_string("Elemento " + result[1] + " comprado con éxito")


health()
working()









