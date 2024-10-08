class Employee():
    new_id = 1
    def __init__(self):
        self.id = Employee.new_id
        Employee.new_id += 1
    def say_id(self):
        print(f"My id is {self.id}.")

class Admin(Employee):
    def say_id(self):
        print("I am an admin.")
        super().say_id()

class Manager(Admin):
    def say_id(self):
        super().say_id()
        print("I'm in charge.")

e1 = Employee()
e2 = Employee()
e3 = Admin()

e3.say_id()

e4 = Manager()
e4.say_id()