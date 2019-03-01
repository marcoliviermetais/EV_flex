import pandas as pd
import numpy as np
import requests
import json
import matplotlib.pyplot as plt
from API_import_coef import API_import_coef
from API_import_conso_commune import API_import_conso_commune
from courbe_init import courbe_init

#  ********************************** PARAMETRES ********************************** #

poste = 2154 #index du poste source dans le fichier GPS_poste_source
nb_transfo = 3 #nombre de transformateurs du poste source
date_debut = '2019-01-07'
date_fin = '2019-01-13'
saison = 'H' #H pour hiver, E pour été

#Choix du scénario 
scenario = 'scenario_1'

#Répartition des profils de consommateurs
#LA SOMME DES POIDS POUR CHAQUE CATEGORIE DOIT VALOIR 1
res = [['RES1_BASE', 0.2], ['RES11_BASE',0.1],['RES2_HP', 0.45], ['RES2_HC', 0.25]]
pro = [['PRO1_BASE', 0.5], ['PRO2_HP', 0.2], ['PRO2_HC',0.1],['PRO5_BASE',0.2]]
ent = [['ENT1_HP'+saison, 0.2], ['ENT1_HC'+saison, 0.05],['ENT3_HP'+saison, 0.65], ['ENT3_HC'+saison, 0.1]]

#Répartition des secteurs dans les trois catégories de profils
secteur_res = ['residentiel']
secteur_pro = ['professionnel', 'agriculture', 'secteur_non_affecte']
secteur_ent = ['industrie', 'tertiaire']

#  **************************** COURBE DE CHARGE **************************** #

courbe_de_charge = courbe_init(poste, nb_transfo, date_debut, date_fin, res, pro, ent, secteur_res, secteur_pro, secteur_ent)


# Graphe 

fig = plt.figure()
plt.plot(courbe_de_charge['horodate'], courbe_de_charge['P'])
plt.xlabel('Date et heure')
plt.ylabel('Puissance (MW)')
plt.show()