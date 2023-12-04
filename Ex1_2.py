from array import array

print("Advent Of Code 2022 - Exercice 1_2")

file = open("input.txt", 'r')

a = True
i=0
file_line=0
file_line_old=0
file_line_max_list=[]


while a:
    file_line = file.readline()
    if file_line != "\n":
       if file_line:
          file_line_old = file_line_old + int(file_line)
          print(file_line_old)
    if file_line=="\n":
       file_line_max_list.append(file_line_old)
       file_line_old=0
       i=i+1
       print("_____________________________")
       print("Elfe",i)
    if not file_line:
       a = False
    
print("_____________________________")
file_line_max_list.sort()
file_line_max_list.reverse()
print("Les 3 Elfes Max sont")
print(file_line_max_list[0])
print(file_line_max_list[1])
print(file_line_max_list[2])
print("SOMME =",file_line_max_list[0]+file_line_max_list[1]+file_line_max_list[2])