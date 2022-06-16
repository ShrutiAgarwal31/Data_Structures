# items must be sorted
# only useful when we have random access in O(1) time ti the list elements by index
# divide and conquer strategy.
# when is element not present in the list? --> when last < first
# number of comparisons required to find an element: log2(n)
# Time complexity:
# case 1: element is present in the list
#        --> best case: O(1) i.e. the element is present in the middle of the list
#        --> worst case: O(log2(n))
# case 2: element is not present in the list
#        --> best case: O(log2(n))
#        --> worst case: O(log2(n))

def binary_search(val, lst):
    found = False
    first = 0
    last = len(lst) - 1
    numOfComparisons = 0

    while first <= last and not found:
        mid = (first + last) // 2
        numOfComparisons += 1

        if val < lst[mid]:
            last = mid - 1
        elif val > lst[mid]:
            first = mid + 1
        else:
            found = True
            return "\n{} found at position: {}\nNumber of Comparisons Required: {}".format(val, mid, numOfComparisons)

    return "\n{} not present in the list.".format(val)

if __name__ == "__main__":
    lst = [3, 5, 6, 8, 91, 123, 123, 332]
    print(binary_search(332, lst))
    print(binary_search(91, lst))
    print(binary_search(22, lst))
