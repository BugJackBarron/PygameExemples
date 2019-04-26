# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 20:50:54 2018

@author: Fabien
"""

import pygame
from pygame.locals import *
from random import randint

Largeur=720
Hauteur=576
class Faucon :#Création d'une classe d'objet Faucon définissant le personnage
    """Classe définissant le comportement de l'objet Faucon"""
    def __init__(self,coord=(0,0),pv=3,puissance=5,vitesse=3,images=[]):
        """Méthode contructeur pour créer un objet de type Faucon défini par
        - ses coordonnées de départ ( centre du rectangle );
        - ses points de vie ( par défaut 3);
        - sa puissance ( nombre de tirs simultanés ) ;
        - les images qui le composent sous la forme d'un tableau ( base,
        glissement gauche, glissement droite)"""
        self.pv=pv
        self.puissance=puissance
        self.vitesse=vitesse
        self.images=[pygame.image.load(img) for img in images]
        self.rect=self.images[0].get_rect()
        self.rect.center=coord
        self.tirs=[]
        self.score=0




    def affiche(self,fenetre,num_img) :
        fenetre.blit(self.images[num_img],self.rect)

    def glisse_gauche(self,lim_gauche=0) :
        if self.rect.left+self.vitesse>lim_gauche :
            self.rect=self.rect.move((-self.vitesse,0))
    def glisse_droite(self,lim_droite=Largeur) :
        if self.rect.right+self.vitesse<lim_droite :
            self.rect=self.rect.move((self.vitesse,0))


class Laser :#Classe gérant les rayons lasers
    def __init__(self,origine):
        self.image=pygame.image.load("Blue_laser.png").convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.center=origine.rect.center
        self.vitesse=10
    def deplace(self,vecteur) :
        self.rect=self.rect.move(vecteur)

class Ennemy :
    """Classe définissant les Tie Fighters ennemis"""


    def __init__(self,pv=1) :
        self.image=pygame.image.load("Tie.png").convert_alpha()
        self.rect=self.image.get_rect()
        #coordonnées de départ déterminées aléatoirement, en particulier la
        #l'ordonnée hors écran
        self.coord=(randint(self.rect.width//2,Largeur-self.rect.width//2),
                    randint(-300,-100))
        self.rect.center=self.coord
        self.vitesse=randint(1,5)
        self.pv=pv


    def deplace(self,vecteur):
        self.rect=self.rect.move(vecteur)
        self.coord=self.rect.center



def Intro(fenetre) :
    """Fonction gérant l'intro du jeu"""
    continuer=1

    pygame.mixer.music.load("Imperial.mid")
    pygame.mixer.music.play()
    Ecran_pres=pygame.image.load("Intro.png")
    Press_Start=pygame.image.load("press_start.png")
    fenetre.blit(Ecran_pres,(0,0))
    fenetre.blit(Press_Start,(0,0))
    clign=1
    while continuer==1 :
        for evenement in pygame.event.get() : #Pour chaque evenement
            if evenement.type==KEYDOWN and evenement.key==K_s :
                 pygame.mixer.music.stop()
                 continuer=0
        fenetre.blit(Ecran_pres,(0,0))
        if clign==1 :
            fenetre.blit(Press_Start,(0,0))

        clign=1-clign
        pygame.display.update()
        pygame.time.wait(300)

def Game_Over(fenetre):
    pygame.mixer.music.load("Game_Over.mp3")
    pygame.mixer.music.play()
    GO=pygame.image.load("Game_Over.png")
    fenetre.blit(GO,(0,0))
    pygame.display.update()
    continuer=1
    while continuer==1 :
         for evenement in pygame.event.get() : #Pour chaque evenement
            if evenement.type == QUIT :#Si c'est QUIT
                continuer=0#Alors on change la valeur de continuer, et la boucle s'arrête.








if __name__=="__main__" :


#### Initialisation de Pygame
    pygame.init()
#Création de deux variables contenant les dimensions  afin de créer une
# grille 10x8:

#fenetre est une variable qui contient l'affichage ( display)
    fenetre = pygame.display.set_mode((Largeur+240, Hauteur))

    Intro(fenetre)

#Création de la variable continuer


    continuer =1
    nbennemis=[5,7,10,20,30]
    scoreniveau=[10,15,20,30,50]
    niveau=0
    Liste_Ennemis=[Ennemy() for i in range(nbennemis[niveau])]
    [fenetre.blit(e.image,e.rect) for e in Liste_Ennemis]
    SoundOn = True
#création de la variable fond

    fond=pygame.image.load("fond_ecran_TP2.jpg").convert()
    Zone_texte=pygame.image.load("Zone_texte.png").convert_alpha()
    Zone_text_rect=Zone_texte.get_rect()
    Zone_text_rect=Zone_text_rect.move((Largeur,0))
    fenetre.blit(fond,(0,0))
    fenetre.blit(Zone_texte,Zone_text_rect)
    Millenium=Faucon(coord=(300,540),
                     images=["Faucon_h.png",
                     "Faucon_hg.png",
                     "Faucon_hd.png"],vitesse=10,pv=5)
    Millenium.affiche(fenetre,0)

    pygame.display.update()

    Boum=pygame.mixer.Sound("Boum.wav")
    Chewycry=pygame.mixer.Sound("chewycry.wav")
    LaserSound=pygame.mixer.Sound("LAZER.WAV")
    #Imperial=pygame.mixer.Sound("Imperial.mid")
    #Imperial.play()
    Intro(fenetre)
    while continuer ==1 : #tant que continuer est égal à 1, on recommence la boucle
        image=0
        if (Millenium.score>scoreniveau [0]) and len(scoreniveau)>1 :
            scoreniveau.pop(0)
            nbennemis.pop(0)
        if len(Liste_Ennemis)<nbennemis[niveau] :
            Liste_Ennemis.append(Ennemy())
        for evenement in pygame.event.get() : #Pour chaque evenement
            if evenement.type == QUIT :#Si c'est QUIT
                continuer=0#Alors on change la valeur de continuer, et la boucle s'arrête.
            if evenement.type==KEYDOWN and evenement.key==K_F10 :# F10 pour couper ou remettre le son
                SoundOn=not(SoundOn)
        dic_touche=pygame.key.get_pressed()
        if dic_touche[K_LEFT]:
            Millenium.glisse_gauche()
            image=1
        if dic_touche[K_RIGHT]:
            Millenium.glisse_droite()
            image=2
        if dic_touche[K_SPACE]and (
                    len(Millenium.tirs)<Millenium.puissance) :
                Millenium.tirs.append(Laser(Millenium))
                if SoundOn : LaserSound.play()


        ##teste la collision entre le faucon et les Tie
        colM=Millenium.rect.collidelist(Liste_Ennemis)
        if colM!=-1 :
            Liste_Ennemis.pop(colM)
            if SoundOn : Chewycry.play()
            Millenium.pv=Millenium.pv-1
            if Millenium.pv==0 :
                continuer=0

        #Blit du fond et du Faucon
        fenetre.blit(fond,(0,0))

        Millenium.affiche(fenetre,image)
        #Blit des tie ou disparition
        for e in Liste_Ennemis :
            if e.rect.top>Hauteur :
                Liste_Ennemis.remove(e)
            else :
                e.deplace((0,e.vitesse))
                fenetre.blit(e.image,e.rect)
        #Blit des lasers ou disparition
        for l in Millenium.tirs :
            if l.rect.bottom<0 :
                Millenium.tirs.remove(l)
            else :
                col=l.rect.collidelist(Liste_Ennemis)
                if col!=-1:
                    Millenium.tirs.remove(l)
                    Liste_Ennemis.pop(col)
                    Millenium.score+=1
                    if SoundOn : Boum.play()
                l.deplace((0,-l.vitesse))
                fenetre.blit(l.image,l.rect)

        font = pygame.font.Font(None, 36)
        text = font.render("""Score : {}""".format(Millenium.score), 1, (150, 10, 10))
        textvie=font.render("Vie : {}".format(Millenium.pv),1,(10,150,150))
        textpos = text.get_rect()
        textviepos=textvie.get_rect()
        textpos.center = Zone_text_rect.center
        textviepos.center=Zone_text_rect.center
        textviepos=textviepos.move((0,50))
        fenetre.blit(Zone_texte,Zone_text_rect)
        fenetre.blit(text, textpos)
        fenetre.blit(textvie, textviepos)
        pygame.time.wait(15)#pause de xx(dépend du pc...)  millisecondes, histoire de voir ce qui se passe.
        pygame.display.update()


    Game_Over(fenetre)
pygame.display.quit()

