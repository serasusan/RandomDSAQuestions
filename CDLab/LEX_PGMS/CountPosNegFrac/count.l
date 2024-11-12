%{
    #include<stdio.h>
    int cp=0,cn=0,cf=0;
%}

%%
[+][0-9]+ {cp+=1;}
[-][0-9]+ {cn+=1;}
[0-9]+[/][1-9][0-9]* {cf+=1;}
[\n] {return 0;}
%%

int main(){
    printf("Enter the numbers\n");
    yylex();
    printf("Positives : %d, Negatives : %d, Fractions : %d\n",cp,cn,cf);
}

int yywrap(){
    return 1;
}