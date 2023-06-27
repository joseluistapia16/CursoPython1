from procesos.operaciones import *
from entradas.entradas import *
"""
def funcion3():
    numero1 = int(input("Numero 1:"))
    numero2 = int(input("Numero 2:"))
    x = suma(numero1,numero2)
    print("Total:"+str(x))

def funcion4():
    estudiante = input("Nombre de estudiante:")
    materia = input("Materia:")
    nota1 = float(input("Nota 1:"))
    nota2 = float(input("Nota 2:"))
    nota3 = float(input("Nota 3:"))
    res = promedio(nota1,nota2,nota3)
    print("Promedio:"+str(res))
    msg = mensaje(res)
    print(msg)

def funcion5():
    rol = input("Rol:").upper()
    msg = getRol(rol)
    print(msg)


def funcion6():
    edad = int(input("Edad:"))
    msg = getEdad(edad)
    print(msg)

def funcion7():
    cliente = input("Cliente:")
    producto = input("Producto:")
    precio = float(input("Precio:"))
    cantidad = int(input("Cantidad:"))
    subtotal =getSubtotal(precio,cantidad)
    iva = getIva(subtotal)
    des = getDescuento(subtotal)
    total = getTotal(subtotal,iva,des)
    res = "Subtotal:"+str(round(subtotal,2))+"\nIva:"+str(round(iva,2)) \
          + "\nDescuento:" + str(round(des, 2)) +"\nTotal a pagar:"+str(round(total,2))
    print(res)



def funcion8():
    c= 1
    s=0
    ac = 0
    while c< 10:
        if c%2!=0:
           print(c)
           s= s+1
           ac = ac + c
        c= c+1
    print("Total impares es "+str(s))
    print("Total acumulado es "+str(ac))

    c =0
    ac=0
    for i in range(1,11):
        if i % 2==0:
          ac = ac + i
          print(i)
          c= c+1
    print("Total de pares  es "+str(c))
    print("Total acumulado es "+str(ac))
def funcion9():
    datos =("MARIA",20,100, True,300)
    #print(datos[0])
    for i in range(len(datos)):
        print(datos[i])
    print("Tamaño de tupla",len(datos))
    datos =("MARIA",20)
    print(datos)

    lista = []
    lista.append("DIAZ")
    lista.append(300)
    lista.append(True)
    lista.append("POO")
    lista.append(54)
    print(len(lista))
    print(lista)
    lista[1]=500
    #lista.pop(1)
    del lista[2]
    print(lista)
    lista.clear()
    print(len(lista))

    dic ={
          "clave1" : 200,
           100 : "Python",
        (3,7,8,4): True,
        True : (1,2,3)
    }
    dic[False] =1000
    print(dic[False])
    dic[False]=5
    del dic[False]
    print(dic)

def funcion1():
    print("Linea 1")
    nombre = input("Nombre:")

def funcion10():
    lista = []
    i=0
    while i<5:
        valor = int(input("Valor "+str(i+1)+ ":"))
        res = getRepeat(lista,valor)
        if res == True:
            print("Valor repetido")
            i = i-1
        else:
            lista.append(valor)
        i = i +1

    for i in range(len(lista)):
        print(lista[i])

def funcion11():
    ing = Inputs()
    num = ing.inputInt("Ingrese su edad:")

funcion11()
"""
from impl.run import *
if __name__ == '__main__':
    obr = Run()
    obr.start()

