

class max_sub_arr:
    def __init__(self, in_arr, size):
        self.in_arr = in_arr 
        self.size   = size

    def bruteforce(self):
        """
        - use lcur and rcur for bruteforce search of all possible sub-arrays.
        - then, use another loop to find sum of subarr
        - guess compare check using globals

        TIME        : O(n^3)
        SPACE       : O(n)
        """
        # for comparing
        MAX_SUB_ARR_SUM = self.in_arr[0]
        MAX_LCUR        = 0
        MAX_RCUR        = 0

        # use lcur and rcur
        for lcur in range(0, self.size):
            # make sure not empty arr 
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
                    
                

if __name__ == "__main__":
    arr = [-2,1,-3,4,-1,2,1,-5,4]
    soln = max_sub_arr(in_arr=arr, size=len(arr))

    # brute force
    max_sum, lcur, rcur = soln.bruteforce()
    print(arr[lcur:rcur], "sum:", max_sum)