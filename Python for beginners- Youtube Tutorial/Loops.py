#LOOPS: used to repeat instructions like a loop. inorder to stop the loop we need to provide a false statement.
#each loop is called an Iteration.
#2 types: while & for
#while condition: #some work

count = 1
while count <= 5 :
    print("hello")
    count += 1
print(count)

i = 1
while i <=5 :
    print("True", i)
    i+=1

#PRACTICE QUESTIONS:

#1. Print numbers from 1-100?
j = 1
while j <= 100 :
    print(j)
    j += 1

#2. Print numbers from 100-1?
k = 100
while k >= 1 :    # stopping condition
    print(k)
    k -= 1

#3. Print the multiplication table of a number n.
n = int(input("Enter num: "))
i = 1
while i <= 10:
    print(n*i)
    i += 1


# Break & Continue:
#- Break: terminate the loop when encountered.
#- Continue: terminates execution in the current iteration & continues execution of the loop with next iteration.

i = 1
while i <=5 :
    print(i)
    if(i== 3):
        break
    i+=1

nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 36)

x = 36
w = 0
while w < len(nums) :
    if(nums[w] == x) :
        print("FOUND at idx", w)
        break
    else:
        print("finding..")
        w += 1
print("end of loop")

#continue:
i = 0
while i <=5 :
    if(i== 3):
        i +=1
        continue #skips and follows the rest.
    print(i)
    i +=1

#FOR LOOPS: used for sequential traversal.

letters = ["a", "b", "c", "d", "e"]

for val in letters:
    print(val)

#PRACTICE QUESTIONS:

#WAP to find the sum of first n numbers. (using while)?
n = 5
sum = 0
for i in range(1, n+1):
    sum += i

print("total sum =", sum)