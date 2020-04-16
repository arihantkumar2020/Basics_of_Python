def person(name, age=20):      #a and b are formal arguments, age has a default value here
    print(name)
    print(age)

def sum(a, *b):
     c = a
     for i in b:
         c += i
     print(c)


#types of actual arguments

#position arguments - maintains sequence
person('arihant', 21)           #5 and 6 are actual arguments

#keyword arguments - in case we don't know the sequence
person(age=20, name='arihant')

#default arguments - assigning default value to formal argument
person('arihant')

#variable length arguments - when number of parameters passed is not fixed
sum(5, 6, 34, 78)