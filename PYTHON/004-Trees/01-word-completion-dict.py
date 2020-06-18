
class Node:
    def __init__(self, val, rank=None, child_node=None, ht=None):
        self.val        = val 
        self.rank       = rank
        self.children   = {}
        self._ht        = ht
        self._add_child(child_node)
        
    def _add_child(self, child_node):
        if child_node is not None:
            # checks for dups as well! Inserts if new
            self.children[child_node.val] = child_node

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        # without this if condn, we will overwite our root
        if not self.root:
            self.root = self.__grow_tree(data)
        #else
        self.root._add_child(self.__grow_tree(data))

    def __grow_tree(self, data, height=0):
        # base cond.
        if height == len(data[0])-1:
            val = data[0][height]
            rank = data[1]
            return Node(val, rank, None, ht=height)
        
        val         = data[0][height]
        rank        = 'mbwi' # `mentioned below. word incomplete`
        child_node  = self.__grow_tree(data, height=height+1)

        # Node(val, rank, Node(val, rank, Node(val, rank, ...Node(val, rank, None))))
        return Node(val, rank, child_node, ht=height)

    def traverse_tree(self):
        self.__traverse(self.root)

    def __traverse(self, node):
        #base 
        if node.children == {}:
            # ---------------[start action]-------------------------
            spaces      = (" "*node._ht) * 3
            prefix      = spaces + "|__"
            info        = prefix + node.val
            print(info, node.rank)
            # ------------------[end action]-------------------------
            return

        # ---------------[ actions start ]----------------------
        spaces      = (" "*node._ht) * 3
        prefix      = spaces + "|__"
        info        = prefix + node.val
        print(info, node.rank)
        # ------------------[end action]-------------------------
        for child_node in node.children:
            self.__traverse(node.children[child_node])


if __name__ == '__main__':
    data = [
    'the',
    'of',
    'and',
    'to',
    'a',
    'in',
    'then',
    'thein',
    'their',
    'therein',
    'theinger',

    ]

    words = []
    for rank, word in enumerate(data):
        words.append((word, rank))

    print(words)

    _data1 = ('and', 3)
    _data2 = ('ant', 5)
    _data3 = ('then', 1)
    _data4 = ('the', 0)

    
    # tree
    t = Tree()
    t.insert(_data1)
    t.insert(_data2)
    t.insert(_data4)
    t.insert(_data3)
    root = t.root
    t.traverse_tree()
    
    #1. problem1 : compare res - insert `data3` before `data4` (see ranks and disappearing `then`)
    #2. pr0blem2 : add all _data in word using loo and check results
    #3.             soln: rewrite rank with the snallest