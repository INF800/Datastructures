# ======================================================================================================
# Breadth First Search - Graph
# ======================================================================================================
# i.   Can also be called, level order search or a bruteforce search. Used to find shorted path. For, larger graphs, pretty much useless
# ii.  Convert graph into a tree with any vtx as root in any order and perform BFS.
# iii. Analytically, there are `n` nodes. Thus, T.C is `n`. (Keeping QUEUE opns. and everything aside.) 

from utils import Queue
from itertools import permutations, combinations
import math

# Graph representation using adjacency matrix
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

        - __bfs_prev_node : helper for bfs action
        - __egde_memo     : helper memoisation for get_weight() method

    METHODS
        - add_vtx       : enter into vtx_map (done before adding edges)
        - add_edge      : enter into adj_list (alters Vertex instances)
        - display       : displays graph with help of static function

        - bfs           : bruteforce/levelorder/breadth-first-search
                            + uses Queue (Iterative)
                            + uses Set (for avoiding endless traversal)

        - get_weight                    : takes Vertex / vtxIds as input and gives edge weight
        - greedy_search_shortest_path   : of all perm-combns of paths, selects best path
                                            + not related to bfs
                                            + uses get_weight with memoisation for IDs only
    """
    def __init__(self):
        self.vtx_map = {}
        
        self.__bfs_prev_node = None # recording path length in bfs
        self.__egde_memo = {}

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
        for vtx_id in self.vtx_map.keys():
            neighbors = sorted(self.vtx_map[vtx_id].adj_list)
            for neighbor in neighbors:
                Graph.__print_graph(vtx_id, neighbor[0], neighbor[1])

    # ----------------------------------------------------------------------
    # BFS implementation
    # ----------------------------------------------------------------------
    def get_weight(self, from_vtx, to_vtx, ids_used=False):

        # ------------------------------------------
        # memoisation
        # ------------------------------------------
        if ids_used == True:
            if (from_vtx+to_vtx in self.__egde_memo):
                return self.__egde_memo[from_vtx+to_vtx]
        # else, populate memo
        # ------------------------------------------

        if ids_used==True: #from_vtx, to_vtx are ids not instances of Vertex
            neighbors   = self.vtx_map[from_vtx].adj_list
        else: # instances of Vertex
            neighbors = from_vtx.adj_list

        if from_vtx == to_vtx: return 0 # same vtxs i.e 0 dist        
        
        for id, w in neighbors:
            if not ids_used:
                if id==to_vtx.id: return w
            elif ids_used:
                self.__egde_memo[from_vtx+to_vtx] = w # populate 2of2
                if id==to_vtx: return w

        if ids_used: self.__egde_memo[from_vtx+to_vtx] = False # populate 1of2
        return False # indicate no edge

    @staticmethod
    def __action(goal, cur_vertex, graph):
        # prev node for wt.
        if graph.__bfs_prev_node is None: graph.__bfs_prev_node = cur_vertex

        # log info
        path_len = graph.get_weight(graph.__bfs_prev_node, cur_vertex)
        print(f"visited: {cur_vertex.id}", end="")
        print(f"\t edge({graph.__bfs_prev_node.id} -> {cur_vertex.id}): {path_len}") # note edge != shorted dist in any manner.

        # goal
        if cur_vertex.id == goal:
            print('Found. Path exists. Shortest Path? Use greedy search by taking all possible node edges')
            return True

        # update prev node
        graph.__bfs_prev_node = cur_vertex
        return False

    def bfs(self, start=None, goal=None):
        if start is None: first = self.vtx_map['A'] # can be random: random.choice(self.vtx_map.keys())
        else: first = self.vtx_map[start]
        found = False

        queue       = Queue([first]) #  instant opn: first-in, first-operated upon        
        visited     = set() # IDs of already visited to avoid

        while len(queue) != 0:

            cur_node = queue.dequeue()
            
            # note visited
            visited.add(cur_node.id)
            # exec action
            found = Graph.__action(goal, cur_node, self) # exects action as well
            if found: break
            # update queue
            for v_id, _ in cur_node.adj_list:
                if v_id not in visited: # if condn. must be placed here ONLY. 
                    queue.enqueue(self.vtx_map[v_id]) # in any random order

        # reach here after complete search / goal not found
        graph.__bfs_prev_node = None # reset
        if not found: print("Complete search done. Goal vtx not found")

    def greedy_search_shortest_path(self, start_id, end_id):
        """ No way related to bfs """
        all_nodes   = set(self.vtx_map.keys()) # randomized here (python default hashing)
        beg_node    = set([start_id])
        end_node    = set([end_id])
        mid_path0   = all_nodes - beg_node - end_node

        paths = []
        for num_nodes in range(0, len(mid_path0)+1):
            for comb in combinations(mid_path0, r=num_nodes):
                #print(comb) # if (a, b, c) present, (b, a, c) absent
                for perm in permutations(comb):
                    #print(perm) # # if (a, b, c) present, (b, a, c) present
                    paths.append( list(beg_node) + list(perm) + list(end_node) )

        min_edge_wt = math.inf
        best_path   = None
        for path in paths:
            sum_edge_wts = 0
            broken_or_small_path  = False

            # find length of individual edges in path, add them and select min
            for beg_edge_idx in range(0, len(path)-1, 2):
                end_edge_idx = beg_edge_idx + 1
                # use memoisation(for faster)
                edge_wt = graph.get_weight(path[beg_edge_idx], path[end_edge_idx], ids_used=True)
                sum_edge_wts += edge_wt
                if (edge_wt is False) or (sum_edge_wts>=min_edge_wt): broken_or_small_path=True; break # no edge connecting
            
            if broken_or_small_path: continue # reject path where one of edges is missing (or no path at all)
            
            if sum_edge_wts < min_edge_wt:
                min_edge_wt = sum_edge_wts
                best_path   = path
            #print(f"path: {path}, -------------> dist: {sum_edge_wts} \t best: {min_edge_wt}")

        
        print(f'best path: {best_path}, shortest dist: {min_edge_wt}')

if __name__ == '__main__':

    # -------------------------------------------------------------------
    # a. Get graph information
    # -------------------------------------------------------------------
    # can be json/xml
    graph_info = {
        "props": {
            "plot_dims"    : (100,100), #(width, height)
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
                "label" : 'Lanka',
                "coods" : (99, 99), #(x, y, width, height)
            }
        ],
        "edges" : [
            {"initial": 'A', 'terminal': 'B', 'weight': 100},
            {"initial": 'A', 'terminal': 'D', 'weight': 10},
            {"initial": 'B', 'terminal': 'A', 'weight': 50},
            {"initial": 'A', 'terminal': 'C', 'weight': 100},
            {"initial": 'B', 'terminal': 'D', 'weight': 100},
            {"initial": 'C', 'terminal': 'A', 'weight': 16},
            {"initial": 'D', 'terminal': 'E', 'weight': 16},
        ]
    }

    # -------------------------------------------------------------------
    # b. Use graph information to build graph
    # -------------------------------------------------------------------
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

    # -------------------------------------------------------------------
    # c. BFS & shortest path(greedy search - not related to BFS)
    # -------------------------------------------------------------------
    graph.bfs(goal='T'); print("="*100) 
    graph.bfs(goal='C'); print("="*100)
    
    # Shortest Path? Use greedy search by taking all possible node edges
    graph.bfs(start='B', goal='C');                                 print("="*100)
    graph.greedy_search_shortest_path(start_id='C', end_id='E');    print("="*100)
    graph.greedy_search_shortest_path(start_id='A', end_id='E');    print("="*100)
    graph.greedy_search_shortest_path(start_id='E', end_id='B');    print("="*100)
    graph.greedy_search_shortest_path(start_id='D', end_id='A');    print("="*100)




