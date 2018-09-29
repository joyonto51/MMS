#include <bits/stdc++.h>
using namespace std;

int main()
{
    int Arr[] = {1,2,3,5,6,8,9,11,14,16,19,20,23,24,25,27,28,30};
    int len = sizeof  Arr/sizeof(int);

    int i, a, b = 0, c, y, n, key;
    printf("Enter a number:");
    scanf("%d",&key);

    for(i=0;i<=len;i++)
    {
        a = Arr[i];
        c = key-a;
        int mid, m=0, start=1, end=len;
        mid = int((start + end)/2);

        while((start<=end) && (Arr[mid]!=c))
        {
            if(c < Arr[mid])
            {
                end = mid-1;

            }
            else
            {
                start = mid +1;
            }

            mid = int((start + end)/2);

            if(Arr[mid] == c)
            {
                m = mid + 1;
                b = Arr[mid];
            }
            else
            {
                m = -1;
            }

        }
        y = m;
        n = i+1;
        if(b!=0)
        {
            break;
        }

    }
    cout<<"Value: "<<a<<", "<<b<<endl;
    cout<<"Index: "<<n<<", "<<y<<endl;
}
