# -*- coding: iso-8859-1 -*-
import os
import csv

#settings
extension = 'pdf'                                                   #adjust if an other file
correction = 'Korrektur'
duty = 'Abgabe_01'                                                  #adjust
path = 'C:/Users/user/test_path/'                                   #adjust Care: Windows replace '\' to '/' or use the r 
os.chdir(path)                                                      #other opportunity: os.chdir(r'C:\Users\user\test_path')

#rename files
student_name = []
for pdf in os.listdir('.'):
        name, rest = pdf.split('_',1)                               #seperate name e.g. max mustermann_112_homework1_group1.pdf
        new_name = f'{correction}_{duty}_{name}.{extension}'        #create the new name of the document or file
        student_name.append(name)                                   #save the names in an array
        os.rename(pdf,new_name)                                     #rename the files or documents

#save names in csv
name_csv = f'{correction}_{duty}.csv'
with open(name_csv, 'w', newline='') as csvfile:
    
    fieldnames = ['Studierende']
    thewriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
    thewriter.writeheader()

    for student in student_name:
        thewriter.writerow({'Studierende':student})