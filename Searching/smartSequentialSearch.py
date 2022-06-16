# the list is in sorted ascending order.
# Time Complexity:
# case 1: element is present in the list
#        --> best case: O(1) i.e. the element is the first element of the list
#        --> worst case: O(n) i.e. the element is the last element of the list
# case 2: element is not present in the list
#        --> best case: O(1) i.e. the target is less than the smallest(i.e. the first) element of the list
#        --> worst case: O(n) i.e. the target is greater than the smallest(i.e. the last) element of the list
def smart_sequential_search(val, lst):
    found = False
    loc = 0
    numOfComparasion = 0

    while loc < len(lst) and not found:
        if val <= lst[loc]:
            found = True

        else:
            loc += 1
            numOfComparasion += 1

    if loc == len(lst) or val not in lst:
        return "\n{} not present in list.".format(val)

    return "\n{} is present at index: {}\nNumber of Comparisons Required: {}".format(val, loc, numOfComparasion+1)

if __name__ == "__main__":
    lst = [3, 5, 6, 8, 91, 123, 123, 332]
    print(smart_sequential_search(5, lst))
    print(smart_sequential_search(91, lst))
    print(smart_sequential_search(55, lst))
    print(smart_sequential_search(332, lst))