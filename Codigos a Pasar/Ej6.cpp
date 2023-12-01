#include <stdio.h>

main() {
    int num, factorial = 1, i = 1;
    printf("Ingrese un número entero positivo: ");
    scanf("%d", &num);
    if (num < 0) {
        printf("El número ingresado es negativo\n");
    } else {
        do {
            factorial *= i;
            i++;
        } while (i <= num);
        printf("El factorial de %d es %d\n", num, factorial);
    }
    return 0;
}