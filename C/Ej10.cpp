
int main() {
    int numero;

    // Solicitar al usuario ingresar un número
    printf("Ingrese un número entero positivo: ");
    scanf("%d", &numero);

    // Imprimir un contador regresivo con do-while
    do {
        printf("%d ", numero);
        numero--;
    } while (numero >= 1);

    printf("\n");

    return 0;
}

