# renaming files 
# import libraries
import pandas as pd
import os

# create dataframe from excel sheet
excel_df = pd.read_excel('Test.xlsx')
#print(excel_df)

# creates new folder, needed to be before calling the path to the Files folder or 
# else it would store the newly created file in the files folder 
#renamed_files = 'Renamed Files'
#os.makedirs(renamed_files)

folder_name = 'Files'
# below function is used to get the absolute path to a folder (defines the path)
folder_path = os.path.abspath(folder_name)
# files_in_folder is the list of files in the folder 
files_in_folder = os.listdir(folder_name)

print('\n' .join(files_in_folder)) # prints files vertically, not necessary tho
# prints the names of the files
# for file_name in files_in_folder: 
    # print(file_name)

# only puts the three columns we need into selected df
# need to make a function for later code (unknown spread sheets ect) 
# defines the new dataframe 
selected_df = excel_df[['First name', 'Last name', 'UNumber']] #python is case sensative 
#print(selected_df)

# renaming process 
old_file_name = files_in_folder[0]
print(f"old file name is: {old_file_name}")
new_file_name = 'Whiskers, Cat UNumber.pdf'
#print(f"new file name is{new_file_name}")

# below function concatenates the file name to the file path, might be where we are having issues
old_file_path = os.path.join('Files', old_file_name)
#print( f"old file path is {old_file_path}")
new_file_path = os.path.join('Renamed Files', new_file_name)
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

print(files_in_folder)