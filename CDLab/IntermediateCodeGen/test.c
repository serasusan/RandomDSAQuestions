#include<stdio.h>
#include<string.h>

void gen_code_for_operator(char *inp,char opr,char *reg){
    char temp[30];
    int i=0,j=0;
    while(inp[i]!='\0'){
        if(inp[i]==opr){
            printf("%c\t%c\t%c\t%c\n",opr,*reg,inp[i-1],inp[i+1]);
            temp[j-1]=*reg;
            i+=2;
            (*reg)--;
            continue;
        }
        temp[j]=inp[i];
        i++;
        j++;
    }
    temp[++j]='\0';
    strcpy(inp,temp);
}


void gen_code(char *inp){
    char reg = 'Z';
    gen_code_for_operator(inp,'/',&reg);
    gen_code_for_operator(inp,'*',&reg);
    gen_code_for_operator(inp,'+',&reg);
    gen_code_for_operator(inp,'-',&reg);
    gen_code_for_operator(inp,'=',&reg);
}

void main(){
    char input[100];
    printf("Enter the expression\n");
    scanf("%s",input);
    printf("Optr\tDestn\tOp1\tOp2\n");
    gen_code(input);
    printf("Input : %s",input);
}