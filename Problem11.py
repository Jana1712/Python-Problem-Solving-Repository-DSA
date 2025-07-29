# Write a Python Program to get number from the user, and display table for that number ?

num = int(input("Enter a Number :"))

# 1 * 5 = 5
# 2 * 5 = 10

def table(num):

    for i in range(1,11):
        print(str(i)+"*"+str(num)+" = "+str(i*num))
        
table(num)   

    