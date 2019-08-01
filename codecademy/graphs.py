#Graphs are the perfect data structure for modeling networks, which make them an indispensable piece of your data structure toolkit. They’re composed of nodes, or vertices, which hold data, and edges, which are a connection between two vertices. A single node is a vertex.

#Consider a map of the area where you live. As a graph, we could model bus stops as vertices, with bus routes between stops functioning as the edges.

#What about the internet? Web pages can be vertices, and the hyperlinks which connect them are edges.

#Graphs have varying degrees of connection. The higher the ratio of edges to vertices, the more connected the graph.

#Graphs are an essential data structure in computer science for modeling networks. Let’s review some key terms:

#vertex: A node in a graph.
#edge: A connection between two vertices.
#adjacent: When an edge exists between vertices.
#path: A sequence of one or more edges between vertices.
#disconnected: Graph where at least two vertices have no path connecting them.
#weighted: Graph where edges have an associated cost.
#directed: Graph where travel between vertices can be restricted to a single direction.
#cycle: A path which begins and ends at the same vertex.
#adjacency matrix: Graph representation where vertices are both the rows and the columns. Each cell represents a possible edge.
#adjacency list: Graph representation where each vertex has a list of all the vertices it shares an edge with.

class Vertex:
  def __init__(self, value):
    self.value = value
    self.edges = {}

  def add_edge(self, vertex, weight = 0):
    self.edges[vertex] = weight

  def get_edges(self):
    return list(self.edges.keys())

class Graph:
  def __init__(self, directed = False):
    self.graph_dict = {}
    self.directed = directed

  def add_vertex(self, vertex):
    self.graph_dict[vertex.value] = vertex

  def add_edge(self, from_vertex, to_vertex, weight = 0):
    self.graph_dict[from_vertex.value].add_edge(to_vertex.value, weight)
    if not self.directed:
      self.graph_dict[to_vertex.value].add_edge(from_vertex.value, weight)

  def find_path(self, start_vertex, end_vertex):
    start = [start_vertex]
    seen = {}
    while len(start) > 0:
      current_vertex = start.pop(0)
      seen[current_vertex] = True
      print("Visiting " + current_vertex)
      if current_vertex == end_vertex:
        return True
      else:
        vertex = self.graph_dict[current_vertex]
        next_vertices = vertex.get_edges()
        next_vertices = [vertex for vertex in next_vertices if vertex not in seen]
        start.extend(next_vertices)
        
    return False

