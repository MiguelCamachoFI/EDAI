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
    print("El valor en decimal de",bynary, "es",decimal)   
#Código de inicio
if __name__ == '__main__':
    #Evaluar si el número ingresado es un número binario
    while True:
        try:
            # Pedirle al usuario que ingrese un número binario de 4 bits a convertir
            bynary = int(input("Ingrese un número binario de 4 bits: "))
        except ValueError: # Si el valor no es un número entero
            print('Debe de ser un número binario (contener solo 1s y 0s)')
        else:
            # Iteractuar a través de todos los dígitos en x
            for i in str(bynary):
                if i in '10': # Si el dígito es 1 o 0
                    binary = True
                else:
                    binary = False
                    break
            if binary == False:
                print('Debe ser un número binario (contener solo 1s y 0s)')
            elif len(str(bynary))!=4:
                print("Debe ser un número de 4 bits")
            else:
                break # El número es binario, es seguro romper con el bucle.
    #Imprimir número binario ingresado
    print(bynary, "es binario y de 4 dígitos")
    binaryToDecimal(bynary)
