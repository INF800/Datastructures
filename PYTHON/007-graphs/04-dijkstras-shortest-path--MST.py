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


    # Dijkstra's shortest path (form MST when all edges visited)
    # ------------------------------------------------------------------
    def dij(self, beg_id):
        Graph.__dijkstra(self, beg_id)

    @staticmethod
    def __dijkstra(graph, beg_id):
        """

        TIME        : O(N^2)
        """

        # initialisation
        # All others except adj neighbors given inf
        # neighbors - their actual wts
        shortest_dists_from_beg_id = {}
        for node_id in graph.vtx_map.keys():
            shortest_dists_from_beg_id[node_id] = math.inf
        for neigh_id, neigh_wt in graph.vtx_map[beg_id].adj_list:
            shortest_dists_from_beg_id[neigh_id] = neigh_wt

        def __preoder(cur_id, this_path_sum, path):
            """
                - `Relax` neighbors (if path_sum + edge_cost < cur_cost)
                - add to visited
                - select shortest neigbor
                _ repeat (until visited full)
            """
            # update visited
            path.append(cur_id)
            visited.add(cur_id)
            print(f'>> path: {path}, {sum}')

            # relax neighbors (minimize)
            # and record the least cost node (for proceeding next)
            __least_cost_node = None
            __least_cost      = +math.inf

            neighbors = graph.vtx_map[beg_id].adj_list
            for neigh_id, neigh_wt in neighbors:
                if neigh_id not in visited: # note: checking 
                    existing_cost  = shortest_dists_from_beg_id[neigh_id]
                    cur_cost       = this_path_sum + neigh_wt
                    if cur_cost < existing_cost:
                        shortest_dists_from_beg_id[neigh_id] = cur_cost

                    if (__least_cost < cur_cost) or (__least_cost < existing_cost):
                        __least_cost        = min(cur_cost, existing_cost)
                        __least_cost_node   = neigh_id

            # recur into shortest neighbor
            for neigh_id, neigh_wt in neighbors:
                if neigh_id not in visited: # note: checking 
                    __preoder(__least_cost_node, this_path_sum=cur_cost+__least_cost, path=path)
            
            
            

        visited = set()
        __preoder(beg_id, this_path_sum=0, path=[])


         
        


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

    # print edges (using __Edge)
    graph.display_edges()
    graph.display_edges(reverse=True)
    graph.display_edges(reverse=False)

    # -------------------------------------------------------------------------------
    # Dijkstra's aglorithm (Find shortest path, Build MST)
    # --------------------------------------------------------------------------------
    print('');                                                        print('='*100)
    print('+ DIKSTRAS ALGORITHM: MST - O(n^2');                       print('='*100)
    graph.dij('A');                                                   print('='*100)
    
    # will it work for directed? yes as edges are just illusions.