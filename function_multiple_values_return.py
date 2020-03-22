
def mul_div(m, n):
    e = m*n
    f = m/n
    return e, f

mul, div = mul_div(5, 2)   #function returning multiple values
print("Multiplication =", mul)
print("Division =", div)