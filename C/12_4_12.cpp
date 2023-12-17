/* Programa: Área de un cubo */

#include <conio.h>
#include <math.h>
#include <stdio.h>

int main()
{
    float arista;

    printf( "\n   Introduzca arista: " );
    scanf( "%f", &arista );

    /* Filtramos la arista */

    while ( arista <= 0 )
    {
        printf( "\n   ERROR: La arista debe ser mayor que cero." );
        printf( "\n\n   Introduzca arista: " );
        scanf( "%f", &arista );
    }

    printf( "\n   El %crea de un cubo de arista %f es: %f", 160, arista, 6 * pow( arista, 2 ) );
    getch(); /* Pausa */

    return 0;
}