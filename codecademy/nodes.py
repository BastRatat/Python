
# NODE INTRODUCTION

# Nodes are the fundamental building block of many computer science data structures. They form the basis for linked lists, stacks, queues, trees, and more.
# An individual node contains data and links to other nodes. Each data structure adds additional constraints or behavior to these features to create the desired structure.
# The data contained within a node can be a variety of types. It could be an integer (5), a string ("five"), decimal (5.1), an array ([5,3,4]) or nothing (null).
# The link or links within the node are sometimes referred to as pointers. This is because they “point” to another node.
# Typically, data structures implement nodes with one or more links. If these links are null, it denotes that you have reached the end of the particular node or link path you were previously following.
# Often, due to the data structure, nodes may only be linked to from a single other node.
# If you inadvertently remove the single link to a node, that node’s data and any linked nodes could be “lost” to your application. When this happens to a node, it is considered an orphaned node.


# CLASSES
class Node:
    # class Node that takes a constructor with two properties : value and link_node (default is None for the link_node)
  def __init__(self, value, link_node=None):
    self.value = value
    self.link_node = link_node

    # create a get_value method that works on the object (self) and return the value.
  def get_value(self):
    return self.value

    # create a get_link_node method that works on the object (self) and return the link_node.
  def get_link_node(self):
    return self.link_node

    # create a setter method that allows to update the link on the node.
  def set_link_node(self, link_node):
    self.link_node = link_node

# INSTANTIATION
yacko = Node("likes to yak")
wacko = Node("has a penchant for hoarding snacks")
dot = Node("enjoys spending time in movie lots")

# CALLS
yacko.set_link_node(dot) # yacko has a pointer to dot.
dot.set_link_node(wacko) # dot has a pointer to wacko.

dots_data = yacko.get_link_node().get_value() # gets the link of dots and print its value.

wackos_data = dot.get_link_node().get_value() # gets the link of wacko and print its value.

print(dots_data)
print(wackos_data)

yacko_to_wacko = yacko.get_link_node().get_link_node().get_value()
print(yacko_to_wacko)