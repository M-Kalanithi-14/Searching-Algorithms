from random import shuffle

def FibonacciSearch(arr, item):
    if item in arr:
        m2, m1, n = 0, 1, len(arr)
        m = m2+m1

        while (m < n):
            m2, m1 = m1, m
            m = m2+m1

        offset = -1

        while (m > 1):
            i = min(offset+m2, n-1)

            if (arr[i] < item):
                m, m1 = m1, m2
                m2 = m-m1
                offset = i
            elif (arr[i] > item):
                m = m2
                m1 -= m2
                m2 = m-m1
            else:
                return i

        if m1 and (arr[n-1] == item):
            return n-1
    else:
        return False
 
# Driver Code
arr = [10, 22, 35, 40, 45, 50,
       80, 82, 35, 90, 100,235]
shuffle(arr)
item = 35
index = FibonacciSearch(arr, item)

if bool(index):
    print("Found at index :", index)
    print(arr)
else:
    print(item, "isn't present in the array")