//  Intermediate code generator + Backend


#include<stdio.h>
#include<stdlib.h>
#include<string.h>

char icode[30][30];
int k=0;

void gen_intermediate_code(char *inp,char opr,char *reg){
    int i =0,j=0;
    char temp[30];
    while(inp[i]!='\0'){
        if(inp[i]==opr){
            temp[j-1]=*reg;
            printf("%c\t%c\t%c\t%c\n",opr,*reg,inp[i-1],inp[i+1]);
            icode[k][0]=opr;
            icode[k][1]=*reg;
            icode[k][2]=inp[i-1];
            icode[k][3]=inp[i+1];
            k+=1;
            i+=2;
            (*reg)--;
            continue;
        }
        temp[j]=inp[i];
        i++;
        j++;
    }
    temp[j++]='\0';
    strcpy(inp,temp);
}
void gen(char *inp){
    char reg = 'Z';
    gen_intermediate_code(inp,'/',&reg);
    gen_intermediate_code(inp,'*',&reg);
    gen_intermediate_code(inp,'+',&reg);
    gen_intermediate_code(inp,'-',&reg);
    icode[k][0]='\0';
}

void main(){
    char input[30],str[30],opr[30];
    int i=0;
    printf("Enter the input :\n");
    scanf("%s", input);
    gen(input);
    printf("ICODE : \n");
    for(int i=0;i<=k;i++){
        printf("%s\n",icode[i]);
    }
    i =0;
    printf("Target code \n");
	do{
		strcpy(str, icode[i]);
		switch(str[0]){
			case '+':
				strcpy(opr,"ADD");
				break;
			case '-':
				strcpy(opr,"SUB");
				break;
			case '*':
				strcpy(opr,"MUL");
				break;
			case '/':
				strcpy(opr,"DIV");
				break;
		}
		printf("MOV %c,R%d\n",str[2],i );

		printf("%s %c,R%d\n",opr,str[3],i );

		printf("MOV R%d,%c\n",i,str[1] );

	}while(icode[i++][0]!='\0');
	printf("\n");
}