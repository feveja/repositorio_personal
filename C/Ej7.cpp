#include <stdio.h>

main() {
    int i = 1;
    while (i <= 10) {
        if (i % 2 == 0) {
            printf("%d es par\n", i);
        } else {
            printf("%d es impar\n", i);
        }
        i++;
    }
    return 0;
}