import os

print("Advent Of Code 2023 - Exercice 8_2")

Fichier_Input = open("input.txt", 'r')

Lecture_Boucle = True
ZZZ_non_atteint = True
Lecture_Instructions = True
Liste_Instructions=[]
Fichier_Ligne = ""
Liste_Position = []
Liste_Depart = []
Liste_Reponse = []
Indice_Global=0
Indice=0
Tentative=0


while Lecture_Boucle:
    Fichier_Ligne = Fichier_Input.readline()
    if Fichier_Ligne :
       Fichier_Ligne = Fichier_Ligne.replace("\n","");
       Fichier_Ligne = Fichier_Ligne.replace(" ","");
       Fichier_Ligne = Fichier_Ligne.replace("(","");
       Fichier_Ligne = Fichier_Ligne.replace(")","");
       if Lecture_Instructions == True:
          Instructions=Fichier_Ligne
          print(Instructions)
          Lecture_Instructions = False
       if (Fichier_Ligne.find("=")!=(-1)):
          Position,Deplacement=Fichier_Ligne.split("=")
          Deplacement
          DeplacementL, DeplacementR=Deplacement.split(",")
          #print(Position)
          #print(DeplacementL,DeplacementR)
          Liste_Position.append([Position,DeplacementL,DeplacementR])
          
    else :
       Lecture_Boucle = False

print("_____________________________")
Liste_Instructions=list(Instructions)
#print(Liste_Instructions)
#print(Liste_Position)

for i in range(len(Liste_Position)):
   Position=list(Liste_Position[i][0])
   if (Position[2]).find("A")!=(-1):
      print(i,Position)
      Liste_Depart.append([i,Liste_Position[i][0]])

print("_____________________________")

for j in range(len(Liste_Depart)):
   print(j)
   ZZZ_non_atteint=True
   Tentative=0
   Indice_Global=0
   Nouvelle_Index=Liste_Depart[j][0]
   while ZZZ_non_atteint:
      Index_Courant=Nouvelle_Index
      #print(Nouvelle_Index,Liste_Position[Index_Courant][0],Liste_Position[Index_Courant][1],Liste_Position[Index_Courant][2],Liste_Instructions[Indice],Indice)
      if Liste_Instructions[Indice]=="L":
         Nouvelle_Position=Liste_Position[Index_Courant][1]
         #print("L  ", Nouvelle_Position)
      else :
         Nouvelle_Position=Liste_Position[Index_Courant][2]
         #print("R  ", Nouvelle_Position)
      for i in range(len(Liste_Position)):
         if (Liste_Position[i][0]).find(Nouvelle_Position)!=(-1):
            Nouvelle_Index=i
            break 
      Indice_Global=(Indice_Global+1)
      Indice=(Indice+1)%(len(Liste_Instructions))
      Position=list(Nouvelle_Position)
      if (Position[2]=="Z"):
         print(Liste_Depart[j][1], Nouvelle_Position,Nouvelle_Index,Indice_Global)
         Liste_Reponse.append(Indice_Global)
         print(j,Indice_Global,Liste_Reponse.count(Indice_Global),len(Liste_Depart))
         if (Liste_Reponse.count(Indice_Global))==(len(Liste_Depart)-3):
            print("Temp     ",j,Indice_Global,Liste_Reponse.count(Indice_Global),len(Liste_Depart))
         if (Liste_Reponse.count(Indice_Global))==(len(Liste_Depart)):
            print(j,Indice_Global,Liste_Reponse.count(Indice_Global),len(Liste_Depart))
            ZZZ_non_atteint=False   
         Tentative=Tentative+1
         if Tentative==10:
            ZZZ_non_atteint=False    
   print("_____________________________")
Liste_Reponse.sort()
print(Liste_Reponse)

Reponse=269

for i in range(len(Liste_Reponse)):
   Reponse=Reponse*int(Liste_Reponse[i])/269

print("_____________________________")
print(int(Reponse))









      