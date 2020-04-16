def topten():
    #yield makes function as a generator
    n = 1
    #to find out square root of 10 numbers and fetching them
    while n <= 10:
        sq = n*n
        yield sq
        n+= 1



values = topten()

print(values.__next__())
print(values.__next__())

for i in values:
    print(i)