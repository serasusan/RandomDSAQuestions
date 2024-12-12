#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int n; 

void closure(int k,int mat[][n]){
    for(int i=0;i<n;i++){
        if(mat[k][i]==1){
            printf(",q%d",i);
            closure(i,mat);
        }
    }
}

void main(){
    int s1,s2;
    char st1[5],st2[5],input[5];
    printf("Enter the number of states\n");
    scanf("%d",&n);
    int mat[n][n];
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            mat[i][j]=0;
        }
    }

    FILE *INPUT = fopen("input.txt","r");
    while(fscanf(INPUT,"%s %s %s",st1, input, st2)!=EOF){
        if(strcmp(input,"e")==0){
        // if(input=="e"){
            s1 = st1[1]-'0';
            s2 = st2[1]-'0';
            mat[s1][s2] = 1;   
        }
    }

    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            printf("%d", mat[i][j]);
        }
        printf("\n");
    }

    printf("Epsilon Closures\n");
    for(int k=0;k<n;k++){
        printf("q%d : q%d",k,k);
        closure(k,mat);
        printf("\n");
    }
}