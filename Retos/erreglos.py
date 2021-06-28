

from numpy.lib.shape_base import split


def catalogacion_audiovisual(inventario: list) -> tuple:
    from numpy.lib.shape_base import split
    import pandas as pd
    
    eliminar_dvds= lambda item: item["tipo"]=="DVD" and item["área"]=="Tecnología" and 2021 - item ["año"] > 15
    dvds_eliminados=[x["id"] for x in  list(filter(eliminar_dvds,inventario) )]
    
    #2 
    def eliminar_cds(item):
        if item["tipo"]=="CD":
            if item["área"]=="Tecnología" and 2021 - item ["año"] > 8:
                return True
            elif 2021 - item ["año"] > 10:
                return True
        else:
            return False
    cds_eliminados=[x["id"] for x in  list(filter(eliminar_cds,inventario))]
    permanecen=[x for x in inventario if x["id"] not in dvds_eliminados and x["id"] not in cds_eliminados]
    
    # permanecen= [x for x in inventario if x["id"] not in dvds_eliminados and x["id"] not in cds_eliminados]
    #4
    def ajustar_nombres (item:dict)->dict:
        from functools import reduce
        autores=item["autor"].split(",")
        nombres=[x.split()[1]+ "," + x.split()[0] for x in autores]
        item["autor"]= reduce (lambda x,y: x + ";"+ y, nombres)
        return item 
    
    permanecen=list(map(ajustar_nombres,permanecen))
    #5 
    return permanecen, dvds_eliminados, cds_eliminados 
