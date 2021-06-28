
def simulador_prestamo_baniscutp(datos_prestamo: dict) -> dict:
    
    Tasa_mensual=float(((1+(datos_prestamo["interes anual"]/100))**(1/12))-1)
    saldo_a_finaciar=float(round(datos_prestamo["prestamo"]+datos_prestamo["gastos documentacion"]))
    meses=int(datos_prestamo["cuotas"])

    """ desglose de pasos para calcular cuota"""
    cuota_p1=1+Tasa_mensual
    cuota_p2=(cuota_p1)**(meses*(-1))
    cuota_p3=1-cuota_p2
    cuota_p4=cuota_p3/Tasa_mensual
    cuota_p5=saldo_a_finaciar/cuota_p4

    """ resultado cuota"""
    cuota=float(round(cuota_p5))

    """variables de inicializacion del while"""
    numero_cuota=0
    contenedor_general=[]
    nuevo_saldo=saldo_a_finaciar
    
    while meses>1:
        meses-=1
        numero_cuota+=1
        valor_interes=round((nuevo_saldo*Tasa_mensual),2)
        capital_abonado=round((cuota-valor_interes),2)
        nuevo_saldo=round((nuevo_saldo-capital_abonado),2)
        contenedor_lista= (numero_cuota,capital_abonado,valor_interes,cuota,nuevo_saldo)
        contenedor_general.append(contenedor_lista)
    else:
        meses-=1
        numero_cuota+=1
        capital_abonado=nuevo_saldo
        valor_interes=round((nuevo_saldo*Tasa_mensual),2)
        cuota=round(capital_abonado+valor_interes,2)
        nuevo_saldo=round((nuevo_saldo-capital_abonado),2)

        contenedor_lista= (numero_cuota,capital_abonado,valor_interes,cuota,nuevo_saldo)
        contenedor_general.append(contenedor_lista)

    return {"saldo financiar":saldo_a_finaciar,"cuota":cuota,"amortizacion":contenedor_general}


entrada_1= {
"prestamo": 2000000.0,
"gastos documentacion": 0.0,
"cuotas": 6,
"interes anual": 28.99
}

print(simulador_prestamo_baniscutp(entrada_1))

""" entrada_2 = { "prestamo": 1200000.0, "gastos documentacion": 100000.0, "cuotas": 12, "interes anual": 25.13 }


print(simulador_prestamo_baniscutp(entrada_2)) """


