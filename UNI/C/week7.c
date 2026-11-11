#include <stdio.h>
#define MAX_RECORDS 1000

int main(void) {

    /* declare variables */
    FILE *fp;
    int target_city, target_day, temp_city, temp_day;
    float temp,sum,min,max,count,mean;
    min=1000;
    max=-1000;

    /* read the target city and and day */
    printf("Enter the target city code:\n");
    scanf("%d", &target_city);

    printf("Enter the target day number:\n");
    scanf("%d", &target_day);
    
    /* open file as an input file */
    fp = fopen("temps.txt", "r"); 
    if (fp == NULL)
    {
        printf("Error opening file\n");
        return -1; 
    }
    while (fscanf(fp,"%d %d %f",&temp_city ,&temp_day, &temp)==1){
        printf("%d %d %f",&temp_city ,&temp_day, &temp);
        if (temp_city==target_city && temp_day == target_day){
            count+=1;
            sum+=temp;
        }
    }
    mean=sum/count;
    printf("min = %f \n max = %f \n mean = %f \n count = %f",min,max,mean,count);

    /* close the file */
    fclose(fp);

    return 0;
}
