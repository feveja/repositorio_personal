#include <stdio.h>
main() {
    // Declarar la variable para almacenar el número ingresado por el usuario
    int numero;

    // Solicitar al usuario que ingrese un número
    printf("Ingrese un número: ");
    scanf("%d", &numero);
    // %d actúa como marcador de posición para el valor entero que se proporciona después de la coma.

    // Verificar si el número es par o impar utilizando una estructura selectiva doble if(condicion)...
    if (numero % 2 == 0) {
        printf("El número %d es par.\n", numero);
    } else {
        printf("El número %d es impar.\n", numero);
    }

    return 0;
}
