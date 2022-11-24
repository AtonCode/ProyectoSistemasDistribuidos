### PROYECTO SISTEMAS DISTRIBUIDOS ###

Autores:
    * Tatiana Peña
    * Pablo Bright
    * Alejandro Sacristan

> Descrición --> Sistema distribuido de tienda virtual, se utiliza un cliente, un balanceador de carga y trabajadores

# ¿Cómo correrlo? #

* Primero se debe ejecutar el código del balanceador [balanceador.py]
* Ahora se pueden crear trabajadores, estos reciben un argumento, su dirección y puerto por el que se van a comunicar
        > Se usa worker.py 192.168.0.2:8080 <-- está es una dirección ejemplo, se debe ingresar la de la máquina en la que corre el worker, y un puerto diferente por worker.
* El cliente se puede iniciar en cualquier momento [cliente.py]
        > El cliente ofrece un menú
            -> La opción **1** > Da la información completa del catalogo al cliente y imprime en pantalla
            -> La opción **2** > Pide el nombre de un producto para comprar -> Al comprarlo se elimina de la base de datos
            -> La opción **3** > Termina el proceso del cliente