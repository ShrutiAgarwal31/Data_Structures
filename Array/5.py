# remove duplicate elements from array

def duplicate(Arr):
    count = 0
    new_arr = []
    for i in range(len(Arr)):
        for j in range(i+1, len(Arr)-1):
            if Arr[i] != Arr[j]:
                count += 1

    return count + 1


arr = [1, 2, 2]
print(duplicate(arr))
