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

