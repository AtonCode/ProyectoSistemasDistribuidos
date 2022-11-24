import threading
from time import sleep
import zmq

context = zmq.Context()
alCliente = context.socket(zmq.REP)
alCliente.bind("tcp://*:8001")

workerCheck = context.socket(zmq.REP)
workerCheck.bind("tcp://*:8000")

workers=[]

def conocer():
    while True: 
        newWorker = workerCheck.recv_string()

        workers.append(newWorker)

        workerCheck.send_string("conectado")

        print("new worker: "+newWorker)

def normal():
    while True:
        if len(workers)!=0:
            for i in range(len(workers)):
                print(workers)
                sock = context.socket(zmq.REQ)
                sock.connect("tcp://"+workers[i])

                msg_in = alCliente.recv_string()

                print(msg_in)

                sock.send_string(msg_in)

                sock.RCVTIMEO = 10000
                try:
                    repl=sock.recv_string()
                except:
                    #if len(workers)>1:
                        #sock.connect("tcp://"+workers[(i+1)%(len(workers)-1)])
                        #repl=sock.recv_string()
                        #Aqui la idea es que se lo mande a otro worker, pero se pifea
                    repl="Hubo un problema...."
                    workers.remove(workers[i])

                alCliente.send_string(repl)
        else:
            pass


mainThread = threading.Thread(target=normal)
healthCheck = threading.Thread(target=conocer)

mainThread.start()
healthCheck.start()
