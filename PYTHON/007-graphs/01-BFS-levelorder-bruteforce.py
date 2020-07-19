# ======================================================================================================
# Breadth First Search - Graph
# ======================================================================================================
# i.   Can also be called, level order search or a bruteforce search. Used to find shorted path(only UN-WEIGHTED GRAPH). 
# For, larger graphs, pretty much useless
# ii.  Convert graph into a tree with any vtx as root in any order and perform BFS. (same code as of tree)
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
        - greedy_search_shortest_path   : brute of all perm-combns of paths, selects best path
                                            + not related to bfs
                                            + For WEIGHTED graph
                                            + uses get_weight with memoisation for IDs only
        
        - shortest_path    : for UN-WEIGHTED graph
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
    # Brute force path search (from all perm-combns)
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
            self.__egde_memo[from_vtx+to_vtx] = 0 # populate 3of3
            if from_vtx == to_vtx: return 0 # same vtxs i.e 0 dist
            neighbors   = self.vtx_map[from_vtx].adj_list
        else: # instances of Vertex
            if from_vtx == to_vtx: return 0 # same vtxs i.e 0 dist        
            neighbors = from_vtx.adj_list

        
        for id, w in neighbors:
            if not ids_used:
                if id==to_vtx.id: return w
            elif ids_used:
                self.__egde_memo[from_vtx+to_vtx] = w # populate 2of3
                if id==to_vtx: return w

        if ids_used: self.__egde_memo[from_vtx+to_vtx] = False # populate 1of3
        return False # indicate no edge

    @staticmethod
    def __search_naive(paths):

        #best
        min_edge_wt = math.inf
        best_path   = None
        
        for path in paths:
            sum_edge_wts = 0
            broken_or_small_path  = False

            # find length of individual edges in path, add them and select min
            path_looped = False
            for beg_edge_idx in range(0, len(path)-1):
                end_edge_idx = beg_edge_idx + 1
                # use memoisation(for faster)
                edge_wt = graph.get_weight(path[beg_edge_idx], path[end_edge_idx], ids_used=True)
                sum_edge_wts += edge_wt # minimize
                #print(path)
                #print(path[beg_edge_idx], path[end_edge_idx], edge_wt)
                if (edge_wt is False) or (sum_edge_wts>=min_edge_wt):
                    # sum_edge_wts >= min_edge_wt: Intelligently reduces loop
                    # edge_wt is False: makes sure we are not upating best_path on wrong occasion
                    broken_or_small_path=True; break # no edge connecting
                if (beg_edge_idx == len(path)-2): path_looped = True
            
            if broken_or_small_path or not path_looped: 
                continue # reject path where one of edges is missing (or no path at all)
            
            if sum_edge_wts < min_edge_wt:
                min_edge_wt = sum_edge_wts
                best_path   = path
            #print(f"path: {path}, -------------> dist: {sum_edge_wts} \t best: {min_edge_wt}")
        
        return best_path, min_edge_wt

        
    def greedy_search_shortest_path(self, start_id, end_id):
        """ No way related to bfs 
        - returns path: none shortest_dist: inf if no path avl.

        TIME        : EXPONENTIAL 2^n!!! (use memoisation)
        """
        if start_id not in self.vtx_map.keys() or end_id not in self.vtx_map.keys():
            print('ID not present')
            return

        all_nodes   = set(self.vtx_map.keys()) # randomized here (python default hashing)
        beg_node    = set([start_id])
        end_node    = set([end_id])
        mid_path0   = all_nodes - beg_node - end_node

        # gen all possible paths and search
        
        # gen paths list 1of2
        paths = []
        for num_nodes in range(0, len(mid_path0)+1):
            for comb in combinations(mid_path0, r=num_nodes):
                #print(comb) # if (a, b, c) present, (b, a, c) absent
                for perm in permutations(comb):
                    #print(perm) # # if (a, b, c) present, (b, a, c) present 
                    path = list(beg_node) + list(perm) + list(end_node)
                    # gen paths list 2of2
                    paths.append( path )

        #search and log
        best_path, min_edge_wt = Graph.__search_naive(paths)

        print(f'best path: {best_path}, shortest dist: {min_edge_wt}')

        
    # ----------------------------------------------------------------------
    # BFS
    # ----------------------------------------------------------------------
    def __reconstruct(self, prevs):
        ''' SHORTEST PATH (UN-WEIGHTED)
        input: 
            BFS Traversal o/p 
                + list of nodes eg. ['B', 'A', 'D', 'C', 'E'] (Always unique)
                + prevs[0]   - beg of path
                + prevs[-1]   - end of path
        returns:
            shortest path from beg to end for unweighted graph

        TIME:   O(k!) (to find shortest path not BFS)
                    - k : traversal o/p of bfs (always unique)
                    - k is small most of the times (cz unique). But for large graphs large.
                    - for every `revcur` loop: n, n-1, n-2 ... 1 times

        '''
        shortest_path = [] #A->C->E represented as [(E, C,) (C, A)]  in reverse!
        
        # GENERATE SHAORTEST PATH
        for revcur in range(len(prevs)-1, -1, -1): # rev: end -1 !inclusive

            cur = 0 # beg !inclusive (loop until decreasing rev)
            # converge from both sides (works for odd as well as even len cz. ret=0 for same ids)
            # eg, for ['A', 'B', 'C', 'D', 'E', 'F']
            #                
            #  for (rev = len - 1)
            #  find shortest path: ['A', 'B', 'C', 'D', 'E', 'F']
            #                        ^cur                     ^rev
            #                ['A', 'B', 'C', 'D', 'E', 'F'] 
            #                  ^                        ^   is A->F shortest?
            #                ['A', 'B', 'C', 'D', 'E', 'F'] 
            #                       ^                   ^   is B->F shortest?
            #                ['A', 'B', 'C', 'D', 'E', 'F'] 
            #                            ^              ^   is C->F shortest?
            #                ['A', 'B', 'C', 'D', 'E', 'F'] 
            #                                 ^         ^   is D->F shortest?
            #                ['A', 'B', 'C', 'D', 'E', 'F'] 
            #                                      ^    ^   is E->F shortest?
            # n loops.
            # Do same for (rev = len-1) : ['A', 'B', 'C', 'D', 'E', 'F']
            #                               ^cur                ^rev
            # n-1 loops.
            # Do same for (rev = len-2) : ['A', 'B', 'C', 'D', 'E', 'F']
            #                               ^cur           ^rev
            # n-2 loops.
            # and so on ..
            #
            # so n! is worst case time complexity. but reduces over time if rev makes big jumps.
            while (cur < len(prevs)) and (cur != revcur):
                # 0     - if from == to
                # wt    - edge present
                # False - edge absent
                ret = self.get_weight(from_vtx=prevs[cur], to_vtx=prevs[revcur], ids_used=True)

                # DEBUG
                print(f'{prevs[revcur]} -> {prevs[cur]} edge: {ret} \t\t {revcur} -> {cur} ')
                if ret is not False: 
                    
                    if len(shortest_path) != 0: #[]
                        # check continous path
                        path_end = shortest_path[-1][1]
                        path_beg = prevs[revcur]
                        if (path_beg == path_end): # check wt as well for weightetd G
                            shortest_path.append((prevs[revcur], prevs[cur]))
                        else: pass
                    elif len(shortest_path) == 0: # initial case
                        shortest_path.append((prevs[revcur], prevs[cur]))
                    #print(shortest_path) # print next shortest path
                cur = cur + 1

        print(f'un-weighted shortest path reconstructed (revrse): {shortest_path}')
        unrev = [(fro, to) for (to, fro) in reversed(shortest_path)]
        print(f'un-weighted shortest path reconstructed (corect): {unrev}')
        return unrev# reconstructed

    @staticmethod
    def __display_path(list_of_fro_to):
        """
        input   : [('B', 'A'), ('A', 'C'), ('C', 'E')]
        output  : B->A->C->E
        """
        for fro, _ in list_of_fro_to:
            print(f'{fro}->', end="")
        print(list_of_fro_to[-1][1])


    def __opn(self, cur_id, goal, prevs):
        #print(cur_id)
        prevs.append(cur_id)
        if cur_id == goal: 
            print(f'path exists (direct edges may not be present): {prevs}')
            # reconstruct prevs
            reconstructed = self.__reconstruct(prevs)
            Graph.__display_path(reconstructed)
            return prevs, True
        
        #else
        return prevs, False

    def bfs(self, beg_id, end_id):
        """
        - record prev nodes to reconstruct path
        - can be used in graphs w/ equidistant nodes. eg. MAZE!

        TIME
            - Analytically, O(n)
            - if adjacency matrix O(n^2) cz matrix   
        """
        if beg_id not in self.vtx_map.keys() or end_id not in self.vtx_map.keys():
            print('IDs missing')
            return

        first   = self.vtx_map[beg_id]
        queue   = Queue([first])
        visited = set(first.id)
        prevs   = list([first.id]) # records shortest path

        # Regular BFS 
        # ------------
        while len(queue) != 0:
            # get (explore)
            parent_node = queue.dequeue() # not unique but cur_node_id(below) is unique

            # update queue (visiting)
            for cur_node_id, _ in parent_node.adj_list:
                if cur_node_id not in visited: # access in any order

                    # action o(unlike in bfs above)
                    prevs, goal_found = self.__opn(cur_node_id, goal=end_id, prevs=prevs)
                    if goal_found is True: return
                    
                    # add to visited and enqueue
                    queue.enqueue(self.vtx_map[cur_node_id])
                    visited.add(cur_node_id)


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
            },{
                "id"    : 'Q',
                "label" : 'Turkey',
                "coods" : (15, 80), #(x, y, width, height)
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
            {"initial": 'E', 'terminal': 'C', 'weight': 2},
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
    # c. BFS & and shortest path(greedy search - naive, not related to BFS)
    # -------------------------------------------------------------------
    # Shortest Path? Use greedy search by taking all possible node edges
    # works for both weighted and unweighted
    print("+"*100)
    print('+ Naive Bruteforce');                                    print("+"*100)
    graph.greedy_search_shortest_path(start_id='A', end_id='B');    print("="*100)
    graph.greedy_search_shortest_path(start_id='A', end_id='E');    print("="*100)
    graph.greedy_search_shortest_path(start_id='E', end_id='T');    print("="*100)
    graph.greedy_search_shortest_path(start_id='B', end_id='E');    print("="*100)
    graph.greedy_search_shortest_path(start_id='D', end_id='Q');    print("="*100, end='\n\n')

    # i. complete search / goal search / shortest path(un-weighted ONLY)
    print("+"*100)
    print('+ BFS Search');                                             print("+"*100)
    graph.bfs(beg_id='A', end_id='T');                                 print("="*100) 
    graph.bfs(beg_id='A', end_id='C');                                 print("="*100)
    graph.bfs(beg_id='B', end_id='E');                                 print("="*100)

    # note: B->E in naive (weighted) and B->E in bfs(unweighted)
    # can we use same bfs shortest path search code for B->E weighted?
    # Yes, edit the `__reconstruct`'s shortest path gen. line 271
    # but this is useless for large graphs, so, doesn't worth it.
    



# ======================================================================================================
# Output
# ======================================================================================================
"""
A -------------[100]-----------> B
A -------------[100]-----------> C
A -------------[10]-----------> D
B -------------[50]-----------> A
B -------------[100]-----------> D
C -------------[16]-----------> A
D -------------[16]-----------> E
E -------------[2]-----------> C
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+ Naive Bruteforce
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
best path: ['A', 'B'], shortest dist: 100
====================================================================================================
best path: ['A', 'D', 'E'], shortest dist: 26
====================================================================================================
ID not present
====================================================================================================
best path: ['B', 'A', 'D', 'E'], shortest dist: 76
====================================================================================================
best path: None, shortest dist: inf
====================================================================================================

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+ BFS Search
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
IDs missing
====================================================================================================
path exists (direct edges may not be present): ['A', 'B', 'D', 'C']
C -> A edge: 100                 3 -> 0 
C -> B edge: False               3 -> 1 
C -> D edge: False               3 -> 2 
D -> A edge: 10                  2 -> 0 
D -> B edge: 100                 2 -> 1 
B -> A edge: 100                 1 -> 0 
un-weighted shortest path reconstructed (revrse): [('C', 'A')]
un-weighted shortest path reconstructed (corect): [('A', 'C')]
A->C
====================================================================================================
path exists (direct edges may not be present): ['B', 'A', 'D', 'C', 'E']
E -> B edge: False               4 -> 0 
E -> A edge: False               4 -> 1 
E -> D edge: 16                  4 -> 2 
E -> C edge: False               4 -> 3 
C -> B edge: False               3 -> 0 
C -> A edge: 100                 3 -> 1 
C -> D edge: False               3 -> 2 
D -> B edge: 100                 2 -> 0 
D -> A edge: 10                  2 -> 1 
A -> B edge: 50                  1 -> 0 
un-weighted shortest path reconstructed (revrse): [('E', 'D'), ('D', 'B')]
un-weighted shortest path reconstructed (corect): [('B', 'D'), ('D', 'E')]
B->D->E
====================================================================================================
"""




