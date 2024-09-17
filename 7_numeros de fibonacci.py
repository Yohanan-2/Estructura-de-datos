#Jesus yohanan Zempoaltecatl Lima 
#Materia Orgnizacion y estructurado de datos
numero = int(input("escribe un numero: "))
numero1 = 0
numero2 = 1
iniciador = 0

while iniciador < numero:
    print(" ",numero2, end=",")
    aux = numero2 # guardamos el valor de b iniciado en 1 
    numero2 = numero1 + numero2 # Sumamos el valor anterior a b y b cambia su valor
    numero1 = aux # ahora valor de b que era 1 ahora pasa a a
    iniciador += 1

