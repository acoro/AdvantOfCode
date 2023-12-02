import os

print("Advent Of Code 2023 - Exercice 2_2")

Fichier_Input = open("input.txt", 'r')

Lecture_Boucle = True
Fichier_Ligne = ""
Somme_Game=0
Nombre_Red=0
Nombre_Green=0
Nombre_Blue=0
Somme_Power=0;

while Lecture_Boucle:
    Fichier_Ligne = Fichier_Input.readline()
    Fichier_Ligne = Fichier_Ligne.replace("\n","");
    if Fichier_Ligne :
       Depassement=False
       Game_Ligne_Liste=(Fichier_Ligne.split(":"))
       Game_Cube_Numero=Game_Ligne_Liste[0].split(" ")
       Game_Cube_Liste=((Game_Ligne_Liste[1]).split(";"))
       print(Game_Cube_Numero[1],Game_Cube_Liste)
       for i in Game_Cube_Liste :
           Game_Cube_Set_Liste=(i.split(","))
           for j in Game_Cube_Set_Liste :
               Game_Cube_Color_Set_Liste=(j.split(" "))
               if((Game_Cube_Color_Set_Liste[2]=="red") and (Nombre_Red < int(Game_Cube_Color_Set_Liste[1]))):
                   Nombre_Red=int(Game_Cube_Color_Set_Liste[1])
               if((Game_Cube_Color_Set_Liste[2]=="green") and (Nombre_Green < int(Game_Cube_Color_Set_Liste[1]))):
                   Nombre_Green=int(Game_Cube_Color_Set_Liste[1])
               if((Game_Cube_Color_Set_Liste[2]=="blue") and (Nombre_Blue < int(Game_Cube_Color_Set_Liste[1]))):
                   Nombre_Blue=int(Game_Cube_Color_Set_Liste[1])
       Somme_Power=Somme_Power+(Nombre_Red*Nombre_Green*Nombre_Blue)
       print("Nombre Min Red",Nombre_Red)
       print("Nombre Min Green",Nombre_Green)
       print("Nombre Min Blue",Nombre_Blue)
       print("Somme_Power",Somme_Power)
       Nombre_Red=0
       Nombre_Green=0
       Nombre_Blue=0
       print("_____________________________")
    if not Fichier_Ligne:
       Lecture_Boucle = False
print("_____________________________")
print("La somme total des POWER est ",Somme_Power)
