# api-galaxy

L'api-galaxy est un projet qui répertorie les objets astronomiques en prennant pour référence le catalogue de Messier.

L'intérêt est donc d'afficher les différents coprs celestes en fonction de différents critères (comme la visibilité ou la distance).
Tous les messiers sont disponibles via une API développée en Python.

Pour ce projet, les technologies utilisées sont :

- docker (sqlite)
- flask (WSGI web application framework)
- peewee (ORM)

URL du projet : http://messier.gaetandubosclard.com/

## Accèder aux différents messiers à la fin de l'url : remplacer "param" par :

"Messiers by visibility" -> oeil OU telescope
"Messiers by season" -> ete, hiver, automne, printemps

_Créé par : Gaetan Dubosclard, Pierre Barijaona, Steven Razanajato_

