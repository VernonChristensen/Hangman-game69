# Vernon Christensen
# Conditional
print("Welcome to Ticket Bot")
print("You must be at least 18 to see R rated movies")
age = int(input("how old are you?"))

if age > 18: 
	print("You can go see an R rated movie")
else:
	print("You cannot go see an R rated movie")

print("Thank You")

mysteryNum = 6
guess = int(input("guess a number between 1 and 10: "))
if guess == mysteryNum:
	print("Good guess, that is correct")
elif guess > 10:
	print("please read directions stupid.")
elif guess > mysteryNum:
	print("to high, try again")

else:
	print("too low, try again")

# conditional operators: >, <, >=, <=, ==(is equal to), !=(is not equal to)

birthday = input("is today your birthday(yes/no): ")
if birthday == "yes":
	print("Happy birthday")
elif birthday == "no":
	print("Have a good day anyway")
else:
	print("please read directions")