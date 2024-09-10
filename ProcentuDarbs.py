class Student:
    def __init__(self, name, year, grades = []):
        self.name = name
        self.year = year
    def add_grade(self, grade):
        if type(grade) == grade:
            self.grades.append()
        else:
            pass

roger = Student("Roger van der Weyden", 10)
sandro =Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)

class Grade:
    def minimum_passing(self):
        minimum_passing = 65
    def score(self, score):
        self.score = score

Grade = 100
pieter.add_grade(Grade)