class Person:

    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def name(self):
        return self.firstname + " " + self.lastname


class Employee(Person):

    def __init__(self, first, last, age):
        Person.__init__(self, first, last)
        self.age = age

    def get_employee(self):
        return self.name() + ", " + self.age


x = Person("Marge", "Simpson")
y = Employee("Homer", "Simpson", "53")

print(x.name())
print(y.get_employee())
