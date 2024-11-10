%{
    #include<stdio.h>
    #include<stdlib.h>
%}
%token NUMBER ID NL
%left '+' '-'
%left '*' '/'
%%
valid : E NL {printf("Valid Expression\n");}
E : E '+' E
    | E '*' E
    | E '-' E
    | E '/' E
    | NUMBER
    | ID
    | '(' E ')';
%%

int main(){
    printf("Enter the Expression\n");
    yyparse();
}

int yyerror()
{
    printf("Some error occured\n");
    exit(1);
}