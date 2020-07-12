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

        - __iter__      : inorder traversal (in this way we get ASCENDING ORDER!) 
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
        '''
        # 1. left
        if self.left is not None:
            #yield left.data ? No! use recursive
            for item in self.left: # (NOT)same iterator being called on left
                yield item

        # 2. self
        yield self.item

        # 3. right
        if self.right is not None:
            #yield right.data ? No! use recursive
            for item in self.right: # (NOT)same iterator being called on left
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
# END CLASS NODE
# --------------------------------------------------------------------------------------------------------


class BST:
    """ Binary Search Tree
    DATA MEMBERS
        - root      : holds root node

    METHODS
        - buld tree
        - traverse tree
        - delete item
    """
    def __init__(self):
        self.root = None