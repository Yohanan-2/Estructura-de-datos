#Jesus yohanan Zempoaltecatl Lima 
#Materia Orgnizacion y estructurado de datos
#---------------------------------------
#Elaborar un programa, que calcule las raices de una ecuacion mediante el metodo rapson de manera repetitiva el programa debera pedir un numero maxico de iteraciones o detener el calculo de la raiz cuando el valor de X se repita hasta la segunda
#------------------------------------------s
n = int(input("Cuantas interaciones quieres:"))
x = 1
i = 0
while i < n:
    aux = int((x*100000)%100000)
    #x = x - (((x*x*x)-x-1)/((3*x*x)-1))
    x = x -(((5*x*x*x)+(x/2)+3)/((15*x*x)+(1/2)))
    if (aux - int((x*100000)%100000)) == 0:
        i = n+1
    i += 1
print(x)