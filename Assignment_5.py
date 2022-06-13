# Q1) Program to reverse the string.

print("Ans 1)")
string = input("Enter string: ") #  string variable  
print("The original string  is : ",string)   
reverse_string = ""  # empty String  
count = len(string) # Find length of a string and save in count variable  
while count > 0:   
    reverse_string += string[ count - 1 ] # save the value of str[count-1] in reverseString  
    count = count - 1 # decrement index  
print("The reversed string using a while loop is : ",reverse_string)



#  Q2) Python Program to Print all Numbers in a Range Divisible by a Given Number. (user inputs the range and the number)

print("\nAns 2)")
#The number and range provided by user.
n=int(input("Enter the number: "))
x=int(input("Enter the range: "))
print("The numbers divisible are: ")
for i in range(x):
    if i%n==0:
        print(i) #divisible number


#  Q3) 


print("\nAns3")
# Three sides of the triangle is a, b and c:  
a = float(input('Enter first side: '))  
b = float(input('Enter second side: '))  
c = float(input('Enter third side: '))

if a<b+c:
    if c<a+b:
        if b<a+c:
            # calculate the semi-perimeter  
            s = (a + b + c) / 2  
  
            # calculate the area  
            area = (s*(s-a)*(s-b)*(s-c)) ** 0.5  
            print('The area of the triangle is ',area)
        else:
            print("invalid input")
    else:
        print("invalid input")
else:
    print("invalid input")

# Q4)Write a Python program to construct the following pattern, using a nested for loop.
print("\nAns4")
n=5; 
for i in range(n):
    for j in range(i):
        print ('* ', end="") 
    print('') #to change line

for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('') #to change line

# Q5) Write a python program to print a triangular pattern of the alphabet (user input the number of rows).
#Example: Input the number of rows = 5, then the pattern should come out as given below.
#If the count of the alphabet gets exhausted, repeat the alphabet from A.
print("\nAns5")
n=int(input("number of rows: "))
x=65
# outer loop for ith rows
for i in range(0,n):
    # inner loop for jth columns
    for j in range(0,i+1):
        char = chr(x)
        print(char,end="")
        asciichr += 1
    print()

# Q6) Write a python program to print the prime numbers for a user input range.    
print("\nAns6")
# User will enter range  
lower= int(input("Please, Enter the Lowest Range Value: "))  
upper= int(input("Please, Enter the Upper Range Value: "))  
  
print("The Prime Numbers in the range are: ")  
for number in range (lower, upper + 1):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  #breaks if divisible by another number except 1 and itself.
        else:  
            print (number)


# Q7) Write a python program to find the numbers which are multiple of 7 and divisible by 11 in the range 1-500.
print("\nAns7")
for i in range(1,500):
    if i%7==0:
        if i%11==0:
            print(i)

#8 Input 10 integer values from the user. Write a python program to find and print the following:

#a. positive numbers
print("\nAns8")            
l=[]
for i in range(10):
    a=int(input("Enter value: "))
    l.append(a)
print("positive numbers")
for i in l:
    if i>0:
        print(i)
#b. negative numbers
print("negative numbers")
for i in l:
    if i<0:
        print(i)
#c. odd numbers
print("odd numbers")
for i in l:
    if i%2==1:
        print(i)
#d. even numbers
print("even numbers")
for i in l:
    if i%2==0:
        print(i)
#e. Number of times each number occurs in the List
print("Number of times each number occurs in the List")
for i in l:
    count=0
    for ele in l:
        if (ele == i):
            count = count + 1
    print("Count of",i,"=",count)
  
#9. Write a program to count the number of occurrences of each word in the list(List entered by the user).
print("\nAns9")
l=[]
n=int(input("\nlength of list: ")) #number of desired elements
for i in range(n):
    a=input("Enter value: ") #appending list
    l.append(a)


for i in l:
    count=0
    for ele in l:
        if (ele == i):
            count = count + 1
    print("Count of",i,"=",count) #count of each word





















 
