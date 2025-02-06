from numpy import *


# arr1 = array([1,2,3,4,5])


# arr1 = arr1 + 5

# print(arr1)


# arr2 = array([1,2,3,4,5])

# arr3 = arr1 + arr2

# print(arr3)

# print(sqrt(arr3))
# print(min(arr3))
# print(max(arr3))
# print(log(arr3))


# print(concatenate([arr1,arr2]))


arr4 = array([1,2,3,9,5])

arr5 = arr4.view() ###another adress shallow copy

arr4[1] = 9

print(arr4 , arr5)
print(id(arr4 ), id(arr5))




arr6 = array([1,2,3,9,5])

arr7 = arr6.copy() ###another adress deep copy
arr6[1] = 9

print(arr6 , arr7)
print(id(arr6 ), id(arr7))
