#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){

    char *a2 = (char*)malloc(60*sizeof(char));
    strcpy(a2,"hello worldlll\n");
     char tmp, tmp2;
     int i = 0, j = 0;

     while(a2[i]!='\0'){
        
        if(a2[i]=='l'){
            tmp = a2[i+1];
            a2[i] = 'a';
            a2[i+1] = 'b';
            a2[i+2] = 'c';
            j = i+1;
            while(a2[j]!='\0'){
                tmp2 = a2[j+1];
                a2[j+1] = tmp;
                tmp = tmp2;
                j++;
            }
            //printf("%c\n", a2[i]);
            i++;
            i++;
            
        }
        //printf("%c\n", a2[i]);
         i++;
     }

    printf("%s\n", a2);


    return 0;
}