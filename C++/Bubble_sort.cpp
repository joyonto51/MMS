#include<bits/stdc++.h>
using namespace std;

int main()
{
    int Arr[] = {2,3,4,5,1,8,9,7};
    int ln, m;
    ln = sizeof(Arr)/sizeof(int);
    int i, j, k, min_;
    for(i=0; i<ln; i++)
    {
        for(j=0; j<ln; j++)
        {
            if(Arr[j] > Arr[j+1])
            {
                k = Arr[j];
                Arr[j] = Arr[j+1];
                Arr[j+1] = k;
            }
            for(m=1; m<=ln; m++)
            {
                cout<<Arr[m]<<", ";
            }
            cout<<endl;
        }
    }
    for(m=0; m<ln; m++)
    {
        cout<<Arr[m]<<", ";
    }

}
