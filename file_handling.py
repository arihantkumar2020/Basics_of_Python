#to store data in a persistent way, in a long period
#so we can use file handling, there are other methods as well
#it is simple

f = open('sampleData', 'r')
print(f.readline(5), end = '')      #to read 1 line, to run all data use read()

f1 = open('anotherData', 'a')
f1.write('something')
f1.write('laptop')

for data in f:
    f1.write(data)

f2 = open('comp.jpg', 'rb')
f3 = open('secondmg.jpg', 'wb')

for i in f2:
    f3.write(i)

f.close()
f1.close()
f2.close()
f3.close()