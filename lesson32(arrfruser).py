
from array import *

arr = array('i',[])



x = int(input("Enter length of the array  :  "))

for i in range(x):
    arr.append( int(input("Enter your numbers  :  ")))
    
print(arr)
print("bye")


val = int(input("Enter the value for search : "))

k = 0

for e in arr :
    if e == val :
        print(k)
        break
    k += 1