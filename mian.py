agenda = []
colores = set()

def agregar_color():
    nombre = input("Nombre: ")
    color = input("Color favorito: ")

    if color in colores:
        print(" Ese color ya está registrado")
    else:
        agenda.append({"nombre": nombre, "color": color})
        colores.add(color)
        print(" Color agregado correctamente")


def mostrar_colores():
    if len(agenda) == 0:
        print("No hay colores registrados")
    else:
        print("\n Lista de colores:")
        for c in agenda:
            print(c["nombre"], "->", c["color"])


def eliminar_color():
    nombre = input("Nombre a eliminar: ")

    for c in agenda:
        if c["nombre"] == nombre:
            colores.remove(c["color"])
            agenda.remove(c)
            print(" Color eliminado correctamente")
            return

    print("No se encontró el nombre")


while True:
    print("\n--- MENÚ COLORES ---")
    print("1. Agregar color")
    print("2. Mostrar colores")
    print("3. Eliminar color")
    print("4. Salir")

    op = input("Elige: ")

    if op == "1":
        agregar_color()
    elif op == "2":
        mostrar_colores()
    elif op == "3":
        eliminar_color()
    elif op == "4":
        print("Saliendo...")
        break
    else:
        print("Opción inválida")