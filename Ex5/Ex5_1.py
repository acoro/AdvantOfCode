import os

print("Advent Of Code 2023 - Exercice 5_1")

Fichier_Input = open("input.txt", 'r')

Lecture_Boucle = True
Lecture = False
Lecture_Seeds = True
Lecture_Seeds2Soil = False
Lecture_Soil2Fertilizer = False
Lecture_Fertilizer2Water = False
Lecture_Water2Light = False
Lecture_Light2Temp = False
Lecture_Temp2Humidity = False
Lecture_Humidity2Location = False
Fichier_Ligne = ""
Liste_Seeds2Location=[]


while Lecture_Boucle:
    Fichier_Ligne = Fichier_Input.readline()
    #print(Fichier_Ligne)
    if Fichier_Ligne :
       Fichier_Ligne = Fichier_Ligne.replace("\n","");
       if Lecture_Seeds == True:
          Liste_Seeds2Location=(Fichier_Ligne.split(":"))[1].split(" ")
          Liste_Seeds2Location.pop(0)
          Liste_Seeds_Status=[0]*(len(Liste_Seeds2Location))
          Lecture_Seeds = False
       if Lecture==True:
          Liste_data=Fichier_Ligne.split(" ")
          if Liste_data[0].isdigit():
             Destination,Source,Range=Liste_data
             for i in range(len(Liste_Seeds2Location)):
                if (int(Liste_Seeds2Location[i])>=int(Source)) and (int(Liste_Seeds2Location[i])<(int(Source)+int(Range))):
                   if Liste_Seeds_Status[i]==0: 
                     Liste_Seeds2Location[i]=(int(Destination)-int(Source)+int(Liste_Seeds2Location[i]))
                     Liste_Seeds_Status[i]=1         
          else:
             Lecture=False
             Liste_Seeds_Status=[0]*(len(Liste_Seeds2Location))             
       if Fichier_Ligne.find("-to-")!=(-1):
          Lecture=True          
    else:
       Lecture=False
       Lecture_Boucle = False
 
print("_____________________________")
print("Le minimum est :",min(Liste_Seeds2Location))
