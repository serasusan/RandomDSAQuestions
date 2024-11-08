#include<stdio.h>

void main(){
    int x = 5;
    int *ptr = &x;
    int **ptr2 = &ptr;
    printf("The value of x is %d\n", x);
    printf("The address of x is %d\n", &x);
    printf("The value of x is %d\n", *ptr);
    printf("The address of x is %d\n", ptr);
    printf("The value of x is %d\n", **ptr2);
    printf("The address of x is %d\n", *ptr2);
    int ***ptr3 = &ptr2;
}