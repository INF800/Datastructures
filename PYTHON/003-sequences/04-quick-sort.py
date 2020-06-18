def swap(a, p, q):
    temp  = a[p]
    a[p]  = a[q]
    a[q]  = temp
#end def


def partition(a, beg, end):
    """
    selects end of list as pivot and arranges such that 
    - elements less than/eq to pivot are in left
    - elements right than pivot are in right
    - returns index of partition
    """
    pivot = a[end-1] # keep it untouched
    pidx  = beg   # linearly incr & swap this with lowest

    # go through all elements and push
    # ele < pivot at begining i.e @incrementally increasing pidx
    # note: we don't care if `a[idx] > pivot` because pidx doesn't increment! 
    for idx in range(beg, end):
        if a[idx] <= pivot: 
            swap(a, idx, pidx) # indices!
            pidx += 1 # incr 

    return pidx-1 #as it will always be incremented to +1 extra
#end def


def qsort(a, beg, end):
    """
    partitions first and then calls itself recursively
    (oppt. to msort -> call itself recursively and then merges)
    """
    if (beg>=end-1):
        # `beg==end-1` will not work here as there will be
        # cases where there won't be any leaves! (@end of recursion)
        return

    pidx = partition(a, beg, end)
    qsort(a, beg, pidx) # if we include pidx, we will get into worst case t.c! note: we are not inluding here (beg,end]
    qsort(a, pidx, end)
#end def


def randomize(a, beg, end):
    """ worst case of randomize qsort is still O(n^2)
    but it increases chances if it being o(nlogn) """
    import random
    randint = random.randint(beg, end-1)
    
    for idx in range(beg, end):
        swap(a, idx, randint)

if __name__ == "__main__":
    """
    a = [5,3,2,1,6,3]
    print(partition(a, 0, len(a)))
    #partition(a, 0, 3)
    #print(partition(a, 2, 6))
    print(a)
    """

    a = [5,3,-2,0,1,6,3]
    # basic qsort
    qsort(a, 0, len(a))
    print(a)

    # randomized quicksort - first randomize seq and then call qsort
    # high chaces that divides in middle s.t tc becomes O(nlogn)
    # but worst case is still n^2
    randomize(a, 0, len(a))
    qsort(a,0,len(a))
    print(a)
