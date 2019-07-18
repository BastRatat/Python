# VARIABLES

brunch = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}
# Brunch is served from 1100 to 1600.

early_bird = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
# Early-bird Dinners are served from 1500 to 1800.

dinner = {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
# Dinner is served from 1700 to 2300.

kids = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}
# Kids is served from 1100 to 2100.


# CLASS DECLARATION

class Menu:

    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __str__(self):
        return "{} menu available from {} to {}.".format(str(self.name), self.start_time, self.end_time)

    def calculate_bill(self, purchased_items):
        bill = 0
        for purchased_item in purchased_items:
            if purchased_item in self.items:
                bill += self.items[purchased_item]
        return bill

class Franchise:

    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    def __str__(self):
        return "The adress of the restaurant is {}.".format(str(self.address))

    def available_menus(self, time):
        available_menu = list()
        for menu in self.menus:
            if time >= menu.start_time and time <= menu.end_time:
                available_menu.append(menu)
        return available_menu

# CLASS INSTANTIATION

brunch_menu = Menu("Brunch", brunch, 1100, 1600)
early_bird_menu = Menu("Early bird", early_bird, 1500, 1800)
dinner_menu = Menu("Dinner", dinner, 1700, 2300)
kids_menu = Menu("Kids", kids, 1100, 2100)

flagship_store = Franchise("1232 West End Road", [brunch_menu, early_bird_menu, dinner_menu, kids_menu])
new_installment = Franchise("12 East Mulberry Street", [brunch_menu, early_bird_menu, dinner_menu, kids_menu])





# CALLS 
# print(brunch_menu) # will return Brunch menu available from 1100 to 1600.
# print(brunch_menu.calculate_bill(['pancakes', 'home fries', 'coffee'])) # will return 13.5
# print(early_bird_menu.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)'])) # will return 21.5
# print(flagship_store)
# print(flagship_store.available_menus(1200))



