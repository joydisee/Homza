#I: D'ou tu peux ecrire import "nom_d'un_fichier_en_python"?
from Weather import getWeatherMontreal
import ISS
import Internet
import time

# Some kind of main that will call the different functions to fetch data
# This file will be regularly called by cron

#I: C'est quoi cron?

while True:
    getWeatherMontreal()
    time.sleep(20)
