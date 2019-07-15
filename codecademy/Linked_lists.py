# NODE IMPLEMENTATION

# We first have to create a Node class with a constructor, a get_value method, a get_next_node method and a set_next_node method. 
# Then we create a LinkedList class with a constructor that allows to set up a head and a method to return this head.
# The insert_beginning() will allow us to insert new nodes at the beginning of the linked list.
# CLASSES:
class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node
    
  
  def get_value(self):
    return self.value
  
  def get_next_node(self):
    return self.next_node
  
  def set_next_node(self, next_node):
    self.next_node = next_node
    
class LinkedList:
  
  def __init__(self, value=None):
    self.head_node = Node(value)
    
  def get_head_node(self):
    return self.head_node

  def insert_beginning(self, new_value):
    new_node = Node(new_value) # Create a new node using the class Node
    new_node.set_next_node(self.head_node) # Link new_node to the existing head_node.
    self.head_node = new_node # Replace the current head_node with new_node.

  def stringify_list(self):
    string_list = ""
    current_node = self.get_head_node()
    while current_node:
      if current_node.get_value() != None:
          string_list += str(current_node.get_value()) + "\n"
          current_node = current_node.get_next_node()
    return string_list
  
  # remove_node method 
    def remove_node(self, value_to_remove):
        current_node = self.get_head_node()
        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
        else:
            while current_node:
                next_node = current_node.get_next_node()
            if next_node.get_value() == value_to_remove:
                current_node.set_next_node(next_node.get_next_node())
                current_node = None
            else:
                current_node = next_node
          
# INSTANTIATION
my_node = Node(44)
  
# CALLS
print(my_node.get_value())

