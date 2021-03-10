#include <stdio.h>
int main(void)
{
    unsigned short sudoku[9][9];
    unsigned short resultado = 1;
    unsigned short i, j, k;
    char nombre[26];
    
    // Ingreso de nombre del usuario
    printf("\nIngrese su nombre, por favor: \n");
    scanf("%25[^\n]s", nombre);
    getchar();

    // Ingreso de los números del Sudoku
    printf("\nIngrese con espacios los valores del Sudoku\n");
    printf("\nCuando termine de ingresar 9 valores, de enter para ingresar los valores del renglón siguiente\n");
    
    unsigned short *cifra = (unsigned short *) sudoku;
    // Iteración para el ingreso de números de cada casilla del sudoku.
    for (i = 0 ; i < 81 ; i++)
        scanf("%hu", cifra + i);
    
    cifra = (unsigned short *) sudoku;
    // Iteración para corroborar si hay algún cero en el sudoku.
    for (i = 0 ; i < 81 ; i++)
        if (*(cifra + i) == 0)
        {
            resultado = 0;
            break;
        }
    if (resultado == 0)
        printf("\n%s: No finalizado\n", nombre);
    else
    {
        // Iteracion para verificar si el número de la casilla se repite en la fila  correspondiente.
        for (i = 0 ; i < 9 ; i++)
        {
            for (j = 0 ; j < 8 ; j++)
            {
                for (k = j + 1 ; k < 9 ; k++)
                {
                    if(sudoku[i][j] == sudoku[i][k])
                    {
                        //printf("sudoku[%hu][%hu] == sudoku[%hu][%hu]\n",i,j,i,k);
                        resultado = 0;
                        break;
                    }
                }
                if (resultado == 0)
                    break;
            }
            if (resultado == 0)
                break;
        }
        
        if (resultado == 0)
            printf("\n%s: No logrado\n", nombre);
        else
        {
           // Iteración para verificar si un número se repite en alguna columan del sudoku.
            for (j = 0 ; j < 9 ; j++)
            {
                for (i = 0 ; i < 8 ; i++)
                {
                    for (k = i + 1 ; k < 9 ; k++)
                    {
                        if (sudoku[i][j] == sudoku[k][j])
                        {
                            resultado = 0;
                            break;
                        }
                    }
                    if (resultado == 0)
                    break;
                }
                if (resultado == 0)
                    break;
            }
            
            if (resultado == 0)
                printf("\n%s: No logrado\n", nombre);
            else
                printf("\n%s: Logrado\n", nombre);
        }
        
    }
    
    return 0;
}