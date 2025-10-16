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
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b) #remainder
print(a ** b) #power to

#Comparison/Relational Operator:
a = 50
b = 20
print(a == b) #equivalency       
print(a != b) #not equal to       
print(a >= b) #greater than or equal to
print(a > b)  #greater than


#Assignment Operators:
num = 10
num = num + 10
num +=10  #assignment operator
num -=10
num *=10
num /=5
print("num : ", num)

#Logical operators: not, and, or

#1.NOT
a = 50
b = 30
print(not False)
print(not True)
print(not (a > b))

#2.AND
val1 = True
val2 = True
print("and operator:", val1 and val2)

#type conversion:
a = 2
b = 4.25
sum = a + b #float is superior to int
print(sum)
 #can only concatenate str, not float to str
 #for that we need to use "TYPE CASTING"
 


