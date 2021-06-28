# elementos de entrada
# info_cliente={"nombre": "Cesar Diaz", "nacional":True, "agujas":20000000, "escolares": 30000000, "hogar":20000000}

def calculo_recargos (directorio)->dict:
    info_cliente=directorio

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
        elif a or b or c==True:
            if a==True:
                info_cliente["agujas"]=5.0
            else:
                info_cliente["agujas"]=0.0  
            if b==True:
                info_cliente["escolares"]=5.0
            else:
                info_cliente["escolares"]=0.0
            if c==True:
                info_cliente["hogar"]=5.0
            else:
                info_cliente["hogar"]=0.0
            del info_cliente["nacional"]
            return info_cliente
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
        elif a or b or c==True:
            if a==True:
                info_cliente["agujas"]=3.0
            else:
                info_cliente["agujas"]=0.0  
            if b==True:
                info_cliente["escolares"]=3.0
            else:
                info_cliente["escolares"]=0.0
            if c==True:
                info_cliente["hogar"]=3.0
            else:
                info_cliente["hogar"]=0.0
            del info_cliente["nacional"]
            return info_cliente
        else:
            salida_6={"nombre":info_cliente["nombre"], "agujas": 0.0, "escolares":0.0, "hogar":0.0}
            return salida_6



''' print("nacionales")
print(calculo_recargo("jeisson",0,0,0,True))
print(calculo_recargo("jeisson",150000000.0, 30000000.0,20000000.0,True))
print(calculo_recargo("jeisson",100000001.0,32000000.0,41325120.0,True))
print(calculo_recargo("jeisson",70000100.0,20000000.0, 40000001.0,True))
print(calculo_recargo("jeisson",70000000.0, 30000000.0,40000000.0,True))
print(calculo_recargo("jeisson",70000100.0,20000000.0, 40000001.0,True))
print(calculo_recargo("jeisson",20000000.0,10000000.0, 90000001.0,True))

print("internacionales")
print(calculo_recargo("jeisson",0,0,0,False))# 0,0,0 
print(calculo_recargo("jeisson",50000, 50000,50000, False))# 8,8,8
print(calculo_recargo("jeisson",100000, 5000,50000, False))#8,8,8
print(calculo_recargo("jeisson",26000, 15000,26000, False))#  5,5,5
print(calculo_recargo("jeisson",1000, 50000,1000, False)) # 0,3,0
print(calculo_recargo("jeisson",30000, 1000,30000, False)) # 3,0,3
print(calculo_recargo("jeisson",1000, 30000,30000, False)) # 0,3,3
print(calculo_recargo("jeisson",30000, 30000,1000, False))# 3,3,0 '''