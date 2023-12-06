import os

print("Advent Of Code 2023 - Exercice 5_2")

Fichier_Input = open("input.txt", 'r')

Lecture_Boucle = True
Lecture = False
Lecture_Seeds = True
Fichier_Ligne = ""
Liste_Seeds2Location_Interval=[]
Liste_Seeds2Location=[]
Liste_Seeds_Status=[]
Break =0

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
                Liste_Seeds2Location.append([Source_Interval,Destination_Interval])
                Liste_Seeds_Status.append([0,0])
          print(Liste_Seeds2Location)                        
          print(Liste_Seeds_Status)
          Lecture_Seeds = False
       if Lecture==True:
          Liste_data=Fichier_Ligne.split(" ")
          if Liste_data[0].isdigit():
             print(Liste_data)
             Destination,Source,Range=Liste_data
             for i in range(len(Liste_Seeds2Location)):
                #print("____________________________")
                print(i)
                Source_Debut = int(Liste_Seeds2Location[i] [0])
                Source_Fin = int(Liste_Seeds2Location[i] [1])
                #print(Source_Debut,Source_Fin)
                #print(Source,Range,Destination)
                #print(Liste_Seeds2Location)
                #print(Liste_Seeds_Status)
                if int(Liste_Seeds_Status[i][0])==0:
                   if (Source_Debut>=int(Source)) and (Source_Debut)<(int(Source)+int(Range)):   
                      Liste_Seeds2Location[i][0]=(int(Destination)-int(Source)+int(Liste_Seeds2Location[i][0]))
                      Liste_Seeds_Status[i][0]=1
                      #print(Liste_Seeds2Location) 
                      #print(Liste_Seeds_Status)
                   if (Source_Debut<int(Source)) and (Source_Fin)>=(int(Source)):   
                      Liste_Seeds2Location[i][0]=int(Destination)
                      Liste_Seeds_Status[i][0]=1
                      Liste_Seeds2Location.append([Source_Debut,(int(Source)-1)])
                      Liste_Seeds_Status.append([0,0])
                      #print(Liste_Seeds2Location) 
                      #print(Liste_Seeds_Status)
                if int(Liste_Seeds_Status[i][1])==0:
                   if (Source_Fin>=int(Source)) and (Source_Fin)<(int(Source)+int(Range)):   
                      Liste_Seeds2Location[i][1]=(int(Destination)-int(Source)+int(Liste_Seeds2Location[i][1]))
                      Liste_Seeds_Status[i][1]=1
                      #print(Liste_Seeds2Location) 
                      #print(Liste_Seeds_Status)
                   if (Source_Debut<(int(Source)+int(Range))) and ((Source_Fin)>=(int(Source)+int(Range))):   
                      Liste_Seeds2Location[i][1]=(int(Source)+int(Range)-1)
                      Liste_Seeds_Status[i][1]=1
                      Liste_Seeds2Location.append([(2*(int(Source_Debut))-int(Source)),(int(Source_Fin))])
                      Liste_Seeds_Status.append([0,0])
                      #print(Liste_Seeds2Location) 
                      #print(Liste_Seeds_Status)               
          else:
             Lecture=False
             taille = len(Liste_Seeds_Status)
             Liste_Seeds_Status.clear();
             for i in range(taille):
                Liste_Seeds_Status.append([0,0])
             #print(Liste_Seeds_Status)              
       if Fichier_Ligne.find("-to-")!=(-1):
          print("_____________________________")
          print(Fichier_Ligne)
          Lecture=True
          #Break = Break +1
          if Break ==2:
             print(Liste_Seeds2Location) 
             print(Liste_Seeds_Status)           
             Lecture_Boucle = False
    else:
       Lecture=False
       Lecture_Boucle = False
 
print("_____________________________")

minimum=Liste_Seeds2Location[0][0]
for i in range(len(Liste_Seeds2Location)):
   if minimum >=(int(Liste_Seeds2Location[i][0])):
      minimum=int(Liste_Seeds2Location[i][0])
      print(minimum)
   
print("Le minimum est :",minimum)
