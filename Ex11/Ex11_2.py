import os

print("Advent Of Code 2023 - Exercice 11_2")

Fichier_Input = open("input.txt", 'r')

Lecture_Boucle = True
Fichier_Ligne = ""
Matrice = []
Liste_Galaxies = []
Distance=0
Somme=0
Vide=True
Liste_Vide_Vert = []
Liste_Vide_Hori = []
Offset = 999999

while Lecture_Boucle:
    Fichier_Ligne = Fichier_Input.readline()
    if Fichier_Ligne :
       Fichier_Ligne = Fichier_Ligne.replace("\n","");
       Matrice.append(list(Fichier_Ligne))
    else :
       Lecture_Boucle = False

for k in range(len(Matrice[0])):
    Vide=True
    for j in range(len(Matrice)):
       if Matrice[j][k]=="#":
          Vide=False
    if Vide == True :
       print("Trouvé :",k,j)
       Liste_Vide_Vert.append(k)

for k in range(len(Matrice)):
    Vide=True
    for j in range(len(Matrice[0])):
       if Matrice[k][j]=="#":
          Vide=False
    if Vide == True :
       print("Trouvé :",k,j)
       Liste_Vide_Hori.append(k)     

print("_____________________________")

#print(Matrice)
print(Liste_Vide_Vert)
print(Liste_Vide_Hori)

for k in range(len(Matrice)):
    for j in range(len(Matrice[0])):
       #print(k,j)
       if Matrice[k][j]=="#":
          #print("Trouvé :",k,j)
          Liste_Galaxies.append([k,j])

print("_____________________________")

print(Liste_Galaxies)
print(len(Liste_Galaxies))

for i in range(len (Liste_Galaxies)):
   for k in reversed (Liste_Vide_Hori):
      if int(Liste_Galaxies[i][0]) > int(k):
         Liste_Galaxies[i][0]=int(Liste_Galaxies[i][0]) + Offset
   for k in reversed (Liste_Vide_Vert):
      if int(Liste_Galaxies[i][1]) > int(k):
         Liste_Galaxies[i][1]=int(Liste_Galaxies[i][1]) + Offset 
print("_____________________________")

print(Liste_Galaxies)
print(len(Liste_Galaxies))

print("_____________________________")
for l in range(len(Liste_Galaxies)):
    for m in range(len(Liste_Galaxies)):
       if(m>l):
          Somme=Somme+1
          Distance=Distance+abs(Liste_Galaxies[m][0]-Liste_Galaxies[l][0])+abs(Liste_Galaxies[m][1]-Liste_Galaxies[l][1])
          #print(Distance)
print(Somme,Distance)

