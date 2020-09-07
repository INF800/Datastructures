from collections import namedtuple
from operator import itemgetter
from pprint import pformat

class KDTree:
    # ================================================================
    # Node representation (recursive) used in get_tree()
    # ================================================================
    class __Node(namedtuple('Node', 'location left_child right_child')):
        def __repr__(self):
            return pformat(tuple(self))


    # ================================================================
    # Constructor
    # ================================================================
    def __init__(self, point_list):
        self.root = self.build_kdtree(point_list)

    # ================================================================
    # get tree
    # ================================================================
    def get_root(self):
        """ 
        + Return root node of type KNN.__Node
        + Prints __repr__ recursively on print()
        """   
        return self.root

    # ================================================================
    # traverse tree
    # ================================================================
    def dfs(self):
        def __prefix_action(node, depth):
            pre = (("|" + "   "*len(node.location))*depth) + ("|___")
            print(pre + str(node.location))

        def __dfs(node, depth: int = 0):
            # base condition:
            if node is None: return
            
            __prefix_action(node, depth)
            __dfs(node.left_child, depth=depth+1)
            __dfs(node.right_child, depth=depth+1)
        
        # start recursion
        __dfs(self.root)

    # ================================================================
    # build tree (prefix)
    # ================================================================
    def build_kdtree(self, point_list, depth: int = 0):
        # base:
        if not point_list:
            return None

        # params:
        k = len(point_list[0]) # assumes all points have the same dimension
        # Select axis based on depth so that axis cycles through all valid values
        axis = depth % k # 0, 1, 2, 0 ...
    
        # compute median:
        # Sort point list by axis and choose median as pivot element
        point_list.sort(key=itemgetter(axis))
        med_idx = len(point_list) // 2
    
        # Create node and construct subtrees
        return KDTree.__Node(
            location      = point_list[med_idx], 
            left_child    = self.build_kdtree(point_list[:med_idx], depth + 1),
            right_child   = self.build_kdtree(point_list[med_idx + 1:], depth + 1)
        )


def main():
    """Example usage"""
    point_list = [(7,2), (5,4), (9,6), (4,7), (8,1), (2,3)]
    tree = KDTree(point_list)

    print("="*100)
    print(tree.get_root())

    print("="*100)
    tree.dfs()


if __name__ == '__main__':
    main()
