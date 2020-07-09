from utility import Queue

class PlusNode:
    def __init__(self, left, right):
        """No data. Only addresses"""
        self.left   = left
        self.right  = right
    
    def evaluate(self):
        # inorder traversal for infix expression:
        # goes until leaf and fetches value (num node)
        # then performs addition
        return self.left.evaluate() + self.right.evaluate()

    def inorder(self):
        # same as evaluate(INFIX) but returns inorder string:
        return f'({self.left.inorder()} + {self.right.inorder()})'

    def postorder(self):
        # returns postorder string:
        # Suitable for STACK IMPLEMENTATION
        return f'({self.left.postorder()} {self.right.postorder()} +)'

    def preorder(self):
        # returns preorder string:
        # DOESNT NEED PARENTHESIS
        return f'+ {self.left.preorder()} {self.right.preorder()}'

class TimesNode:
    def __init__(self, left, right):
        """No data. Only addresses"""
        self.left   = left
        self.right  = right

    def evaluate(self):
        # inorder traversal for infix expression:
        # goes until leaf and fetches value (num node)
        # then performs multn.
        return self.left.evaluate() * self.right.evaluate()
    
    def inorder(self):
        # same as evaluate(INFIX) but returns inorder string:
        return f'({self.left.inorder()} x {self.right.inorder()})'

    def postorder(self):
        # returns postorder string:
        # Suitable for STACK IMPLEMENTATION
        return f'({self.left.postorder()} {self.right.postorder()} x)'

    def preorder(self):
        # returns preorder string:
        # DOESNT NEED PARENTHESIS
        return f'x {self.left.preorder()} {self.right.preorder()}'


class NumNode:
    def __init__(self, num):
        """only data - leaf node - always retuns data"""
        self.num   = num

    def evaluate(self):
        return self.num

    def inorder(self):
        return self.num

    def postorder(self):
        return self.num
    
    def preorder(self):
        return self.num

class Tree:
    def __init__(self, cfg_list=[]):
        """Input is prefix grammar (CFG) with token in a 1-D list"""
        self.root   = None
        self.q      = Queue(cfg_list)

    def build_tree(self):
        self.root = self.E(self.q)

    def E(self, q):
        """ Parser Function 
        - token can be either of three
            + number :   (always return) - Note: this is base condn and is at end just as a trick. not cz, top-down construction
            + '+'    :   (recur call - with specific class)
            + '*'    :   (recur call - with specific class)

        Note: We use a top-down construction
        """
        # get token
        token = q.dequeue()

        if token == '+':
            return PlusNode(self.E(q), self.E(q))
        if token == 'x':
            return TimesNode(self.E(q), self.E(q))

        # base condn (same as writing on top)
        return NumNode(float(token))

if __name__ == '__main__':
    # AST for: (5+4) * 6 - 3
    # Note: even for subtraction we use PlusNode

    # build tree: bottom to up (direct)
    add = PlusNode( NumNode(5), NumNode(4) )
    mul = TimesNode( add, NumNode(6) )
    sub = PlusNode( mul, NumNode(-3))
    root = sub

    # build tree: (dynamically using list/stack/queue)
    # arr = ['5', '+', '4', '*', '6', '-', '3']
    # constructed by interpreter/compiler (generally called parser)
    # --------------------------------------------------------------
    # We will implement prefix grammar parser as it doesn't need any
    # paranthesis and can be simply implemented using queue
    tree = Tree(['+', 'x', '+', '5', '4', '6', '-3']) 
    tree.build_tree()

    # traverse tree: 
    # all implementation are same uisng mutually recursive funcs
    print('+'*100)
    print(f'value of AST is: {root.evaluate()} (infix/inorder)') 
    print('+'*100)
    print(f'str rep of AST(inorder): \t {root.inorder()}')
    print(f'str rep of AST(postorder): \t {root.postorder()} \t [IMPLEMENTED USING STACK]')
    print(f'str rep of AST(preorder): \t {root.preorder()} \t [DOESNT NEED PARENTHESIS]')
    print('+'*100)
    print(f'Built tree using CFG(prefix expr): {tree.root.inorder()} val: {tree.root.evaluate()}')
    print('+'*100)
