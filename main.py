import conexion
from integrantes import Integrantes
from integrantes import Borrar

print("ingresar 1 para agregar alumnos")
print()
print("ingresa 2 para eliminar alumnos")

agregar = int(input())

if agregar == 1:
    conec = conexion.baseDeDatos()

    iddni= int(input("ingrese su dni ")) #aqui ingresamos las variables que creamos en la hoja integrantes
    nombres= input("ingrese su nombres ")
    apellido= input("ingrese su apellido ")
    direccion= input("ingrese su direccion ")

    alumno = Integrantes(iddni, nombres, apellido, direccion) # aqui creo variable alumno y le agrego el objeto integrantes de la hoja
    # con las variables de claradas
    conec.insertar_producto(alumno)
if agregar == 2:
    cone = conexion.baseDeDatos()
    borralo = input("ingresa el nombre que desea borrar ")
    cone.borrar_integrantes(borralo)
else:
    print("usted ingreso un numero invalido")
