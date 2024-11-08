#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>


struct exp{
    char op[2],op1[5],op2[5],res[5];
    int flag;
} arr[10];

int n;
void constant();
void output();
void change(int p,char *res);

void main(){
    printf("Enter the number of expressions\n");
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        scanf("%s",arr[i].op);
        scanf("%s",arr[i].op1);
        scanf("%s",arr[i].op2);
        scanf("%s",arr[i].res);
        arr[i].flag = 0;
    }
    constant();
    output();
}

void constant(){
    int i;
    int op1,op2,res;
    char res1[5];
    char op;
    for(i=0;i<n;i++){
        if(isdigit(arr[i].op1[0]) && isdigit(arr[i].op2[0]) || strcmp(arr[i].op,"=")==0){
            op1 = atoi(arr[i].op1);
            op2 = atoi(arr[i].op2);
            op = arr[i].op[0];
            switch(op){
                case '+':
                    res = op1+op2;
                    break;
                case '-':
                    res = op1-op2;
                    break;
                case '*':
                    res = op1*op2;
                    break;
                case '/':
                    res = op1/op2;
                    break;
                case '=':
                    res = op1;
                    break;
            }
            sprintf(res1,"%d",res);
            arr[i].flag = 1;
            change(i,res1);
        }
    }
}

void change(int p, char *res){
    for(int i = p+1;i<n;i++){
        if(strcmp(arr[p].res,arr[i].op1)==0){
            strcpy(arr[i].op1,res);
        }
        if(strcmp(arr[p].res,arr[i].op2)==0){
            strcpy(arr[i].op2,res);
        }
    }
}

void output(){
    int i=0;
    printf("Optimized Code\n");
    for(int i=0;i<n;i++){
        if(!arr[i].flag){
            printf("%s %s %s %s\n",arr[i].op,arr[i].op1,arr[i].op2,arr[i].res);
        }
    }
}