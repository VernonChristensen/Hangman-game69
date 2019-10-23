# Vernon Christensen
print("welcome to the To Do List! ")
todoList = []
while True:
	print("Enter a to add an item")
	print("Enter r to remove an item")
	print("Enter p to print the List")
	print("Enter q to quit")
	choice = input("Make your choice: ")

	if choice == "q":
		break
	elif choice == "a":
		add = input("What would you like to add to the lists? ")
		todoList.append(add)
		print(todoList)
	
	elif choice == "r":
		remove = input("What would you like to remove? ")
		todoList.remove(remove)
		print(todoList)
	elif choice == "p":
		print(todoList)
	else:
		print("You idiot, read the instructions")
