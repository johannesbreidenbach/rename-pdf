# -*- coding: iso-8859-1 -*-
import os
from os import getcwd, chdir, rename
import csv

#settings
correction = 'Korrektur'
path = 'C:/Users/user/test_path/' #Care: Windows replace '\' to '/' or use the r
os.chdir(path) #os.chdir(r'C:\Users\user\test_path')

#rename files
j = 0
for pdf in os.listdir('.'):
    if pdf.count('_') == 4:
        name, number, assign, file, filename = pdf.split('_')
        f_name, extension = filename.split('.')
        new_name = f'{correction}_{name}.{extension}'
        print(new_name)
        os.rename(pdf,new_name)
    elif pdf.count('_') == 5:
        name, number, assign, file, filename, end = pdf.split('_')
        f_name, extension = end.split('.')
        new_name = f'{correction}_{name}.{extension}'
        print(new_name)
        os.rename(pdf,new_name)
    else:
        print('Anzahl an _ stimmen nicht.')
    j += 1


#save names in csv
arr=[]
arr = [0 for i in range(j)]
k = 0
for pdf in os.listdir('.'):
    arr[k] = pdf
    k += 1

with open('Korrektur_Abgabe_1.csv', 'w', newline='') as csvfile:
    
    fieldnames = ['Studierende']
    thewriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
    thewriter.writeheader()

    for student in arr:
        thewriter.writerow({'Studierende':student})