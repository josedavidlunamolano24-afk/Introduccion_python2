# Aplicación de Gestión de Colores

# Descripción

la aplicación permite guardar nombres de personas junto con su color
favorito. Se pueden agregar, mostrar y eliminar registros. Además, evita
que se repitan colores usando un set.

------------------------------------------------------------------------

# Instrucciones de ejecución

1.  Ejecutar el archivo en Python.
2.  Aparecerá un menú con opciones.
3.  Elegir una opción escribiendo un número:
    -   1: Agregar color
    -   2: Mostrar colores
    -   3: Eliminar color
    -   4: Salir
4.  Seguir las instrucciones en pantalla.

------------------------------------------------------------------------

# Explicación de estructuras usadas

# Lista (agenda)

Se usa para almacenar todos los registros:

  agenda = []

Cada elemento es un diccionario con nombre y color.

------------------------------------------------------------------------

# Diccionario

Se usa para guardar los datos de cada persona:

{"nombre": nombre, "color": color}

------------------------------------------------------------------------

# Set (colores)

Se usa para evitar colores repetidos:

colores = set()

------------------------------------------------------------------------

# Tuplas

en el codigo no use las tuplas directamente, pero las podria usar para guardar datos fijos

------------------------------------------------------------------------

# Ciclo for

Se usa para recorrer la lista:

for c in agenda:

------------------------------------------------------------------------

# Ciclo while

Se usa para mantener el menú en ejecución:

while True:

------------------------------------------------------------------------

# Funciones del programa

# agregar_color()

-   Pide nombre y color
-   Verifica si el color ya existe
-   Si no existe, lo guarda

------------------------------------------------------------------------

# mostrar_colores()

-   Muestra todos los registros guardados

------------------------------------------------------------------------

# eliminar_color()

-   Busca un nombre
-   Si lo encuentra, lo elimina

------------------------------------------------------------------------