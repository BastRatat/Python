# Dictionaries

# - A dictionary begins and ends with curly braces ({ and }).
# - Each item consists of a key (i.e., “oatmeal”) and a value (i.e., 3)
# - Each key: value pair (i.e., "oatmeal": 3 or "avocado toast": 6) is separated by a comma (,)
# - It’s considered good practice to insert a space () after each comma, but your code will still run without the space.

sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}
num_cameras = {"backyard": 6,  "garage": 2, "driveway": 1}

# Values can be any type. You can use a string, a number, a list, or even another dictionary as the value associated with a key.

# We can have a list or a dictionary as a value of an item in a dictionary, but we cannot use these data types as keys of the dictionary. If we try to, we will get a TypeError. Keys have to be immutable.
# It will throw a TypeError: unhashable type.

# Two ways of creating an empty dictionary:
empty_dic = {}
empty_dic_2 = dict()

# To add a key :
empty_dic["KEY"] = "VALUE"
print(empty_dic)

# To add multiple keys, we can use the update() method:
user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
user_ids.update({"theLooper": 138475, "stringQueen": 85739})
print(user_ids) # {'teraCoder': 9018293, 'proProgrammer': 119238, 'theLooper': 138475, 'stringQueen': 85739}

# We can overwrite values by modifying values inside keys.
oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
oscar_winners["Supporting Actress"] = "Viola Davis"
oscar_winners["Best Picture"] = "Moonlight" # will overwrite the value associated with "Best Picture" to "Moonlight".

# Let’s say we have two lists that we want to combine into a dictionary.
dict_name = {key:value for key, value in zip(list1, list2)}