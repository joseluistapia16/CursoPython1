def suma(v1,v2):
    res =(v1+v2)
    return res

def promedio(n1,n2,n3):
    return (n1+n2+n3)/3
def getRol(rol):
    if rol=="JEFE" or rol=="GERENTE" or rol =="EJECUTIVO":
        return "Administrativo"
    else:
        if rol == "CONSERJE" or rol=="VENDEDOR" or rol=="MENSAJERO":
           return "Operativo"
        else:
            return "Externo"
def mensaje(res):
    if res<0 or res>10:
        return "Valor invalido!"
    else:
        if res>=0 and res<7:
            return "REPROBADO"
        if res>=7 and res<=10:
            return "APROBADO"
def funcion2():
    y = 90
    t = 10
    u = 100
    x =(y+t)
    #print(x)
    y = "Maria"
    t = "De los Angeles"
    x = (y+" "+t+str(u))
    print(x)

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
    if edad<0:
        print("Invalido!")
    if edad>=0 and edad<11:
        print("Infante!")
    if edad>10 and edad<18:
        print("Adolescente")
    if edad>17 and edad<26:
        print("Joven")
    if edad>25 and edad < 65:
        print("Adulto")
    if edad>64:
        print("Adulto mayor")

def funcion7():
    cliente = input("Cliente:")
    producto = input("Producto:")
    precio = float(input("Precio:"))
    cantidad = int(input("Cantidad:"))
    subtotal =(precio * cantidad)
    iva = (subtotal*0.12)
    total = (subtotal+iva)
    descuento5=(total*0.05)
    descuento= (subtotal-descuento5)
    ivad= (descuento*0.12)
    res = "Subtotal:"+str(round(subtotal,2))+"\nIva:"+str(round(iva,2))\
    +"\nTotal a pagar:"+str(round(total,2))
    #print(res)
    if subtotal>=100:
        descuento5 = (subtotal * 0.05)
        descuento = (subtotal - descuento5)
        ivad = (descuento * 0.12)
        totalpago = (descuento + ivad)
        print("EL Decuento es:"+str(round(descuento,2)))
        print("Iva:" +str(ivad))
        print("Total a pagar:"+str(round(totalpago,2)))

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


funcion5()

