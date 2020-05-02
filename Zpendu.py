#!Python3

#biblis
import os #utilisation de fichiers externes
import pickle #stockage/récupération d'objets dans des fichiers externes
import fonctions_pendu
import time
#os.chdir("E:/Documents/10_Projets/06_Informatique/Python/zpendu")

#intro du jeu
os.system('cls')
print("**********".center(50))
print("Bienvenue dans le pendu".center(50))
print("**********".center(50), "\n")

while 1==1:
    strChoix=input("Que souhaitez vous faire :\n[J]ouer\n[A]fficher les scores\n[Q]uitter\n")
    if strChoix.lower()=='j': #Jouer
        #On demande le nom du joeur
        strPseudo=input("Quel est votre pseudo?")
        strPseudo=strPseudo.lower()
        #On test s'il existe dans la base de données des joueurs
        dictScores = fonctions_pendu.dictRecupScores()

        #si oui, on lui rappelle son score
        if strPseudo in dictScores.keys():
            print("votre score actuel est :", dictScores[strPseudo] )
        #sinon on l'inscrit avec un score de 0
        else:
            print("Première partie, bienvenue", strPseudo)
            dictScores[strPseudo]=int()

        #on ouvre la "bibliothèque" de mot pour en récupérer un
        strMotATrouver=fonctions_pendu.strMotAleatoire()
        #On créé une variable qui contiendra notre avancement:
        strMotEnCours = "-" #on au toujours au moins un caractère
        i=1
        while i<len(strMotATrouver):
            strMotEnCours = strMotEnCours[:i] + "-"
            i += 1

        time.sleep(1)
        os.system('cls')
        print("**********".center(50))
        print("{}, il faut trouver le mot suivant : {} , {} lettres".format(strPseudo,strMotEnCours,len(strMotEnCours)))

        #Boucle du jeu, tant qu'on n'a pas gagné ou perdu
        boolGagne = boolPerdu = False
        nbDecomptePendu = 0
        while boolPerdu == False and boolGagne == False:
            #on demande une lettre et on vérifie l'entrée de l'utilisateur
            strLettreJoue=("nok")
            while len(strLettreJoue) != 1:
                try:
                    strLettreJoue = input("Quelle lettre souhaitez vous choisir?")
                    assert len(strLettreJoue)==1
                except AssertionError:
                    print("Merci de n'entrer qu'une lettre, svp")
                except:
                    print("Merci de n'entrer qu'une lettre, svp")

            print("lettre choisie :", strLettreJoue.lower(),"\n")
            time.sleep(1)
            os.system('cls')

            boolLettreTrouvee=False            
            i=0
            while i<len(strMotATrouver):
                #print(strLettreJoue, "-", strMotATrouver[i])
                if strLettreJoue == strMotATrouver[i]:
                    boolLettreTrouvee=True
                    strMotEnCours = strMotEnCours[0:i] + strLettreJoue + strMotEnCours[i+1:]
                    
                i += 1
            print(strMotEnCours.center(20))
            
            #on la compare à la chaine 
            if boolLettreTrouvee == True:
                print("lettre {} est présente, vous en êtes à {}/8 erreurs\n".format(strLettreJoue,nbDecomptePendu))
                if strMotEnCours == strMotATrouver:
                    boolGagne = True
            elif boolLettreTrouvee == False:
                nbDecomptePendu +=1
                print("Raté pour le {}, vous avez fait {}/8 erreurs".format(strLettreJoue,nbDecomptePendu))
                if nbDecomptePendu >= 8:
                    boolPerdu = True
            
        if boolGagne:
            dictScores[strPseudo]+= 8-nbDecomptePendu
            fonctions_pendu.dictMajScores(dictScores)
            print("Félicitations, vous avez trouvé le mot", strMotATrouver)
            print("Vous gagnez", 8-nbDecomptePendu, "points, nouveau score :", dictScores[strPseudo])
        else:
            print("Perdu! le mot était", strMotATrouver)

    elif strChoix.lower()=='a': #Afficher les scores
        print("Listes des scores")
        dictScores = fonctions_pendu.dictRecupScores()
        for elts in dictScores:
            print(elts, ":", dictScores[elts])
        input("appuyez sur -Entrée- pour revenir au menu")
        os.system('cls')

    elif strChoix.lower()=='q': #Quitter
        print("le programme va s'arrêter, à bientôt!")
        exit()

    else: #entrée invalide
        print("entre non valide, veuillez réessayer")