#Escribir un programa que pida al usuario un número entero positivo
# y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

''' print("ingrese un numero entrero postivo")
contador=int(input())
regresion=contador
print(regresion,sep=",",end=" ")


while contador>0:
    contador-=1
    regresion-=1
    print(regresion,sep=",", end=" ") '''


#________________________________Ejercicio 2_______________________________________________
# Escribir un programa que pida al usuario un número entero y
#  muestre por pantalla un triángulo rectángulo como el de más abajo, 
# de altura el número introducido.

''' print("ingrese un numero entrero postivo")
contador=int(input())
valor=contador 
punto_1=str()

for i in range( 0,valor):
    puntos="*"
    punto_1+=puntos
    print (punto_1) '''


#________________________________Ejercicio 3 _______________________________________________
# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo 
# como el de más abajo, de altura el número introducido.
print("ingrese un numero entero postivo")
contador=int(input())
valor=contador 


for i in range(1,valor,2):
    acumulador=str(i)
    avance=acumulador+str(i)
    print(avance)