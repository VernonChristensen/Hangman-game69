# Vernon Christensen
myWord = "Joe sister"
misses = 0


hanglist = [''' pic 1''', ''' pic 2''']

while misses < 7:
	print(hanglist[misses])
	guess = input("Guess a letter: ")
	if guess in myWord:
		# loop threw secret and find all the matching letters
		print("That letter is in the secret word ")
	else:
		misses = misses + 1



wronglist = []
rightlist = []
choice = input("type a word: ")


mystring = "Joe Sister"
myList = list(mystring)
print(myList)
secret = []
#how to create a list with _ in place of letters
for a in myList:
	secret.append("_")

print(secret)

# How to replace an _ with a letter

secret[2] = "i"
print(myWord)

# How to keep track of misses



if choice == myWord:
	print("It's a match")
else:
	print("Not a match")
while True:

	letter = input("Type a Letter ")
	if letter in myWord:
		print("Letter is in the word")
		rightlist.append(letter)
	else:
		print("Letter is not in the word")
		wronglist.append(letter)

	print(wronglist)
	print(rightlist)

	count = 0
	for j in myWord:
		if j == letter:
			print(count)
			count += 1
