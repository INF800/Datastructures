def merge(a, beg, end):
    """
    - `a` has left and right sublists which are
    sorted but `a` isn't.
    - The left and right sublists are separated
    by mid but are in same list
    """
    mid  = (end+beg)//2
    lidx = beg
    ridx = mid
    res  = [None]*(end-beg) # variable length
    k    = 0

    while (lidx<mid) and (ridx<end):
        if a[lidx] <= a[ridx]: res[k] = a[lidx]; lidx += 1
        elif a[lidx] > a[ridx] : res[k] = a[ridx]; ridx += 1
        k += 1
    
    while (lidx<mid): res[k] = a[lidx]; lidx += 1; k += 1
    while (ridx<end): res[k] = a[ridx]; ridx += 1; k += 1

    a[beg:end] = res[:] # sort in exact index
#end def

def msort(a, beg, end):
    """
    merges sort
    """
    if beg==end-1: # -1 as we use natural numbers
        # for spl. case - empty list - use `beg>=len-1`
        return
    mid = (end+beg)//2
    msort(a, beg, mid) # will reach left most leaf
    # starts coming back
    msort(a, mid, end)
    # starts coming back
    merge(a, beg, end)

#end def

if __name__ == "__main__":
    """
    # Test `merge`
    #a =[5,3] 
    a =[3,5,4,1]
    #merge(a, 0, len(a))
    merge(a, 2,4)
    print(a)
    """

    # Test `msort`
    #a = [5,3,4,1]
    a = [3,-5,2,-7,5,-4,3,2]
    msort(a, 0, len(a))
    print(a)