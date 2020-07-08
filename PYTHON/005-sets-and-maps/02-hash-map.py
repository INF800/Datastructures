from utility import HashSet

class HashMap:
    """
    DATA MEMBERS
        - hset          : HashSet instance to hold `keys`

    PRIVATE CLASSES
        - __KVPair      : To map keys to to their values
                            + it's instance is stored in _hset, not simple py-objs

    METHODS 
        - add           : adds e to HashMap

        -__len__        : returns size of hashmap i.e _hset
    """

    class __KVPair:
        def __init__(self, k, v):
            self.k = k
            self.v = v

        def get_key(self):
            return self.k

        def get_value(self):
            return self.v

        def __hash__(self):
            """
            - While computing hash in hashset hash(ele) is used.
            - As inst. of __KVPair will be  ele,
                    + hash(__KVPairObj) should return hash(k)
                    + It is same as if we are storing only keys in _list of hset
                        + but with help of this class, we store values as well
            """
            return hash(self.k)

        def __eq__(self, other):
            """ In hashset implementation, we check equalities based on keys"""
            if type(self) != type(other): # we store only __KVPair obj
                return False
    
            return (self.k == other.k) # both kvpairobjs are same if their keys are same

    # ---------------------------------
    # end class __KVPair
    # ---------------------------------

    def __init__(self, kv_pairs=[]):
        """
        kv_pairs = [
            ['a', 'apple'], 
            ['p','parrot'], 
            ['d', 'dog']
        ]
        """
        self._hset = HashSet([])

        for k, v in kv_pairs:
            self.add(k, v)

    def add(self, k, v):
        # instead of storing just keys(simple py-objs) in set, 
        # store __KVPair instance
        KVPair = HashMap.__KVPair(k, v)
        self._hset.add(KVPair)

    def remove(self, k):
        KVPair = HashMap.__KVPair(k, None) # val is not important
        self._hset.remove(KVPair)
    
    def keys(self):
        for KVPair in self._hset:
            yield KVPair.get_key()

    def __iter__(self):
        for KVPair in self._hset:
            yield KVPair.get_key(), KVPair.get_value()

    def __len__(self):
        return len(self._hset)

    # dont use `if e in dic.keys()` cz it is lin search
    # use `if e in dict` cz hashed search
    def __contains__(self, k):
        KVPair = HashMap.__KVPair(k, None)
        return KVPair in self._hset


if __name__ == '__main__':
    lst = [
        ['a',       'apple'], 
        ['p',       'parrot'],
        [53,        'fiftythree'],
        ['d',       'dog'],
        [-53,       'neg_fiftythree'],
        ['x',       'xmas']
    ]
    
    for k, v in lst:
        print(f'k:{k} \t v:{v}')

    def printline(func, s='+', x=100):
        print(s*x)
        func()
        print(s*x)

    @printline 
    def A():
        print('TESTING HASH-MAP')

    @printline
    def test_add_keys_iter():
        hmap = HashMap(lst)

        # test 1-1 keys
        keys        = []
        actual_keys = ['a', 'd', 'p', 'x', 53, -53]
        for k in hmap.keys():
            #print(k)
            keys.append(k)
        
        # log test
        failed = False
        for e in actual_keys:
            if e not in keys:
                print('Test 1-1: Add / Keys() Failed') 
                failed =True
                break
        if not failed:
            print('Test 1-1: Add / Keys() Passed')
        
        # test 1-2 iter
        actual_keys     = ['a', 'd', 'p', 'x', 53, -53]
        corresp_vals    = ['apple', 'dog', 'parrot', 'xmas', 'fiftythree', 'neg_fiftythree']
        keys            = []
        vals            = []
        for k, v in hmap:
            #print(f'k:{k} \t v:{v}')
            keys.append(k)
            vals.append(v)
        
        # log test
        failed = False
        for k, v, tk, tv in zip(
            sorted(map(lambda x: str(x), actual_keys)), corresp_vals, 
            sorted(map(lambda x: str(x), actual_keys)), vals):

            if (k != tk) and (v != tv):
                print('Test 1-2: Add / iter Failed')
                failed = True
                break
        
        if not failed:
            print('Test 1-2: Add / iter Passed')

    @printline
    def test_remove():
        
        hmap = HashMap(lst)
        hmap.remove('x')

        for k, _ in hmap:
            # note: `in` shows polymorphism for both iterator and contains
            # print(f'k:{k} \t v:{v}')
            pass

        if 'x' in hmap:
            print('Test 2-1: Remove / iter Failed')
        print('Test 2-1: Remove / iter Passed')