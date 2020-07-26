# ======================================================================================================
# Trie Data Structure
# ======================================================================================================
# - only membership(retrieval) test. Cannot be used for deletion
# - Can suggest alternatives unlike bloom filter's only True/False output
#       + But bloom filters are clearly Faster!
#       + Trie takes more space (ironic to T-S-Complexity) 
# - Implementation using linked list of linked lists. Same can be done using
#       + Sparse matrix
#       + Trie Tree  

class TrieNode:
    """
    DATA MEMBERS
        - val       : unit of the key
        - next      : node addr of succesive unit of the same key as `val`
        - follows   : node addr of succesive unit of difft. key
    """
    def __init__(self, unit, next=None, follows=None):
        self.val        = unit
        self.next       = next
        self.follows    = follows
    # end def __init__
# end class Node


class Trie:
    """
    DATA MEMBERS
        - root      : like root of tree. denotes starting point

    METHODS
        - insert    : recursive. can be done iteratively too.
        - contains  : recursive  
    """

    def __init__(self, contents=[]):
        self.root = None

        for __key in contents:
            self.insert(__key)


    def insert(self, key):
        """
        - recursively insert into linked list of linked lists
        """
        def __insert(node, item, depth=0):
            # base (consistent w/ all cases below)
            if len(item) == depth:
                return None
            
            # for `none` root
            if node is None:
                node = TrieNode(item[depth])

            # follow - if val already exists (recursively)
            # else, next - if new
            if node.val == item[depth]:
                node.follows = __insert(node, item, depth=depth+1)
            else:
                node.next = __insert(node, item, depth=depth+1)



        # recur 
        self.root = __insert(self.root, key)


    def __contains__(self, key):
        """
        - recursively check membership
        """
        pass