# print alternate elements of array

def alternate(arr):
    new_arr = []
    for i in range(0, len(arr), 2):
        new_arr.append(arr[i])
    return new_arr

arr = [1,2,3,4,5,6,7]
print(alternate(arr))
