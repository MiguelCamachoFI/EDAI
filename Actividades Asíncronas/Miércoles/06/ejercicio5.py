#Realizado con Python 3.8.10 64-bits en Ubuntu 20.04.2 LTS mediante WSL
#Pedirle a usuario que ingrese 2 números de tipo float
n1=float(input("Introduce tu primer número: "))
n2=float(input("Introduce tu segundo número: "))
#Imprimir la suma
print("La suma de",n1,"+",n2,"es igual a",n1+n2)
#Imprimir la resta
print("La resta de",n1,"-",n2,"es igual a",n1-n2)
#Imprimir la multiplicación
print("El producto de",n1,"*",n2,"es igual a",n1*n2)
#Evaluar si n2=0
if n2==0:
    print("La división es indefinida, por lo tanto no tiene módulo")
else:
    #Imprimir la división
    print("La división de",n1,"/",n2,"es igual a",n1/n2)
    #Imprimir el módulo
    print("El módulo de",n1,"%",n2,"es igual a",n1%n2)
#Imprimir la potencia
print("La potencia de",n1,"**",n2,"es igual a",n1**n2)