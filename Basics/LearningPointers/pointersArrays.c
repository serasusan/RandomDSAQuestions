#include<stdio.h>

void SumofElements(int A[], int size){
    int i, sum = 0;
    // int size = sizeof(A)/sizeof(A[0]); // This will not work as the array is passed by reference and not by value
    // printf("Size of array in function = %d\n", size);
    for(i = 0; i < size; i++){
        sum += A[i];
    }
    printf("Sum of elements = %d\n", sum);
}

void doubleArray(int A[], int size){ //int *A is also valid
    for(int i = 0; i < size; i++){
        A[i] = 2*A[i];
    }
}
void main(){
    int A[] = {2, 4, 5, 8, 1};
    int *p = A;
    printf("Address of first element of the array is %d\n", A);
    printf("Address of first element of the array is %d\n", &A[0]);
    printf("Address of first element of the array is %d\n", p);
    printf("Value of first element of the array is %d\n", *p);
    printf("Value of first element of the array is %d\n", A[0]);
    printf("Value of second element of the array is %d\n", *(p+1));
    
    for(int i = 0; i < 5; i++){
        printf("Address using A+i = %d\n", A+i);
        printf("Address using p++= %d\n",p++);
        printf("Address using &A[i] = %d\n", &A[i]);
        printf("Value = %d\n", A[i]);
        printf("Value = %d\n", *(A+i));
        printf("Value using p = %d\n", *(p-1));
    }
    int size = sizeof(A)/sizeof(A[0]);
    SumofElements(A, size);
    doubleArray(A, size);
    for(int i = 0; i < size; i++){
        printf("%d ", A[i]);
    }
}