# Python program to find an element x
# in a sorted array using Exponential Search
 
# A recurssive binary search function returns
# location  of item in given array arr[l..r] is
# present, otherwise -1
def ExponentialSearch(arr, item):
    n = len(arr)

    def binarySearch( arr, l, r, item):
        if r >= l:
            mid = l+(r-l)//2
            
            if arr[mid] == item:
                return mid

            if arr[mid] > item:
                return binarySearch(arr, l, mid-1, item)

            return binarySearch(arr, mid+1, r, item)

        return -1

    if arr[0] == item:
        return 0

    i = 1

    while i < n and arr[i] <= item:
        i *= 2

    return binarySearch(arr, i//2, min(i, n-1), item)

# Driver Code
arr = [2, 3, 4, 10, 40]
item = 10

result = ExponentialSearch(arr, item)
if result == -1:
    print "Element not found in thye array"
else:
    print "Element is present at index %d" %(result)