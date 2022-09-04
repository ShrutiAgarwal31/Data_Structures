"""
set are un-ordered.
mutable.
the elements of the set are immutable.
cannot be nested. why?
--> sets are mutable and sets do not include the mutable elements
"""
set1 = {1,2,3}
set2 = {1,2,3,1,2,3}

if(set2==set1):
    print(True)
else:
    print(False)

set1.add(55)
print(set1)

set3 = {1,2,3,{4,5,6}}
print(set3)
