class Node:
    def __init__(self, val=None, left=None, right=None, height=None):
        self.val        = val
        self.right      = right
        self.left       = left
        self.isLeaf     = (self.right is None) and (self.left is None)
        self.height     = height

class Tree:
    """
    DATA MEMBERS:   
        - root      : it will hold all node classes

    METHODS:
        - build tree (builds tree(root) recursively)
            - creates `root`
            - utilizes `grow_tree` (with depth(int) param cntr)
                - always returns the node it created
        - traverse tree
            - traverses `root` recursively
                - utilizes `_traverse`
    """

    def __init__(self, max_ht=4):
        self.root       = None
        self.max_ht     = max_ht

    def build_tree(self):
        self.root = self.__grow_tree("I am root")
        
    def traverse_tree(self):
        self._traverse(self.root)


    def __grow_tree(self, val=None, depth=0):
        # base condition
        if depth == self.max_ht:
            return Node(f"I am leaf at ht. {depth}", None, None, height=depth)
        
        # else, build trees recursively by returning nodes into parent nodes.
        # In the end, all nodes will be returned to parent of all - root.
        # Imagine all individual parent-child group as a tree which will be 
        # built by `__grow_tree`
        left    = self.__grow_tree(f"I am node at ht. {depth+1}", depth=depth+1)
        right   = self.__grow_tree(f"I am node at ht. {depth+1}", depth=depth+1)
        return Node(val, left=left, right=right, height=depth)

    def _traverse(self, node):
        # base condn.
        if node.isLeaf:
            # action -------------------------------------------------> common to all pre, post & in-fix
            spaces      = (" "*node.height) * 3
            prefix      = spaces + "|__"
            info        = prefix + node.val
            print(info)
            # end action
            return

        # else, perform action & traverse tree recursively.
        # ==================================================

        #perform action(here) -----------------------------------------> pre order
        spaces      = (" "*node.height) * 3
        prefix      = spaces + "|__"
        info        = prefix + node.val
        print(info)
        # end action

        # Traverse recursively.
        self._traverse(node.left)
        # perform action(here) ----------------------------------------> in order
        self._traverse(node.right)
        # perform action(here) ----------------------------------------> post order

if __name__ == "__main__":
    my_tree = Tree(max_ht=2)
    # build tree with hardcoded values
    my_tree.build_tree()
    # print results
    my_tree.traverse_tree()