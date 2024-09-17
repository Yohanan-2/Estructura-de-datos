#Jesus yohanan Zempoaltecatl Lima 
#Materia Orgnizacion y estructurado de datos
pidio = float(input("Ingrese la cantidad del pidio: "))
pago = float(input("Ingresa la cantidad del pago mensual: "))
interes_fijo = float(input("¿Cuanto es la tasa de interes en %?: "))
numero_meses = float(input("¿A cuantos meses lo nuevo_pagoara?: "))
nuevo_pago = 0; aux=0
i = 1
print("MES \t | \t CAPITAL \t | \t INTERES \t | \t pago_mensual \t | \t NUEVOCAPITAL")
while i<=numero_meses:
    nuevo_pago = pidio*(interes_fijo / 100)
    aux = pidio
    pidio = pidio - (pago + nuevo_pago)
    if(i<10):
        print(" ",i," \t | \t ", round(aux,1), " \t | \t ", round(nuevo_pago,1)," \t | \t ", round(pago, 1)," \t | \t ", round(pidio,1))
    else:
        print("",i," \t | \t ", round(aux,1), " \t | \t ", round(nuevo_pago,1)," \t | \t", round(pago,1)," \t | \t ", round(pidio,1))
    i+=1