#include <bits/stdc++.h>
using namespace std;

/* Function to get index of ceiling of x in arr[low..high] */
int ceilSearch(int arr[], int low, int high, int x) {
  int i;

  /* If x is smaller than or equal to first element,
    then return the first element */
  if(x <= arr[low])
    return low;

  /* Otherwise, linearly search for ceil value */
  for(i = low; i < high; i++)
  {
    if(arr[i] == x)
      return i;

    /* if x lies between arr[i] and arr[i+1] including
       arr[i+1], then return arr[i+1] */
    if(arr[i] < x && arr[i+1] >= x)
       return i+1;
  }

  /* If we reach here then x is greater than the last element
    of the array,  return -1 in this case */
  return -1;
}


/* Driver program to check above functions */
int main(){
   int arr[] = {1, 8, 2, 19, 10, 12, 10};
   int n = sizeof(arr)/sizeof(arr[0]);
   sort(arr,arr+n);//ceil search is applicable to sorted array
   int x = 18;
   int index = ceilSearch(arr, 0, n-1, x);
   if(index == -1)
     cout<<"Ceiling of "<<x<<" doesn't exist in array "<<endl;
   else
     cout<<"ceiling of "<<x<<" is "<<arr[index]<<endl;
   return 0;
}
