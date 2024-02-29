# Lab 14: File Handleing 

## Overview

This project aims to enhance your understanding of file handling in Python, including reading from and writing to files, handling JSON data, and implementing error handling techniques. You will work with three different files to complete the tasks outlined below.

## Tasks

### Task 1: Setup File Paths

Your first task is to locate the file paths for three files provided for this project. Save these file paths as string variables in your Python script. If you are using a Windows machine, remember to prefix the file path with `r` to avoid escape character issues. For example:

```plaintext
file_path = r'C:\path\to\your\file.txt'
```

- `file_path1` for `file1.txt`
- `file_path2` for `file2.txt`
- `badfile.pdf` for a deliberately incorrect file to simulate an error

### Task 2: Read Text Content

Open `file1.txt` and read its content into a string. Return this string so it can be printed or used later in the program.

### Task 3: Parse JSON from File

For the second file, `file2.txt`, you'll need to read the file and then parse its content as JSON to convert it into a Python dictionary. Once you have the dictionary, retrieve and return the value associated with the key `'Password'`.

### Task 4: Error Handling with File Operations

Attempt to open a non-existent file (or one that is expected to cause an error upon reading, such as `badfile.pdf`). Use a try-except block to handle the error appropriately. If an error occurs, your function should return the message `'Error: Can't Read file'`.


## Submission Guidelines

- Ensure your script includes the necessary imports and correct function definitions as described in each task.


