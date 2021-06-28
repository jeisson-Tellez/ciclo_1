#Cual sería la expresión List Comprehension para generar la siguiente 

""" lista=[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

salida=[x**3 for x in range(0,11)]
print()
print(salida)
print()
print(lista==salida) """

#_______________________Ejercicio 1 de mintic__________________________________________
# Utilizar la función incorporada map() para crear una función que retorne una lista con la 
# longitud de cada palabra (separadas por espacios) de una frase. La función recibe una cadena 
# de texto y retornará una lista.

# crear la funcion 
# recibo una cadena de caracteres
#separar cada palabra de la frase por espacio
# mido la longitud de cada palabra
# envuelvo el resultado en una lista

""" def longitud_palabra(frase)->list:
    separacion_palabras=list(map(len,frase.split()))
    # medicion=[len(palabra) for palabra in separacion_palabras]
    return separacion_palabras


Cadena_1="mi familia es muy bonita"
Cadena_2="Ejercicios para la solución de problemas "
Cadena_3="la nacion esta dirigido por el dolor de las elites"

print(longitud_palabra(Cadena_1))
print(longitud_palabra(Cadena_2))
print(longitud_palabra(Cadena_3)) """

#______________________ejercicio 1 profesor____________________________________

# Utilice map() para imprimir el cuadrado de cada número redondeado
# a tres lugares decimales
my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]

#identificar la operacion para elevar cada numero al cuadrado
#realizar una operacion con map que tenga como argumento  una funcion lambda que eleve al cuadrado
# cada numero y como objeto iterable  tenga el argumento de la funcion 
#redondear cada numero 

""" def cuadrado(lista=list)-> list:
    elevacion= list(map(lambda x: round(x**2,3),lista))
    return elevacion

print(cuadrado(my_floats)) """

#_______________________Ejercicio 2 de mintic__________________________________________
# Crear una función que tome una lista de dígitos y devuelva al número al que corresponden. 
# Por ejemplo [1,2,3] corresponde a el número ciento veintitrés (123). Utilizar la función 
# reduce

from functools import reduce

#  definir la funcion
# unir los numerosy entregar una valor unico 
""" 
def unir_digitos(lista=list):
    final=reduce(lambda a,b: str(a)+str(b), lista)
    return final


lista_1=[1,2,3]
lista_2=[1,2,3,7]
lista_3=[6,2,3,9]
lista_4=[1,9,3,9,6,25,42,68,8]
lista_5=[10,2,5,33]

print(unir_digitos(lista_1))
print(unir_digitos(lista_2))
print(unir_digitos(lista_3))
print(unir_digitos(lista_4))
print(unir_digitos(lista_5)) """

#solucion del mintic 
""" def digitos_a_numero(digitos):
    return reduce(lambda x,y:x*10 + y,digitos)

print(digitos_a_numero([4,3,9,2])) """

#______________________ejercicio 2 profesor____________________________________

# Utilice reduce() para imprimir el producto de estos números
""" my_numbers = [4, 6, 9, 23, 5]

def producto_lista(lista)->int:
    resultado=reduce(lambda x,y: x*y, lista)
    return resultado

print(producto_lista(my_numbers)) """

#_______________________Ejercicio 3 de mintic__________________________________________

# Crear una función que retorne las palabras de una lista de palabras que comience con una 
# letra en específico. Utilizar la función filter.

# defir la funcion
#filtrar las palabrar 


""" def filtro_lista(letra, cadena)->list:
    resultado=list(filter(lambda palabra: palabra[0]==letra,cadena))
    return resultado

def pasa_lista(frase=str)->list:
    resultado=list(frase.split())
    return resultado

Cadena_1="mi familia es muy bonita"
Cadena_2="Ejercicios para la solución de problemas "
Cadena_3="la nacion esta dirigido por el dolor de las elites"
list_1=['mi', 'familia', 'es', 'muy', 'bonita']

print(filtro_lista("f",list_1))
print(pasa_lista(Cadena_1)) """

#______________________ejercicio 3 profesor____________________________________
