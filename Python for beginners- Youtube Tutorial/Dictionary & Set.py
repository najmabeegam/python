#DICTIONARY: store data values in key:value pairs.
#undordered, mutable, & don't allow duplicate keys.

info = {
    "key" : "value",
    "name" : "najma",
    "age" : "27",
}
print(info)
print(info["key"])
print(info["name"])

#Nested Dictonary:

student = {
    "name" : "najma beegam",
    "subjects" : {
        "phy" : 97,
        "chem" : 98,
        "math" : 95
    }
}

print(student)

#Methods:

student = {
    "name" : "najma beegam",
    "subjects" : {
        "phy" : 97,
        "chem" : 98,
        "math" : 95
    }
}
print(student.keys())
print(student.items())
print(student.items())
student.update({"city" : "delhi"}) #updates the dictonary
print(student)

#SET: collection of unordered items. there is no order.
#each element in the set must be unique & immutable.
#repeated elemets stored only once.

collection = {1, 2, 3, 4, "hello world"}
print(collection)
print(type(collection))

#empty set:
collection1 = set()
print(type(collection1))

#Methods:
#sets are mutable but elements in the sets are immutable.
collection2 = set()
collection2.add(1)
collection2.add(2)
collection2.add("najma")
collection2.remove(2) #remove
collection2.clear() #clear
collection2.pop() #pops up the value.
print(collection2)

#union: combines both set values & returns new. duplicates will be count as 1.
#intersection: combines common values & returns new
set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1.union(set2))
print(set1.intersection(set2))