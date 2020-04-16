def factorialofnum(num):
    if num==0 :
        return 1

    return num*factorialofnum(num-1)


print("Finding factorial using recursion : ")
num = int(input("Enter a number : "))
factorial = factorialofnum(num)
print("Factorial of the number :", factorial)