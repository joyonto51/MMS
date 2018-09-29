#include <bits/stdc++.h>
using namespace std;

int main()
{
    int x,y,A[100];
    cin>>y;
    for(x=1;x<=y;x++)
    {
     cin>>A[x];
    }

    int i,j,key;
    for(j=1;j<y;j++)
    {
        key = A[j];
        i = j-1;
        while(i>0 && A[i]>key)
        {
            A[i+1] = A[i];
            i = i-1;
        }
        A[i+1] = key;
    }


    int m;
    for(m=1;m<y;m++)
    {
        cout<< A[m]<<" ";
    }

}
