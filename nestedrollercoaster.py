print("Welcome to the Nested Rollercoaster")

height=int(input("What is your height in cm? "))


if height >= 120:
	print("You can ride the rollercoaster!")
	age = int(input("What is your age? "))
	if age<12 :
		print("Please pay $5")
	elif 12<=age<=18:
		print("Please pay $7")
	else:
		print("Please pay $12")
else:
	print("Sorry, you need to grow taller to ride")