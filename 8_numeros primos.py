#Jesus yohanan Zempoaltecatl Lima 
#Materia Orgnizacion y estructurado de datos
numero = int(input("escribe un numeroero "))
iniciador = 1
divisible = 0
while iniciador <= numero:
    operador = numero % iniciador
    if operador == 0:
        divisible += 1
    iniciador += 1  
if divisible>2:
    print("No es primo")
else:
    print("Es primo")