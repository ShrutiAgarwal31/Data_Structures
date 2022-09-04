"""
List are ordered.
If two list are same but
the order of the elements are different,
that implies the lists are not equal
"""

list_1 = [1,2,3,4,5]
list_2 = [5,4,3,2,1]
if(list_2==list_1):
    print(True)
else:
    print(False)