#Jesus yohanan Zempoaltecatl Lima 
#Materia Orgnizacion y estructurado de datos
from math import sqrt
a = int(input("Escribe a: "))
b = int(input("Escribe b: "))
c = int(input("Escribe c: "))
x1 = 0
x2 = 0
p = (b*b) - (4*a*c)
print("P es: ",p)
if p == 0:
    x1 = (-1*b) / (2*a)
    print(x1)
if p > 0: 
    x1 = ((-1*b) + (sqrt(p)))/(2*a)
    x2 = ((-1*b) - (sqrt(p)))/(2*a)
    print("Resultado x1: ",x1)
    print("Resultado x2: ",x2)
if p<0:
    print("No existe solucion real")