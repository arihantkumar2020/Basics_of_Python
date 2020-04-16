def factorialofnum(num):
    factorial = 1
    for i in range(2, num+1):
        factorial *= i
    return factorial


print("Calculating factorial of a number:")
num = int(input("Enter a number : "))
result = factorialofnum(num)
print("Factorial of the number", result)