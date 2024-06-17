//print 5 stars

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int i;
    for(i=1;i<=5;i++)
    {
        for(int j=1;j<=i;j++){
            printf("*");
        }
        printf("\n");
    }
}