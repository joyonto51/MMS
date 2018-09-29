#include<stdio.h>
int main()
{
char ch;
printf("Please Enter the letter:");
scanf("%c",&ch);
if(ch=='a'|| ch=='e'||ch=='i'||ch=='o'||ch=='u')
{
printf("The letter is Vowel\n");
}
else{
printf("The letter is Consonant\n");
}
return 0;

}
