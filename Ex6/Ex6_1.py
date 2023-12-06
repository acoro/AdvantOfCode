import os

print("Advent Of Code 2023 - Exercice 6_1")

Fichier_Input = open("input.txt", 'r')

Lecture_Boucle = True
Fichier_Ligne = ""
Liste_Temps=[]
Liste_Distance=[]
j=1

while Lecture_Boucle:
    Fichier_Ligne = Fichier_Input.readline()
    Fichier_Ligne = Fichier_Ligne.replace("\n","");
    Fichier_Ligne = Fichier_Ligne.replace("  "," ");
    if Fichier_Ligne :
       Fichier_Ligne_split=(Fichier_Ligne.split(":"))
       Fichier_Ligne_split=Fichier_Ligne_split[1].split(" ")
       for i in range(len(Fichier_Ligne_split)):
          if Fichier_Ligne_split[i].isdigit():
             if j==1:
                Liste_Temps.append(Fichier_Ligne_split[i])
             else :
                Liste_Distance.append(Fichier_Ligne_split[i])
       j=j+1
    if not Fichier_Ligne:
       Lecture_Boucle = False
print("_____________________________")
print(Liste_Temps)
print(Liste_Distance)
Resultat=1
Resultat_intermediaire=0

for i in range(len(Liste_Temps)):
   print("_____________________________")
   print("Temps =",Liste_Temps[i])
   print("Distance = ",Liste_Distance[i])
   for j in range(int(Liste_Temps[i])):
      Temps_Chargement = j + 1
      Temps_Restant= int(Liste_Temps[i]) - Temps_Chargement
      Distance = Temps_Restant*Temps_Chargement
      print(Temps_Chargement,Temps_Restant,Distance)
      if Distance>int(Liste_Distance[i]):
         Resultat_intermediaire=Resultat_intermediaire+1
   Resultat=Resultat*Resultat_intermediaire
   Resultat_intermediaire=0
   
print("_____________________________")
print("Le Résultat est :",Resultat)

      