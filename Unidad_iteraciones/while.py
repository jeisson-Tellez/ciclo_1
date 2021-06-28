# n=5 # inicializacion- declaro variable (s) base
# # valido la condicion inicial- debe obtener un valor booleano 
# while n>0:
#     # aqui se evalua otransforma la variable, este es el cuerpo
#     n += -1 #este es el contador del ciclo y acerca la condicion a su negacion 
#     print (n)

# factorial con while
""" def facto1(n:int):
    # inicializar secuencia
    resultado=1
    contador=1
    #validar 
    while contador<=n:
        resultado*=contador
        contador+=1
    return resultado

print (facto1(5)) """

#__________________ejercicio minimo comun multiplo________________________________

#algoritmo resursivo


""" def mcd(x, y):
    # Validar
    if y < 0:
        return "No puede buscar divisores si hay números negativos"

    # Algoritmo
    if y == 0:
        return x
    if x >= y:
        return mcd(y, x % y) 
    else:
        return mcd(y, x) """

#__algoritmo iterativo   

#iniacializar 

def mcd(x,y):
    if y<0:
        return " dato errado"
    if y>x:
        casi=x
        x=y
        Y=casi
    while x>=y:
        if y==0:
            break
        casi=x%y
        x=y
        y=casi
    return x


print(mcd(20,15))
print("hola")