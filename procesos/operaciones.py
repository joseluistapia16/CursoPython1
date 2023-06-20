def suma(v1,v2):
    res =(v1+v2)
    return res

def getSubtotal(pre,cant):
    return (pre*cant)

def getIva(subtotal):
    return (subtotal*0.12)

def getTotal(subtotal, iva, descuento):
    return (subtotal+iva)-descuento
def getDescuento(subtotal):
    des=0
    if subtotal>100:
        des = (subtotal*0.05)
        return des
    else:
        return des


def getEdad(edad):
    if edad < 0:
      return "Invalido!"
    if edad >= 0 and edad < 11:
      return "Infante!"
    if edad > 10 and edad < 18:
      return "Adolescente"
    if edad > 17 and edad < 26:
      return "Joven"
    if edad > 25 and edad < 65:
      return "Adulto"
    if edad > 64:
      return "Adulto mayor"
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

def getRepeat(lista,valor):
    res = False
    for i in range(len(lista)):
        if valor== lista[i]:
           res = True
           break
    return res