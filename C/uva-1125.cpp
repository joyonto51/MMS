#include<bits/stdc++.h>
using namespace std;
int main()
{
    int T,x;
    cin>>T;
    for(x=0;x<T;x++)
    {
        int N,k,n,m,a=0,b=0,c=0,d=0,e=0,f=0,g=0,h=0,i=0,j=0;
        cin>>N;
        for(k=1;k<=N;k++)
        {
            n=k;
            while(n!=0)
            {
                m=n%10;
                n=n/10;
                if(m==0)
                {
                    a=a+1;
                }
                else if(m==1)
                {
                    b=b+1;
                }
                 else if(m==2)
                {
                    c=c+1;
                }
                 else if(m==3)
                {
                    d=d+1;
                }
                 else if(m==4)
                {
                    e=e+1;
                }
                 else if(m==5)
                {
                    f=f+1;
                }
                 else if(m==6)
                {
                    g=g+1;
                }
                 else if(m==7)
                {
                    h=h+1;
                }
                 else if(m==8)
                {
                    i=i+1;
                }
                 else
                {
                    j=j+1;
                }
            }
        }

        cout<<a<<" "<<b<<" "<<c<<" "<<d<<" "<<e<<" "<<f<<" "<<g<<" "<<h<<" "<<i<<" "<<j<<endl;
    }
    return 0;
}

