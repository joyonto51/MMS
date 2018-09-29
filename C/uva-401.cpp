#include <bits/stdc++.h>
using namespace std;

int main()
{
    int c_ln,i;
    string A,c;
    c = "AHIMTOUVWXY018";
    c_ln = c.length();
    while(cin>>A)
    {
        string D,b;
        int ln,n=0,N1=0,N2=0;
        b = A;
        reverse(b.begin(),b.end());
        if(A==b){
            N1 = 1;
        }
        D = A;
        ln = A.length();
        for(i=0;i<ln;i++)
        {
            if (D[i]=='L')
            {
                D[i]='J';
                n += 1;
            }
            else if(D[i]=='J')
            {
                D[i] = 'L';
                n += 1;
            }
            else if(D[i]=='2')
            {
                D[i] = 'S';
                n += 1;
            }
            else if(D[i]=='S')
            {
                D[i] = '2';
                n += 1;
            }
            else if(D[i]=='5')
            {
                D[i] = 'Z';
                n += 1;
            }
            else if(D[i]=='Z')
            {
                D[i] = '5';
                n += 1;
            }
            else if(D[i]=='3')
            {
                D[i] = 'E';
                n += 1;
            }
            else if(D[i]=='E')
            {
                D[i] = '3';
                n += 1;
            }
        }
        reverse(D.begin(),D.end());
        for(i=0;i<ln;i++)
        {
            for(int j=0;j<c_ln;j++)
            {
                if(D[i]==c[j])
                {
                    n+=1;
                    break;
                }
            }
        }
        if (D==A && ln==n)
        {
            N2 = 1;
        }

        if(N1==1 && N2==1)
        {
            cout<<A<<" -- is a mirrored palindrome.\n"<<endl;
        }
        else if(N1==1 && N2!=1)
        {
            cout<<A<<" -- is a regular palindrome.\n"<<endl;
        }
        else if(N1!=1 && N2==1)
        {
            cout<<A<<" -- is a mirrored string.\n"<<endl;
        }
        else
        {
            cout<<A<<" -- is not a palindrome.\n"<<endl;
        }
    }

return 0;
}
