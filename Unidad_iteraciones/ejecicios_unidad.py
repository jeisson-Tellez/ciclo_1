#____________________________Ejercicio 1__________________________________________________
#Escribir un programa que solicite ingresar 10 notas de alumnos y nos informe cuántos 
#tienen notas mayores o iguales a 7 y cuántos menores

# print("escriba sus 10 nota por favor :")

# cantidad = 1
# contadorMayor = 0
# contadorMenor = 0

# while (cantidad < 11):
#     nota = int(input())
#     if (nota >= 0) and (nota < 11):
#         if nota >= 7:
#             contadorMayor =  contadorMayor + 1
#         else:
#             contadorMenor =  contadorMenor + 1
#     else:
#         print("no es una nota, por favor escriba una nota")
#     cantidad = cantidad + 1
    
# print("Cantidad de notas mayores e iguales a 7 " + str(contadorMayor))
# print("Cantidad de notas menores  a 7 " + str (contadorMenor))

#____ codigo propio
#Escribir un programa que solicite ingresar 10 notas de alumnos y nos informe cuántos 
#tienen notas mayores o iguales a 7 y cuántos menores

# inicializar - variables base

""" contador_mayores=0
contador_menores=0
contador_total=0
print("escriba sus 10 nota por favor :")
nota = int(input())
#validar 
while nota>=0 and nota <=10:
    nota = int(input())
    contador_total+=1
    if contador_total>10:
        break
    if nota >= 7 and nota<=10:
        contador_mayores+=1
    elif nota>=0 and nota<=7:
        contador_menores+=1
    if (contador_mayores+contador_menores)==10:
        print("la distribicion de notas es: " +"mayores a 7 = "+ str(contador_mayores)+" y menores a 7 = " + str(contador_menores))
else:
    print("valor fuera del rango")
 """

#________________________ejercicio 2___________________________________________
#Se ingresan un conjunto de n alturas de personas por teclado. Mostrar la altura promedio 
# de las personas.

# inicializar
""" contador=0
print("cantidad de datos a ingresar:")
numero_alturas =int(input())
print("digite la altura en metros")
#altura_cm =float(input())
altura_cm = 0
# condicion y cuerpo4
valor = 0
while altura_cm >= 0:
    altura_cm = float(input())
    contador += 1
    valor = valor + altura_cm
    if contador == numero_alturas:
        total = valor/numero_alturas
        print("la altura promedio es:  " + str(total) )
else:
    print("altura no valida") """

#_____________________Ejercicio 3___________________________________

# """ En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500, realizar 
# un programa que lea los sueldos que cobra cada empleado e informe cuántos empleados 
# cobran entre $100 y $300 y cuántos cobran más de $300. Además el programa deberá 
# informar el importe que gasta la empresa en sueldos al personal. """

#inicializar 

''' print("escriba el numero de empleados de la empresa")
numero_empleados=int(input())
salario_menor_300=0
salario_mayor_300=0
total1=0
total2=0
while numero_empleados >0:
    print("digite el valor del salario")
    salario_empleado=int(input())

    if salario_empleado>=100 and salario_empleado<=500:
        if salario_empleado>=100 and salario_empleado<=300:
            salario_menor_300+=1
            total1=total1 + salario_empleado
        if salario_empleado>300 and salario_empleado<=500:
            salario_mayor_300+=1
            total2=total2+salario_empleado
        if numero_empleados==1:
            print("los empleados que cobran entre $100 y $300 son:  "+ str(salario_menor_300))
            print("los empleados que cobran cobran más de $300 son:  "+ str(salario_mayor_300))
            total_final=total1+total2
            print("el importe que gasta la empresa en sueldos al personal es :  "+ str(total_final))
    else:
        print("valor fuera de rango ")
    numero_empleados-=1 '''


#_____________________Ejercicio 4___________________________________
# Realizar un programa que imprima 25 términos de la serie 11 - 22 - 33 - 44, etc. (No se 
# ingresan valores por teclado)

# inicializacion 
''' 
serie=11
contador=25
m=0
valor=0

while contador>0:
    contador-=1
    m+=1
    valor= serie*m
    print(m)
    print (valor) '''


#_____________________Ejercicio 5___________________________________

#  Realizar un programa que permita cargar dos listas de 15 valores cada una. Informar con 
# un mensaje cuál de las dos listas tiene un valor acumulado mayor (mensajes "Lista 1 
# mayor", "Lista 2 mayor", "Listas iguales"

''' indice=0
numero_elementos=15

def carga_lista(lista_1,lista_2):
    indice=int(0)
    numero_elementos=15
    while numero_elementos>0:
        
        
        numero_elementos=numero_elementos-1
    if acumulado_lista_1>acumulado_lista_2:
        return "lista 1 Mayor"
    elif acumulado_lista_1<acumulado_lista_2:
        return "lista 2 Mayor"
    else:
        return "Listas iguales"


lista_3=[1,5,6,4,8,98,52,45,65,48,8,5,69,2,4]
lista_4=[56,12,48,52,4,65,48,2,1,6,8,7,54,6,2]

print(sum(lista_4))
# print(carga_lista(lista_3,lista_4)) '''

d = {'a':10, 'b':1, 'c':22}
t = list(d.items())
print(t)