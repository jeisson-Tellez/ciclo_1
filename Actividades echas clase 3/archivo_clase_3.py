#___________________CAPTURA DE DATOS________________________________________________


# # primera forma de captura de datos en python
# # se utilizas un print y luego el imput guardandolo en una variable
# #print("Escriba su nombre")
# #Nombre=input()
# #segunda forma, se guarda todo en una sola linea 
# #nombre=input("Escriba su nombre: ")

# # # Ejercicio 4 de la clase 2, modificado para la clase 3 con la funcion input
# # # primero debo identificar el problema, nunca comienzo a programar sin saber el problema
# # # problema: cuantas cajas de refresco van a sobrar si se comprar 9 cajas y cada caja trae 24 refredco
# # # y quiero que todos lo invitados tomer la misma cantidad de refresco
# # #defino el algoritmo o instruccion 
# # # 1. debo declarar las variables
# # Numero_Cajas_Refresco_adquiridas=9
# # Numero__refresco_por_Caja=24
# # Numero_Invitados=56
# # # 2. Realizo las ecuaciones pertinentes 
# # Total_resfresco_adquiridos=Numero_Cajas_Refresco_adquiridas*Numero__refresco_por_Caja
# # print(Total_resfresco_adquiridos/Numero_Invitados)
# # print(Total_resfresco_adquiridos//Numero_Invitados)
# # print(Total_resfresco_adquiridos%Numero_Invitados)
# # ejercicio con Input
# Numero_Cajas_Refresco_adquiridas= int( input("numero de cajas adquiridas: "))
# Numero__refresco_por_Caja= int( input("numero de refrescos por caja: "))
# Numero_Invitados= int( input("numero de invitados: "))
# # 2. Realizo las ecuaciones pertinentes 
# Total_resfresco_adquiridos=Numero_Cajas_Refresco_adquiridas*Numero__refresco_por_Caja
# print(Total_resfresco_adquiridos/Numero_Invitados)
# print(Total_resfresco_adquiridos//Numero_Invitados)
# print(Total_resfresco_adquiridos%Numero_Invitados)


#_____________________DEFINIR FUNCIONES_________________________________________
# #se utiliza para reutilizar un bloque de codigo, un script, formando una funcion, se usa "def"
# #lo que hace es ejecutar todas las tareas predefinidas en un codigo 
# def refrescos_sobrantes(): #se pone el nombre de la funcion, los argumentos todavia no se cuales son?
#     # es necesario que se marque una identacion, puesto que no ejecuta si no la tiene
#     Numero_Cajas_Refresco_adquiridas= int( input("numero de cajas adquiridas: "))
#     Numero__refresco_por_Caja= int( input("numero de refrescos por caja: "))
#     Numero_Invitados= int( input("numero de invitados: "))
#     # # 2. Realizo las ecuaciones pertinentes 
#     Total_resfresco_adquiridos=Numero_Cajas_Refresco_adquiridas*Numero__refresco_por_Caja
#     print(Total_resfresco_adquiridos/Numero_Invitados)
#     print(Total_resfresco_adquiridos//Numero_Invitados)
#     print(Total_resfresco_adquiridos%Numero_Invitados)

# # MUY IMPORTANTE!! la identacion ayuda a python a definir el bloque de codigo de la funcion
# # solo se ejecuta dentro del codigo lo que esta identado, en el caso anterior una vez
# # al llamar la funcion, esta se pone sin identar y ejecuta el codigo identado.
# refrescos_sobrantes()
# # esto ayuda a optimizar el codigo fuente

#___________________ARGUMENTOS DE UNA FUNCION__________________________________

# # Los argumentos son las entradas que estan predefinidas en una funcion
# #estas son necesarias para desarrollar las instrucciones o el bloque de codigo
# # por lo cual, al llamar la funcion esta pedira los datos de entrada
# def refrescos_sobrantes(Numero_Cajas_Refresco_adquiridas,Numero__refresco_por_Caja,Numero_Invitados ):
#     Total_resfresco_adquiridos=Numero_Cajas_Refresco_adquiridas*Numero__refresco_por_Caja
#     print(Total_resfresco_adquiridos/Numero_Invitados)
#     print(Total_resfresco_adquiridos//Numero_Invitados)
#     print(Total_resfresco_adquiridos%Numero_Invitados)
# #lo que vienen acontinuacion es un Ejemplo de la funcion con los argumentos definidos
# refrescos_sobrantes(9,12,25)


#_____________________________RETURN______________________________________________________
# seguimos con la funcion, en esta parte lo que hacemos es lo siguiente#
# la funcion print() nos ayuda imprimiendo en consola los elementos que yo quiera
#Sin embargo, es necesario sacarla de mi funcion, dado que limita a solo impriir en consla la funcion
# entonces, para sacar el  print() y obtener igualmente datos al correr el programa
# uso la palabra "Return", esta lo que hace es que al final de realizar todas las instrucciones 
#instrucciones obtenidas por la funcion que hicimos, me devuelva un valor que yo defino


def refrescos_sobrantes(Numero_Cajas_Refresco_adquiridas,Numero__refresco_por_Caja,Numero_Invitados ):
    """ Esta funcion me dice  cosas muy interesantes que despues escribo
    """
    Total_resfresco_adquiridos=Numero_Cajas_Refresco_adquiridas*Numero__refresco_por_Caja
    Total_resfresco_adquiridos/Numero_Invitados
    Total_resfresco_adquiridos//Numero_Invitados
    return Total_resfresco_adquiridos%Numero_Invitados

print(refrescos_sobrantes(4,6,2))


# Ahora bien, es para tener en cuenta lo siguiente:
# al ejecutar la funcion creada, no se imprime nada en consola, para verla, entonces, que hace return
# pues esa funcion le dice a la funcion que debe imprirse del codigo cuando se lo indiquen con un print
# por lo cual," print(refrescos_sobrantes(4,6,2)) " retorna lo que establece en el return
# imprime el primer return que de la linea de codigo de la funcion creada 

refrescos_sobrantes

