# Name: Vernon Christensen	
# Period 6
# Dice Rolling Simulator
import random
rolls = int(input("how many rolls:"))

x = 1 

a = 0
b = 0 
c = 0
d = 0
e = 0
f = 0


while x <= rolls:
	number = random.randint(1,6)
	if number == 1:
		a += 1
	if number == 2:
		b += 1
	if number == 3:
		c += 1
	if number == 4:
		d += 1
	if number == 5:
		e += 1
	if number == 6:
		f += 1
	print("Roll " + str(x) + " is " + str(number))
	x = x +1

print("Total Rolls: " + str(rolls))
print("The results are: ")
print("1s: " + str(a))
print("2s: " + str(b))
print("3s: " + str(c))
print("4s: " + str(d))
print("5s: " + str(e))
print("6s: " + str(f))


print("The percentages are:")
print("1s: " + str((a/rolls)*100) + "%")
print("2s: " + str((b/rolls)*100) + "%")
print("3s: " + str((c/rolls)*100) + "%")
print("4s: " + str((d/rolls)*100) + "%")
print("5s: " + str((e/rolls)*100) + "%")
print("6s: " + str((f/rolls)*100) + "%")
