# renaming files 
# import libraries
import pandas as pd
import os

# create dataframe from excel sheet
excel_df = pd.read_excel('Test.xlsx')
print(excel_df)

folder_name = 'Files'

folder_path = os.path.abspath(folder_name)
files_in_folder = os.listdir(folder_name)

print('\n' .join(files_in_folder)) # prints files vertically, not necessary tho
# prints the names of the files
# for file_name in files_in_folder: 
    # print(file_name)

