class TreeNode:
    # The constructor of the Treenode class takes self and value as parameter.
    def __init__(self, value):
        self.value = value
        # We will store the references to child nodes in a list.
        self.children = []

    def add_child(self, child_node):
        print("Adding {}".format(child_node.value))
        # add the child_node the self.children list.
        self.children.append(child_node)
    
    # To removes nodes from a tree, we'll call remove() on a specific node, pass another node as an argument, remove from self.children any nodes which match the argument node.
    def remove_child(self, child_node):
        print("Removing {} from {}".format(child_node.value, self.value))
        self.children = [child for child in self.children if child is not child_node]

    #Tree traversal is a standard operation for finding nodes with a specific value or printing all the nodes available in a tree..
    def traverse(self):
        nodes_to_visit = [self]
        while len(nodes_to_visit) > 0:
            current_node = nodes_to_visit.pop()
            print(current_node.value)
            nodes_to_visit += current_node.children

        

root = TreeNode("CEO")
first_child = TreeNode("Vice-President")
second_child = TreeNode("Head of Marketing")

root.add_child(first_child)
root.add_child(second_child)
root.traverse()