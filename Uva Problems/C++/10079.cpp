#include<bits/stdc++.h>
using namespace std;

int main()
{
    int n,i;
    long int k;
    while(true)
    {
        k=0;
        scanf("%ld", &n);
        if (n<0)
        {
            break;
        }
        else
        {
            for(i=0;i<=n;i++)
            {
                k = k+i;
            }
            k+=1;
            printf("%ld\n",k);
        }

    }
    return 0;
}
