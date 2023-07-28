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

# only puts the three columns we need into selected df
# need to make a function for later code (unknown spread sheets ect) 
# defines the new dataframe 
selected_df = excel_df[['First name', 'Last name', 'UNumber']] #python is case sensative 
#print(selected_df)

# renaming process 
old_file_name = files_in_folder[0]
#print(f"old file name is: {old_file_name}")
new_file_name = 'Whiskers, Cat UNumber.pdf'
#print(f"new file name is{new_file_name}")

# below function concatenates the file name to the file path, might be where we are having issues
'''

old_file_path = os.path.join('Files', old_file_name)
#print( f"old file path is {old_file_path}")

#new_file_path = os.path.join('Renamed Files', new_file_name)

new_file_path = os.path.join(os.path.dirname(old_file_path), new_file_name)
#print(f"new file path is {new_file_path}")

# worked when using old_file_path rather than the name, 
# when defining the old_file_path, we concatanated the file we wanted and where it was located, see print statement ~ line 40 
if os.path.exists(old_file_path) and os.path.isfile(old_file_path):
    # Rename the file
    # when renaming the file, you put the path to the old file (with name) and path to new file (with name)
    # NOT using text file names
    os.rename(old_file_path, new_file_path)
    print("File renamed successfully.")
else:
    print("Original file not found or not accessible.")

# renames the file that was assigned to old_file_name to the text that was assigned as new file name
#os.rename(old_file_path, new_file_path)

'''

#print(files_in_folder)
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

cleaned_names_df = pd.DataFrame(cleaned_file_names)

# adds original file name to compare (will be useful later when 
# comparing to make sure correct file was renamed)
cleaned_names_df['File Name'] = files_in_folder
#print("\n", cleaned_names_df)

# now that we have the file names 'searchable'
# lets work on the part that compares to excel df so we can find the unumber and rename the file
# using the match function 

# note: selected_df is the excel df 
#       cleaned_names_df is the file names we need to match with the excel names
# if there is a match, we rename the file based on 'last, first unumber'
# if there isnt a match, the file gets moved to a filder named "to rename", or something like that

# shuffle the excel dataframe:
selected_df2 = selected_df.sample(frac=1)
#print("\n ", selected_df2)

# .isin() function checks if the first part (before the .) is in the second df, returns a boolian 
#matches = cleaned_names_df['Last name'].isin(selected_df['Last name'])
#matching_rows_df = cleaned_names_df[matches]
#print(matching_rows_df) # gives result of the matches (what matched between the two df)
#print("\n",matches) # gives true false statement for the files the matched 

# Merge df2 with df1 based on first_name and last_name
merged_df = cleaned_names_df.merge(selected_df2, on=['First name', 'Last name'], how='inner')

# Drop the duplicate first_name and last_name column from df2
merged_df.drop(['First name', 'Last name'], axis=1, inplace=True)

# Rename the columns for clarity (optional)
merged_df.rename(columns={'first_name_x': 'First name', 'last_name_x': 'Last name'}, inplace=True)

# Output the final merged dataframe with unumber added to df2
print(merged_df)