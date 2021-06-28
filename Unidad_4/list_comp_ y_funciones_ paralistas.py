# Necesitamos crear una lista de enteros que contenga la longitud de cada 
# palabra en una frase, pero solo si la palabra no es "el".
# La frase es: "el rápido zorro marrón salta sobre el perro perezoso"

from typing import List


''' frase="el rápido zorro marrón salta sobre el perro perezoso"
lista_palabras=frase.split()
lista_palabras=[len(palabra) for palabra in lista_palabras if palabra !="el" ]
print(lista_palabras) '''


# Crea una nueva lista que a partir de otra lista de números que contenga 
# solo los números positivos de la lista, como enteros.
# La lista es:
''' numeros = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]

nueva_lista= [int(numero) for numero in numeros if numero>0]

print (nueva_lista)
 '''

# Extraiga en un conjunto los dígitos que existen en una frase.
#  La frase es "Hello 12345 World 5602"

''' frase= "Hello 12345 World 5602"
conjunto=  {digito for digito in frase if not digito.isalpha() and digito.isnumeric( )}
print(conjunto)
 '''

# ejercicio 4 
''' print([x**2 for x in range(10)])
print([2**i for i in range(13)]) '''


# ejercicio 5
# Cual sería la expresión List Comprehension 
# para generar la siguiente 
''' 
lista=[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]


decifrar= [x**3 for x in range(11)]
# decifrar=[int(numero/x) for numero in lista for x in range(1,10)if numero%x==0]
print (decifrar) '''


# funcion map 

''' fruta = ["Manzana", "Banano", "Pera", "Durazno", "Naranja"]

def cambiar_letra_a(cadena):
    return cadena[1]== "a"

lista= list(map(cambiar_letra_a,fruta))
print(lista) '''


#funcion map con lambda
''' fruta = ["Manzana", "Banano", "Pera", "Durazno", "Naranja"]

lista=list(map(lambda cadena: cadena[1]=="a",fruta))
print(lista) '''

''' # funcion map con varias listas 
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [1, 2, 3, 4, 5]
#recibe dos listas y opera con una funcion anonima, lo que hace es hacer una lista de tuplas
#de los listas dadas
resultado=list(map(lambda a,b:(a,b),my_strings,my_numbers))
print(resultado)
print(type(resultado))
print(type(resultado[0])) '''


# funcion filter

''' fruta = ["Manzana", "Banano", "Pera", "Durazno", "Naranja"]

def cambiar_letra_a(cadena):
    return cadena[1]== "a"

lista=list(filter(cambiar_letra_a,fruta))
print(lista)
print(type (lista))
print(type (lista[0])) '''

# funcion filter- ejercicio 2

''' dromes = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk")
palindromes = list(filter(lambda palabra: palabra==palabra[::-1],dromes ))
print(palindromes)

# ['madam', 'anutforajaroftuna'] '''


# funcion reduce

''' from functools import reduce

lista = [2, 4, 7, 3]
#valor = reduce(lambda x, y: x + y, lista)   
valor=reduce(lambda x,y: x+y, lista)
print(valor) '''

# funcion reduce con valor inicial 

''' from functools import reduce

lista = [2, 4, 7, 3]
valor=reduce(lambda x,y: x+y, lista,10) # aqui el 10 es el valor inicial  
print(valor) '''

''' numeros = [1, 2, 3]
espanol = ["Uno", "Dos", "Tres", "Cuatro"]
ingles = ["One", "Two"]
frances = ["Un", "Deux"]
print(list(zip(numeros, espanol, ingles, frances))) '''

""" # Función enumerate(iterables)
lenguajes = ["Java", "C", "C++", "Rust", "Elixir"]
lista=list(enumerate(lenguajes))
print(lista) """


#_____________Ejercicio de funciones _____________________________


# La empresa ABCD tiene hasta 100 empleados. La compañía decide crear un número 
# de identificación único UID para cada uno de sus empleados. La compañía le ha 
# asignado la tarea de validar los UIDs generados aleatoriamente. Un UID válido debe 
# cumplir con las siguientes reglas:
# • Debe contener por lo menos dos letras mayúsculas en el alfabeto inglés.
# • Debe tener por lo menos 3 dígitos.
# • Contener únicamente dígitos alfanuméricos.
# • No tener repeticiones.
# • Contener exactamente 10 caracteres.

uids = ["B1CD102354", "B1CDEF2354"]

for uid in uids:
    contenedor=[]
    contenedor.append(len(list(filter(lambda elemento: elemento.isupper(),list(uids))))>=2)
    contenedor.append(len(list(filter(lambda elemento: elemento.isdigit(),list(uids))))>=3)
    contenedor.append(len(list(filter(lambda elemento: not (elemento.isalnum()),list(uids))))==0)
    contenedor.append(len(uid)==len(set(uid)))
    contenedor.append(len(uid)==10)
    print("valido") if all (contenedor) else print ("invalido")
