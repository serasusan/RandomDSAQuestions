%{
    #include<string.h>
    #include<stdio.h>
    int ispalindrome(char *str){
        for(int i=0;i<strlen(str)/2;i++){
            if(str[i]!=str[strlen(str)-i-1]){
                return 0;
            }
        }
        return 1;
    }
%}
%%
[a-zA-Z]+ {
    if(ispalindrome(yytext)){
        printf("%s is a palindrome\n",yytext);
    }
    else{
        printf("%s is not a palindrome\n",yytext);
    }
}
[\n] {return 0;}
. {}
%%
int main(){
    printf("Enter the string\n");
    yylex();
    return 0;
}

int yywrap(){
    return 1;
}