/* Programa: Dígitos de un número entero */

#include <conio.h>
#include <stdio.h>

int main()
{
    int n;

    printf( "\n   Introduzca un numero entero: ", 163 );
    scanf( "%d", &n );

    if ( n >= -9 && n <= 9 )
        printf( "\n   Tiene 1 digito.", 161 );
    else
        if ( n >= -99 && n <= 99 )
            printf( "\n   Tiene 2 digitos.", 161 );
        else
            if ( n >= -999 && n <= 999 )
                printf( "\n   Tiene 3 digitos.", 161 );
            else
                printf( "\n   Tiene mas de 3 digitos.", 160, 161 );

    getch(); /* Pausa */

    return 0;
}
