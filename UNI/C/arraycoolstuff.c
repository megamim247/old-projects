#include <stdio.h>
#include <string.h>
int main(void){
    int i,original,count;
    char out[7];
    printf("Enter a calue for n:\n");
    scanf("%d",&i);
    original=i;
    if(i>=0){
        count=0;
        while (i!=0){
            if (i%2==1){
                out[count]='1';
            } else {
                out[count]='0'; 
            }
            count++;
            i=i/2;
        }
        printf("%d in base 2 is ",original);
        for(int n=count-1;n>=0;n--){
            printf("%c",out[n]);
        }
    }else{
        printf("invalid input");
    };
}