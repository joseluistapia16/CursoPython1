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

'''
cliente = input("Cliente:")
producto = input("Producto:")
precio = float(input("Precio:"))
cantidad = int(input("Cantidad:"))
subtotal =(precio * cantidad)
iva = (subtotal*0.12)
total = (subtotal+iva)
res = "Subtotal:"+str(round(subtotal,2))+"\nIva:"+str(round(iva,2))\
      +"\nTotal a pagar:"+str(round(total))
print(res)