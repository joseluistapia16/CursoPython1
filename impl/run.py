from dominio.entidades import *
from entradas.entradas import *
from menu.menuC import *
from procesos.procesos import *
from archivos.archivos import *
class Run:

    def __init__(self):
        self.menu = MenuC()
        self.ing = Inputs()
        self.proc = Procesos()
        self.ruta = "C:/Users/Usuario/PycharmProjects/CursoPython1/cursopython.csv"
        self.arch = Archivo()
        self.lista = self.arch.readBanks(self.ruta)

    def start(self):
        tupla = ("CREAR","CONSULTAR",
                 "ACTUALIZAR","ELIMINAR",
                 "LISTAR","SALIR")
        op=self.menu.getMenu(tupla)
        if op== 1:
            self.registro()
            self.start()
        if op==2:
            self.consulta()
            self.start()
        if op==3:
            self.actualizar()
            self.start()
        if op==4:
            self.eliminar()
            self.start()
        if op== 5:
            self.listar()
            self.start()

    def registro(self):
        print("\t\tRegistro de Bancos")
        nombre = input("Nombre de Banco:")
        self.lista= self.arch.readBanks(self.ruta)
        pos = self.proc.getBankPosition(nombre,self.lista)
        if pos==-1:
            direccion = input("Direccion:")
            n_agencias = self.ing.inputInt("Numero de agencias:")
            obj = Banco(nombre,direccion,n_agencias)
            datos = obj.nombre+";"+obj.direccion+";"+str(obj.getN_agencias())+";\n"
            self.arch.create(self.ruta,datos,"a")
            print("Datos guardados!")
        else:
            print("Banco ya existe!!")
        input("<Presione Enter> para continuar...")

    def consulta(self):
        print("\t\tConsulta de bancos")
        banco = input("Nombre del banco:")
        self.lista = self.arch.readBanks(self.ruta)
        obj = self.proc.getBank(banco,self.lista)
        if obj!=None:
            print(obj.getFields())
        else:
            print("Banco no existe!")
        input("<Presione Enter> para continuar...")

    def actualizar(self):
        print("\t\tACTUALIZAR DATOS DEL BANCO")
        banco = input("Nombre del banco:")
        self.lista = self.arch.readBanks(self.ruta)
        pos = self.proc.getBankPosition(banco,self.lista)
        if pos>-1:
            print(self.lista[pos].getFields())
            direccion = input("Direccion:")
            numero = self.ing.inputInt("Numero de agencia:")
            self.lista[pos].direccion = direccion
            self.lista[pos].setN_agencias(numero)
            msg = ""
            for i in range(len(self.lista)):
                msg = msg + self.lista[i].nombre+";"+self.lista[i].direccion+";"\
                      +str(self.lista[i].getN_agencias())+";\n"
            #print(msg)
            self.arch.create(self.ruta,msg,"w")
            print("Datos actualizados...")
        else:
            print("Banco no existe!!")
        input("<Presione Enter> para continuar...")

    def eliminar(self):
        print("\t\tEliminar datos del banco")
        banco = input("Nombre del banco:")
        self.lista= self.arch.readBanks(self.ruta)
        pos = self.proc.getBankPosition(banco,self.lista)
        if pos>-1:
            print(self.lista[pos].getFields())
            input("Enter para continuar el borrado de datos!")
            self.lista.pop(pos)
            msg = ""
            for i in range(len(self.lista)):
                msg = msg + self.lista[i].nombre+";"+self.lista[i].direccion+";"+\
                      str(self.lista[i].getN_agencias())+";\n"
            #print(msg)
            self.arch.create(self.ruta,msg,"w")
            print("Los datos han sido borrados!")
        else:
            print("Banco no existe!!")
        input("<Presione Enter> para continuar...")


    def listar(self):
        print("\t\tListado de Bancos")
        self.lista = self.arch.readBanks(self.ruta)
        for i in range(len(self.lista)):
            print(self.lista[i].getData())
        input("<Presione Enter> para continuar...")





