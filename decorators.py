#decorators are used to add extra features to a function
#suppose we want to apply divide function, now create a function which accepts 2 parameters, divide and return it
#But what if user wants the bigger number as numerator and the smaller number as denominator, irrespective of the sequence of passing parameters to the function
# ex: div(5,10) or div(10, 5) should always returns 2

def div(a, b):
    print(a/b)

def smart_div(func):
    def inner(a,b):
        if a<b :
            a,b = b,a
        return func(a,b)
    return inner

#here we are changing the definition of div, before calling the function
div = smart_div(div)
div(3,7)
