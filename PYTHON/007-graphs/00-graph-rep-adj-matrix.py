# Adjacency Matrix Representation
# If not weighted simple 1/0 else if weighted wt/0 in matrix posn.
# If directed only outbound edge recorded

class Vertex:
    """ Not much needed. everything recorded in Graph
    Data Members
        - id
        - label
        - coods    
    """
    def __init__(self, id, label=None, coods=(None, None)):
        self.id     = id
        self.label  = label
        self.coods  = coods

class Graph:
    """
    DATA MEMBERS:
        - vtx_map       : map (created from `vertices` data) 
        - num_vtxs      : for dims of adj_mat
        - adj_matrix    : created from `edges` data
    """

    def __init__(self):
        self.vtx_map        = {}

        self.num_vtxs       = 0
        self.id2num         = {}
        self.num2id         = {}

        self.adj_matrix     = {} # k - id, v - str with nos.

    def add_vtx(self, v):
        if type(v) != Vertex: raise('Type mismatch')

        if v.id not in self.vtx_map:
            self.vtx_map[v.id] = v
            
            # record converter map - unique id (used in add_edge later)
            self.id2num[v.id]           = self.num_vtxs
            self.num2id[self.num_vtxs]  = v.id

            # incr one more col if exists
            for row_id in self.adj_matrix:
                self.adj_matrix[row_id] += [0]

            # populate adj_matrix(dict)
            self.num_vtxs += 1
            cur_row = [0]*self.num_vtxs
            self.adj_matrix[v.id] = cur_row

    def add_edge(self, u, v, w=0, directed=False):
        """ Assuming all vertices added, """
        if self.num_vtxs == 0: raise('no vertices')
        
        if (u in self.vtx_map) and (u in self.vtx_map): # `and` cz vertices added beforehand
            if directed is False:
                self.adj_matrix[v][self.id2num[u.id]] = w # v - u  
                self.adj_matrix[u][self.id2num[v.id]] = w # u - v
            if directed is True:
                self.adj_matrix[u][self.id2num[v]] = w # u -> v

    @staticmethod
    def __print_graph(from_vtx, to_vtx, weight):
        print(f"{from_vtx} -------------[{weight}]-----------> {to_vtx}")

    def display(self):
        for from_vtx_id in self.adj_matrix:
            for idx, possible_to_vtxs in enumerate(self.adj_matrix[from_vtx_id]):
                if possible_to_vtxs != 0:
                    to_vtx_id   = self.num2id[idx]
                    weight      = self.adj_matrix[from_vtx_id][idx]
                    # action
                    Graph.__print_graph(from_vtx_id, to_vtx_id, weight)

    def get_adj_matrix(self):
        return self.adj_matrix

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
            {"initial": 'A', 'terminal': 'D', 'weight': 10},
            {"initial": 'B', 'terminal': 'A', 'weight': 50},
            {"initial": 'A', 'terminal': 'C', 'weight': 100},
            {"initial": 'B', 'terminal': 'D', 'weight': 100},
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
    print(graph.get_adj_matrix())
    graph.display()