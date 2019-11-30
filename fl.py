import os
from threading import Thread
from tkinter import *

from flask import app, request, render_template

app1 = app.Flask('app1')

# variable globale parce que c'est plus simple pour resoudre ton bug
compteur = 0


@app1.route('/', methods=['GET'])
def index():
    # il faut qu'elle soit globale !
    global compteur
    if "open" in request.args:
        print("open")
        compteur += 1
        Application.ouvrir()
    elif "close" in request.args:
        print("close")
        compteur -= 1
        Application.fermer()
    return render_template('index.html', compteur=compteur)


def start_app1():
    print("starting app1")
    app1.run(port=5001)


class FenetreGraphique(Tk):
    #
    # Variables de la classe
    LARGEUR = 850         # Dimensions de la fenêtre
    HAUTEUR = 600
    POS_X_PORTIQUE = 40    # Position du portique
    POS_Y_PORTIQUE = 100

    # Constructeur de la fenêtre
    def __init__(self):
        Tk.__init__(self)
        # Titre
        self.title("Flask, WS sur un Thread")
        dimensionFenetre = "%dx%d" % (self.LARGEUR, self.HAUTEUR)
        self.geometry(dimensionFenetre)
        # Instanciation d'une zone qui contiendra un portique
        #self.portique1 = Portique(self, self.POS_X_PORTIQUE, self.POS_Y_PORTIQUE, 1)
        # Initialisation de l'événement de gestion de la fermeture de la fenêtre graphique
        self.protocol("WM_DELETE_WINDOW", self.fermetureFenetreCroix)

    # Gestion de la fermeture de la fenetre

    def ouvrir(self):
        print("Tkinter a bien reçu le message !")
        print("j'aime pas tkinter je te laisse faire pascal")
        door_opened = '''
             /|
            / |
           /__|______
          |  __  __  |
          | |  ||  | |
          | |__||__| |
          |  __  __()|
          | |  ||  | |
          | |  ||  | |
          | |__||__| |
          |__________|
        '''
        print(door_opened)

    def fermer(self):
        print("Tkinter a bien reçu le message !")
        print("j'aime toujours pas tkinter :)")
        door_opened = '''
         ==========+
        |  __  __  ||
        | |  ||  | ||
        | |  ||  | ||
        | |__||__| ||
        |  __  __()||
        | |  ||  | +|
        | |  ||  | ||
        | |  ||  | ||
        | |__||__| ||
        |__________||
        '''
        print(door_opened)

    def fermetureFenetreCroix(self):
        print("Interception de la fermeture de la fenetre par la croix")

        self.destroy()


if __name__ == '__main__':
    print("lancement du serveur web")
    Thread(target=start_app1).start()
    print("main : instanciation tkinter")
    Application = FenetreGraphique()
    Application.mainloop()
    print("bye !")
