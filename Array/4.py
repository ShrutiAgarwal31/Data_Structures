# rotate array by n

from collections import deque

def rotate(Arr, n):
    deq_arr = deque(arr)
    deq_arr.rotate(n)
    return deq_arr


arr = [1,2,3,4,5]
print(rotate(arr, -2))
print(rotate(arr, 1))