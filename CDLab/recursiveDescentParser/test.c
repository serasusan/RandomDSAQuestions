#include<stdio.h>
#include<stdlib.h>
#include<string.h>

char inp[20],Output[30],inp_ptr=0;
void E();
void T();
void T_Prime();
void E_Prime();
void F();

void E(){
    int temp, length = strlen(Output);
    //find E
    for(temp=0;temp<length && Output[temp]!='E';temp++);
    //shift
    for(int i=length;i>temp;i--)
        Output[i+2]=Output[i];
    //Replace
    Output[temp++]='T';
    Output[temp++]='E';
    Output[temp++]=39;
    printf("E=%-25s",Output);
    printf("E->TE'\n");
    T();
    E_Prime();
}

void E_Prime()
{
    int temp;
    for(temp=0;temp<strlen(Output) && Output[temp]!='E';temp++);
    if(inp[inp_ptr]=='+'){
        for(int i=strlen(Output);i>temp;i--){
            Output[i+3]=Output[i];
        }
        Output[temp++]='+';
        Output[temp++]='T';
        Output[temp++]='E';
        Output[temp++]=39;
        printf("E=%-25s",Output);
        printf("E'->+TE'\n");
        inp_ptr++;
        T();
        E_Prime();
    }
    else{
        for(int i=temp;i<strlen(Output);i++){
            Output[i]=Output[i+2];
        }
        printf("E=%-25s",Output);
        printf("E'->e\n");
    }
}

void T()
{
    int i,temp,len = strlen(Output);
    //find T
    for(temp=0;temp<len && Output[temp]!='T';temp++);
    //Shift
    for(i=len;i>temp;i--){
        Output[i+2] = Output[i];
    }
    //Insert
    Output[temp++] = 'F';
    Output[temp++] = 'T';
    Output[temp++] = 39;
    //print
    printf("E=%-25s",Output);
    printf("T->FT'\n");
    //recursively call
    F();
    T_Prime();
}

void F()
{
    int temp;
    for(temp=0;temp<strlen(Output) && Output[temp]!='F';temp++);
    if(inp[inp_ptr]=='i'){
        Output[temp] = 'i';
        printf("E->%-25s",Output);
        printf("F->i\n");
        inp_ptr++;
    }
    else if(inp[inp_ptr]=='('){
        for(int i = strlen(Output);i>temp;i--){
            Output[i+2]=Output[i];
        }
        Output[temp++]='(';
        Output[temp++]='E';
        Output[temp++]=')';
        printf("E=%-25s",Output);
        printf("F->(E)\n");
        inp_ptr++;
        E();
        if(inp[inp_ptr]==')'){
            inp_ptr++;
        }
        else{
            printf("Parsing failed\n");
            exit(1);
        }
    }
    else{
        printf("Parsing Failed\n");
        exit(1);
    }
}

void T_Prime(){
    int temp, l = strlen(Output);
    for(temp=0;temp<l && Output[temp]!='T';temp++);
    if(inp[inp_ptr]=='*'){
        for(int i=l;i>temp;i--){
            Output[i+3]=Output[i];
        }
        Output[temp++]='*';
        Output[temp++]='F';
        Output[temp++]='T';
        Output[temp++]=39;
        printf("E=%-25s",Output);
        printf("T'->*FT'\n");
        inp_ptr++;
        F();
        T_Prime();
    }
    else{
        for(int i=temp;i<l;i++){
            Output[i]=Output[i+2];
        }
        printf("E=%-25s",Output);
        printf("T'->e\n");
    }
}
void main(){
    printf("The grammar is \n");
    printf("E->TE'\nE'->+TE'|e\nT->FT'\nT'->*FT'|e\nF->(E)|i\n");
    printf("Enter the input\n");
    scanf("%s",inp);
    printf("Expressions\t");
    printf("Sequence of production rules\n");
    E();
    if(inp_ptr==strlen(inp)){
        printf("Parsing successful\n");
    }
    else{
        printf("Failed\n");
    }
}