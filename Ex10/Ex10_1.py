import os

print("Advent Of Code 2023 - Exercice 10_1")

Fichier_Input = open("input.txt", 'r')

Lecture_Boucle = True
Derniere_Ligne = False
Fichier_Ligne = ""
Buffer = ""
Matrice = []
Position_Trouve = False
Arrive = False
Mouvement =""
Position = []
Next_Position = []
Distance=0
x=0
y=0


# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.

Haut={"|","F","7"}
Gauche={"-","F","L"}
Bas={"|","J","L"}
Droite={"-","J","7"}

while Lecture_Boucle:
    Fichier_Ligne = Fichier_Input.readline()
    if Fichier_Ligne :
       Fichier_Ligne = "." + Fichier_Ligne.replace("\n",".");
       Matrice.append(list(Fichier_Ligne))
       Taille = len(Matrice[0])
       print(Taille)

    else :
       Lecture_Boucle = False
       for i in range(len(Matrice[0])):
          Buffer=Buffer +"."
       Matrice.insert(0,list(Buffer))
       Matrice.append(list(Buffer))

print("_____________________________")

print(Matrice)

for j in range(len(Matrice)):
   if Position_Trouve :
      break
   for k in range(len(Matrice[0])):
      if Position_Trouve :
         break
      print(k,j)
      if Matrice[k][j]=="S":
         print("Trouvé :",j,k)
         Position=[j,k]
         Position_Trouve = True

x=int(Position[0])
y=int(Position[1])
print(x,y)
print(Matrice[y][x])
print("_____________________________")
print(Matrice[y-1][x])
print(Matrice[y+1][x])
print(Matrice[y][x-1])
print(Matrice[y][x+1])
print("_____________________________")
if (len(Haut&set(Matrice[y-1][x])))==1:
   Next_Position=Matrice[y-1][x]
   Next_Position_Trouve = True
   Mouvement="H"
   print(Matrice[y-1][x], "Test1")
elif(len(Gauche&set(Matrice[y][x-1])))==1:
   Next_Position=Matrice[y][x-1]
   Next_Position_Trouve = True
   Mouvement="G"
   print(Matrice[y][x-1],"Test2")
elif(len(Bas&set(Matrice[y+1][x])))==1:
   Next_Position=Matrice[y+1][x]
   Next_Position_Trouve = True
   Mouvement="B"
   print((Matrice[y+1][x]),"Test3")
#(len(Droite&set(Matrice[y][x+1]))))

print("_____________________________")
while not Arrive:
   print(Distance,"          ", x,y,"          ",Next_Position,"          ", Matrice[y][x],"          ", Mouvement)
   if Mouvement == "H":
      if Next_Position == "|" :
         Mouvement ="H"
         y=y-1
      elif Next_Position == "F" :
         Mouvement ="D"
         x=x+1
      elif Next_Position == "7" :
         Mouvement ="G"
         x=x-1        
   elif Mouvement == "G":
      if Next_Position == "-" :
         Mouvement ="G"
         x=x-1
      elif Next_Position == "F" :
         Mouvement ="B"
         y=y+1
      elif Next_Position == "L" :
         Mouvement ="H"
         y=y-1
   elif Mouvement == "B":
      if Next_Position == "|" :
         Mouvement ="B"
         y=y+1
      elif Next_Position == "L" :
         Mouvement ="D"
         x=x+1
      elif Next_Position == "J" :
         Mouvement ="G"
         x=x-1 
   elif Mouvement == "D":
      if Next_Position == "-" :
         Mouvement ="D"
         x=x+1
      elif Next_Position == "J" :
         Mouvement ="H"
         y=y-1
      elif Next_Position == "7" :
         Mouvement ="B"
         y=y+1
   Next_Position=Matrice[y][x]          
   Distance=Distance+1
   if Next_Position == "S":
      Arrive = True

print("_____________________________")
print((Distance)/2)


      