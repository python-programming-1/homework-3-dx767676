def collatz(num):
	if num % 2 == 0:
		num = num // 2
	else:
		num = num*3 + 1
	return num

while True:
	try:
		x = int(input("Please enter a number: "))
		break
	except ValueError:
		print("That was not a valid number. Please try agagin...")
while x!=1:
	x = collatz(x)
	print(x)

