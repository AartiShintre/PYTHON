collection = set()
print(type(collection))  # set is mutable; we can change the values
#set is mutable
#elements of set is imutable

#set methods
collection.add(1)
collection.add(2)
collection.add(2)
print(collection)
collection.remove(1)
print(collection)
#collection.clear()
#print(collection)
print(collection.pop())

#union
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set1.union(set2)
print(set3)
set4 = set1.intersection(set2)
print(set4)

#WAP to store 9 and 9.0 seperatly inside the set
# 1st approch
set ={ 9, "9.0"}
print(set)

# 2nd approch
values = {
    ("float", 9.0),
    ("int", 9)
}
print(values)