from dominio.entidades import *

class Procesos:

    def getBank(self,name,lista):
        obj= None
        for i in range(len(lista)):
            if name== lista[i].nombre:
                obj= lista[i]
                break
        return obj

    def getBankPosition(self,name, lista):
        pos = -1
        for i in range(len(lista)):
            if name== lista[i].nombre:
                pos = i
                break
        return pos