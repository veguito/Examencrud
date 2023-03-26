
def guardar_registro():
    nombre = input("Titulo del libro: ")
    autor = input("Nombre del autor: ")
    editorial = input("Editorial: ")
    edicion = input("edicion: ")


    Libros = {
        "nombre": nombre,
        "autor": autor,
        "editorial": editorial,
        "edicion": edicion,

    }
    return Libros

def actualizar_registro():
    print("***Que desea modificar")
    print("1. Modificar todos los datos del libro")
    print("2. Modificar un elemento del libro")
    opcion = input("Ingrese una opcion: ")
    if opcion == "1":
        nombre = input("Titulo del libro: ")
        autor = input("Nombre del autor: ")
        editorial = input("Editorial: ")
        edicion = input("edicion: ")


        Libros = {
            "nombre": nombre,
            "autor": autor,
            "editorial": editorial,
            "edicion": edicion,

        }
        return Libros
    elif opcion == "2":
        indice = input("Ingrese el indice: ")
        valor = input("Ingrese el valor a modificar: ")
        Libros = {indice: valor}
        return Libros