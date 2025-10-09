# kickoff_django

Projet universitaire visant à introduire Django.

Par Roland RAKOTOMALALA - BUT 3A Info

# Introduction TD1

1 - **Pour installer django** :

`pip install django`

Puis vérifier la version de django admin avec `django-admin --version`

2 - **Initialiser le projet**

`django-admin startproject TutoDjango`

**Transition**

Après avoir configuré le fichier settings.py selon le TD1, on passe à la migration des tables.

3 - **Migration**

**Explication** : Certaines de ces applications utilisent toutefois au moins une table de la base de données, donc il
nous faut créer les tables dans la base avant de pouvoir les utiliser. Pour ce faire, lancez la commande
suivante : `python manage.py migrate`

**En bref** : Nous devons simplement comprendre que les migrations représentent un moyen de configurer la base de données de notre application.

**INFORMATION**

Dans Django, une application est une sous-section de votre projet entier. Django nous encourage à compartimenter notre projet entier Django en applications, pour deux raisons principales :

• Cela permet de garder notre projet organisé et gérable au fur et à mesure qu'il se développe ;
• Cela signifie qu'une application peut éventuellement être réutilisée dans plusieurs projets.

Comme il s'agit de notre tout premier projet Django, il sera suffisamment petit pour que notre code puisse
s'intégrer sans peine dans une seule application. Chaque application doit avoir un nom approprié qui
représente le concept dont l'application est responsable.

**Projet VS Application**

Une **application** est une application Web qui
fait quelque chose – par exemple un système de blog, une base de données publique ou une petite
application de sondage.
Un **projet** est un ensemble de réglages et d’applications pour un site Web
particulier. Un projet peut contenir plusieurs applications. Une application peut apparaître dans plusieurs
projets.

4 - **Initialisation** **de notre première application**

`python3 ./manage.py startapp monApp`

Commande à taper à la racine du projet (`/TutoDjango`).

**Rappel**

Une **vue** a pour fonction de répondre à la visite d'un utilisateur sur le site en renvoyant une page que l’utilisateur peut voir. Une vue est une fonction qui accepte un objet HttpRequest comme paramètre et retourne un objet HttpResponse. Dans notre exemple de vue, nous renvoyons une réponse HTTP avec un contenu HTML simple : un titre H1 disant «Hello Django !».

---

Fin du TD1.

# Début TP1

**Définition** :

- Une migration est un ensemble d'instructions permettant de passer le schéma de votre base de données
  d'un état à un autre. Il est important de noter que ces instructions peuvent être exécutées
  automatiquement, comme un code.

à retenir du document :

* Modifiez les modèles (dans models.py).
* Exécutez `manage.py makemigrations` pour créer des migrations correspondant à ces changements.
* Exécutez `manage.py migrate` pour appliquer ces modifications à la base de données.

Pour ouvrir le shell `python3 manage.py shell`

Erreur I/O : pour la régler, je suis parti dans les settings et j'ai changé le chemin databases __dir__ par /tmp.

Pour éviter de tout perdre à chaque fois, je vais cp ce qui a dans /tmp à chaque fin de séance.

# FIN DU TP1

# DEBUT DU TD2

superuser : 
username : admin
mdp : admin
mail : rolrkt@yahoo.com

---

Dans la documentation il est dit que CompositePrimaryKey est à ce jour incompatible avec Django Admin.

# Fin du TD2

Fin de séance, je suis à la page 9 du TP2

attention il faut installer : `pip install django-bootstrap5`

documentation bootstrap5 : https://django-bootstrap5.readthedocs.io/en/latest/quickstart.html

# FIN DU TP 2

# FIN DU TD 3

# DÉBUT DU TP 3

# FIN DU TP3

# DÉBUT DU TD4

# FIN DU TD4

# DÉBUT DU TP4