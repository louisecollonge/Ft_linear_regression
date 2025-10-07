# 
# Ce programme implemente une regression lineaire a partir de l'algorithme de descente de gradient
# depuis un nuage de points. Il en ressort une fonction affine y = ax + b
# 

import pandas
import matplotlib.pyplot as plt
import numpy


try:
	df = pandas.read_csv('data.csv', sep=',') # interprete les nombre comme des float ou des int
	x = df['km'].values.astype(float)			# abscisses x = km (mileage)
	y = df['price'].values.astype(float)		# ordonnees y = prix
															# Un operation sur x est appliquee a toutes les valeurs de x
except FileNotFoundError:
	print("Missing data.csv file")
	exit()


# normaliser x et y = les convertir pour etre a la meme echelle (ameliore l'algorithme)
x_moy, y_moy					= numpy.mean(x), numpy.mean(y)
x_ecart_type, y_ecart_type	= numpy.std(x), numpy.std(y)
x_normalized					= (x - x_moy) / x_ecart_type
y_normalized					= (y - y_moy) / y_ecart_type


# y = ax + b ; choisir a, b au hasard et learningRate
a, b = 0, 0
learningRate = 0.01


# descente du gradient -> regression lineaire
for _ in range (1000):
	y_predicted_normalized = a * x_normalized + b
	# calculer l'erreur quadratique moyenne (= fonction de cout): eleve = bcp d'erreur
	a_corr = learningRate * (1 / len(x)) * numpy.sum((y_predicted_normalized - y_normalized) * x_normalized)
	b_corr = learningRate * (1 / len(x)) * numpy.sum((y_predicted_normalized - y_normalized))
	# corriger a et b selon la descente de gradient, cad dans la direction qui reduit l'erreur
	a = a - a_corr
	b = b - b_corr


# recalculer apres descente de gradient avec a et b finaux
y_predicted_normalized = a * x_normalized + b
y_predicted = y_predicted_normalized * y_ecart_type + y_moy


# enregistrer parametres pour entrainement estimateCarPrice.py
with open('parameters.txt', 'w') as outFile:
	outFile.write(f"{a} {b} {x_moy} {x_ecart_type} {y_moy} {y_ecart_type}\n")



# calculs de precision pour Precision.py
errors		= y - y_predicted
mae			= numpy.mean(numpy.abs(errors))
mse			= numpy.mean(errors ** 2) # carre des erreurs
rmse			= numpy.sqrt(mse)
r_squared	= 1 - (numpy.sum(errors ** 2) / numpy.sum((y - numpy.mean(y)) ** 2))

with open('parameters.txt', 'a') as outFile:
	outFile.write(f"{mae} {mse} {rmse} {r_squared}\n")



# generer une ligne continue
x_line = numpy.linspace(min(x), max(x), 100)								# genere des points entre min et max de x pour un trace continu
x_line_normalized = (x_line - x_moy) / x_ecart_type					# normaliser x_line pour pouvoir calculer y_line_normalized
y_line_normalized = a * x_line_normalized + b							# calcul de y pour tous les points de la droite
y_line = y_line_normalized * y_ecart_type + y_moy						# denormaliser y pour l'affichage

# affichage du graphique
plt.figure(figsize=(10, 6))													# taille de la fenetre
plt.scatter(x, y, color='blue', label='Price per km')					# afficher les points en bleu
plt.plot(x_line, y_line, color='red', label='Linear regression')	# afficher la droite de fonction affine
plt.title("Linear regression with gradient descent algorithm")		# afficher un titre en haut au milieu
plt.xlabel("km")																	# afficher unite des abscisses
plt.ylabel("Price")																# afficher unites des ordonnees
plt.grid(True)																		# afficher un cadrillage
plt.legend()																		# afficher une legende en haut a droite
plt.show()																			# afficher le graphique



# histogramme des residus = distribution des erreurs entre y reel et y predit
plt.hist(errors, bins=20, color='blue', edgecolor='black')
plt.xlabel("Résidus")
plt.ylabel("Fréquence")
plt.title("Distribution des résidus")
plt.show()





# 
# 
# * Normalisation de x et y *
# 
# Lorsque x et y ont des valeurs d'ordres de grandeur tres differents,
# l'algorithme devient lent et instable.
# Il faut transformer x et y pour les mettre sur des echelles similaires,
# centrees autour de 0.
# 
# 				x_normalized = (x - moyenne(x)) / ecart-type(x)
# 
# L'ecart-type reflete l'etalement des valeurs de x.
# Ainsi, x et y sont sur la meme echelle [-1.22, 0, 1.22], ce qui rend les calculs
# de la descente de gradient plus efficaces.
# 
# L'algorithme trouvera une droite representant la fonction affine y = ax + b
# avec a et b calcules a partir de x_normalized et de y_normalized.
# Cette fonction n'est pas valide sur x et y (non-normalises).
# 
# 
# 
# 
# * Erreur quadratique moyenne ou MSE *
# 
# C'est la formule mathematique d'une fonction dite de cout.
# Elle donne un resultat qui evalue pour x, si le y predit est proche du y reel.
# Ce resultat est la derivee partielle de la fonction de cout par rapport a a, 
# multipliee par le taux d'apprentissage.
# 
# La derivee indique la direction et la vitesse avec laquelle la fonction de cout
# augmente ou diminue quand on change a.
# 
# Si la derivee est positive, ca veut dire qu'en augmentant a, le cout augmente. 
# Ca veut dire que l'erreur augmente. On veut donc diminuer a.
# 
# Si la derivee est negative, ca veut dire qu'en augmentant a, le cout diminue. 
# C'est ce qu'on veut. On veut donc augmenter a.
# 
# Donc le resultat de la fonction de cout, a_corr ou b_corr, doit etre soustrait
# a a ou b respectivement, pour inverser le signe.
# 
# 
# 
# 
# * Affichage d'une droite *
# 
# x_line est un ensemble de point generes entre le min et le max de x et qui formeront
# une droite continue sur le graphique. x_line n'est pas normalise puisqu'on utilise x.
# 
# On normalise x_line en r_line_normalized, car on ne peut recuperer y qu'en passant par
# la fonction affine que l'algo nous a trouve, et qui utilise x et y normalises.
# 
# Une fois qu'on a calcule l'ensemble des y_line_normalized, on doit les de-normaliser
# pour les afficher. Pour cela, il suffit d'inverser la formule de normalisation.
# 
# 				y_line = y_line_normalized * y_ecart_type + y_moy
# 
# 
# 
# 
# * Histogramme des residus *
# 
# Distribution des erreurs entre y reel et y predit par l'algo. 
# Distribution gaussienne = normale = erreurs aleatoires symetriquement reparties autour de 0
# Dans notre algo, les erreurs sont un peu biaisee positivement: la courbe gaussienne est > 0:
# le prix suggere est souvent trop bas.
# 
# Ca peut s' expliquer par:
# - la repartition ne suis pas tout a fait une regression lineaire 
#   (d'autres facteurs entrent en jeu: la marque de la voiture, son etat...)
# - certaines donnees de data.csv sont desequilibrees
# - les donnees de data.csv sont trop peu nombreuses
# 
# 
