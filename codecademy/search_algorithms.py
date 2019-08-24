
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

#3. LINEARY SEARCH - implementation

#Here is the pseudocode for linear search as a function:

# For each element in the search_list
    # if element equal target value then
       # return its index
# if element is not found then 
    # raise a ValueError

def linear_search(search_list, target_value):
    for index in range(len(search_list)):
        print(search_list[index])
        if search_list[index] == target_value:
            return index
    raise ValueError('{} is not in list'.format(target_value))

values = [54, 22, 46, 99]
print(linear_search(values, 22))

# Example : 
number_list = [ 10, 14, 19, 26, 27, 31, 33, 35, 42, 44]
target_number = 33

try:
    result = linear_search(number_list, target_number)
    print(result)
except:
    ValueError as error_message:
        print('{}'.format(error_message))

# finding duplicates in lists

# Search list and target value
tour_locations = [ "New York City", "Los Angeles", "Bangkok", "Istanbul", "London", "New York City", "Toronto"]
target_city = "New York City"

#Linear Search Algorithm
def linear_search(search_list, target_value):
  matches = []
  for idx in range(len(search_list)):
    if search_list[idx] == target_value:
      matches.append(idx)
  
  if matches:
    return matches
  else:
    raise ValueError("{0} not in list".format(target_value))

tour_stops = linear_search(tour_locations, target_city)
print(tour_stops)

# find the maximum value (algo):
# Search list
test_scores = [88, 93, 75, 100, 80, 67, 71, 92, 90, 83]

#Linear Search Algorithm
def linear_search(search_list):
  maximum_score_index = None
  for idx in range(len(search_list)):
    if not maximum_score_index or search_list[idx] > search_list[maximum_score_index]:
      maximum_score_index = idx
  return maximum_score_index

# Function call
highest_score = linear_search(test_scores)

#Prints out the highest score in the list
print(highest_score)


































