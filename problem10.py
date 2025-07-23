# write a program to get number from the user, and display table for that number :

num = int(input("Enter your number: "))

print(f"You entered {num}")

for i in range(1,11):
    print(str(i*f"{num}"))
    
    
    