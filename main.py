import pickle

class Tarjeta:
    def __init__(self , numero , saldo):
        self.numero=numero
        self.saldo=saldo

    def imprime(self):
        print("Numero: ",self.numero,"\n Saldo: ",self.saldo)

def  agregarTarjeta(nombre,saldo):
    tarjetas1=[];
    tarjeta=Tarjeta(nombre,saldo)
    fichero_apertura = open("tarjetas_examen", "rb+")
    tarjetas = pickle.load(fichero_apertura)
    fichero_apertura.close()
    fichero_tarjetas = open("tarjetas_examen", "wb+")
    if isinstance(tarjetas,list):
        tarjetas.append(tarjeta)
        pickle.dump(tarjetas,fichero_tarjetas)
    else:
        tarjetas1.append(tarjetas)
        tarjetas1.append(tarjeta)
        pickle.dump(tarjetas1, fichero_tarjetas)
    fichero_tarjetas.close()


def consultarTarjeta():
    fichero_apertura = open("tarjetas_examen", "rb+")
    tarjetas = pickle.load(fichero_apertura)
    if isinstance(tarjetas,list):
        for c in tarjetas:
            Tarjeta.imprime(c)
    else:
        Tarjeta.imprime(tarjetas)
    fichero_apertura.close()


def cambiarSaldo(nombre,saldo):
    fichero_apertura = open("tarjetas_examen", "rb+")
    tarjetas = pickle.load(fichero_apertura)
    fichero_apertura.close()
    if isinstance(tarjetas, list):
        for c in tarjetas:
            if c.numero==nombre:
                c.saldo=saldo
    else:
        if tarjetas.numero == nombre:
            tarjetas.saldo = saldo
    fichero_tarjetas = open("tarjetas_examen", "wb+")
    pickle.dump(tarjetas, fichero_tarjetas)
    fichero_tarjetas.close()

def eliminarTarjetas():
    fichero_nuevo = open("tarjetas_examen", "wb+")
    tarjeta1=Tarjeta("1","1")
    pickle.dump(tarjeta1, fichero_nuevo)
    fichero_nuevo.close()


eliminarTarjetas()

print("EXAMEN DE COMPUTACION - UNAM - FISICA")
n=0
while n!=4:
    print("BIENVENIDO AL MENU DEL SISTEMA DE VENTA Y RECARGAS DEL METRO\n")
    print("Presione el numero para ingresar a su funcion correspondiente\n")
    print("1.-Agregar tarjetas\n")
    print("2.-Cambiar el saldo de alguna tarjeta\n")
    print("3.-Consultar las BD del sistema\n")
    print("4.-Salir del sistema")
    n=int(input())
    if n==1:
        print("Ingrese el numero de la tarjeta")
        nombre=input()
        print("Ingrese su saldo")
        saldo=input()
        agregarTarjeta(nombre,saldo)
    elif n==2:
        print("Ingrese el numero de la tarjeta")
        nombre = input()
        print("Ingrese su nuevo saldo")
        saldo = input()
        cambiarSaldo(nombre,saldo)
    elif n==3:
        consultarTarjeta()
