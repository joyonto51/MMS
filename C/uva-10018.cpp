#include <bits/stdc++.h>
using namespace std;

long int reverse_num( long int n)
{
    long int m=0;
    while(true)
    {
        m += n%10;
        n = n/10;
        if(n==0)
        {
            break;
        }
        m = m * 10;
    }
    return m;
}


int main()
{
    int T,i;
    cin>>T;
    for(i=0;i<T;i++)
    {
        long int n,m,x=0;
        cin>>n;
        while(true)
        {
            m=reverse_num(n);
            if (x>=1 && n==m)
            {
                break;
            }
            else
            {
                n = n + m;
                x += 1;
            }

        }
        cout<<x<<" "<<n<<endl;
    }
    return 0;
}
