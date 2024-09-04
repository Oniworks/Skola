class circle:
    pi = 3.14
    def __init__ (self, diameter):
        print(f"Ņew circle with diameter: {diameter}")
    def area(self, radius):
        area = (self.pi*radius**2)/39.37
        return area
    
pizza = circle(12)
table = circle(36)
room = circle(11460)

pizza_a = pizza.area(12/2)
table_a = table.area(36/2)
room_a = room.area(11460/2)
              
print(pizza_a, table_a, room_a)