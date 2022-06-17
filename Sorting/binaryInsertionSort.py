def binary_search(first, last, val, lst):
    mid = 0

    if first == last:
        if lst[first] > val:
            return first
        else:
            return first + 1

    if first <= last:
        mid =(first + last) // 2
        if val < lst[mid]:
            return binary_search(first, mid-1, val, lst)
        elif val > lst[mid]:
            return binary_search(mid+1, last, val, lst)
        else:
            return mid
    else:
        return -1


def insertion_sort(lst):
    size = len(lst)

    for i in range(1, size):
        j = i-1
        key = lst[i]
        loc = binary_search(0, j, key, lst)
        while j >= loc:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key
    return lst


if __name__ == "__main__":
    # lst = [1,2,3,4,5,6]
    lst = [37, 23, 0, 17, 12, 72, 31, 46, 100, 88, 54]
    print(insertion_sort(lst))
    # print(binary_search(0, len(lst)-1, 3, lst))
    # print(binary_search(0, len(lst) - 1, 33, lst))