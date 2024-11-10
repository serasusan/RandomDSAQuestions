#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int n,z,i,j;
char act[30],a[30],stk[30];
void check();


void main(){
    printf("This is the grammar\nE->E+E\nE->E*E\nE->(E)\nE->id\n");
    printf("Enter the expression\n");
    scanf("%s",a);
    n = strlen(a);
    for(i=0,j=0;j<n;i++,j++){
    strcpy(act,"Shift->");
        // j,a -> input i,stk -> stack
        if(a[j]=='i' && a[j+1]=='d'){
            stk[i]=a[j];
            stk[i+1]=a[j+1];
            stk[i+2]='\0';
            a[j]=' ';
            a[j+1]=' ';
            printf("%s\t%s\t%sid\n",stk,a,act);
            check();
        }
        else{
            stk[i]=a[j];
            stk[i+1]='\0';
            a[j]=' ';
            printf("%s\t%s\t%ssymbols\n",stk,a,act);
            check();
        }
    }
    
}
void check(){
        strcpy(act,"Reduce to E\n");
        for(z=0;z<n;z++){
            if(stk[z]=='i' && stk[z+1]=='d'){
                stk[z]='E';
                stk[z+1]='\0';
                printf("%s\t%s\t%s",stk,a,act);
                j++;
            }
        }
        
        for(z=0;z<n;z++){
            if(stk[z]=='E' && stk[z+1]=='+' && stk[z+2]=='E'){
                stk[z]='E';
                stk[z+1]='\0';
                stk[z+2]='\0';
                printf("%s\t%s\t%s\n",stk,a,act);
                i-=2;
            }
        }

        for(z=0;z<n;z++){
            if(stk[z]=='E' && stk[z+1]=='*' && stk[z+2]=='E'){
                stk[z]='E';
                stk[z+1]='\0';
                stk[z+2]='\0';
                printf("%s\t%s\t%s\n",stk,a,act);
                i-=2;
            }
        }
        for(z=0;z<n;z++){
            if(stk[z]=='(' && stk[z+1]=='E' && stk[z+2]==')'){
                stk[z]='E';
                stk[z+1]='\0';
                stk[z+2]='\0';
                printf("%s\t%s\t%s\n",stk,a,act);
                i-=2;
            }
        }
        
    }