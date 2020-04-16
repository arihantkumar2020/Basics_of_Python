class Student:

    #static or class variable
    school = 'telusko'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):   #instance method, because we are passing self
        #types of instance methods
        #accessor methods(or accessors), if we are only fetching the values
        #mutator methods(or accessors), if we are modifying values
        return (self.m1 + self.m2 + self.m3)/3

    def get_m1(self):   #this type of method also known as getters(or accessors)
        return self.m1

    def set_m1(self, value):    #this type of method also known as setters(or mutators)
        self.m1 = value

    @classmethod        #decorators, to work with class methods
    def getSchool(cls):  #it is a class method, cls for working with class variable, self for working with instance variable
        return cls.school

    @staticmethod       #to work with static methods
    def info():     #static method
        print('This is a student class')




s1 = Student(40, 45, 60)
s2 = Student(65, 70, 89)

print(s2.avg())
print(Student.getSchool())

Student.info()