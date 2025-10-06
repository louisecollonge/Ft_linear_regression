def getParameters():
	try:
		with open('parameters.txt', 'r') as inFile:
			parameters = inFile.readline().split()
			return parameters
	except FileNotFoundError:
		return None

def promptUser():
	while True:
		try:
			mileage = input("Enter a mileage in kilometers: ")
			mileage = float(mileage)
			if mileage < 0:
				raise ValueError
			return mileage
		except ValueError:
			print("Please enter a valid number.")
			pass


def estimatePrice():
	mileage = promptUser()

	parameters = getParameters()
	if parameters is None:
		print("The price of your car is 0.")
		return

	a = float(parameters[0])
	b = float(parameters[1])
	x_moy = float(parameters[2])
	x_ecart_type = float(parameters[3])
	y_moy = float(parameters[4])
	y_ecart_type = float(parameters[5])

	x_normalized = (mileage - x_moy) / x_ecart_type
	y_normalized = a * x_normalized + b
	price = y_normalized * y_ecart_type + y_moy

	print("The price of you car is", price)

estimatePrice()