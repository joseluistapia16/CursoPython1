from dominio.entidades import *
from entradas.entradas import *
from menu.menuC import *
from procesos.procesos import *
class Run:

    def __init__(self):
        self.menu = MenuC()
        self.lista = []
        self.ing = Inputs()
        self.proc = Procesos()

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
        pos = self.proc.getBankPosition(nombre,self.lista)
        if pos==-1:
            direccion = input("Direccion:")
            n_agencias = self.ing.inputInt("Numero de agencias:")
            obj = Banco(nombre,direccion,n_agencias)
            self.lista.append(obj)
            print("Datos guardados!")
        else:
            print("Banco ya existe!!")
        input("<Presione Enter> para continuar...")

    def consulta(self):
        print("\t\tConsulta de bancos")
        banco = input("Nombre del banco:")
        obj = self.proc.getBank(banco,self.lista)
        if obj!=None:
            print(obj.getFields())
        else:
            print("Banco no existe!")
        input("<Presione Enter> para continuar...")

    def actualizar(self):
        print("\t\tACTUALIZAR DATOS DEL BANCO")
        banco = input("Nombre del banco:")
        pos = self.proc.getBankPosition(banco,self.lista)
        if pos>-1:
            print(self.lista[pos].getFields())
            direccion = input("Direccion:")
            numero = self.ing.inputInt("Numero de agencia:")
            self.lista[pos].direccion = direccion
            self.lista[pos].setN_agencias(numero)
            print("Datos actualizados...")
        else:
            print("Banco no existe!!")
        input("<Presione Enter> para continuar...")

    def eliminar(self):
        print("\t\tEliminar datos del banco")
        banco = input("Nombre del banco:")
        pos = self.proc.getBankPosition(banco,self.lista)
        if pos>-1:
            print(self.lista[pos].getFields())
            input("Enter para continuar el borrado de datos!")
            self.lista.pop(pos)
            print("Los datos han sido borrados!")
        else:
            print("Banco no existe!!")
        input("<Presione Enter> para continuar...")


    def listar(self):
        print("\t\tListado de Bancos")
        for i in range(len(self.lista)):
            print(self.lista[i].getData())
        input("<Presione Enter> para continuar...")





