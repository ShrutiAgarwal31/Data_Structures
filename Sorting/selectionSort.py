# orders a list of values by repeatedly putting the smallest( or largest) unplaced value into its final position.
# not a stable sort.
# Time Complexity -
# best case --> O(n2) i.e array is already sorted
# worst case --> O(n2) i.e array is in descending order
# best case --> O(n2) i.e array is already sorted

def selection_sort(lst):

    for i in range(len(lst)):
        min_idx = i

        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_idx]:
                min_idx = j

        lst[i], lst[min_idx] = lst[min_idx], lst[i]
        print("Pass {}: {}".format(i, lst))

    return lst

if __name__ == "__main__":
    lst = [12, 6, 22, 14, 8, 17, 16]
    print(selection_sort(lst))
