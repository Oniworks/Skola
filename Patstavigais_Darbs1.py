class Menu:
    def __init__(self, name:str, items:dict, start_time:str, end_time:str):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return f"{self.name} available from {self.start_time} to {self.end_time}"
    
    def calculate_bill(self, purchased_items:list):
        return sum([self.items[item] for item in purchased_items])

brunch = Menu("Brunch", {
    'pancakes': 7.50,
    'waffles': 9.00,
    'burger': 11.00,
    'home fries': 4.50,
    'coffee': 1.50,
    'espresso': 3.00,
    'tea': 1.00,
    'mimosa': 10.50,
    'orange juice': 3.50
    },
    "11:00", "16:00")

early_bird = Menu("Early Bird", {
    'salumeria plate': 8.00,
    'salad and breadsticks (serves 2, no refills)': 14.00,
    'pizza with quattro formaggi': 9.00,
    'duck ragu': 17.50,
    'mushroom ravioli (vegan)': 13.50,
    'coffee': 1.50,
    'espresso': 3.00,
    },
    "15:00", "18:00")

dinner = Menu("Dinner", {
    'crostini with eggplant caponata': 13.00,
    'caesar salad': 16.00,
    'pizza with quattro formaggi': 11.00,
    'duck ragu': 19.50,
    'mushroom ravioli (vegan)': 13.50,
    'coffee': 2.00,
    'espresso': 3.00,
    },
    "17:00", "23:00")

kids = Menu("Kids", {
    'chicken nuggets': 6.50,
    'fusilli with wild mushrooms': 12.00,
    'apple juice': 3.00,
    },
    "11:00", "21:00")

print(Menu.calculate_bill(brunch, ["pancakes", "home fries", "coffee"]))
print(Menu.calculate_bill(early_bird, ["salumeria plate", "mushroom ravioli (vegan)"]))

#tiku lidz 12. punktam