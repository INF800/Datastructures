#include <iostream>
using namespace std;

void merge(int a[], int beg, int end) {
    int res[end-beg];
    int k = 0;
    int mid = (end+beg)/2;
    int lidx = beg;
    int ridx = mid;
    
    while ((lidx<=mid) && (ridx<end)){
        if (a[lidx]<=a[ridx]) res[k] = a[lidx]; lidx++;
        if (a[lidx]>a[ridx]) res[k] = a[ridx]; ridx++;
        k++;
    }
    
    while (lidx<=mid) res[k] = a[lidx]; lidx++; k++;
    while (ridx<end)  res[k] = a[ridx]; ridx++; k++;
    
    for(int idx=0; idx<(end-beg); idx++){
        a[beg+idx] = res[idx];
    }
}

int main(){
    
    int arr[2] = {5,8};
    int n = 2;
    merge(arr, 0, n);
    for(int i=0; i<n; i++){
        cout<<arr[i]<<" ";
    }
}
