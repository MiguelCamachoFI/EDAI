#Realizado con Python 3.8.10 64-bits en Ubuntu 20.04.2 LTS mediante WSL
#Importar la librería math
import math
#Definir la función math
def factorial(n):
    #Regresar el resultado mediante la función math.factorial()
    return math.factorial(n)
#Calculadora con menú
op='0'
while op!='7':
    print("¿Qué desea hacer?")
    print("1) Suma\n 2) Resta\n 3) Multiplicación\n 4) División y módulo\n 5) Potencia\n 6) Factorial\n 7) Salir")
    op=input("Elige una opción: ")
    if op=='1':
        print("Ha seleccionado suma")
        #Pedirle a usuario que ingrese 2 números de tipo float
        n1=float(input("Introduce tu primer número: "))
        n2=float(input("Introduce tu segundo número: "))
        #Imprimir la suma
        print("La suma de",n1,"+",n2,"es igual a",n1+n2,"\n")
    elif op=='2':
        print("Ha seleccionado resta")
        #Pedirle a usuario que ingrese 2 números de tipo float
        n1=float(input("Introduce tu primer número: "))
        n2=float(input("Introduce tu segundo número: "))
        #Imprimir la resta
        print("La resta de",n1,"-",n2,"es igual a",n1-n2,"\n")
    elif op=='3':
        print("Ha seleccionado multiplicación")
        #Pedirle a usuario que ingrese 2 números de tipo float
        n1=float(input("Introduce tu primer número: "))
        n2=float(input("Introduce tu segundo número: "))
        #Imprimir la multiplicación
        print("El producto de",n1,"*",n2,"es igual a",n1*n2,"\n")
    elif op=='4':
        print("Ha seleccionado división y módulo")
        #Pedirle a usuario que ingrese 2 números de tipo float
        n1=float(input("Introduce tu primer número: "))
        n2=float(input("Introduce tu segundo número: "))
        #Evaluar si n2=0
        if n2==0:
            print("La división es indefinida, por lo tanto no tiene módulo\n")
        else:
            #Imprimir la división
            print("La división de",n1,"/",n2,"es igual a",n1/n2)
            #Imprimir el módulo
            print("El módulo de",n1,"%",n2,"es igual a",n1%n2,"\n")
    elif op=='5':
        print("Ha seleccionado potencia")
        #Pedirle a usuario que ingrese 2 números de tipo float
        n1=float(input("Introduce tu primer número: "))
        n2=float(input("Introduce tu segundo número: "))
        #Imprimir la potencia
        print("La potencia de",n1,"**",n2,"es igual a",n1**n2,"\n")
    elif op=='6':
        print("Ha seleccionado factorial")
        #Preguntarle al usuario que ingrese un factorial
        n=int(input("Ingrese un factorial: "))
        print("El factorial de", n,"es", factorial(n),"\n")
    elif op=='7':
        #Si el usuario decide salir del programa
        print("Gracias por usar mi programa")
    else:
        #Si el usuario selecciona una opción no válida
        print("Opción no válida :(","\n")