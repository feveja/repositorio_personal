#include <stdio.h>

main() {
    int numero;

    // Solicitar al usuario que ingrese un número
    printf("Ingresa un número entero: ");
    scanf("%d", &numero);

    // Verificar si el número es par o impar usando el operador %
    if (numero % 2 == 0) {
        printf("El número %d es par.\n", numero);
    } else {
        printf("El número %d es impar.\n", numero);
    }

    // Utilizar un bucle while para imprimir los números del 1 al 10
    int contador = 1;
    printf("Imprimir números del 1 al 10:\n");
    while (contador <= 10) {
        printf("%d ", contador);
        contador++;
    }
    printf("\n");

    return 0;
}
