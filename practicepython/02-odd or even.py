#Ask the user for a number. Depending on whether the number is even or odd, print out an 
# appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?
#Extras:
#If the number is a multiple of 4, print out a different message.
#Ask the user for two numbers: one number to check(call it num) and one number
#to divide by(check).If check divides evenly into num, tell that to the user.
#If not, print a different appropriate message.

num1 = int(input('Enter 1st Number; '))
if num1 % 4 == 0:
    print('It is even number and It is multiple of 4')
elif num1 % 2 == 0:
     print("It's even number")
else:
    print("it's odd number")
num2 = int(input('Enter 2nd number; '))
if num1 % num2 == 0:
    print(f'{num1} can be divided by {num2}')
else:
    print(f'{num1} cannot be divided by {num2}') 
     


