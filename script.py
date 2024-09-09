class Circle:
    pi = 3.14
    def __init__(self, diameter):
        self.radiuss = diameter / 2
        print(f"Creating circle with diameter {diameter}")
    def circumference(self):
        circumference = 2 * self.pi * self.radiuss
        return circumference
    def __repr__(self):
        return f"Circle with radiuss: {self.radiuss}"
    
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza.circumference(), teaching_table.circumference(), round_room.circumferenmce())
