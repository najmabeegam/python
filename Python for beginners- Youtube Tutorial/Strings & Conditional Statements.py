# Strings:
# - can be stored in single double or triple quotes
# ESCAPE SEQUENCE CHARACTERS: used for formatting

str1 = "This is a string. We are creating it in python."
print(str1)

#if the second sentence has to be printed next line use \n.
#\t: tab space

str1 = "This is a string. \nWe are creating it in python."
print(str1)

#CONCATENATION:
#hello + world = helloworld

str1 = "Najma "
str2 = "Beegam"

print(str1 + str2)

#LENGTH:
len(str)

str1 = "Najma "
print(len(str1))

str2 = "Beegam"
print(len(str2))
                       #OR

str1 = "Najma "
len1 = len(str1)
print(len(str1))

str2 = "Beegam"
len2 = len(str2)
print(len(str2))
final = (str1 + str2)
print(final)
print(len(final))


#INDEXING:
# # starts with 0

str = "najma beegam"
ch = str[0]
print(ch)
print(str[4])

#SLICING:
#accessing parts of the str
# str[starting_idx: ending_idx]

str = "najma beegam"
print(str[1 : 4])
print(str[ : 4]) #starts with 0
print(str[1 : len(str)]) #until last of the str
print(str[1 : ])               

#negative index: counts backwards; starts with -1, -2 and so on.

str1 = "apple"
print(str1[-3:-1])

#FUNCTIONS:

#endswith
str = " My name is Najma" 
print(str.endswith("jma"))

#capitalize
str = " my name is Najma"
print(str.capitalize())

#replace
str = " my name is Najma"
print(str.replace("a", "o"))

#find
str = " my name is Najma"
print(str.find("a")) #first index of first occurence

#count
str = " my name is Najma"
print(str.count("a")) 


#PRACTICE QUESTIONS:

# 1. WAP to input user's first name & print its length?

name = input("first name is : ")
print(len(name))

# 2. WAP to find the occurence of '$' in a string?
str = "$$$$$$$"
print(str.count("$"))

#CONDITIONAL STATEMENTS:
#IF-ELIF-ELSE (SYNTAX)- rules of programming

# 1. if:
age = 21

if(age >=18):
    print("can vote")
    print("can drive")

# 2. elif:
light = "green"

if(light == "red"):
    print("stop")
elif(light == "green"):
    print("go")
elif(light == "yellow"):
    print("wait")

# 3. else: can be written only once and at the last

light = "blue"

if(light == "red"):
    print("stop")
elif(light == "green"):
    print("go")
elif(light == "yellow"):
    print("wait")
else:
    print("light is broken")

#indentation means proper spacing.

#PRACTICE QUESTIONS:

# 1.  mark = 82

if(mark >= 90):
    print("Grade A")
elif(mark >=80 and mark <90):
    print("Grade B")
else:
    print("Grade C")

#nesting: writing one statement within another
age = 34

if(age >= 18):
    if(age >= 18):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")

# 2. WAP to check if a number entrered by the user is odd or even?

num = 14
rem = num % 2

if(rem == 0):
    print("even")
else:
    print("odd")

# 3. WAP to find the greatest of 4 numbers entered by the user?

a = int(input("first number: "))
b = int(input("second number: "))
c = int(input("third number: "))
d = int(input("fourth number: "))

if(a >= b and a >= c):
    print("first number is greatest", a)
elif(b >=a and b >=c):
    print("second number is greatest", b)
elif(c >=a and c >=b and c>=d):
    print("third number is greatest", c)
else:
    print("fourth is the largest", d)

# 4. WAP to check if a number is a multiple of 7 or not?
a = 7

if(a % 7 == 0):
    print("yes")
else:
    print("no")


