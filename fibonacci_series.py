def fib(num):
    a=0
    b=1
    if num<0:
        print("Fibonacci series cannot be printed.")
    elif num==0:
        print()
    elif num==1:
        print(a)
    else:
        print(a, end='  ')
        print(b, end='  ')
        for i in range(num-2):
            c=a+b
            print(c, end='  ')
            a=b
            b=c
        print()



print("Printing fibonacci series:")
num = int(input("how many numbers you wanna print? "))
print()
fib(num)
print("\nPrinting series completed...")