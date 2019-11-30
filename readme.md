# Projet Portique

## Comment ça marche ?

1. on lance flask dans un thread en premier
2. on instance Tkinter ensuite

## flask :

* pas de socket io, pas de librairie rien.
* seulement un bouton et une méthode GET
* on appuie sur le bouton, flask reçoit une requete GET qui contient
  * open : il augmente la variable globale compteur et appelle une méthode ouvrir

      sur l'instance de la porte
  * close : idem

## tkinter

* 2 méthodes externes qui font qq chose (pour l'instant des prints...)
* et c'est tout. J'ai repris ton code pour instancier tkinter

## Asynchrone

s'il est possible de manipuler directement le portique (autrement qu'avec
les boutons), alors la page web n'en sait rien.
On ne peut forcer la page à se rafraichir depuis l'objet tkinter
il faut trouver un moyen de forcer le rafraichissement de la page.
Peut-être qu'avec socketio ça peut marcher...

mais j'y ai pas reflechi.
