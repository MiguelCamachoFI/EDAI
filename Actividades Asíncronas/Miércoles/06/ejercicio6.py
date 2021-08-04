#Realizado con Python 3.8.10 64-bits en Ubuntu 20.04.2 LTS mediante WSL
#Pedir al usuario que ingrese un número entero
num = int(input("Ingrese un número: "))
#Inicializar fac en 1
fac = 1
#Iniciar ciclo for
for i in range(1, num + 1):
    fac = fac * i
#Imprimir el resultado
print("El factorial de", num, "es", fac)