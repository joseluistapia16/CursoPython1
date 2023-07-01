from dominio.entidades import *

class Archivo:

    def create(self,ruta,datos,modo):
        arch = open(ruta,modo)
        arch.write(datos)
        arch.close()

    def readBanks(self,ruta):
        lista = []
        arch = open(ruta,"r")
        for linea  in arch.readlines():
            tupla = linea.split(";")
            obj = Banco(tupla[0],tupla[1],int(tupla[2]))
            lista.append(obj)
        arch.close()
        return lista
