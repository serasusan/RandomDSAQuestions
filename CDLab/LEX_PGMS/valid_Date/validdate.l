%{
    #include <stdio.h>
    #include <string.h>
    int valid = 0, yr = 0;
    char date[20];
%}

%%
([0][1-9]|[1-2][0-9]|[3][0-1])\/(01|03|05|07|08|10|12)\/([1-2][0-9][0-9][0-9]) { valid = 1; }
([0][1-9]|[1-2][0-9]|30)\/(04|06|09|11)\/([1-2][0-9][0-9][0-9]) { valid = 1; }
([0][1-9]|[1][0-9]|2[0-8])\/02\/([1-2][0-9][0-9][0-9]) { valid = 1; }
([0][1-9]|1[0-9]|2[0-9])\/02\/([1-2][0-9][0-9][0-9]) {
    yr = 0;
    for (int i = 6; i < yyleng; i++) {
        yr = yr * 10 + (yytext[i] - '0');
    }
    if (yr % 400 == 0 || (yr % 4 == 0 && yr % 100 != 0)) {
        valid = 1;
    }
}
%%

int main() {
    printf("Enter the date (DD/MM/YYYY): ");
    scanf("%s", date);

    yy_scan_string(date);
    yylex();


    if (valid == 0) {
        printf("Invalid\n");
    } else {
        printf("Valid\n");
    }

    return 0;
}

int yywrap() {
    return 1;
}
