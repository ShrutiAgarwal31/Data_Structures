# in-place
# stable sort
# Time Complexity : O(n2)
def insertion_sort(lst):

    size = len(lst)

    for i in range(1, size):
        key = lst[i]
        j = i-1

        while j >= 0 and key < lst[j]:
            lst[j+1], lst[j] = lst[j], key
            # lst[j + 1], lst[j] = lst[j], lst[j+1]
            j -= 1
        print("pass: {}-->{}".format(i, lst))
    return lst






if __name__ == "__main__":
    lst = [12, 6, 22, 14, 8, 17]
    print(insertion_sort(lst))
