#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int hello(char **pc){

	*pc = (char *) malloc(11*sizeof(char));
	
	strcpy(*pc, "hello world\n");

	return 0;

}
int main(){
	char *pc=NULL;
	int i;
	i = hello(&pc);
	printf("%s\n",pc);
	//if(!hello(pc)) printf("day la chuoi pc: ");
	//for(i = 0;i<11;i++) printf("%c",*(pc+i));
	return 0;
}

