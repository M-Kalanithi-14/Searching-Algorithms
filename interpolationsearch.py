def InterpolationSearch(arr, item):
    start, end = 0, len(arr)-1

    while (start<=end):
        pos = start+((end-start)//(arr[end]-arr[start])*(item-arr[start]))

        if arr[pos] == item:
            return pos
        elif arr[pos] < item:
            start = pos+1
        else:
            end = pos-1
    else:
        return False
 
# Driver code 

arr = [10, 12, 13, 16, 18, 19, 20,
       21, 22, 23, 24, 33, 35, 42, 47]
item = 18
res = InterpolationSearch(arr, item)

if res:
    print("Element found at index", res)
else:
    print("Element not found")