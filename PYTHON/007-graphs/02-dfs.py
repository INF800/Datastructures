# ======================================================================================================
# Depth First Search - Graph
# ======================================================================================================
# - Same as pre-order traversal or can use recursion or stack.
# - Stack is used so that we can 
#       + suspend last_prev and
#       + work with most-recent-prev-node.
# - This is not greedy search. Makes mistakes and reaches goal (called ...)
# cannot be used to find 'shortest' path; But finds path

# using adj_list representation
from utils import Stack

class Vertex:
    """
    DATA MEMBERS
        - id         : unique id
        - coods      : (x, y, w, h) co-ordinates for plotting
        - prev       : needed?
        - adj_list   : [Most improtant] List of all neighbours IDs as str w/ weights

    METHODS
        - add_neighbour     : Vertex addr and edge wight as input, populates adj_list 
    """
    
    def __init__(self, id, label=None, coods=(None, None)):
        self.id         = id
        self.adj_list   = []

        self.coods      = coods
        self.label      = label

    def add_neighbour(self, vtx_id, wt):

        if vtx_id not in self.adj_list:
            self.adj_list.append((vtx_id, wt))
            # sort later
        #else, do nothing

class Graph:
    """
    DATA MEMBERS
        - vtx_map       : map vtx IDs to Vertex instances

    METHODS
        - add_vtx       : enter into vtx_map
        - add_edge      : enter into adj_list (alters Vertex instnces)
        - print_graph
    """
    def __init__(self):
        self.vtx_map = {}

    def add_vtx(self, vtx):
        if type(vtx) != Vertex : raise('Type mismatch')
        
        if vtx.id not in self.vtx_map:
            self.vtx_map[vtx.id] = vtx

    def add_edge(self, u, v, w=0, directed=False):
        """ 
            - Run this only after adding vertices using
            - u, v are IDs not vtx objs
            - Note:
                + Directed      : u -> v
                + Undirected    : u - v
        """
        # assuming vertices are already present
        if (u in self.vtx_map) and (v in self.vtx_map): # both must be true
            if directed is False:
                self.vtx_map[u].add_neighbour(v, w) # u - v
                self.vtx_map[v].add_neighbour(u, w) # v - u
            if directed is True:
                self.vtx_map[u].add_neighbour(v, w) # u -> v


    @staticmethod
    def __print_graph(from_vtx, to_vtx, weight):
        print(f"{from_vtx} -------------[{weight}]-----------> {to_vtx}")

    def display(self):
        print('\nNodes: ', self.vtx_map.keys())

        for vtx_id in self.vtx_map.keys():
            neighbors = sorted(self.vtx_map[vtx_id].adj_list)
            for neighbor in neighbors:
                Graph.__print_graph(vtx_id, neighbor[0], neighbor[1])

    # -----------------------------------------------
    # DFS
    # -----------------------------------------------
    @staticmethod
    def __disp_list(path):
        """ path is list if ids """
        if path is False: print('Empty'); return

        # else,
        for _id in path:
            print(_id, end=" <- -> ")
        print('(Paths can go backwards too)')
            

    @staticmethod # Iterative approach
    def __dfs(graph, beg_id, goal):
        """ returns path if present else false"""
        first   = graph.vtx_map[beg_id]
        stack   = Stack([first])
        visited = set([first.id])

        path = [first.id]

        while len(stack) != 0:
            # explore: (Not unique. Goes through all nodes until goal)
            recent_prev_node = stack.pop()

            neighbors = recent_prev_node.adj_list
            for v_id, _ in neighbors:
                if v_id not in visited:
                    # visit: (always unique)
                    # update visited and stack
                    stack.push(graph.vtx_map[v_id])
                    visited.add(v_id)

                    # action
                    path.append(v_id)
                    #if v_id == goal:
                    #    return path

        # reaches here if goal not found
        return path

    @staticmethod # recursive approach
    def __dfs_recursive(graph, beg_id, goal):
        path    = []
        visited = set()

        # full traversal. Break for goal?
        def preorder(cur_node):
            """ 
            - For pre-order action is done while calling time
            - For post-order action is done while returning time
            """
            # action (while calling time)
            path.append(cur_node.id)
            visited.add(cur_node.id)
            
            # check goal

            for neighbor_id, _ in cur_node.adj_list:
                # base condn.
                if neighbor_id not in visited:
                    preorder(graph.vtx_map[neighbor_id])

        # preorder traversal
        # populates global path
        preorder(graph.vtx_map[beg_id])
        return path


    @staticmethod # recursive approach
    def __dfs_possible_paths(graph, beg_id, end_id):
        """ exponential time complexity - EXHAUSTIVE SEARCH """
        print('possible paths (recursive approach):')

        def _bfs_paths(cur_id, goal_id, path):
            """ preorder (action while calling time) """
            # action
            path.append(cur_id)
            if cur_id == goal_id:
                print(f'\t+ path found to {cur_id}: {path}')
                return # impt.

            for neigh_id, _ in graph.vtx_map[cur_id].adj_list:
                # base
                if neigh_id not in visited:
                    visited.add(neigh_id)
                    _bfs_paths(neigh_id, goal_id, path)
                
                    # at end of recursion (when returns) step back one step and start searching
                    # again. Stepping back is done by next two lines.
                    # reaches here when 1. possible path ends or 2. cur id is found  
                    visited.remove(neigh_id)
                    path.pop()

        # recur 
        visited = set(beg_id)
        _bfs_paths(beg_id, end_id, [])


    @staticmethod
    def __dfs_possible_paths_i(graph, beg_id, end_id):
        print('possible paths (iterative approach): ')

        first   = graph.vtx_map[beg_id]
        stack   = Stack([first.id])
        visited = set([first.id]) 

        path = [first.id]

        while len(stack) != 0:
            # explore
            cur_id = stack.pop()

            # visit
            neighbors = graph.vtx_map[cur_id].adj_list
            for neigh_id, _ in neighbors:
                if neigh_id not in visited:
                    # update
                    visited.add(neigh_id)
                    stack.push(neigh_id)

                    # action
                    path.append(neigh_id)
                    if neigh_id == end_id:
                        print(f'\t+ path found to {end_id}: {path}')

                        # Is it even 
                        #
                        # Possible?


        #print(path)


    def dfs(self, beg_id, end_id):
        if (beg_id not in self.vtx_map) and (end_id not in self.vtx_map):
            print('nodes missing')
            return

        # regular dfs search (iterative) - full traversal
        path = Graph.__dfs(graph=self, beg_id=beg_id, goal=end_id)
        Graph.__disp_list(path)
        # regular dfs search (recursive) - full traversal
        path_r = Graph.__dfs_recursive(graph=self, beg_id=beg_id, goal=end_id)
        Graph.__disp_list(path_r) # path never false

        # dfs to get all possible paths (recursive)
        Graph.__dfs_possible_paths(graph=self, beg_id=beg_id, end_id=end_id)
        # dfs to get all possible paths (iterative)
        # not working how?
        Graph.__dfs_possible_paths_i(graph=self, beg_id=beg_id, end_id=end_id)


# ---------------------------------------------------------------
# Main
# ---------------------------------------------------------------
if __name__ == '__main__':
    # can be json/xml
    graph_info = {
        "props": {
            "plot_dims"    : (100,100),
            "directed"     : True,
            "weighted"     : True
        },
        "vertices": [
            {
                "id"    : 'A',
                "label" : 'India',
                "coods" : (10, 10), #(x, y, width, height)
            },{
                "id"    : 'B',
                "label" : 'China',
                "coods" : (10, 20), #(x, y, width, height)
            },{
                "id"    : 'C',
                "label" : 'USA',
                "coods" : (50, 20), #(x, y, width, height)
            },{
                "id"    : 'D',
                "label" : 'Italy',
                "coods" : (50, 50), #(x, y, width, height)
            },{
                "id"    : 'E',
                "label" : 'England',
                "coods" : (10, 90), #(x, y, width, height)
            }
        ],
        "edges" : [
            {"initial": 'A', 'terminal': 'B', 'weight': 100},
            {"initial": 'A', 'terminal': 'D', 'weight': 10},
            {"initial": 'B', 'terminal': 'A', 'weight': 50},
            {"initial": 'A', 'terminal': 'C', 'weight': 100},
            {"initial": 'B', 'terminal': 'D', 'weight': 100},
            {"initial": 'C', 'terminal': 'D', 'weight': 70},
            {"initial": 'D', 'terminal': 'E', 'weight': 7},
            {"initial": 'E', 'terminal': 'A', 'weight': 30},
        ]
    }

    graph = Graph()

    # Build graph - 1of2 - populate vertices
    for vtx_info in graph_info['vertices']:
        vtx = Vertex( id=vtx_info['id'], label=vtx_info['label'], coods=vtx_info['coods']) 
        graph.add_vtx( vtx )

    # Build graph - 2of2 - add edges (make connections)
    for edge_info in graph_info['edges']:
        graph.add_edge(
            u           = edge_info['initial'],
            v           = edge_info['terminal'],
            w           = edge_info['weight'],
            directed    = graph_info['props']['directed']
        )
    
    # print graph
    graph.display()

    # ---------------------------------------------------------------
    # DFS
    # ---------------------------------------------------------------
    graph.dfs(beg_id='A', end_id='D');                  print("="*100)
    # note: BDEADC is not printed in below dfs cz, d occurs 2 times
    graph.dfs(beg_id='B', end_id='C');                  print("="*100)
    graph.dfs(beg_id='B', end_id='X');                  print("="*100)