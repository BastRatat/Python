#A heap is one common implementation of a priority queue.

#Heaps are used to maintain a maximum or minimum value in a dataset.

#Think of the min-heap as a binary tree with two qualities:

#The root is the minimum value of the dataset.
#Every child’s value is greater than its parent.

#We can picture min-heaps as binary trees, where each node has at most two children. As we add elements to the heap, they’re added from left to right until we’ve filled the entire level.

#The location of each child or parent derives from a formula using the index.

#left child: (index * 2) + 1
#right child: (index * 2) + 2
#parent: (index - 1) / 2 — not used on the root!

#Heapifying up :
#We’re adding an element to the bottom of the tree and moving upwards, so we’re heapifying up.

# CLASS DECLARATION

class MinHeap:
  def __init__(self):
    self.heap_list = [None]
    self.count = 0

  def parent_idx(self, idx):
    return idx // 2

  def left_child_idx(self, idx):
    return idx * 2

  def right_child_idx(self, idx):
    return idx * 2 + 1

  def child_present(self, idx):
    return self.left_child_idx(idx) <= self.count
  
  def retrieve_min(self):
    if self.count == 0:
      print("No items in heap")
      return None
    
    min = self.heap_list[1]
    self.heap_list[1] = self.heap_list[self.count]
    self.count -= 1
    self.heap_list.pop()
    self.heapify_down()
    return min

  def add(self, element):
    self.count += 1
    self.heap_list.append(element)
    self.heapify_up()


  def get_smaller_child_idx(self, idx):
    if self.right_child_idx(idx) > self.count:
      return self.left_child_idx(idx)
    else:
      left_child = self.heap_list[self.left_child_idx(idx)]
      right_child = self.heap_list[self.right_child_idx(idx)]
      if left_child < right_child:
        return self.left_child_idx(idx)
      else:
        return self.right_child_idx(idx)
    
  def heapify_up(self):
    idx = self.count
    swap_count = 0
    while self.parent_idx(idx) > 0:
      if self.heap_list[self.parent_idx(idx)] > self.heap_list[idx]:
        swap_count += 1
        tmp = self.heap_list[self.parent_idx(idx)]
        self.heap_list[self.parent_idx(idx)] = self.heap_list[idx]
        self.heap_list[idx] = tmp
      idx = self.parent_idx(idx)

    element_count = len(self.heap_list)
    if element_count > 10000:
      print("Heap of {0} elements restored with {1} swaps"
            .format(element_count, swap_count))
      print("")    
      
  def heapify_down(self):
    idx = 1
    # starts at 1 because we swapped first and last elements
    swap_count = 1
    while self.child_present(idx):
      smaller_child_idx = self.get_smaller_child_idx(idx)
      if self.heap_list[idx] > self.heap_list[smaller_child_idx]:
        swap_count += 1
        tmp = self.heap_list[smaller_child_idx]
        self.heap_list[smaller_child_idx] = self.heap_list[idx]
        self.heap_list[idx] = tmp
      idx = smaller_child_idx

    element_count = len(self.heap_list)
    if element_count >= 10000:
      print("Heap of {0} elements restored with {1} swaps"
            .format(element_count, swap_count))
      print("")  