# ============================================================================================================================
# Bloom Filters
# ============================================================================================================================
# - membership data structure. rets yes/no only. Cannot be used for other operation like delete etc.
# - Never gives `False Negative` but can give `False positive` (Adding some items may add other unwanted items automatically!)
# - probability score can be calulated using:
#       + Number of bits used (greater the better)
#       + Number of hash funcs (greater the better)
#       + Number of items added (lesser the better)
#       - Formula: 
#
# - Create a simple array of some len(initially all zero) and then make rets of hashes for adding item `1`

class BloomFilter:
    """ MEMBERSHIP DATASTRUCTURE

    Data Members
        - bit_arr       : constant sized bit array 1/0 eles only. (use Bitset data struc for space eff.)

    Methods:
        
        - hash_func1    : uses predetermined "suffix" to python hash func for distinction (can use unique seed too)
        - hash_func2    : - do -
        - hash_func3    : - do -

        - add          : adds element e (imuuatable pyobj) to bloom filter
                            + Adding some items may add other unwanted items automatically!
        - __contains__ : checks if element e (imuuatable pyobj) in bloom filter  
                            + Sometimes may return YES even if not present
                            + Never returns YES if not present
                            + Probability of it can found using m,n,k

    Note: This is BIT array! won't take much space! and Very fast membership test too!!
    """

    def __init__(self, contents=[], bit_arr_size=100):
        self.bit_arr = [0] * bit_arr_size # Initially all 0. use `Bitset` datastruc for space eff.
        
        self.__bit_arr_size         = bit_arr_size
        self.__hash_func1_suffix    = '000011' # anything but different
        self.__hash_func2_suffix    = '001111'
        self.__hash_func3_suffix    = '111111'

        for e in contents:
            self.add(e)

    def add(self, e):
        # get bloom idxs
        hash1_idx = BloomFilter.__hash_func(e, self.__hash_func1_suffix, self.__bit_arr_size)
        hash2_idx = BloomFilter.__hash_func(e, self.__hash_func2_suffix, self.__bit_arr_size)
        hash3_idx = BloomFilter.__hash_func(e, self.__hash_func3_suffix, self.__bit_arr_size)

        # put `1` in respective idxs meaning element present
        self.bit_arr[hash1_idx] = 1
        self.bit_arr[hash2_idx] = 1
        self.bit_arr[hash3_idx] = 1

    def __contains__(self, e):
        # get bloom idxs
        hash1_idx = BloomFilter.__hash_func(e, self.__hash_func1_suffix, self.__bit_arr_size)
        hash2_idx = BloomFilter.__hash_func(e, self.__hash_func2_suffix, self.__bit_arr_size)
        hash3_idx = BloomFilter.__hash_func(e, self.__hash_func3_suffix, self.__bit_arr_size)

        # if all idx vals are `1`, member present
        # sometimes answer is wrong (but never `NO` for member item)
        if (self.bit_arr[hash1_idx] == 0) or (self.bit_arr[hash2_idx] == 0) or (self.bit_arr[hash3_idx] == 0):
            return False
        #else,
        return True
    
    # -----------------------------------------------------
    # hash func
    # -----------------------------------------------------
    @staticmethod
    def __hash_func(e, suffix, bit_arr_size):
        """
        - Hash func must gen uniformly distributed vals
        """
        to_hash = str(e) + suffix + str(type(e)) # make sure '1001'(str) and 1001(int) noticed differently 

        int_hash_val = hash(to_hash) # suffix guaranteed the hash func is unique
        idx = int_hash_val % bit_arr_size # in range [0, bit_arr_size]

        return idx





if __name__ == "__main__":
    lst = ['apple', -99, 0, 6, 1.3, (3,6), [3,6]]

    # 1. add
    bf = BloomFilter(lst)

    # 2. test membership
    print('Must be true:')
    for item in lst:
        print(item in bf)

    print('Must be false:')
    print('-99' in bf) # rets true if type not used with "suffix" as int(-99) is present
    print('hash' in bf)
    print((6,3) in bf)
    print([6,3] in bf) # note as str representation is used order is important