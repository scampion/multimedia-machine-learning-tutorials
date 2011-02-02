.. video face recognition

Détection et reconnaissance de visages dans les vidéos
======================================================


Demonstration
-------------
.. raw:: html

  <iframe title="YouTube video player" class="youtube-player" type="text/html" width="480" height="390" src="http://www.youtube.com/embed/g2OkGh0x8iE" frameborder="0" allowFullScreen></iframe>


Télécharger les données d'apprentisage 
--------------------------------------

Nous utiliserons les données du corpus : Labeled Faces in the Wild
http://vis-www.cs.umass.edu/lfw/lfw-funneled.tgz

Detecter les visages 
--------------------
Utiliser script facedetector basé sur le detecteur Haar d'OpenCV :
::

  facedetector.py <chemin de l image>


Formater les données d'apprentisage
-----------------------------------
Dupliquer le répertoire *training* en *training_preprocessed*
Pour chaque image du répertoire training_preprocessed, extraire le visage en une image de taille 64x64 et en niveau de gris.

Extraire des videos les visages détectés
----------------------------------------
Avec FFMpeg, extraire quelques données de test dans le même format que précedemment


Calculer les composantes principales du jeu de données
------------------------------------------------------
#. Calculer le visage moyen 
#. Utiliser le script pca.py pour extraire les composantes principales
#. Transformer vos images en descripteur 

Classification des visages 
--------------------------
#. Réaliser d'apprentisage avec l'algorithme des SVM 
#. Utiliser une grille de recherche pour optimiser les parametres 
#. Utiliser votre classifieur sur les données provenants des vidéos



Annexe 
------

Commande GNU/Linux
~~~~~~~~~~~~~~~~~~
::
  convert image.jpg -crop 32x32+16+16 -colorspace gray -compress none -depth 8 test.pgm 
  man paste 

FaceDetector
~~~~~~~~~~~~
.. literalinclude:: ../src/video_faces_recognition/facedetector.py

FaceRecognizer
~~~~~~~~~~~~~~ 
.. literalinclude:: ../src/video_faces_recognition/facerecognizer.py


FaceDetector + sampler
~~~~~~~~~~~~~~~~~~~~~~
.. literalinclude:: ../src/video_faces_recognition/facedetect_pic.py

Demo
~~~~
.. literalinclude:: ../src/video_faces_recognition/demo.py

