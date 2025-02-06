#  https://docs.python.org/3/library/array.html

from array import *


values = array('i',[5,7,9,45,6])

# print(values)


# values = array('i',[5,7,9,45,6])

# values.reverse()
# print(values)


# print(values[1])


# for i in range(len(values)):
#     print(values[i],end="   ")

# print()

# for e in values:
#     print(e,end= "  ")

# print()

# ch = array('u',['a','b','c','f','e'])


# for f in ch:
#     print(f , end= "    ")


newArr = array(values.typecode,(a*a for a in values))

for x in newArr :
    print(x, end= " ")

