# Tuple method

# count
tuple = (2, 4, 5, 6, 2, 3, 4, 4, 7)
count = tuple.count(4)
print(count)

my_tuple = ('a', 1, 'f', 'a', 5, 'a')
print(my_tuple.count('a'))

# len
bike = ('yamaha', 'honda', 'tvs', 're')
print(len(bike))

# min
tuple = (9, 11, 22, 45, 33, 5, 17, 30)
x = min(tuple)
print(x)

# max
tuple = (9, 11, 22, 45, 33, 5, 17, 30)
x = max(tuple)
print(x)

# sum
tyuples = (2, 4, 6, 8, 10)
tptal = sum(tyuples)
print(tptal)

tuple = (2, 4, 6, 8, 10, 20)
sum = 0
for num in tuple:
    sum = num + sum
    print(sum)

# sort
animals = ('lion', 'cat', 'elephant', 'tiger', 'beer', 'horse')
print(sorted(animals))

# del
x = (2, 4, 6, 8, 10)
print(x)
# del(x)
# print(x)

# looptuple
list_of_tuple = []
for i in range(5):
    a_tuple = (i, i + 1)
    list_of_tuple.append(a_tuple)
    print(list_of_tuple)
