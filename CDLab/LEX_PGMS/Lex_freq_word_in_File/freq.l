%{
    #include<stdio.h>
    #include<string.h>
    int cnt = 0;
    char word[30];
%}

%%
[a-zA-Z]+ {if(strcmp(word,yytext)==0) {cnt+=1;}}
[\n] {}
. {}
%%

int main(){
    FILE *file = fopen("input.txt","r");
    yyin = file;
    printf("Enter the word\n");
    scanf("%s",word);
    yylex();
    printf("Count :%d\n",cnt);
}

int yywrap(){
    return 1;
}