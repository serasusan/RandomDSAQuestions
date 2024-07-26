#include<stdio.h>

int main(){
    long nc = 0;
    int c;

    while((c = getchar()) != EOF)
    {
        printf("Character: %c\n", c);
        nc++;
    }

    printf("Loop ended. EOF value: %d\n", EOF);
    return 0;
}