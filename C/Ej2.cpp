#include <stdio.h>

main() {
    // Declaracion de variables
    float importeTotal, importeFinal;
    const float descuento = 0.2;  // 20%

    // Solicitar al usuario el importe total de la compra
    printf("Ingrese el importe total de la compra: $");
    scanf("%f", &importeTotal);
    // Verificar si el importe total es igual o mayor a $50 para aplicar el descuento
    if (importeTotal >= 50) {
        // Calcular el importe final con descuento
        importeFinal = importeTotal - (importeTotal * descuento);

        // Mostrar el importe final que debe pagar el cliente
        printf("El importe a pagar con descuento es: $%.2f\n", importeFinal);
    } else {
        // Si el importe total es menor a $50, no se aplica descuento
        printf("El importe a pagar sin descuento es: $%.2f\n", importeTotal);
    }

    return 0;
}

