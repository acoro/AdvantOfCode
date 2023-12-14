import os

print("Advent Of Code 2023 - Exercice 10_2")
os.remove("input_tmp.txt")
Fichier_Input = open("input.txt", 'r')

Lecture_Boucle = True
Derniere_Ligne = False
Fichier_Ligne = ""
Buffer = ""
Matrice = []
Matrice_temp = []
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
       Matrice_temp.append(list(Fichier_Ligne))
       Taille = len(Matrice[0])
       print(Taille)

    else :
       Lecture_Boucle = False
       for i in range(len(Matrice[0])):
          Buffer=Buffer +"."
       Matrice.insert(0,list(Buffer))
       Matrice.append(list(Buffer))
       Matrice_temp.insert(0,list(Buffer))
       Matrice_temp.append(list(Buffer))

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
   print(Distance,"          ", x,y,"          ", Matrice[y][x],"         ", Mouvement)
   Matrice_temp[y][x]="C"
   if Mouvement == "H":
      if Next_Position == "|" :
         # if Matrice[y][x-1]==".":
            # Matrice[y][x-1]="0"
            # print("Modification1")
         # if Matrice[y][x+1]==".":
            # Matrice[y][x+1]="1"
            # print("Modification2")
         Mouvement ="H"
         y=y-1
      elif Next_Position == "F" :
         # if Matrice[y][x-1]==".":
            # Matrice[y][x-1]="0" 
            # print("Modification3")
         # if Matrice[y-1][x-1]==".":
            # Matrice[y-1][x-1]="0"  
            # print("Modification4")
         # if Matrice[y-1][x]==".":
            # Matrice[y-1][x]="0"   
            # print("Modification5")
         Mouvement ="D"
         x=x+1
      elif Next_Position == "7" :
         # if Matrice[y][x+1]==".":
            # Matrice[y][x+1]="1"
            # print("Modification6")
         # if Matrice[y-1][x+1]==".":
            # Matrice[y-1][x+1]="1"
            # print("Modification7")
         # if Matrice[y-1][x]==".":
            # Matrice[y-1][x]="1"
            # print("Modification8")
         Mouvement ="G"
         x=x-1        
   elif Mouvement == "G":
      if Next_Position == "-" :
         # if Matrice[y-1][x]==".":
            # Matrice[y-1][x]="1"
            # print("Modification9")
         # if Matrice[y+1][x]==".":
            # Matrice[y+1][x]="0"
            # print("Modification10")
         Mouvement ="G"
         x=x-1
      elif Next_Position == "F" :
         # if Matrice[y-1][x]==".":
            # Matrice[y-1][x]="1" 
            # print("Modification11")
         # if Matrice[y-1][x-1]==".":
            # Matrice[y-1][x-1]="1" 
            # print("Modification12")            
         # if Matrice[y][x-1]==".":
            # Matrice[y][x-1]="1" 
            # print("Modification13")            
         Mouvement ="B"
         y=y+1
      elif Next_Position == "L" :
         # if Matrice[y][x-1]==".":
            # Matrice[y][x-1]="0"
            # print("Modification14")            
         # if Matrice[y+1][x-1]==".":
            # Matrice[y+1][x-1]="0" 
            # print("Modification15")            
         # if Matrice[y+1][x]==".":
            # Matrice[y+1][x]="0" 
            # print("Modification16")             
         Mouvement ="H"
         y=y-1
   elif Mouvement == "B":
      if Next_Position == "|" :
         # if Matrice[y][x-1]==".":
            # Matrice[y][x-1]="1"
            # print("Modification17")
         # if Matrice[y][x+1]==".":
            # Matrice[y][x+1]="0"
            # print("Modification18")
         Mouvement ="B"
         y=y+1
      elif Next_Position == "L" :
         # if Matrice[y][x-1]==".":
            # Matrice[y][x-1]="1"
            # print("Modification19")
         # if Matrice[y+1][x-1]==".":
            # Matrice[y+1][x-1]="1"
            # print("Modification20")
         # if Matrice[y+1][x]==".":
            # Matrice[y+1][x]="1"
            # print("Modification21")
         Mouvement ="D"
         x=x+1
      elif Next_Position == "J" :
         # if Matrice[y][x+1]==".":
            # Matrice[y][x+1]="0"
            # print("Modification22")
         # if Matrice[y+1][x+1]==".":
            # Matrice[y+1][x+1]="0"
            # print("Modification23")
         # if Matrice[y+1][x]==".":
            # Matrice[y+1][x]="0"
            # print("Modification24")
         Mouvement ="G"
         x=x-1 
   elif Mouvement == "D":
      if Next_Position == "-" :
         # if Matrice[y-1][x]==".":
            # Matrice[y-1][x]="0"
            # print("Modification25")
         # if Matrice[y+1][x]==".":
            # Matrice[y+1][x]="1"
            # print("Modification26")
         Mouvement ="D"
         x=x+1
      elif Next_Position == "J" :
         # if Matrice[y+1][x]==".":
            # Matrice[y+1][x]="1" 
            # print("Modification27")
         # if Matrice[y+1][x+1]==".":
            # Matrice[y+1][x+1]="1"  
            # print("Modification28")
         # if Matrice[y][x+1]==".":
            # Matrice[y][x+1]="1"   
            # print("Modification29")
         Mouvement ="H"
         y=y-1
      elif Next_Position == "7" :
         # if Matrice[y-1][x]==".":
            # Matrice[y-1][x]="0" 
            # print("Modification30")
         # if Matrice[y-1][x+1]==".":
            # Matrice[y-1][x+1]="0"  
            # print("Modification31")
         # if Matrice[y][x+1]==".":
            # Matrice[y][x+1]="0"  
            # print("Modification32")
         Mouvement ="B"
         y=y+1
   Next_Position=Matrice[y][x]          
   Distance=Distance+1
   if Next_Position == "S" or Next_Position == "C":
      Arrive = True
      Matrice[y][x]="J"
print("_____________________________")
print((Distance)/2)
     


In = 0
Out = 0 
Previous =""
print("_____________________________")

for j in range(len(Matrice)):
   Tiles = -1
   for k in range(len(Matrice[0])):
      print(Matrice[j][k],Matrice_temp[j][k], Tiles)
      if Matrice_temp[j][k]=="C":
         if Matrice[j][k]=="|":
            Tiles = Tiles*(-1)
         elif Matrice[j][k]=="F":
            Previous="F"
            Tiles = Tiles*(-1)
         elif Matrice[j][k]=="J":
            if Previous=="L":
               Tiles = Tiles*(-1)           
         elif Matrice[j][k]=="7":
            if Previous=="F":
               Tiles = Tiles*(-1)              
         elif Matrice[j][k]=="L":
            Previous="L"
            Tiles = Tiles*(-1)  
      else :
         if Tiles ==(-1) :
            Out= Out +1;
            print(j,k,"Out ",Out)
            Matrice_temp[j][k]="0"
         elif Tiles ==(1) :
            In = In + 1
            Matrice_temp[j][k]="1"
            print(j,k,"In ",In, " -------------------------------------")

print("_____________________________")
print("Out ",Out)
print("In ",In)

Fichier_Temporaire = open("input_tmp.txt", "x")

for j in range(len(Matrice)):
   Fichier_Ligne=""
   for k in range(len(Matrice[0])):
      Fichier_Ligne=Fichier_Ligne+Matrice_temp[j][k]
   Fichier_Temporaire.write(Fichier_Ligne+"\n")