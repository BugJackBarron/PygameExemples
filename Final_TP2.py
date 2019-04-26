# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 20:50:54 2018

@author: Fabien
"""
import pygame
from pygame.locals import *
from itertools import cycle

class Faucon:
    def __init__(self,x,y):
        self.images=cycle([pygame.image.load("Faucon.png").convert_alpha()])        
        self.rect=pygame.Rect(x,y,self.images[0].get_width(),self.images[0].get_height())
        self.vitesse=3
        
def Charge_Niveau(fichier):
    """Renvoie un tableau contenantchaque élément du niveau"""
    with open(fichier,'r') as f :
        return [[a for a in ligne if a!='\n'] for ligne in f]

def Affiche_murs(niveau, mur):
    for num_line,line in enumerate(niveau) :
        for num_col,cellule in enumerate(line) :
            if cellule=="m" :
                fenetre.blit(mur,(num_col*72,num_line*72))
                
def Position_grille(t,dimension=72):
    """retourne un tuple contenant le numéro de ligne et le numéro de colonne 
    dans une grille de dimension donnée, par défaut 72"""
    return tuple([a//dimension for a in t])

def Somme_position(P,V):
    return tuple([sum(t) for t in zip(P,V) ])

def Detecte_collision (rect,niveau,vitesse=(0,0),objet="m",unite_grille=72):
    """Détecte une collision entre un rectangle et un objet du niveau,
        par défaut un mur"""
    if vitesse[1]<0 :#Colision haute
        col_l,line_l=Position_grille(Somme_position(rect.topleft,vitesse))
        col_r,line_r=Position_grille(Somme_position(rect.topright,vitesse))
        #print("Dans la ligne{} et la colonne {} : objet {}".format(line_l,col_l
         #     ,niveau[line_l][col_l]))
        #print("Dans la ligne{} et la colonne {} : objet {}".format(line_r,col_r
          #    ,niveau[line_r][col_r]))
        try :
            return (niveau[line_l][col_l]==objet) or (niveau[line_r][col_r]==objet)
        except :
            return True
    if vitesse[1]>0 :#colision basse
        col_l,line_l=Position_grille(Somme_position(rect.bottomleft,vitesse))
        col_r,line_r=Position_grille(Somme_position(rect.bottomright,vitesse))
        #print("Dans la ligne{} et la colonne {} : objet {}".format(line_l,col_l
         #     ,niveau[line_l][col_l]))
        #print("Dans la ligne{} et la colonne {} : objet {}".format(line_r,col_r
          #    ,niveau[line_r][col_r]))
        try :
            return (niveau[line_l][col_l]==objet) or (niveau[line_r][col_r]==objet)
        except :
            return True
    if vitesse[0]<0 :#Colision Gauche
        col_l,line_l=Position_grille(Somme_position(rect.bottomleft,vitesse))
        col_r,line_r=Position_grille(Somme_position(rect.topleft,vitesse))
        #print("Dans la ligne{} et la colonne {} : objet {}".format(line_l,col_l
         #     ,niveau[line_l][col_l]))
        #print("Dans la ligne{} et la colonne {} : objet {}".format(line_r,col_r
          #    ,niveau[line_r][col_r]))
        try :
            return (niveau[line_l][col_l]==objet) or (niveau[line_r][col_r]==objet)
        except :
            return True
    if vitesse[0]>0:#colision droite
        col_l,line_l=Position_grille(Somme_position(rect.bottomright,vitesse))
        col_r,line_r=Position_grille(Somme_position(rect.topright,vitesse))
        #print("Dans la ligne{} et la colonne {} : objet {}".format(line_l,col_l
         #     ,niveau[line_l][col_l]))
        #print("Dans la ligne{} et la colonne {} : objet {}".format(line_r,col_r
          #    ,niveau[line_r][col_r]))
        try :
            return (niveau[line_l][col_l]==objet) or (niveau[line_r][col_r]==objet)
        except :
            return True
    return False
        
    
        
#### Initialisation de Pygame
pygame.init() 
#Création de deux variables contenant les dimensions  afin de créer une
# grille 10x8:
Largeur, Hauteur = 720,576
#fenetre est une variable qui contient l'affichage ( display)
fenetre = pygame.display.set_mode((Largeur, Hauteur))
#Création de la variable continuer
continuer =1

#création de la variable fond

fond=pygame.image.load("fond_ecran_TP2.jpg").convert()
mur=pygame.image.load("Mur_SW.png").convert_alpha()
niveau=Charge_Niveau("TP2_niv1")

#Creation de la variable personnage

base=pygame.image.load("Faucon/FAucon710.png").convert_alpha()
personnage=base.copy()
vitesse=6
#Placement du fond sur la fenetre
fenetre.blit(fond,(0,0))
#Creation du Rect
position_personnage=personnage.get_rect()
position_personnage=position_personnage.move(72,72)

Affiche_murs(niveau,mur)


#Boucle Tant que :
while continuer ==1 : #tant que continuer est égal à 1, on recommence la boucle
    for evenement in pygame.event.get() : #Pour chaque evenement
        if evenement.type == QUIT :#Si c'est QUIT
            continuer=0#Alors on change la valeur de continuer, et la boucle s'arrête.
    dic_touche=pygame.key.get_pressed()
    
    if dic_touche[K_DOWN] :
        if position_personnage.bottom<Hauteur and not(Detecte_collision(position_personnage,
                                                               niveau
                                                             ,vitesse=(0,vitesse))):
            position_personnage=position_personnage.move(0,vitesse)#On met à jour la nouvelle position
            personnage=base
            
    elif dic_touche[K_UP] :
        if position_personnage.top>0 and not(Detecte_collision(position_personnage,
                                                               niveau
                                                             ,vitesse=(0,-vitesse))):
            position_personnage=position_personnage.move(0,-vitesse)#On met à jour la nouvelle position
            personnage=pygame.transform.rotate(base,180)
            
    elif dic_touche[K_LEFT] :
        if position_personnage.left>0 and not(Detecte_collision(position_personnage,
                                                               niveau
                                                             ,vitesse=(-vitesse,0))):
            position_personnage=position_personnage.move(-vitesse,0)#On met à jour la nouvelle position
            personnage=pygame.transform.rotate(base,-90)
            
    elif dic_touche[K_RIGHT] :
        if position_personnage.right<Largeur and not(Detecte_collision(position_personnage,
                                                               niveau
                                                             ,vitesse=(vitesse,0))):
            position_personnage=position_personnage.move(vitesse,0)#On met à jour la nouvelle position
            personnage=pygame.transform.rotate(base,90)
            
    #On recolle le fond
    fenetre.blit(fond,(0,0))
    Affiche_murs(niveau,mur)
    #on recolle le personnage
    fenetre.blit(personnage,position_personnage)
    
    pygame.display.update() #rafraichissement de l'écran
    #pygame.time.wait(1)#pause de 10 millisecondes, histoire de voir ce qui se passe.

#On quitte Pygame ( Attention ! Absolument nécessaire sous windows ! )
pygame.quit()