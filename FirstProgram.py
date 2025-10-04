while True:
	try:
		mileage = input("Enter a mileage in kilometers: ")
		mileage = int(mileage)
		break
	except ValueError:
		print("Please enter a valid integer.")
		pass

a0 = 0
a1 = 0
price = a0 + a1 * mileage

print("The price of your car is:", price)
