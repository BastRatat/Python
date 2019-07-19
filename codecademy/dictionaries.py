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

# Access a value in a dictionary :
my_dict = dict() 
my_dict.update({1: "vrai", 2: "faux"})
print(my_dict)

zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}
print(zodiac_elements["earth"])
 
#We saw that we can avoid KeyErrors by checking if a key is in a dictionary first. Another method we could use is a try/except:

# Ex1
building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}

key_to_check = "Landmark 81"

if key_to_check in building_heights:
  print(building_heights["Landmark 81"])

# Ex2
caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120}
try:
    print(caffeine_level["matcha"])
except KeyError:
    print("Unknown Caffeine Level")

# Safely get a key.
# Dictionaries have a .get() method to search for a value instead of the my_dict[key] notation we have been using. If the key you are trying to .get() does not exist, it will return None by default

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}

tc_id = user_ids.get("teraCoder")
print(tc_id) #this line will return 100019:

#You can also specify a value to return if the key doesn’t exist.

stack_id = user_ids.get("superStackSmash", 100000)
print(stack_id) #this line will return 100000:

#Sometimes we want to get a key and remove it from the dictionary. We can use the .pop() method.

available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20

health_points += available_items.pop("stamina grains", 0)
health_points  += available_items.pop("power stew", 0)
health_points += available_items.pop("mystic bread", 0)

print(available_items)
print(health_points)

#Sometimes we want to operate on all of the keys in a dictionary. We can use the .key() methods
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

users = user_ids.keys()
lessons = num_exercises.keys()

print(users)
print(lessons)

# To get all value, we use the .values() method.

num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

total_exercises = 0

for value in num_exercises.values():
  total_exercises += value

print(total_exercises) #115

# You can get both the keys and the values with the .items() method.

pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}

for position, number in pct_women_in_occupation.items():
  print("Women make up {} percent of {}s.".format(number, position))