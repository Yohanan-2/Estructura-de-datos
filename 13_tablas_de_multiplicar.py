#Jesus yohanan Zempoaltecatl Lima 
#Materia Orgnizacion y estructurado de datos
i = 1; j = 1; aux = 0; aux2 = 0; ass = 0; tabla = int(input("¿Hasta que tbla de multiplicar quiere?: "))
op = 10-((2*tabla) % 10) #crea un limite para imprimir
if ((2*tabla) % 10) == 0:
    op = 0
ark = ((2*tabla) + op)#ayuda a crear el limite de las tablas de multiplicar es decir hasta la tabla X
print(ark)
while i<=10:
    print()
    while j<=5:
        if (j+aux)<= tabla:
            if ((j+aux)*(i-aux2))<10:
                print((j+aux)," X ",(i-aux2), " = ",str((j+aux)*(i-aux2)), end="    ")
            else:
                if (i-aux2)==10:
                    print((j+aux)," X ",(i-aux2), "=",str((j+aux)*(i-aux2)), end="    ")
                else:
                    print((j+aux)," X ",(i-aux2), " =",str((j+aux)*(i-aux2)), end="    ")
        j += 1
    if i==10 :
        i = 0 #reiniciamos el bucle
        print()
        aux += 5 # ayuda a crear la fila de abajo  
    i+=1
    j=1
    ass += 1
    if ass == (ark): #ass es un limite de impresion por fila de cada tabla, es decir crea la multiplicacion de 1 hasta 10 de cada uno
        i = 11
    #if ass == (ark): copia de seguridad para que puedas hacer una prube quintando (ark) y poniendo un 6
    #   i=11
    # el limite es 10 
    # si quieres saber porque puedes poner en cada print antes de (j+aux) que imprimira ass+1,"---",
    

