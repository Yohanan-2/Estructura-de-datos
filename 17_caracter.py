#14/09/2024
#Jesus Yohanan Zempoaltecatl Lima
#Estructura y organizacion de datos
text = input("Escribe un texto largo: "); i=0
palabra = input("Esribe la palabra que deseas encontrar: ")
aux = len(text); aux2 = 0; write = ""
while i < aux:
    if text[i] == " " or i == (aux-1):
        if i == (aux-1):
            write = text[aux2:i+1]
        else:
            write = text[aux2:i]
        print("\n\n",write,"\n\n")
        if write == palabra:
            print("La palabra fue encontrada [",aux2,":",i,"]: ", write)
            i = aux+1
        else:
            aux2 = i+1  
            print("no encontrado\n*************\n")
    i +=1
    
print("********************************************\npuede comprobarlo escribiendo viendo los indices",)
i = int(input("¿Quiere comprobarlo?\n1:si\n2:no\n: "))
if i == 1:
    #aux = int(input("Escribe la primera coordenada de la izquierda: "))
    #aux2 = int(input("Escribe la segunda coordenada: ")); i = 0
    i=0; print("\n")
    while i < len(text):
        print(i,": ",text[i])
        i+=1