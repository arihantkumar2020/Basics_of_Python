def person(name, **data):
    print(name)
    print(data)
    for i,j in data.items():
        print(i, j)

person('arihant', age=20, city='muradnagar', mobile=98765430)