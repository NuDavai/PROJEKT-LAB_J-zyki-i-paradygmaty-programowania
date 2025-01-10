class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Chuck", 30)
print(f"Cześć, jestem {p1.name} i mam {p1.age} lat")
print(p1)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Mam na imie {self.name} i mam {self.age} lat"

p1 = Person("Chuck", 30)
print(p1)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Mam na imie {self.name} i mam {self.age} lat"

    def rokUrodzenia(self):
        print(f"Urodziłem się w {2024-self.age} roku")

p1 = Person("Chuck", 30)
p1.rokUrodzenia()


print(p1.age)
p1.age = 40
print(p1.age)
del p1.age

p1.age = 30
print(p1.age)

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(f"First name: {self.firstname}, Lastname: {self.lastname}")

personJohn = Person("John", "Dzwon")
personJohn.printname()

class Student(Person):
    pass

studentJanek = Student("Janek", "Chrzanek")
studentJanek.printname()

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print(f"Welcome student {self.firstname} {self.lastname} to the class of {self.graduationyear}")

studentJanek = Student("Janek", "Chrzanek", 2019)
studentJanek.printname()
studentJanek.welcome()