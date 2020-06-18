data = [
    'then',
    'thein',
    'their',
    'therein',
    'theinger'
]

words = []
for rank, word in enumerate(data):
    words.append((word, rank))

print(words)

class Node:
    def __init__(self, val=None, rank=None, child_node=None, depth=None):
        self.val    = val
        self.rank   = rank
        self.children = [] # same as none
        self.depth = depth
        self.add_child(child_node)
    
    def add_child(self, child_node):
        if child_node is None:
            return
        if not self.children:
            self.children.append(child_node)
        # check duplicates
        unique = True
        for _node in self.children:
            if _node.val == child_node.val:
                unique = False
                break
        if unique:
            self.children.append(child_node)

class Tree:
    def __init__(self):
        self.root = None
    
    def buid_tree(self, data):
        """data is tuple of string to be added and rank of string eg. ('then', 32)"""
        # we are overwriting!
        # it should be if not: ..below line.. else self.root.__Addchild(__build(data))
        self.root = self.__build(data)

    def __build(self, data, height=0):
        # base
        if height==len(data[0])-1:
            val     = data[0][height]
            rank    = data[1] if (height == len(data[0]) - 1) else None
            return Node(val, rank, None, depth=height)

        val     = data[0][height]
        rank    = height if height == len(data[0]) else None
        
        child_node = self.__build(data, height+1) 
        
        # Node(val, rank, Node(val, rank, Node(val, rank, ...Node(val, rank, None))))
        return Node(val, rank, child_node, depth=height)

    def traverse_tree(self, data=None):
        self._traverse(self.root)

    def _traverse(self, node):
        # base
        if node.children == []:
            # ---------------[start action]-------------------------
            spaces      = (" "*node.depth) * 3
            prefix      = spaces + "|__"
            info        = prefix + node.val
            print(info, node.rank)
            # ------------------[end action]-------------------------
            return
        
        # ---------------[ actions start ]----------------------
        spaces      = (" "*node.depth) * 3
        prefix      = spaces + "|__"
        info        = prefix + node.val
        # ------------------[end action]-------------------------
        print(info, node.rank)
        for child_node in node.children:
            self._traverse(child_node)



if __name__ == "__main__":
    data = [('then', 0), ('thein', 1), ('their', 2), ('therein', 3), ('theinger', 4)]
    
    _data = ('then', 0)

    tree = Tree()
    tree.buid_tree(data=_data)
    root = tree.root


    print('\M')
    tree.traverse_tree()


    