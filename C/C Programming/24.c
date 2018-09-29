#include<stdio.h>
int main()
{
float num1,num2;
printf("Enter a number:");
scanf("%f",&num1);
printf("Enter the another number:");
scanf("%f",&num2);
printf("%f+%f=%o.2f/n",num1,num2,num1+num2);
printf("%f-%f=%0.2f/n",num1,num2,num1-num2);
printf("%f*%f=%0.2f/n",num1,num2,num1*num2);
printf("%f/%f=%0.3f/n",num1,num2,num1/num2);
return 0;
}
