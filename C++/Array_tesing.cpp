#include<bits/stdc++.h>
using namespace std;

int main()
{
    int i,j,k,ln;
    int Arr[] = {1,4,3,2,6,5};
    ln = sizeof(Arr)/sizeof(int);

    for(i=0; i<ln; i++)
    {
        for(j=0; j<ln; j++)
        {   if(Arr[j] > Arr[j+2])
            {
                k = Arr[j+2];
                cout<<"k"<<endl;
                Arr[j+2] = Arr[j];
                Arr[j] = k;
            }

            for(j=0; j<ln; j++)
            {
                cout<<Arr[j]<<", ";
            }
            cout<<endl;
        }

    }
}
