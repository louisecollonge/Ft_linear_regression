# 
# Calcul de plusieurs mesures de precision cad des erreurs de l'algorithme 
# 

def getParameters():
	try:
		with open('parameters.txt', 'r') as inFile:
			inFile.readline()
			line2 = inFile.readline()
			if line2:
				return line2.strip().split() # strip retire le \n final, split separe aux espaces
	except FileNotFoundError:
		return None

def calculatePrecision():
	parameters = getParameters()
	if parameters is None:
		print("Run SecondProgram first.")
		return
	if len(parameters) != 4:
		print("Error: invalid number of parameters in parameters.txt")
		return
	try:
		mae			= float(parameters[0])
		mse			= float(parameters[1])
		rmse			= float(parameters[2])
		r_squared	= float(parameters[3])
	except ValueError:
		print("Error: invalid parameter format in parameters.txt")
		return

	print("\033[1m" + "\nPRECISION OF THE ALGORITHM:" + "\033[0m")
	print(">> Mean Absolute Error =\t\t" + "\033[1m" + f"{round(mae)}" + "\033[0m" + "\t(erreur de prix moyenne)")
	print(">> Mean Squared Error =\t\t\t" + "\033[1m" + f"{round(mse)}" + "\033[0m" + "\t(moyenne des erreurs au carre, tient compte des grands ecarts)")
	print(">> Root Mean Squared Error =\t\t" + "\033[1m" + f"{round(rmse)}" + "\033[0m" + "\t(erreur de prix moyenne, tient compte des grands ecarts)")
	print(">> Coefficient of determination =\t" + "\033[1m" + f"{r_squared:.2f}" + "\033[0m" + "\t(variance du prix ; 100% = bon, 0% = mauvais)\n")


calculatePrecision()
