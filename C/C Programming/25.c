#include<stdio.h>
int main()
{
float num1,num2,megh;
char mg;
printf("Enter a number:");
scanf("%f",&num1);
printf("Enter another number:");
scanf("%f",&num2);
megh=num1+num2;
mg='+';
printf("%f %c %f=%0.2f\n",num1,mg,num2,megh);
megh=num1-num2;
mg='-';
printf("%f %c %f=%0.2f\n",num1,mg,num2,megh);
megh=num1*num2;
mg='*';
printf("%f %c %f=%0.2f\n",num1,mg,num2,megh);
megh=num1/num2;
mg='/';
printf("%f %c %f=%0.2f\n",num1,mg,num2,megh);
return 0;
}
