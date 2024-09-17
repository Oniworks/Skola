#Extra
class Person():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def __repr__(self):
        return f"Name: {self.name}\nAge: {self.age}\nGender: {self.gender}"

class Patient(Person):
    def __init__(self, name, age, gender,patient_id, ailments, appointments):
        super().__init__(name, age, gender)
        self.patient_id = patient_id
        self.ailments = ailments
        self.appointments = appointments
    def add_ailment(self, ailment):
        self.ailments.append(ailment)
    def scheduele_appopintment(self, appointment):
        self.appointments.append(appointment)
    def __repr__(self):
        return super().__repr__() + f"\nPatient ID: {self.patient_id}\nAilments: {self.ailments}"

class Staff(Person):
    def __init__(self, name, age, gender, staff_id, department):
        super().__init__(name, age, gender)
        self.staff_id = staff_id
        self.department = department
    def __repr__(self):
        return super().__repr__() + f"\nStaff ID: {self.staff_id}\nDepartment: {self.department}"

class Doctor(Staff):
    def __init__(self, name, age, gender, staff_id, department, specialization, patients):
        super().__init__(name, age, gender, staff_id, department)
        self.specialization = specialization
        self.patients = patients
    def add_patient(self, patient):
        self.patients.append(patient)
    def __repr__(self):
        return super().__repr__() + f"\nSpecialization: {self.specialization}"
class Nurse(Staff):
    def __init__(self, name, age, gender, staff_id, department, shift):
        super().__init__(name, age, gender, staff_id, department)
        self.shift = shift
    def __repr__(self):
        return super().__repr__() + f"\nShift: {self.shift}"

class Appointment():
    def __init__(self, appointment_id, patient, doctor, date, time):
        self.appointment_id = appointment_id
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.time = time
    def __repr__(self):
        return f"Appointment ID: {self.appointment_id}\nPatient: {self.patient}\nDoctor: {self.doctor}\nDate: {self.date}\nTime: {self.time}"

smith = Patient("John Smith", 25, "Male", 12345, [], [])
gru = Doctor("Dr. Gru", 45, "Male", 67890, "Cardiology", "Cardiology", [])
Joy = Nurse("Nurse Smith", 35, "Female", 54321, "Cardiology", "Day")
appointment = Appointment(1, smith, gru, "20.10.2024", "10:00")

smith.add_ailment("Sharp pains in the chest area")
gru.add_patient(smith)
smith.scheduele_appopintment("DrGru, Cardiology")

print(appointment)

'''
#Advanced
class Employee():
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
    def __repr__(self):
        return f"Name: {self.name}\nEmployee ID: {self.employee_id}\nSalary: {self.salary}"
    def calculate_pay(self):
        return self.salary

class Manager(Employee):
    def __init__(self, name, employee_id, salary, bonus):
        super().__init__(name, employee_id, salary)
        self.bonus = bonus
    def calculate_pay(self):
        return self.salary + self.bonus

class Engineer(Employee):
    def __init__(self, name, employee_id, salary, specialty):
        super().__init__(name, employee_id, salary)
        self.specialty = specialty
    def calculate_pay(self):
        return self.salary

class Intern(Employee):
    def __init__(self, name, employee_id, salary, school):
        super().__init__(name, employee_id, salary)
        self.school = school
    def calculate_pay(self):
        return self.salary/2

employee = Employee("John Smith", 1, 50000)
manager = Manager("Jane Doe", 2, 75000, 5000)
engineer = Engineer("Bob Johnson", 3, 85000, "Software Engineering")
intern = Intern("Sarah Lee", 4, 50000, "University of California")
print(employee.calculate_pay())
print(manager.calculate_pay())
print(engineer.calculate_pay())
print(intern.calculate_pay())


#Intermediate
class Vehicle():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def __repr__(self):
        return f"This vehicle is a {self.make} {self.model}, model year {self.year}"

class Car(Vehicle):
    def __init__(self, make, model, year, number_of_doors):
        super().__init__(make, model, year)
        self.number_of_doors = number_of_doors
    def __repr__(self):
        return super().__repr__ () + f" and has {self.number_of_doors} doors"

class Truck(Vehicle):
    def __init__(self, make, model, year, payload_capacity):
        super().__init__(make, model, year)
        self.payload_capacity = payload_capacity
    def __repr__(self):
        return super().__repr__ () + f" and has a payload capacity of {self.payload_capacity}"

bmw = Car("BMW", "328d", "2005", "4-doors")
print(bmw)
toyota = Truck("Toyota", "Hilux", "2015", "1 Ton")
print(toyota)


#Beginner
class Book():
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
    def __repr__(self):
        return f"Book- {self.title}, Author- {self.author}, ISBN- {self.isbn}"

ToKillAMockingbird = Book("To Kill a Mockingbird", "Harper Lee", "9780060935467")

print(ToKillAMockingbird)
'''