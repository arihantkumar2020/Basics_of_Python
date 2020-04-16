class A:
    def __init__(self):
        print('in A init')

    def feature1(self):
        print('feature 1 working')

class B(A):

    def __init__(self):
        print('in B init')
        super().__init__()

    def feature3(self):
        print('feature 3 working')

    def feature4(self):
        print('feature 4 working')

class D:
    def __init__(self):
        print('in D init')

    def feature1(self):
        print('feature 1 - d')

class C(A, D):
    def __init__(self):
        super().__init__()
        print('in C init')



b1 = B()
c1 = C()
c1.feature1()