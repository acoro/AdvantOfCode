import os

print("Advent Of Code 2023 - Exercice 4_1")

Fichier_Input = open("input.txt", 'r')

Lecture_Boucle = True
Fichier_Ligne = ""
Nombre_Resultat=0
Liste_Resultat=[]
Somme_Points=0

while Lecture_Boucle:
    Fichier_Ligne = Fichier_Input.readline()
    Fichier_Ligne = Fichier_Ligne.replace("\n","");
    Fichier_Ligne = Fichier_Ligne.replace("  "," ");
    if Fichier_Ligne :
       Tirage_Ligne_Liste=(Fichier_Ligne.split(":"))
       Tirage_Numero=Tirage_Ligne_Liste[0].split(" ")
       Cartes_Liste_Gagnant,Mes_Carte_Liste=((Tirage_Ligne_Liste[1]).split("|"))
       Carte_Liste_Gagnant=(Cartes_Liste_Gagnant.split(" "))
       Ma_Carte_Liste=(Mes_Carte_Liste.split(" "))
       set_Carte_Liste_Gagnant = set(Carte_Liste_Gagnant)
       set_Ma_Carte_Liste = set(Ma_Carte_Liste)
       print(Tirage_Numero[1],Carte_Liste_Gagnant,Ma_Carte_Liste,set_Carte_Liste_Gagnant&set_Ma_Carte_Liste)
       Nombre_Resultat=len(set_Carte_Liste_Gagnant&set_Ma_Carte_Liste)-1
       Liste_Resultat.append(Nombre_Resultat)
    if not Fichier_Ligne:
       Lecture_Boucle = False
print("_____________________________")
print(Liste_Resultat)

for i in Liste_Resultat:
   if i!=0:
      Somme_Points = Somme_Points + 2**(i-1)

print("_____________________________")
print("Le nombre de points est ", Somme_Points)
