#include "stdio.h"
#include "string.h"
#include "stdlib.h"

char Exp[15], ip = 0, Output[50];

void E_Prime();
void E();
void T_Prime();
void T();
void F();

void E()
{
    int temp = 0, length = strlen(Output);
    for (temp = 0; temp < length && Output[temp] != 'E'; temp++);
    for (int i = length; i > temp; i--)
        Output[i + 2] = Output[i];
    Output[temp] = 'T';
    Output[temp + 1] = 'E';
    Output[temp + 2] = 39;
    printf("E=%-25s", Output);
    printf("E -> TE'\n");
    T();
    E_Prime();
}

void E_Prime()
{
    int temp = 0, length = strlen(Output);
    for (temp = 0; temp < length && Output[temp] != 'E'; temp++)
        ;
    if (Exp[ip] == '+')
    {
        for (int i = length; i > temp; i--)
            Output[i + 2] = Output[i];
        Output[temp++] = '+';
        Output[temp++] = 'T';
        Output[temp++] = 'E';
        Output[temp++] = 39;
        printf("E=%-25s", Output);
        printf("E' -> +TE'\n");
        ip++;
        T();
        E_Prime();
    }
    else
    {
        for (int i = temp; i < strlen(Output); i++)
            Output[i] = Output[i + 2];
        printf("E=%-25s", Output);
        printf("E' -> e\n");
    }
}

void T()
{
    int temp = 0, length = strlen(Output);
    for (temp = 0; temp < length && Output[temp] != 'T'; temp++);
    for (int i = length; i > temp; i--)
        Output[i + 2] = Output[i];
    Output[temp++] = 'F';
    Output[temp++] = 'T';
    Output[temp] = 39;
    printf("E=%-25sT -> FT'\n", Output);
    F();
    T_Prime();
}

void T_Prime()
{
    int temp = 0, length = strlen(Output);
    for (temp = 0; temp < length && Output[temp] != 'T'; temp++);
    if (Exp[ip] == '*')
    {
        for (int i = length; i > temp; i--)
            Output[i + 3] = Output[i];
        Output[temp++] = '*';
        Output[temp++] = 'F';
        Output[temp++] = 'T';
        Output[temp] = 39;
        printf("E=%-25s", Output);
        printf("T' -> *FT'\n");
        ip++;
        F();
        T_Prime();
    }
    else
    {
        for (int i = temp; i < strlen(Output); i++)
            Output[i] = Output[i + 2];
        printf("E=%-25s", Output);
        printf("T' -> e\n");
    }
}

void F()
{
    int temp = 0;
    for (temp = 0; temp < strlen(Output) && Output[temp] != 'F'; temp++)
        ;
    if (Exp[ip] == 'i')
    {
        Output[temp] = 'i';
        printf("E=%-25s", Output);
        printf("F -> i\n");
        ip++;
    }
    else if (Exp[ip] == '(')
    {
        ip++;
        for (int i = strlen(Output); i > temp; i--)
            Output[i + 2] = Output[i];
        Output[temp] = '(';
        Output[temp + 1] = 'E';
        Output[temp + 2] = ')';
        printf("E=%-25s", Output);
        printf("F -> (E)\n");
        E();
        if (Exp[ip] == ')')
            ip++;
        else
        {
            printf("Parsing Failed");
            exit(1);
        }
    }
    else
    {
        printf("Parsing Failed");
        exit(1);
    }
}

void main()
{
    printf("Grammar:");
    printf("\nE -> TE' \nE' -> +TE' | e \nT -> FT' \nT' -> *FT' | e \nF -> (E) | i");
    printf("\nEnter the input expression: ");
    scanf("%s", Exp);
    printf("Expressions");
    printf("\tSequence of production rules\n");
    E();
    if (ip == strlen(Exp))
        printf("Parsing Successful");
    else
        printf("Parsing Failed");
}