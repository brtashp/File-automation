# renaming files 
# import libraries
import pandas as pd
import os

# create dataframe from excel sheet
excel_df = pd.read_excel('Test.xlsx')

# cleaning excel data (especially the U numbers)
def add_U_if_missing(value):
    if isinstance(value, (str, int)):
        str_value = str(value)
        if not str_value.startswith('U'):
            return 'U' + str_value
    return value

def remove_dashes(value):
    if isinstance(value, (str, int)):
        return value.replace('-', '')
    return value

# Apply the functions to the DataFrame column
excel_df['UNumber'] = excel_df['UNumber'].apply(add_U_if_missing)
excel_df['UNumber'] = excel_df['UNumber'].apply(remove_dashes)

# Print the modified DataFrame
#print(excel_df)

folder_name = 'Files'
# below function is used to get the absolute path to a folder (defines the path)
folder_path = os.path.abspath(folder_name)
# files_in_folder is the list of files in the folder to be renamed
files_in_folder = os.listdir(folder_name)

selected_df = excel_df[['First name', 'Last name', 'UNumber']] #python is case sensative 

# creating a new folder name (for a new folder)
new_folder_name = 'Redo Names'

# creates the folder with the defined name in 'new_folder_name'

cleaned_file_names = []

for file_name in files_in_folder:
    parts = file_name.split(' - ')

    if len(parts) == 2:
        names_text = parts[1].strip()
        names = names_text.split()

        if len(names) >= 1:
            # Extract the last name, which might contain the file type
            last_name = names[-1]

            # Check and split the last name from the last dot
            if "." in last_name:
                last_name, file_type = last_name.rsplit(".", 1)
            else:
                file_type = None

            # The remaining names are first names
            first_names = names[:-1]

            entry = {"First name": ' '.join(first_names), "Last name": last_name, "File type": file_type}
            cleaned_file_names.append(entry)

#print(cleaned_file_names)

cleaned_names_df = pd.DataFrame(cleaned_file_names)

#print(cleaned_names_df)

# adds original file name to compare (will be useful later when 
# comparing to make sure correct file was renamed)
cleaned_names_df['File Name'] = files_in_folder

# shuffle the excel dataframe:
selected_df2 = selected_df.sample(frac=1)

# Perform a left merge to keep all rows from df2 while matching "First name" and "Last name" columns
merged_df2 = cleaned_names_df.merge(selected_df2, on=['First name', 'Last name'], how='left')

# Reorder the columns to have "First name", "Last name", "UNumber", and "File Type" at the front
merged_df2 = merged_df2[['First name', 'Last name', 'UNumber', 'File type', 'File Name']]

merged_df2 = merged_df2.astype(str)
merged_df2['File type'] = merged_df2['File type'].astype(str)

print(merged_df2)
print(merged_df2.dtypes)

#print(merged_df2)
# Output the final merged dataframe with "UNumber" added to df2
#print(merged_df2)

for i in range(len(files_in_folder)):

    if merged_df2['UNumber'][i] != 'nan':
        old_file_name = merged_df2.loc[i, 'File Name']
        new_file_name = merged_df2['Last name'][i] + ", " + merged_df2['First name'][i] + " " + merged_df2['UNumber'][i] + "." + merged_df2['File type'][i]

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