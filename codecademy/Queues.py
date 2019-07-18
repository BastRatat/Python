# QUEUE

#Contain data nodes

#Support three main operations:
#ENQUEUE : adds data to the back of the queue
#DEQUEUE : removes and provides data from the front of the queue
#PEEK : provides data on the front of the queue

#Can be implemented using a linked list or array

#Bounded queues have a limited size.

#Enqueueing onto a full queue causes a queue overflow

#Queues process data First In, First Out (FIFO)

# CLASS DECLARATIONS

class Node:
    # We first create a Node class because a Queue data structure contains nodes.
    
    # Four methods : constructor, set_next_node, get_next_node, get_value
    
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
 
    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_next_node(self):
        return self.next_node

    def get_value(self):
        return self.value


class Queue:

    def __init__(self, max_size=None):
        self.head = None
        self.tail = None
        self.max_size = max_size
        self.size = 0

    # Provide data from self.head (the front of the queue).
    def peek(self):
        return self.head.get_value()

    # Check the size of the queue.
    def get_size(self):
        return self.size

    # Check if the queue still has space (if not, we cannot enqueue).
    def has_space(self):
        if self.max_size == None:
            return True
        else:
            return self.max_size > self.get_size()

    # Check if the object is empty.
    def is_empty(self):
        return self.size.get_value() == 0


