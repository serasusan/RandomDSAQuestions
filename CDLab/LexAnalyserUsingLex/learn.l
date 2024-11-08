%{
    int COMMENT = 0;
    int cnt = 0;
%}
identifier [a-zA-Z][a-zA-Z0-9]*
%%
#.* {printf("\n%s is a preprocessor directive\n",yytext);}
float | int | double | char | switch | void | while | if | do | 
case | else | const | struct | typedef {printf("%s is a keyword\n", yytext);}
"/*" {COMMENT=1;}
"*/" {COMMENT=0;}
\{ {if(!COMMENT) printf("Block begins\n");}
\} {if(!COMMENT) printf("Block ends\n");}
[0-9]+ {if(!COMMENT) printf("%s is a number\n",yytext);}
{identifier}\( {if(!COMMENT) printf("\n FUNCTION %s\n",yytext);}
\)(\;)? { if(!COMMENT) ECHO; printf("\n"); }
{identifier}(\[[0-9]*\])? {if(!COMMENT) printf("\n identifier %s\n",yytext);}
= {if(!COMMENT) printf("%s is an assignment operator\n", yytext);}
\> | \< | \>= | \<= {if(!COMMENT) printf("%s is a relational operator",yytext);}
\+|\-|\*|\\ {if(!COMMENT) printf("\n%s is an operator",yytext);}
%%
int main(){
    yyin = fopen("input.c","r");
    yylex();
    fclose(yyin);
    printf("Total number of comments : %d\n",cnt);
    return 0;
}
int yywrap(){
    return 1;
}
