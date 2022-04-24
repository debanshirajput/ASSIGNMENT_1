#Q 1: Find the average of three numbers entered by the user.

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

#Average
avg = (a + b + c)/3
print("The Average of the given three numbers is:", avg)

#Q 2: Compute a person's income tax (in $).

#To compute a person's income tax (in $)
grossincome = float(input("Enter the Gross Income:"))

#Standard deduction of $10,000.
standarddeduction = 10000

n_dependents = int(input("Enter the number of dependents:"))

#$3000 deduction for each dependent.
dependentdeduction = 3000

taxableincome = grossincome - standarddeduction - (dependentdeduction * n_dependents)
print("Taxable income: ", taxableincome)

#Tax rate = 20%

Tax = (taxableincome * 20)/100
print("Tax: ", Tax)
 


#Question :3 Store different data type values into a list.

Name = input("Enter the name of the Student: ")
SID = int(input("Enter the Student ID:"))
Gender = input("Enter the gender of the Student(F,M,U): ")
Course_name = input("Enter the Student's course name: ")
CGPA = float(input("Enter the Student's CGPA: "))

Studentlist = ['Name','SID','Gender','Course_name','CGPA']
print(Studentlist)

Studentinfo = [Name,SID,Gender,Course_name,CGPA]
print(" The list of the student information: ",Studentinfo)

 
#Question 4: Make a list to enter marks of five students and display them in a sorted manner.

Student1_marks = int(input("Enter the marks of the Student 1: "))
Student2_marks = int(input("Enter the marks of the Student 2: "))
Student3_marks = int(input("Enter the marks of the Student 3: "))
Student4_marks = int(input("Enter the marks of the Student 4: "))
Student5_marks = int(input("Enter the marks of the Student 5: "))

Student_markslist = [Student1_marks, Student2_marks, Student3_marks, Student4_marks, Student5_marks]
print(" List of the Student Marks: ", Student_markslist)

#Sorted list
print(" Sorted Student List (increasing order): ")
Student_markslist.sort()
print(Student_markslist)



#Question 5:-
#(a) Print a specified list after removing fourth element i.e. Black.
#(b) Remove Black and Pink from the list and replace it with Purple.


Color_list = ['Red' 'Green', 'White', 'Black', 'Pink', 'Yellow']
#Print (a) part
print('(a)')
print(Color_list)
#Remove  fourth element i.e. black.
Color_list.remove('Black')
print(" List after removing Black Color : ", Color_list)

Color_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#Print (b) part
print('(b)')
print(Color_list)
#Replace Black and Pink with Purple
Color_list[3:5] = ['Purple']
print(" List after replacing Black and Pink with Purple Color: ", Color_list)
