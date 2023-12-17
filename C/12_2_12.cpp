/* Programa: Número cercano al 1 ó al 0 */

#include <conio.h>
#include <stdio.h>

int main()
{
    float numero;

    printf( "\n   Introduzca un numero real: ", 163 );
    scanf( "%f", &numero );

    if ( numero > 0.5 )
        printf( "\n   Esta mas cercano al 1", 160, 160 );
    else

        if ( numero < 0.5 )
            printf( "\n   Esta mas cercano al 0", 160, 160 );
        else
            printf( "\n   Esta en medio", 160 );

    getch(); /* Pausa */

    return 0;
}