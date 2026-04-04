
# Main to fetch the inout marks(5 subjects)

import average, grade
   
# storing subjects to a list, for a better user experience
subjects = ["English","Maths","Chemistry","Physics","Biology"]

marks = []

i=0

while i <=4:

    try:   

        marks.insert(i,int(input(f"Enter {subjects[i]} marks: ")))  # fetching the user input marks

        if marks[i] < 0 or marks[i] > 100:  # checking if marks between 0 and 100 or not

            marks.pop(i)  # removing the marks stored in the list if less than 0 and more than 100

            print("\nPlease enter a mark between 0 and 100\n")
            
            continue     

        i +=1

    except ValueError: # used to handle the error casued while user enters non-numerical inputs as marks

        print("\nNon-numerical value entered for marks!!. Please enter actual marks\n")

        continue 

 

print (f"\nSubject based marks: {marks}")  # input marks are displayed

average01= average.calculate_average(marks) # calling average function

grade01 = grade.get_grade(average01)  # calling grade fucntion

print(f"\nAverage marks: {average01}45") # displaying Average 

print(f"\nGrade: {grade01}\n") # displaying Grade