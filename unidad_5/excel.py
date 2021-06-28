import pandas as pd

def crear_archivo_ejemplo1(nombre_archivo = "C:/Users/jeiss/Documents/Material_Mintic/ciclo 1/Diagramas de Flujo/clases_python/unidad_5/prueba21.txt"):
    archivo = open(nombre_archivo, "w")

    # \n, \t, \b, \r, \\, \r\n
    archivo.write("Hola Mundo!")
    archivo.write("\n") # Cambio de linea
    archivo.write("Este es mi primer archivo\n")
    archivo.write("Esta linea es la ultima!\n")
    archivo.write("Otra prueba de escritura\n")
    archivo.write("La expresion es {}\n".format(1+5))
