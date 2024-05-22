# -*- coding: iso-8859-1 -*-
import os
import csv

#settings
extension = 'pdf'                                                                       # adjust if an other file
correction = 'correction'
submission = 'submission_01'                                                            # adjust
path = 'C:/Users/user/test_path/'                                                       # adjust Care: Windows replace '\' to '/' or use the r 
os.chdir(path)                                                                          # other opportunity: os.chdir(r'C:\Users\user\test_path')

#rename files
student_name = [['Studentys']]                                                          # column heading
for pdf in os.listdir('.'):
        name, rest = pdf.split('_',1)                                                   # seperate name e.g. max mustermann_112_homework1_group1.pdf
        new_name = f'{correction}_{submission}_{name.replace(' ','_')}.{extension}'     # create the new name of the document or file and change space to _ (max_mustermann)
        student_name.append([name])                                                     # save the names in an array
        os.rename(pdf,new_name)                                                         # rename the files or documents

#save names in csv
name_csv = f'{correction}_{submission}.csv'
with open(name_csv, 'w', newline='', encoding='utf-8-sig') as csvfile:                  # encoding='utf-8-sig' for better view in excel
    thewriter = csv.writer(csvfile, dialect='excel')
    thewriter.writerows(student_name)
