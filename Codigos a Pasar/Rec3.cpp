#include <stdio.h>

main() {
    int num;

    // Solicitar entrada de usuario
    printf("Ingrese un n�mero: \n");
    scanf("%d", &num);

    // Comprobar si el numero es positivo, negativo o cero
    if (num > 0) {
        printf("El numero ingresado es positivo");
    } else if (num < 0) {
        printf("El numero ingresado es negativo");
    } else {
        printf("El numero ingresado es igual a cero");
    }

    return 0;
}
