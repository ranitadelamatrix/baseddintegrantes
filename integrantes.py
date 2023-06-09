class Integrantes():
    iddni= 0,
    nombres= "",
    apellido= "",
    direccion= "",

    def __init__(self, iddni, nombres, apellido, direccion) -> None:
        self.iddni = iddni
        self.nombres = nombres
        self.apellido = apellido
        self.direccion  = direccion

    def getiddni(self): #con el get llamamos a la variable para poder usarla
        return self.iddni
    def getnombres(self):
        return self.nombres
    def getapellido(self):
        return self.apellido
    def getdireccion(self):
        return self.direccion
    
    def setiddni(self, iddni):
        self.iddni = iddni
    def setnombres(self,nombres): #utilizamos los set para poder manipular las variables
        self.nombres = nombres
    def setapellido(self, apellido):
        self.apellido = apellido
    def setdireccion(self, apellido):
        self.apellido = apellido
    
class Borrar():
    nombres = ""
    def __init__(self, nombres) -> None:
        self.nombres = nombres
    def getnombres(self):
        return self.nombres
    def setnombres(self, nombres):
        self.nombres = nombres
    

