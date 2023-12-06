import os

print("Advent Of Code 2023 - Exercice 6_2")

Fichier_Input = open("input.txt", 'r')

Lecture_Boucle = True
Fichier_Ligne = ""
Liste_Temps=[]
Liste_Distance=[]
j=1

while Lecture_Boucle:
    Fichier_Ligne = Fichier_Input.readline()
    Fichier_Ligne = Fichier_Ligne.replace("\n","");
    Fichier_Ligne = Fichier_Ligne.replace(" ","");
    print(Fichier_Ligne)
    if Fichier_Ligne :
       Fichier_Ligne_split=(Fichier_Ligne.split(":"))
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

Depart_Boucle = int(Liste_Distance[0])/int(Liste_Temps[0])
print(int(Depart_Boucle))

print("_____________________________")
print("Temps =",Liste_Temps[0])
print("Distance = ",Liste_Distance[0])
for j in range(int(Depart_Boucle),int(Liste_Temps[0])):
   Temps_Chargement = j + 1
   Temps_Restant= int(Liste_Temps[0]) - Temps_Chargement
   Distance = Temps_Restant*Temps_Chargement
   Ecart=int(Liste_Distance[0])-Distance
   if Distance>int(Liste_Distance[0]):
      break;
print(Temps_Chargement,Temps_Restant,Distance,Liste_Distance[0],Ecart)
Resultat=int(Liste_Temps[0])-2*Temps_Chargement+1
print(Resultat)

      