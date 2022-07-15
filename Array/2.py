# second maximum number of array

def sec_max(arr):
    for i in arr:
        arr.pop(arr.index(max(arr)))
        return max(arr)

arr = [1,2,3,6,4,5]
print("MAX: ", max(arr))
print("SECOND MAX: ", sec_max(arr))