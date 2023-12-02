import os

print("Advent Of Code 2023 - Exercice 2_1")

Fichier_Input = open("input.txt", 'r')

Lecture_Boucle = True
Fichier_Ligne = ""
Somme_Game=0

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
               if((Game_Cube_Color_Set_Liste[2]=="red") and (int(Game_Cube_Color_Set_Liste[1])>12)) :
                   print("Dépassement red")
                   Depassement=True
               if((Game_Cube_Color_Set_Liste[2]=="green") and (int(Game_Cube_Color_Set_Liste[1])>13)) :
                   print("Dépassement green")
                   Depassement=True
               if((Game_Cube_Color_Set_Liste[2]=="blue") and (int(Game_Cube_Color_Set_Liste[1])>14)) :
                   print("Dépassement blue")
                   Depassement=True
       if Depassement==False :
           Somme_Game=Somme_Game+int(Game_Cube_Numero[1])
           print("Somme_Game ", Somme_Game)
       print("_____________________________")
    if not Fichier_Ligne:
       Lecture_Boucle = False
print("_____________________________")
print("La somme total des GAME est",Somme_Game)
