"""
BST
    - 
"""


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
        - __iter__          : (traverse tree) exploit mutually recursive iter in Node
                                    + Simply returns mutually recursive iterator() of root node

        - __contains__      : exploit iterator
        - __del__           : exploit iterator
    """
    def __init__(self, contents=[]):
        self.root = None

        for e in contents:
            self.insert(e)

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
            else: # accept duplicates too
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
     
    lst    = [1,4,-3,5,0] # only ordinal data. str not allowed
    bst    = BST(lst)

    # 1. iterator
    for e in bst:
        print(e) 