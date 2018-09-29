#include <bits/stdc++.h>
using namespace std;
int main()
{
    int i,n,m;
    while(true)
    {
        cin>>n;
        if(n==0)
        {
            break;
        }
    while(true)
        {
        i=0;
        while(n!=0)
            {
            m=n%10;
            n=n/10;
            i=i+m;
            }

        n=i;
        if(i<10)
            {
                cout<<n<<endl;
                break;
            }
        }

    }
}
