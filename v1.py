# renaming files 
# import libraries
import pandas as pd
import os

# create dataframe from excel sheet
excel_df = pd.read_excel('Test.xlsx')

folder_name = 'Files'
# below function is used to get the absolute path to a folder (defines the path)
folder_path = os.path.abspath(folder_name)
# files_in_folder is the list of files in the folder to be renamed
files_in_folder = os.listdir(folder_name)

selected_df = excel_df[['First name', 'Last name', 'UNumber']] #python is case sensative 

# creating a new folder name (for a new folder)
new_folder_name = 'Redo Names'

# creates the folder with the defined name in 'new_folder_name'
#os.makedirs(new_folder_name)

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

# shuffle the excel dataframe:
selected_df2 = selected_df.sample(frac=1)

# Perform a left merge to keep all rows from df2 while matching "First name" and "Last name" columns
merged_df2 = cleaned_names_df.merge(selected_df2, on=['First name', 'Last name'], how='left')

# Reorder the columns to have "First name", "Last name", "UNumber", and "File Names" at the front
merged_df2 = merged_df2[['First name', 'Last name', 'UNumber', 'File Name']]

merged_df2 = merged_df2.astype(str)

print(merged_df2)
# Output the final merged dataframe with "UNumber" added to df2
#print(merged_df2)

for i in range(len(files_in_folder)):

    if merged_df2['UNumber'][i] != 'nan':
        old_file_name = merged_df2.loc[i, 'File Name']
        new_file_name = merged_df2['Last name'][i] + ", " + merged_df2['First name'][i] + " " + merged_df2['UNumber'][i]

        old_file_path = os.path.join('Files', old_file_name)
        new_file_path = os.path.join(os.path.dirname(old_file_path), new_file_name)

        if os.path.exists(old_file_path) and os.path.isfile(old_file_path):
            os.rename(old_file_path, new_file_path)
            print("File renamed successfully.")
        else:
            print("Original file not found or not accessible.")    
    else: 
        source_path = os.path.join(folder_name, merged_df2.loc[i, 'File Name'])
        target_path = os.path.join(new_folder_name, merged_df2.loc[i, 'File Name'])
        os.replace(source_path, target_path)
