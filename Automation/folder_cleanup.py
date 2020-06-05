import os
import tkinter

'''
For future implementations of this project, I'll add
a GUI for navigating and choosing folders that a user may want
to clean. 

What this file does:

    - Allows a user to enter a file directory and remove 
        a list of file types.
    - File types can be specified. Maybe you're writing a program
        that creates log files, so you can specify for those to be removed.
'''

# Here is where you want the program to clean
directory_path = "C:\\Users\\light\\Downloads"

# Here is where you choose what you want removed
ext_list = [".ppk"]

os.chdir(directory_path)
items = os.listdir()
for item in items:
    for extention in ext_list:
        if extention in item:
            os.remove(item)