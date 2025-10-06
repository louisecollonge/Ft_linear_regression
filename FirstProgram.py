while True:
	try:
		mileage = input("Enter a mileage in kilometers: ")
		mileage = int(mileage)
		break
	except ValueError:
		print("Please enter a valid integer.")
		pass

a = 0
b = 0
price = a + b * mileage

print("The price of your car is:", price)
