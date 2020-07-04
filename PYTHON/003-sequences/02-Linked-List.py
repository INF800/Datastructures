class Node:
    """
    DATA MEMBERS:
        - item      : data 
        - next      : address to next variable
    
    METHODS
        - get_item  : return self.item      {}              - > {OBJ self.item}
        - set_item  : mutator               {OBJ item}      - > {}
        - get_next  : return self.next      {}              - > {OBJ self.next}
        - set_next  : mutator               {OBJ next}      - > {}
    """

    def __init__(self, item=None, next=None):
        self.item   = item
        self.next   = next

    def get_item(self):
        return self.item
    
    def set_item(self, item):
        self.item = item
        
    def get_next(self):
        return self.next
    
    def set_next(self, next):
        self.next = next

class Llist:
    """

    KEY IS TO GET PREV NODE!

    DATA MEMBERS
        - contents  : list of input items as elements (used only while llist initialisation)
        - first     : first node
        - last      : last node
        - size      : len of llist

    METHODS
        - append            : creates node with item and add at end     {OBJ item}          -> {}
        - __getitem__       : returns item of node at index             {INT idx}           -> {OBJ}
        - __setitem__       : mutates item of node at index             {INT idx, OBJ item} -> {}
        - __add__           : return new llist - adds two llists        {LLIST other}       -> {LLIST result}
        - insert            : creates node with item an inserts         {OBJ item}          -> {}
    """

    def __init__(self, contents=[]):
        """
        - To avoid manier special cases we put an empty dummy node at beg.
            + as key to many opns. is to get prev node, we need the dummy 
        - Empty llist still has that empty node
        """
        self.first  = Node() # dummy (To access first actual node, use ll.first.get_next().item (Note: ll not empty))
        self.last   = self.first # the same node
        self.size   = 0 # incremented in self.append (below)

        for ele in contents:
            self.append(ele)

    def append(self, item):
        """
        - take advantage of self.lat
        - don't forget to
            + incr self.size
            + rewrite self.last
        
        TIME    : O(1)
        """
        _node = Node(item=item)

        self.last.set_next(_node)
        self.size += 1

        self.last = _node

    def __getitem__(self, idx):
        """
        TIME    : O(n)
        """
        if idx < 0 : raise('Index cannot be negative')
        if idx > self.size-1 : raise('Llist index out of range')
        # else

        cursor = self.first.get_next() # addr of actual node at idx 0 (not dummy)
        for _ in range(0, idx):
            cursor = cursor.get_next() 
            # _         - stops at prev node of idx
            # curson    - stops at node at idx
        return cursor.get_item()

    def __setitem__(self, idx, item):
        """
        TIME    : O(n)
        """
        if idx < 0 : raise('Index cannot be negative')
        if idx > self.size-1 : raise('Llist index out of range')
        # else

        cursor = self.first.get_next() # addr of actual node at idx 0 (not dummy)
        for _ in range(0, idx):
            cursor = cursor.get_next() 
            # _         - stops at prev node of idx
            # curson    - stops at node at idx
        cursor.set_item(item)

    def __add__(self, other):
        """
        TIME    : O(m+n)
        """
        if type(self) != type(other) : raise('Not a LList')
        res     = Llist()

        cursor = self.first.get_next()
        while cursor is not None:
            res.append(cursor.get_item())
            cursor = cursor.get_next()

        cursor = other.first.get_next()
        while cursor is not None:
            res.append(cursor.get_item())
            cursor = cursor.get_next()

        return res

    def __len__(self):
        """ O(1) """
        return self.size

    def insert(self, idx, item):
        """
        TIME    : O(n)
        """
        if idx < 0 : raise('Index cannot be negative')
        if idx > self.size-1 : raise('Llist index out of range')
        # else
        _node = Node(item=item)

        # get prev node of idx
        cursor = self.first.get_next()
        for _ in range(0, idx-1): # -1: until prev 
            cursor = cursor.get_next()
        # 1
        _node.set_next(cursor.get_next())
        # 2
        cursor.set_next(_node)
        # 3
        self.size += 1

    def __delitem__(self, idx):
        """
        TIME    : O(n)
        """
        if idx < 0 : raise('Index cannot be negative')
        if idx > self.size-1 : raise('Llist index out of range')
        # else

        # get prev node of idx
        cursor = self.first.get_next()
        for _ in range(0, idx-1): # -1: until prev 
            cursor = cursor.get_next()
        
        next_node_of_idx = cursor.get_next().get_next()
        cursor.set_next(next_node_of_idx)
        self.size -= 1

    def __iter__(self):
        """
        TIME    : O(n)
        """
        cursor = self.first.get_next()

        while cursor is not None:
            yield cursor.get_item()
            cursor = cursor.get_next()

    def __eq__(self, other):
        """
        TIME    : O(n)
        """
        if type(self) != type(other) : return False
        if len(self) != len(other) : return False

        cursor1 = self.first.get_next()
        cursor2 = other.first.get_next()

        while cursor1 is not None:
            if cursor1.get_item() != cursor2.get_item():
                return False
            cursor1 = cursor1.get_next()
            cursor2 = cursor2.get_next()

        return True

    def __contains__(self, item):
        """
        TIME    : O(n)
        """
        cursor = self.first.get_next()
        while cursor is not None:
            if cursor.get_item() == item:
                return True
            cursor = cursor.get_next()
        return False

# ------------------------------------------------
# END
# ------------------------------------------------

if __name__ == "__main__":
    def print_head(head=''):
        len = 100
        print(f"\n{'+'*len}\n+ {head}\n{'+'*len}")

    # Tests
    # -----
    # 1. empty list
    l = Llist()
    print_head(l.__doc__)

    # 2. append
    print_head('2. Append')
    contents    = [9, -3, 495, -2, 0, 1]
    ll          = Llist(contents=contents)
    print('First Node: ', ll.first.get_next().item) # note
    print('Last Node: ', ll.last.item)
    print('Size of Llist: ', ll.size)

    # 3. get, set
    print_head('3. Indexed GET, SET')
    print('At index 5: ', ll[5])
    ll[5] = -99
    print('At index 5: ', ll[5])

    # 4. concat
    print_head('4. Concat (Add)')
    ll2 = Llist([1,2,3])
    res = ll+ll2
    for idx in range(0, len(res)):
        print(res[idx], end=",")

    # 5. insert, insert at (idx -1  idx 99)
    print_head('4. Insert')
    x = Llist([0,1,2,3,4,6,7])
    x.insert(5, 'x')

    for idx in range(0, len(x)):
        print(x[idx], end=",")

    # 6. delete, delete at (idx -1) 
    print_head('6. Delete')
    del x[5]
    for idx in range(0, len(x)):
        print(x[idx], end=",")

    # 7. iterator
    print_head('6. Iterator')
    test = Llist(['a', 'b', 'c', 'd'])
    for e in test:
        print(e, end=',')

    # 8. length
    print_head('8. Length')
    print('len: ', len(ll))

    # 9. equality
    print_head('9. Equality')
    a = Llist([0,2,5])
    b = Llist([0,2,5])
    c = Llist()
    d = Llist()
    e = Llist([2])
    print(a==b)
    print(c==d)
    print(a==e)
    print(c==e)

    # 10. search (contains)
    print_head('9. Contains')
    y = Llist([1,88,33,4,-6,7])
    print(2 in y)
    print(7 in y)