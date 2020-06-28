import math

def printhead(string, x=100):
    print("\n\n"+"+"*x)
    print("+ " + string)
    print("+"*x)

class max_sub_arr:
    def __init__(self, in_arr, size):
        self.in_arr = in_arr
        self.size   = size

        # if all items are positive,
        # solution is trivial: The main array!
        all_postive = True
        for idx in range(0, size):
            if in_arr[idx] < 0:
                all_postive = False
                break
        if all_postive is True:
            raise("All Inputs are Positive!")

    def bruteforce(self):
        """Simple Bruteforce

        - use lcur and rcur for bruteforce search of all possible sub-arrays.
        - then, use another loop to find sum of subarr
        - guess compare check using globals

        TIME        : O(n^3)
        SPACE       : O(n)
        """
        # for comparing (initially least )
        MAX_SUB_ARR_SUM = -math.inf
        MAX_LCUR        = None # as it is least, if condition will exec at-
        MAX_RCUR        = None # least once. Hence, idxs wont be `None` in end

        # use lcur and rcur
        for lcur in range(0, self.size):
            for rcur in range(lcur, self.size):
                # guess and check
                # print("processing:", self.in_arr[lcur:rcur+1]) # Note: while accesing always use `rcur+1` (cz slicing is !inclusive)
                
                SUB_ARR_SUM = 0
                for idx in range(lcur, rcur+1): # Note: while accesing always use `rcur+1` (cz slicing is !inclusive) 
                    SUB_ARR_SUM += self.in_arr[idx]
                    if (SUB_ARR_SUM > MAX_SUB_ARR_SUM):
                        MAX_SUB_ARR_SUM     = SUB_ARR_SUM
                        MAX_LCUR            = lcur
                        MAX_RCUR            = rcur # Note:(see note above) as we are not returning rcur+1 use +1 in main driver code cz slicing is !inclusive
                        #break #if max sum not needed

        return MAX_SUB_ARR_SUM, MAX_LCUR, MAX_RCUR
                    
    def bruteforce_cache(self):
        """Bruteforce w/ Cache

        - use lcur and rcur for bruteforce search of all possible sub-arrays.
        - then, use `rcur` to find sum of sub-arrays
        - guess compare check using globals

        TIME        : O(n^2)
        SPACE       : O(n)
        """
        # for comparing (initially least )
        MAX_SUB_ARR_SUM = -math.inf
        MAX_LCUR        = None # as MSS is least, if condition will exec at-
        MAX_RCUR        = None # least once. Hence, idxs wont be `None` in end

        # use lcur and rcur
        for lcur in range(0, self.size):
            _running_sum = 0
            for rcur in range(lcur, self.size):
                #print("processing:", self.in_arr[lcur:rcur+1]) # note: +1 (explined in `def bruteforce`)
                _running_sum += self.in_arr[rcur] 
                #print(_running_sum)
                if _running_sum > MAX_SUB_ARR_SUM:
                    MAX_SUB_ARR_SUM     = _running_sum
                    MAX_LCUR            = lcur
                    MAX_RCUR            = rcur # note: not using +1 (explained above). Use +1 in main driver code cz slicing is !inclusive

        return MAX_SUB_ARR_SUM, MAX_LCUR, MAX_RCUR

    def divide_and_conquer(self):
        """Divide & Conquer

        - divide array into two halves (by mid)
        - `end` not inclusive i.e (beg,end]
        - base condn. return single element
        - return maximum of the three (with indices)
            i.      max of left-sub-array SUM (recursive call) 
            iii.    max of right-sub-array SUM  (recursive call)
            iv.     max of left-sub-array, right-sub-array and whole-array SUM (custom func)

        TIME        : O(nlogn)
        SPACE       : not O(num. of calls) cz. we fiddle ONLY with indices
        """
        def recur(beg, end):
            """ SIMILAR TO MERGESORT (postfix traversal)
            - focus on either if the three RECURSIVELY:
                + left      : max sub-array sum 
                + right     : max sub-array sum 
                + crossing  : max sub-array sum 
            - we recursively return either 
                + single element (or)
                + max(l_max, r_max, cross_max) 
            """
            # base
            if beg == end-1:
                return self.in_arr[beg], beg, end

            mid = (beg + end)//2
            l_max, lcur, rcur     = recur(beg, mid)
            r_max, lcur, rcur     = recur(mid, end)
            x_max, lcur, rcur     = self.__x_max(beg, mid, end)
            
            # return max(
            #   recur(beg, mid),
            #   recur(mid, end),
            #   x_sum(beg, mid, end))
            if l_max >= r_max and l_max >= x_max:
                return l_max, beg, mid
            elif r_max >= l_max and r_max >= x_max:
                return r_max, mid, end
            else: #x_max > l_max and x_max > r_max:
                return x_max, lcur, rcur

        # main recursive call
        return recur(beg=0, end=self.size)

    def __x_max(self, beg, mid, end):
        """Crossing-Sum from Mid

        - Not same as iterating from beg->end & finding MSS

        TIME        : O(n)
        SPACE       : O(n)
        """
        L_CUR   = None
        R_CUR   = None

        _running_sum = 0; L_MAX = -math.inf
        for idx in range(mid-1, beg-1, -1): # mid !inclusive 
            _running_sum += self.in_arr[idx]
            if _running_sum > L_MAX:
                L_MAX       = _running_sum
                L_CUR       = idx  

        _running_sum = 0; R_MAX = -math.inf
        for idx in range(mid, end, 1): # end !inclusive
            _running_sum += self.in_arr[idx]
            if _running_sum > R_MAX:
                R_MAX       = _running_sum
                R_CUR       = idx  


        # Only `L_MAX+R_MAX`
        return L_MAX+R_MAX, L_CUR, R_CUR

    def kadane(self):
        """Kadane's algorithm (w/o indiced. only w/ MSS)

        - Idea is -- for each idx in array find
            + max of sum-of-subarray that ends at that idx
            + (max of all found them sum-of-subarray is soln.)


        TIME        : O(n)
        SPACE       : O(n)
        """
        MSS             = -math.inf
        _running_sum    = 0

        for idx in range(0, self.size):
            cur_val         = self.in_arr[idx]
            # according to kadane, max of sum-of-subarray that ends at any
            # givem idx is --
            # max of `cur_val` at idx max and max-of-sum-of-subarray so far plus `cur_val`
            _running_sum    = max(cur_val, _running_sum+cur_val)
            # collect `MSS` which is best i.e max of all mss at all pos
            MSS = max(MSS, _running_sum)
        
        return MSS

    def max_subarray_sum_with_indices(self):
        """ Kadane's w/ inices
        Computes the subarray indices as well as maximum sum as well

        - Same as Kladane
            + find MSS until cur idx
            + collect the best
        - Note: How indices are caught

        TIME        : O(n)
        SPACE       : O(n)
        """
        MSS = -math.inf
        L_CUR = R_CUR = None
        _running_sum = 0

        for idx, val in enumerate(self.in_arr):
            # i. find max of sum-of-subarray that ends at `idx`
            if _running_sum <= 0:
                _running_sum  = val
                _start        = idx
            else:
                _running_sum += val

            # ii. collect best
            if _running_sum > MSS:
                MSS     = _running_sum
                L_CUR   = _start         
                R_CUR   = idx + 1

        # as idx starts and ends (beg, end) --
        # R_CUR should be inclusive in main driver code
        return MSS, L_CUR, R_CUR

if __name__ == "__main__":
    # input
    # [-2,1,-3,4,-1,2,1,-5,4]
    # [-2,1,-3,4,-1,2,1,-5,4,7]
    # [-2,1,-3,4,-1,2,1,-5,4, 0,9,2]
    # [1,0,-2,1,-3,4,-1,2,1,-5,4, 0,9,2]
    arr = [-9.0, 10.0, 2.0, 3.0]#[-10,9,2,4]
    print(len(arr))
    soln = max_sub_arr(in_arr=arr, size=len(arr))

    # 1. bruteforce
    printhead(soln.bruteforce.__doc__)
    max_sum, lcur, rcur = soln.bruteforce()
    print(arr[lcur:rcur+1], "sum:", max_sum)

    # 2. bruteforce w/ cache
    printhead(soln.bruteforce_cache.__doc__)
    max_sum, lcur, rcur = soln.bruteforce_cache()
    print(arr[lcur:rcur+1], "sum:", max_sum)

    # 3. divide and conquer 
    printhead(soln.divide_and_conquer.__doc__)
    max_sum, lcur, rcur = soln.divide_and_conquer() # not working with 0,9,2
    print(arr[lcur:rcur+1], "sum:", max_sum)

    # 4. Kadane's algorithm (w/o indices)
    printhead(soln.kadane.__doc__)
    max_sum = soln.kadane()
    print(f"MSS is: {max_sum}")

    # 5. Kadane's w/ indices
    printhead(soln.max_subarray_sum_with_indices.__doc__)
    max_sum, lcur, rcur = soln.max_subarray_sum_with_indices()
    print(arr[lcur:rcur], "sum:", max_sum)
