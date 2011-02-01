.. Classification d'objets dans les images avec les sacs de mots visuels et l'algorithme de classification SVM

Classification d'objets dans les images avec les sacs de mots visuels
=====================================================================

Résumé
------
L'objectif de ces travaux pratiques est d'utiliser l'algorithme des SVM [#svm]_ (Séparateurs à Vaste Marge) pour la détection d'objets dans les images.
Pour cela travaillerons avec un descripteur local appelé SURF [#surf]_ .
Nous utiliserons ce descripteur avec la méthode des sacs de mots [#bow]_ et l'algorithme associé de réduction de dimensions K-Means [#kmeans]_ .
Nous terminerons enfin par l'utilisation des SVMs pour déterminer la catégorie de l'objet représenté dans l'image. 

Corpus de données
------------------
Nous utiliserons le corpus Caltech256 [#caltech]_ pour ce TP. Nous n'utiliserons que deux classes d'objets, les motocycles et les avions. 

Visionner les images associées à ces deux catégories
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Calcul d'un descripteur
-----------------------

Calculer les SURFs à l'aide du script surfs.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Nous utiliserons la librairie OpenCV [#opencv]_ pour l'extraction des points d'intérêt et leurs descriptions. 
A la fin du traitement, deux fichiers sont produits :
* moto
* plane

Chacun de ces fichiers est un dictionnaire python (hashtable) de type : clé (nom du fichier image) : valeurs (tableau de vecteurs 128 dim)}

Ouvrir le fichier moto : 

:: 
   import pickle 
   moto = pickle.load(open('moto'))
   moto.keys()[0]
   moto.values()[0]


Dictionnaire visuel 
-------------------

Calculer le dictionnaire visuel à l'aide du KMeans
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Utiliser les paramètres suivants : 
* LEARN\_SIZE = 100
* K = 8
* ITER = 10 


Quantifier les vecteurs d'apprentissage et d'évaluation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Utiliser les 100 premières images pour l'évaluation. 

Classification
--------------

Avec les SVM, classer l'ensemble des données d'évalution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Donnner les mesures de rappel, précision, F-mesure.

Avec les Random Forest, classer l'ensemble des données d'évalution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Donnner les mesures de rappel, précision, F-mesure.


Variations
----------
Augmenter la taille du vocabulaire
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Quels observations peut-on faire ? 

Augmenter le nombre d'itération
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Quels observations peut-on faire ? 

Augmenter la taille d'apprentissage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Quels observations peut-on faire ? 

 
Calculer les histogrammes à l'aide du script histo.py
-----------------------------------------------------
A la fin du traitement, deux fichiers sont produits :
* moto
* plane

Recommencer les étapes, kmeans, vectorisations et classification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 

Annexes 
-------

Récupération et formatage des données
-------------------------------------
.. literalinclude:: ../src/pics_bow/Makefile
   :language: make	    

Calcul des SURFs
----------------
.. literalinclude:: ../src/pics_bow/surfs.py


Calcul du dictionnaire de mots
------------------------------
.. literalinclude:: ../src/pics_bow/kmeans.py 


Quantification des vecteurs
---------------------------
.. literalinclude:: ../src/pics_bow/assign.py

Classification des images
-------------------------
.. literalinclude:: ../src/pics_bow/classif.py


Résultats : 
-----------

:: 

   In [4]: run classif.py
   Precision : 90.00% (360/400)


.. rubric:: Liens 
.. [#svm] http://fr.wikipedia.org/wiki/Machine_%C3%A0_vecteurs_de_support
.. [#surf] http://fr.wikipedia.org/wiki/Speeded_Up_Robust_Features
.. [#bow] http://fr.wikipedia.org/wiki/Sac_de_mots
.. [#kmeans] http://fr.wikipedia.org/wiki/K-means
.. [#caltech] http://www.vision.caltech.edu/Image_Datasets/Caltech256/
.. [#opencv] http://opencv.willowgarage.com/