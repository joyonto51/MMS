#include<stdio.h>
int main()
{
int a,d;
float b,c,e;
printf("Enter the value of a:");
scanf("%d",&a);
d=a/2;
printf("the result is:%d\n",d);
c=(float)a;
b=c/2;
printf("the result is:%f\n",b);
e=b-d;
printf("the result is:%f\n",e);
if(e==0)
{
    printf("The number is Even");
}
else
{
    printf("The number is Odd");
}
}
