# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 23:12:20 2018

@author: Fabien
"""
from random import randint
from IPython.display import display, clear_output, HTML

nbexo_reussi,nb_erreur=0,0

def verif_score():
    print("Il y a eu {} exercices réussis et {} tentatives !".format(nbexo_reussi,nberreur))

def verif_exo1(f) :
    #génération d'un tableau de 100x100 contenant uniuqement des m...
    global nbexo_reussi,nb_erreur
    tab=[['m' for j in range(100)] for i in range(100)]
    i,j= randint(0,99),randint(0,99)
    tab[i][j]='a'
    if (i,j)==f(tab) :
        print("Bien vu ! Passez à l'exercice suivant !")
        nbexo_reussi+=1
        nb_erreur+=1
    else :
        print("""Raté ! Vous aves donné comme position {},
              alors que la position réelle était {}""".format(f(tab),(i,j)))
        nb_erreur+=1
        
def verif_exo2(f):
    global nbexo_reussi,nb_erreur
    with open('TP2_niv1','r') as file :
        tableau=[[a for a in ligne if a!='\n'] for ligne in file]
    
    def voisins(tableau,i,j):
        lst=[]
        if (i>0) and (i<len(tableau)-1):
            if (j>0) and (j<len(tableau[i])-1) :
                  for xi in (i-1,i,i+1) :
                      for yj in (j-1,j,j+1):
                          if xi!=i or yj!=j :
                              lst.append(tableau[xi][yj])
        return lst
    
    i=randint(1,len(tableau)-1)
    j=randint(1,len(tableau[i])-1)
    if voisins(tableau,i,j)==f(tableau,i,j) :
        print("Bien vu ! Passez à l'exercice suivant !")
        nbexo_reussi+=1
        nb_erreur+=1
    else :
        print("""Raté ! Vous aves donné comme liste de voisin {}
        pour la position ( {} , {} ),
        alors que la liste réelle était {}""".format(f(tableau,i,j) , i , 
        j ,voisins(tableau,i,j)))
        nb_erreur+=1
                
                      
    
        
            