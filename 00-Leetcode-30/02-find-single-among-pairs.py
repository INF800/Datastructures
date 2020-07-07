def printhead(text,size=100):
    print("\n\n" + "+"*size)
    print("+" + text)
    print("+"*size)

class FindSingleAmongPairs:
    def __init__(self, in_arr, size):
        self.in_arr     = in_arr
        self.size       = size

    def xor(self):
        """Using XOR

        - XOR for a,b \in Z i.e decimal numbers is similar to either of two funcs
            + max(a,b) * min(a,b) -> where * is decimal subtraction
            + abs(a-b)  


        TIME        : O(n)
        SPACE       : O(n)
        """
        res = 0
        for ele in self.in_arr:
            res = res^ele
        return res

    def hash_map(self):
        """Using Hash Map

        Note: we are using hmap keys exactly like sets. Can solve using sets (easier)
            + can etend this to count number of occurances

        - For every ele in arr,
            + create a key-val pair using `ele` as key 
                - `val` not necessary (can be anything)
                -  only unique will be added as key cz dict
            + if key already exists,
                - remove the key-val pair
            + in the end all pairs will be removed except single among pairs. return it's KEY


        TIME        : O(n)
        SPACE       : O(n)
        """
        hmap = {}

        for idx, ele in enumerate(self.in_arr):    
            if ele in hmap.keys():
                # remove k-v pair if appears twice
                # Note: this should be done before appending uniqe eles
                del hmap[ele]
            else:
                # add unique elements as keys
                hmap[ele] = idx

        # in the end only single among pairs will be remaining.
        single_ele      = list(hmap.keys())[0]
        single_ele_idx  = hmap[single_ele]
        return single_ele, single_ele_idx

    def sets(self):
        """Using SET

        Note: Exactly like hmap. Only without v in k-v pair.
                + cannot extend to count number of occcurances


        TIME        : O(n)
        SPACE       : O(n)
        """

        single_ele_acc = set([])

        for ele in self.in_arr:
            if ele in single_ele_acc:
                # remove paired
                single_ele_acc.remove(ele)
            else:
                # append unique
                single_ele_acc.add(ele)
        
        # in end only single among pairs will survive
        return list(single_ele_acc)[0]


if __name__ == "__main__":
    
    # arr = [1,2,3,2,3,1,5,-4,5,6,6]
    arr = [-1, 1, 1]
    soln = FindSingleAmongPairs(in_arr=arr, size=len(arr))

    printhead(soln.xor.__doc__)
    single_ele  = soln.xor()
    print("single ele among pairs is:", single_ele)

    printhead(soln.hash_map.__doc__)
    ele, idx = soln.hash_map()
    print("single ele among pairs is:", ele, "at index:", idx)

    printhead(soln.sets.__doc__)
    single_ele  = soln.sets()
    print("single ele among pairs is:", single_ele)

