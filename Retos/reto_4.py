from numpy import split
import pandas as pd

def catalogacion_audiovisual(inventario: list) -> tuple:
    
    #1
    dvds=[x for x in inventario if x["tipo"]=="DVD"]
    dvds_eliminados=list(filter(lambda x: x["área"]== "Tecnología"and 2021 -x["año"] != 15,dvds)) 
    dvds_eliminados=list(map(lambda x: x["id"], dvds_eliminados))
    
    #2 
    cds=[x for x in inventario if x["tipo"]=="CD"]
    cds_eliminados=list(filter(lambda x: x["área"]== "Tecnología"and 2021 -x["año"] > 8,cds)) 
    cds_eliminados=list(filter(lambda x: x["área"]!= "Tecnología"and 2021 -x["año"] > 10,cds)) 
    cds_eliminados=list(map(lambda x: x["id"], cds_eliminados))
    

    #3
    
    permanecen=[x for x in dvds if x["área"]in ["Administración", "Física","Matemáticas"]]
    permanecen+=list(filter( lambda x:["área"]=="Tecnología"and 2021 -x["año"]<=15,dvds))
    permanecen+=list(filter( lambda x:["área"]=="Tecnología"and 2021 -x["año"]<=8, cds))
    permanecen+=list(filter( lambda x:["área"]!="Tecnología"and 2021 -x["año"]<=10, cds))
    permanecen.sort(key=lambda item: item["id"])

    #4
    def ajustar_nombres(item:dict)->dict:
        from functools import reduce
        autores=item["autor"].split(",")
        nombres=[x.split()[1]+ "," + x.split()[0] for x in autores]
        item["autor"]= reduce (lambda x,y: x + ";"+ y, nombres)
        return item
    
    permanecen=list(map(ajustar_nombres,permanecen))
    #5 
    return permanecen, dvds_eliminados,cds_eliminados





inventario = [{"id": "10", "titulo":
"Administración de compras", "tipo":
"DVD", "área": "Administración",
"autor": "César Díaz,Andrés García",
"año": 2005}, {"id": "20", "titulo":
"Fundamentos de programación", "tipo":
"DVD", "área": "Tecnología", "autor":
"César Díaz", "año": 2003}, {"id": "30",
"titulo": "Actualidad matemática",
"tipo": "CD", "área": "Matemáticas",
"autor": "Pedro Navaja", "año": 1987},
{"id": "40", "titulo": "Actualidad informática",
 "tipo": "CD", "área":
"Tecnología", "autor": "Bill Gates",
"año": 2019}, {"id": "50", "titulo":
"Atomic Physics for Dummies", "tipo":
"DVD", "área": "Física", "autor":
"Albert Einstein", "año": 1955}]

print(catalogacion_audiovisual(inventario))

salida=([{"id": "10", "titulo": "Administración de compras",
"tipo": "DVD", "área":
"Administración", "autor":
"Díaz,César;García,Andrés", "año":
2005}, {"id": "40", "titulo":
"Actualidad informática", "tipo": "CD",
"área": "Tecnología", "autor":
"Gates,Bill", "año": 2019}, {"id": "50",
"titulo": "Atomic Physics for Dummies",
"tipo": "DVD", "área": "Física",
"autor": "Einstein,Albert", "año":
1955}], ["20"], ["30"] )
