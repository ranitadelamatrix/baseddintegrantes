import mysql.connector
import integrantes  #primero debemos importar la conxion de msql y tambien tener el pip instalado

class baseDeDatos(): # creamos una clase asi para hacer la conexion
     def __init__(self): #iniciamos la clase como constructor
          try:
            self.conexion = mysql.connector.connect(  #siempre self para indicar variable al constructor seguido d la variable
                host='localhost', # luego agregamos la conexino
                user='root',
                port= 3306,
                password='pancho1677',
                database='grupo_ispc'

                ) #creamos la variable self.conexion y le asiganamos el mysql.conect()
            
            if self.conexion.is_connected(): #si self.conexion se conecto imprimi conexion
                print("LA CONEXION FUE EXITOSA")
          except:
                 print("no se pudo conectar")

     def insertar_producto(self, alumno):
          
          if self.conexion.is_connected(): # si la conexion es conectado ejecutame esto try
               try:
                    cursor = self.conexion.cursor()
                    senteciaSql = "INSERT INTO integrantes values(%s,%s,%s,%s)"
                    data= (alumno.getiddni(),
                           alumno.getnombres(),
                           alumno.getapellido(),
                           alumno.getdireccion()
                           )
                    cursor.execute(senteciaSql, data)
                    self.conexion.commit()
                    self.conexion.close() #cerrame la conexion
                    print("se realizo")
               except mysql.connector.Error as descripcionDelError:
                         print("no se pudo", descripcionDelError)

     def borrar_integrantes(self, a):
          if self.conexion.is_connected():
               try:
                    cursor = self.conexion.cursor()
                    borrar = "DELETE FROM integrantes WHERE nombres = '%s'"%a
                    cursor.execute(borrar)
                    self.conexion.commit()
                    self.conexion.close()
                    print("se borro el integrante", a)
               except mysql.connector.Error as elerror:
                    print("el error es", elerror)




















"""def insertar(self, a, b ,c ,d): #creamos una funcin insertar
          self.a = a
          self.b = b
          self.c = c
          self.d = d
          try:
               sql = 'insert into integrantes(iddni, nombres, apellido, direccion)value'
               valor= (a,b , "ddd22dd", "ddddd222sss")
               total = sql, total
               self.cursor.execute(total)
               print("ingreso nombre correctamente")
               self.conexion.commit()
          except:
               print("no se cargar el dato")"""

"""def eliminar(self):
         borrar = 'delete from integrantes where nombres = "toga"'
         self.cursor.execute(borrar)
         self.conexion.commit()"""

"""def crearTabla(self, a):
         self.tabla = a
         sql = f"create table {self.tabla}(id int, nombres varchar(20), apellido varchar(20), direccion varchar(20))"
         self.cursor.execute(sql)
         self.conexion.commit()
         print(f"la tabla {self.tabla} se creo con exito")"""



#nuevaconexion = baseDeDatos() #llamamos a la clase
#nuevaconexion.insertar()
#nuevaconexion.crearTabla("chicos")
#nuevaconexion.borrarTabla("chicos")
#nuevaconexion.eliminar()