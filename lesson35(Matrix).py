from numpy import *

arr1 = array([
    [1,2,3,4,5,9],
    [5,7,8,6,4,4]
])


# print(arr1)
# print(arr1.dtype)
# print(arr1.shape)       #rows and columns
# print(arr1.ndim)        #gives dimentions of the array


# arr2=arr1.flatten()    #changes the 2d to 1d

# print(arr2)     


# arr3= arr2.reshape(3,4)

# print(arr3)


# arr3.flatten()

# print()

# arr4 = arr3.reshape(2,2,3)

# print(arr4)


# m = matrix(arr1)

# print(m)


m1 = matrix('1 2 3 ; 4 5 6; 8 6 3 ')
m2 = matrix('5 7 4 ; 2 7 9; 1 6 2 ')


m3 = m1 * m2

m4 = m1 + m2

print(m3)

print(m4)


