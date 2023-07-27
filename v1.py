# renaming files 
# import libraries
import pandas as pd
import os
import re

# create dataframe from excel sheet
excel_df = pd.read_excel('Test.xlsx')

folder_name = 'Files'
# below function is used to get the absolute path to a folder (defines the path)
folder_path = os.path.abspath(folder_name)
# files_in_folder is the list of files in the folder 
files_in_folder = os.listdir(folder_name)

#print('\n' .join(files_in_folder)) # prints files vertically, not necessary tho

selected_df = excel_df[['First name', 'Last name', 'UNumber']] #python is case sensative 
#print(selected_df)

# create the function to identify parts to remove from file name 
# need to remove the gibberish (pleonasm) 
# since this will also rename the file, maybe we 'remove' the gibberish, 
# then search based on the first string found within the first column, 
# then if we cannot find it, have it search the second column using the first string
# then repeat the above steps but with the second string, and if there is no second string 
# then ingore/move the file to the 'Need to be renamed' folder or something?

print(files_in_folder[1])

file_name = files_in_folder[1]
pattern = r' - (.+)\.pdf'

match = re.search(pattern, file_name) 

if match:
    names_text = match.group(1)

    names = names_text.split()

    name1 = names[0]
    name2 = names[1]

    print("Name 1:", name1)
    print("Name 2:", name2)

else:
    print("No names found")