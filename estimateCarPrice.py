# 
# Ce programme estime le prix d'une voiture selon son kilometrage.
# Avant son entrainement par le linearRegression, il donnera toujours 0.
# Apres, il utilisera la fonction trouvee par l'algorithme du linearRegression,
# grace a la recuperation des parametres de cette fonction dans le
# fichier parameters.txt
# 

def getParameters():
	try:
		with open('parameters.txt', 'r') as inFile:
			line1 = inFile.readline()
			if line1:
				return line1.strip().split()
	except FileNotFoundError:
		return None


def promptUser():
	while True:
		try:
			mileage = float(input("Enter a mileage in kilometers: "))
			if mileage < 0:
				raise ValueError
			return mileage
		except ValueError:
			print("This is not a valid number.")
			pass
		except KeyboardInterrupt: # protection contre ctrl^C
			print("\nExiting...")
			exit()
		except EOFError: # protection contre ctrl^D
			print("\nExiting...")
			exit()


def estimatePrice():
	mileage		= promptUser()
	parameters	= getParameters()

	if parameters is None:
		print("The price of your car is 0. The model has not been trained yet. Please run linearRegression first.")
		return
	if len(parameters) != 6:
		print("Error: invalid number of parameters in parameters.txt")
		return

	try:
		a					= float(parameters[0])
		b					= float(parameters[1])
		x_moy				= float(parameters[2])
		x_ecart_type	= float(parameters[3])
		y_moy				= float(parameters[4])
		y_ecart_type	= float(parameters[5])
	except ValueError:
		print("Error: invalid parameter format in parameters.txt")
		return

	x_normalized	= (mileage - x_moy) / x_ecart_type		# normaliser x
	y_normalized	= a * x_normalized + b						# calcul de y normalise
	price				= y_normalized * y_ecart_type + y_moy	# denormaliser y

	if price < 0:
		price = 0

	print("The price of your car is ", round(price), ".", sep='')

estimatePrice()
