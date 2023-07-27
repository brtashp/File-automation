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