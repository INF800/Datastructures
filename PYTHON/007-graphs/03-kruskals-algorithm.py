# Using same graph representation as adj_list. Can do with adj_matrix as well.
# But has extra data structure - __Edge which which can be used to sort them.

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

    # Minimum Spanning Tree
    def buldMSP(self, algorithm='Kruskal Optimized'):

        # kruskal's algorithm - O(N^2)
        if algorithm == 'Kruskal':
            
            MST_nodes, MST_edges = Graph.__Kruskals(graph=self)
            
            print(f'nodes: {[node for node in MST_nodes]}\nMST_edges:')
            for edge in MST_edges:
                Graph.__print_edge(edge.u_id, edge.v_id, edge.wt)

        # kruskal's algorithm - O(NlogN)
        elif algorithm == 'Kruskal Optimized':
            MST_edges = Graph.__kruskal_optimized(graph=self)

            print('optimized usig union find/partiton:')
            for edge in MST_edges:
                Graph.__print_edge(edge.u_id, edge.v_id, edge.wt)

    # ----------------------------------------------------------------
    # Kruskal's algorithm
    # ----------------------------------------------------------------
    @staticmethod
    def __Kruskals(graph):
        """ Buidiing minimum spanning tree (There are no cycles in trees)

        MST: truck should clean min. roads s.t all destinations are reachable
        
        - Mimimum spanning tree consists of total `|V|-1` edges
        - Algorithm:
            + Initially sort all edges (for faster lookup) ----------------------------------------------------------> |E|lg|E|
            + Select shortest edge (if not forming cycle / already visited)
                + Sets used - to check both constraints
            + repeat until `|V|-1` edges selected -------------------------------------------------------------------> |V|-1 
        
        - Use of sets data-structures
            + Sets are ingeniously used to record added vertices
                - It makes sure
                    1// no vetex is visited more than once
                    2// cycles are not formed - trees are ACYCLIC (means same as 1//)
            + How?
                - Initially create list of |V| sets with each set having one(unique) vertices
                - When edge E is being considered,
                    + if vertices of E in same set in list of sets? --------------------------------------------------> O(|V|) - lin. search in list of sets
                        - ignore. move to next shortest edge. (cz, already visited / forms cycle)
                    + if in dfft sets,
                        - Include E in MST
                        - Add and Remove: Add union of the two sets to list and remove the the two sets ---------------> Rehashing!
        
        - Note: 
            - Each new set after iter represnts new group of connected-vertices(path) (in MST being formed)
                + Initially, as there are no edges in MST, no. of groups = no. of edges!
            - Finally, one of sets will be list of all vertices of MST  

        TIME:       + Simple Set                - O(|V|^2)
                    + Optimized union opn       - 
        """
        # sort all edges into Stack (can use array w/ linear cursor too.)
        list_of_all_edges   = sorted(graph.edges, reverse=True) # |E| lg(|E|)
        sorted_edges        = Stack(list_of_all_edges)

        # create unique sets for each vertex:
        # each set in the list repesent unique unconnected path of MST
        # Initiall, as there are v paths cz, |V| vertices
        unique_unconn_paths = [set(vtx_id) for vtx_id in graph.vtx_map.keys()]

        MST_edges_accumulator = [] # list of __Edge instances

        # for graph with |V| edges, MST has |V-1| edges
        # truck should clean min. roads s.t all destinations are reachable
        n_vtxs = len(unique_unconn_paths) # same as |V|
        new_unconn_path_vtxs = None
        while len(MST_edges_accumulator) != (n_vtxs-1): # O(|V|)
            cur_shortest_edge     = sorted_edges.pop()
            cur_u                 = cur_shortest_edge.u_id
            cur_v                 = cur_shortest_edge.v_id
            cur_wt                = cur_shortest_edge.wt

            __u_set_idx = None
            __v_set_idx = None
            __skip_edge = False
            # make sure path is acyclic and get idxs of sets
            idx = 0
            while idx != len(unique_unconn_paths): # O(|V|)
                cur_set = unique_unconn_paths[idx]

                # skip this edge if cyclic
                if (cur_u in cur_set) and (cur_v in cur_set): 
                    __skip_edge = True
                    break # inner for-loop
                
                # else, log idx of sets
                elif cur_u in cur_set: __u_set_idx = idx
                elif cur_v in cur_set: __v_set_idx = idx
                if (__u_set_idx is not None) and (__v_set_idx is not None):
                    break
                idx +=1

            if __skip_edge is not True:
                
                # append MST edge, 
                MST_edges_accumulator.append( Graph.__Edge(cur_u, cur_v, cur_wt) )       
                
                # union & delete old 2 sets
                new_unconn_path_vtxs = unique_unconn_paths[__u_set_idx].union(unique_unconn_paths[__v_set_idx])
                unique_unconn_paths.append(new_unconn_path_vtxs)
                
                # del is shift opn - O(|V|) can use hmaps instead -- O(1)
                # or simply make it None and a simple conditional to ignore if none..
                # If you really want to do so, never pop a set. then can compare if
                # sets are equal in 0(1) by checking addr -- `if x is y:` 
                # BEST OPTION: Use partition data-structure
                if __v_set_idx > __u_set_idx:
                    del unique_unconn_paths[__v_set_idx], unique_unconn_paths[__u_set_idx]
                else: 
                    del unique_unconn_paths[__u_set_idx], unique_unconn_paths[__v_set_idx]
            
        return new_unconn_path_vtxs, MST_edges_accumulator

    # ----------------------------------------------------------------
    # Kruskal's algorithm - optimal
    # ----------------------------------------------------------------
    @staticmethod
    def __kruskal_optimized(graph):
        """
        + OPTIMAL

        - UnionFind/Partition Dataset
            + used to check if if path is acyclic in optimal way 
                (just like 2 sets list in un-optimal way)
        """

        class __UnionFind:
            """
            Used for two set opns - (using just a list/hmap)
                + Set Membership
                + Union opn.
            """
            def __init__(self, list_of_node_ids):
                # note: can be a list as well where IDs are idxs
                self.__partition = {}
                
                for _id in list_of_node_ids:
                    # initially each node is root of it's own tree
                    self.__partition[_id] = _id 

            def find_root(self, x_id):
                # if roots of two ids are same - same path i.e same path
                # note: this is ammortized 1 - path depth is notably small
                cur_node = self.__partition[x_id]
                while self.__partition[cur_node] != cur_node:
                    # update
                    cur_node = self.__partition[cur_node]
                
                return cur_node # ends at root

            def union(self, u_id_root, v_id_root):
                # point any one of roots to other
                self.__partition[u_id_root] = v_id_root

            def get_path(self, x_id):
                path = []
                cur_node = self.__partition[x_id]
                while self.__partition[cur_node] != cur_node:
                    path = path.append(cur_node)
                    cur_node = self.__partition[cur_node]

                return path


        # ---------------------------------
        # end class UnionFind  / partition
        # ----------------------------------
        
        # kruskals algorithm:
        # -------------------
        
        # get sorted edges
        list_of_all_edges   = sorted(graph.edges, reverse=True) # |E| lg(|E|)
        sorted_edges        = Stack(list_of_all_edges)
        n_vtxs              = len(graph.vtx_map.keys())

        # create patrition for faster union/set membership 
        partition = __UnionFind(graph.vtx_map.keys())

        MST_edges = []
        while len(MST_edges) != (n_vtxs-1): # always n_vtxs-1 edges in MST
            
            _cur_edge   = sorted_edges.pop()
            cur_u_id    = _cur_edge.u_id
            cur_v_id    = _cur_edge.v_id
            cur_wt      = _cur_edge.wt

            root_u_id = partition.find_root(cur_u_id) 
            root_v_id = partition.find_root(cur_v_id)

            if root_u_id == root_v_id: # same path hence, ignore.
                continue

            #else append to accumulator and union the sets
            MST_edges.append(Graph.__Edge(cur_u_id, cur_v_id, cur_wt))
            partition.union(root_u_id, root_v_id)

        # geting all nodes can be done from returned edges

        return MST_edges




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
    # Kruskal's aglorithm (Build MST)
    # --------------------------------------------------------------------------------
    print('');                                                        print('='*100)
    print('+ KRUSKALS ALGORITHM: MST - O(n^2');                       print('='*100)
    graph.buldMSP(algorithm='Kruskal');                               print('='*100)
    
    print('+ KRUSKALS OPTIMIZED: MST - O(nlogn');                     print('='*100)
    graph.buldMSP(algorithm='Kruskal Optimized');                     print('='*100)
    
    # will it work for directed? yes as edges are just illusions.