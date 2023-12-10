import os

print("Advent Of Code 2023 - Exercice 9_2")

Fichier_Input = open("input.txt", 'r')

Lecture_Boucle = True
Derniere_Ligne = False
Fichier_Ligne = ""
Liste_Nombre = []
Liste_global = []
Liste_temporaire = []
Liste_intermediaire = []
Index=0
Somme=0


while Lecture_Boucle:
    print("_____________________________")
    Fichier_Ligne = Fichier_Input.readline()
    Liste_global.clear()
    Liste_intermediaire.clear()
    Derniere_Ligne = True
    Index=0
    if Fichier_Ligne :
       Fichier_Ligne = Fichier_Ligne.replace("\n","");
       Liste_Nombre=Fichier_Ligne.split(" ")
       Liste_global.append(Liste_Nombre)
       Liste_intermediaire = Liste_Nombre[:]
       print(Liste_intermediaire)
       while Derniere_Ligne:
          print(Index)
          Liste_intermediaire.clear()
          for i in range(len(Liste_global[Index])-1):
              Liste_intermediaire.append((int(Liste_global[Index][i+1])-int(Liste_global[Index][i])))
          Liste_global.append(Liste_intermediaire[:])
          print(Liste_intermediaire)
          if (Liste_intermediaire.count(0))==(len(Liste_intermediaire)):
             print(Liste_global)
             for j in range(len(Liste_global)):
                if (j%2)==0 :
                   Somme=Somme+int(Liste_global[j][0])               
                else :
                   Somme=Somme-int(Liste_global[j][0])
             print(Somme)
             Derniere_Ligne = False
          Index=Index+1
    else :
       Lecture_Boucle = False

print("_____________________________")
print(" La Somme est ", Somme)









      