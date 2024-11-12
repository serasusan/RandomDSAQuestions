%{
    int lines_count=1;
    int words_count=0;
    int chars_count=1;
%}
%%
[\n] { lines_count++;chars_count+=yyleng;}
[\t ] { chars_count+=yyleng;}
[^\t\n ]+ {words_count+=1; chars_count+=yyleng;}
%%
int yywrap(){
    return 1;
}
int main(){
    FILE *file;
    file = fopen("input.txt","r");
    if(!file){
        printf("File error\n");
        return 1;
    }
    yyin = file;
    yylex();
    printf("\n");
    printf("Lines: %d\n",lines_count);
    printf("Words: %d\n",words_count);
    printf("Characters: %d\n",chars_count);
    return 0;
}
