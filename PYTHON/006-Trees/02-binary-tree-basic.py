from utility import Queue, Stack

class Node:
    def __init__(self, val=None, left=None, right=None, height=None):
        self.val        = val
        self.right      = right
        self.left       = left
        self.isLeaf     = (self.right is None) and (self.left is None)
        self.height     = height
    
    def get_val(self):
        return self.val
    
    def get_left(self):
        return self.left    
    
    def get_right(self):
        return self.right
    # --------------------------------------------------------------------------
    def traverse_preorder(self):
        '''
        Traverse in preorder (mutually recursive funcs)
        recur(self) -> recur(left) -> recur(right)
        '''
        # base condition
        if self.isLeaf == True: return self.prefix() + self.val
        
        # else recur into base
        # recur(self) -> recur(left) -> recur(right)
        cur_val     = self.prefix() + self.val
        left_val    = self.left.traverse_preorder()
        right_val   = self.right.traverse_preorder()
        return f'{cur_val}\n{left_val}\n{right_val}'

    def prefix(self):
        return  (self.height * (' '*3)) + '|___'

    # --------------------------------------------------------------------------
    def traverse_inorder(self):
        '''
        Traverse in inorder (mutually recursive funcs)
        recur(left) -> recur(self) -> recur(right)
        '''
        # base condition
        if self.isLeaf == True: return self.prefix2() + self.val

        left_val    = self.left.traverse_inorder() 
        cur_val     = self.prefix2() + self.val 
        right_val   = self.right.traverse_inorder()
        return f'{left_val}\n{cur_val}\n{right_val}'

    def prefix2(self):
        '''Note: prefixes are just for indendation!'''
        if self.height == 0 : return ''
        return ((self.height-1) * (' '*3)) + '  |---'

    # --------------------------------------------------------------------------
    def traverse_postorder(self):
        '''
        Traverse in postorder (mutually recursive funcs)
        recur(left) -> recur(rigt) -> recur(self)
        '''
        # base condition
        if self.isLeaf == True: return self.prefix3() + self.val

        left_val    = self.left.traverse_postorder()
        right_val   = self.right.traverse_postorder() 
        cur_val     = self.prefix3() + self.val 
        return f'{left_val}\n{right_val}\n{cur_val}'

    def prefix3(self):
        return  (self.height * (' '*3)) + '|˜˜˜'


# ------------------------------------------------------------------------
# Tree class
# ------------------------------------------------------------------------

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
            # exta action for node (not needed in mutually recursive functions)
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
        # --> perform action(here) ----------------------------------------> in order
        '''
        spaces      = (" "*node.height) * 3
        prefix      = spaces + "|__"
        info        = prefix + node.val
        print(info)
        # end action
        '''
        self._traverse(node.right)
        # --> perform action(here) ----------------------------------------> post order
        '''
        spaces      = (" "*node.height) * 3
        prefix      = spaces + "|__"
        info        = prefix + node.val
        print(info)
        # end action
        '''

    # --------------------------------------------------------------------------
    # BFS: Level order traversal
    # --------------------------------------------------------------------------
    @staticmethod
    def __action(node):
        """ Define operaton  to perform on any node (including leaf)"""
        print(f">> {node.get_val()}")

    def traverse_bfs(self, iterative=True):
        """ LEVEL-ORDER
        ITERATTIVE 
            - use queue
            - enqueue root to empty queue
            - until queue is not empty
                - deque and preform action on returned node (cur_node)
                - enqueue children of cur_node to same queue
        """
        if self.root is None:
            raise("Tree empty!")
        #else,
        if iterative == True:
            # Level order traversal (ITERATIVE METHOD)
            # ----------------------------------------
            first = self.root
            queue = Queue([first])

            while len(queue) != 0:
    
                # 1.get foremost from queue
                cur_node = queue.dequeue()
                
                # 2.action:
                Tree.__action(cur_node)

                # 3.update queue (can do it using for loop (multiple children))
                if cur_node.get_left()  is not None: queue.enqueue(cur_node.get_left())
                if cur_node.get_right() is not None: queue.enqueue(cur_node.get_right( ))
            
    # --------------------------------------------------------------------------
    # DFS
    # --------------------------------------------------------------------------
    def traverse_dfs(self, iterative=True):
        if self.root is None:
            raise("Tree empty!")
        #else,
        if iterative == True:

            # DFS search traversal (ITERATIVE METHOD)
            # ----------------------------------------
            first = self.root
            stack = Stack([first])

            while len(stack) != 0:
                # 1. get node
                cur_node = stack.pop()

                # 2. action
                Tree.__action(cur_node)

                # 3.update stack (can do it using for loop (multiple children))
                if cur_node.get_left()  is not None: stack.push(cur_node.get_left())
                if cur_node.get_right() is not None: stack.push(cur_node.get_right( ))

        if iterative == False:
            
            # DFS search traversal (RECURSIVE METHOD)
            # ----------------------------------------
            def __dfs(node):
                """ Same as pre-order traversal """
                # 1. action
                Tree.__action(node)

                # 2. base condn (not at beg s.t action called only once)
                if node.get_left() is not None  : __dfs(node.get_left())
                if node.get_right() is not None : __dfs(node.get_right())

            # call recursive func
            __dfs(self.root)

if __name__ == "__main__":
    # create tree
    my_tree = Tree(max_ht=2) # ht=2

    # build tree with hardcoded values
    my_tree.build_tree()
    
    # traverse tree
    my_tree.traverse_tree() # pre/in/post-order using non-mutual recur funcs

    print("", "","+"*100, 'TESTING MUTUALLY RECURSIVE TRAVERSAL FUNCS', "+"*100, sep="\n",end='\n\n')
    print(my_tree.root.traverse_preorder(), end='\n\n')
    print(my_tree.root.traverse_inorder(), end='\n\n')
    print(my_tree.root.traverse_postorder(), end='\n\n')

    print("", "","+"*100, 'TESTING  BFS: LEVEL ORDER TRAVERSAL (ITERATIVE)', "+"*100, sep="\n",end='\n\n')
    my_tree.traverse_bfs()
    
    print("", "","+"*100, 'TESTING  DFS TRAVERSAL (ITERATIVE)', "+"*100, sep="\n",end='\n\n')
    my_tree.traverse_dfs()

    print("", "","+"*100, 'TESTING  DFS TRAVERSAL (RECURSION)', "+"*100, sep="\n",end='\n\n')
    my_tree.traverse_dfs(iterative=False) # same as preorder traversal
