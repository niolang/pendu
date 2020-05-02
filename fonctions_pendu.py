#!Python3
#fonctions pour le pendu
import os 
import pickle
from random import randrange 
strChemin=os.getcwd()
#os.chdir("E:/Documents/10_Projets/06_Informatique/Python/zpendu")

def strMotAleatoire():
    fileDico = open("liste_francais_nom_commun_ss_accents.txt")
    strDicoData = list(fileDico.read().split("\n"))
    strMotATrouver = strDicoData[randrange(len(strDicoData))] #un seul pour commencer
    fileDico.close()
    return strMotATrouver

def dictRecupScores():
    fileScores = open("sav_scores.txt", "rb")
    unpicklerScores = pickle.Unpickler(fileScores)
    dictScores = unpicklerScores.load()
    fileScores.close()
    return dictScores

def dictMajScores(dictScores:dict):
    fileScores = open("sav_scores.txt", "wb")
    picklerScores =pickle.Pickler(fileScores)
    picklerScores.dump(dictScores)
    fileScores.close()