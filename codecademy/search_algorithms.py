
# SEARCH ALGOS - conceptuals

# 1. LINEAR SEARCH

#Linear search is a search algorithm that sequentially checks whether a given value is an element of a specified list by scanning the elements of a list one-by-one until it finds the target value.

#The time complexity for linear search is O(N), but its performance is dependent on its input:
#    - Best Case: The algorithm requires only 1 comparison to find the target value in the first position of the list.
#    - Worst Case: The algorithm requires only n comparison to find the target value in the last position of the list or does not exist in the list.
#    - Average Case: The algorithm makes N/2 comparisons.

#Linear search is a good choice for a search algorithm when:
#    - You expect the target value to be positioned near the beginning of the list.
#    - A search needs to be performed on an unsorted list because linear search traverses the entire list from beginning to end, regardless of its order.

#Without any knowledge about the ordering, we would resort to a linear search taking O(N) time.

#2. BINARY SEARCH

# In each iteration, we are cutting the list in half. The time complexity is O(log N)
# For example, a sorted list of 64 elements will take at most log2(64) = 6 comparisons.




















