
# stable sort i.e. items with the same value will maintain their relative order in the list.
# in-place sorting
# number of comparisons in general: n(n-1)/2
# Time Complexity: O(n2)

def bubble_sort(lst):
    size = len(lst)
    swaps = 0

    for i in range(size-1):
        swapping = False
        for j in range(size-1-i):
            if lst[j] > lst[j+1]:
                 lst[j], lst[j+1] = lst[j+1], lst[j]
                 swaps += 1
                 swapping = True

        if swapping == False:
            return swaps, lst

        print("pass: {} --> {}".format(i+1, lst))

    print("swaps: ", swaps)
    return lst

if __name__ == "__main__":
    lst = [12, 6, 22, 14, 8, 17]
    print(bubble_sort(lst))
