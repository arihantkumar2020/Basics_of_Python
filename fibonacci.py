a: int=0
b=1
print("0 1 ", end='')
for i in range(0, 25):
    c=a+b
    print(c, end=' ')
    a=b
    b=c
