#include<stdio.h>
#include<stdlib.h>
int fib(int num);

int main(){
    int n,x;
    printf("Ingresa el valor de n: ");
    scanf("%d",&n);
    x=fib(n);
    printf("El valor de fib(%d) es %d",n,x);
    return 0;
}
int fib(int num){
    if (num==0)
       return 1;
    if (num==1)
       return 1;
    return fib(num-1)+fib(num-2);  
}