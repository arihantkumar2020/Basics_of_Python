class A:
    def feature1(self):
        print('feature 1 working')

    def feature2(self):
        print('feature 2 working')

class B(A):     #single level inheritance
    def feature3(self):
        print('feature 3 working')

    def feature4(self):
        print('feature 4 working')

class C(B):     #multi level inheritance
    def feature5(self):
        print('feature 5 working')

class E:
    def feature7(self):
        print('feature 7 working')

class D(A, E):  #multiple inheritance
    def feature6(self):
        print('feature 6 working')

a1 = A()
a1.feature1()

b1 = B()
b1.feature1()

c1 = C()
c1.feature1()

d1 = D()
d1.feature7()