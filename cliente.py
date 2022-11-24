import zmq
import pymongo as db
import certifi
from time import time

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://100.96.1.18:8001")

bdclient = db.MongoClient("mongodb://admin:admin@ac-k7prfpv-shard-00-00.x7lltov.mongodb.net:27017,ac-k7prfpv-shard-00-01.x7lltov.mongodb.net:27017,ac-k7prfpv-shard-00-02.x7lltov.mongodb.net:27017/?ssl=true&replicaSet=atlas-zzo4os-shard-0&authSource=admin&retryWrites=true&w=majority", tlsCAFile=certifi.where())

mydb = bdclient['distribuidos']

mycol = mydb["users"]
start_time = 0;
valid = 1
def menu():
    opcion=0
    print('')
    print("_______________________")
    print("MENU TIENDA DISTRIBUIDA")
    print("1. Ver catalogo")
    print("2. comprar articulo por nombre (Ingrese la opción acompañada del nombre del articulo)")
    print("3. salir")
    inp=int(input("Ingrese una opción:  "))
    if 0<inp and inp<4:
        opcion=inp
        start_time = time()
    else:
        while(inp<1 and 3<inp):
            print("opción inválida...")
            inp=int(input("Ingrese una opción:  "))
        opcion=inp
    return opcion

opt=0

def validar(username, password):
    x = mycol.find_one({"username":username})
    passworddb = x['password']

    if (passworddb == password):
        return 0
    else:
        return 1

def login():
    username = (input("Ingrese un usuario:  "))
    password = (input("Ingrese un la contraseña:  "))
    return validar(username, password)

def inicio():
    opcion=0
    print('')
    print("_______________________")
    print("Bienvenido a nuestra tienda")
    print("1. Iniciar Sesión")
    print("2. Registrarse")
    print("3. salir")
    inp=int(input("Ingrese una opción:  "))
    if 0<inp and inp<4:
        opcion=inp
    else:
        while(inp<1 and 3<inp):
            print("opción inválida...")
            inp=int(input("Ingrese una opción:  "))
        opcion=inp
    return opcion

def registrarse():
    username = (input("Ingrese un usuario:  "))
    password = (input("Ingrese un la contraseña:  "))

    newUser = { "username": username, "password": password } 

    mycol.insert_one(newUser)


def iniciar():
    if startopt==1:
        return login()
    elif startopt==2:
        registrarse()
        print('--------------------------------------')
        print('\n' + 'Estas listo para iniciar sesión')
        return login()

while opt!=3:
    startopt = inicio()
    valid = iniciar()
    

    if valid == 0:
        opt=menu()
        if opt==1:
            #mensaje de ver todo
            print("catalogo")
            msg = "1"
            socket.send_string(msg)
            msg_in = socket.recv_string()
            elapsed_time = time() - start_time
            print(msg_in)
            print('El tiempo de ejecución es: ' + str(elapsed_time))
        elif opt==2:
            product=(input("Ingrese el nombre del producto:  ")) 
            #mensaje de comprar
            print("comprar")
            msg = "2 " + product 
            socket.send_string(msg)
            msg_in = socket.recv_string()
            elapsed_time = time() - start_time
            print(msg_in)
            print('El tiempo de ejecución es: ' + str(elapsed_time))
    elif valid == 1:
        print('Algo falló revisa tu usario o contraseña')
    
    