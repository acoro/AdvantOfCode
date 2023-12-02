print("Advent Of Code 2023 - Exercice 1_1")

Fichier = open("input.txt", 'r')

Lecture_Boucle = True
Fichier_Caractere = 0
Premier_Digit = 0
Dernier_Digit = 0
Premier_Digit_OK = False
Somme_Flocons = 0

while Lecture_Boucle:
    Fichier_Caractere = Fichier.read(1)
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
       Lecture_Boucle = False
       
print("_____________________________")
print("Le nombre total de flocons est ",Somme_Flocons)