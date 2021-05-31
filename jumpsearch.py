from math import sqrt
from random import shuffle

def JumpSearch(arr, item):
    n, prev =  len(arr), 0
    step = sqrt(n)

    while arr[int(min(step, n)-1)] < item:
        prev = step
        step += sqrt(n)

        if prev >= n:
            return False

    while arr[int(prev)] < item:
        prev += 1

        if prev == min(step, n):
            return -1

    if arr[int(prev)] == item:
        return prev
    else:     
        return False
 
# Driver code to test function
arr = [ 0, 1, 1, 2, 3, 5, 8, 13, 21,
    34, 55, 89, 144, 233, 377, 610 ]
shuffle(arr)
item = 5
index = JumpSearch(arr, item)

if index:
    print("Number" , item, "is at index" ,"%.0f"%index)
else:
    print("Not Found")