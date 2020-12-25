import random
name = input("what ur name ")
number=random.randrange(0,20)
guessCheck="wrong"
print("Welcome to Number Guess " + name)

while guessCheck=="wrong":
	response=int(input("Please input a number between 0 and 20:"))
	try:
		val=response
	except ValueError:
		print("This is not a valid integer. Please try again " + name)
		continue
	val=response
	if val<number:
		print("This is lower than actual number. Please try again ." + name )
	elif val>number:
		print("This is higher than actual number. Please try again ." + name)
	else:
		print("This is the correct number " + name)
		guessCheck="correct"

print("Thank you for playing Number Guess. See you again, bye have a great time " + name)

