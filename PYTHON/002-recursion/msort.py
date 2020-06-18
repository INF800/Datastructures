def merge(arr, beg, end):
    mid = (beg + end)//2
    res = [None] * (end-beg)
    k = 0
    lidx = beg
    ridx = mid

    while (lidx<mid) and (ridx<end):
        if arr[lidx] <= arr[ridx]:
            res[k] = arr[lidx]
            lidx = lidx + 1
        elif arr[lidx] > arr[ridx]:
            res[k] = arr[ridx]
            ridx = ridx + 1
        k = k+1

    while (lidx<mid): res[k] = arr[lidx]; k=k+1; lidx=lidx+1
    while (ridx<end): res[k] = arr[ridx]; k=k+1; ridx=ridx+1
    
    for i in range(0, end-beg):
        arr[beg+i] = res[i] 



def func(arr, beg, end):
    
    if beg == end-1:
        return

    mid = (end + beg) // 2
    func(arr, beg, mid)
    func(arr, mid, end)
    #print("beg:",beg," mid:",mid," end:",end)
    #print(arr[beg:end])
    #merge(arr, beg, end)

a = [5,4,3,8,-9,3]
func(a, 0, 6)

'''
arr = [4,8,9,1,2,4]
merge(arr, 0, 6)
print(arr)
'''