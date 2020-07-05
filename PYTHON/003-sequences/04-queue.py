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
        ratio=0.75
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

        if self.isempty(): raise('Queue Empty!')        

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
        if self.isempty(): raise('Queue is empty!')
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