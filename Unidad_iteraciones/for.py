""" #contar una serie de datos
contador=0 # se ajuste esta a cero  ntes del ciclo
# contar elementos de una lsita 
for valor in [3, 41, 12, 9, 74, 15]: # este bucle pasa a traves del rango
    # valor es la variable de iteracion: aqui para el objetivo del programa no se usa
    contador+=1 #cuenta el avance 
print("el numero de elementos de la lista es: ", contador) """



""" #calcula el total de un conjunto de números, se muestra a
#variable de inicializacion 
total=0 # funciona como un contenedor 
for valor in [3, 41, 12, 9, 74, 15]:
    total+=valor # variable de iteracion usada 
print("el totales: ", total) """


# bucles de maximos y minimos 

""" mayor=None # None le dice a python que la variable esta vacia
print("antes:  ", mayor)
for valor in [3, 41, 12, 9, 74, 15]:
    if mayor is None or valor > mayor:
        mayor=valor
    print("bucle: ", valor, mayor)
print("Mayor es: " + str(mayor)) """


#________________________________Taller for________________________________________________
# Confeccionar un programa que lea n pares de datos, cada par de datos corresponde a la 
# medida de la base y la altura de un triángulo. El programa deberá informar:
# a) De cada triángulo la medida de su base, su altura y su superficie.
# b) La cantidad de triángulos cuya superficie es mayor a 12.

''' 
Triangulor={
    "base":[4, 15, 46, 89, 4, 15, 23],
    "altura":[6,12,46,48,73,46,19]
    }


for bases,alturas in zip(Triangulor["base"],Triangulor["altura"]):
    superficie= bases*alturas
    print("el triangulo tiene de base" , bases, "de altura", alturas, " de superficie", superficie )

print(type(superficie)) '''


#________________________________Ejercicio 2________________________________________________

# 9. Desarrollar un programa que solicite la carga de 10 números e imprima la suma de los 
# últimos 5 valores ingresados.
''' 
numeros=[]
contador=0
while contador!=10 or contador<10:
    print("digite un numero")
    adicion=input()
    contador+=1
    numeros.extend(adicion)
print(" la lista de numeros es:", numeros)
total=0
for numero in numeros[5:10]:
    sumatoria=int(numero)
    total+=sumatoria

print("el valor de la suma de los ultimos 5 digitos es: ",total) '''

#________________________________Ejercicio 3 ________________________________________________




