#Q1) A school has following rules for grading system:
#  a. Below 25 - F
#  b. 25 to 45 - E
#  c. 45 to 50 - D
#  d. 50 to 60 - C
#  e. 60 to 80 - B
#  f. Above 80 - A
# Ask user to enter marks and print the corresponding grade.
print("\nAns 1)")
marks=int(input("Enter marks of the student: ")) #prompt to enter marks for the student by the user.
if marks < 25:       #condition for 'F' grade.
    print("GRADE: F")
elif marks>=25 and marks<45: #condition for 'E' grade.
    print("GRADE: E")
elif marks>=45 and marks<50: #condition for 'D' grade.
    print("GRADE: D")
elif marks>=50 and marks<60: #condition for 'C' grade.
    print("GRADE: C")
elif marks>=60 and marks<=80: #condition for 'B' grade.
    print("GRADE: B")
else:                #condition for 'A' grade.
    print("GRADE: A")


#Q2)  A year is a leap year if it is divisible by 4, except that years divisible by 100 are not leap years unless they are also divisible by 400. Write a program that asks the user
#   for a year and prints out whether it is a leap year or not.
print("\nAns 2)")
year= int(input("\nEnter a year: "))#prompt to enter a year.
if year%100==0: #Check for year divisible by 100
    if year%400==0: #Condition for leap year
        print("Leap Year")
    else:
        print("Not a leap year")
else:
    if year%4==0: #Condition for leap year
        print("Leap Year")
    else:
        print("Not a leap year")


#Q3)  Write a multiplication game program for kids. The program should give the player
# ten randomly generated multiplication questions to do. After each, the program
# should tell them whether they got it right or wrong and what the correct answer is.
# Question 1: 3 x 4 = 12
# Right!
# Question 2: 8 x 6 = 44
# Wrong. The answer is 48.

print("\nAns 3)")
import random #importing random library
count=1 #initializing count
while count < 11: #condition to iterate the loop 10 times.
        number_1 = random.randint(1,10)
        number_2 = random.randint(1,10)
        guess = int(input("\nWhat is " + str(number_1) + " x " + str(number_2) + " = ")) #Question seen by user.
        answer = (number_1*number_2)
        if guess==answer:
            print("Right!") #response by program
        else:
            print("Wrong. The answer is", answer)  #response by program
        count += 1



#Q4) A jar of Halloween candy contains an unknown amount of candy and if you can guess exactly how much candy is in the bowl, then you win all the candy. You ask
#   the person in charge the following: If the candy is divided evenly among 5 people, how many pieces would be left over? The answer is 2 pieces. You then ask about
#   dividing the candy evenly among 6 people, and the amount left over is 3 pieces. Finally, you ask about dividing the candy evenly among 7 people, and the amount
#   left over is 2 pieces. By looking at the bowl, you can tell that there are less than 200 pieces. Write a program to determine how many pieces are in the bowl.
print("\nAns 4)")
for i in range(200):
    if i % 5 == 2:
         if i % 6 == 3:
             if i % 7 == 2:
                 print("\nThere are ", i, ' candies are in the bowl!')
        
   
     
    














        



    
