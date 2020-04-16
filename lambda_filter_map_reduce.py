from functools import reduce

#use of lambda function with filter function
#filter() function is used to filter the sequence on the basis of condition
nums = [3, 1, 4, 6, 5, 7, 9, 10]
evens = list(filter(lambda a : a%2==0, nums))
print(evens)

#with map() function
#to modify all value in a sequence at once, we use mapping
doubles = list(map(lambda a : a*2,evens))
print(doubles)


#with reduce function()
#reduce() function is used to reduce a sequence to a single numerical value
sum = reduce(lambda a,b : a+b, doubles)
#or sum = reduce(add_all, doubles)
print(sum)