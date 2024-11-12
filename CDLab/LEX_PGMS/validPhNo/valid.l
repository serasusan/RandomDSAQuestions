%{
#include <stdio.h>
%}

DIGIT       [0-9]
MOBILE      [6-9]{1}{DIGIT}{9}

%%
{MOBILE}    { printf("Valid Mobile Number\n"); }
.           { printf("Invalid Mobile Number\n");}
\n          { exit(1);}
%%

int main()
{
    printf("Enter the mobile number\n");
    
    yylex();
    return 0;
}

int yywrap(){
    return 1;
}