class Queue:
    """
    DATA MEMBERS
        - _list     : internal list
        - _size     : keeps track of _list size
        - head      : tracks beg idx of queue
        - tail      : tracks end

    METHODS
        - enqueue       : ammortized append
        - dequeue       : ammortized remove from beg
        - __len__       : lengh of queue ((head and tail are -1 if empty))
        - __makeroom    : increases portion at end
        - __compress    : same as makeroom (shifts left and truncates unused portion at beg)
        - isempty       : return bool (exploiits __len__)
        - get_front     : returns e at head
        - get_tail      : returns e at tail

    All operations are O(n) or Ammortized O(n)
    """
    def __init__(self, contents=[], initial_size=10):
        self._list = [None]*initial_size
        self._size = initial_size 
        self.head  = -1
        self.tail  = -1

        for e in contents:
            self.enqueue(e)

    def enqueue(self, ele):
        ratio=0.6
        if len(self) > self._size*ratio:
            self.__makeroom()

        if self.isempty():
            self.head = self.tail = 0
            self._list[self.head] = ele
            return
            
        self._list[self.tail+1] = ele
        self.tail += 1


    def __makeroom(self):
        new_list = [None] * (2*self._size)
        
        k = 0
        idx = self.head
        while idx <= self.tail:
            new_list[k] = self._list[idx]
            k   += 1
            idx += 1
        
        self._list      = new_list
        self._size      = 2 * self._size
        self.tail       = self.tail-self.head
        self.head       = 0

    def dequeue(self):
        ratio = 0.2
        if self.head > self._size*ratio:
            self.__compress()

        if self.isempty(): return 'Queue Empty!'

        popped = self._list[self.head]
        self._list[self.head] = None
        self.head += 1
        return popped


    def __compress(self):
        new_list = [None] * self._size

        k = 0
        idx = self.head
        while idx <= self.tail:
            new_list[k] = self._list[idx]
            k   += 1
            idx += 1
        
        self._list  = new_list
        self._size  = self._size # not truncating but shifting to left
        self.tail   = self.tail-self.head
        self.head   = 0

    def __len__(self):
        if (self.head == -1) and (self.tail==-1): return 0
        return (self.tail - self.head)+1

    def isempty(self):
        if (len(self) == 0) or (self.head > self.tail): return True
        return False

    def get_head(self):
        if self.isempty(): return 'Queue is empty!'
        return self._list[self.head]

    def get_tail(self):
        if self.isempty(): raise('Queue is empty!')
        return self._list[self.tail]

# -------------------------------------------------------
# end queue
# -------------------------------------------------------

if __name__ == '__main__':

    # 1. empty queue
    q = Queue()
    if q.isempty() == True: print('1. Empty queue test passed')
    
    # 2. enqueue
    lst = range(10)
    for e in lst:
        q.enqueue(e)
        #print(q._list, q.tail)
    if q._size == 20:
        print('2. Enqueue test passed')

    # 3. dequeue
    for _ in range(0, 10):
        q.dequeue()
        #print(q._list, q.head, q.tail)
        if q.head==5 and q.tail==4: print('3. Deque test passes')

    # 4. general
    lst = [3,5,2,3,'a','v', 'i', 'o', 't', 'h', '-9']
    q = Queue(lst)
    print('head: ', q.get_head())
    print('tail: ', q.get_tail())
    print(len(q))
    for i in range(0,9):
        print('popped: ', q.dequeue())
    print('after popping')
    print('q: ', q._list)
    print('head: ', q.get_head())
    print('tail: ', q.get_tail())
    print(len(q))



class Stack:
    """
    DATA MEMBERS
        - _list     : helper internal array
        - size      : keeps track of size  

    METHODS
        - push      : inserts e at top
        - pop       : removes and return the e at top
        - top       : return e at top
        = __topidx  : returns idx of top
        - isEmpty   : bool

    All opeations have TIME O(n) or ammortized O(n)
    """

    def __init__(self, contents=[]):
        self._list = []

        for e in contents:
            self.push(e)
        
    def push(self, ele):
        self._list.append(ele)
    
    def pop(self):
        if self.isEmpty():
            range('Stack underflow!')
        
        popped = self._list[self.__topidx()]
        del self._list[self.__topidx()]
        return popped
    
    def top(self):
        if self.isEmpty():
            raise('Stack is empty!')
        
        return self._list[self.__topidx()]

    def isEmpty(self):
        if len(self._list) == 0: return True
        return False


    def __topidx(self):
        return len(self._list) - 1
        
    def __len__(self):
        return len(self._list)


# ------------------------------------------------
# end stack
# ------------------------------------------------

if __name__ == '__main__':
    
    # 1. empty stack
    s = Stack()
    if s.isEmpty() is True:
        print('1. Empty stack text passed')

    # 2.push and top
    lst = list(range(10))
    for e in lst:
        s.push(e)
    if s.top() == 9:
        print('2. Push test and top test passed')

    # 3. pop test
    if (s.pop() == 9) and (s.top()==8):
        print('3. Pop test passed')

class HashSet:
    """
    DATA MEMBERS
        - _items        : internal list to hold items
        - _size         : true size of internal list(_items) - used to compute idx
        - num_of_items  : size of Set (apparent size of _items)
    

    METHDOS:
        - __add(e, _list, _size)    : if item added, return true. if already exists returns false
        - __rehash(_list, _size, factor) : copy internal list into new(incr/decr size) and after rehashing 
        - __remove(e, _list, _size) : removes e for _list returns true. if not found, return false

        - __load                : returns load factor after computing
        - add(e)                : exploit __add and __rehash to update _list 
        - remove(e)             : exploit __remove

    All operations are O(n) or ammortized O(n)
    """

    def __init__(self, contents=[], init_size=10):
        self._items         = [None]*init_size
        self._size          = init_size
        self.num_of_items   = 0

        for e in contents:
            self.add(e)

    # -----------------------------------------------
    # implement add
    # -----------------------------------------------
    def __load(self):
        """
        high    : _list full
        low     : _list empty
        """
        return self.num_of_items / self._size

    # @staticmethod
    def __add(self, e):
        """
        return 
            - false : if item already exists. Nohting done
            - true  : if item added
        """
        
        # 1. compute hash as idx
        # reminder is taken as index. 
        #   + always between (0, len-1) (both inclusive)
        #   + never negative
        idx = hash(e) % self._size 

        # 2. Linear probing - computed idx won't always be unique.
        #   + If not unique fill next right most locn by lin search
        #   + if end of list is already filled, cant linear probe. so add one more ele to _items
        while idx < self._size:
            # case1: already exists
            if self._items[idx] == e: return False
            # case 2: empty
            if self._items[idx] is None:
                self._items[idx] = e
                return True
            # case 3: some another obj present
            if self._items[idx] is not None:
                # linear probe but
                idx += 1 # linear probe
                if idx == self._size: # if out of range, 
                    
                    # add one more block to internal list with e in it
                    # Note: This has major problem - need to rehash as _size changes
                    #self._items = self._items + [e]
                    #self._size = self._size + 1
                    #return True
                    
                    # Alternative:
                    # start from beg again. 
                    # if encounters none(which is inevitable) 
                    # after writing to it, terminates
                    idx = 0

    def __rehash(self, step_fac=2):

        old_list = self._items
        old_size = self._size # true size of _list

        new_size   = int(step_fac*old_size)
        new_list   = [None] * new_size
        # update 
        #   - _list with biiger one(empty)
        #   - _size (Hashing using new _size)
        self._items = new_list
        self._size  = new_size
        
        # copy into new list
        for e in old_list:
            self.__add(e)

        # delete old list
        del old_list



    def add(self, ele):
        max_load_factor = 0.75

        if self.__add(ele): # computing hash, linear probing done in __add inplace
            self.num_of_items += 1

            # if max load factor reached (i.e _list if filling up)
            # linear probing will take high T.C. So, increase size
            # (items filled in continous chain with empty __placeholders)
            if self.__load() > max_load_factor:
                self.__rehash(2) # double _list

    # -----------------------------------------------
    # implement remove
    # -----------------------------------------------
    def __remove(self, e):
        # 1. compute hash
        idx = hash(e) % self._size

        # 2. Probe for item linearly
        while idx < self._size:
            # case1: already exists
            if self._items[idx] ==  e:
                self._items[idx] = None # remove
                return True
            # case 2: empty
            if self._items[idx] is None: return False # empty
            # case 3: some another obj present
            if self._items[idx] is not None:
                # linear probe but
                idx += 1 # linear probe
                if idx == self._size: # if out of range, 
                    idx = 0 # start from beg

    def remove(self, e):
        min_load_factor = 0.25

        if self.__remove(e):
            self.num_of_items -= 1

        # rehash into new list with smaller size
        # if load is less than 25% i.e only 25% or less is filled
        # decrease the _list(halve it)
        if self.__load() < min_load_factor:
            self.__rehash(0.5) # halve _list


    # -----------------------------------------------
    # basic
    # -----------------------------------------------
    def __len__(self):
        return self.num_of_items

    def __contains__(self, e):
        # 1. compute hash
        idx = hash(e) % self._size

        # 2. Probe for item linearly
        while idx < self._size:
            # case1: already exists
            if self._items[idx] ==  e:
                return True
            # case 2: empty
            if self._items[idx] is None: return False # empty
            # case 3: some another obj present
            if self._items[idx] is not None:
                # linear probe but
                idx += 1 # linear probe
                if idx == self._size: # if out of range, 
                    idx = 0 # start from beg

    def __iter__(self):
        for idx in range(0, self._size):
            if self._items[idx] is not None:
                yield self._items[idx]


# ---------------------------------------------------
# Note
#       - Insted of using beg = 0 at out of range, to get back to initial
#       - we can use idx = (idx+1) % _size
#           + it makes sure idx is never > size
#                >>> 0%10
#                0
#                >>> 1%10
#                1
#                >>> 10%10
#                0
#                >>> 9%10 (max possible is >>>> _size - 1 <<<<<<<)
#                9
#                >>> 
# ---------------------------------------------------
# END HASHSET
# ---------------------------------------------------


if __name__ == '__main__':
    def printline(s='+', x=100):
        print('\n' + s*x)

    #print(HashSet.__doc__)
    printline()

    # 1. Add
    # ------
    #lst = list(range(10)) # will be added linearly
    lst = [ 9, 19, 'z', '0', -1, 'r', 'a',0,0, -11, 'q', -11]
    s = HashSet(lst)
    #print(s._items)
    #print('unique: ', s.num_of_items)

    failed = False
    for e in lst:
        if e not in s._items:
            print('Test 1-1: Add/rehash FAILED!')
            failed = True
    if not failed:
        print('Test 1-1: Add/rehash passed')

    if len(s) == len(set(lst)):
        print('Test 1-2: Add/rehash passed')
    else:
        print('Test 1-2: Add/rehash FAILED!')

    # 2. Remove / contains
    # ----------
    printline()
    #print('unique before removing: ', len(s))
    #s.remove(-11)
    #print(s._items)
    #print('unique after removing: ', len(s))

    if -11 in s:
        print('Test 2-1: Contains passed')
    else:
        print('Test 2-1: Contains FAILED!')

    s.remove(-11)
    if -11 not in s:
        print('Test 2-2: Remove/contains passed')
    else:
        print('Test 2-2: contains FAILED!')

    # 3. ITER
    printline()
    accumulator = []
    for x in s:
        accumulator.append(x)
    #print(accumulator)
    #print( list( set(s._items) - set([None]) ) )

    failed = False
    for e in list( set(s._items) - set([None]) ):
        if e not in accumulator:
            print('Test 3: Iterator FAILED')
            failed = True
    if not failed:
        print('Test 3: Iterator passed')