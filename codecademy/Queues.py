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
    
        # has to check if the queue is full before running.
    def enqueue(self, value):
        if self.has_space():
            item_to_add = Node(value)
            print("Adding {} to the queue".format(str(item_to_add.get_value)))
            if self.is_empty():
                self.head = item_to_add
                self.tail = item_to_add
            else:
                self.tail.set_next_node(item_to_add)
            self.size += 1
        else:
            print("The queue already contain {}, there's no more room for enqueuing...".format(self.max_size)

    # Has to check if the queue is empty before running.
    def dequeue(self):
        if not self.is_empty():
            item_to_remove = self.head
            print("Removing {} from the queue...".format(str(item_to_remove.get_value())))
            if self.get_size == 1:
                self.head = None
                self.tail = None
            else:
                self.head = item_to_remove.get_next_node()
            self.size -= 1
        else: 
            print("The queue is empty, you cannot dequeue...")



    # Provide data from self.head (the front of the queue).
    def peek(self):
        if self.is_empty():
            print("The queue is empty, there's nothing to return...")
        else:
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

