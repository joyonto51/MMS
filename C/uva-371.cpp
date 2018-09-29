#include <bits/stdc++.h>
using namespace std;
int main()
{
   while(true)
   {
    long int m,L,H;
    scanf("%d%d",&L,&H);
    if(H==0 && L==0)
    {
        break;
    }
    if(L>H)
    {
        m=H;
        H=L;
        L=m;
    }

    long int i,x,y;
    int Z,V=0,S=0;

    for(i=L;i<=H;i++)
    {
        x = i;
        y = i;
        Z = 0;
        while(true)
        {
            if(x%2==0)
            {
                x = x/2;
            }
            else
            {
                x = (3*x)+1;
            }
            Z = Z+1;
            if(x==1)
            {
                break;
            }

        }

        if(S<Z)
        {
            S = Z;
            V = y;
        }

    }

    cout<<"Between "<<L<<" and "<<H<<", "<<V<<" generates the longest sequence of "<<S<<" values."<<endl;

    }
}

