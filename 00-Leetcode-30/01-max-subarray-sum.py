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
        # for comparing (initially some random)
        MAX_SUB_ARR_SUM = self.in_arr[0]
        MAX_LCUR        = 0
        MAX_RCUR        = 1

        # use lcur and rcur
        for lcur in range(0, self.size):
            # make sure not empty sub-arr 
            # eg. [0:0] or [1:1] or [2:2] i.e lcur==rcur
            # thus use `lcur+1` not simply `lcur`
            for rcur in range(lcur+1, self.size):
                # guess and check
                #print("processing:", self.in_arr[lcur:rcur])
                SUB_ARR_SUM = 0
                for idx in range(lcur, rcur):
                    SUB_ARR_SUM += self.in_arr[idx]
                    if SUB_ARR_SUM > MAX_SUB_ARR_SUM:
                        MAX_SUB_ARR_SUM     = SUB_ARR_SUM
                        MAX_LCUR            = lcur
                        MAX_RCUR            = rcur 
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
        # for comparing (initially some random)
        MAX_SUB_ARR_SUM = self.in_arr[0]
        MAX_LCUR        = 0
        MAX_RCUR        = 1

        # use lcur and rcur
        for lcur in range(0, self.size):
            # rcur should start from exactly from `lcur` 
            # but rcur should not be eq to lcur (cz it causes empty array)
            # thus WHILE ACCESSING SUB-ARRAY use `lcur:rcur+1` not `lcur:rcur`
            _running_sum = 0
            for rcur in range(lcur, self.size):
                #print("processing:", self.in_arr[lcur:rcur+1]) #note: rcur+1
                _running_sum += self.in_arr[rcur] 
                #print(_running_sum)
                if _running_sum > MAX_SUB_ARR_SUM:
                    MAX_SUB_ARR_SUM     = _running_sum
                    MAX_LCUR            = lcur
                    MAX_RCUR            = rcur + 1 # note +1

        return MAX_SUB_ARR_SUM, MAX_LCUR, MAX_RCUR

    def divide_and_conquer(self):
        """Divide & Conquer

        - divide array into two halves (by mid)
        - `end` not inclusive i.e (beg,end]
        - return maximum of the three
            i.      max of left-sub-array SUM (recursive call) 
            iii.    max of right-sub-array SUM  (recursive call)
            iv.     max of left-sub-array, right-sub-array and whole-array SUM (custom func)

        TIME        : O(nlogn)
        SPACE       : O(n)
        """
        def recur(beg, end):
            """ 
            - focus on either if the three RECURSIVELY:
                + left      : max sub-array sum 
                + right     : max sub-array sum 
                + crossing  : max sub-array sum 
            """
            # base
            if beg == end-1:
                return self.in_arr[beg]

            mid = (beg + end)//2
            l_max       = recur(beg, mid)
            r_max       = recur(mid, end)
            x_max       = self.__x_max(beg, mid, end)
            return max(l_max, r_max, x_max)

        # main recursive call
        return  recur(beg=0, end=self.size)

    def __x_max(self, beg, mid, end):
        """Crossing-Sum from Mid

        - Not same as iterating from beg->end & finding MSS

        TIME        : O(n)
        SPACE       : O(n)
        """
        L_CUR   = None
        R_CUR   = None

        _running_sum = 0; L_MAX = self.in_arr[beg]
        for idx in range(mid-1, beg-1, -1): # mid !inclusive 
            _running_sum += self.in_arr[idx]
            L_MAX         = max(_running_sum, L_MAX) 

        _running_sum = 0; R_MAX = self.in_arr[mid]
        for idx in range(mid, end, 1): # end !inclusive
            _running_sum += self.in_arr[idx]
            R_MAX         = max(_running_sum, R_MAX)

        # Only `L_MAX+R_MAX` because -- ?
        return L_MAX+R_MAX



if __name__ == "__main__":
    # input
    arr = [-2,1,-3,4,-1,2,1,-5,4]
    soln = max_sub_arr(in_arr=arr, size=len(arr))

    # 1. bruteforce
    printhead(soln.bruteforce.__doc__)
    max_sum, lcur, rcur = soln.bruteforce()
    print(arr[lcur:rcur], "sum:", max_sum)

    # 2. bruteforce w/ cache
    printhead(soln.bruteforce_cache.__doc__)
    max_sum, lcur, rcur = soln.bruteforce_cache()
    print(arr[lcur:rcur], "sum:", max_sum)

    # 3. divide and conquer
    printhead(soln.divide_and_conquer.__doc__)
    a = soln.divide_and_conquer()
    print(a)


