from entradas.entradas import *

class MenuC:

    def __init__(self):
        self.ing = Inputs()

    def getMenu(self,tupla):
        for i in range(len(tupla)):
            print(str(i+1)+".- "+tupla[i]+".")
        op=-1
        while op<1 or op>len(tupla):
            op = self.ing.inputInt("Ingrese una opcion[1.."+str(len(tupla))+"]:")
        return op