#Python for Beginners Youtube Tutorial
#Basics:

# Task1: Calculate SIMPLE INTEREST (SI) = PxRxT/100
p = float(input("p : "))
r = float(input("r : "))
t = float(input("t : "))
si = (p*r*t)/100
print(si)

# Task2: Arithmatic operators
a = 5
b = 2
sum = a + b
print(sum)

# INPUT IN PYTHON

name = input("enter your name: ")
print("Welcome", name)

# input() -str
# int(input()) -integers
# float(input()) - float

name = input("enter name: ")
age = int(input("age is: "))
marks = float(input("mark is: "))

print("Welcome", name)
print("age is", age)
print("marks is", marks)
print(type(age))


#Practice Questions:

# 1. Write a program tto input 2 numbers & print their sum?

a = int(input("value of a is: "))
b = float(input("value of b is: "))
sum = (a + b)
print(sum)

# 2. WAP to input side of a square & print its area?

x = int(input("side of the square: "))
Area = (x*x)
print("The area of the square is ", Area)

# 3. WAP to input 2 floating point numbers & print their average?

flt1 = float(input("float 1 is : "))
flt2 = float(input("float 2 is : "))
print("Average = ", (flt1 + flt2)/2)

# 4. WAP to input 2 int numbers, a and b. Print True if a greater than or equal to b. If not print False?

a = int(input("a = "))
b = int(input("b = "))

print(a >= b)

 