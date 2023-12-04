import os

print("Advent Of Code 2023 - Exercice 3_1")

Fichier_Input = open("input.txt", 'r')

Lecture_Boucle_1 = True
Lecture_Boucle_2 = True
Modification = True
Fichier_Caractere = ""
Liste_Caractere=[]
Caractere_Speciaux=["-","*","&","#","+","$","=","%","@","/"]
Somme_Nombre=0
Somme_Total=0
Nombre=0

while Lecture_Boucle_1:
   Fichier_Caractere = Fichier_Input.read(1)
   if Fichier_Caractere != "\n" and Fichier_Caractere != "":
       if Fichier_Caractere in Caractere_Speciaux:
          Fichier_Caractere="*"
       Liste_Caractere.append(Fichier_Caractere)
   if not Fichier_Caractere:
       Lecture_Boucle_1 = False
   
Taille = len(Liste_Caractere)**0.5

for i in range(len(Liste_Caractere)):
   if not Liste_Caractere[i].isdigit():
      Somme_Total = Somme_Total + Nombre
      Nombre = 0
   else :
      Nombre=Nombre*10+int(Liste_Caractere[i])
      
if Nombre !=0:
   Somme_Total = Somme_Total + Nombre
   Nombre = 0

while Lecture_Boucle_2:
   for i in range(len(Liste_Caractere)):
      if Liste_Caractere[i] =="*":
         if ((i+1)%int(Taille))!= 1:
            if Liste_Caractere[i-1] != ".":
               if Liste_Caractere[i-1] != "*":
                  Liste_Caractere[i-1]="*"
                  Modification = True
         if ((i+1)%int(Taille))!= 0 :
            if Liste_Caractere[i+1] != ".":
               if Liste_Caractere[i+1] != "*":
                  Liste_Caractere[i+1]="*"
                  Modification = True
         if (i+1)%int(Taille)!=1:
            if i>=Taille :
               if Liste_Caractere[i-1-int(Taille)] != ".":
                  if Liste_Caractere[i-1-int(Taille)] != "*":
                     Liste_Caractere[i-1-int(Taille)]="*"
                     Modification = True
         if i>=Taille :
            if Liste_Caractere[i-int(Taille)] != ".":
               if Liste_Caractere[i-int(Taille)] != "*":
                  Liste_Caractere[i-int(Taille)]="*"
                  Modification = True              
         if (i+1)%int(Taille)!=0 :
            if i>=Taille :
               if Liste_Caractere[i+1-int(Taille)] != ".":
                  if Liste_Caractere[i+1-int(Taille)] != "*":
                     Liste_Caractere[i+1-int(Taille)]="*"
                     Modification = True
         if (i+1)%int(Taille)!=1 :
            if i<(Taille*(Taille-1)) :
               if Liste_Caractere[i-1+int(Taille)] != ".":
                  if Liste_Caractere[i-1+int(Taille)] != "*":
                     Liste_Caractere[i-1+int(Taille)]="*"
                     Modification = True
         if i<(Taille*(Taille-1)) :
            if Liste_Caractere[i+int(Taille)] != ".":
               if Liste_Caractere[i+int(Taille)] != "*":
                  Liste_Caractere[i+int(Taille)]="*"
                  Modification = True             
         if (i+1)%int(Taille)!=0 :
            if i<(Taille*(Taille-1)) :
               if Liste_Caractere[i+1+int(Taille)] != ".":
                  if Liste_Caractere[i+1+int(Taille)] != "*":
                     Liste_Caractere[i+1+int(Taille)]="*"
                     Modification = True                  
   if Modification == True:
      Modification = False
   else :
      Lecture_Boucle_2=False

for i in range(len(Liste_Caractere)):
   if not Liste_Caractere[i].isdigit():
      Somme_Nombre = Somme_Nombre + Nombre
      Nombre = 0
   else :
      Nombre=Nombre*10+int(Liste_Caractere[i])
if Nombre !=0:
   Somme_Nombre = Somme_Nombre + Nombre

print("_____________________________")
print("Le nombre Total est :", Somme_Total - Somme_Nombre)