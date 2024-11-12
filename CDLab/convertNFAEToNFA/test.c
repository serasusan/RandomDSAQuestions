#include<stdio.h>
#include<stdlib.h>

struct node {
    int st;
    struct node *link;
};

void insert_trantbl(int r, char c, int s);
int findalpha(char c);
void findclosure(int sta,int x);
void print_e_closure(int i);
void union_closure(int i);
void findfinalstates();

int noalpha,nostate,startstate,nofinal, finalstate[20],notransition,r,s,buffer[20],e_closure[20][20],set[20],m;
char alpha[20],c;
struct node *transition[20][20] = {NULL};

void main(){
    int i,j,k;
    printf("Enter the number of alphabets\n");
    scanf("%d",&noalpha);
    // getchar();

    printf("Enter the alphabets\n");
    for(i=0;i<noalpha;i++){
        scanf(" %c",&alpha[i]); // either scanf like this where the blank space/newline is also taken into account.
        // alpha[i] = getchar(); 
        // getchar(); // or do this to getchar newline characters also
    }
    printf("The alphabets are \n");
    for(int i=0;i<noalpha;i++){
        printf("%c",alpha[i]);
    }
    

    printf("\nEnter the number of states\n");
    scanf("%d",&nostate);

    printf("Enter the start state\n");
    scanf("%d",&startstate);

    printf("Enter the number of final states\n");
    scanf("%d",&nofinal);

    printf("Enter the final states\n");
    for(i=0;i<nofinal;i++){
        scanf("%d",&finalstate[i]);
    }

    printf("Enter the number of transitions\n");
    scanf("%d",&notransition);

    printf("Enter the transitions\n");
    for(i=0;i<notransition;i++){
        scanf("%d %c %d",&r,&c,&s);
        insert_trantbl(r,c,s);
    }

    printf("\n");
    
    for(i=1;i<=nostate;i++){
        c=0;
        for(j=0;j<20;j++){
            buffer[j]=0;
            e_closure[i][j]=0;
        }
        findclosure(i,i);
    }

    printf("Equivalent NFA without Epsilon\n");
    printf("------------------------------\n");
    printf("Start state :");
    print_e_closure(startstate);

    printf("\nAlphabets:");
    for(i=0;i<noalpha;i++){
        printf("%c ",alpha[i]);
    }

    printf("\nStates:");
    for(i=1;i<=nostate;i++){
        print_e_closure(i);
    }
    printf("\n");

    printf("Transitions are:\n");
    int t;
    struct node* temp;
    for(i=1;i<=nostate;i++){
        for(j=0;j<noalpha-1;j++){
            for(m=1;m<=nostate;m++)
                set[m]=0;

            for(k=0;e_closure[i][k]!=0;k++){
                t = e_closure[i][k];
                temp = transition[t][j];
                while(temp!=NULL){
                    union_closure(temp->st);
                    temp = temp->link;
                }
            }
        printf("\n");
        print_e_closure(i);
        printf("%c\t",alpha[j]);
        printf("{");
        for(int n=1;n<=nostate;n++){
            if(set[n]!=0)
                printf("q%d, ",n);
        }
        printf("}\n");
        }
    }

    printf("Final States: ");
    findfinalstates();
}



void insert_trantbl(int r, char c, int s){
    int j;
    j=findalpha(c);
    if(j==999){
        printf("No alphabet as %c",c);
        exit(0);
    }
    struct node * temp;
    temp = (struct node *)malloc(sizeof(struct node));
    temp->st = s;
    temp->link = transition[r][j];
    transition[r][j] = temp;
}


int findalpha(char c){
    for(int i=0;i<noalpha;i++){
        
        if(alpha[i]==c){
            return i;
        }
    }
    return 999;
}

void findclosure(int sta,int x){
    if(buffer[x])
        return;
    struct node *temp;
    e_closure[sta][c++]=x;
    if(alpha[noalpha-1]=='e' && transition[x][noalpha-1]!=NULL){
        temp = transition[x][noalpha-1];
        while(temp!=NULL){
            findclosure(sta,temp->st);
            temp = temp->link;
        }
    }
}

void print_e_closure(int i){
    printf("{");
    for(int j=0;e_closure[i][j]!=0;j++){
        printf("q%d, ",e_closure[i][j]);
    }
    printf("}");
}

void union_closure(int i){
    int j=0,k;
    while(e_closure[i][j]!=0){
        k = e_closure[i][j];
        set[k]=1;
        j++;
    }
}

void findfinalstates(){
    for(int i=0;i<nofinal;i++){
        for(int j=1;j<=nostate;j++){
            for(int k=0;e_closure[j][k]!=0;k++){
                if(e_closure[j][k]==finalstate[i]){
                    print_e_closure(j);
                }
            }
        }
    }
}