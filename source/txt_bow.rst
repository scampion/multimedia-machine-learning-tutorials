.. Text bag of word

Classification de documents textuels avec la méthode des 'sacs de mots' et les séparateurs à vaste marges
=========================================================================================================

Copier le jeu de données Reuters
--------------------------------
Chaque nouvelle Reuters [#reuters_dataset]_ est classée par catégorie/répertoire 

Préparer les données 
--------------------
* Retirer la ponctuation du texte à l'aide de la commande tr.
Transformer les lettres majuscules en minuscules.
	
::

  r [:punct:] ' '
  tr [A-Z] [a-z]
	
* Normaliser les mots avec l'algorithme de stemming de Porter [#porter]_

  * compiler le fichier source porter.c 
  * utiliser : porter ./path/of/the/file 

Calculer le vocabulaire des mots les plus fréquents :
-----------------------------------------------------

Variables nécessaires :

* Une table de hashage globale pour compter les termes  
* Une table de hashage par document pour compter les termes  
* Un tableau de taille égale au nombre de documents pour stocker les tables précedemment décrite
* Pour la détection des stop-words, utiliser une table de hashage pour compter le nombre de documents où chaque terme est présent.

Pseudo algorithme:
::
 
  tableau : term_counts_per_doc  
  hastab  : term_counts = {}
  hastab  : document_counts = {}

  Pour chaque document :
    hashtab : term_count_in_doc 
 
    Pour chaque mot dans le document:
      term_count_in_doc[term] += 1 
      term_counts[term] += 1
 
    Pour chaque terme dans la table :  term_count_in_doc
      document_counts[term] +=1 

Supprimer les stop-words
------------------------
Stop-words, mots présents dans 80% des documents.


Conserver les N mots les plus fréquents
---------------------------------------
Les sauvegarder dans un fichier texte (un terme par ligne) 
valeurs de N possibles : 500, 1000, 2000, 5000



A partir du vocabulaire, vectoriser les documents
-------------------------------------------------

:: 

  Pour chaque document : 
    Créer un vecteur vide de taille N (longueur du vocabulaire)
    Pour chaque terme dans le document : 
      hashtab : term_count_in_doc 
 
      Pour chaque mot dans le document:
        term_count_in_doc[term] += 1 

      Pour chaque term dans term_count_in_doc: 
        Si le terme est dans le vocabulaire :
	  i = numero de ligne du terme dans le vocabulaire
	  vecteur[i] = nombre de termes 
	
Classifier les données
----------------------

* Entrainer le classifieur SVM et les différents noyaux (rbf, linear, poly) avec les vecteurs d'entrainement. 
* Evaluer le taux d'erreurs avec les données de tests

Produire la matrice de confusion pour le meilleur classifieur
-------------------------------------------------------------

Annexes
-------

Bag of words
~~~~~~~~~~~~
.. literalinclude:: ../src/txt_bow/bow.py  

Training
~~~~~~~~

.. literalinclude:: ../src/txt_bow/train.py

Classification 
~~~~~~~~~~~~~~

.. literalinclude:: ../src/txt_bow/classif.py


.. rubric:: Liens

.. [#reuters_dataset] http://disi.unitn.it/moschitti/corpora/Reuters21578-Apte-90Cat.tar.gz
.. [#porter] http://tartarus.org/~martin/PorterStemmer/