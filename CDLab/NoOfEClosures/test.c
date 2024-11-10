#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int n;

void closure(int state,int m[][n]){
    for(int i=0;i<n;i++){
        if(m[state][i]==1){
            printf(",q%d",i);
            closure(i,m);
        }
    }
}

void main(){
    int s1,s2;
    char state1[3],state2[3],input[3];
    FILE *INPUT = fopen("input.txt","r");
    printf("Enter the number of states\n");
    scanf("%d",&n);
    int m[n][n];
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            m[i][j]=0;
        }
    }
    while(fscanf(INPUT,"%s %s %s",state1,input,state2)!=EOF){
        if(strcmp(input,"e")==0){
            s1 = state1[1] - '0';
            s2 = state2[1] - '0';
            m[s1][s2]=1;
        }
    }

    fclose(INPUT);
    printf("Epsilon Closures\n");
    for(int i=0;i<n;i++){
        printf("\nq%d: q%d",i,i);
        closure(i,m);
        printf("\n");
    }

}