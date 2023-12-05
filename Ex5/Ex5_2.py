import os

print("Advent Of Code 2023 - Exercice 5_2")

Fichier_Input = open("input.txt", 'r')

Lecture_Boucle = True
Lecture = False
Lecture_Seeds = True
Fichier_Ligne = ""
Liste_Seeds2Location_Interval=[]
Liste_Seeds2Location=[]

while Lecture_Boucle:
    Fichier_Ligne = Fichier_Input.readline()
    if Fichier_Ligne :
       Fichier_Ligne = Fichier_Ligne.replace("\n","");
       if Lecture_Seeds == True:
          Liste_Seeds2Location_Interval=(Fichier_Ligne.split(":"))[1].split(" ")
          Liste_Seeds2Location_Interval.pop(0)
          for i in range(len(Liste_Seeds2Location_Interval)):
             print(Liste_Seeds2Location_Interval[i])
             if (i%2)==0:
                Source_Interval=int(Liste_Seeds2Location_Interval[i])
                Destination_Interval=0
             else:
                Destination_Interval=int(Liste_Seeds2Location_Interval[i])+Source_Interval-1
             for i in range(Source_Interval,Destination_Interval):
                Liste_Seeds2Location.append(i)
                #print("Trop long !!!!!")                
          Liste_Seeds_Status=[0]*(len(Liste_Seeds2Location))
          Lecture_Seeds = False
       if Lecture==True:
          Liste_data=Fichier_Ligne.split(" ")
          if Liste_data[0].isdigit():
             Destination,Source,Range=Liste_data
             for i in range(len(Liste_Seeds2Location)):
                if Liste_Seeds_Status[i]==0: 
                   if (int(Liste_Seeds2Location[i])>=int(Source)) and (int(Liste_Seeds2Location[i])<(int(Source)+int(Range))):   
                     Liste_Seeds2Location[i]=(int(Destination)-int(Source)+int(Liste_Seeds2Location[i]))
                     Liste_Seeds_Status[i]=1         
          else:
             Lecture=False
             Liste_Seeds_Status=[0]*(len(Liste_Seeds2Location))             
       if Fichier_Ligne.find("-to-")!=(-1):
          print(Fichier_Ligne)
          Lecture=True          
    else:
       Lecture=False
       Lecture_Boucle = False
 
print("_____________________________")
print("Le minimum est :",min(Liste_Seeds2Location))
