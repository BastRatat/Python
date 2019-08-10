#Bubble sort is an introductory sorting algorithm that iterates through a list and compares pairings of adjacent elements.

#According to the sorting criteria, the algorithm swaps elements to shift elements towards the beginning or end of the list.

#For example, bubble sort transforms a list to an ascending order, from lowest to highest:

list1 = [5, 2, 9, 1, 5]
list_sorted = [1, 2, 5, 5, 9]

#We implement the algorithm with two loops : 
#    - The first loop iterates as long as the list is unsorted and we assume it’s unsorted to start.
#    - Within this loop, another iteration moves through the list. For each pairing, the algorithm asks:
#        - if the first element is larger than the second element, then we swap the position of the elements. The larger element is now at a greater index than the smaller element.

#When a swap is made, we know that the list is still unsorted. The outer loop will run again when the inner loop concludes.

#The process repeats until the largest element makes its way to the last index of the list. The outer loop will run until no swaps are made within the inner loop.

#We create a temporary variable to avoid that some elements get replaced :
temp = list[index_1]
list[index_1] = list[index_2]
list[index_2] = NotImplementedType

#We can also use multiple assignments which removes the need for a temporary variable :
list[index_1], list[index_2] = list[index_2], list[index_1]

#We are performing n-1 comparisons for our inner loop. Then, we must go through the list n times in order to ensure that each item in our list has been placed in its proper order.

#Algorithm efficiency :
#O(n(n−1))=O(n(n))=O(n^2)
