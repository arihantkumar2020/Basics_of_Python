class Computer:
    def config(self):
        print("i5 machine, 8 gb ram, 1 tb")

comp1 = Computer()
comp2 = Computer()

Computer.config(comp1)
Computer.config(comp2)

comp1.config()
comp2.config()
