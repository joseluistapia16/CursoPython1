class Banco:

    def __init__(self,nombre,direccion,n_agencias):
        self.nombre = nombre
        self.direccion = direccion
        self.__n_agencias = n_agencias

    def setN_agencias(self,n_agencias):
        self.__n_agencias = n_agencias

    def getN_agencias(self):
        return self.__n_agencias

    def getData(self):
        return self.nombre+" "+self.direccion+" "+str(self.__n_agencias)

    def __prueba(self,nombre):
        return "Hola "+nombre

class Auto:

    def __init__(self,placa, marca, n_velocidades):
        self.__placa = placa
        self.marca = marca
        self.n_velocidades = n_velocidades

    def setPlaca(self,placa):
        self.__placa= placa

    def getPlaca(self):
        return self.__placa

    def getData(self):
        return self.__placa+" "+self.marca+" "+str(self.n_velocidades)

class Estudiante:


    def __init__(self,cedula, nombre, n_materias):
        self.__cedula = cedula
        self.nombre = nombre
        self.n_materias = n_materias


    def setCedula(self,cedula):
        self.__cedula= cedula


    def getCedula(self):
        return self.__cedula


    def getData(self):
        return self.__cedula+" "+self.nombre+" "+str(self.n_materias)


    def __prueba(self, nombre):
        return "Hola " + nombre

class Escuela:


    def __init__(self,tipo, nombre, direccion):
        self.__tipo = tipo
        self.nombre = nombre
        self.direccion = direccion


    def setTipo(self, tipo):
        self.__tipo = tipo


    def getTipo(self):
        return self.__tipo


    def getData(self):
        return self.__tipo + " " + self.nombre + " " + self.direccion


    def __prueba(self, nombre):
        return "Hola " + nombre

class Telefono:
    def __init__(self, tipo, marca, precio):
        self.__tipo = tipo
        self.marca =marca
        self.precio = precio

    def setTipo(self, tipo):
        self.__tipo = tipo
    def getTipo(self):
        return self.__tipo
    def getData(self):
        return self.__tipo + " " + self.marca + " " + str(self.precio)
    def __prueba(self, nombre):
        return "Hola " + nombre

# codigo de prueba
objB = Banco("PICHINCHA","QUITO",30)
print(objB.getData())
objB.nombre="GUAYAQUIL"
objB.direccion="URDESA"
objB.setN_agencias(50)
print(objB.getN_agencias())
print(objB.getData())