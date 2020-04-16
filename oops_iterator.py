'''nums = [7, 8, 9, 5]

it = iter(nums)
print(it.__next__())
print(it.__next__())
print(next(it))


'''

class TopTen:
    def __init__(self):
        self.num = 1

    def __iter__(self):     #gives iterator
        return self

    def __next__(self):     #gives next value
        if self.num <= 10:
            val = self.num
            self.num+=1
            return val
        else:
            raise StopIteration     #exception

values = TopTen()

print(values.__next__())
print(next(values))

for i in values:
    print(i)