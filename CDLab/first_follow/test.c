#include<stdio.h>
#include<stdlib.h>
#include<ctype.h>
#include<string.h>

void first(char c);
void follow(char c);
char a[50][50],f[10];
int m = 0,n;
void main(){
    int ch=1,i;
    char c,cha;
    printf("Enter the number of productions\n");
    scanf("%d",&n);
    printf("Enter the productions\n");
    for(i=0;i<n;i++){
        scanf("%s%c", a[i], &cha);
    }
    do{
        m=0;
        printf("Enter the element whose first & follow is to be found\n");
        scanf("%c", &c);
        first(c);
        printf("First of %c {",c);
        for(i=0;i<m;i++){
            printf("%c",f[i]);
        }
        printf("}\n");
        strcpy(f, " ");
        m=0;
        follow(c);
        printf("Follow of %c {",c);
        for(i=0;i<m;i++){
            printf("%c",f[i]);
        }
        printf("}\n");
        printf("Do you want to continue(0/1)?\n");
        scanf("%d%c",&ch,&cha);
    }while(ch!=0);
}

void first(char c){
    if(!isupper(c)){
        f[m++]=c;
    }
    for(int i=0;i<n;i++){
        if(a[i][0]==c){
            if(a[i][2]=='$'){
                follow(a[i][0]);
            }
            else if(islower(a[i][2])){
                f[m++]=a[i][2];
            }
            else{
                first(a[i][2]);
            }
        }
    }
}

void follow(char c){
    int k = 0,i = 0;
    if(c==a[0][0]){
        f[m++]='$';
    }
    for(i=0;i<n;i++){
        for(k=2;k<strlen(a[i]);k++){
            if(a[i][k]==c){
                if(a[i][k+1]!='\0'){
                    first(a[i][k+1]);
                }
                else if(a[i][k+1]=='\0' && a[i][0]!=c){
                    follow(a[i][0]);
                }
            }
        }
    }
}