class School:
    def __init__(self, name, level, numberOfStudents):
        self.name = name
        self.level = level
        self.numberOfStudents = numberOfStudents
    
    def get_name(self):
        return self.name
    def get_level(self):
        return self.level
    def get_numberOfStudents(self):
        return self.numberOfStudents
    def set_numberOfStudents(self, numberOfStudents):
        self.numberOfStudents = numberOfStudents
    
    def __repr__(self):
        return f"{self.name} is a {self.level} school with {self.numberOfStudents} students"

class Primary(School):
    def __init__(self, name, level, numberOfStudents, pickupPolicy):
        super().__init__(name, level, numberOfStudents)
        self.pickupPolicy = pickupPolicy
    def get_pickupPolicy(self):
        return self.pickupPolicy
    
    def __repr__(self):
        return super().__repr__() + f"\nPickup policy: {self.pickupPolicy}"

class Middle(School):
    def __init__(self, name, level, numberOfStudents):
        super().__init__(name, level, numberOfStudents)

class High(School):
    def __init__(self, name, level, numberOfStudents, sportsTeams):
        super().__init__(name, level, numberOfStudents)
        self.sportsTeams = sportsTeams
    
    def __repr__(self):
        return super().__repr__() + f"\nSports teams: {', '.join(self.sportsTeams)}"

a1 = Primary("St. Paul's", "Primary", 100, "After lessons")
a2 = Middle("St. Paul's", "Middle", 100)
a3 = High("St. Paul's", "High", 100, ["Baseball", "Football", "Hockey", "Volleyball", "Soccer", "Basketball"])

print(a1)
print(a2)
print(a3)