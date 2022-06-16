# Time Complexity:
# case 1: element is present in the list
#        --> best case: O(1) i.e. the element is the first element of the list
#        --> worst case: O(n) i.e. the element is the last element of the list
# case 2: element is not present in the list
#        --> best case: O(n) i.e. search the entire list
#        --> worst case: O(n) i.e. search the entire list

def linear_search(val, lst):
    found = False
    numOfComputations = 0
    for num in lst:
        numOfComputations += 1
        if num == val:
            found = True
            return "{} found at index: {}.\nNum of computations required: {}".format(num, lst.index(num), numOfComputations)

    return  "\n{} is not presemt in the list.".format(num)

if __name__ == "__main__":

    lst = [10, 20, 30, 40, 11, 22, 33, 44]
    print(linear_search(11, lst))
    print(linear_search(100, lst))
