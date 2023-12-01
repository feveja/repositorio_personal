#include <stdio.h>

main() {
    int a, b, c, sum;
    float avg;

    // Solicitar entrada de usuario
    printf("Ingrese 3 n�meros: \n");
    scanf("%d %d %d", &a, &b, &c);

    // Calcular la suma
    sum = a + b + c;

    // Calcular el promedio de los tres n�meros
    avg = sum / 3.0;

    // Mostrar la suma y el promedio
    printf("Suma = %d \n", sum);
    printf("Promedio = %.2f", avg);

    return 0;
}
