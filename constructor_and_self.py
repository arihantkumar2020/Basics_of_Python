class Computer:
    def __init__(self):
        self.name = 'arihant'
        self.age = 28

    def update(self):
        self.age = 30

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            False


c1 = Computer()
c2 = Computer()

#to compare objects we can define our won function
if c1.compare(c2):
    print("both objects are same")

print(c1.name)
print(c2.name)