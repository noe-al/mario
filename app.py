# Función para añadir un alumno a la lista
def añadir(alumnos):
    # Pedimos los datos al usuario
    nombre = input("Nombre: ")
    edad = input("Edad: ")
    
    
    # Mientras lo que escriba no sea un número, lo volvemos a pedir
    while not edad.isdigit():
        print("La edad tiene que ser un número.")
        edad = input("Edad: ")

    curso = input("Curso: ")

    # Creamos un diccionario con los datos del alumno
    alumno = {"nombre": nombre, "edad": edad, "curso": curso}

    # Añadimos el alumno a la lista
    alumnos.append(alumno)

    print("Alumno añadido.")


# Función para mostrar todos los alumnos
def mostrar(alumnos):
    # Si la lista está vacía, no hay alumnos
    if len(alumnos) == 0:
        print("No hay alumnos.")
    else:
        print("------Lista de alumnos:------")
        # Recorremos la lista y enseñamos cada alumno
        for a in alumnos:
            print("Nombre:", a["nombre"])
            print("Edad:", a["edad"])
            print("Curso:", a["curso"])
            print("--------")


# Función para buscar un alumno por nombre
def buscar(alumnos):
    nombre = input("Nombre a buscar: ")
    encontrado = False

    # Recorremos la lista buscando el nombre
    for a in alumnos:
        if a["nombre"] == nombre:
            print("------Alumno encontrado:------")
            print("Nombre:", a["nombre"])
            print("Edad:", a["edad"])
            print("Curso:", a["curso"])
            encontrado = True

    # Si no se encontró ningún alumno
    if not encontrado:
        print("No encontrado.")


# Función que muestra el menú y devuelve la opción
def menu():
    print("------MENÚ------")
    print("1. Añadir alumno")
    print("2. Mostrar alumnos")
    print("3. Buscar alumno")
    print("4. Salir")
    return input("Opción: ")


# Función principal del programa
def main():
    alumnos = []   # Lista donde se guardarán los alumnos
    salir = False  # Control para salir del programa

    # Bucle principal
    while not salir:
        opcion = menu()  # Mostramos el menú

        # Según la opción elegida, hacemos una cosa u otra
        if opcion == "1":
            añadir(alumnos)
        elif opcion == "2":
            mostrar(alumnos)
        elif opcion == "3":
            buscar(alumnos)
        elif opcion == "4":
            salir = True   # Cambiamos a True para terminar
        else:
            print("Opción incorrecta.")


# Llamamos a la función principal para empezar el programa
main()