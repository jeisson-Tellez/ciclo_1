# elementos de entrada
# info_cliente={"nombre": "Cesar Diaz", "nacional":True, "agujas":20000000, "escolares": 30000000, "hogar":20000000}

def calculo_recargo (nombre, agujas, escolares, hogar,nacional=True,)->dict:
    info_cliente={"nombre": nombre, 
    "nacional":nacional, "agujas":agujas,
    "escolares": escolares, "hogar":hogar}

    if info_cliente["nacional"]==True:
        a=info_cliente["agujas"]>70000000
        b= info_cliente["escolares"]>30000000
        c= info_cliente["hogar"]>40000000

        compra_total=info_cliente["agujas"]+info_cliente["escolares"]+info_cliente["hogar"]

        if compra_total>=200000000:
            salida_1={"nombre":info_cliente["nombre"], "agujas": 10.0, "escolares":10.0, "hogar":10.0}
            return salida_1
        elif a==True and b==True and c ==True:
            salida_2={"nombre":info_cliente["nombre"], "agujas": 7.0, "escolares":7.0, "hogar":7.0}
            return salida_2
        elif (b ==False and c==False) or a==True:
            salida_2A={"nombre":info_cliente["nombre"], "agujas": 0.5, "escolares":0.0, "hogar":0.0}
            return salida_2A
        elif (a and c==False) or b==True:
            salida_2B={"nombre":info_cliente["nombre"], "agujas": 0.0, "escolares":5.0, "hogar":0.0}
            return salida_2B
        elif (a and b==False) or c==True:
            salida_2C={"nombre":info_cliente["nombre"], "agujas": 0.0, "escolares":0.0, "hogar":5.0}
            return salida_2C
        else:
            salida_3={"nombre":info_cliente["nombre"], "agujas": 0.0, "escolares":0.0, "hogar":0.0}
            return salida_3
    if info_cliente["nacional"]==False:

        a=info_cliente["agujas"]>25000
        b= info_cliente["escolares"]>10000
        c= info_cliente["hogar"]>15000

        compra_total=info_cliente["agujas"]+info_cliente["escolares"]+info_cliente["hogar"]
        if compra_total>=100000:
            salida_4={"nombre":info_cliente["nombre"], "agujas": 8.0, "escolares":8.0, "hogar":8.0}
            return salida_4
        elif a==True and b==True and c ==True:
            salida_5={"nombre":info_cliente["nombre"], "agujas": 5.0, "escolares":5.0, "hogar":5.0}
            return salida_5
        elif (b and c==False) or a==True:
            salida_5A={"nombre":info_cliente["nombre"], "agujas": 3.0, "escolares":0.0, "hogar":0.0}
            return salida_5A
        elif (a and c==False) or b==True:
            salida_5B={"nombre":info_cliente["nombre"], "agujas": 0.0, "escolares":3.0, "hogar":0.0}
            return salida_5B
        elif (a and b==False) or c==True:
            salida_5C={"nombre":info_cliente["nombre"], "agujas": 0.0, "escolares":0.0, "hogar":3.0}
            return salida_5C
        else:
            salida_6={"nombre":info_cliente["nombre"], "agujas": 0.0, "escolares":0.0, "hogar":0.0}
            return salida_6



# print(calculo_recargo("jeisson",70000010,100,100,True))
print(calculo_recargo("jeisson",0,0,0,True))
print(calculo_recargo("jeisson",150000000.0, 30000000.0,20000000.0,True))
print(calculo_recargo("jeisson",100000001.0,32000000.0,41325120.0,True))
print(calculo_recargo("jeisson",70000100.0,20000000.0, 40000001.0,True))
#print(calculo_recargo("jeisson",70000000.0, 30000000.0,40000000.0,True))