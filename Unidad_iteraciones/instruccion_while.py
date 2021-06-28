# instreccion while
cocodrilo=65

# def cocodile(numero): 
#     while numero > 1:
#         postivo = numero - 2
#         return postivo

# n = 5
# while n > 0:
#     print(n)
#     n = n - 1
# print('Despegue!')

# numero= 212
# while numero > 0:
#     print (numero)
#     numero = numero - 1

# print('Despegue!')

# los signos -> significan anotacion de retorno
# para el caso de la funcion significa  indica que devuelve un entero 

def factorial(n:int)->int:
    """ importante: estas son las variables de inicializacion de la iteracion"""
    """ es el escenario base, resultado es la variable que se transforma y numero_actual es el contador"""
    resultado = 1
    numero_actual= 2 
    while numero_actual <= n: 
        """ cuando inciamos la condiciones hablamos de while, se aplica lo de las proposiciones"""
        resultado= resultado * numero_actual
        numero_actual += 1
        """ahora bien,  lo anterior es el cuerpo del ciclo-se ejecuta varias veces- las instrucciones"""
    return resultado


def fibonnacci(n):
    """acontinuacion se realizara la inicializacion de la iteracion"""
    
    pass


# promedio, total, contar = 0.0, 0, 0

# print("Introduzca la nota de un estudiante (-1 para salir): ")
# grado = int(input())
# while grado != -1:
#     total = total + grado
#     contar = contar + 1
#     print("Introduzca la nota de un estudiante (-1 para salir): ")
#     grado = int(input())
# promedio = total / contar
# print("Promedio de notas del grado escolar es: " + str(promedio))

# def cuenta_regresiva(n):
#     primer= 0
#     if n > primer:
#         print(n)
#         cuenta_regresiva(n-1)


# def banco_cuenta(consignacion):
#     if consignacion > 0:
#         print (consignacion)
#         banco_cuenta(consignacion-300)
#     else:
#         print ("sin saldo disponilbe")


# def factorial1(n):
#     # primero debo hacer la validacon de la expresion
#     if n < 0:
#         return "este es un valor erroneo"
#     # esto es  el cuerpo despues de la validacion 
#     elif n == 0:
#         return 1
#     else:
#         return 


# esta funcion no me correo por alguna razon 

# def factorial(n):
#     # Validar
#     if n < 0:
#         return "Número erróneo"
#     # Algoritmo
#     if n == 0:
#         return 1
#     else:
#         print ("hola")

variable = 10

# while variable > 0:
#     print('Actual valor de variable:', variable)
#     variable = variable -1
#     if variable == 5:
#         break

coco_loco= 1
while coco_loco>5:
    print ("esta casi listo" + str(coco_loco))
    coco_loco=coco_loco+1
    if coco_loco==12:
        break