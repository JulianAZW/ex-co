import pickle
import random
class Tarjeta:
    def __init__(self , numero , saldo):
        self.numero=numero
        self.saldo=int(saldo)

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
                c.saldo=int(saldo)+int(c.saldo)
                print("Tu saldo nuevo es: ",c.saldo)
    else:
        if tarjetas.numero == nombre:
            tarjetas.saldo = saldo+tarjetas.saldo
            print("Tu saldo nuevo es: ", tarjetas.saldo)
    fichero_tarjetas = open("tarjetas_examen", "wb+")
    pickle.dump(tarjetas, fichero_tarjetas)
    fichero_tarjetas.close()

def consultaSaldo(nombre):
    fichero_apertura = open("tarjetas_examen", "rb+")
    tarjetas = pickle.load(fichero_apertura)
    fichero_apertura.close()
    if isinstance(tarjetas, list):
        for c in tarjetas:
            if c.numero==nombre:
                print("Tu saldo es: ",c.saldo)
    else:
        if tarjetas.numero == nombre:
            print("Tu saldo es: ", tarjetas.saldo)


def eliminarTarjetas():
    fichero_nuevo = open("tarjetas_examen", "wb+")
    tarjeta1=Tarjeta("2021",2021)
    pickle.dump(tarjeta1, fichero_nuevo)
    fichero_nuevo.close()


print("EXAMEN DE COMPUTACION - UNAM - FISICA")
n=0
while n!=5:
    print("BIENVENIDO AL MENU DEL SISTEMA DE VENTA Y RECARGAS DEL METRO\n")
    print("Presione el numero para ingresar a su funcion correspondiente\n")
    print("1.-Comprar una tarjeta\n")
    print("2.-Recargar saldo\n")
    '''PA EL PROFE'''
    print("3.-Consultar el saldo de mi tarjeta\n")
    print("4.-Consultar las BD del sistema\n")
    print("5.-Finalizar operacion")
    n=int(input())
    if n==1:
        print("Usted esta comprando una tarjeta")
        nombre= str(random.randrange(1000000000))
        print("Ingrese su saldo")
        saldo=input()
        agregarTarjeta(nombre,saldo)
        print("Su numero de tarjeta es:", nombre)
    elif n==2:
        print("Ingrese el numero de la tarjeta")
        nombre = input()
        print("Ingrese la cantidad a agregar")
        saldo = input()
        cambiarSaldo(nombre,saldo)
    elif n==4:
        consultarTarjeta()
    elif n==3:
        print("Ingrese el numero de la tarjeta")
        nombre = input()
        consultaSaldo(nombre)

