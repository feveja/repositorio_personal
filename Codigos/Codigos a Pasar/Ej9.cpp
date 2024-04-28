#include <stdio.h>

int main() {
    int num, i;

    // Solicitar al usuario ingresar un número
    printf("Ingrese un número entero: ");
    scanf("%d", &num);

    // Imprimir la tabla de multiplicar con bucle for
    for (i = 1; i <= 10; i++) {
        printf("%d x %d = %d\n", num, i, num * i);
    }

    return 0;
}
