# write a python program to take age from the user to check whether user able to participate in voting or not.
# if age is less than 18 then it don't allow to participation and show after how much year a person will be able to participate :


name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age >=18:
    print(f"Hi {name}! Your are Eligible to participate in voting")
    
else:
    my_age = 18 - age     
    print(f"Sorry! Your are a Not Eligible to participate in voting, you will be able to participate after {myage} years")     
    
    
    
# Write a python program to take marks from the user to check whether user able to admission in college or not. 
# if mark is less than 60 then it don't allow to take admission

user = input("Enter your name: ")
marks = int(input("Enter your marks: "))

if marks >=60:
    print(f"Hi {name}!, Your are able to admission in college")
    
else:
    userMarks = 60 - marks
    print(f"Sorry! you cannot take admission in college, you need {userMarks} numbers more to take admission")    