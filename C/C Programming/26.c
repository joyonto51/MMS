#include<stdio.h>
int main()
{
int num1,num2,megh;
char mg;
printf("Enter a number:");
scanf("%d",&num1);
printf("Enter another number:");
scanf("%d",&num2);
megh=num1+num2;
mg='+';
printf("%d %c %d=%d\n",num1,mg,num2,megh);
megh=num1-num2;
mg='-';
printf("%d %c %d=%d\n",num1,mg,num2,megh);
megh=num1*num2;
mg='*';
printf("%d %c %d=%d\n",num1,mg,num2,megh);
megh=num1/num2;
mg='/';
printf("%d %c %d=%d\n",num1,mg,num2,megh);
return 0;
}
