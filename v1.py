# renaming files 
# import libraries
import pandas as pd
import os
#import re # library not used anymore

# create dataframe from excel sheet
excel_df = pd.read_excel('Test.xlsx')
#print(excel_df)

folder_name = 'Files'
# below function is used to get the absolute path to a folder (defines the path)
folder_path = os.path.abspath(folder_name)
# files_in_folder is the list of files in the folder 
files_in_folder = os.listdir(folder_name)

#print('\n' .join(files_in_folder)) # prints files vertically, not necessary tho

selected_df = excel_df[['First name', 'Last name', 'UNumber']] #python is case sensative 
#print(selected_df)

# create df to store the output of the named file 
cleaned_file_names = []

for file_name in files_in_folder:
    parts = file_name.split(' - ')

    if len(parts) == 2:
        names_text = parts[1].strip()
        names = names_text.split()

        if len(names) >= 1:
            # Check and split name2 from the last dot, if it exists
            name1 = names[0]
            name2 = names[1] if len(names) >= 2 else None

            if name1 and "." in name1:
                name1, _ = name1.rsplit(".", 1)

            if name2 and "." in name2:
                name2, _ = name2.rsplit(".", 1)

            entry = {"First name": name1, "Last name": name2}
            cleaned_file_names.append(entry)

        else:
            print("no after hyphen")
    else:
        print("No hyphen found")


cleaned_names_df = pd.DataFrame(cleaned_file_names)

# adds original file name to compare (will be useful later when 
# comparing to make sure correct file was renamed)
cleaned_names_df['File Name'] = files_in_folder
#print(cleaned_names_df)

# now that we have the file names 'searchable'
# lets work on the part that compares to excel df so we can find the unumber and rename the file
# using the match function 

# note: selected_df is the excel df 
#       cleaned_names_df is the file names we need to match with the excel names
# if there is a match, we rename the file based on 'last, first unumber'
# if there isnt a match, the file gets moved to a filder named "to rename", or something like that

# shuffle the excel dataframe:
selected_df = selected_df.sample(frac=1)
#print(selected_df)

# .isin() function checks if the first part (before the .) is in the second df, returns a boolian 
matches = cleaned_names_df['Last name'].isin(selected_df['Last name'])
matching_rows_df = cleaned_names_df[matches]
print(matching_rows_df)
print(matches)

# looping time 
# loop 1 - checks if first name matches, if yes then file can be renamed based on the match 