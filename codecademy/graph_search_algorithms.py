# BASIC GRAPH SEARCH CONCEPTUAL

# You can use a graph search algorithm to traverse the entirety of a graph data structure in search of a specific vertex value.

#There are two common approaches to using a graph search to progress through a graph:

#depth-first search, known as DFS follows each possible path to its end
#breadth-first search, known as BFS broadens its search from the point of origin to an ever-expanding circle of neighboring vertices

#The big O runtime for both depth-first search and breadth-first search is O(vertices + edges).

#depth-first search is pretty adept at organizing vertices (or vertex values) with a clear order of visitation from beginning to end.

#There are three main traversal orders that you’ll come across for graph traversal:

#Preorder, in which each vertex is added to the “visited” list and added to the output list BEFORE getting added to the stack
#Postorder, in which each vertex is added to the “visited” list and added to the output list AFTER it is popped off the stack
#Reverse Post-Order (also known as Topological Sort), which returns an output list that is exactly the reverse of the post-order list

# Sum up :

#You can use a graph search algorithm to traverse the entirety of a graph data structure to locate a specific value
#Vertices in a graph search include a “visited” list to keep track of whether or not each vertex has been checked
#Depth-first search (DFS) and breadth-first search (BFS) are two common approaches to graph search
#The runtime for graph search algorithms is O(vertices + edges)
#DFS, which employs either recursion or a stack data structure, is useful for determining whether a path exists between two points
#BFS, which generally relies on a queue data structure, is helpful in finding the shortest path between two points
#There are three common traversal orders which you can apply with DFS to generate a list of all values in a graph: pre-order, post-order, and reverse post-order

# DFS

#We define a function dfs that accepts the following as parameters:

#graph (this is the graph that we pass in)
#current_vertex (the value passed in will be the start vertex)
#target_value (the value we are looking for)
#visited (a list to collect the path of our algorithm) Give visited a default value of None. We won’t be passing any argument in for visited when we call the function; this parameter only exists here for the recursive calls!






def dfs(graph, current_vertex, target_value, visited = None):
  if visited is None:
    visited = []
  visited.append(current_vertex)
  # base case
  if current_vertex is target_value:
    return visited
  # recursive step
  for neighbor in graph[current_vertex]:
    if neighbor not in visited:
      path = dfs(graph, neighbor, target_value, visited)
      if path:
        return path

def bfs(graph, start_vertex, target_value):
  path = [start_vertex]
  vertex_and_path = [start_vertex, path]
  bfs_queue = [vertex_and_path]
  visited = set()
  while bfs_queue:
    current_vertex, path = bfs_queue.pop(0)
    visited.add(current_vertex)
    for neighbor in graph[current_vertex]:
      if neighbor not in visited:
        if neighbor is target_value:
          return path + [neighbor]
        else:
          bfs_queue.append([neighbor, path + [neighbor]])











