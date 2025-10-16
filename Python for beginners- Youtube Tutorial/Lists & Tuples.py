#LISTS: A build-in data that stores set of values. can store diff. types of value.

marks = [45.9, 95.6, 88.0, 73.5, 90.0]
print(marks)
print(type(marks))
print(marks[1])  #index
print(marks[0])
print(len(marks))


student = ["Karan", 95.0, "Delhi"]
print(student)

#lists are mutable.
#List Slicing can be done similar to string slicing.

#List Methods:

#1. Append:
list = [2, 1, 3]
list.append(5)
print(list)

#2. Sort: ascending and descending:
list = [2, 1, 3]
# print(list.sort())
print(list.sort(reverse=True))
print(list)

#3. Reverese:
list = [2, 1, 3]
list.reverse()
print(list)

#4. Insert: insert element at index
list = [2, 1, 3]
list.insert(2, 5)
print(list)

#5. Remove & Pop:
list = [2, 1, 3]
list.pop(2) #remove element at index.
print(list)

#TUPLES: build-in data type that let us create immutable sequences f values.

tup = (2, 1, 3, 4) #use perentesis
tup1 = (1,)
print(tup1)
print(type(tup))

#methods: index & count

#PRACTICE QUESTIONS:

#1.WAP to ask the user to enter names of their 3 fav movies & store them in a list.

fav = ["swades" , "indian", "happy"]
print(fav)
print(type(fav))



