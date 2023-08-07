# File-automation

This code was intended to help with automizing my tasks with naming student files 

My tasks are to rename a student file based on an excel sheet containing the students full name (first and last) and associated unumber. 
This code will take the original file names of the files that need to be renamed, 'clean' the information that is captured from the file name since they are user input names, and compare with the excel file information. The excel file containing the information needed to rename the file is reorganized into a dataframe and compared with the extracted file name data. Then once a comparison of the first and last name are made, it can be decided that the file can be renamed with the specific student information.

If there is not a match or the file is named incorrectly, it is then stored in a created folder for a user input to rename the files. 

Within this repository are test files used to ensure the code works prior to using with real student IDs
