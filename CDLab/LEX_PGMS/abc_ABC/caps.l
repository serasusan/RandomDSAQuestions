%{
    #include<stdio.h>
%}
%%
[\n] {printf("\n");return 0;}
"abc" {printf("ABC");}
. printf("%s",yytext);
%%
int yywrap(){
    return 1;
}
int main(){
    printf("Enter string\n");
    yylex();
    return 0;
}
