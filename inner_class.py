class Student:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()

    #inner class
    class Laptop:
        def __init__(self):
            self.brand = 'lenovo'
            self.cpu = 'i5'
            self.ram = 8

        def show(self):
            print(self.brand, self.cpu, self.ram)



s1 = Student('arihant', 2)
s2 = Student('kumar', 3)

print(s1.lap.brand)

lap1 = s1.lap
lap2 = s2.lap

print(lap1.cpu)
print(lap2.ram)

lap3 = Student.Laptop()
lap3.show()

s1.show()