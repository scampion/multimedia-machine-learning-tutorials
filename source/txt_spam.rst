.. Txt spam classifier 

Détection de spam par classification naïve bayesienne
=====================================================

Résumé
------
L'objectif de ces travaux pratiques sera donc la mise en oeuvre d'un detecteur de spam. Pour cela nous aborderons les outils utiles pour la préparation, le formatage des données. 
Nous travaillerons ensuite la phase d'apprentisage via l'extraction des caractéristiques de chaque attribut.

Enfin nous terminerons par la phase de prédiction spam ou non-spam (ham) ou nous mettront en oeuvre une mesure de qualité (rappel/precision) de notre outil.

Récupération des données
------------------------
Pour ce TP, nous utiliserons les données du corpus **SPAM E-mail Database** disponible à l'adresse suivante : http://archive.ics.uci.edu/ml/datasets/Spambase

Cette base contient 4601 instances ( dont 1813 spams = 39.4%).
Chaque email est caractérisé par 58 attributs (57 continus, 1 label)
* 48 attributs réels continus compris entre [0,100] de type fréquence des mots en pourcentage. 
*  6 attributs réels continus compris entre [0,100] de type fréquence des caractères en pourcentage. 
*  3 attibuts réels de type longueur moyenne,maximal et total des mots en majuscules.
*  le dernier attribut pour caratériser le spam (1) ou le ham (0)

#. Télécharger le corpus et commenter la documentation associée
#. Que pensez-vous de l'hypothèse d'indépendance des attributs ?

Phase d'apprentisage
--------------------
On suppose que chaque attribut suit du corpus SpamBase suit une loi normale (également appelée de Gauss) : 
:math:`p(x)\ =\ \frac{1}{\sigma \sqrt{2\pi}}\ \mathrm{e}^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2}`

.. figure:: _static/loi_normale.png
   :alt: source Wikipédia
source wikipedia 

Pour chaque classe spam et ham, prendre **les 50 premiers emails** pour calculer l'espérance :math:`\mu` et la variance 

:math:`\sigma` de chaque attributs. 

Pour rappel : 

:math:`\mu = \frac 1N \sum_{i=1}^N x_i`

:math:`\sigma^2 = \frac {1}{(N-1)} \sum_{i=1}^N  \left(x_i - \mu \right)^2`


#. Calculer la valeur des paramètres pour chacun des attributs
#. Commenter ces valeurs ? 

Classification des emails
-------------------------
On souhaite classifier des documents par leur contenu, par exemple des E-mails en spam et non-spam(ham).

source Wikipédia [#wikipedia]_ : 

On écrit la probabilité d'un document ''D'', étant donné une classe ''C'',
:math:`p(D\vert C)=\prod_i p(w_i \vert C)\,` 

Quelle est la probabilité qu'un document ''D'' appartienne à une classe donnée ''C'' ? En d'autres termes, quelle est la valeur de :math:`p(C \vert D)\,`? 
:math:`p(D\vert C)={p(D\cap C)\over p(C)}`

et 
:math:`p(C\vert D)={p(D\cap C)\over p(D)}`

Le théorème de Bayes nous permet d'inférer la probabilité en termes de vraisemblance. 

:math:`p(C\vert D)={p(C)\over p(D)}\,p(D\vert C)` 

Si on suppose qu'il n'existe que deux classes mutuellement exclusives, :math:`S` et  :math:`\neg S` (e.g. spam et ham), telles que chaque élément (email) appartienne soit à l'une, soit à l'autre,
:math:`p(D\vert S)=\prod_i p(w_i \vert S)\,` 
et 
:math:`p(D\vert\neg S)=\prod_i p(w_i\vert\neg S)\,` 

En utilisant le résultat bayésien ci-dessus, on peut écrire :
:math:`p(S\vert D)={p(S)\over p(D)}\,\prod_i p(w_i \vert S)` 
:math:`p(\neg S\vert D)={p(\neg S)\over p(D)}\,\prod_i p(w_i \vert\neg S)`


Alors, en divisant les deux équations, on obtient :
:math:`{p(S\vert D)\over p(\neg S\vert D)}={p(S)\,\prod_i p(w_i \vert S)\over p(\neg S)\,\prod_i p(w_i \vert\neg S)}`

Qui peut être factorisée de nouveau en :

:math:`{p(S\vert D)\over p(\neg S\vert D)}={p(S)\over p(\neg S)}\,\prod_i {p(w_i \vert S)\over p(w_i \vert\neg S)}`

Par conséquent, le rapport de probabilités :math:`p(S|D) / p(\neg S|D)` peut être exprimé comme une série de rapports de vraisemblance.
La probabilité :math:`p(S|D)` elle-même peut être inférée facilement avec :math:`log (p(S | D) / p(\neg S | D))` puisqu'on observe que :math:`p(S|D) + p(\neg S|D) = 1`. 

En utilisant les logarithmes de chacun de ces rapports, on obtient :
:math:`\ln{p(S\vert D)\over p(\neg S\vert D)}=\ln{p(S)\over p(\neg S)}+\sum_i \ln{p(w_i\vert S)\over p(w_i\vert\neg S)}` 

Le document peut donc être classifié comme suit : Il s'agit de spam si :math:`p(S\vert D) > p(\neg S\vert D)` (i.e. si :math:`\ln{p(S\vert D)\over p(\neg S\vert D)} > 0`), sinon il s'agit de courrier normal.

Implémenter le classifieur
~~~~~~~~~~~~~~~~~~~~~~~~~~
En prenant l'hypothèse, qu'un message sur deux est un spam :math:`p(S) = p(\neg S)` implémenter
donc la fonction calculant pour chaque attribut : 
:math:`\sum_i \ln{p(w_i\vert S)\over p(w_i\vert\neg S)}` 

Observer vos résultats avec quelques emails choisis manuellement. 

Mesurer l'éfficacité du classifieur
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
On utilisera le taux de rappel et de précision définie comme ceci : 

:math:`Rappel_i = \frac{documents~correctement~attribues~a~la~classe~i}{nombre~de~documents~appartenants~a~la~classe~i}` 

:math:`Precision_i = \frac{documents~correctement~attribues~a~la~classe~i}{nombre~de~documents~attribues~a~la~classe~i}` 

#. Interpreter les valeurs obtenues

Améliorations
-------------

Comment améliorer le rappel du ham ? 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



Annexes
-------

Résultats
~~~~~~~~~
Nombre de mails utilisés pour l'apprentisage : **50**

::

	--------------------------------------------------------------------------------
	HAM
	precision : 0.937360178971
	recall : 0.75143472023
	--------------------------------------------------------------------------------
	SPAM
	precision : 0.707100591716
	recall : 0.92277992278


Spam classifier
~~~~~~~~~~~~~~~~
.. literalinclude:: ../src/txt_spam/spam_naives_classifier.py

Makefile
~~~~~~~~
.. literalinclude:: ../src/txt_spam/Makefile
   :language: make



.. rubric:: 
.. [#wikipedia] http://fr.wikipedia.org/wiki/Classification_na%C3%AFve_bayesienne
