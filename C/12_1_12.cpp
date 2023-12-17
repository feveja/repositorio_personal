/* Programa: Validar hora */

#include <conio.h>
#include <stdio.h>

int main()
{
    int h, m, s;

    printf( "\n   Introduzca horas: " );
    scanf( "%d", &h );
    printf( "\n   Introduzca minutos: " );
    scanf( "%d", &m );
    printf( "\n   Introduzca segundos: " );
    scanf( "%d", &s );

    if ( h >= 0 && h <= 23 && m >= 0 && m <= 59 && s >= 0 && s <= 59 )
        printf( "\n   HORA CORRECTA" );
    else
        printf( "\n   HORA INCORRECTA" );

    getch(); /* Pausa */

    return 0;
}