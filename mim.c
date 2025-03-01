#include <stdio.h>
int main(void) {
    int a;
    float b;
    scanf("%d,%f",&a,&b);
    if (a) {
        printf("%d",a);
        printf("%f",b);
    } else {
        printf("%f",b);
    }
    return 0;
}