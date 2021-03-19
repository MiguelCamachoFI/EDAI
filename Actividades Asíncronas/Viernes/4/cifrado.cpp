#include<stdio.h>
#include<stdlib.h>
#include<iostream>
using namespace std;
/*
 Programa que realiza la implementación del cifrado César
*/
#define TAM_PALABRA 20
#define TAM_ABC 26
char abecedarioEnClaro[TAM_ABC] =
{'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T'
,'U','V','W','X','Y','Z'};
char abecedarioCifrado[TAM_ABC] =
{'D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W'
,'X','Y','Z','A','B','C'};
void cifrar(char *textoEnClaro);
void descifrar(char *textoCifrado);
int main(){
    short opcion = 0, contador;
    char palabra[TAM_PALABRA];
    while (1){
        cout<<"CIFRADO CÉSAR"<<endl;
        for (contador=0 ; contador<26; contador++)
        cout<<*(abecedarioEnClaro+contador);
        cout<<"\n";
        for (contador=0 ; contador<26; contador++)
        cout<<*(abecedarioCifrado+contador);
        cout<<"\n";
        cout<<"\nElegir una opción:\n";
        cout<<"1) Cifrar\n";
        cout<<"2) Descifrar.\n";
        cout<<"3) Salir.\n";
        cin>>opcion;
        switch(opcion){
            case 1:
            cout<<"Ingresar la palabra a cifrar (en mayúsculas): "<<endl;
            cin>>palabra;
            cifrar(palabra);
            break;
            case 2:
            cout<<"Ingresar la palabra a descifrar (en mayúsculas): "<<endl;
            cin>>palabra;
            descifrar(palabra);
            break;
            case 3:
            return 0;
            default:
            cout<<"Opción no válida."<<endl;
        }
    }
    return 0;
}
//Cifrar mensaje
void cifrar(char *textoEnClaro){
    cout<<"El texto cifrado es: ", textoEnClaro;
    int contadorAbcedario, contadorPalabra, indice = 0;
    for (contadorPalabra=0 ; contadorPalabra<textoEnClaro[contadorPalabra] ;
    contadorPalabra++)
    for (contadorAbcedario=0 ; contadorAbcedario<TAM_ABC ;
    contadorAbcedario++)
    if (abecedarioEnClaro[contadorAbcedario] ==
    textoEnClaro[contadorPalabra]){
        //Mostrar mensaje cifrado
        cout<<abecedarioCifrado[contadorAbcedario];
        contadorAbcedario = 26;
    }
    cout<<"\n"<<endl;
}
//Descifrar mensaje
void descifrar(char *textoCifrado){
    cout<<"El texto %s descifrado es: ", textoCifrado;
    int contadorAbcedario, contadorPalabra, indice = 0;
    for (contadorPalabra=0 ; contadorPalabra<textoCifrado[contadorPalabra] ;
    contadorPalabra++)
    for (contadorAbcedario=0 ; contadorAbcedario<TAM_ABC ;
    contadorAbcedario++)
    if (abecedarioCifrado[contadorAbcedario] ==
    textoCifrado[contadorPalabra]){
        //Mostrar mensaje descifrado
        cout<<abecedarioEnClaro[contadorAbcedario];
        contadorAbcedario = 26;
    }
    cout<<"\n"<<endl;
}