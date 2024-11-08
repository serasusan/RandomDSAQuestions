#include<stdio.h>

void main(){
    int a = 1025; // 00000000 00000000 00000100 00000001
    int *ptr = &a;
    printf("Size of integer is %d bytes\n", sizeof(int));
    printf("Address = %d, value = %d\n", ptr, *ptr);
    printf("Address = %d, value = %d\n", ptr+1, *(ptr+1));  
    char *ptr2;
    ptr2 = (char*)ptr; // typecasting
    printf("Size of char is %d bytes\n", sizeof(char));
    printf("Address = %d, value = %d\n", ptr2, *ptr2);
    printf("Address = %d, value = %d\n", ptr2+1, *(ptr2+1));
//     Size of integer is 4 bytes
//     Address = -1161920956, value = 1025
//     Size of char is 1 bytes
//     Address = -1161920956, value = 1

//     This is because when we typecast the pointer to a char pointer, it will only read the first byte of the integer.
    void *ptr3;
    ptr3 = ptr;
    printf("Address = %d\n", ptr3);
    // printf("Value = %d\n", *ptr3); // This will give an error as void pointers cannot be dereferenced
}