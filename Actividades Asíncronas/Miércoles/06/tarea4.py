#Realizado con Python 3.8.10 64-bits en Ubuntu 20.04.2 LTS mediante WSL
#Definir una función para convertir de binario a decimal
def binaryToDecimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    #Imprimir el valor en decimales
    print(decimal)   
#Código de inicio
if __name__ == '__main__':
    bynary=int(input("Ingrese un valor binario de 4 bits a convertir: "))
    binaryToDecimal(bynary)