%{
    int vowel_count = 0;
    int consonant_count = 0;
%}
%%
[aeiouAEIOU] {vowel_count++;printf("%s",yytext);}
[a-zA-Z] {consonant_count++;printf("%s",yytext);}
[\n] {printf("\n");return 0;}
%%
int main(){
    printf("Enter the string:");
    yylex();
    printf("vowel_count: %d\n",vowel_count);
    printf("consonant_count : %d\n",consonant_count);
    return 0;
}