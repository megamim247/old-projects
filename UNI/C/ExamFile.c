//==========================Question 1================================ 
#include <stdio.h>

#define MAX_SIZE 100

int main(void)
{
	int a[MAX_SIZE];
	int size, i, k, count;
    float mean;
    mean=0;
    count=0;
	
	/* read the array size */ 
	printf("Enter the array size:\n");
	scanf("%d", &size);
	
	/* read array values */
	printf("Enter %d integer values:\n", size);
	for (i = 0; i < size; i++)
	{
		scanf("%d", &a[i]);
	}

	/* read the value for k */
	printf("Enter the value for k:\n");
	scanf("%d", &k);
    

	/** Write your code here **/	
	for (i = 0; i < size; i++)
	{
		if(a[i]%k==0){
		    count++;
		    mean+=a[i];
		}
	}
	if (count!=0){
        mean=mean/count;
	} else{
	    mean=0;
	}
    printf("The mean is: %.1f",mean);
	return 0;
}

//===============================Question 2=================================
#include <stdio.h>

#define MAX_SIZE 100

void find_occurrences(int arr[], int size, int value, int *first, int *last);

int main(void)
{
	int a[MAX_SIZE];
	int size, i, v;
	int first_index=-1, last_index=-1;
	
	/* read the target value */
	printf("Enter the target value:\n");
	scanf("%d", &v);

	/* read the array size */ 
	printf("Enter the array size:\n");
	scanf("%d", &size);
	
	/* read array values */
	printf("Enter %d integer values:\n", size);
	for (i = 0; i < size; i++)
	{
		scanf("%d", &a[i]);
	}


	/** Write your code here **/
	find_occurrences(a,size,v,&first_index,&last_index);
	
	/* write out the result */
	printf("The array is: ");
	for (i = 0; i < size; i++)
	{
		printf("%d ", a[i]);
	}
	printf("\n");

	printf("The first index is: %d\n", first_index);
	printf("The last index is: %d\n", last_index);

	return 0;
}

void find_occurrences(int arr[], int size, int value, int *first, int *last)
{
	/** Write your code here **/
	for (int i = 0; i < size; i++)
	{
        if(arr[i]==value){
            if(*first==-1){
                *first=i;
            }
            *last=i;
        }
	}
}

//===============================Question 3====================================
#include <stdio.h>
#define MAX_LEN 100

void remove_duplicate_lowercase(char s[]);

int main(void)
{
	char str[MAX_LEN];

	/* read the string using fgets - at most MAX_LEN - 1 
	   characters will be read; the null terminator is 
	   added to the end of the string */
	printf("Enter a string:\n");
	fgets(str, MAX_LEN, stdin);


    /** Write your code here **/
    remove_duplicate_lowercase(str);
    

	/* display output */
	printf("The modified string is: %s\n", str);
	
	return 0;
}

void remove_duplicate_lowercase(char s[])
{
	/** Write your code here **/
    char chars[26]={0};
    int count=0;
    int count2;
    while (s[count]!=0){
        if (s[count]>='a' && s[count]<='z'){
            chars[s[count]-'a']++;
            while (chars[s[count]-'a']>1){
                count2=count;
                while (s[count2+1]!=0){
                    s[count2]=s[count2+1];
                    count2++;
                }
                chars[s[count]-'a']++;
            }
        }
        count++;
    }
    return;
}
//===========================Question 4===========================
#include <stdio.h>
#define MAX_LEN 100

int count_words(char filename[], int *total_count);

int main (void)
{
	char filename[MAX_LEN];
	int count;

	/* read the filename */
	printf("Enter the filename:\n");
	scanf("%s", filename);

	/* display output */
	if (count_words(filename, &count))
	{
		printf("The total number of words is: %d\n", count);
	}
	else
	{
		printf("Error opening file\n");
	}

	return 0;
}

int count_words(char filename[], int *total_count)
{
	/** Write your code here **/
	FILE *fp;
	char line[MAX_LEN];
	int count,curcount;
	int i;
	fp=fopen(filename,"r");
	if ( fp == NULL )
    {
        return 0;
    }
    while (fgets(line,MAX_LEN,fp) !=NULL)
    {
        count=0;
        i=0;
        curcount=0;
        while(line[i]==' '){
            i++;
        }
        while(line[i]!=0){
            if (line[i]==' ' || line[i]=='\t' || line[i]=='\n' || line[i]==',' || line[i]=='.' || line[i]=='!' || line[i]=='?'){
                curcount++;
            }else{
                if (curcount>0){
                    count++;
                    curcount=0;
                }
            }
            i++;
        }
        
        *total_count+=count+1; //+1 to account for end of line
    }
    fclose(fp);
    return 1;
}
