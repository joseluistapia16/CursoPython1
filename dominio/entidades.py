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


class Vehiculo:

    def __init__(self,marca,modelo,n_velocidad):
        self.__marca = marca
        self.modelo = modelo
        self._n_velocidades = n_velocidad

    def setMarca(self,marca):
        self.__marca = marca

    def getMarca(self):
        return self.__marca

    def getData(self):
        return self.__marca+" "+self.modelo+" "+self._n_velocidades

class Auto(Vehiculo):

    def __init__(self,marca,modelo,n_velocidad,chasis):
        Vehiculo.__init__(self,marca,modelo,n_velocidad)
        self.chasis = chasis
        print(self.__descripcion())

    def __descripcion(self):
        return "Esto es un auto...."

    def getData(self):
        return self.getMarca()+" "+self.modelo+" "+str(self._n_velocidades)+" "+self.chasis


class Moto(Vehiculo):

    def _init_(self, marca, modelo, n_velocidad):
        Vehiculo.__init__(self, marca, modelo, n_velocidad)

    def getData(self):
        return self.getMarca()+ " " + self.modelo + " " + str(self._n_velocidades)


class Buque(Vehiculo):
    def __init__(self, marca, modelo, n_velocidad, eslora_dimension):
        Vehiculo.__init__(self, marca, modelo, n_velocidad)
        self.eslora_dimension = eslora_dimension

    def getData(self):
        return self.getMarca()+ " " + self.modelo + " " + str(self._n_velocidades)+ " " +str( self.eslora_dimension)



# codigo de prueba


"""
objB = Banco("PICHINCHA","QUITO",30)
print(objB.getData())
objB.nombre="GUAYAQUIL"
objB.direccion="URDESA"
objB.setN_agencias(50)
print(objB.getN_agencias())
print(objB.getData())


obA = Auto("MAZDA","2000",6,"XLO989898")
print(obA.getData())
obA.setMarca("TOYOTA")
obA.modelo="2020"
obA._n_velocidades=8
print(obA.getMarca())
print(obA.getData())

obM = Moto("SUZUKI","2000",5)
print(obM.getData())
obM.setMarca("HONDA")
obM.modelo="2045"
obM._n_velocidades =7
print(obM.getData())
"""
obB = Buque("KIA","2022",9,40.90)

print(obB.getData())
obB.setMarca("ECUADOR")
obB.modelo="1908"
obB.eslora_dimension=100
print(obB.getData())