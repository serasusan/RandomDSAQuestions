#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<stdbool.h> //don't forget this

bool isDelimiter(char ch){
    if(ch == ' ' || ch == '+' || ch == '*' || ch == '/' || ch == ',' ||
       ch == ';' || ch == '[' || ch == ']' || ch == '{' || ch == '}' ||
       ch == '(' || ch == ')' || ch == '=' || ch == '<' || ch == '>')
       {
        return true;
       }
    return false;
}

bool isOperator(char ch){
    if(ch == '+' || ch == '-' || ch == '*' || ch == '/' || ch == '=' ||
       ch == '>' || ch == '<')
    {
        return true;
    }
    return false;
}

bool isValidIdentifier(char *str){
    if(str[0]=='0' || str[0]=='1' || str[0]=='2' || str[0]=='3' || str[0]=='4' ||
       str[0]=='5' || str[0]=='6' || str[0]=='7' || str[0]=='8' || str[0]=='9')
    {
        return false;
    }
    return true;
}

bool isKeyword(char *str){
    if(!strcmp(str,"if") || !strcmp(str,"else")
    || !strcmp(str,"do") || !strcmp(str,"while")
    || !strcmp(str,"int") || !strcmp(str,"float")
    || !strcmp(str,"double") || !strcmp(str,"short")
    || !strcmp(str,"switch") || !strcmp(str,"char")
    || !strcmp(str,"return") || !strcmp(str,"void") 
    || !strcmp(str,"struct") || !strcmp(str,"static")
    || !strcmp(str,"goto") || !strcmp(str,"typedef"))
    {
        return true;
    }
    return false;
}

bool isInteger(char *str){
    int len = strlen(str);
    if(len == 0){
        return false;
    }
    for(int i=0;i<len;i++){
        if(str[i]!='0' && str[i]!='1' && str[i]!='2' && str[i]!='3' && str[i]!='4'
        && str[i]!='5' && str[i]!='6' && str[i]!='7' && str[i]!='8' && str[i]!='9')
        {
            return false;
        }
    }
    return true;
}

bool isRealNumber(char *str){
    int len = strlen(str);
    bool hasDecimal = false;

    if(len==0){
        return false;
    }

    for(int i=0;i<len;i++){
        if(str[i]!='0' && str[i]!='1' && str[i]!='2' && str[i]!='3' && str[i]!='4'
        && str[i]!='5' && str[i]!='6' && str[i]!='7' && str[i]!='8' && str[i]!='9'
        && str[i]!='.' || (str[i]=='-' && i>0)){
            return false;
        }
        if(str[i]=='.'){
            if(hasDecimal){
                return false;
            }
            hasDecimal = true;
        }
    }
    return hasDecimal;
}

char *substring(char *str,int left, int right){
    char * substr = (char *)malloc(sizeof(char)*(right-left+2));
    for(int i=left;i<=right;i++){
        substr[i-left] = str[i];
    }
    substr[right-left+1]='\0';
    return substr;
}

void parse(char *str){
    int left = 0, right = 0;
    int len = strlen(str);
    while(right<=len && left<=right){
        if(isDelimiter(str[right])==false){
            right+=1;
        }
        if(isDelimiter(str[right])==true && (left==right)){
            if(isOperator(str[right])==true){
                printf("%c is an operator\n",str[right]);
            }
            right++;
            left=right;
        }
        if((isDelimiter(str[right])==true && (left!=right)) || ((right==len) && left!=right)){
            char *substr = substring(str,left,right-1);
            if(isKeyword(substr)==true){
                printf("%s is a keyword\n",substr);
            }
            else if(isInteger(substr)==true){
                printf("%s is an integer\n",substr);
            }
            else if(isRealNumber(substr)==true){
                printf("%s is a real number\n",substr);
            }
            else if(isValidIdentifier(substr)==true && isDelimiter(substr[right-1])==false){
                printf("%s is a valid identifier\n",substr);
            }
            else if(isValidIdentifier(substr)==false && isDelimiter(substr[right-1])==false){
                printf("%s is not a valid identifier\n",substr);
            }
            left=right;
        }
    }
}
int main(){
    char input[100];
    printf("Enter the string\n");
    scanf("%[^\n]",input);
    printf("After parsing\n");
    parse(input);
}