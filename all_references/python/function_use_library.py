import builtins
from functools import reduce
####
# Misc
####

# Exponentation (2^4)
print(2 ** 4)

# variables
height = 1.79  # meters
weight = 74.2  # kg

bmi = weight / (height ** 2)
print(bmi)

type(bmi)

round(1.68, 1)  # 1.7
round(1.68, 1)  # 2
help(round)

# tuples
even_nums = (2, 4, 6)
print(type(even_nums))
print(even_nums)
x, y, z = even_nums
x = even_nums[0]

# comparison - Not has higher prio than and/or
x = 13
x > 5 and x < 18
x < 5 or x > 10
not(x < 5)

# loops
z = 6
if z % 2 == 0:
    print("checking " + str(z))
    print("z is even")
elif z % 3 == 0:  # never reached if also even
    print("z is divisible by 3")
else:
    print("z is odd")

# while loops
y = 50
print(str(y))
while y > 1:
    y = y / 4
    print(str(y))

# for loops - iteration
height_list = [1.73, 1.68, 1.71, 1.89]
for height in height_list:
    print(height)

for index, height in enumerate(height_list):
    print("index " + str(index) + ": " + str(height))

for letter in "family":
    print(letter.capitalize())

for x in range(10):  # 0 through 9 for 10 iterations
    print(x)

# map
result = map(lambda height: height ** 2, height_list)
print(list(result))

# filter
result = filter(lambda height: height > 1.72, height_list)
print(list(result))

# reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates ((((1+2)+3)+4)+5)
# from functools import reduce
result = reduce(lambda height_prod, height: height_prod * height, height_list)
print(result)

# builtins
# import builtins
dir(builtins)
