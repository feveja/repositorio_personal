#include <stdio.h>

main() {
    float celsius, fahrenheit;

    // Solicitar entrada de usuario
    printf("Ingrese la temperatura en grados Celsius: \n");
    scanf("%f", &celsius);

    // Calcular la temperatura en grados Fahrenheit
    fahrenheit = (celsius * 9/5) + 32;

    // Mostrar el resultado
    printf("La temperatura en grados Fahrenheit es: %.2f", fahrenheit);

    return 0;
}
