import os

print("Advent Of Code 2023 - Exercice 5_2")

Fichier_Input = open("input.txt", 'r')
Fichier_Output = open("input_temporaire.txt", 'x')

Lecture_Boucle = True
Fichier_Ligne = ""
Data=[]
Liste_Seeds2Location_Interval=[]
Liste_Seeds2Location=[]

while Lecture_Boucle:
    Fichier_Ligne = Fichier_Input.readline()
    if Fichier_Ligne :
       Data.append(Fichier_Ligne)
    else:
       Lecture_Boucle = False   

for i in reversed (range(len(Data))):
   if i != 0:
       Fichier_Output.writelines(Data[i])
Liste_Seeds2Location_Interval=(Data[0].split(":"))[1].split(" ")
Liste_Seeds2Location_Interval.pop(0)

for i in (range(len(Liste_Seeds2Location_Interval))):
   Liste_Seeds2Location_Interval[i]=int(Liste_Seeds2Location_Interval[i])
   
Max=max(Liste_Seeds2Location_Interval)

for i in range(len(Liste_Seeds2Location_Interval)):
   print(Liste_Seeds2Location_Interval[i])
   if (i%2)==0:
      Source_Interval=int(Liste_Seeds2Location_Interval[i])
      Destination_Interval=0
   else:
      Destination_Interval=int(Liste_Seeds2Location_Interval[i])+Source_Interval-1
      Liste_Seeds2Location.append([Source_Interval,Destination_Interval])

print(Liste_Seeds2Location)
print(Max)
print("_____________________________")
Location_Trouve=False

for i in range(Max):
   if Location_Trouve==True:
      break
   print("_____________________________")
   print(i)
   Location2Seed=i
   Liste_Seeds_Status=0 
   Lecture_Boucle = True
   Fichier_Output.close()
   Fichier_Output = open("input_temporaire.txt", 'r')
   while Lecture_Boucle:
      Fichier_Ligne = Fichier_Output.readline()
      if Fichier_Ligne :
         Fichier_Ligne = Fichier_Ligne.replace("\n","");
         Liste_data=Fichier_Ligne.split(" ")
         if Liste_data[0].isdigit():
            Source,Destination,Range=Liste_data
            if (int(Location2Seed)>=int(Source)) and (int(Location2Seed)<(int(Source)+int(Range))):
               if Liste_Seeds_Status==0: 
                  Location2Seed=(int(Destination)-int(Source)+int(Location2Seed))
                  Liste_Seeds_Status=1
                  #print(Location2Seed)                    
         else:
            Liste_Seeds_Status=0     
      else:
         Lecture=False
         Lecture_Boucle = False
   for j in range(len(Liste_Seeds2Location)):
      Source_Debut = int(Liste_Seeds2Location[j] [0])
      Source_Fin = int(Liste_Seeds2Location[j] [1])
      if (Location2Seed >=Source_Debut) and (Location2Seed <= Source_Fin):
         print (Location2Seed, i)
         Location_Min=i
         Location_Trouve=True
         break

Fichier_Output.close() 
os.remove("input_temporaire.txt")

print("_____________________________")
print("Le minimum est :",Location_Min) 

