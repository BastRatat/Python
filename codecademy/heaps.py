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

    # 3 helper methods
    def parent_idx(self, idx):
        return idx // 2

    def left_child_idx(self, idx):
        return idx * 2

    def right_child_idx(self, idx):
        return idx * 2 + 1

    def retrieve_min(self):
        if self.count == 0:
            print("No items in heap")
            return None
        min = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.count]
        self.heap_list.pop()
        self.count -= 1
        print("Last element moved to first: {}".format(self.heap_list))
        self.heapify_down()
        return min

    def heapify_down(self):
        print("Heapifying down...")
        idx = 1

    def add(self, element):
        print("Adding {} to {}...".format(element, self.heap_list))
        self.count += 1
        self.heap_list.append(element)
        self.heapify_up()

    def heapify_up(self):
        idx = self.count
        while self.parent_idx(idx) > 0:
            if self.heap_list[self.parent_idx(idx)] > self.heap_list[idx]:
                tmp = self.heap_list[self.parent_idx(idx)]
                print("swapping {0} with {1}".format(tmp, self.heap_list[idx]))
                self.heap_list[self.parent_idx(idx)] = self.heap_list[idx]
                self.heap_list[idx] = tmp
            idx = self.parent_idx(idx)
        print("HEAP RESTORED! {0}".format(self.heap_list))
        print("")  
            


# INSTANTIATION
heap = MinHeap()
print(heap.heap_list)
heap.add(45)
print(heap.heap_list)