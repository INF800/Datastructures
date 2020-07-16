class Node:
    """ Node (of BST)
    DATA MEMBERS  
        - item      : value  of node
        - left      : addr of left node (left.item < parent.item)
        - right     : addr of right node (right.item >= parent.item)

    METHODS
        - getitem
        - setitem
        - getleft
        - setleft
        - getright
        - setright

        - __iter__      : IN-ORDER traversal (in this way we get ASCENDING ORDER!) 
                            + Note: Implementation - In a node! not in a tree!
    """
    def __init__(self, item=None, left=None, right=None):
        self.item       = item
        self.right      = right
        self.left       = left

    def __iter__(self):
        ''' 
        - (Ascending - cz inorder)Implemented at node level. 
        - Just have to yield this node's data? No!

        INORDER TRAVERSAL
            - check if children avl.
            - recur in in asc. order
        '''
        # 1. left
        if self.left is not None:
            #yield left.data ? No! use recursive
            for item in self.left: # recursive iterator being called on left (for self.left's left and right)
                yield item

        # 2. self
        yield self.item
        
        # 3. right
        if self.right is not None:
            #yield right.data ? No! use recursive
            for item in self.right: # recursive iterator called on left (for self.right's left and right)
                yield item

    def get_item(self):
        return self.item

    def set_item(self, e):
        self.item = e

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def set_left(self, e):
        self.left = e

    def set_right(self, e):
        self.right = e

# --------------------------------------------------------------------------------------------------------
# END CLASS NODE (for BST)
# --------------------------------------------------------------------------------------------------------


class BST:
    """ Binary Search Tree
    DATA MEMBERS
        - root      : holds root node

    METHODS
        - insert            : (build tree) appends ele to tree using @staticmethod __insert(node, ele)
        - insert_unique     : (build tree) same as above but only unique values (CAN BE USED FOR INDEXED SEARCH)
        - __iter__          : (traverse tree) exploit mutually recursive iter in Node
                                    + Simply returns mutually recursive iterator() of root node
        - __contains__      : exploit iterator
        - __del__           : key is to get prev node
    """
    def __init__(self, contents=[], unique=False):
        self.root = None
        
        self.is_unique = True if unique is True else False

        for e in contents:
            if unique == False:
                self.insert(e)
            elif unique==True:
                self.insert_unique(e)

    def insert(self, ele):
        """ Accepts duplicates """

        def __insert(node, e):
            """
            - if node is empty, append new node w/ e
            - if not empty, recursive call (in-order asc.)
            """
            if node == None: return Node(item=e) # return 1of2

            # else,
            if e < node.get_item():
                node.set_left( __insert(node.get_left(), e) )
            else: # accept duplicates too by creating new node for them on right
                node.set_right( __insert(node.get_right(), e) )

            return node # return 2of2
        # end def __insert

        # append / insert to root
        self.root = __insert(self.root, ele)

    def insert_unique(self, ele):
        """ Accepts duplicates """

        def __insert(node, e):
            """
            - if node is empty, append new node w/ e
            - if not empty, recursive call (in-order asc.)
            """
            if node == None: return Node(item=e) # return 1of2

            # else,
            if e < node.get_item():
                node.set_left( __insert(node.get_left(), e) )
            
            # detect dups if wanted
            # if node.get_item() == e: pass # do nothing, or log dups
            if node.get_item() == e: print('duplicate: ', e)

            if e > node.get_item(): # accept duplicates too
                node.set_right( __insert(node.get_right(), e) )

            return node # return 2of2
        # end def __insert

        # append / insert to root
        self.root = __insert(self.root, ele)

    def __iter__(self):
        if self.root == None: return [].__iter__() # same as None
        # else,
        return self.root.__iter__()

# --------------------------------------------------------------------------------------------------------
# END CLASS BST
# --------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    def print_line(head='',s='+', x=100): 
        print('\n')
        print(s*x)
        print('+ '+head)
        print(s*x)
     
    lst = [1,0,4,-3,1,5,0] # only ordinal data. str not allowed. 

    # 1. test insert()
    print_line('1. test insert()')
    bst = BST(lst)

    # 2. test iterator
    print_line('2. test iterator')
    for e in bst:
        print(e, end=' ') 

    # 3. test unique bst
    print_line('3. test unique bst')
    bst2 = BST(lst, unique=True)
    for e in bst2:
        print(e, end=' ') 

    # 4. delete
    pass
