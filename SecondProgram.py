import csv
import pandas
import matplotlib
import matplotlib.pyplot as plt
import numpy

df = pandas.read_csv('data.csv', sep=',')
data_csv = df.values.astype(int)
# print(data_csv)
x = df['km'].values		# definir les abscisses
y = df['price'].values	# definir les ordonnees


# calcul de regression lineaire, a re-coder !
coefficients = numpy.polyfit(x, y, 1)
polynome = numpy.poly1d(coefficients)
x_reg = numpy.linspace(min(x), max(x), 100)
y_reg = polynome(x_reg)

# todo algorithme de descente du gradient



# creer le graphique
plt.figure(figsize=(10, 6))												# taille de la fenetre
plt.scatter(x, y, color='blue', label='Price per km')				# afficher les points en bleu
plt.plot(x_reg, y_reg, color='red', label='Linear regression')
plt.title("Linear regression with gradient descent algorithm")	# afficher un titre en haut au milieu
plt.xlabel("km")																# afficher unite des abscisses
plt.ylabel("Price")															# afficher unites des ordonnees
plt.grid(True)																	# afficher un cadrillage
plt.legend()																	# afficher une legende en haut a droite
plt.show()																		# afficher le graphique

















#################### VERSION 2 D'AFFICHAGE DU GRAPHIQUE ####################
# with open('data.csv') as f:
# 	csvfile = csv.reader(f)
# 	for row in csvfile:
# 		x, y = row
# 		try:
# 			x = int(x)
# 			y = int(y)
# 		except ValueError:
# 			pass
# 		# print(x, y)

#################### VERSION 3 D'AFFICHAGE DU GRAPHIQUE ####################
# f = open('data.csv')
# csv_reader = csv.reader(f)
# data_csv = numpy.array(list(csv_reader))
# # print(data_csv)

#################### VERSION 4 D'AFFICHAGE DU GRAPHIQUE ####################
# with open('data.csv') as f:
# 	csvReader = csv.reader(f)
# 	next(csvReader)
# 	data_list = list(csvReader)
# 	data_csv = numpy.array(data_list, dtype=int)
# 	# print(data_csv)

