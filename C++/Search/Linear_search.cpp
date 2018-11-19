// C++ code for linearly search x in arr[].  If x
// is present  then return its  location,  otherwise
// return -1
#include <bits/stdc++.h>
using namespace std;

int search(int arr[], int n, int x)
{
    int i;
    for (i = 0; i < n; i++)
        if (arr[i] == x)
         return i;
    return -1;
}

int main()
{
    int arr[6] = {1,2,8,4,6,8};
    int x = 6;
    int ans = search(arr,6,x);
    if(ans!=-1){
        cout<<x<<" is found at position: "<<ans<<endl;
    }else{
        cout<<x<<" is not found in array"<<endl;
    }
}