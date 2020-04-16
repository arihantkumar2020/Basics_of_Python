class PyCharm:
    def execute(self):
        print('compiling')
        print('running')

class MyEditor:
    def execute(self):
        print('spell check')

class Laptop:
    def code(self, ide):
        ide.execute()   #doesn't matter to which class ide belongs, but it should have a method name execute(), it is duck typing

ide = PyCharm()
lap1 = Laptop()
lap1.code(ide)