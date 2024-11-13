# -*- coding: iso-8859-1 -*-
"""
Author: Breidenbach, Johannes
Date: 2021-10-26
Description: Rename pdf files and save the new names in csv file
"""
"""
Required packages:
-os
-csv
-pandas
-openpyxl
install with pip or conda
"""
import os
import csv
import pandas as pd

"""settings"""
save_csv = False                                                                        # adjust which file is requierd by saving names list
save_excel = True
extension = 'pdf'                                                                       # adjust if an other file is in folder
correction = 'submission_01'                                                            # adapt to use case
number = '01'                                                                           # adapt to use case
submission = 'Abgabe_' + number                                                         # adapt to use case
path = os.path.join('.', 'your', 'path')                                                # Adapt this to your folder structure
os.chdir(path)                                                                          # change the working directory, other opportunity: os.chdir(r'C:\Users\user\your\path')

"""rename files"""
list_files = os.listdir('.')                                                            # crate list of all files in directory
list_pdfs = [file for file in list_files if file.endswith('.pdf')]                      # write all pdf documents in a new list

student_name = [['Studentys']]
student_name_excel = []

for pdf in list_pdfs:
        name, rest = pdf.split('_',1)                                                   # seperate name e.g. max mustermann_112_homework1_group1.pdf
        new_name = f'{correction}_{submission}_{name.replace(' ','_')}.{extension}'     # create the new name of the document or file
        student_name.append([name])                                                     # save the names in a list
        student_name_excel.append([name])                                               # save the names in a list
        os.rename(pdf,new_name)                                                         # rename the files or documents

"""save names in csv"""
if save_csv:
        name_csv = f'{correction}_{submission}.csv'
        with open(name_csv, 'w', newline='', encoding='utf-8-sig') as csvfile:          # encoding='utf-8-sig' for better view in excel
                thewriter = csv.writer(csvfile, dialect='excel')
                thewriter.writerows(student_name)

"""save names in excel"""
if save_excel:
        name_excel = f'{correction}_{submission}.xlsx'
        df = pd.DataFrame(student_name_excel, columns=['Studentys'])
        df.to_excel(name_excel, index=False)
