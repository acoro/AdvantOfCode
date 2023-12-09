import os

print("Advent Of Code 2023 - Exercice 7_2")

Fichier_Input = open("input.txt", 'r')

Lecture_Boucle = True
Fichier_Ligne = ""
Cartes_Tampon = ""
Liste_Cartes_Gains=[]
Liste_Quinte=[]
Liste_Carre=[]
isCarre = False
Liste_Full=[]
Liste_Brelan=[]
isBrelan = False
Liste_Deux_Paires=[]
Liste_Paire=[]
Liste_Haute_Carte=[]
# A-> A, K -> B, Q->C, J-> X, T -> E, 9->F 8->G 7->H 6->I 5->L 4->M 3->N 2->O )
Dico_Brelan=["AAA","BBB","CCC","XXX","EEE","FFF","GGG","HHH","III","LLL","MMM","NNN","OOO"]
Dico_Carre=["AAAA","BBBB","CCCC","XXXX","EEEE","FFFF","GGGG","HHHH","IIII","LLLL","MMMM","NNNN","OOOO"]
Gains=0
Indice=1

while Lecture_Boucle:
    print("_____________________________")
    Cartes_Tampon=""
    isBrelan = False
    isCarre = False
    Fichier_Ligne = Fichier_Input.readline()
    Fichier_Ligne = Fichier_Ligne.replace("\n","")
    if Fichier_Ligne :
       Liste_Cartes,Gain=(Fichier_Ligne.split(" "))
       Liste_Cartes = Liste_Cartes.replace("K","B")
       Liste_Cartes = Liste_Cartes.replace("Q","C")
       Liste_Cartes = Liste_Cartes.replace("J","X")
       Liste_Cartes = Liste_Cartes.replace("T","E")
       Liste_Cartes = Liste_Cartes.replace("9","F")
       Liste_Cartes = Liste_Cartes.replace("8","G")
       Liste_Cartes = Liste_Cartes.replace("7","H")
       Liste_Cartes = Liste_Cartes.replace("6","I")
       Liste_Cartes = Liste_Cartes.replace("5","L")
       Liste_Cartes = Liste_Cartes.replace("4","M")
       Liste_Cartes = Liste_Cartes.replace("3","N")
       Liste_Cartes = Liste_Cartes.replace("2","O")
       Cartes=list(Liste_Cartes)
       Cartes.sort()
       for i in range(len(Cartes)):
          Cartes_Tampon=Cartes_Tampon+Cartes[i]
       print(Liste_Cartes, Gain)
       print(Cartes, Cartes_Tampon)
       SetCartes=set(Cartes)
       Taille=len(SetCartes)
       print(SetCartes,Taille)
       if (Taille == 5):
          if Cartes_Tampon.find("X")!=(-1):
             Liste_Paire.append([Liste_Cartes,int(Gain)])         
          else :
             Liste_Haute_Carte.append([Liste_Cartes,int(Gain)])
       if (Taille == 4):
          if Cartes_Tampon.find("X")!=(-1):
             Liste_Brelan.append([Liste_Cartes,int(Gain)])          
          else :          
             Liste_Paire.append([Liste_Cartes,int(Gain)])
       if (Taille == 3):
          for i in range(len(Dico_Brelan)):
             if Cartes_Tampon.find(Dico_Brelan[i])!=(-1):
               isBrelan = True
               break       
          if isBrelan == True :
             if Cartes_Tampon.find("X")!=(-1): 
               Liste_Carre.append([Liste_Cartes,int(Gain)])
             else :             
               Liste_Brelan.append([Liste_Cartes,int(Gain)])
          else :
             if Cartes_Tampon.find("XX")!=(-1):
                Liste_Carre.append([Liste_Cartes,int(Gain)])
             else :
                if Cartes_Tampon.find("X")!=(-1):
                   Liste_Full.append([Liste_Cartes,int(Gain)])
                else:
                   Liste_Deux_Paires.append([Liste_Cartes,int(Gain)])
       if (Taille == 2):
          if Cartes_Tampon.find("X")!=(-1):
             Liste_Quinte.append([Liste_Cartes,int(Gain)])
          else:
             for i in range(len(Dico_Carre)):
                if Cartes_Tampon.find(Dico_Carre[i])!=(-1):
                  isCarre = True
                  break     
             if isCarre == True :       
               Liste_Carre.append([Liste_Cartes,int(Gain)])
             else :
               Liste_Full.append([Liste_Cartes,int(Gain)])
       if (Taille == 1):      
          Liste_Quinte.append([Liste_Cartes,int(Gain)])

       print(Liste_Cartes_Gains)
    if not Fichier_Ligne:
       Lecture_Boucle = False


   
print("_____________________________")
Liste_Haute_Carte.sort()
for i in reversed (range(len(Liste_Haute_Carte))):
   Gains=Gains+(Indice)*(Liste_Haute_Carte[i][1])
   Indice=Indice+1
   print(Gains)
print("Haute_Carte ", Liste_Haute_Carte)
print("_____________________________")
Liste_Paire.sort();
for i in reversed (range(len(Liste_Paire))):
   Gains=Gains+(Indice)*(Liste_Paire[i][1])
   Indice=Indice+1
   print(Gains)
print("Liste_Paire ", Liste_Paire)
print("_____________________________")
Liste_Deux_Paires.sort()
for i in reversed (range(len(Liste_Deux_Paires))):
   Gains=Gains+(Indice)*(Liste_Deux_Paires[i][1])
   Indice=Indice+1
   print(Gains)
print("Liste_Deux_Paires ", Liste_Deux_Paires)
print("_____________________________")
Liste_Brelan.sort()
for i in reversed (range(len(Liste_Brelan))):
   Gains=Gains+(Indice)*(Liste_Brelan[i][1])
   Indice=Indice+1
   print(Gains)
print("Liste_Brelan ", Liste_Brelan)
print("_____________________________")
Liste_Full.sort()
for i in reversed (range(len(Liste_Full))):
   Gains=Gains+(Indice)*(Liste_Full[i][1])
   Indice=Indice+1
   print(Gains)
print("Liste_Full ", Liste_Full)
print("_____________________________")
Liste_Carre.sort()
for i in reversed (range(len(Liste_Carre))):
   Gains=Gains+(Indice)*(Liste_Carre[i][1])
   Indice=Indice+1
   print(Gains)
print("Liste_Carre ", Liste_Carre)
print("_____________________________")
Liste_Quinte.sort()
for i in reversed (range(len(Liste_Quinte))):
   Gains=Gains+(Indice)*(Liste_Quinte[i][1])
   Indice=Indice+1
   print(Gains)
print("Liste_Quinte ", Liste_Quinte)
print("_____________________________")
print("Le Total est ", Gains)





      