%{
#include<stdlib.h>
#include <stdio.h>
int yyerror();
int yylex();
%}

%token DIGIT LETTER UND NL
%% 
valid : variable NL { printf("Valid Expression\n");exit(0);}
variable :  LETTER alphanumeric | UND alphanumeric;
alphanumeric : LETTER alphanumeric | DIGIT alphanumeric | UND alphanumeric | DIGIT | UND | LETTER;
%%
int main(){
    printf("Enter the Expression\n");
    yyparse();
}

int yyerror(){
    printf("\n INVALID Expression\n");
    exit(0);
}