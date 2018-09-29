#include<bits/stdc++.h>
using namespace std;

int main()
{
    int Arr []= {2,3,4,1,5,7,8,9,6};
    int i, n, a;
    n = sizeof(Arr)/sizeof(int);
    int j, min_num;

    for(i=0; i<n; i++)
    {
        for(j=i+1; j<n; j++)
        {
            if(Arr[min_num] > Arr[j])
            {
                min_num = j;
            }
        }
        a = Arr[i];
        Arr[i] = Arr[min_num];
        Arr[min_num] = a;
    }
    int k;
    cout<<"{ ";
    for(k=0; k<n; k++)
    {
        cout<<Arr[k];
        if(k!=n-1)
        {
            cout<<", ";
        }

    }
    cout<<" }"<<endl;
}
