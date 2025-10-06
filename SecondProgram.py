import pandas
import matplotlib.pyplot as plt
import numpy


#!~~~~~~~~~~~~~~~~~~~~~~~~~~~~ RECUPERER LES DONNEES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~!#

df = pandas.read_csv('data.csv', sep=',') # interprete les nombre comme des float ou des int
x = df['km'].values								# abscisses x = km. En faisant une operation sur x, on la fera d'un coup sur toutes les valeurs de x
y = df['price'].values							# ordonnees y = prix


#!~~~~~~~~~~~~~~~~~~~~~~~ MON ALGO DE DESCENTE DU GRADIENT ~~~~~~~~~~~~~~~~~~~~~~~!#

# normaliser x: lui donner la bonne echelle (l'ecart-type mesure l'etalement des donnees), sinon l'algo serait trop long
x_moy				= numpy.mean(x)
x_ecart_type	= numpy.std(x)
x_normalized	= (x - x_moy) / x_ecart_type

# prendre une droite (y = a x + b) au hasard, par ex. a et b egal a 0
a, b = 0, 0

# choisir un learningRate
learningRate = 0.01

# descente du gradient -> regression lineaire
for _ in range (1000):
	y_predicted = a * x_normalized + b

	# calculer le score de cette droite avec la formule MSE d'erreur quadratique moyenne (= fonction de cout): score eleve = bcp d'erreur
	a_corr = learningRate * (1 / len(x)) * numpy.sum((y_predicted - y) * x_normalized)
	b_corr = learningRate * (1 / len(x)) * numpy.sum((y_predicted - y))

	# corriger a et b selon la descente de gradient, cad dans la direction qui reduit l'erreur
	a = a - a_corr
	b = b - b_corr

x_reg = numpy.linspace(min(x), max(x), 100) # genere des points entre le min et le max de x pour un trace continu sur le graphique
x_reg_normalized = (x_reg - x_moy) / x_ecart_type
y_reg = (a * x_reg_normalized + b) # calcul de y pour tous les points de la droite, donc x_reg


#!~~~~~~~~~~~~~~~~~~~~~~~~~~~~ AFFICHAGE DU GRAPHIQUE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~!#

plt.figure(figsize=(10, 6))												# taille de la fenetre
plt.scatter(x, y, color='blue', label='Price per km')				# afficher les points en bleu
plt.plot(x_reg, y_reg, color='red', label='Linear regression')	# afficher la droite de fonction affine
plt.title("Linear regression with gradient descent algorithm")	# afficher un titre en haut au milieu
plt.xlabel("km")																# afficher unite des abscisses
plt.ylabel("Price")															# afficher unites des ordonnees
plt.grid(True)																	# afficher un cadrillage
plt.legend()																	# afficher une legende en haut a droite
plt.show()																		# afficher le graphique


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