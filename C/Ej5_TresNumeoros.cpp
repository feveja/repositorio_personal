#include <stdio.h>

int main() {
    int num1, num2, num3;

    // Leer tres números enteros en el rango de 1 a 848
    printf("Ingresa tres números enteros (entre 1 y 848): ");
    scanf("%d %d %d", &num1, &num2, &num3);

    while (num1 < 1 || num1 > 848 || num2 < 1 || num2 > 848 || num3 < 1 || num3 > 848) {
        printf("Por favor, asegúrate de que los números estén en el rango de 1 a 848.\n");
        printf("Ingresa tres números enteros (entre 1 y 848): ");
        scanf("%d %d %d", &num1, &num2, &num3);
    }

    // Encontrar el mayor de los tres números
    int mayor;

    if (num1 >= num2 && num1 >= num3) {
        mayor = num1;
    } else if (num2 >= num1 && num2 >= num3) {
        mayor = num2;
    } else {
        mayor = num3;
    }

    // Imprimir el mayor
    printf("%d es el mayor.\n", mayor);

    // Imprimir los números en orden descendente
    printf("Los números en orden descendente son: ");
    if (mayor == num1) {
        if (num2 >= num3) {
            printf("%d %d %d\n", mayor, num2, num3);
        } else {
            printf("%d %d %d\n", mayor, num3, num2);
        }
    } else if (mayor == num2) {
        if (num1 >= num3) {
            printf("%d %d %d\n", mayor, num1, num3);
        } else {
            printf("%d %d %d\n", mayor, num3, num1);
        }
    } else {
        if (num1 >= num2) {
            printf("%d %d %d\n", mayor, num1, num2);
        } else {
            printf("%d %d %d\n", mayor, num2, num1);
        }
    }

    return 0;
}
