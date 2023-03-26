from Crud import *
from Funciones import *
while True:
    print("***Menu de opciones***")
    print("1.|-->Biblioteca<--|")
    print("2.|-->Agregar un libro<--|")
    print("3.|-->Actualizar libro<--|")
    print("4.|-->Eliminar un registro<--|")
    print("5.|-->Salir del sistema<--|")
    opcion = input("Ingrese un opcion: ")
    if opcion == "1":
        buscar_libros()
    elif opcion == "2":
        Libros = guardar_registro()
        registro(Libros)
    elif opcion == "3":
        id = int(input("Ingrese el ID del libro a modificar: "))
        Libros = actualizar_registro()
        modificar_registro(id,Libros)
    elif opcion == "4":
        id = int(input("Ingrese el ID a eliminar: "))
        eliminar= eliminar_libro(id)
