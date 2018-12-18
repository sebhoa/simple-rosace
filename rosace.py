#! /usr/bin/env python3

"""
Dessine sur un cercle les tables de multiplication formant
ainsi une belle rosace
Usage : rosace.py -t n -m m -c
Dessine la table de n sur m points répartis sur un cercle
Si l'option -c est présente, le cercle sera en couleur
"""

import turtle
import argparse
import random

class Rosace(turtle.Turtle):

    DEFAULT_TABLE = 2
    DEFAULT_MODULO = 10
    DEFAULT_COLOR = 'black'
    RADIUS = 250
    INITIAL_POS = 0, -RADIUS

    def __init__(self):
        self.table = Rosace.DEFAULT_TABLE
        self.modulo = Rosace.DEFAULT_MODULO
        self.pts = []

        # La Partie turtle de la rosace
        #
        turtle.Turtle.__init__(self)


    def settings(self):
        # Réglagles de la tortue
        #
        self.ht()               # masquer la tortue
        self.screen.tracer(400) # ça c'est juste pour dessiner plus vite
        self.screen.colormode(255)
        self.color(Rosace.DEFAULT_COLOR)

        # Traitement des options
        #
        parser = argparse.ArgumentParser()
        parser.add_argument('-t', help='Un entier entre 2 et 9, la table qu\'on va dessiner')
        parser.add_argument('-m', help='Un diviseur de 360')
        parser.add_argument('-c', help='Rajoute de la couleur', action='store_true')

        args = parser.parse_args()
        if args.t:
            self.table = int(args.t)
        if args.m:
            modulo = int(args.m)
            if 360 % modulo == 0:
                self.modulo = modulo
        if args.c:
            self.color(self.random_color())


    def random_color(self):
        return tuple([random.randint(0,255) for _ in range(3)])

    def mainloop(self):
        self.screen.update()    # pour mettre à jour le canvas (à cause du tracer(400))
        self.screen.mainloop()

    # -- FONCTIONS DE DESSIN
    # --

    def move_to(self, pos, trace=False):
        if not trace:
            self.up()
        self.goto(pos)
        self.down()


    def draw_circle(self):
        """
        Dessine le cercle intial et récupère en même temps les 
        différents points sur ce cercle correspondant aux entiers
        0, 1, 2... self.modulo - 1
        """
        self.move_to(Rosace.INITIAL_POS)
        delta_angle = 360 // self.modulo
        for _ in range(self.modulo):
            self.pts.append(self.pos())
            self.circle(Rosace.RADIUS, delta_angle)


    def draw_segments(self):
        """
        Dessine la multiplication : m = n * self.table pour les
        n de 1 à self.modulo - 1, en liant les points n et m 
        """
        for n in range(1,self.modulo):
            m = (self.table * n) % self.modulo 
            self.move_to(self.pts[n])
            self.move_to(self.pts[m], True)

    def update(self):
        self.screen.update()

    def reset(self):
        self.pts.clear()
        self.clear()



# MAIN

my_draw = Rosace()
my_draw.settings()
my_draw.draw_circle()
my_draw.draw_segments()
my_draw.mainloop()





