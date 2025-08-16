# Write a Python Program to get number from the user, and display table for that number ?

num = int(input("Enter a Number :"))

# 1 * 5 = 5
# 2 * 5 = 10

def table(num):

    for i in range(1,11):
        print(str(i)+"*"+str(num)+" = "+str(i*num))
        
table(num)   




#OUTPUT :

5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
5 * 6 = 30 
5 * 7 = 35
5 * 8 = 40
5 * 9 = 45
5 * 10 = 50
