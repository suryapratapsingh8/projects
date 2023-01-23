import random

import math
lower = int(input("Enter Lower bound:- "))

upper = int(input("Enter Upper bound:- "))

a=math.floor(math.log(upper - lower + 1, 2))
x = random.randint(lower, upper)

print("\n\tYou've only ",a,
	" chances to guess the integer!\n")

count = 0


while count < a:
	count+=1
	
	guess = int(input("Guess a number:- "))
    
	if x == guess:
		print("Congratulations you did it in ",
			count, " try")
	
		break
	elif x > guess:
		print("number is bigger than this number!")
	elif x < guess:
		print("number is smaller than this number!")

if count >= a:
	print("\nThe number is ", x)
	print("\tBetter Luck Next time!")


