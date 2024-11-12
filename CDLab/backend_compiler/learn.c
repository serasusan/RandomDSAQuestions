#include<stdio.h>
#include<stdlib.h>
#include<string.h>

void main(){
    char icode[30][30],opr[10];
    int i=0,j=0;

    printf("Enter the icode(Terminated by exit\n");
    do{
        scanf("%s",icode[i]);
    }while(strcmp(icode[i++],"exit")!=0);
    i = 0;
    printf("%c",icode[0][2]);
    while(strcmp(icode[i],"exit")!=0){
        switch(icode[i][3]){
            case '+':
                strcpy(opr,"ADD");
                break;
            case '-':
                strcpy(opr,"SUB");
                break; 
            case '*':
                strcpy(opr,"MUL");
                break;
            case '/':
                strcpy(opr,"DIV");
                break;      
        }

        printf("MOV %c,R%d\n",icode[i][2],j);
        printf("%s %c,R%d\n",opr,icode[i][4],j);
        printf("MOV R%d,%c\n",j,icode[i][0]);
        j++;
        i++;
    }
}