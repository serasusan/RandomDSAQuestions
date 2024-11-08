#include<stdio.h>

void main(){
    int a = 6;
    int *ptr = &a;
    printf("The value of a is %d\n", a);
    printf("The address of a is %u\n", &a);
    printf("The value of a is %d\n", *ptr);
    printf("The address of a is %u\n", ptr);
    *(ptr+1 )= 7; // This will cause a segmentation fault as we are trying to access memory that is not allocated to us
    // causes segmentation fault during runtime
    printf("%d\n", (*(ptr+1)));

}