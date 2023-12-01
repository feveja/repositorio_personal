#include <stdio.h>

main() {
    int numero, suma = 0;

    // Solicitar al usuario ingresar números positivos
    do {
        printf("Ingrese un número positivo (o un número negativo para salir): ");
        scanf("%d", &numero);

        // Sumar solo si el número es positivo
        if (numero > 0) {
            suma += numero;
        }

    } while (numero >= 0);

    // Imprimir la suma
    printf("La suma de los números positivos ingresados es: %d\n", suma);

    return 0;
}
