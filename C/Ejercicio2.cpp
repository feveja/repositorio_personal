#include <stdio.h>

main() {
    // Declaraci�n de variables
    int numero;

    // Solicitar al usuario ingresar un n�mero
    printf("Ingrese un numero: ");
    scanf("%d", &numero);

    // Verificar si el n�mero es par o impar
    if (numero % 2 == 0) {
        // Si el residuo de la divisi�n por 2 es cero, el n�mero es par
        printf("%d es un numero par.\n", numero);
    } else {
        // Si el residuo de la divisi�n por 2 no es cero, el n�mero es impar
        printf("%d es un numero impar.\n", numero);
    }

    return 0;
}

