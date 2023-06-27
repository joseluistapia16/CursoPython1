class Inputs:

    def inputInt(self,cadena):
        num = -1
        while num<0:
            try:
                num= int(input(cadena))
            except:
                num=-1
                print("Valor invalido!")
        return num

