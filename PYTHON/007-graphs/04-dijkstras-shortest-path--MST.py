# Using same graph representation as adj_list. Can do with adj_matrix as well.
# But has extra data structure - __Edge which which can be used to sort them.

from utils import Stack
import math

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

    # ----------------------
    # Edge Data Structure
    # ----------------------
    class __Edge:
        def __init__(self, u_id, v_id, wt=None):
            """ u -> v """
            self.u_id      = u_id
            self.v_id      = v_id

            if wt is not None: self.wt = wt

        # for sorting egges - 
        # used in algorithms like kruskals
        def __lt__(self, other):
            return self.wt < other.wt

    # ----------------------
    # Graph
    # ----------------------
    def __init__(self, g_props):
        self.vtx_map    = {}

        self.edges      = [] #list of edges 

        self._directed   = g_props['directed']
        self._weighted   = g_props['weighted']

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

            - edge obj is appended in list of edges 
                + for both dir/undir graphs
        """
        # assuming vertices are already present
        if (u not in self.vtx_map) or (v not in self.vtx_map): raise('vtx not added! Add it first.')

        #else
        if directed is False:
            self.vtx_map[u].add_neighbour(v, w) # u - v
            self.vtx_map[v].add_neighbour(u, w) # v - u

        if directed is True:
            self.vtx_map[u].add_neighbour(v, w) # u -> v

        # add edge instances to list in graph
        self.edges.append(Graph.__Edge(u, v, w))


    @staticmethod
    def __print_edge(from_vtx, to_vtx, weight):
        print(f"{from_vtx} -------------[{weight}]-----------> {to_vtx}")

    def display(self):
        for vtx_id in self.vtx_map.keys():
            neighbors = sorted(self.vtx_map[vtx_id].adj_list)
            for neighbor in neighbors:
                Graph.__print_edge(vtx_id, neighbor[0], neighbor[1])
    
    # display edges using __Edge instances
    def display_edges(self, reverse=None): 
        print(f'\nNote: faster lookup! (reverse={reverse})')

        if reverse is not None:    
            for edge in sorted(self.edges, reverse=reverse):
                Graph.__print_edge(edge.u_id, edge.v_id, edge.wt)
        else:
            for edge in self.edges:
                Graph.__print_edge(edge.u_id, edge.v_id, edge.wt)

    # ------------------------------------------------------------------
    # Dijkstra's shortest path (form MST when all edges visited)
    # ------------------------------------------------------------------
    def dij(self, beg_id, pqueue=False):
        if pqueue is False:
            # not efficient - O(V^2)
            Graph.__dijkstra(self, beg_id)

        elif pqueue is True:
            # optimal using priority queue - O(VlgV)
            pass

    @staticmethod
    def __get_least_cost_and_id_from_set(input_set): # O(V)
        __least_cost_node   = None
        __least_cost        = None
        
        # can store the least cost globally for faster processing
        for cur_node_id, cur_node_cost in input_set:
            if __least_cost is None:
                __least_cost_node   = cur_node_id
                __least_cost        = cur_node_cost

            elif cur_node_cost < __least_cost:
                __least_cost        = cur_node_cost
                __least_cost_node   = cur_node_id

        return __least_cost_node, __least_cost

    @staticmethod
    def __dijkstra(graph, beg_id):
        """ DIJKSTRA'S ALGORITHM (without using priority queue)
        - Extension of Krukal's
        - Greedy algorithm but moves like dfs from single source

        - Uses 2 sets w/ dfft. purposes
            - `visited`: (like in dfs) tracks vtxs which have been operated upon
                + If visited, node will have best cost
            - `unvisited` : (like stack in dfs) same node can be inserted and popped multiple times
                + tracks adj nodes with their weights (in a loop)
                + pop(remove node as well) the least wt node as `cur` and proceed iteratively untile not empty
                + instead of set(O(n)) - use pqueue(O(logn)) for efficiency
        - Only prev vtx (i.e `cur`) of adj_vtx is needed for min-cost-path-from-src
        - `cost` data-structure to store changing costs maps `vtx-id` to `cur_cost`

        Note: If I want to reach any RANDOM DESTINATION from a FIXED STARTING point,
                + No matter which intermediate node / where it is,
                    + least cost to reach is constant! (cz we always start from SAME FIXED LOCATION!)

        Algorithm:
            - initialize cost, prev --
                + cost[bed_id]=0; cost[others] = inf 
                + prev[all] = null
            - add (beg_id, 0) to `unvisited`

            - while `unvisited` !empty --
                
                + cur_cost, cur_id = least_cost_node(unvisited) #O(N). pqueue here is more eff. -- O(logN)
                + pop(cur_id, unvisited)
                + add(cur_id, visited)

                + for adj_node, adj_wt in adj_list:
                    + if adj_node not in visited: # if in visited, already operated upon and stored best cost 
                        
                        +  -- relaxation --
                        + new_cost      = cur_cost + adj_wt
                        + existing_cost = cost[adj_list

                        + if new_cost < existing_cost: # if new_cost is better
                            + cost[adj_node] = new_cost # record cur cost
                            + prev[adj_node] = cur_node # record path
                            
                            + unvisited.add( (adj_node, new_cost) ) # update and proceed to it! Like dfs


        TIME        : O(N^2)
        """
        # initialize pev, cost
        PREV = {}
        COST = {}
        for _id in graph.vtx_map.keys():
            PREV[_id] = None
            COST[_id] = math.inf
        COST[beg_id] = 0

        # initialize visited, unvisited
        visited = set()
        unvisited = set([(beg_id, 0)]) #(cur_id, cur_cost)

        while len(unvisited) != 0:

            cur_least_node_id, cur_least_cost = Graph.__get_least_cost_and_id_from_set(unvisited)

            # update
            unvisited.remove((cur_least_node_id, cur_least_cost))
            visited.add(cur_least_node_id)

            for adj_id, adj_wt in graph.vtx_map[cur_least_node_id].adj_list:
                if adj_id not in visited:
                    # try to `relax` if already not
                    new_cost        = cur_least_cost + adj_wt
                    exisiting_cost  = COST[adj_id]

                    if new_cost < exisiting_cost:
                        # update --
                        # 1. `cost` datastructue
                        # 2. `prev` for shortest path
                        # 3. importantly, `unvisited` s.t loop proceed in DFS 
                        #       + Only difference is, we start with least_most vtx here
                        COST[adj_id]    = new_cost
                        PREV[adj_id]    = cur_least_node_id

                        unvisited.add((adj_id, new_cost))

        # Display
        print('construct shortest path to any node using `prevs`. If `None`, isolated node')
        print(PREV)
        print('\nfind cost shortest path to any node using `cost`. If `Inf`, isolated node')
        print(COST)

        



         
        


# --------------------------------------------------------------------------------------------------------------
# End class Graph
# --------------------------------------------------------------------------------------------------------------

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
            }
        ],
        "edges" : [
            {"initial": 'A', 'terminal': 'B', 'weight': 100},
            {"initial": 'D', 'terminal': 'B', 'weight': 99950},
            {"initial": 'C', 'terminal': 'B', 'weight': 20},
        ]
    }

    # Build the graph
    g_props = {
        'directed': graph_info['props']['directed'],
        'weighted': graph_info['props']['weighted']
    }
    graph = Graph(g_props=g_props)


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

    """
    # print edges (using __Edge)
    graph.display_edges()
    graph.display_edges(reverse=True)
    graph.display_edges(reverse=False)
    """

    # -------------------------------------------------------------------------------
    # Dijkstra's aglorithm (Find shortest path, Build MST)
    # --------------------------------------------------------------------------------
    print('');                                                        print('='*100)
    print('+ DIKSTRAS ALGORITHM: MST - O(n^2');                       print('='*100)
    graph.dij('A', pqueue=False);                                     print('='*100)
    
    # will it work for directed? yes as edges are just illusions.