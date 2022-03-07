############################ PROJET MARMITON ############################
###Prérequis 
1-Installer le modules : Pandas,numpy, tkinter, fonction webdriver du package selenium,
bs4, time.
2-Conserver le contenu du fichier zip dans un seul dossier 
3-Code fonctionne sur la version python 3.7

###Structure 
1ere Partie : 
-Extraction des donées du site marmiton
-Affichage des plats
-Choix du plat
-Extraction de la recette de marmiton et ingrédients
NB: le choix du plat doit être un numéro allant de 0 à 3
2ere Partie : 
-Extraction des données sur Monoprix
-Réalisation du panier 
-Choix de l'heure de récuparation pour le premier produit
-Ajout dans le panier des produits restants
-Determintation et affichage des produits non dispoibles sur le site
-Affichage du panier pour verification, validation et paiement

####
Pour mener à bien ce projet nous avons récupérer des données de 2 sites;
-Marmiton 
-Monoprix
il se pourrait donc que ces deux sites puissent se mettre à jour

### Procédure de lancement
->Si vous exécuter le code sur jupiterLab il serait préférable d'exécuter
toutes les fonctions.
Pour le lancement final du projet il suffira de lancer le bloc "#marker" qui se situe à la fin du projet

-> Si vous exécuter sur spyder il suffira de lancer alors tout le bloc de code 
en une seule fois

Nb:Lors du lancement sur spyder si vous travaillez sur une version supérieur
il se pourrait que vous aillez la notification d'erreur 
"find_element_by_* commands are deprecated in selenium" , il suffira juste 
de remplacer la syntaxe par "driver.find_element(By.....)"
Plus de détail sur : https://stackoverflow.com/questions/69875125/find-element-by-commands-are-deprecated-in-selenium
Malgré tout le code pourra s'exécuter pour la plupart sur spyder
