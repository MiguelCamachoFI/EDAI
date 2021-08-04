#Realizado con Python 3.8.10 64-bits en Ubuntu 20.04.2 LTS mediante WSL
#Pedir al usuario que ingrese un número entero
num = int(input("Ingrese un número: "))
#Inicializar fac y i en 1
fac = 1
i = 1
#Iniciar ciclo while
while i <= num:
    fac = fac * i
    i = i + 1
#Imprimir el resultado
print("El factorial de", num, "es", fac)