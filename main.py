'''
y = 90
t = 10
u = 100
x =(y+t)
#print(x)
y = "Maria"
t = "De los Angeles"
x = (y+" "+t+str(u))
print(x)

numero1 = int(input("Numero 1:"))
numero2 = int(input("Numero 2:"))
x = (numero1+numero2)
print("Total:"+str(x))



estudiante = input("Nombre de estudiante:")
materia = input("Materia:")
nota1 = float(input("Nota 1:"))
nota2 = float(input("Nota 2:"))
nota3 = float(input("Nota 3:"))
total = (nota1+nota2+nota3)
promedio = (total/3)
if promedio<0 or promedio>10:
    print("Valor invalido!")
else:
    print("Promedio:" + str(round(promedio, 2)))
    if promedio>=0 and promedio<7:
        print("REPROBADO")
    if promedio>=7 and promedio<=10:
        print("APROBADO")
rol = input("Rol:").upper()
if rol=="JEFE" or rol=="GERENTE" or rol =="EJECUTIVO":
    print("Administrativo")
else:
    if rol == "CONSERJE" or rol=="VENDEDOR" or rol=="MENSAJERO":
       print("Operativo")
    else:
        print("Externo")

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

datos =("MARIA",20,100, True,300)
#print(datos[0])
for i in range(len(datos)):
    print(datos[i])
print("Tamaño de tupla",len(datos))
datos =("MARIA",20)
print(datos)
'''
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
