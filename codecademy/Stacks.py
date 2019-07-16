#A stack is a data structure which contains an ordered set of data.

#Stacks provide three methods for interaction:

#Push - adds data to the “top” of the stack
#Pop - returns and removes data from the “top” of the stack
#Peek - returns data from the “top” of the stack without removing it

#This is a Last In, First Out or LIFO structure.

# Depending on the implementation, the top of the stack is equivalent to the head node of a linked list and the bottom of the stack is equivalent to the tail node.

#A constraint that may be placed on a stack is its size. This is done to limit and quantify the resources the data structure will take up when it is “full”.

#Attempting to push data onto an already full stack will result in a stack overflow. 

# SUM UP

#Stacks:

#Contain data nodes
#Support three main operations
#Push adds data to the top of the stack
#Pop removes and provides data from the top of the stack
#Peek reveals data on the top of the stack
#Implementations include a linked list or array
#Can have a limited size
#Pushing data onto a full stack results in a stack overflow
#Stacks process data Last In, First Out (LIFO)

from node import Node

class Stack:
  def __init__(self, limit=1000):
    self.top_item = None
    self.size = 0
    self.limit = limit
  
  # This first method will instantiate a node from Node, set that node to be the current top item on the stack on set the stack instance's top item equal to the new item. 
  def push(self, value):
    if self.has_space():
      item = Node(value)
      item.set_next_node(self.top_item)
      self.top_item = item
      self.size += 1
      print("Adding {} to the pizza stack!".format(value))
    else:
      print("No room for {}!".format(value))

      # This method will create a variable items_to_remove equal to the top item of the stack, will set a new top item (since we are removing our stack first item) and return the value of the item to be removed.
  def pop(self):
    if not self.is_empty():
      item_to_remove = self.top_item
      self.top_item = item_to_remove.get_next_node()
      self.size -= 1
      print("Delivering " + item_to_remove.get_value())
      return item_to_remove.get_value()
    print("All out of pizza.")

  def peek(self):
    if not self.is_empty():
      return self.top_item.get_value()
    print("Nothing to see here!")

  def has_space(self):
    return self.limit > self.size

  def is_empty(self):
    return self.size == 0
  