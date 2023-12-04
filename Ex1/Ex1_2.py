import os

print("Advent Of Code 2023 - Exercice 1_2")

Fichier_Input = open("input.txt", 'r')
Fichier_Temporaire = open("input_tmp.txt", "x")

Lecture_Boucle_1 = True
Lecture_Boucle_2 = True
Fichier_Ligne = ""
Fichier_Caractere = 0
Premier_Digit = 0
Dernier_Digit = 0
Premier_Digit_OK = False
Somme_Flocons = 0

while Lecture_Boucle_1:
    Fichier_Caractere = Fichier_Input.read(1)
    if Fichier_Caractere != "\n":
       Fichier_Ligne = Fichier_Ligne + Fichier_Caractere
       Fichier_Ligne = Fichier_Ligne.replace("one","o1e")
       Fichier_Ligne = Fichier_Ligne.replace("two","t2o")
       Fichier_Ligne = Fichier_Ligne.replace("three","t3e")
       Fichier_Ligne = Fichier_Ligne.replace("four","f4r")
       Fichier_Ligne = Fichier_Ligne.replace("five","f5e")
       Fichier_Ligne = Fichier_Ligne.replace("six","s6x")
       Fichier_Ligne = Fichier_Ligne.replace("seven","s7n")
       Fichier_Ligne = Fichier_Ligne.replace("eight","e8t")
       Fichier_Ligne = Fichier_Ligne.replace("nine","n9e")
       print(Fichier_Ligne)   
    else :
       print("_______________________________")  
       Fichier_Temporaire.write(Fichier_Ligne+"\n")
       Fichier_Ligne = ""
    if not Fichier_Caractere:
       Lecture_Boucle_1 = False

Fichier_Temporaire.close()
Fichier_Temporaire = open("input_tmp.txt", "r")
    
while Lecture_Boucle_2:
    Fichier_Caractere = Fichier_Temporaire.read(1)
    if Fichier_Caractere != "\n":
       if Fichier_Caractere.isdigit():
          if Premier_Digit_OK == False:
             Premier_Digit = Fichier_Caractere
             Dernier_Digit = Fichier_Caractere
             Premier_Digit_OK = True
          else :
             Dernier_Digit = Fichier_Caractere            
    else :
       print("____________________________")
       Somme_Flocons = Somme_Flocons + int(Premier_Digit)*10 + int(Dernier_Digit)
       print(Premier_Digit,Dernier_Digit,Somme_Flocons)       
       Premier_Digit = 0
       Dernier_Digit = 0
       Premier_Digit_OK = False
    if not Fichier_Caractere:
       Lecture_Boucle_2 = False

Fichier_Temporaire.close()      
print("_____________________________")
print("Le nombre total de flocons est ",Somme_Flocons)
os.remove("input_tmp.txt")