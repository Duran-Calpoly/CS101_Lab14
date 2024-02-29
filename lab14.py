"""Task1: Go find the relative file paths for the 3 files I provided you. 
And save them as strings. If your on windows put an r'before_the_filepath'
Should look something like: 'file.txt'"""


file_path1 = ''
file_path2 = ''
bad_file = ''

"""Task2: Open the file1.txt and read the content to a string and return it"""
def read_file_content():


    pass

# Usage example (ensure the correct file_path1 is set before running this):
file_content1 = read_file_content()
print(file_content1)



"""Task3: Open file2.txt read the file, use json.load(content), to convert it to a dictionary. Then return the dict['Password'] value"""

import json

def get_password_from_json():
    pass

# Usage example (ensure the correct file_path2 is set before running this):
password = get_password_from_json()
print(password)




"""Task4: use a try block to try to open bad_file.txt. write an exception block to handle the failure. 
Be sure to use the approriate exception. 
Then return 'Error: Can't Read file' from the exception block"""

def try_open_bad_file():
    pass
## Usage example (ensure the correct bad_file path is set before running this):
error_message = try_open_bad_file()
print(error_message)



