#include <stdio.h>

int main() {
    float nota;

    // Solicitar la nota al usuario y asegurarse de que esté en el rango de 1 a 7
    printf("Ingresa la nota del alumno (entre 1 y 7): ");
    scanf("%f", &nota);

    while (nota < 1 || nota > 7) {
        printf("Por favor, ingresa una nota válida en el rango de 1 a 7.\n");
        printf("Ingresa la nota del alumno (entre 1 y 7): ");
        scanf("%f", &nota);
    }

    // Evaluar la nota e imprimir el comentario correspondiente
    if (nota >= 7.0) {
        printf("Excelente\n");
    } else if (nota >= 6.0) {
        printf("Muy Bueno\n");
    } else if (nota >= 5.0) {
        printf("Bueno\n");
    } else if (nota >= 4.0) {
        printf("Regular\n");
    } else {
        printf("Malo\n");
    }

    return 0;
}
