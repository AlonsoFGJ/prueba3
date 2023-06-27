import funciones as fp
import os
import numpy as np

valordias = 0
arreglo_hab = np.zeros((2,5),int)


lista_rut=[]
lista_nombredu=[]
lista_identi=[]
lista_nombrema=[]
lista_cantdi=[]

def validar_dias():
    while True:
        try:
            dias = int(input("Ingrese la cantidad de días que su mascota permanecerá en la guardería: "))
            if dias >= 1:
                return dias
            else:
                print("ERROR! Debe ingresar 1 o más días")
        except:
            print("ERROR! Debe ingresar un numero")

def identificador():
    for d in range(10):
        id = d
        print(f"Su identificador único es: {id}")
        return id

def validar_nombrema():
    while True:
        nombre = input("Ingrese nombre de la mascota: ")
        if len(nombre.strip()) >= 3 and nombre.isalpha():
            return nombre
        else:
            print("ERROR! EL NOMBRE DEBE TENER AL MENOS 3 LETRAS!")

def menu():
        print("""   Menú
        1.- Grabar
        2.- Buscar 
        3.- Retirarse
        4.- Salir""")

def opcion1():
    os.system('cls')
    rut = fp.validar_rut()
    nombredu = fp.validar_nombre()
    identi = identificador()
    nombrema = validar_nombrema()
    dias = validar_dias()

    lista_rut.append(rut)
    lista_nombredu.append(nombredu)
    lista_identi.append(identi)
    lista_nombrema.append(nombrema)
    lista_cantdi.append(dias)
    for x in range(2):
            print(f"N°{x+1}:", end="")
            for y in range(5):
                    print(arreglo_hab[x][y], end=" ")
    input("Elija una habitación para su mascota: ")

def opcion2():
    rut = fp.validar_rut
    if rut in range(len(lista_rut)):
        posicion = (len(lista_rut))
        
def opcion3():
    rut = fp.validar_rut
    if rut in range(len(lista_rut)):
        posicion = (len(lista_rut))
        valordias = dias * 15000
        




while True:
    os.system('cls')
    print(menu())
    opcion = fp.validar_opcion()
    
    if opcion==1:
        opcion1()
    elif opcion==2:
         opcion2()

    elif opcion==3:
        opcion3()
    else:
        print("Adios! :D")
        break