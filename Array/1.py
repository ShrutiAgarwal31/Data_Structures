def insert_element(Arr, x, idx):
    for i in range(len(Arr)+1):
        if i == idx:
            Arr.insert(idx, x)
            print(Arr)

    pass

def search_element(Arr, x):
    for i in Arr:
        if x == i:
            return "TRUE"
    return "FALSE"

def delete_element(Arr, x):
    for i in Arr:
        if x == i:
            Arr.pop(Arr.index(i))
            return "TRUE"
    return "FALSE"

arr = [1,2,3,4,5,6,7]
print("OG: ", arr)
print(search_element(arr, 1))
print(search_element(arr, 11))
print(delete_element(arr, 2))
print(delete_element(arr, 22))
insert_element(arr, 222, 1)
insert_element(arr, 69, 4)


